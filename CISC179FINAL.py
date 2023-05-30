import tkinter as tk
from tkinter import filedialog
import os
import unittest

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Analyzer")

        self.file_path = None

        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self.root, text="Select a file:")
        self.file_label.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()

        if self.file_path:
            self.analyze_file()

    def analyze_file(self):
        if self.validate_file():

            pass

    def validate_file(self):
        if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
            return True
        else:

            raise FileNotFoundError("File not found or not readable.")
            return False


class MyTest(unittest.TestCase):
    def test_my_functionality(self):
        
        pass

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
