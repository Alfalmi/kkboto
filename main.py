import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(columnspan=3, rowspan=3)

# logo = Image.open('logo.png')
# bg = ImageTk.PhotoImage(logo)
# bg_label = tk.Label(image=bg)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.configure(bg='#707698')


def textin():
    txt = text_box.get(1.0, "end-1c")
    resp['text'] = txt


# input text
text_box = tk.Text(root, height=3, width=40, padx=15, pady=15)

text_box.grid(column=0, row=2)

# send button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=textin, font="Raleway", bg="#171A2B",
                       fg="white", height=2, width=9)
browse_text.set("Send")
browse_btn.grid(column=2, row=2)

# response
resp = tk.Label(root, text='Pregunta...?!', bg='#707698', font='Helvetica 14')
resp.grid(column=0, row=0)

root.mainloop()
