from tkinter import *
root = Tk()
root.geometry("400x450")
root.title("Welcome from McDonald's")

lst = Label(root,text="Regular Menu")
listbox = Listbox(root)
listbox.insert(1,"Promotion Meals")
listbox.insert(2,"Chicken McCrispy")

lst.pack()
listbox.pack()
root.mainloop()

'''frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

bth1 = Button(frame,text="Promotion Meals",fg="red").place(x=30,y=50)
bth1.pack(side=LEFT)

bth2 = Button(frame,text="Chicken McCrispy",fg="blue").place(x=30,y=90)
bth2.pack(side=LEFT)

root.mainloop()'''


"""print("Welcome from McDonald's")

userquest = str(input("Please choose your order : "))
menu = ["Promotion Meals","Chicken McCrispy","Sharing","Ala Carte & Value Meals","Sides","Sides","Desserts","Beverages","For the Family"]
print("Please chooose your menu",menu)

#add comment
print("Add code")"""