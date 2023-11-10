import tkinter as tk
import datetime

def show_datetime():
    current_datetime = datetime.datetime.now()
    datetime_label.config(text=f"Current date and time: {current_datetime}")


root = tk.Tk()
root.title("Graphic Calendar")


datetime_label = tk.Label(root, text="", font=("Helvetica", 14))
datetime_label.pack(pady=10)

update_button = tk.Button(root, text="Update", command=show_datetime)
update_button.pack(pady=10)

exit_button = tk.Button(root, text="Close", command=root.quit)
exit_button.pack(pady=10)

show_datetime()

root.mainloop()
