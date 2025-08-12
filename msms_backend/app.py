from flask import Flask
from flask_cors import CORS
from routes.sales import sales_bp

app = Flask(__name__)
CORS(app)

# Register sales blueprint
app.register_blueprint(sales_bp, url_prefix="/api/sales")

if __name__ == "__main__":
    app.run(debug=True)
