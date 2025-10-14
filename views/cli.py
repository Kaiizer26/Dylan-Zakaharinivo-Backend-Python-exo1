"affichage du cli"
class View:
    def show_menu(self):
        print("\n=== TODO LIST ===")
        print("1. Ajouter une tache")
        print("2. Afficher les taches")
        print("3. Supprimer")
        print("4. Quitter")
        print("================")
    
    def get_input(self, prompt):
        return input(f"{prompt}: ").strip()
    
    def show_tasks(self, tasks):
        if not tasks:
            print("Aucune tache")
            return
        
        for task in tasks:
            print(task)
    
    def show_message(self, message):
        print(f"{message}")