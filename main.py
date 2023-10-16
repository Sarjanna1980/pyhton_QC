import tkinter as tk
from tkinter import PhotoImage

# Create the main window
main_window = tk.Tk()
main_window.title("GUI Application with Image Background")
main_window.geometry("900x900")
main_window.iconbitmap("C:/Users/Sahar/Desktop/PythonProject1/myIcon.ico")

bg_image = PhotoImage(file="Desktop Cover_01.png")  # Replace "Desktop Cover_01.png" with your image file
main_window.bg_image = bg_image
# Create a canvas widget to display the background image
canvas = tk.Canvas(main_window, width=1450, height=900)
canvas.grid(row=0, column=0, rowspan=80, columnspan=20)
canvas.create_image(0, 0, anchor=tk.NW, image=main_window.bg_image)

label = tk.Label(main_window, text="Selected option: None").grid(row=5, column=0)


# Create a variable to store the selected option
radio_var = tk.StringVar()

# Create radio buttons
radio_button1 = tk.Radiobutton(main_window, text="Option 1", variable=radio_var, value="Option 1", ).grid(row=6, column=0)
radio_button2 = tk.Radiobutton(main_window, text="Option 2", variable=radio_var, value="Option 2", ).grid(row=7, column=0)
radio_button3 = tk.Radiobutton(main_window, text="Option 3", variable=radio_var, value="Option 3", ).grid(row=8, column=0)

tk.Label(main_window, text="Order Number", fg="red", bg="blue4", font=("Arial", 16)).grid(row=0, column=0,
                                                                                          sticky='e')
tk.Label(main_window, text="Procedure number : QCP-INSP-021", fg="red", bg="blue4", font=("Arial", 20)).grid(
    row=0, column=6, sticky='e')
entry_l1 = tk.Entry(main_window)
entry_l1.grid(row=0, column=1, sticky='w', )

def on_click():
    global bg_image
    top = tk.Toplevel()
    top.title("second")
    top.geometry("1424x780")
    bg_image = PhotoImage(file="Desktop Cover_01.png")
    canvas = tk.Canvas(top, width=1424, height=780)
    canvas.grid(row=0, column=0, rowspan=10, columnspan=10)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    button2 = tk.Button(top, text="Click me", command=top.quit)
    button2.grid(row=0, column=0, columnspan=2)
button = tk.Button(main_window, text="Click me", command=on_click)
button.grid(row=3, column=0, columnspan=2)

main_window.mainloop()