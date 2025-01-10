from flask import Flask, jsonify, request, render_template
from dataStructures import LinkedList, Queue

app = Flask(__name__)

task_list = LinkedList()
priority_queue = Queue()

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
    if task:
        task_list.add_task(task)
        priority_queue.enqueue(task)  # Add to queue for prioritization
        return jsonify({"message": "Task added!"}), 201
    return jsonify({"error": "Task is required!"}), 400

@app.route('/tasks/<task>', methods=['DELETE'])
def delete_task(task):
    task_list.remove_task(task)
    return jsonify({"message": "Task removed!"})

@app.route('/prioritize', methods=['POST'])
def prioritize_task():
    if not priority_queue.is_empty():
        highest_priority_task = priority_queue.dequeue()
        return jsonify({"prioritized_task": highest_priority_task})
    return jsonify({"message": "No tasks to prioritize!"}), 404

if __name__ == '__main__':
    app.run(debug=True)