import tkinter as tk
from tkinter import messagebox
import os

class NoteTakingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Note Taking App")
        
        self.notes_file = "notes.txt"

        self.create_widgets()
        self.load_notes()

    def create_widgets(self):
        # Text Entry
        self.note_entry = tk.Text(self.root, height=10, width=40)
        self.note_entry.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Add Note", command=self.add_note)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(button_frame, text="Edit Note", command=self.edit_note)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Note", command=self.delete_note)
        self.delete_button.grid(row=0, column=2, padx=5)

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                notes = file.read()
                self.note_entry.insert(tk.END, notes)

    def save_notes(self, notes):
        with open(self.notes_file, "w") as file:
            file.write(notes)

    def add_note(self):
        note = self.note_entry.get("1.0", tk.END).strip()
        if note:
            self.note_entry.delete("1.0", tk.END)
            self.note_entry.focus()
            with open(self.notes_file, "a") as file:
                file.write(note + "\n")
        else:
            messagebox.showwarning("Empty Note", "Please enter a note.")

    def edit_note(self):
        selected_text = self.note_entry.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            self.note_entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
        else:
            messagebox.showwarning("No Note Selected", "Please select a note to edit.")

    def delete_note(self):
        selected_text = self.note_entry.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected note?")
            if confirmed:
                self.note_entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
        else:
            messagebox.showwarning("No Note Selected", "Please select a note to delete.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = NoteTakingApp()
    app.run()
