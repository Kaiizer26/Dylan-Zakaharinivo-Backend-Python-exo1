
# ============================================
# Couche Modèle (POO)
# ============================================

from datetime import datetime
from enum import Enum
from typing import List, Optional
import json
import os


class TaskStatus(Enum):
    """Énumération des états possibles d'une tâche"""
    TODO = "À faire"
    IN_PROGRESS = "En cours"
    DONE = "Terminée"


class Task:
    """Classe représentant une tâche unique"""
    
    _id_counter = 1  # Compteur de classe pour les IDs uniques
    
    def __init__(self, title: str, description: str = "", priority: int = 1):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.priority = priority  # 1 (basse) à 3 (haute)
        self.status = TaskStatus.TODO
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def mark_done(self) -> None:
        """Marquer la tâche comme terminée"""
        self.status = TaskStatus.DONE
        self.completed_at = datetime.now()
    
    def mark_in_progress(self) -> None:
        """Marquer la tâche comme en cours"""
        self.status = TaskStatus.IN_PROGRESS
    
    def mark_todo(self) -> None:
        """Marquer la tâche comme à faire"""
        self.status = TaskStatus.TODO
        self.completed_at = None
    
    def __str__(self) -> str:
        priority_symbol = "🔴" if self.priority == 3 else "🟡" if self.priority == 2 else "🟢"
        status_symbol = "✓" if self.status == TaskStatus.DONE else "→" if self.status == TaskStatus.IN_PROGRESS else "○"
        return f"{status_symbol} [{self.id}] {priority_symbol} {self.title} ({self.status.value})"
    
    def to_dict(self) -> dict:
        """Convertir la tâche en dictionnaire pour la sérialisation"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }


class TaskManager:
    """Gestionnaire de tâches - Pattern Singleton possible"""
    
    def __init__(self, filepath: str = "tasks.json"):
        self.tasks: List[Task] = []
        self.filepath = filepath
        self.load_tasks()
    
    def add_task(self, title: str, description: str = "", priority: int = 1) -> Task:
        """Ajouter une nouvelle tâche"""
        if not title.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if priority not in [1, 2, 3]:
            raise ValueError("La priorité doit être entre 1 et 3")
        
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Récupérer une tâche par son ID"""
        return next((t for t in self.tasks if t.id == task_id), None)
    
    def delete_task(self, task_id: int) -> bool:
        """Supprimer une tâche par son ID"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def get_all_tasks(self) -> List[Task]:
        """Récupérer toutes les tâches"""
        return sorted(self.tasks, key=lambda t: (-t.priority, t.created_at))
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Filtrer les tâches par statut"""
        return [t for t in self.get_all_tasks() if t.status == status]
    
    def save_tasks(self) -> None:
        """Sauvegarder les tâches en JSON"""
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Erreur lors de la sauvegarde : {e}")
    
    def load_tasks(self) -> None:
        """Charger les tâches depuis un fichier JSON"""
        if not os.path.exists(self.filepath):
            return
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = []
                for item in data:
                    task = Task(item["title"], item["description"], item["priority"])
                    task.id = item["id"]
                    task.status = TaskStatus[item["status"]]
                    task.created_at = datetime.fromisoformat(item["created_at"])
                    if item["completed_at"]:
                        task.completed_at = datetime.fromisoformat(item["completed_at"])
                    self.tasks.append(task)
                    # Mettre à jour le compteur d'ID
                    Task._id_counter = max(Task._id_counter, task.id + 1)
        except IOError as e:
            print(f"Erreur lors du chargement : {e}")

