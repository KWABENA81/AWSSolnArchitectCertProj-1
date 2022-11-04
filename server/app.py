from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        "channel":"The Show",
        "tutorial":"React, Flask and Docker"
    } 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




# @app.errorhandler(404)
# def not_found(e):
#     return app.send_static_file('index.html')

# @app.route('/api/time')
# def get_current_time():
#     return {'time': time.time()}
# def index():
#     return("Hello")