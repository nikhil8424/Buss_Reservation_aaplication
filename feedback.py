import tkinter as tk
from tkinter import messagebox
import winsound

def submit_feedback():
    try:
        play_sound()
        display_feedback()
        save_feedback()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def play_sound():
    try:
        winsound.PlaySound("button_click.wav", winsound.SND_FILENAME)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while playing sound: {e}")

def display_feedback():
    try:
        feedback_text = [
            feedback1.get("1.0", "end-1c"),
            feedback2.get("1.0", "end-1c"),
            feedback3.get("1.0", "end-1c"),
            feedback4.get("1.0", "end-1c")
        ]
        satisfaction_scale = overall_satisfaction.get()
        stars = "⭐" * int(satisfaction_scale)

        feedback_msg = f"Feedback Summary:\n\n" \
                       f"1. Did the app perform well without any glitches or crashes? {feedback_text[0]}\n\n" \
                       f"2. Additional features you would like to see added: {feedback_text[1]}\n\n" \
                       f"3. Share about your experience with the app: {feedback_text[2]}\n\n" \
                       f"4. Did the app have all the features you expected? {feedback_text[3]}"

        feedback_msg += f"\n\nSatisfaction Scale: {stars}"
        messagebox.showinfo("Feedback Summary", feedback_msg)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while displaying feedback: {e}")

def save_feedback():
    try:
        with open("feedback.txt", "a") as file:
            file.write("Username: " + e1.get() + "\n")
            file.write("Email id: " + e2.get() + "\n")
            file.write("Feedback:\n")
            file.write("1. Did the app perform well without any glitches or crashes? " + feedback1.get("1.0", "end-1c") + "\n")
            file.write("2. Additional features you would like to see added: " + feedback2.get("1.0", "end-1c") + "\n")
            file.write("3. Share about your experience with the app: " + feedback3.get("1.0", "end-1c") + "\n")
            file.write("4. Did the app have all the features you expected? " + feedback4.get("1.0", "end-1c") + "\n")
            file.write("Overall Satisfaction: " + str(overall_satisfaction.get()) + " stars\n\n")
        messagebox.showinfo("Feedback Saved", "Feedback has been saved successfully!")
        root.destroy()
        import mainpage
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving feedback to file: {e}")
        import mainpage
root = tk.Tk()
root.geometry("500x500")
root.title("FEEDBACK PAGE")

label_font = ("Comic Sans MS", 12)
bg_color = "yellow"
root.configure(bg="lightblue")

# Labels and Entries for username and email
tk.Label(root, text="Username:", bg=bg_color, fg="black", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='e')
e1 = tk.Entry(root, bg="lightgrey", fg="black")
e1.grid(row=0, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="E-mail id:", bg=bg_color, fg="black", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='e')
e2 = tk.Entry(root, bg="lightgrey", fg="black")
e2.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Feedback Questions with Text widgets
tk.Label(root, text="Did the app perform well without any glitches or crashes?", bg=bg_color, fg="black", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky='e')
feedback1 = tk.Text(root, height=3, width=40, bg="lightgrey", fg="black")
feedback1.grid(row=2, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Additional features you would like to see added:", bg=bg_color, fg="black", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky='e')
feedback2 = tk.Text(root, height=3, width=40, bg="lightgrey", fg="black")
feedback2.grid(row=3, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Share about your experience with the app:", bg=bg_color, fg="black", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky='e')
feedback3 = tk.Text(root, height=3, width=40, bg="lightgrey", fg="black")
feedback3.grid(row=4, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Did the app have all the features you expected?", bg=bg_color, fg="black", font=label_font).grid(row=5, column=0, padx=10, pady=5, sticky='e')
feedback4 = tk.Text(root, height=3, width=40, bg="lightgrey", fg="black")
feedback4.grid(row=5, column=1, padx=10, pady=5, sticky='w')

# Scale for overall satisfaction
tk.Label(root, text="Overall Satisfaction:", bg=bg_color, fg="black", font=label_font).grid(row=6, column=0, padx=10, pady=5, sticky='e')
overall_satisfaction = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL)
overall_satisfaction.grid(row=6, column=1, padx=10, pady=5, sticky='w')

# Submit Button
submit_button = tk.Button(root, text="Submit", bg="green", fg="white", command=submit_feedback)
submit_button.grid(row=7, columnspan=2, padx=10, pady=10, sticky='nsew')

# Center the window
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x_coordinate = (root.winfo_screenwidth() - width) // 2
y_coordinate = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
