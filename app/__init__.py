from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# all variables based on this application has to be instantiated after the app instance is created
bootstrap = Bootstrap(app)


# flask app instance uses from object method to load in all configuartion variables
app.config.from_object(Config)

# set up database variables

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes
# the way to run flask on a separate port
