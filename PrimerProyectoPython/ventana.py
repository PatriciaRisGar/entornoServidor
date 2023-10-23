from tkinter import *
from tkinter import messagebox
from controlador import ControladorPokemon

controlador = ControladorPokemon()
ventana = Tk()

imagen = controlador.generarPokemonAleatorio()


# Pasar valor cuadroTexto a controlador
def enviarDato():
    pokemonUsu = cuadroTexto.get()

    if controlador.comprobarNombrePokemon(pokemonUsu):
        infoAcierto()
    else:
        infoError()


# Cerrar ventana
def cerrar():
    ventana.destroy()


# Cuando acierta trae otro pokemon
def recargarFrame(imagen):
    fotoLabel.configure(image=imagen)
    fotoLabel.image = imagen
    cuadroTexto.delete(0, END)


# Modal acierto
def infoAcierto():
    messagebox.showinfo("Solución", "Acertaste")
    btonCerrar = Button(ventana, text="Salir del programa", command=cerrar)
    imagen = controlador.generarPokemonAleatorio()
    btonCerrar.pack()
    recargarFrame(imagen)


# Modal error
def infoError():
    messagebox.showwarning("Solución", "Perdiste")
    btonCerrar = Button(ventana, text="Cerrar", command=cerrar)
    btonCerrar.pack()


# Ajustes ventana
ventana.resizable(0, 0)
ventana.title("Pokemon adivino")
ventana.geometry("500x300")


# Crear frame
miFrame = Frame(ventana, padx=20, pady=50)
miFrame.pack()

tituloLabel = Label(miFrame, text="¿Quién es ese pokemon?")
tituloLabel.grid(row=0, column=1)

fotoLabel = Label(miFrame, image=imagen)
fotoLabel.grid(row=1, column=1)

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=3, column=1, padx=150)

boton = Button(ventana, text="Adivinar", command=enviarDato)
boton.pack()


# Ejecutar ventana
ventana.mainloop()
