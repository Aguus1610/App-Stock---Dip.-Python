from tkinter import Tk
from vista import *
from observador import ConcreteObserverA



class Controlador:
    """
    Esta clase es la principal, la que permite ejecutar la app,
    creando el controlador, inicializando la vista y el observador A.}
    Tambien ejecuta una actualizacion de treeview.
    """
    
    def __init__(self, master):
        self.master_control = master
        self.objeto_vista = Ventana(self.master_control)
        self.observador_a=ConcreteObserverA(self.objeto_vista.objeto_base )
        

        tree = self.objeto_vista.tree
        actualizar_al_inicio = Crud() 
        actualizar_al_inicio.actualizar(tree)    
            

if __name__ == "__main__":
    master_tk = tk.Tk()
    aplicacion = Controlador(master_tk)  


    master_tk.mainloop()

