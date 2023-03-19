import tkinter, webview
from tkinter import Tk

window = Tk()
window.overrideredirect(True)

def close():
  res = tkinter.messagebox.askyesno("Are you sure?", "Are you sure you want to close the application or process? This may affect the quality of your EpicGames installation.")
  if res: window.overrideredirect(False)
  else: pass

label = tkinter.Label(window, text="Please wait while we edit the configuration in ./home/user/.cache/epicgames/make.properties").grid(column=0, row=0)
btn = tkinter.Button(window, text="Cancel", command=close).grid(column=0, row=1)

bar = Progressbar(window, length=200).grid(column=0, row=2)
bar['value'] = 70

window.mainloop()
