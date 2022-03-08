from flask import Flask
from flask import jsonify
import datetime
import requests
import os
from com.util.logger import AppLogger
from com.session.session_data import SessionData
from com.db.app_db import AppDB
from com.service.app_service import AppService

app = Flask(__name__)
os.environ["APP_VERSION"] = "0.0.1"
app_db = None


@app.route('/api/health', methods=['GET'])
def health():
    app_verison = os.environ["APP_VERSION"]
    response_json = {"message": "OK", "version": app_verison}
    return jsonify(success=True, data=response_json)


@app.route('/api/initialize')
def initialize():
    global app_db
    host = os.environ["db.host"]
    port = int(str(os.environ["db.port"]))
    username = os.environ["db.user"]
    password = os.environ["db.pwd"]
    db_name = os.environ["db.database"]

    app_logger = AppLogger()
    app_logger.init_handlers()

    app_db = AppDB()
    app_db.initialize(host, port, username, password, db_name)
    SessionData.getInstance().set_val("app_db", app_db)

    app_service = AppService()
    app_service.start()
    SessionData.getInstance().set_val("app_service", app_service)

    return f'Initialized profit_agents_app at {datetime.datetime.now()}'


def call_initialize():
    print("calling initialize......" + str(datetime.datetime.now()))
    requests.get("http://127.0.0.1:8055/api/initialize")


if __name__ == '__main__':
    os.environ["db.host"] = "127.0.0.1"
    os.environ["db.port"] = "27017"
    os.environ["db.database"] = "db_name"
    os.environ["db.user"] = "dbuser"
    os.environ["db.pwd"] = "password"
    call_initialize()
    app.run(debug=True, host='0.0.0.0', port=8055, use_reloader=False)
