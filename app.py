from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def homepage():
    name = request.args.get('name')
    if name is None:
        name = "Somebody"
    return render_template('index.html',ctx={'name':name})

if __name__=='__main__':
    app.run()