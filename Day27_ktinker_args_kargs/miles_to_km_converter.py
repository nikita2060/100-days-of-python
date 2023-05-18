from tkinter import *


def miles_to_km():
    mile = entry.get()
    km = str(round(int(mile) * 1.6))
    result_label.config(text=km)


window = Tk()
window.title("Mile to km converter")
window.minsize(width=300, height=300)

entry = Entry(width=7)
entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
