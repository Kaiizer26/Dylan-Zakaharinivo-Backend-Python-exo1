"le point d'entrée"
from model.task import TaskManager
from views.cli import View
from controllers.task_controller import Controller

if __name__ == "__main__":
    manager = TaskManager()
    view = View()
    controller = Controller(manager, view)
    controller.run()