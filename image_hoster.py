import os
from flask import Flask, send_file
app = Flask(__name__)
@app.route('/<image>')
def send_image(image):
	return send_file(f'assets/{image}.png', mimetype='image/gif')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
