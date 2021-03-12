import os

from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    name = os.getenv('NAME', "")
    return f'Hello {name}, thats GitHub Actions World!'


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    application.run(threaded=True, port=5000)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    application.run(threaded=True, port=5000)
