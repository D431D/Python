from Tkinter import *

def funcion():
   v.set("David")
def imprimir():	
	print 'hola '+textNombre.get()+' '+textApellido.get()+' Vives en: '+textDomicilio.get()

v0 = Tk() # Tk() Es la ventana principal
frame = Frame()
v = StringVar()
frame.config(bg="black") # Le da color al fondo

labelNombre=Label(frame, text="Nombre")
labelNombre.config(bg = 'green') #color al label
textNombre = Entry(frame)
textNombre.config(bg = 'blue') #color al area de texto

labelApellido = Label(frame, text="Apellidos")
textApellido = Entry(frame)

labelDomicilio = Label(frame, text="Domicilio")
textDomicilio = Entry(frame)

button=Button(frame, text="hola", command=imprimir)


button.pack(side=BOTTOM)

labelNombre.pack()
textNombre.pack()

labelApellido.pack()
textApellido.pack()

labelDomicilio.pack()
textDomicilio.pack()
frame.pack()
frame.mainloop()

"""
from Tkinter import * 
v0 = Tk() # Tk() Es la ventana principal
v1=Toplevel(v0) # Crea una ventana hija

def mostrar(ventana): ventana.deiconify()
def ocultar(ventana):ventana.withdraw()
def ejecutar(f): v0.after(200,f)

v0.config(bg="black") # Le da color al fondo
v0.geometry("500x500")

b1=Button(v0,text="ABRIR VENTANA V1",command=lambda: ejecutar(mostrar(v1))) 
b1.grid(row=1,column=1)
b2=Button(v0,text="OCULTAR VENTANA V1",command=lambda: ejecutar(ocultar(v1))) 
b2.grid(row=1,column=2)

v1.withdraw()
v0.mainloop()*"""
