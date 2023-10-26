

from tkinter import *
root=Tk()
root.title("Fibonacci")
root.geometry("500x500")

label_series = Label(root,text="Fibonacci Series")
label_sum=Label(root,text="Fibonacci Sum")

def fibonacci():
    num = 12
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter<=num):
        label_series["text"]+=str(sum)+" "
        counter = counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no

label_sum["text"]="the fibnocci sum is : "+str(sum)

btn = Button(root,text="Show Fibonacci Series",command=fibonacci)
btn.pack()
label_sum.pack()
label_series.pack()

        

root.mainloop()