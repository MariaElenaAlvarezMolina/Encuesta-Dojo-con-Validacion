from flask import Flask

app = Flask(__name__)

app.secret_key = "Secret.key_123"