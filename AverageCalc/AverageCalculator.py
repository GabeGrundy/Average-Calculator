import tkinter as tk
from PIL import Image, ImageTk

# window properties
window = tk.Tk()
window.title("Three Number Average Calculator")
window.geometry("600x400")
window.resizable(False, False)
window.config(bg="#1f1f1f")
window.iconbitmap("Calc.ico")

# custom functions
def LightMode(): #makes a light mode function that makes the screen turn white (dark mode is default)
    window.configure(bg="#f0f0f0")
    btnLight.configure(bg="#f0f0f0", fg="black")
    btnDark.configure(bg="#f0f0f0", fg="black")
    lblNumber1.configure(bg="#f0f0f0", fg="black")
    lblNumber2.configure(bg="#f0f0f0", fg="black")
    lblNumber3.configure(bg="#f0f0f0", fg="black")
    lblAnswer.configure(bg="#f0f0f0", fg="black")
    txtNumber1.configure(bg="#f0f0f0", fg="black")
    txtNumber2.configure(bg="#f0f0f0", fg="black")
    txtNumber3.configure(bg="#f0f0f0", fg="black")
    btnCalc.configure(bg="#f0f0f0", fg="black")

def DarkMode(): #makes a dark mode function that makes the screen turn dark grey
    window.configure(bg="#1f1f1f")
    btnLight.configure(bg="#1f1f1f", fg="white")
    btnDark.configure(bg="#1f1f1f", fg="white")
    lblNumber1.configure(bg="#1f1f1f", fg="white")
    lblNumber2.configure(bg="#1f1f1f", fg="white")
    lblNumber3.configure(bg="#1f1f1f", fg="white")
    lblAnswer.configure(bg="#1f1f1f", fg="white")
    txtNumber1.configure(bg="#1f1f1f", fg="white")
    txtNumber2.configure(bg="#1f1f1f", fg="white")
    txtNumber3.configure(bg="#1f1f1f", fg="white")
    btnCalc.configure(bg="#1f1f1f", fg="white")

def calculateAverage(): # takes the three numbers from the three textboxes and adds them together and divides them by 3
    try:
        Number1 = float(txtNumber1.get())
        Number2 = float(txtNumber2.get())
        Number3 = float(txtNumber3.get())
        average = (Number1 + Number2 + Number3) / 3
        lblAnswer.config(text=average)
    except ValueError:
        lblAnswer.config(text="ERROR: Numbers only silly.")


# add image
image = Image.open('average.PNG')
# Resize the image to fit the window
image = image.resize((600, 65))
image = ImageTk.PhotoImage(image)

# create labels that describe each box and one that shows the answer 
image_label = tk.Label(window, image=image)
lblNumber1 = tk.Label(window, text="Number 1: ", bg="#1f1f1f", fg="white")
lblNumber2 = tk.Label(window, text="Number 2: ", bg="#1f1f1f", fg="white")
lblNumber3 = tk.Label(window, text="Number 3: ", bg="#1f1f1f", fg="white")
lblAnswer = tk.Label(window, text="Answer: ", bg="#1f1f1f", fg="white")

# create textboxes for user input 
txtNumber1 = tk.Entry(window, bg="#1f1f1f", fg="white")
txtNumber2 = tk.Entry(window, bg="#1f1f1f", fg="white")
txtNumber3 = tk.Entry(window, bg="#1f1f1f", fg="white")

# create buttons
btnCalc = tk.Button(window, text="Calculate Average!", command=calculateAverage, bg="#1f1f1f", fg="white")
btnLight = tk.Button(window, text="Light Mode", command=LightMode, bg="#1f1f1f", fg="white")
btnDark = tk.Button(window, text="Dark Mode", command=DarkMode, bg="#1f1f1f", fg="white")

# add gui items to grid
image_label.pack()
btnCalc.place(relx=0.5, rely=0.7, anchor="center")
lblNumber1.place(relx=0.2, rely=0.4, anchor="center")
lblNumber2.place(relx=0.2, rely=0.5, anchor="center")
lblNumber3.place(relx=0.2, rely=0.6, anchor="center")
txtNumber1.place(relx=0.4, rely=0.4, anchor="center")
txtNumber2.place(relx=0.4, rely=0.5, anchor="center")
txtNumber3.place(relx=0.4, rely=0.6, anchor="center")
lblAnswer.place(relx=0.7, rely=0.5, anchor="center")
btnLight.place(relx=0.1, rely=0.2, anchor="nw")
btnDark.place(relx=0.9, rely=0.2, anchor="ne")

# window build
window.mainloop()