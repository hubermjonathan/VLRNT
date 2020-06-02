from flask import Flask, send_file
app = Flask(__name__)
@app.route('/<image>')
def send_image(image):
	return send_file(f'assets/{image}.png', mimetype='image/gif')
