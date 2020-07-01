from tkinter import *
def imagen():
    ventana=Tk()
    ventana.title("wey ya")
    ventana.resizable(False,False)
    ventana.geometry("300x280")
    ventana.config(bg="light steelblue")
    ventana.attributes('-topmost', True)
    ventana.update()
    ventana.attributes('-topmost', False)
    image=PhotoImage(file="wey ya.gif")
    image=image.subsample(3,3)
    label=Label(image=image)
    label.pack()    
    ventana.mainloop()

def mensaje_error():
    ventana=Tk()
    ventana.title("Error")
    ventana.resizable(False,False)
    ventana.geometry("250x75")
    ventana.config(bg="light steelblue")
    ventana.attributes('-topmost', True)
    ventana.update()
    ventana.attributes('-topmost', False)
    #etiqueta#
    el=Label(ventana,text="Los valores ingresados no son correctos",bg="deep skyblue2",fg="black")
    el.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=X)
    def salida():
        ventana.destroy()
    #boton#
    boton=Button(ventana, text = "Aceptar", command=salida).place(x=100,y=42)
    #ventana siempre abierta#
    ventana.mainloop()