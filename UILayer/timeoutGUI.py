import tkinter as tk
from ServiceLayer import TimeoutService


service = TimeoutService.TimeoutService()

root = tk.Tk()
root.geometry(str(root.winfo_screenwidth()) + 'x' + str(root.winfo_screenheight()))
print(root.winfo_screenwidth())
canvasHeading = tk.Canvas(root, width=1366, height=50)
canvasHeading.config(background='white')
print(service.get_windows_username())
canvasHeading.pack()

canvasHeading.create_text(100, 100, text='Welcome', fill='black')


#uploadTextbox = tk.Entry(root)
#canvas.create_window(100, 140, window =uploadTextbox)

#uploadButton = tk.Button(text='Upload')
#canvas.create_window(200, 180, window=uploadButton)

w = tk.Label(root, text='Welcome to Timeout!!')
w.pack()

frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="QUIT",fg="red",command=quit)
button.pack()

root.mainloop()