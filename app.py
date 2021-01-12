import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def default_route():
    return 'Hello, World!'

if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    app.run(
        threaded=True,
        host='0.0.0.0',
        port=port
    )
