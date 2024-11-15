from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config
import os


# สร้าง instance ของ db และ jwt
db = SQLAlchemy()
jwt = JWTManager()
app = Flask(__name__)
def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    # Initialize db และ jwt
    db.init_app(app)
    jwt.init_app(app)

    # นำเข้าและลงทะเบียน Blueprints
    from routes.api_routes import api_blueprint
    from routes.auth_routes import auth_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.before_request
    def create_tables():
        with app.app_context():
            db.create_all()  

    

    return app
@app.route('/')
def home():
    return ("/templates")


if __name__ == '__main__':
    app = create_app()  # สร้างแอปพลิเคชัน
    app.run(host='0.0.0.0', port=5000)  # เปิดเซิร์ฟเวอร์
