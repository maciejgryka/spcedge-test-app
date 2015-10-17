import os

from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = os.getenv('DEBUG', False)


@app.route('/')
def home():
    return 'There is nothing here.'


if __name__ == '__main__':
    app.run()
