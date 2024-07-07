class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"{'[x]' if self.completed else '[ ]'} {self.title}: {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print("Task index out of range.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
        else:
            print("Task index out of range.")

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Complete")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            description = input("Task description (optional): ")
            to_do_list.add_task(title, description)
        elif choice == '2':
            task_index = int(input("Task index to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Task index to mark complete: "))
            to_do_list.mark_task_complete(task_index)
        elif choice == '4':
            to_do_list.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
