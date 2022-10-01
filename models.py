from admin import KartlarView
from extensions import db,admin
from flask_admin.contrib.sqla import ModelView



class Bank_mehsullari(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    mehsul_title = db.Column(db.String(100),  )
    mehsul_name = db.Column (db.String(255))
    mehsul_desc = db.Column (db.Text)


    






    def __init__(self,qiy,ilkin,kredit,buraxilma,cash_back,istifade_mud,yas_hed,valy):
        self.qiymet = qiy
        self.ilkin_medaxil = ilkin
        self.kredit_xetti = kredit
        self.buraxilma_haqqi = buraxilma
        self.cash_back_bonus = cash_back
        self.istifade_muddeti = istifade_mud
        self.yas_heddi = yas_hed
        self.valyuta = valy




    def save(self):
        db.session.add(self)
        db.session.commit()






class Kartlar(db.Model):
    __tablename__ = 'kartlar'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    image_url = db.Column (db.String(255))
    desc = db.Column (db.String(255),)
    text = db.Column (db.Text )
    classes = db.Column(db.Text)
    xususiyyetler = db.Column(db.Text)
    sifarish_et = db.Column (db.Boolean, nullable = False, default = True)
    etrafli = db.Column (db.Boolean, nullable=False , default = True)
    ms_4 = db.Column (db.Text)

    


    def __repr__(self):
        return self.title




    def __init__(self,title,img,desc,text,sifarish,etrafli,xus):
        self.title = title
        self.image_url = img
        self.desc = desc
        self.text = text
        self.sifarish_et = sifarish
        self.etrafli = etrafli
        self.xusuiyyetler = xus




    def save(self):
        db.session.add(self)
        db.session.commit()





class Kampaniyalar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column (db.String(255))
    text = db.Column (db.Text, )
    desc = db.Column (db.Text)
    vaxt_aralig = db.Column (db.Text, nullable = True,)
    create_at = db.Column (db.Date, nullable=True)
    

    

    def __repr__(self):
        return self.title




    def __init__(self,title,img,text,vaxt_a,cr_at):
        self.title = title
        self.image_url = img
        self.text = text
        self.vaxt_aralig = vaxt_a
        self.create_at = cr_at




    def save(self):
        db.session.add(self)
        db.session.commit() 



class Xeberler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column (db.String(255))
    desc = db.Column(db.Text)
    text = db.Column (db.Text, )
    create_at = db.Column (db.Date, nullable=True)
    

    

    def __repr__(self):
        return self.title




    def __init__(self,title,img,text,cr_at):
        self.title = title
        self.image_url = img
        self.text = text
        self.create_at = cr_at




    def save(self):
        db.session.add(self)
        db.session.commit() 




class Musteriler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(30),  nullable=False)
    soyad = db.Column (db.String(30),nullable=False)
    ata_adi = db.Column (db.String(30),nullable=False)
    mobile = db.Column (db.String(30),nullable=False )
    mail = db.Column (db.String(50))
    dogum_tarix = db.Column (db.Date,)
    unvan = db.Column(db.String(50),)
    valyuta = db.Column(db.String(30),  nullable=False)
    kart_id = db.Column(db.Integer, db.ForeignKey('kartlar.id'))
    kart = db.relationship("Kartlar")




    def __repr__(self):
        return self.ad




    def __init__(self,ad,soyad ,ata_adi,mob,mail,dogum,unvan,nov,valy):
        self.ad = ad
        self.soyad = soyad
        self.ata_adi = ata_adi
        self.mobile = mob
        self.mail = mail
        self.dogum_tarix = dogum
        self.unvan = unvan
        self.kart_id = nov
        self.valyuta = valy




    def save(self):
        db.session.add(self)
        db.session.commit()




class Uzadilma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reqemler = db.Column(db.Integer,  nullable=False)
    vesiqe = db.Column (db.String(30),nullable=False)
    mobile = db.Column (db.String(30),nullable=False )
    uzadilma_nov = db.Column(db.String(30),nullable=False)
    filal_id = db.Column(db.Integer, db.ForeignKey('filallar.id'))
    filal = db.relationship("Filallar")


    def __repr__(self):
        self.vesiqe



    def __init__(self,reqemler,vesiqe,mob,uzadilma_nov,filal_id):
        self.reqemler = reqemler
        self.vesiqe = vesiqe
        self.mobile = mob
        self.uzadilma_nov = uzadilma_nov
        self.filal_id = filal_id




    def save(self):
        db.session.add(self)
        db.session.commit()


class Filallar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filal = db.Column (db.String(30),nullable=False)


    def __repr__(self):
        return self.filal


admin.add_view(KartlarView(Kartlar, db.session))
admin.add_view(KartlarView(Filallar, db.session))
admin.add_view(ModelView(Bank_mehsullari, db.session))
admin.add_view(KartlarView(Kampaniyalar, db.session))
admin.add_view(KartlarView(Xeberler, db.session))
admin.add_view(ModelView(Musteriler, db.session))
admin.add_view(ModelView(Uzadilma, db.session))


