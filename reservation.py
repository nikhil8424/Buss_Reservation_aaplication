import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from tkinter import PhotoImage


def homepage():
    root.destroy()
    import mainpage
    
def save_to_database():
    try:
        # Retrieve values from the GUI
        from_location = from_var.get()
        to_location = to_var.get()
        date = date_var.get()
        

        # Insert values into the database
        cursor.execute('''
            INSERT INTO bus_data (from_location, to_location, date)
            VALUES (?, ?, ?)
        ''', (from_location, to_location, date))
        conn.commit()
        
        # Show the Our Services section
        show_our_services()

    except sqlite3.Error as e:
        # Handle SQLite errors
        print(f"SQLite error occurred: {e}")
        # You can add code here to handle the error, such as logging or showing an error message to the user
    except Exception as e:
        # Handle other types of exceptions
        print(f"An error occurred: {e}")
        # You can add code here to handle the error, such as logging or showing an error message to the user
def show_our_services():
    # Hide the input section
    input_frame.pack_forget()
    # Show the Our Services section
    services_frame.pack()

#third window in reservation sectiop
def open_new_window():
    # Destroy existing widgets in the main window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Bus Reservation System")
    root.state("zoomed")

    # Set background color
    root.configure(bg="light blue")  # You can choose any color you like

    # Variable declarations
    from_var_new = tk.StringVar()
    to_var_new = tk.StringVar()
    date_var_new = tk.StringVar()
    bus_class_var_new = tk.StringVar()
    seat_var_new = tk.StringVar()
    
    # Input section
    input_frame_new = ttk.Frame(root)
    input_frame_new.pack(pady=10, anchor='center')

    tk.Label(input_frame_new, text="Reserve Your Seat!", font=("Helvetica", 20)).grid(row=0, column=1, columnspan=2, pady=10)
    tk.Label(input_frame_new, text="", font=("Helvetica", 16)).grid(row=1, column=1, columnspan=4)
    tk.Label(input_frame_new, text="pickup point:", font=("Helvetica", 18)).grid(row=2, column=0, pady=5)
    tk.Entry(input_frame_new, textvariable=from_var_new).grid(row=2, column=1, pady=5)
    tk.Label(input_frame_new, text="drop point:", font=("Helvetica", 18)).grid(row=2, column=2, pady=5)
    tk.Entry(input_frame_new, textvariable=to_var_new).grid(row=2, column=3, pady=5)
    tk.Label(input_frame_new, text="No. of Seats", font=("Helvetica", 18)).grid(row=3, column=0, pady=5)
    tk.Entry(input_frame_new, textvariable=date_var_new).grid(row=3, column=1, pady=5)
    tk.Label(input_frame_new, text="Bus Class:", font=("Helvetica", 18)).grid(row=3, column=2, pady=5)
    tk.Label(input_frame_new, text="Seat type:", font=("Helvetica", 18)).grid(row=4, column=0, pady=5)

    # Declare bus_classes_new and seat_types_new
    bus_classes_new = ["Deluxe", "Semi-Deluxe", "Economy"]
    seat_types_new = ["Window", "Aisle"]
    
    # Bus class and seat type dropdown menus
    bus_class_dropdown = ttk.Combobox(input_frame_new, textvariable=bus_class_var_new, values=bus_classes_new)
    bus_class_dropdown.grid(row=3, column=3, pady=5)
    bus_class_dropdown.set("Deluxe")  # Set default value
    
    seat_type_dropdown = ttk.Combobox(input_frame_new, textvariable=seat_var_new, values=seat_types_new)
    seat_type_dropdown.grid(row=4, column=1, pady=5)
    seat_type_dropdown.set("Aisle")  # Set default value

    tk.Button(input_frame_new, text="Proceed to Payment", command=window_for_payment).grid(row=5, column=1, columnspan=2, pady=10)



#fourth window in payment secion

