import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil

# GUI Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("File Organizer Tool")
        self.geometry("500x400")

        # Widgets
        self.label = ctk.CTkLabel(self, text="File Organizer Tool", font=("Arial", 20))
        self.label.pack(pady=20)

        self.select_button = ctk.CTkButton(self, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.organize_button = ctk.CTkButton(self, text="Organize Files", command=self.organize_files, state="disabled")
        self.organize_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.status_label.pack(pady=20)

        self.selected_folder = ""

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.status_label.configure(text=f"Selected Folder: {self.selected_folder}")
            self.organize_button.configure(state="normal")

    def organize_files(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder!")
            return

        try:
            for filename in os.listdir(self.selected_folder):
                file_path = os.path.join(self.selected_folder, filename)
                if os.path.isfile(file_path):
                    file_extension = filename.split(".")[-1].lower()
                    target_folder = os.path.join(self.selected_folder, file_extension.capitalize() + "s")

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, filename))

            self.status_label.configure(text="Files organized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()