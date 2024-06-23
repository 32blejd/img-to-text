from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract as pyt

root = Tk()
root.geometry("400x700")
root.resizable(width=True, height=True)
panel = None
text_area = None

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((350, 350))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    extracted_text = pyt.image_to_string(Image.open(x))
    text_area = Text(root, wrap=WORD)
    text_area.insert(INSERT, extracted_text)
    text_area.pack()
    text_area.config(state=NORMAL)
    return panel, text_area
def theme():
    color = root.configure(bg='black')
    return color



button_open = Button(root, text='open image', command=open_img).pack()
button_theme = Button(root, text='black theme', command=theme).pack()


root.mainloop()