def window_for_payment():
    try:
        # Destroy existing widgets in the main window
        for widget in root.winfo_children():
            widget.destroy()

        root.title("Bus Reservation System")
        root.geometry("800x600")
        root.state("zoomed")

        # Set background color
        root.configure(bg="light blue")  

        # Variable declarations
        from_var_new = tk.StringVar()
        to_var_new = tk.StringVar()
        date_var_new = tk.StringVar()
        card_var_new = tk.StringVar()
        card_var_new1 = tk.StringVar()
        card_var_new2 = tk.StringVar()
        card_var_new3 = tk.StringVar()

        # Input section
        input_frame_new1 = ttk.Frame(root)
        input_frame_new1.pack(pady=10, anchor='center')

        tk.Label(input_frame_new1, text="Payment section!", font=("Helvetica", 20)).grid(row=0, column=1, columnspan=2, pady=10)
        tk.Label(input_frame_new1, text="", font=("Helvetica", 16)).grid(row=1, column=1, columnspan=4)
        tk.Label(input_frame_new1, text="pass Name:", font=("Helvetica", 18)).grid(row=2, column=0, pady=5)
        tk.Entry(input_frame_new1, textvariable=from_var_new).grid(row=2, column=1, pady=5)
        tk.Label(input_frame_new1, text="Phone No:", font=("Helvetica", 18)).grid(row=2, column=2, pady=5)
        tk.Entry(input_frame_new1, textvariable=to_var_new).grid(row=2, column=3, pady=5)
        tk.Label(input_frame_new1, text="Pass age:", font=("Helvetica", 18)).grid(row=3, column=0, pady=5)
        tk.Entry(input_frame_new1, textvariable=date_var_new).grid(row=3, column=1, pady=5)
        tk.Label(input_frame_new1, text="Credit Card no:", font=("Helvetica", 18)).grid(row=4, column=0, pady=5)
        tk.Entry(input_frame_new1, textvariable=card_var_new).grid(row=4, column=1, pady=5)
        tk.Label(input_frame_new1, text="owner name:", font=("Helvetica", 18)).grid(row=6, column=2, pady=5)
        tk.Entry(input_frame_new1, textvariable=card_var_new1).grid(row=6, column=3, pady=5)
        tk.Label(input_frame_new1, text="Cvv:", font=("Helvetica", 18)).grid(row=6, column=0, pady=5)
        tk.Entry(input_frame_new1, textvariable=card_var_new2).grid(row=6, column=1, pady=5)
        tk.Label(input_frame_new1, text="Expiry date:", font=("Helvetica", 18)).grid(row=4, column=2, pady=5)
        tk.Entry(input_frame_new1, textvariable=card_var_new3).grid(row=4, column=3, pady=5)
        tk.Button(input_frame_new1, text=" Payment Done ", font=("Helvetica", 18), command=homepage).grid(row=8, column=1, columnspan=2, pady=10)

        def select_button_clicked_new():
            try:
                # Get the values entered by the user
                pass_name = from_var_new.get()
                phone_no = to_var_new.get()
                pass_age = date_var_new.get()
                credit_card_no = card_var_new.get()  # Corrected variable name

                # Connect to SQLite database
                conn = sqlite3.connect("python.db")
                cursor = conn.cursor()

                # Create a table if it doesn't exist
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS payment_data (
                        id INTEGER PRIMARY KEY,
                        pass_name TEXT,
                        phone_no TEXT,
                        pass_age TEXT,
                        credit_card_no TEXT
                    )
                ''')

                # Insert user data into the table
                cursor.execute('''
                    INSERT INTO payment_data (pass_name, phone_no, pass_age, credit_card_no)
                    VALUES (?, ?, ?, ?)
                ''', (pass_name, phone_no, pass_age, credit_card_no))

                # Commit the changes and close the connection
                conn.commit()
                conn.close()

                print("Payment Done. Data inserted into the database.")
                homepage()  # Call the homepage function after successful payment

            except sqlite3.Error as e:
                # Handle SQLite errors
                print(f"SQLite error occurred: {e}")
                # You can add code here to handle the error, such as logging or showing an error message to the user
            except Exception as e:
                # Handle other types of exceptions
                print(f"An error occurred: {e}")
                # You can add code here to handle the error, such as logging or showing an error message to the user

    except Exception as e:
        # Handle exceptions related to widget creation or main window operations
        print(f"An error occurred: {e}")
        # You can add code here to handle the error, such as logging or showing an error message to the user

# Connect to SQLite database
conn = sqlite3.connect('python.db')
cursor = conn.cursor()

# Create a table to store values
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bus_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_location TEXT,
        to_location TEXT,
        date TEXT,

    )
''')
conn.commit()


# Create the main Tkinter window
root = tk.Tk()

# Set the window position and size
root.title("Bus Reservation System")
root.state("zoomed")
root.configure(bg="light blue")

# Variable declarations
from_var = tk.StringVar()#mainwindow
to_var = tk.StringVar()#mainwindow
date_var = tk.StringVar()#mainwindoe

bus_name_var = tk.StringVar()
departure_time_var = tk.StringVar()
arrival_time_var = tk.StringVar()
duration_var = tk.StringVar()
rating_var = tk.StringVar()
fare_var = tk.IntVar()

# Input section
input_frame = ttk.Frame(root)
input_frame.place(relx=0.5, rely=0.5, anchor='center')


tk.Label(input_frame, text="Welcome to MyBus    ", font=("wistfil", 20)).grid(row=0, column=1, columnspan=3, pady=10)
tk.Label(input_frame, text="India's No.1 online Bus Reservation Site         ", font=("wistfil", 16)).grid(row=1, column=1, columnspan=3)

tk.Label(input_frame, text="From:", font=("wistfil", 16)).grid(row=2, column=0, pady=5)
tk.Entry(input_frame, textvariable=from_var).grid(row=2, column=1, pady=5)
tk.Label(input_frame, text="To:", font=("wistfil", 16)).grid(row=2, column=2, pady=5)
tk.Entry(input_frame, textvariable=to_var).grid(row=2, column=3, pady=5)
tk.Label(input_frame, text="Date:", font=("wistfil", 16)).grid(row=3, column=0, pady=5)
tk.Entry(input_frame, textvariable=date_var).grid(row=3, column=1, pady=5)
tk.Button(input_frame, text="Proceed Further", command=save_to_database, font=("wistfil", 16)).grid(row=4, column=1, columnspan=2, pady=10)

