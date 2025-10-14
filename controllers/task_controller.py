""" Logique système"""
class Controller:
    def __init__(self, manager, view):
        self.manager = manager
        self.view = view
    
    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Choix")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_all()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Au revoir!")
                break
            else:
                self.view.show_message("Choix invalide")
    
    def add_task(self):
        title = self.view.get_input("Titre de la tache")
        self.manager.add(title)
        self.view.show_message("Tache ajoutee")
    
    def show_all(self):
        tasks = self.manager.get_all()
        self.view.show_tasks(tasks)
    
    def delete_task(self):
        self.show_all()
        task_id = int(self.view.get_input("ID a supprimer"))
        if self.manager.delete(task_id):
            self.view.show_message("Tache supprimee")
        else:
            self.view.show_message("Tache non trouvee")