import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<asset>')
def send_asset(asset):
    if asset == 'favicon.ico': return ('', 404)

    for filename in os.listdir(f'{os.getcwd()}/assets'):
        if filename.startswith(asset.lower()):
            return send_file(f'assets/{filename}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
