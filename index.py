from flask import Flask
from src.routes.OffshoreRoutes import offshore_bp
from src.routes.OfacRoutes import ofac_bp
from src.routes.UserRoutes import user_bp
from src.utils.Limiter import limiter
from flask_jwt_extended import JWTManager

app = Flask(__name__)
limiter.init_app(app)
app.config["JWT_SECRET_KEY"] = "a54l2q31923eqw32177ew4564fwef4as$#%&T$acft-"
jwt = JWTManager(app)
app.register_blueprint(offshore_bp)
app.register_blueprint(ofac_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run()