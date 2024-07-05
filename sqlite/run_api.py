from flask import Flask
from blueprints.b_users import user_blueprint

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>This is the main route on the api. If you are reading this the api is up and running!</p>"


app.register_blueprint(user_blueprint)
