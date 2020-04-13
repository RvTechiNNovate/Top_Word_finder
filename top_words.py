from tkinter import *
from tkinter import filedialog
import os
import docxpy as dx
from tkinter import scrolledtext
from tkinter import messagebox
import slate3k as sk
from collections import Counter
import re
    
def top_words(file_path,num):
    pdf=sk.PDF(open(file_path,'rb'))
    list_words=re.findall("\w+",pdf.text())
    ctr=Counter(list_words)
    result=dict()
    result=ctr.most_common(num)
    return result

def reset():
    #reset dir path
    s=entry_dir.get()
    ln=len(s)
    entry_dir.delete(0,ln)
    #reset keyword
    p=entry_key.get()
    ln2=len(p)
    entry_key.delete(0,ln2)
    #reset text box
    text_box.delete('1.0',END)
    
def browse():
    file_path=filedialog.askopenfile()
    entry_dir.insert(0,file_path.name)


def search():
    text_box.place(x=600,y=150)
    try:
        file=entry_dir.get()
        num=int(entry_key.get())
        res=top_words(file,num)
        text_box.delete('1.0',END)
        text_box.configure(fg="black",font=('book antique',15));text_box.insert(END,"    \tWord\tFrequency\n    \t-----------------------------\n")
        for k,v in res:
            text_box.insert(END,f"    \t{k}\t{v}\n")
    except Exception as e:
        messagebox.showinfo("Invalid File","Currupt file or not supported");print(e)
        



root=Tk()

root.state('zoomed')
root.configure(bg='teal')
root.resizable(width=False,height=False)
root.title("My Project2")

lbl_title=Label(root,text='TOP WORDS',font=('cambria',24,'bold','underline'),bg='teal',fg='white')
lbl_title.pack(padx=10)

lbl_dir=Label(root,text="File: ",font=('cambria',14,'bold'),bg='teal',fg='white')
lbl_dir.place(x=70,y=150)

lbl_key=Label(root,text="Topwords: ",font=('cambria',14,'bold'),bg='teal',fg='white')
lbl_key.place(x=50,y=200)

entry_dir=Entry(root,font=('',14),bd=3)
entry_dir.place(x=200,y=150)



entry_key=Entry(root,font=('',14),bd=3)
entry_key.place(x=200,y=200)

btn_brwse=Button(root,command=browse,text=" Browse ",font=('book antiqua',13),bd=5)
btn_brwse.place(x=460,y=150)

btn_srch=Button(root,text=" Search ",command=search,font=('book antiqua',13),bd=3)
btn_srch.place(x=200,y=250)

btn_rst=Button(root,text=" Reset ",command=reset,font=('book antiqua',13),bd=3)
btn_rst.place(x=300,y=250)


text_box=scrolledtext.ScrolledText(root,width=35,height=20,font=('',10))


root.mainloop()

