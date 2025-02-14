from flask import Flask, jsonify, request, render_template
from dataStructures import LinkedList, Queue
import heapq

app = Flask(__name__)

task_list = LinkedList()
priority_queue = Queue()

priority_map = {
    'high': 1,
    'medium': 2,
    'low': 3
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_list.get_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    priority = request.json.get('priority')

    if task and priority in priority_map:
        task_list.add_task((task, priority))  
        priority_queue.enqueue((priority_map[priority], task))
        return jsonify({"message": "Task added!"}), 201
    return jsonify({"error": "Task and valid priority required!"}), 400

@app.route('/tasks/<task>', methods=['DELETE'])
def delete_task(task):
    task_list.remove_task(task)
    priority_queue.remove_task(task)
    return jsonify({"message": "Task removed!"})

@app.route('/prioritized-tasks', methods=['GET'])
def get_prioritized_tasks():
    return jsonify(priority_queue.get_tasks())

if __name__ == '__main__':
    app.run(debug=True)
