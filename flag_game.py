import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

class FlagGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Flag Game")

        # Load flag images
        self.flag_images = self.load_flag_images("flags")
        self.flag_names = list(self.flag_images.keys())
        random.shuffle(self.flag_names)

        # GUI elements
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.label = tk.Label(root, text="Which country's flag is this?")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_flag)
        self.next_button.pack()

        self.score = 0
        self.current_flag_index = 0
        self.show_flag()

    def load_flag_images(self, folder):
        flag_images = {}
        for filename in os.listdir(folder):
            if filename.endswith(".png"):
                country_name = filename.split(".")[0]
                image = Image.open(os.path.join(folder, filename))
                image = image.resize((400, 300), Image.ANTIALIAS)
                flag_images[country_name] = ImageTk.PhotoImage(image)
        return flag_images

    def show_flag(self):
        country_name = self.flag_names[self.current_flag_index]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.flag_images[country_name])
        self.current_country = country_name

    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        if user_answer == self.current_country.lower():
            messagebox.showinfo("Correct", "Correct! Well done!")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", f"Incorrect! The correct answer was {self.current_country}.")
        self.entry.delete(0, tk.END)

    def next_flag(self):
        self.current_flag_index = (self.current_flag_index + 1) % len(self.flag_names)
        self.show_flag()

if __name__ == "__main__":
    root = tk.Tk()
    game = FlagGame(root)
    root.mainloop()
