from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	site_name = request.form['site']
	print(site_name)
	if site_name:
		return jsonify({'name' : site_name})
	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)