# ============================================
# POINT D'ENTRÉE
# ============================================

# Importer les classes depuis les autres modules
from model.task import TaskManager
from views.cli import TaskView
from controllers.task_controller import TaskController


if __name__ == "__main__":
    # Initialiser l'application
    manager = TaskManager("tasks.json")
    view = TaskView()
    controller = TaskController(manager, view)
    
    # Démarrer
    controller.run()