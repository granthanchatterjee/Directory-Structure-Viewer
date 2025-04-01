import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip

def get_structure(folder_path, prefix=""):
    try:
        items = sorted(os.listdir(folder_path))
        structure = ""
        for index, item in enumerate(items):
            item_path = os.path.join(folder_path, item)
            is_last = (index == len(items) - 1)
            connector = "└─ " if is_last else "├─ "
            structure += prefix + connector + item + "\n"
            if os.path.isdir(item_path):
                new_prefix = prefix + ("   " if is_last else "│  ")
                structure += get_structure(item_path, new_prefix)
        return structure
    except Exception as e:
        return f"Error: {e}"

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_name = os.path.basename(folder_path)
        structure = folder_name + "\n" + get_structure(folder_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, structure)
    else:
        messagebox.showwarning("Warning", "No folder selected!")

def copy_to_clipboard():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Success", "Folder structure copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No folder structure to copy!")

root = tk.Tk()
root.title("Folder Structure Viewer")
root.geometry("600x500")
root.resizable(False, False)

browse_button = tk.Button(root, text="Select Folder", command=browse_folder, font=("Arial", 12))
browse_button.pack(pady=10)

text_box = tk.Text(root, wrap="word", font=("Courier", 10), height=20, width=70)
text_box.pack(padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack(pady=10)

root.mainloop()