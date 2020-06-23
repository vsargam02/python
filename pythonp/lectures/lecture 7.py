#lamba function
# twice= lambda x  :2*x
# print(twice(5))



#from tkinter import*        #  * is everything
import tkinter



import tkinter as tk     #alias
# def handleClick():
#     strVar.set(strVar2.get())
#
# window=tk.Tk()
# tk.Label(window, text='coding').pack()
#
# strVar2 = tk.StringVar()
# tk.Entry(window, textvariable= strVar2).pack()
#
# tk.Button(window,text='Click Me',command=handleClick).pack()
#
# strVar=tk.StringVar()
# tk.Label(window,textvariable=strVar).pack()
#
# window.mainloop()

command=lambda: handleClick(7)


#CALCULATOR
def handleClick(btnVal):
    curr = strVar.get()
    if btnVal == '=':
        strVar.set(eval(curr))
    else:

        strVar.set(curr+ btnVal)

window = tk.Tk()
window.title('calculator')
strVar=tk.StringVar()
tk.Label(window, textvariable= strVar).grid(row=0,column=0,columnspan=4)
tk.Button(window, text='7',command=lambda:handleClick('7'),width=5,height=2).grid(row=1,column=0)
tk.Button(window, text='8',command=lambda:handleClick('8'),width=5, height=2).grid(row=1,column=1)
tk.Button(window, text='9',command=lambda:handleClick('9'), width=5, height=2).grid(row=1,column=2)
tk.Button(window, text='/',command=lambda:handleClick('/'), width=5, height=2).grid(row=1,column=3)

tk.Button(window, text='4',command=lambda:handleClick('4'), width=5, height=2).grid(row=2,column=0)
tk.Button(window, text='5',command=lambda:handleClick('5'), width=5, height=2).grid(row=2,column=1)
tk.Button(window, text='6',command=lambda:handleClick('6'), width=5, height=2).grid(row=2,column=2)
tk.Button(window, text='*',command=lambda:handleClick('*'), width=5, height=2).grid(row=2,column=3)

tk.Button(window, text='1',command=lambda:handleClick('1'), width=5, height=2).grid(row=3,column=0)
tk.Button(window, text='2',command=lambda:handleClick('2'), width=5, height=2).grid(row=3,column=1)
tk.Button(window, text='3',command=lambda:handleClick('3'), width=5, height=2).grid(row=3,column=2)
tk.Button(window, text='-',command=lambda:handleClick('-'), width=5, height=2).grid(row=3,column=3)

tk.Button(window, text='.',command=lambda:handleClick('.'), width=5, height=2).grid(row=4,column=0)
tk.Button(window, text='0',command=lambda:handleClick('0'), width=5, height=2).grid(row=4,column=1)
tk.Button(window, text='=',command=lambda:handleClick('='), width=5, height=2).grid(row=4,column=2)
tk.Button(window, text='+',command=lambda:handleClick('+'), width=5, height=2).grid(row=4,column=3)

window.mainloop()












