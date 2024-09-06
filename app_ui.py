import tkinter as tk
from ToDoManager import ToDoManager

class TodoApp:
    def __init__(self):
        self.manager = ToDoManager('data/Tasks.pkl')
        self.root = tk.Tk()
        self.root.title("To-Do List")
        
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.manager.add_task(task)
            self.entry.delete(0, tk.END)
            self.load_tasks()

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            self.manager.remove_task(selected_task[0])
            self.load_tasks()

    def complete_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            self.manager.complete_task(selected_task[0])
            self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        for todo in self.manager.tasks:  # Cambié self.manager.todos a self.manager.tasks
            status = "✓" if todo["completed"] else "✗"
            self.listbox.insert(tk.END, f"{status} {todo['task']}")

    def run(self):
        self.root.mainloop()
