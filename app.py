from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.before_request
def before_api_request():
    print("Запрос к API")

@app.route('/500')
def error_creator():
    print("error")
    return jsonify(error = "my error"), 500

@app.errorhandler(500)
def not_found(error):
    print("ERROROROOROROROR")
    return jsonify({'error': 'Not found this thing'}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    user_list = ['John', 'Carla', 'Mathew']
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True) # 5000