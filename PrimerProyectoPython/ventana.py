from tkinter import *
from tkinter import messagebox
from controlador import ControladorPokemon

controlador = ControladorPokemon()
ventana = Tk()

controlador.generarPokemonAleatorio()


def enviarDato():
    pokemonUsu = cuadroTexto.get()

    if controlador.comprobarNombrePokemon(pokemonUsu):
        infoAcierto()
    else:
        infoError()


def cerrar():
    ventana.destroy()


def infoAcierto():
    messagebox.showinfo("Solución", "WIN")
    btonCerrar = Button(ventana, text="Cerrar", command=cerrar)
    btonCerrar.pack()


def infoError():
    messagebox.showwarning("Solución", "LOSER")
    btonCerrar = Button(ventana, text="Cerrar", command=cerrar)
    btonCerrar.pack()


# Ajustes ventana
ventana.resizable(0, 0)
ventana.title("Pokemon adivino")


# Crear frame
miFrame = Frame(ventana, width=900, height=800)
miFrame.pack()

tituloLabel = Label(miFrame, text="¿Quién es ese pokemon?", font=("Comic Sans MS", 30))
tituloLabel.grid(row=0, column=1)

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=2, column=1, padx=150)

boton = Button(ventana, text="Adivinar", command=enviarDato)
boton.pack()


# Ejecutar ventana
ventana.mainloop()
