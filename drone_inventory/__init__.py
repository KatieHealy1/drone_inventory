from flask import Flask
from .site.routes import site # site is the variable we used in routes.py
from .authentication.routes import auth
from .api.routes import api
from .models import db as root_db, login_manager, ma
from config import Config #pulling in class from config.py
from drone_inventory.helpers import JSONEncoder
from flask_migrate import Migrate

# flask Cors import = cross origin resource sharing - future proofing
# from an externam source
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)
app.json_encoder = JSONEncoder

CORS(app)