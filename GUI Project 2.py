"""

Author:  Jack Frank
Date written: 07/15/2024
Assignment:   Module6 Project Status Report II
Short Desc:   This is a GUI in progress, used 
for creating a simulation of ordering a menu
from a fake resturaunt called "Goody Burger 
Interprises."


"""

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


root = Tk()
root.title("Goody Burger Interprises: Food For Thought")

# Function for handling button click.
def ViewMenu():
    menu_items = "Menu:\n\n1. Burger - $5.99\n2. Fries - $2.49\n3. Soda - $1.99\n4. Salad - $4.99\n5. GUI Burger - $12.99"
    menu_window = Toplevel(root)
    menu_label = Label(menu_window, text=menu_items, padx=20, pady=20)
    menu_label.pack()

    backButton = Button(menu_window, text= "Go back?", command=menu_window.destroy)
    backButton.pack()

def Exit():
    root.destroy()

def OrderUp():
    selected_items = []  # List to store selected items

    while True:
        # Prompt user to select an item
        user_choice = simpledialog.askstring("Order Items", "Enter item number to add to order (press Cancel to finish):")
        
        if user_choice is None:  # User clicked Cancel
            break
        
        try:
            item_number = int(user_choice)
            if item_number >= 1 and item_number <= 5:  # Valid item number range
                items = ["Burger", "Fries", "Soda", "Salad", "GUI Burger"]
                selected_items.append(items[item_number - 1])
            else:
                messagebox.showinfo("Invalid Selection", "Please enter a number between 1 and 5.")
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter a valid number.")

    if selected_items:
        order_summary = "You ordered:\n\n" + "\n".join(selected_items)
        order_window = Toplevel(root)
        order_label = Label(order_window, text=order_summary, padx=20, pady=20)
        order_label.pack()

        # Ask user if they want to continue ordering
        answer = messagebox.askyesno("Continue Ordering", "Do you want to place another order?")
        if not answer:
            Exit()  # If user chooses not to continue, exit the application


#Labels
myLabel1=Label(root, text="Welcome to Goody Burger Interprises")
myLabel2=Label(root, text="Would you like to review your order?")
myLabel3=Label(root, text="...Or would you like to leave?")

# Three buttons
myButton1 = Button(root, text="View Order", command=ViewMenu)
myButton2 = Button(root, text="Place Order", command=OrderUp)
myButton3 = Button(root, text="Exit", command=Exit)

# Grid layout
myLabel1.grid(row=0, column=0, columnspan=3, pady=15, sticky='nsew')
myLabel2.grid(row=1, column=0, columnspan=3, pady=15, sticky='nsew')
myLabel3.grid(row=2, column=0, columnspan=3, pady=15, sticky='nsew')
myButton1.grid(row=3, column=0, padx=20, pady=15, sticky='nsew')
myButton2.grid(row=3, column=1, padx=20, pady=15, sticky='nsew')
myButton3.grid(row=3, column=2, padx=20, pady=15, sticky='nsew')

#Configure grid to center
for row in range(4):
    root.grid_rowconfigure(row, weight=1)
for col in range(3):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()