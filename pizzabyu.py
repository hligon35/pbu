"""
Author: Harold Ligon
Date written: 12/2/2024
Assignment: Final Project
This program gathers the users choice selection for a pizza then creates an order.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import time

def closeGreetingWindow():
    greetingWindow.destroy()

# Create the greeting window
greetingWindow = tk.Tk()
greetingWindow.title("Greeting")

# Get screen width and height display
greetingWindow.state('zoomed')  

# Create a label with the title 'PizzaByU'
label = ttk.Label(greetingWindow, text = 'PizzaByU', 
                    font = ("Times New Roman", 100))
label.pack(side = 'top', anchor = 'center', pady = 350)

# Add image to background


# Set a timer to close the greeting window after half a second
greetingWindow.after(1000, closeGreetingWindow)
greetingWindow.mainloop()

# Create the Order Screen window
orderWindow = tk.Tk()
orderWindow.title("Order Screen")

# Set full screen display
orderWindow.state('zoomed')

# Create a label with the title 'Customize your order'
title = ttk.Label(orderWindow, text = 'Customize your order', font = ("Times New Roman", 40), anchor = 'center')
title.grid(padx = (450, 0), pady = (10, 0))


# Create a label for 'Size'
sizeLabel = ttk.Label(orderWindow, text = 'Pizza Size', font = ("Times New Roman", 20), anchor = 'center')
sizeLabel.grid(padx = (450, 0), pady = (10, 0))

# Defining size options
sizeOptions = ['Personal', 'Small', 'Medium', 'Large', 'XLarge']

# Variable to hold size options
size = tk.StringVar()
    
# Creating radio buttons for various sizes
for i, option in enumerate(sizeOptions, start = 1):
    radioButton = ttk.Radiobutton(orderWindow, text = option, variable = size, value = option)
    radioButton.grid(row = 5, column = i)
    radioButton.place(relx = 0.10, rely = 0.12, anchor = 'center')

for col in range(len(sizeOptions)):
    orderWindow.grid_columnconfigure(col, weight=1)


'''
#####

# Create a label for 'Crust'
crustLabel = ttk.Label(orderWindow, text = 'Crust', font = ("Times New Roman", 20), anchor = 'center')
crustLabel.grid(padx = (450, 0), pady = (50, 0))

# Defining crust options
crustOptions = ['Thin', 'Hand Tossed', 'Stuffed']

# Variable to hold crust options
crust = tk.StringVar()

# Creating radio buttons for various crust options
for i, option in enumerate(crustOptions, start = 1):
    radioButton = ttk.Radiobutton(orderWindow, text = option, variable = crust, value = option)
    radioButton.grid(row = 7, column = i)

#####

# Create a label for 'Sauce'
sauceLabel = ttk.Label(orderWindow, text = 'Sauce', font = ("Times New Roman", 20), anchor = 'center')
sauceLabel.grid(padx = (450, 0), pady = (80, 0))

# Defining sauce options
sauceOptions = ['Light', 'Regular', 'Extra']

# Variable to hold sauce options
sauce = tk.StringVar()

# Creating radio buttons for various sauce options
for i, option in enumerate(sauceOptions, start = 1):
    radioButton = ttk.Radiobutton(orderWindow, text = option, variable = sauce, value = option)
    radioButton.grid(row = 10, column = i)

#####

# Create a label for 'Cheese'
cheeseLabel = ttk.Label(orderWindow, text = 'Cheese', font = ("Times New Roman", 20), anchor = 'center')
cheeseLabel.grid(padx = (450, 0), pady = (110, 0))

# Defining cheese options
cheeseOptions = ['Light', 'Regular', 'Extra']

# Variable to hold cheese options
cheese = tk.StringVar()

# Creating radio buttons for various cheese options
for i, option in enumerate(cheeseOptions, start = 1):
    radioButton = ttk.Radiobutton(orderWindow, text = option, variable = cheese, value = option)
    radioButton.grid(row = 13, column = i)
#####

# Create a label for 'Toppings'
toppingsLabel = ttk.Label(orderWindow, text = 'Toppings', font = ("Times New Roman", 20), anchor = 'center')
toppingsLabel.grid(padx = (450, 0), pady = (140, 0))

# Defining cheese options
toppingsOptions = ['Three Cheese', 'Pepperoni', 'Sausage', 'Ham', 'Onions', 'Peppers', 'Mushrooms']

# Variable to hold cheese options
toppings = tk.StringVar()

# Creating radio buttons for various cheese options
for i, option in enumerate(toppingsOptions, start = 1):
    radioButton = ttk.Radiobutton(orderWindow, text = option, variable = toppings, value = option)
    radioButton.grid(row = 16, column = i)
'''
orderWindow.mainloop()