from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_project'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Respublika@127.0.0.1:3306/BankResp'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'



from models import *
from extensions import * 
from controllers import * 

if __name__ == "__main__":
    db.init_app(app)
    migrate.init_app(app)
    app.run(debug=True)
