# ============================================
# Couche Présentation (Affichage)
# ============================================

import sys
from typing import List, TYPE_CHECKING

# Éviter l'import circulaire
if TYPE_CHECKING:
    from model.task import Task

# Fix encodage Windows pour les emojis
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class TaskView:
    """Gère l'affichage des tâches et la saisie utilisateur"""
    
    @staticmethod
    def display_menu() -> None:
        """Afficher le menu principal"""
        print("\n" + "="*50)
        print("📋 GESTIONNAIRE DE TÂCHES".center(50))
        print("="*50)
        print("1. ➕ Ajouter une tâche")
        print("2. 📄 Afficher toutes les tâches")
        print("3. ✓ Marquer comme terminée")
        print("4. → Marquer en cours")
        print("5. 🗑️  Supprimer une tâche")
        print("6. 🔍 Afficher par statut")
        print("7. 🚪 Quitter")
        print("="*50)
    
    @staticmethod
    def display_tasks(tasks: "List[Task]") -> None:
        """Afficher une liste de tâches"""
        if not tasks:
            print("ℹ️  Aucune tâche trouvée.")
            return
        
        print("\n" + "-"*60)
        for task in tasks:
            print(task)
        print("-"*60)
    
    @staticmethod
    def display_task_detail(task: "Task") -> None:
        """Afficher les détails d'une tâche"""
        print(f"\n📌 Détails de la tâche #{task.id}")
        print(f"   Titre: {task.title}")
        print(f"   Description: {task.description or 'N/A'}")
        print(f"   Priorité: {'Haute' if task.priority == 3 else 'Moyenne' if task.priority == 2 else 'Basse'}")
        print(f"   Statut: {task.status.value}")
        print(f"   Créée: {task.created_at.strftime('%d/%m/%Y %H:%M')}")
        if task.completed_at:
            print(f"   Terminée: {task.completed_at.strftime('%d/%m/%Y %H:%M')}")
    
    @staticmethod
    def get_input(prompt: str) -> str:
        """Obtenir une saisie utilisateur"""
        return input(f"\n{prompt}: ").strip()
    
    @staticmethod
    def show_success(message: str) -> None:
        """Afficher un message de succès"""
        print(f"✅ {message}")
    
    @staticmethod
    def show_error(message: str) -> None:
        """Afficher un message d'erreur"""
        print(f"❌ {message}")