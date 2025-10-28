import segno
from tkinter import filedialog
import tkinter as tkin


window=tkin.Tk()
window.title('hi')
window.geometry("550x450")

frame=tkin.Frame(borderwidth=5,relief="groove")

link=tkin.Entry(master=frame)
link.insert(0,"Insert Link Here")

img_file_loc=tkin.Entry(master=frame,width=20)

# #functions :)
# def load_img_file():
    # song=filedialog.askopenfilename(initialdir='Pictures', title = "Choose an Image File", filetypes=(("PNG","*.png"),("JPG", "*.jpg"),("Webp", "*.webp"),))
    
    # img_file_loc.insert(0,song)
    
    # print(img_file_loc.get())

# def create_qr_code_art():
    # qr_code=segno.make(link.get(),error="h")
    # qr_code.to_artistic(background=img_file_loc.get(),target=img_file_loc.get().split("/")[-1],scale=8)
    
    # qr_code.save(
        # "qr_code.png",
        # border=2,
        # error="h"
    # )
def create_qr_code():
    qr_code=segno.make(link.get())
    qr_code.designator
    
    qr_code.save(
        "qr_code.png",
        border=2,
    )
    print("alllllllllllllllllllllllllllllllllll done")
#img=tkin.Button(text="image file location if you want",master=frame,command=load_img_file)

create_qr_norm=tkin.Button(text="Create QR CODE",master=frame,width=20,command=create_qr_code)

#create_qr_art=tkin.Button(text="Create QR CODE with ART",master=frame,width=20,command=create_qr_code_art)


frame.pack()
link.pack()
#img.pack()
#img_file_loc.pack()
create_qr_norm.pack()
#create_qr_art.pack()

tkin.mainloop()