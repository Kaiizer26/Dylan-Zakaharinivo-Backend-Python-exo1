"""Classes métierss"""
class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
    
    def __str__(self):
        return f"[{self.id}] {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def delete(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    
    def get_all(self):
        return self.tasks
    
    
