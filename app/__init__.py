from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


app = Flask(__name__)

# all variables based on this application has to be instantiated after the app instance is created
bootstrap = Bootstrap(app)


# flask app instance uses from object method to load in all configuartion variables
app.config.from_object(Config)


from app import routes
# the way to run flask on a separate port
