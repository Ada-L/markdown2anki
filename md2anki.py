#!F:/python
# coding: utf-8



import pandas as pd
import re
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import re
import pandas as pd
import tkinter.messagebox

def rep(sym,s):
    while sym in s:
        s=s.replace(sym,'[]',1).replace(sym,'[/]',1)
        rep(sym,s)
    #news=s.replace('[]','[$]').replace('[/]','[/$]')
    return s

def testbank2anki():
    name=tkinter.filedialog.askopenfilename()
    f=open(name,'r',encoding='utf-8')
    lines=f.read()
    #replace mathblocks
    lines=rep('> $$',lines)
    lines=rep('$$',lines)
    lines=rep('$',lines)
    lines=lines.replace('[]','[$]').replace('[/]','[/$]')
    #replace clozes
    lines=lines.replace('<u>','{{c1::').replace('</u>','}}')
    #replace titles
    lines=lines.replace('#','').replace('\n\n','\n')
    #split by the line
    lines=lines.split('---\n')
    #Q&A
    question=lines[0::2]
    answer=lines[1::2]
    #export
    dataframe=pd.DataFrame(dict(a=question, b=answer))
    dataframe.to_csv(name+'.csv', header=False, index=False,sep=',')
    tk.messagebox.showinfo(message='OK!')

def md2anki():
    name=tkinter.filedialog.askopenfilename()
    f=open(name,'r',encoding='utf-8')
    lines=f.read()
    #replace mathblocks
    lines=rep('> $$',lines)#when quoted
    lines=rep('$$',lines)
    lines=rep('$',lines)
    lines=lines.replace('[]','[$]').replace('[/]','[/$]')
    #replace clozes
    lines=lines.replace('<u>','{{c1::').replace('</u>','}}')
    #split to list
    lines=lines.split('\n\n')
    lines.append('#')
    #index to record the para nums
    ind1=[]
    ind2=[]
    #question list
    question=[]
    for i in range(1,len(lines)-1):
        if lines[i].count('#')==0 and lines[i-1].count('#')!=0:
            ind1.append(i)
            question.append(lines[i-1].replace('#',''))
        if lines[i].count('#')==0 and lines[i+1].count('#')!=0:
            ind2.append(i)
        
    answer=[]
    for i in range(len(ind1)):
        ans=''
        for j in range(ind1[i],ind2[i]+1):
            ans=ans+lines[j]+'\n'
        answer.append(ans)
    #export
    dataframe=pd.DataFrame(dict(a=question, b=answer))
    dataframe.to_csv(name.replace('.md','')+'.csv', header=False, index=False,sep=',')
    tk.messagebox.showinfo(message='OK!')


root = Tk()  # base window

mdbutton = Button(text="markdown",fg='red',command=md2anki)
mdbutton.pack()
testbankbutton = Button(text="testbank",fg='red',command=testbank2anki)
testbankbutton.pack()

root.mainloop()
