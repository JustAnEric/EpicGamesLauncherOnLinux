import tkinter, webview
from tkinter import Tk

window = Tk()

label = tkinter.Label(window, text="Please wait while we edit the configuration in ./home/user/.cache/epicgames/make.properties").grid(column=0, row=0)

window.mainloop()
