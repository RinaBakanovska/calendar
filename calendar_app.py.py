import tkinter as tk
import datetime

class DateTimeService:
    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now()

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphic Calendar")

        self.datetime_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.datetime_label.pack(pady=10)

        self.update_button = tk.Button(root, text="Update", command=self.update_datetime)
        self.update_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Close", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def update_datetime(self):
        current_datetime = DateTimeService.get_current_datetime()
        self.datetime_label.config(text=f"Current date and time: {current_datetime}")

    def show_datetime(self):
        self.update_datetime()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    gui.show_datetime()
