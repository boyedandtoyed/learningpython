from tkinter import *
root = Tk()
root.title("What the heck")
root.iconbitmap(r"C:\Users\Hp\anaconda3\pkgs\pywin32-227-py37he774522_1\Lib\site-packages\win32\Demos\images\frowny.bmp")
root.geometry("500x500")

my_label = Label(root, text="Binod TIwari"+u"\u00b0", font=("Helvetica", 32)).pack(pady=100)
my_button = Button(root, text=u"\u00BB", font=("Helvetica", 32)).pack(pady=100)
root.mainloop()
