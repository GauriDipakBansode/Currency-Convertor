import tkinter              #using tkinter

m=tkinter.Tk()  
m['bg']="skyblue" 
Font_tuple = ("Comic Sans MS",15, "bold")                     #creating a tkinter window
m.title("Exchange master")
m.geometry('534x160')
l1=tkinter.Label(text="From:",anchor="w",width=10,bg="skyblue",fg="white")
l1.configure(font = Font_tuple)
l1.grid(row=1,column=0)
l2=tkinter.Label(text="To:",anchor="e",width=10,bg="skyblue",fg="white")
l2.configure(font = Font_tuple)
l2.grid(row=1,column=2)

E1=tkinter.Entry(m,width=43)
E1.grid(row=3,column=0)

ans=tkinter.DoubleVar()

result=tkinter.Entry(m,width=43,relief="raised",textvariable=ans,bg="white",fg="black")
result.grid(row=3,column=2)
selected_option = tkinter.StringVar(m)
# Create the dropdown menu
options = ["Rupees", "Yuan", "Euro", "Dollar","Rand"]
dropdown = tkinter.OptionMenu(m, selected_option, *options)
dropdown.config(width=18)
dropdown.configure(font = Font_tuple)
dropdown.grid(row=2,column=0)
# Add a button to display the selected option
selected_option.set("Rupees")

selected_option2 = tkinter.StringVar(m)
options2 = ["Rupees", "Yuan", "Euro", "Dollar","Rand"]
dropdown = tkinter.OptionMenu(m, selected_option2, *options)
dropdown.grid(row=2,column=2)
dropdown.configure(font = Font_tuple)
dropdown.config(width=18)
selected_option2.set("Rupees")

def clear():
   result.delete(0,"end")
   E1.delete(0,"end")
   

def convert():
    if selected_option.get()=="Rupees":
        if selected_option2.get()=="Dollar":
            rs=float(E1.get())/83.44
            ans.set(rs)
        elif selected_option2.get()=="Euro":
            rs=float(E1.get())*0.011
            ans.set(rs)
        elif selected_option2.get()=="Yuan":
            rs=float(E1.get())*0.085
            ans.set(rs)
        elif selected_option2.get()=="Rand":
            rs=float(E1.get())*0.22
            ans.set(rs)
        elif selected_option2.get()=="Rupees":
            rs=float(E1.get())
            ans.set(rs)
           
    elif selected_option.get()=="Dollar":
        if selected_option2.get()=="Rupees":
            d=float(E1.get())*83.44
            ans.set(d)
        elif selected_option2.get()=="Euro":
            d=float(E1.get())*0.92
            ans.set(d)
        elif selected_option2.get()=="Yuan":
            d=float(E1.get())*7.23
            ans.set(d)
        elif selected_option2.get()=="Rand":
            d=float(E1.get())*18.73
            ans.set(d)
        elif selected_option2.get()=="Dollar":
            d=float(E1.get())
            ans.set(d)

    elif selected_option.get()=="Euro":
        if selected_option2.get()=="Rupees":
            e=float(E1.get())*90.37
            ans.set(e) 
        elif selected_option2.get()=="Dollar":
            e=float(E1.get())*1.08 
            ans.set(e)
        elif selected_option2.get()=="Yuan":
            e=float(E1.get())*7.85
            ans.set(e)
        elif selected_option2.get()=="Rand":
            e=float(E1.get())*20.27 
            ans.set(e)
        elif selected_option2.get()=="Euro":
            e=float(E1.get())
            ans.set(e)
            
    elif selected_option.get()=="Yuan":
        if selected_option2.get()=="Rupees":
            y=float(E1.get())*11.74
            ans.set(y)
        elif selected_option2.get()=="Dollar":
            y=float(E1.get())*0.14 
            ans.set(y)
        elif selected_option2.get()=="Euro":
            y=float(E1.get())*0.13
            ans.set(y)
        elif selected_option2.get()=="Rand":
            y=float(E1.get())*2.58
            ans.set(y)
        elif selected_option2.get()=="Yuan":
            y=float(E1.get())
            ans.set(y)
            
    elif selected_option.get()=="Rand": 
        if selected_option2.get()=="Rupees":
            r=float(E1.get())*4.47
            ans.set(r)
        elif selected_option2.get()=="Dollar":
            r=float(E1.get())*0.054
            ans.set(r)
        elif selected_option2.get()=="Yuan":
            r=float(E1.get())*0.39
            ans.set(r)
        elif selected_option2.get()=="Euro":
            r=float(E1.get())*0.050
            ans.set(r)
        elif selected_option2.get()=="Rand":
            r=float(E1.get()) 
            ans.set(r)     
    


convert_button=tkinter.Button(m,text="Convert",anchor="w",width=21,command=convert,bg="purple",fg="white")
convert_button.grid(row=4,column=0)
convert_button.configure(font = Font_tuple)
clear_button=tkinter.Button(m, text='Clear',anchor="w",width=21,command=clear,bg="purple",fg="white")
clear_button.grid(row=4 ,column=2)
clear_button.configure(font = Font_tuple)
m.mainloop()