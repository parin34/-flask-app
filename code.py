from flask import Flask, jsonify,request 
app = Flask(__name__)

tasks = [
    {
        'id':1, 
        'name':'Raju' ,
        'contact':9997,
        'done':False
},
  {
        'id':2, 
        'name':'Rahu;' ,
        'contact':1190,
        'done':False
}
]

@ app.route("/")
def hello_world():
    return "Hello World!"

@ app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

@ app.route("/add-data")
def add_task():

    if not request.jason:
        return jsonify({
            "status":'error',
            "message":"Please provide the data"
        }, 400)
    tasks = {
        "id": tasks[-1]['id'] +1,
        'name': request.jason['name'],
        'contact': request['contact'],
        'done':False
    }
    tasks.append(tasks)
    return jsonify({
        "status":'success',
        "message":"task added successfully"
    })

if __name__ == '__main__':
    app.run()