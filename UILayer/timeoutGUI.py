import tkinter as tk


root = tk.Tk()
root.geometry(str(root.winfo_screenwidth()) + 'x' + str(root.winfo_screenheight()))

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

uploadTextbox = tk.Entry(root)
canvas.create_window(100, 140, window =uploadTextbox)

uploadButton = tk.Button(text='Upload')
canvas.create_window(200, 180, window=uploadButton)

w = tk.Label(root, text='Welcome to Timeout!!')
w.pack()

frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="QUIT",fg="red",command=quit)
button.pack()

root.mainloop()