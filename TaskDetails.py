# TaskDetails.py

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def display(self):
        print("Task Details:")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Priority: {self.priority}")

if __name__ == "__main__":
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (e.g., 2024-07-01): ")
    priority = input("Enter priority (e.g., High, Medium, Low): ")

    task = Task(title, description, due_date, priority)
    task.display()