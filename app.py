from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary storage for tasks
tasks = []


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- GET ALL TASKS ----------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# ---------------- ADD TASK ----------------
@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    task_name = data.get("task")

    # Check if task is empty
    if not task_name:
        return jsonify({
            "message": "Task cannot be empty"
        }), 400

    # Create new task
    new_task = {
        "id": len(tasks) + 1,
        "task": task_name,
        "completed": False
    }

    # Add task to list
    tasks.append(new_task)

    return jsonify(new_task)


# ---------------- COMPLETE / UNCOMPLETE TASK ----------------
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            # Change True to False
            # or False to True
            task["completed"] = not task["completed"]

            return jsonify(task)

    return jsonify({
        "message": "Task not found"
    }), 404


# ---------------- DELETE TASK ----------------
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return jsonify({
                "message": "Task deleted"
            })

    return jsonify({
        "message": "Task not found"
    }), 404


# ---------------- START SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)