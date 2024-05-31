import re
from peewee import *
from tkinter import messagebox
from datetime import datetime
from base_datos import *
from decoradores import *
from observador import Subject



class Crud(Subject):
    """
    Esta clase permite crear, eliminar y modificar datos en la base utilizando peewee,
     y ademas permite mostrarlos en un Treeview.
    Contiene las funciones: crear, actualizar, eliminar modificar. 
    Todas poseen un decorador @contar_llamadas.
    
    """
    

    @contar_llamadas
    def crear(self, mi_tree, nombre, categoria, medida, precio, cantidad):
        """
        Este metodo crea un nuevo registro en la base de datos, si el nombre del producto es valido, 
        tomando la informacion desde los entry y de los comboxes.
        Ademas, se crea una nueva instancia de la clase Subject, para notificar al observador.
        """
        valor = int(precio * cantidad) 

        # Validar el nombre con expresiones regulares
        if not re.match("^[a-z, ,A-Z]+$", nombre):
            messagebox.showwarning("Error", "El nombre del producto solo debe contener letras.")
            return
        
        if nombre and precio and cantidad != " ":
            self.fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            producto=Producto()
            producto.nombre=nombre
            producto.categoria=categoria
            producto.medida=medida
            producto.precio=precio
            producto.cantidad=cantidad
            producto.valor=valor
            producto.fecha_in=self.fecha_actual
            producto.save()
            
            self.notificar("Registrado: ", nombre, cantidad)
            Crud.actualizar(self, mi_tree)
            messagebox.showinfo("Éxito", "Producto creado correctamente.")

            
        else:
            messagebox.showwarning("Error", "Por favor, ingrese todos los campos.")

    @contar_llamadas
    def actualizar(self, mi_tree):
        """
        Esta funcion actualiza la vista del treeview cargando los datos de la base.
        """

        # Limpiar el Treeview antes de cargar los nuevos datos
        records=mi_tree.get_children()
        for element in records:
            mi_tree.delete(element)

        for filas in Producto.select():
                mi_tree.insert("", 0, text=filas.id, values=(filas.id, filas.nombre, filas.categoria, filas.medida, filas.precio, filas.cantidad, filas.valor, filas.fecha_in))

        if records == " ":
            messagebox.showwarning("Error", "No hay datos en la base de datos.")

        if records != " ":
            self.notificar(self)    


 

    @contar_llamadas
    def eliminar(self, mi_tree):
        """
        Este metodo elimina un registro de la base de datos, 
        tomando el elemento seleccionado del Treeview.
        Ademas, se crea una nueva instancia de la clase Subject,
        para notificar al observador.
        """
        elemento_seleccionado = mi_tree.selection()
        if elemento_seleccionado:
            # Eliminar el producto seleccionado
            id_seleccionado = mi_tree.item(elemento_seleccionado, 'values')[0]
            categoria_seleccionado = mi_tree.item(elemento_seleccionado, 'values')[2]
            borrar = Producto.get(Producto.id == id_seleccionado)
            borrar.delete_instance()
            self.notificar("Eliminado: ", categoria_seleccionado)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            Crud.actualizar(self, mi_tree)
            
        else:
            messagebox.showwarning("Error", "Seleccione un producto para eliminar.")


    @contar_llamadas
    def modificar(self, mi_tree, nombre, categoria, medida, precio, cantidad):
        """
        Este metodo modifica un registro de la base de datos, 
        tomando el elemento seleccionado del Treeview.
        Ademas, se crea una nueva instancia de la clase Subject, 
        para notificar al observador.
        """

        if not nombre or not precio or not cantidad:
            messagebox.showwarning("Error", "Por favor, complete todos los campos.")
            return

        valor = int(precio * cantidad) 
        elemento_seleccionado = mi_tree.selection()
        if not elemento_seleccionado:
            messagebox.showwarning("Error", "Seleccione un producto para actualizar.")
            return

        id_seleccionado = mi_tree.item(elemento_seleccionado, 'values')[0]

        try:
            self.fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            modificar = Producto.update({Producto.nombre:nombre, Producto.categoria:categoria, Producto.medida:medida, Producto.precio:precio, Producto.cantidad:cantidad, Producto.valor:valor, Producto.fecha_in:self.fecha_actual}).where(Producto.id == id_seleccionado)
            modificar.execute()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            Crud.actualizar(self, mi_tree)
            self.notificar(self, "Actualizado: ", nombre)
        except SyntaxError:
            messagebox.showinfo("ERROR", "Hay un error de tipo 'SyntaxError' ")
        except ValueError:
            messagebox.showinfo("ERROR", "Hay un error de tipo 'ValueError' ") 


    @contar_llamadas
    def sort_treeview(tv, col, reverse):
        data = [(tv.set(child, col), child) for child in tv.get_children('')]
        data.sort(reverse=reverse)
        for index, item in enumerate(data):
            tv.move(item[1], '', index)
        tv.heading(col, command=lambda: Crud.sort_treeview(tv, col, not reverse))




