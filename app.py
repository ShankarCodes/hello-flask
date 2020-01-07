from flask import Flask,render_template,request
import pymongo 
client = pymongo.MongoClient("mongodb+srv://shankar:whitey123@db-g15hj.mongodb.net/test?retryWrites=true&w=majority")
db = client.data
collect = db['storage']
app = Flask(__name__)

@app.route('/')
def homepage():
    name = request.args.get('name')
    collect.insert_one(dict(request.args))
    if name is None:
        name = "Somebody"
    return render_template('index.html',ctx={'name':name})

if __name__=='__main__':
    app.run()

#git push heroku master