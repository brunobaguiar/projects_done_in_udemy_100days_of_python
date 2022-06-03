from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import colorgram

root = Tk()
root.title('Image Colour Palette Generator')
root.config(padx=50, pady=50, bg='grey')

image_path = ""
mark_path = ""
image_colours = ""
rgb_colours = []
colours_dict = {}


class Table:
    def __init__(self, root):
        # code for creating table
        for key in colours_dict:
            for i in range(len(colours_dict[key])):
                if i == 0:
                    self.e = Entry(root, width=15, bg=colours_dict[key][i + 2],
                                   font=('Arial', 10, 'normal'))

                    self.e.grid(row=5+key, column=i)
                else:
                    self.e = Entry(root, width=15, fg="black",
                                   font=('Arial', 10, 'normal'))

                    self.e.grid(row=5+key, column=i)
                    self.e.insert(END, colours_dict[key][i])


def rescale_image(img):
    # set the base width of the result
    basewidth = 300
    # determining the height ratio
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    # resize image and save
    img = img.resize((basewidth, hsize), Image.LANCZOS)
    return img


def open_image():
    global image_path
    root.filename = filedialog.askopenfilename(initialdir="/Pictures", title="Select a file", filetypes=(
        ("JPEG (*.jpg)", "*.jpg"), ("PNG (*.png)", "*.png"), ("All files", "*.*")))
    my_image = Image.open(root.filename)
    resized_my_image = rescale_image(my_image)
    my_tk_image = ImageTk.PhotoImage(resized_my_image)
    label = Label(image=my_tk_image)
    label.image = my_tk_image  # keep a reference and tkinter will show the image!
    label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)
    image_path = root.filename


def convert_rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def get_color():
    # Table headings
    Label(text="Color", width=15, borderwidth=1).grid(column=0, row=4, pady=5)
    Label(text="RGB", width=15, borderwidth=1).grid(column=1, row=4, pady=5)
    Label(text="HEX", width=15, borderwidth=1).grid(column=2, row=4, pady=5)
    # Extract 10 colors from an image.
    colors = colorgram.extract(image_path, 10)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colours.append(new_color)
    for i in range(len(rgb_colours)):
        colours_dict[i] = [rgb_colours[i], str(rgb_colours[i]), convert_rgb_to_hex(rgb_colours[i])]
    t = Table(root)


# GUI Interface

Label(text="Choose an Image", width=15, bg="grey", font=('Arial', 12, 'bold')).grid(column=0, row=0, padx=5, pady=5, columnspan=2)
Button(root, text="Open Image", width=15, command=open_image).grid(column=2, row=0, padx=5, pady=5)
Button(root, text="Run", width=15, command=get_color).grid(column=1, row=3, padx=5, pady=5)


root.mainloop()
