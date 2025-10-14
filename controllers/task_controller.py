# ============================================
#  Couche Métier (Logique)
# ============================================

from model.task import TaskManager, TaskStatus
from views.cli import TaskView


class TaskController:
    """Contrôleur - orchestre la logique métier"""
    
    def __init__(self, manager: TaskManager, view: TaskView):
        self.manager = manager
        self.view = view
    
    def run(self) -> None:
        """Boucle principale de l'application"""
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Choisissez une option")
            
            try:
                if choice == "1":
                    self.create_task()
                elif choice == "2":
                    self.list_all_tasks()
                elif choice == "3":
                    self.mark_done()
                elif choice == "4":
                    self.mark_in_progress()
                elif choice == "5":
                    self.delete_task()
                elif choice == "6":
                    self.filter_by_status()
                elif choice == "7":
                    self.view.show_success("À bientôt!")
                    break
                else:
                    self.view.show_error("Option invalide")
            except ValueError as e:
                self.view.show_error(f"Entrée invalide: {e}")
            except Exception as e:
                self.view.show_error(f"Erreur: {str(e)}")
    
    def create_task(self) -> None:
        """Créer une nouvelle tâche"""
        title = self.view.get_input("Titre de la tâche")
        description = self.view.get_input("Description (optionnel)")
        priority_str = self.view.get_input("Priorité (1=basse, 2=moyenne, 3=haute)")
        
        try:
            priority = int(priority_str)
            task = self.manager.add_task(title, description, priority)
            self.view.show_success(f"Tâche créée: {task}")
        except ValueError:
            self.view.show_error("La priorité doit être un nombre entre 1 et 3")
    
    def list_all_tasks(self) -> None:
        """Afficher toutes les tâches"""
        tasks = self.manager.get_all_tasks()
        self.view.display_tasks(tasks)
    
    def mark_done(self) -> None:
        """Marquer une tâche comme terminée"""
        self.list_all_tasks()
        try:
            task_id = int(self.view.get_input("ID de la tâche à marquer terminée"))
            task = self.manager.get_task(task_id)
            
            if task:
                task.mark_done()
                self.manager.save_tasks()
                self.view.show_success(f"Tâche #{task_id} marquée comme terminée")
            else:
                self.view.show_error(f"Tâche #{task_id} non trouvée")
        except ValueError:
            self.view.show_error("Veuillez entrer un ID valide")
    
    def mark_in_progress(self) -> None:
        """Marquer une tâche comme en cours"""
        self.list_all_tasks()
        try:
            task_id = int(self.view.get_input("ID de la tâche à marquer en cours"))
            task = self.manager.get_task(task_id)
            
            if task:
                task.mark_in_progress()
                self.manager.save_tasks()
                self.view.show_success(f"Tâche #{task_id} marquée en cours")
            else:
                self.view.show_error(f"Tâche #{task_id} non trouvée")
        except ValueError:
            self.view.show_error("Veuillez entrer un ID valide")
    
    def delete_task(self) -> None:
        """Supprimer une tâche"""
        self.list_all_tasks()
        try:
            task_id = int(self.view.get_input("ID de la tâche à supprimer"))
            
            if self.manager.delete_task(task_id):
                self.view.show_success(f"Tâche #{task_id} supprimée")
            else:
                self.view.show_error(f"Tâche #{task_id} non trouvée")
        except ValueError:
            self.view.show_error("Veuillez entrer un ID valide")
    
    def filter_by_status(self) -> None:
        """Afficher les tâches filtrées par statut"""
        print("\nStatuts disponibles:")
        for i, status in enumerate(TaskStatus, 1):
            print(f"{i}. {status.value}")
        
        try:
            choice = int(self.view.get_input("Choisissez un statut"))
            status = list(TaskStatus)[choice - 1]
            tasks = self.manager.get_tasks_by_status(status)
            self.view.display_tasks(tasks)
        except (ValueError, IndexError):
            self.view.show_error("Choix invalide")