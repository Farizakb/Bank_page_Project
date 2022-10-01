from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField,EmailField
from wtforms.validators import DataRequired, Email, Length
from models import Kartlar, Filallar



class MusterilerForm(FlaskForm):
    ad = StringField(label= "Adınız", validators=[DataRequired(),Length(min=3,max=30)])
    soyad = StringField(label= "Soyadınız", validators=[DataRequired(),Length(min=5,max=40)])
    ata_adi = StringField(label= "Atanızın adı", validators=[DataRequired(),Length(min=3,max=30)])
    mobile = StringField(label= "Mobil nömrə", validators=[DataRequired(),Length(min=3,max=30)])
    mail = EmailField(label = "E-mail", validators=[Email(), Length(min=4,max=30)])
    dogum_tarix = DateField(label= "Doğum tarixi")
    unvan = StringField(label="Qeydiyyat ünvanı")
    kartin_nov = SelectField(label="Kartın növünü seçin: ", choices=[(kart.id, kart.title) for kart in Kartlar.query.all()],validators=[DataRequired()])
    valyuta = SelectField(label="Kartın valyutasını seçin: ", choices=["AZN","EUR","USD"],validators=[DataRequired()])


class UzadilmaForm(FlaskForm):
    reqemler =  StringField(label= "Kartınızın son 8 rəqəmi", validators=[DataRequired(),Length(min=8,max=8)])
    vesiqe = StringField(label= "Şəxsiyyəti təsdiq edən sənət", validators=[DataRequired(),Length(min=3,max=30)])
    mobile = StringField(label= "Mobil nömrə", validators=[DataRequired(),Length(min=3,max=30)])
    uzadilma_nov = SelectField(label="Sifarişin növü", choices=["1 Gün","3 Gün"])
    filal = SelectField(label="Kartın görürüləcəyi filal", choices=[(filal.id, filal.filal) for filal in Filallar.query.all()])

