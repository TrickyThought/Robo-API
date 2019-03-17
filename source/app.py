#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for

import time
import Robot

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

app = Flask(__name__)

# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
#robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

@app.route('/robo/api/v1.0/moveforward', methods=['PUT'])
def move_forward():
    speed = get_speed(request)
    duration = get_duration(request)
    print("MoveForward speed: " + str(speed) + " duration:" + str(duration))
    return jsonify({'MoveForward': speed})

@app.route('/robo/api/v1.0/movebackward', methods=['PUT'])
def move_backward():
    speed = get_speed(request)
    duration = get_duration(request)
    print("MoveBackward speed: " + str(speed) + " duration:" + str(duration))
    return jsonify({'MoveBackward': speed})

@app.route('/robo/api/v1.0/moveleft', methods=['PUT'])
def move_left():
    speed = get_speed(request)
    duration = get_duration(request)
    print("MoveLeft speed: " + str(speed) + " duration:" + str(duration))
    return jsonify({'MoveLeft': speed})

@app.route('/robo/api/v1.0/moveright', methods=['PUT'])
def move_right():
    speed = get_speed(request)
    duration = get_duration(request)
    print("MoveRight speed: " + str(speed) + " duration:" + str(duration))
    return jsonify({'MoveRight': speed})

@app.route('/robo/api/v1.0/stop', methods=['PUT'])
def stop():
    print("Stop")
    return jsonify({'Stop': true})

def get_speed(request):
    if not request.json:
        abort(400)
    if not ('speed' in request.json) or (type(request.json['speed']) != float and type(request.json['speed']) != int):
        abort(400)
    
    return request.json['speed']

def get_duration(request):
    if not request.json:
        abort(400)
    if not ('duration' in request.json) or (type(request.json['duration']) != float and type(request.json['duration']) != int):
        return None
    
    return request.json['duration']

'''
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
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
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')