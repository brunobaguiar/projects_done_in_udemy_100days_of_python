from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('Watermark Your Images')

image_path = ""
mark_path = ""


def open_image():
    global image_path
    root.filename = filedialog.askopenfilename(initialdir="/Pictures", title="Select a file", filetypes=(
        ("JPEG (*.jpg)", "*.jpg"), ("PNG (*.png)", "*.png"), ("All files", "*.*")))
    Label(root, text=root.filename).grid(column=0, row=2)
    ImageTk.PhotoImage(Image.open(root.filename))
    image_path = root.filename
    return image_path


def open_watermark():
    global mark_path
    root.filename = filedialog.askopenfilename(initialdir="/Pictures", title="Select a file", filetypes=(
        ("JPEG (*.jpg)", "*.jpg"), ("PNG (*.png)", "*.png"), ("All files", "*.*")))
    Label(root, text=root.filename).grid(column=0, row=5)
    ImageTk.PhotoImage(Image.open(root.filename))
    mark_path = root.filename
    return mark_path


def show_image(x_pos=0, y_pos=0):
    # Opening the primary image (used in background)
    img1 = Image.open(image_path).convert("RGBA")
    # Opening the secondary image (overlay image)
    img2 = Image.open(mark_path).convert("RGBA")
    # Pasting img2 image on top of img1
    # starting at coordinates (0, 0)
    img1.paste(img2, (int(Entry_x.get()), int(Entry_y.get())), mask=img2)
    # Displaying the image
    img1.show()


# GUI Interface

Label(text="Choose an Image to Watermark").grid(column=0, row=0)
Button(root, text="Open Image", command=open_image).grid(column=0, row=1)
Label(text="Choose an Watermark").grid(column=0, row=3)
Button(root, text="Open Watermark", command=open_watermark).grid(column=0, row=4)
Label(text="Choose x position").grid(column=0, row=6)
Entry_x = Entry(root)
Entry_x.insert(0, "0")
Entry_x.grid(column=0, row=7)
Label(text="Choose y position").grid(column=0, row=8)
Entry_y = Entry(root)
Entry_y.insert(0, "0")
Entry_y.grid(column=0, row=9)
Label(text="Click to preview Image").grid(column=0, row=10)
Button(root, text="Preview", command=show_image).grid(column=0, row=11)

root.mainloop()
