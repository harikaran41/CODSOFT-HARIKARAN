import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List Application")
        master.geometry("500x500") 
        self.tasks = []
        
        self.task_label = tk.Label(master, text="Task:")
        self.task_label.pack(pady=5)

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox_frame = tk.Frame(master)
        self.task_listbox_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_listbox_frame, width=50, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_listbox_frame, orient="vertical")
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.complete_button = tk.Button(master, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)   
        self.delete_button.pack(pady=5)
        
        self.search_label = tk.Label(master, text="Search Task:")
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(master, width=40)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_tasks) # Live search

        self.clear_search_button = tk.Button(master, text="Clear Search", command=self.clear_search)
        self.clear_search_button.pack(pady=5)

        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task_listbox(self, filtered_tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks_to_display = filtered_tasks if filtered_tasks is not None else self.tasks
        for i, item in enumerate(tasks_to_display):
            status = "✓ " if item["completed"] else "  "
            self.task_listbox.insert(tk.END, f"{status}{item['task']}")
            if item["completed"]:
                self.task_listbox.itemconfig(i, {'fg': 'gray', 'bg': 'lightgreen'})
            else:
                self.task_listbox.itemconfig(i, {'fg': 'black', 'bg': 'white'})

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
        
            displayed_task_text = self.task_listbox.get(selected_index).lstrip('✓ ').lstrip('  ')
            original_index = -1
            for i, task_item in enumerate(self.tasks):
                if task_item["task"] == displayed_task_text:
                    original_index = i
                    break

            if original_index != -1:
                self.tasks[original_index]["completed"] = not self.tasks[original_index]["completed"]
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "Task not found in original list. Please clear search if active.")

        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark complete.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            displayed_task_text = self.task_listbox.get(selected_index).lstrip('✓ ').lstrip('  ')
            original_index = -1
            for i, task_item in enumerate(self.tasks):
                if task_item["task"] == displayed_task_text:
                    original_index = i
                    break

            if original_index != -1:
                del self.tasks[original_index]
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "Task not found in original list. Please clear search if active.")

        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def search_tasks(self, event=None):
        query = self.search_entry.get().lower()
        if query:
            filtered_tasks = [task for task in self.tasks if query in task["task"].lower()]
            self.update_task_listbox(filtered_tasks)
        else:
            self.update_task_listbox()

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.update_task_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

       
        
   