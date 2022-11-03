from flask import Flask

app = Flask(__name__)

def index():
    return("Hello")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=['GET'])
def index():
    return ('Hello')


# @app.errorhandler(404)
# def not_found(e):
#     return app.send_static_file('index.html')

# @app.route('/api/time')
# def get_current_time():
#     return {'time': time.time()}
