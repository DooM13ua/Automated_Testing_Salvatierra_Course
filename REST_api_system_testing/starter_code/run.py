from Automated_Testing.REST_api_system_testing.starter_code.app import app
from Automated_Testing.REST_api_system_testing.starter_code.db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
