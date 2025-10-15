## TODO List CLI

Une petite appli de gestion de tâches en ligne de commande, simple et rapide à lancer.
C’est un petit projet en architecture MVC (Model - View - Controller).

## Structure

```
├── controllers
│   └── task_controller.py
├── model
│   └── task.py
├── views
│   └── cli.py
├── main.py
```

## ⚙️ Installation

Aucune dépendance externe.

## 🚀 Lancer l’application

python main.py

## ✨ Fonctionnalités

➕ Ajouter une tâche

📋 Afficher toutes les tâches

🗑️ Supprimer une tâche

## 🧩 Architecture MVC

Model → Gère les données (Task, TaskManager)

View → Affiche les menus et les messages

Controller → Gère les actions utilisateur

Main → Démarre l’application

## Création d'un environnement virtuel

Pour créer un environnement virtuel, faites ces lignes de commandes : 
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```