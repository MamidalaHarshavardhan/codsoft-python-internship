import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'X' if self.completed else ' '}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

class ToDoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list
        self.title("To-Do List")
        self.geometry("300x400")

        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_task_entry = tk.Entry(self)
        self.add_task_entry.pack(fill=tk.X)

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(fill=tk.X)

        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(fill=tk.X)

        self.mark_completed_button = tk.Button(self, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(fill=tk.X)

        self.update_task_list()

    def add_task(self):
        description = self.add_task_entry.get()
        if description:
            self.todo_list.add_task(description)
            self.add_task_entry.delete(0, tk.END)
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.delete_task(selected_task_index[0])
            self.update_task_list()

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.mark_task_completed(selected_task_index[0])
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    todo_list = ToDoList()
    app = ToDoApp(todo_list)
    app.mainloop()
