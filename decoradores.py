from tkinter import messagebox
import functools
from datetime import *

def contar_llamadas(func, archivo= "llamadas de funciones.txt"):
    """
    Este metodo crea un decorador para contar las llamadas de funciones y 
    crear un registro en un archivo de texto.
    """
    @functools.wraps(func)
    def wrapper_contar_llamadas(*args, **kwargs):
        wrapper_contar_llamadas.llamadas += 1
        texto = '######### NUEVA LLAMADA A FUNCIÓN: '+ func.__name__ +' #########'
        print(texto ,end='!\n')
        fecha=datetime.now().strftime("%d/%m/%Y %H:%M")
        print('Llamada número %s a la función %s' % (wrapper_contar_llamadas.llamadas, func.__name__))
        with open(archivo, 'a') as f:
                f.write(f"Llamada numero {wrapper_contar_llamadas.llamadas} a la funcion {str.upper(func.__name__)} --- HORA: {fecha} \n")
        return func(*args, **kwargs)
    
    wrapper_contar_llamadas.llamadas = 0
    return wrapper_contar_llamadas

def decorador_limpiar_campos(funcion):
    """
    Este es el metodo del decorador para limpiar campos
    """
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        print("------- CAMPOS VACIOS -------")
        messagebox.showinfo("Campos vacios", "Los campos estan vacios.")
        return funcion(*args, **kwargs)
    return wrapper

def decorador_leer(funcion):
    """
    Este es el metodo del decorador para mostrar
    """
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        confirm= messagebox.askyesno("Leer", "Al leer el proyecto se rellenaran los campos con los datoss. ¿Desea leer el proyecto?")
        if confirm == "yes":
            print("------- LEER -------")
        return funcion(*args, **kwargs)   
    return wrapper


# Función para cambiar el tema con decorador

