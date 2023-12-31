import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task(description, due_date, priority):
    task = {'description': description, 'due_date': due_date, 'priority': priority, 'completed': False}
    tasks.append(task)

def display_tasks(task_list):
    return "\n\n".join([f"Description: {task['description']}\nDue Date: {task['due_date']}\nPriority: {task['priority']}\nStatus: {'Completed' if task['completed'] else 'Not Completed'}" for task in task_list])

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        task['completed'] = True
        completed_tasks.append(task)

def update_task(task_index, description, due_date, priority):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        task.update({'description': description, 'due_date': due_date, 'priority': priority})

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks.pop(task_index - 1)

def todo_app():
    def add_task_command():
        description = add_description.get()
        due_date = add_due_date.get()
        priority = add_priority.get()

        if description:
            add_task(description, due_date, priority)
            update_task_list()
            clear_input_fields()
        else:
            messagebox.showerror("Error", "Description cannot be empty")

    def complete_task_command():
        task_index = int(complete_task_index.get())
        complete_task(task_index)
        update_task_list()

    def update_task_command():
        task_index = int(update_task_index.get())
        description = update_description.get()
        due_date = update_due_date.get()
        priority = update_priority.get()
        update_task(task_index, description, due_date, priority)
        update_task_list()

    def remove_task_command():
        task_index = int(remove_task_index.get())
        remove_task(task_index)
        update_task_list()

    def update_task_list():
        task_list_text.config(state=tk.NORMAL)
        task_list_text.delete('1.0', tk.END)
        task_list_text.insert(tk.END, display_tasks(tasks))
        task_list_text.config(state=tk.DISABLED)

    def clear_input_fields():
        add_description.delete(0, tk.END)
        add_due_date.delete(0, tk.END)
        add_priority.delete(0, tk.END)

    root = tk.Tk()
    root.title("To-Do List Application")
    root.configure(bg='#F5F5F5')

    def create_entry_label(parent, label_text, row):
        label = tk.Label(parent, text=label_text, bg='#F5F5F5')  
        label.grid(row=row, column=0)
        entry = tk.Entry(parent, bg='#E0E0E0')
        entry.grid(row=row, column=1)
        return entry

    def create_button(parent, button_text, row, command, bg_color):
        button = tk.Button(parent, text=button_text, command=command, bg=bg_color, fg='white')  
        button.grid(row=row, column=0, columnspan=2)
        return button

    add_description = create_entry_label(root, "Description:", 0)
    add_due_date = create_entry_label(root, "Due Date:", 1)
    add_priority = create_entry_label(root, "Priority:", 2)
    create_button(root, "Add Task", 3, add_task_command, bg_color='Green')  

    complete_task_index = create_entry_label(root, "Task Index:", 4)
    create_button(root, "Mark as Completed", 5, complete_task_command, bg_color='Blue')  

    update_description = create_entry_label(root, "New Description:", 6)
    update_due_date = create_entry_label(root, "New Due Date:", 7)
    update_priority = create_entry_label(root, "New Priority:", 8)
    update_task_index = create_entry_label(root, "Task Index:", 9)
    create_button(root, "Update Task", 10, update_task_command, bg_color='Brown')  

    remove_task_index = create_entry_label(root, "Task Index:", 11)
    create_button(root, "Remove Task", 12, remove_task_command, bg_color='Red')  

    create_button(root, "Quit", 13, root.destroy, bg_color='#999999')

    task_list_label = tk.Label(root, text="Task List:", bg='#F5F5F5')  
    task_list_label.grid(row=14, column=0, columnspan=2)
    task_list_text = tk.Text(root, height=10, width=50, bg='#E0E0E0', fg='black')  
    task_list_text.grid(row=15, column=0, columnspan=2)
    task_list_text.config(state=tk.DISABLED)

    update_task_list()
    root.mainloop()

if __name__ == '__main__':
    todo_app()
