import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

def homepage():
    root.destroy()
    import mainpage
    
def window_for_cancellation():
    for widget in root.winfo_children():
        widget.destroy()
    root.state("zoomed")

    background_label = tk.Label(root, bg="#e7cee4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    pass_name_var_cancel = tk.StringVar()
    phone_no_var_cancel = tk.StringVar()
    credit_card_no_var_cancel = tk.StringVar()

    input_frame_cancel = ttk.Frame(root)
    input_frame_cancel.pack(pady=10, anchor='center')

    tk.Label(input_frame_cancel, text="Cancellation section!", font=("Helvetica", 20), foreground="black").grid(row=0, column=1, columnspan=2, pady=10)
    tk.Label(input_frame_cancel, text="", font=("Helvetica", 16)).grid(row=1, column=1, columnspan=4)
    tk.Label(input_frame_cancel, text="Pass Name:", font=("Helvetica", 18), foreground="black").grid(row=2, column=0, pady=5)
    tk.Entry(input_frame_cancel, textvariable=pass_name_var_cancel).grid(row=2, column=1, pady=5)
    tk.Label(input_frame_cancel, text="Phone No:", font=("Helvetica", 18), foreground="black").grid(row=2, column=2, pady=5)
    tk.Entry(input_frame_cancel, textvariable=phone_no_var_cancel).grid(row=2, column=3, pady=5)
    tk.Label(input_frame_cancel, text="Credit Card No:", font=("Helvetica", 18), foreground="black").grid(row=4, column=0, pady=5)
    tk.Entry(input_frame_cancel, textvariable=credit_card_no_var_cancel).grid(row=4, column=1, pady=5)

    def cancel_button_clicked():
        pass_name_to_cancel = pass_name_var_cancel.get()

        conn = sqlite3.connect("python.db")
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM payment_data
            WHERE pass_name = ?
        ''', (pass_name_to_cancel,))

        conn.commit()
        conn.close()

        print(f"Reservation for {pass_name_to_cancel} canceled. Data deleted from the database.")

    tk.Button(input_frame_cancel, text=" Cancel Reservation ", font=("Helvetica", 18), command=homepage, foreground="white", background="blue").grid(row=8, column=1, columnspan=2, pady=10)

root = tk.Tk()
root.title("Bus Reservation System")
root.geometry("900x700")
root.after(1000, window_for_cancellation)

root.mainloop()
