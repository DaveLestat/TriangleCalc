import tkinter as tk
from tkinter import messagebox
from triangle import RightTriangle

root = tk.Tk()
root.title("Right Triangle Calculator")
root.geometry("650x230")  # Set the window size

# Labels and entry fields for side A and B
label_side_a = tk.Label(root, text="Side A:")
label_side_a.grid(row=0, column=0, sticky=tk.W)
entry_side_a = tk.Entry(root)
entry_side_a.grid(row=0, column=1, sticky=tk.E)

label_side_b = tk.Label(root, text="Side B:")
label_side_b.grid(row=1, column=0, sticky=tk.W)
entry_side_b = tk.Entry(root)
entry_side_b.grid(row=1, column=1, sticky=tk.E)

# Labels and readonly entry fields for hypotenuse, area, and perimeter
label_hypotenuse = tk.Label(root, text="Hypotenuse:")
label_hypotenuse.grid(row=0, column=2, sticky=tk.W)
entry_hypotenuse = tk.Entry(root, state='readonly')
entry_hypotenuse.grid(row=0, column=3)

label_area = tk.Label(root, text="Area:")
label_area.grid(row=1, column=2, sticky=tk.W)
entry_area = tk.Entry(root, state='readonly')
entry_area.grid(row=1, column=3)

label_perimeter = tk.Label(root, text="Perimeter:")
label_perimeter.grid(row=2, column=2, sticky=tk.W)
entry_perimeter = tk.Entry(root, state='readonly')
entry_perimeter.grid(row=2, column=3)

# Canvas for drawing the triangle
canvas = tk.Canvas(root, width=300, height=150)
canvas.grid(row=3, columnspan=4)

def validate_input(side_a, side_b):
    if side_a <= 0 or side_b <= 0:
        raise ValueError("Sides must be positive integers")

def calculate_hypotenuse():
    try:
        side_a = int(entry_side_a.get())
        side_b = int(entry_side_b.get())
        validate_input(side_a, side_b)
        triangle = RightTriangle(side_a, side_b)
        entry_hypotenuse.configure(state='normal')
        entry_area.configure(state='normal')
        entry_perimeter.configure(state='normal')
        entry_hypotenuse.delete(0, tk.END)
        entry_hypotenuse.insert(0, str(triangle.sideC))
        entry_area.delete(0, tk.END)
        entry_area.insert(0, str(triangle.area))
        entry_perimeter.delete(0, tk.END)
        entry_perimeter.insert(0, str(triangle.perimeter))
        entry_hypotenuse.configure(state='readonly')
        entry_area.configure(state='readonly')
        entry_perimeter.configure(state='readonly')
        draw_triangle(side_a, side_b)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

def draw_triangle(side_a, side_b):
    canvas.delete("all")  # Clear previous drawings
    scale = min(200 / max(side_a, side_b), 3)  # Scaling factor
    canvas.create_polygon(10, 140, 10, 140 - side_b*scale, 10 + side_a*scale, 140, outline='black', fill='')

def clear_fields():
    entry_side_a.delete(0, tk.END)
    entry_side_b.delete(0, tk.END)
    entry_hypotenuse.configure(state='normal')
    entry_area.configure(state='normal')
    entry_perimeter.configure(state='normal')
    entry_hypotenuse.delete(0, tk.END)
    entry_area.delete(0, tk.END)
    entry_perimeter.delete(0, tk.END)
    entry_hypotenuse.configure(state='readonly')
    entry_area.configure(state='readonly')
    entry_perimeter.configure(state='readonly')
    canvas.delete("all")

calculate_button = tk.Button(root, text="Calculate", command=calculate_hypotenuse)
calculate_button.grid(row=2, column=0, pady=5, padx=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=2, column=1, pady=5, padx=5)

root.mainloop()