# Our Services section
services_frame = ttk.Frame(root)

ttk.Label(services_frame, text="Our Services", background='#6AFB92', font=("wistfil", 16)).grid(row=0, column=0, columnspan=6, pady=5, sticky=tk.W)
# Departure Time section
ttk.Label(services_frame, text="Departure Time", background='#6AFB92', font=("wistfil", 16)).grid(row=2, column=0, pady=10, sticky=tk.W)
ttk.Label(services_frame, text="Buses", background='#a9e8c0', font=("wistfil", 16)).grid(row=1, column=1, pady=10)
ttk.Label(services_frame, text="Duration", background='#a9e8c0', font=("wistfil", 16)).grid(row=1, column=2, pady=10)
ttk.Label(services_frame, text="Rating", background='#a9e8c0', font=("wistfil", 16)).grid(row=1, column=3, pady=10)
ttk.Label(services_frame, text="Fare", background='#a9e8c0', font=("wistfil", 16)).grid(row=1, column=4, pady=10)
ttk.Label(services_frame, text="Selection", background='#a9e8c0', font=("wistfil", 16)).grid(row=1, column=5, pady=10)

# Departure Time 1
checkbutton1 = ttk.Checkbutton(services_frame, text="[] 10 PM to 2 AM", style="TCheckbutton")
checkbutton1.grid(row=3, column=0, pady=5, padx=35)
ttk.Label(services_frame, text="bus1", font=("wistfil", 16)).grid(row=3, column=1, pady=5, padx=35)
ttk.Label(services_frame, text="4hr", font=("wistfil", 16)).grid(row=3, column=2, pady=5, padx=35)
ttk.Label(services_frame, text="3star", font=("wistfil", 16)).grid(row=3, column=3, pady=5, padx=35)
ttk.Label(services_frame, text="4000", font=("wistfil", 16)).grid(row=3, column=4, pady=5, padx=35)
ttk.Button(services_frame, text="[confirm]", style="TButton", command=open_new_window).grid(row=3, column=5, pady=5, padx=35)

# Departure Time 2
checkbutton2 = ttk.Checkbutton(services_frame, text="[] 10 PM to 2 AM", style="TCheckbutton")
checkbutton2.grid(row=4, column=0, pady=5, padx=35)
ttk.Label(services_frame, text="bus2", font=("wistfil", 16)).grid(row=4, column=1, pady=5, padx=35)
ttk.Label(services_frame, text="3hr", font=("wistfil", 16)).grid(row=4, column=2, pady=5, padx=35)
ttk.Label(services_frame, text="4star", font=("wistfil", 16)).grid(row=4, column=3, pady=5, padx=35)
ttk.Label(services_frame, text="5000", font=("wistfil", 16)).grid(row=4, column=4, pady=5, padx=35)
ttk.Button(services_frame, text="[confirm]", style="TButton", command=open_new_window).grid(row=4, column=5, pady=5, padx=35)

# Arrival Time section
ttk.Label(services_frame, text="Arrival Time", background='#6AFB92', font=("wistfil", 16)).grid(row=7, column=0, pady=10, sticky=tk.W)

# Arrival Time 1
checkbutton4 = ttk.Checkbutton(services_frame, text="[] 10 PM to 2 AM", style="TCheckbutton")
checkbutton4.grid(row=8, column=0, pady=5, padx=35)
ttk.Label(services_frame, text="bus4", font=("wistfil", 16)).grid(row=8, column=1, pady=5, padx=35)
ttk.Label(services_frame, text="4hr", font=("wistfil", 16)).grid(row=8, column=2, pady=5, padx=35)
ttk.Label(services_frame, text="3star", font=("wistfil", 16)).grid(row=8, column=3, pady=5, padx=35)
ttk.Label(services_frame, text="4000", font=("wistfil", 16)).grid(row=8, column=4, pady=5, padx=35)
ttk.Button(services_frame, text="[confirm]", style="TButton", command=open_new_window).grid(row=8, column=5, pady=5, padx=35)

# Arrival Time 2
checkbutton5 = ttk.Checkbutton(services_frame, text="[] 10 PM to 2 AM", style="TCheckbutton")
checkbutton5.grid(row=9, column=0, pady=5, padx=35)
ttk.Label(services_frame, text="bus5", font=("wistfil", 16)).grid(row=9, column=1, pady=5, padx=35)
ttk.Label(services_frame, text="4hr", font=("wistfil", 16)).grid(row=9, column=2, pady=5, padx=35)
ttk.Label(services_frame, text="3star", font=("wistfil", 16)).grid(row=9, column=3, pady=5, padx=35)
ttk.Label(services_frame, text="4000", font=("wistfil", 16)).grid(row=9, column=4, pady=5, padx=35)
ttk.Button(services_frame, text="[confirm]", style="TButton", command=open_new_window).grid(row=9, column=5, pady=5, padx=35)

# Initially show the input section
input_frame.pack()

# Run the Tkinter event loop
root.mainloop()
