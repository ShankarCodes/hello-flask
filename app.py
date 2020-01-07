from flask import Flask,render_template,request,redirect
import pymongo 
client = pymongo.MongoClient("mongodb+srv://shankar:whitey123@db-g15hj.mongodb.net/test?retryWrites=true&w=majority")
db = client.data
collect = db['storage']
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')
    
@app.route('/add')
def insert():
    data = dict(request.args)
    if data:
        collect.insert_one(data)
    return redirect('/data')
@app.route('/data')
def query():
    data = collect.find()
    dt = []
    for cnt in data:
        cnt.pop('_id')
        dt = dt + [cnt]
    return render_template('data.html',ctx = dt)
if __name__=='__main__':
    app.run()

#git push heroku master
"""
{% for key,value in ctx.items() %}
<h4>{{key}}:{{value}}</h4>
{%endfor%}
"""