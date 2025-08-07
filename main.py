
from flask import Flask
from app.routes.driver import driver_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

app.register_blueprint(driver_bp, url_prefix='/api/driver')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
