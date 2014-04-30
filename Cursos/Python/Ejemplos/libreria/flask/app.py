#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from flask import request, url_for

from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'rock': #Esto esta hardcodeado, JAMAS hacer cosas parecidas de verdad xD
        return 'curso'
    return None

tasks = [
            {
            'id' : 1,
            'title' : 'REST API para todos!',
            'description' : 'Preparando los tests para todos :)',
            'done' : False
            },
            {
            'id' : 2,
            'title' : 'Espero que os este gustando',
            'description' : 'Flask esta muy chulo, al igual que la piton!',
            'done' : False
            }
        ]

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
#@auth.login_required   #Use it if want authentication
def get_tasks():
    #return jsonify( {'tasks' : tasks})   # Original, sin uri
    return jsonify( {'tasks' : list(map(make_public_task, tasks))})


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = list(filter(lambda x: x['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify( {'task' : task[0]})


@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
            'id' : tasks[-1]['id'] + 1,
            'title' : request.json['title'],
            'description' : request.json.get('description', ''),
            'done' : False
            }
    tasks.append(task)
    return jsonify( {'task' : task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = list(filter(lambda x: x['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify( {'task' : task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = list(filter(lambda x: x['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify( {'result' : True})


@app.route('/')
def index():
    return "Hello world"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( {'error' : 'Not found' } ), 404)

@auth.error_handler
def unaithorized():
    #return make_response(jsonify({'error':'Unauthorized access'}), 401) #Si usamos error 401 el navegador mostrara una caja de login
    return make_response(jsonify({'error':'Unauthorized access'}), 403)

if __name__ == "__main__":
    app.run(debug = True)
