from tkinter import *


def km_to_miles():
    km = float(km_input.get())
    miles = km * 0.621371192
    miles_result_label.config(text=f'{miles}')


window = Tk()
window.title('Kilometers to Miles Converter')
window.config(padx=20, pady=20)

km_input = Entry(width=7)
km_input.grid(column=1, row=0)

km_label = Label(text='Kilometers')
km_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

miles_result_label = Label(text='0')
miles_result_label.grid(column=1, row=1)

kilometer_label = Label(text='mi')
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=km_to_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()
