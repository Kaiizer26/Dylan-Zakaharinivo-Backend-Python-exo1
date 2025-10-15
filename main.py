from flask import Flask
from controllers.task_controller import task_routes

# création de l'appli flask
app = Flask(__name__)

# enregistrement du blueprint contenant les routes
app.register_blueprint(task_routes)

# point d'entrée 
if __name__ == "__main__":
    app.run(debug=True)
