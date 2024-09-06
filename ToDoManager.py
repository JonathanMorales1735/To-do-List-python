import pickle

class ToDoManager:
    def __init__(self, file_path):
        self.filePath = file_path
        self.tasks = self.loadTasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.saveTasks()

    def remove_task(self, taskIndex):
        if 0 <= taskIndex < len(self.tasks):
            del self.tasks[taskIndex]
            self.saveTasks()

    def complete_task(self, taskIndex):
        if 0 <= taskIndex < len(self.tasks):
            self.tasks[taskIndex]["completed"] = True
            self.saveTasks()

    def loadTasks(self):
        try:
            with open(self.filePath, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []
        
    def saveTasks(self):
        with open(self.filePath, 'wb') as file:
            pickle.dump(self.tasks, file)
