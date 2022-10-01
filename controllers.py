from telnetlib import PRAGMA_HEARTBEAT
from flask import render_template , request , redirect
import requests
from datetime import datetime
from app import app
from models import *
from forms import MusterilerForm, UzadilmaForm



@app.route("/")
def Esas_sehife():

    r = requests.get(f"https://www.cbar.az/currencies/{datetime.now().strftime('%d.%m.%Y')}.xml")
    x = r.text
    y = x.split("Valute")

    for i in y:
        if "USD" in i:
            u = i.split("Value>")
            USD = u[1].split("</")[0]
        if "EUR" in i:
            e = i.split("Value>")      
            EUR = e[1].split("</")[0]
        if "RUB" in i:
            r = i.split("Value>")      
            RUB = r[1].split("</")[0]
        if "GBP" in i:
            g = i.split("Value>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            GBP = g[1].split("</")[0]

    print(USD,EUR,RUB,GBP)
    

    kartlar = Bank_mehsullari.query.filter_by(mehsul_title = "Plastik Kartlar").all()
    emanetler = Bank_mehsullari.query.filter_by(mehsul_title = "Əmanətlər").all()
    kreditlər = Bank_mehsullari.query.filter_by(mehsul_title = "Kreditlər").all()
    b_kreditler = Bank_mehsullari.query.filter_by(mehsul_title = "Biznes Kreditleri").all()
    return render_template('home.html',kartlar = kartlar, emanetler = emanetler, kreditlər = kreditlər, 
    b_kreditler = b_kreditler,USD = USD,EUR = EUR, RUB = RUB, GBP = GBP)




@app.route("/cards/")
def Cards():
    cards = Kartlar.query.all()
    return render_template('plastik_kartlar.html', datas = cards)




@app.route("/cards/<title>/")
def Cards_Details(title):
    card = Kartlar.query.filter_by(title = title.replace('-',' ')).first()
    
    return render_template('cards_detail.html', data = card)






@app.route("/kampaniyalar/")
def Kampaniyalarr():
    kampaniyalar = Kampaniyalar.query.all()
    return render_template('kampaniyalar.html', datas = kampaniyalar)



@app.route("/kampaniya/<title>/")
def Kampaniya(title):
    kampaniya = Kampaniyalar.query.filter_by(title = title.replace('-',' ')).first()
    return render_template('kampaniya.html', data = kampaniya)





@app.route("/xeberler/")
def Xeberlerr():
    xeberler = Xeberler.query.all()
    return render_template('xeberler.html', datas = xeberler)



@app.route("/xeber/<title>/")
def Xeber(title):
    xeber = Xeberler.query.filter_by(title = title.replace('-',' ')).first()
    return render_template('xeber.html', data = xeber)


@app.route("/cards/sifarish/",methods = ["GET", "POST"])
def Cards_sifatish():
    print("kecdi")
    form = MusterilerForm()
    if request.method == "POST":
        print("kecdi")
        post_data = request.form
        print(post_data)
        form = MusterilerForm(data = post_data)
        if form.validate_on_submit():
            print("kecdi")
            musteri = Musteriler(ad=form.ad.data,soyad=form.soyad.data,ata_adi=form.ata_adi.data,
            mob=form.mobile.data,mail=form.mail.data,dogum=form.dogum_tarix.data,unvan=form.unvan.data,
            nov=form.kartin_nov.data,valy=form.valyuta.data)
            musteri.save()
            form.ad.data = " "
            form.soyad.data = " "
            form.ata_adi.data = " "
            form.mobile.data = " "
            form.mail.data = " "
            form.dogum_tarix.data = " "
            form.unvan.data = " "
            form.kartin_nov.data = " "
            form.valyuta.data = " "
    return render_template('kart_sifarish.html', form = form)



@app.route("/onlayn/uzadilma/",methods = ["GET", "POST"])
def Card_uzadilma():
    form = UzadilmaForm()
    if request.method == "POST":
        print("kecdi")
        post_data = request.data
        form = UzadilmaForm(data = post_data)
        if form.validate_on_submit():
            print("kecdi")
            uzadilma = Uzadilma(reqemler=form.reqemler.data,vesiqe=form.vesiqe.data,mob=form.mobile.data,
            uzadilma_nov=form.uzadilma_nov.data,filal_id=form.filal.data)
            uzadilma.save()
            form.reqemler.data = " "
            form.vesiqe.data = " "
            form.mobile.data = " "
            form.uzadilma_nov.data = " "
            form.filal.data = " "
    return render_template('extension.html',form = form)

