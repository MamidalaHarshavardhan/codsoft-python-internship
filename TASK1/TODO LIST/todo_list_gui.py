import tkinter as tk
from tkinter import messagebox, filedialog
import json

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

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid input")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks = [{'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(task['description']) for task in tasks]
                for task, data in zip(self.tasks, tasks):
                    if data['completed']:
                        task.mark_completed()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = ToDoList()
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the listbox and scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(
            frame,
            width=50,
            height=10,
            bd=0,
            selectbackground="#a6a6a6",
            activestyle="none"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Create an entry box to add new tasks
        self.task_entry = tk.Entry(
            self.root,
            font=("Arial", 12)
        )
        self.task_entry.pack(pady=10)

        # Create buttons to add, delete, and mark tasks as complete
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        add_task_button = tk.Button(
            button_frame,
            text="Add Task",
            command=self.add_task
        )
        add_task_button.pack(side=tk.LEFT, padx=10)

        delete_task_button = tk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task
        )
        delete_task_button.pack(side=tk.LEFT, padx=10)

        complete_task_button = tk.Button(
            button_frame,
            text="Complete Task",
            command=self.complete_task
        )
        complete_task_button.pack(side=tk.LEFT, padx=10)

        save_task_button = tk.Button(
            button_frame,
            text="Save Tasks",
            command=self.save_tasks
        )
        save_task_button.pack(side=tk.LEFT, padx=10)

        load_task_button = tk.Button(
            button_frame,
            text="Load Tasks",
            command=self.load_tasks
        )
        load_task_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.todo_list.add_task(task_description)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task description.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.delete_task(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.mark_task_completed(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def save_tasks(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.todo_list.save_to_file(filename)

    def load_tasks(self):
        filename = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.todo_list.load_from_file(filename)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
