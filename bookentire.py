import tkinter as tk
from tkinter import ttk
import sqlite3

def homepage():
    root.destroy()
    import mainpage

def window_for_booking():
    for widget in root.winfo_children():
        widget.destroy()
    root.state("zoomed")

    root.configure(bg="light blue")

    bus_type_var = tk.StringVar()
    timings_var = tk.StringVar()
    date_var = tk.StringVar()
    driver_needed_var = tk.BooleanVar()
    pickup_location_var = tk.StringVar()
    drop_location_var = tk.StringVar()
    num_seaters_var = tk.StringVar()
    num_seaters_options = ["Volvo 21 seater bus: Good for weddings, picnics, and corporate events",
                           "Volvo 42 seater bus: Available for booking on Clear Car Rental",
                           "Sml Executive 13 seater bus: Good for groups of up to 13 people"]

    input_frame_booking = ttk.Frame(root, style='LightBlue.TFrame')
    input_frame_booking.pack(pady=10, anchor='center')

    tk.Label(input_frame_booking, text="BOOK ENTIRE BUS!!!", font=("Helvetica", 20), foreground="blue").grid(row=0, column=1, columnspan=2, pady=10)
    tk.Label(input_frame_booking, text="", font=("Helvetica", 16)).grid(row=1, column=1, columnspan=4)
    tk.Label(input_frame_booking, text="Bus Type:", font=("Helvetica", 18), foreground="blue").grid(row=2, column=0, pady=5)
    tk.OptionMenu(input_frame_booking, bus_type_var, *num_seaters_options).grid(row=2, column=1, pady=5, columnspan=3)
    tk.Label(input_frame_booking, text="Timings:", font=("Helvetica", 18), foreground="blue").grid(row=4, column=0, pady=5)
    tk.Entry(input_frame_booking, textvariable=timings_var).grid(row=4, column=1, pady=5)
    tk.Label(input_frame_booking, text="Date:", font=("Helvetica", 18), foreground="blue").grid(row=4, column=2, pady=5)
    tk.Entry(input_frame_booking, textvariable=date_var).grid(row=4, column=3, pady=5)
    tk.Label(input_frame_booking, text="Driver Needed:", font=("Helvetica", 18), foreground="blue").grid(row=6, column=0, pady=5)
    tk.Checkbutton(input_frame_booking, variable=driver_needed_var, onvalue=True, offvalue=False).grid(row=6, column=1, pady=5)
    tk.Label(input_frame_booking, text="Pickup Location:", font=("Helvetica", 18), foreground="blue").grid(row=6, column=2, pady=5)
    tk.Entry(input_frame_booking, textvariable=pickup_location_var).grid(row=6, column=3, pady=5)
    tk.Label(input_frame_booking, text="Drop Location:", font=("Helvetica", 18), foreground="blue").grid(row=8, column=0, pady=5)
    tk.Entry(input_frame_booking, textvariable=drop_location_var).grid(row=8, column=1, pady=5)
    tk.Label(input_frame_booking, text="Number of Seaters:", font=("Helvetica", 18), foreground="blue").grid(row=8, column=2, pady=5)
    tk.OptionMenu(input_frame_booking, num_seaters_var, *["28", "35", "50", "60"]).grid(row=8, column=3, pady=5)

    def book_button_clicked():
        bus_type = bus_type_var.get()
        timings = timings_var.get()
        date = date_var.get()
        driver_needed = driver_needed_var.get()
        pickup_location = pickup_location_var.get()
        drop_location = drop_location_var.get()
        num_seaters = num_seaters_var.get()

        conn = sqlite3.connect("python.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bus_booking (
                id INTEGER PRIMARY KEY,
                bus_type TEXT,
                timings TEXT,
                date TEXT,
                driver_needed BOOLEAN,
                pickup_location TEXT,
                drop_location TEXT,
                num_seaters TEXT
            )
        ''')

        cursor.execute('''
            INSERT INTO bus_booking (bus_type, timings, date, driver_needed, pickup_location, drop_location, num_seaters)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (bus_type, timings, date, driver_needed, pickup_location, drop_location, num_seaters))

        conn.commit()
        conn.close()

        print("Bus booking successful. Data inserted into the database.")

        homepage()

    tk.Button(input_frame_booking, text=" Book Bus ", font=("Helvetica", 18), command=book_button_clicked, foreground="white", background="blue").grid(row=10, column=1, columnspan=2, pady=10)

root = tk.Tk()
root.title("Bus Reservation System")
root.geometry("900x700")
root.after(1000, window_for_booking)

root.mainloop()
