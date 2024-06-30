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
            print("invalid input")

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
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def main():
    todo_list = ToDoList()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_from_file(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            
