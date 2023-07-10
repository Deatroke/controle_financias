from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Controle de Finanças")

frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Controle Financeiro").grid(column=1, row=0)

ttk.Label(frm, text="Entrada ").grid(column=0, row=1)
ttk.Label(frm, text="Saída ").grid(column=1, row=1)
ttk.Label(frm, text="Total").grid(column=2, row=1)

ttk.Label(frm, text="Opções:").grid(column=1, row=2)
ttk.Button(frm, text="Entrada", command=root.destroy).grid(column=0, row=3)
ttk.Button(frm, text="Saída", command=root.destroy).grid(column=1, row=3)
ttk.Button(frm, text="Histórico", command=root.destroy).grid(column=2, row=3)

root.mainloop()