from tkinter import *
from PIL import Image, ImageTk


def main():
    root = Tk()
    root.geometry("750x270")
    canvas = Canvas(root, width=1000, height=1500)
    canvas.pack()
    img = (Image.open("report_fixed_empty.png"))
    resized_image = img.resize((300, 205), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(10, 10, anchor=NW, image=new_image)
    root.mainloop()


if __name__ == '__main__':
    main()
