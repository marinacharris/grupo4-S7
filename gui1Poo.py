import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk() #Tk, ventana
        self.ventana1.title('Mini Calc')
        self.num1= tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana1,width=20, textvariable=self.num1) #Entry, caja de texto
        self.entrada1.grid(column=0,row=0)
        self.num2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana1,width=20, textvariable=self.num2)
        self.entrada2.grid(column=1, row=0)
        self.opcion = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana1, text='Suma', value=1, variable=self.opcion)
        self.radio1.grid(column=0,row=1)
        self.radio2 = tk.Radiobutton(self.ventana1, text= 'Resta', value=2, variable =self.opcion)
        self.radio2.grid(column=1,row=1)
        self.boton1 = tk.Button(self.ventana1, text='Operar', command=self.operaciones)
        self.boton1.grid(column=0, row=2)
        self.etiqueta1 = tk.Label(self.ventana1,text='--')
        self.etiqueta1.grid(column=1, row=2)
        self.ventana1.mainloop()
    
    def operaciones(self):
        if self.opcion.get()==1:
            op = float(self.num1.get())+float(self.num2.get())
            self.etiqueta1['text']=op
        if self.opcion.get()==2:
            op = float(self.num1.get())-float(self.num2.get())
            self.etiqueta1['text']=op
            
        
        
x = Aplicacion()
        
        