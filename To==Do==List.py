#Task 1
import tkinter as tk   #This is import the tkinter 
from tkinter import messagebox

class To_Do_List:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.tasks = []

        self.task_list = tk.Listbox(self.root, width=40, height=10) #This is Create  a GUI components
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="red", fg="white")
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="blue", fg="white")
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="green", fg="white")
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_entry.get()
            if task:
                self.tasks[task_index] = task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.task_entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select a task to update.......Please try again:)")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks.pop(task_index)
            self.task_list.delete(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete.......Please try again:)")

if __name__ == "__main__":
    root = tk.Tk()
    app = To_Do_List(root)
    root.mainloop()