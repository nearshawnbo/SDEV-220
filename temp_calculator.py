import tkinter as tk
# App Set-Up
window = tk.Tk()
window.title("TempCalculator")
window.geometry("600x350")
window.configure(bg="#D6D2D2")

#Main Card
card = tk.Frame(window, bg="#d7c7f8", width=595, height=345)
card.place(relx=0.5, rely=0.5, anchor="center") 

#Title

title = tk.Label(
    card,
    text="Celsius to Fahrenheit",
    bg="#e6e1f0",
    fg="#5b3a8c",
    font=("Arial", 24, "bold")
)
title.pack(pady=25)

#Input Row

input_frame = tk.Frame( card, bg="#e6e1f0")
input_frame.pack(pady=10)

celsius_entry = tk.Entry(
    input_frame,
    width= 18,
     font=("Arial", 14)
)
celsius_entry.grid(row=0, column=0, padx=22, ipady=6)

fahrenheit_output = tk.Label (
    input_frame,
    width= 18,
    bg="#b9a6d8",
    fg="#ffffff",
    font=("Arial", 14),
    anchor="center"
)
fahrenheit_output.grid(row=0, column=1, padx=22, ipady=6)

#Conversion Logic

def calculate():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_output.config(text=f"{fahrenheit:.1f}")
    except ValueError:
        fahrenheit_output.config(text="Invalid")

#Calc Button

calc_button = tk.Button(
    card,
    text="Calculate",
    command=calculate,
    bg="#6a3ea1",
    fg="white",
    font=("Arial", 14),
     padx=20,
    pady=6
)
calc_button.pack(pady=25)

window.mainloop()
