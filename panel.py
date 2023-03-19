import tkinter, webview, time
from tkinter import Tk, ttk, messagebox

window = Tk()
window.overrideredirect(True)

label = tkinter.Label(window, text="Please wait while we edit the configuration in ./home/user/.cache/epicgames/make.properties").grid(column=0, row=0)
btn = tkinter.Button(window, text="Cancel", command=close).grid(column=0, row=1)

bar = ttk.Progressbar(window, length=200)
bar['value'] = 70
bar.grid(column=0, row=2)

def close():
  res = messagebox.askyesno("Are you sure?", "Are you sure you want to close the application or process? This may affect the quality of your EpicGames installation.")
  if res: label.configure(text="Closing down..."); time.sleep(3); window.close()
  else: pass

window.mainloop()
