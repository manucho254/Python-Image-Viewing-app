from tkinter import *
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import *

class Images(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title('Image Viewer')
        self.root.geometry('1370x680+-10+10')
        self.root.resizable(width=1, height=1)
        self.root.configure(bg="gray72")
        
        files = "image3.jpeg"

        self.var = StringVar()
        self.var.set(files.title())
        self.nameLabel = Label(
            self.root , textvariable=self.var, 
            bd=2, fg='black', bg='white', 
            font='helvetica, 15 bold', relief='raised', width=50)
        self.nameLabel.place(x=400, y=1)

        self.img1 = Image.open(files)
        self.img1 =  self.img1.resize((1360, 640), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img1)
        self.imageLabel = Label(self.root)
        self.imageLabel.place(x=2, y=30)
        self.imageLabel["compound"] = LEFT
        self.imageLabel["image"] = self.img

        #  list of images
        def loadImages():
            directory = filedialog.askdirectory()
        
            os.chdir(directory)# it permits to change the current dir
            allImages = os.listdir()
            allImages.reverse()
            self.listImages = Listbox(self.root, bd=5, width=191, height=2,selectbackground='grey73')
            self.listImages.place(x=0, y=900)
            for image in allImages: # it returns the list of files song
                pos = 0
                if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                    self.listImages.insert(pos, image)
                    pos +=1
            self.listImages.selection_set(0)
            self.listImages.see(0)
            self.listImages.activate(0)
            self.listImages.selection_anchor(0)
            image = self.listImages.curselection()
            images = self.listImages.get(image[0])
            self.img1 = Image.open(images)
            self.img1 =  self.img1.resize((1360, 640), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img1,)
            self.imageLabel = Label(self.root)
            self.imageLabel.place(x=2, y=30)
            self.imageLabel["compound"] = LEFT
            self.imageLabel["image"] = self.img

            
        def nextImage():
            try:
                next_one = self.listImages.curselection()
                next_one = next_one[0]+1
                image = self.listImages.get(next_one)
                self.img1 = Image.open(image)
                self.img1 =  self.img1.resize((1360, 640), Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(self.img1,)
                self.imageLabel = Label(self.root)
                self.imageLabel.place(x=2, y=30)
                self.imageLabel["compound"] = LEFT
                self.imageLabel["image"] = self.img
                self.listImages.select_clear(0, END)
                self.listImages.activate(next_one)
                self.listImages.selection_set(next_one, last=None)
                self.var.set(image)
                self.button1 = Button(self.root,  text='<', bd=5 ,bg='gray72', fg='black', font='helvetica, 10 bold', command=previousImage)
                self.button1.place(x=2, y=270)
                self.button2 = Button(self.root,  text='>', bd=5 , bg='gray72', fg='black', font='helvetica, 10 bold', command=nextImage)
                self.button2.place(x=1340, y=270)
            except:
                showerror("No Next Image", "Please press the Previous button")

        def previousImage():
            try:
                next_one = self.listImages.curselection()
                next_one = next_one[0]-1
                image = self.listImages.get(next_one)
                self.img1 = Image.open(image)
                self.img1 =  self.img1.resize((1360, 640), Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(self.img1,)
                self.imageLabel = Label(self.root)
                self.imageLabel.place(x=2, y=30)
                self.imageLabel["compound"] = LEFT
                self.imageLabel["image"] = self.img
                self.listImages.select_clear(0, END)
                self.listImages.activate(next_one)
                self.listImages.selection_set(next_one, last=None)
                self.var.set(image)
                self.button1 = Button(self.root,  text='<', bd=5 ,bg='gray72', fg='black', font='helvetica, 10 bold', command=previousImage)
                self.button1.place(x=2, y=270)
                self.button2 = Button(self.root,  text='>', bd=5 , bg='gray72', fg='black', font='helvetica, 10 bold', command=nextImage)
                self.button2.place(x=1340, y=270)
            except:
                showerror("No Previous Image", "Please press the Next button")

        self.root.bind('<Right>', lambda x: nextImage())
        self.root.bind('<Left>', lambda x: previousImage())

        
        self.buttonBrowse = Button(self.root , text=u"\U0001F5C1 Broswe Images \U0001F5C1 ", bd=3, font='helvetica, 10 bold', command=loadImages)
        self.buttonBrowse.place(x=4, y=1)

        self.Exit = Button(self.root , text="Exit", bd=3, fg='red', width=10, font='helvetica, 10',  command=self.root.destroy)
        self.Exit.place(x=1274, y=1)

def main():
    root = Tk()
    ui = Images(root)
    root.mainloop()

if __name__ == "__main__":
    main()

