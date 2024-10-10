from tkinter import *
import ast

root = Tk()
root.geometry("400x260")  

i = 0 
def get_number(num):
    global i
    display.insert(i,num) 
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode='eval')
        result = eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def undo():
    entre_string = display.get()
    if len(entre_string):
        new_string = entre_string[:-1]
        clear_all()
        display.insert(0,new_string)

    else:
        clear_all()
        display.insert(0,"")

display = Entry(root, width=30, font=("Arial", 18))  
display.grid(row=0, columnspan=6, padx=5, pady=5)  
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=str(button_text),width=5,height=2,font=("Arial", 12), command=lambda text=button_text:get_number(text) )
        counter+=1
        button.grid(row=x+1,column=y, padx=2, pady=2)  # Add some padding around the buttons

button = Button(root,text="0",width=5,height=2,font=("Arial", 12), command=lambda :get_number(0) )
button.grid(row=4,column=1, padx=2, pady=2)

count = 0
operations = ['+','-','*','/','*3.14','%','(','**',')','**2']
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root,text=operations[count],width=5,height=2,font=("Arial", 12), command=lambda text= operations[count]:get_operation(text))
            count+=1
            button.grid(row=x+1,column=y+3, padx=2, pady=2)

Button(root,text="AC",width=5,height=2,font=("Arial", 12), command=clear_all).grid(row=4,column=0, padx=2, pady=2)
Button(root,text="=",width=5,height=2,font=("Arial", 12), command=calculate).grid(row=4,column=2, padx=2, pady=2)

Button(root,text="<-",width=5,height=2,font=("Arial", 12), command=lambda : undo()).grid(row=4,column=4, padx=2, pady=2)

root.mainloop()