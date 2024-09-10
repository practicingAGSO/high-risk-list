from flask import Flask
from src.routes.OffshoreRoutes import offshore_bp
from src.routes.OfacRoutes import ofac_bp
from src.routes.UserRoutes import user_bp
from src.utils.Limiter import limiter
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
limiter.init_app(app)
app.config["JWT_SECRET_KEY"] = "a54l2q31923eqw32177ew4564fwef4as$#%&T$acft-"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
jwt = JWTManager(app)
app.register_blueprint(offshore_bp)
app.register_blueprint(ofac_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run()