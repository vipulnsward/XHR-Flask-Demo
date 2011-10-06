from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/xhr/<req>')
def xhr(req):
    print "Request Data:"+req
    return "You entered: "+req

@app.route('/home')
def home():
    return render_template('Client.html')

if __name__ == '__main__':
    app.run(debug='true')
