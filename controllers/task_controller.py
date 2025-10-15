from flask import Blueprint, jsonify, request
from model.task import TaskManager

# on crée une instance de TaskManager pour gérer les tâches
task_manager = TaskManager()

# blueprint (sépare les routes du reste du code)
task_routes = Blueprint("task_routes", __name__)

# récupérer toutes les tâches
@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = [t.to_dict() for t in task_manager.get_all()]
    return jsonify(tasks), 200


# ajouter une tâche
@task_routes.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    title = data["title"]
    task = task_manager.add(title)
    return jsonify(task.to_dict()), 201


# supprimer une tâche
@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_manager.delete(task_id):
        return jsonify({"message": "Task deleted"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404
