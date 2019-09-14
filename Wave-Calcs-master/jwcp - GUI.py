#Stephen Duncanson
#Wave calc program for Jill
#jwcp

import math
import tkinter as tk
from tkinter import ttk

G = 32.1719 #ft/s^2

def k_solve():
    t_0 = float(t_0_entry_var.get())
    d = float(d_entry_var.get())

    #calculate an initial guess
    k_0 = ((2*math.pi)**2)/(G*(t_0**2))
    k = k_0

    #Use guess to calculate t value
    t_1 = (2*math.pi)/(math.sqrt(G*k_0*math.tanh(k_0*d)))

    #calculate error
    e = (math.fabs(t_1 - t_0))/t_0

    iter_counter = 0
    
    while e > 0.001:
        iter_text.configure(text="k = "+format(k,".4f")+", e = "+format(e,'.5f')+" iterating...")
        root.update()
    if t_1 < t_0:
        k = k-.1*e
        iter_counter +=1 
    elif t_1 > t_0:
        k = k+.1*e
        iter_counter +=1 
    #since I cant rename vars, t1 is current t_0 is old always
    t_0 = t_1    
    t_1 = (2*math.pi)/(math.sqrt(G*k*math.tanh(k*d)))
    e = (math.fabs(t_1-t_0))/(t_0)

    if iter_counter > 10000:
        root.destroy 
    iter_text.set(iter_text.get+"\nK = "+str(k))
    iter_text.set(iter_text.get+"\nError = "+str(e))


root = tk.Tk()                              #Create the window 
root.title("jwcp - Jill's Wave Calc Program")



t_0_label = tk.Label(root, text="t (sec)")
d_label = tk.Label(root, text="d (ft)")
t_0_label.grid(column=1,row=0,sticky=tk.E)
d_label.grid(column=1,row=1,sticky=tk.E)


t_0_entry_var = tk.StringVar()
t_0_entry_var = tk.Entry(root,textvariable=t_0_entry_var)
t_0_entry_var.config(font=("Consolas",10))
t_0_entry_var.grid(column=2,row=0,sticky=tk.W+tk.E)

d_entry_var = tk.StringVar()
d_entry_var = tk.Entry(root,textvariable=d_entry_var)
d_entry_var.config(font=("Consolas",10))
d_entry_var.grid(column=2,row=1,sticky=tk.W+tk.E)

k_button = tk.Button(root,text='Solve k',command=k_solve)#,command=
k_button.grid(row=2,column=1,columnspan=2,sticky=tk.W+tk.E,ipadx=2,ipady=2,padx=2,pady=2)

iter_frame = tk.Frame(root)
iter_frame.grid(column=1,row=3,columnspan=2,rowspan=2,sticky=tk.E)

iter_text = tk.Label(iter_frame, text="")
iter_text.grid(column=1,row=0,sticky=tk.E)


root.mainloop()





