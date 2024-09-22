from flask import Flask, request
import sqlite3
import os 


app = Flask(__name__)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    # Vulnerable to SQL injection
    todo = request.form['todo']
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO todos (task) VALUES ('{todo}')")  # Unsafe
    conn.commit()
    return "Todo added!"

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.todos = json.load(f)
        else:
            self.todos = []

    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f)

    def add_task(self, task):
        self.todos.append(task)
        self.save_todos()

    def view_tasks(self):
        if not self.todos:
            print("No tasks in your to-do list.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.todos):
                print(f"{index + 1}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.todos):
            removed_task = self.todos.pop(index)
            self.save_todos()
            print(f"Deleted task: '{removed_task}'")
        else:
            print("Invalid task number.")

def main():
    app = TodoApp()


    print("Hello World! (: ")

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            app.add_task(task)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            app.view_tasks()
            try:
                task_num = int(input("Enter the task number to delete: ")) - 1
                app.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    app.run(debug=True)
