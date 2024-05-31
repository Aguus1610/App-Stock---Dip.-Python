from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from modelo import *
from base_datos import *
from ttkthemes import ThemedStyle
from modelo import Crud
from observador import *	
from decoradores import *
from functools import *

class Ventana:
    """
    Esta clase sirve para agrupar todos los elementos de la interfaz gráfica, 
    sinedo algunos los label, entry, botones, menú, etc.
    Utiliza la clase Crud para manipular los datos en la base de datos.  
    Se crea un treeview para poder visualizar los datos cargados a la base de datos.
    Ademas posee "ttkthemes" para seleccionar un tema que personalice la ventana.

    """
    

    def __init__(self, master_tk):

        # -------------- Titulo y ventana ---------------------------------------------------------------


        self.master = master_tk
        self.master.title("Control de Stock")
        self.master.geometry("1000x500")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.objeto_base=Crud()
        self.objeto_vista=FuncionesVentana()
        db.create_tables([Producto])

        # Variables de control para los Entry widgets

        self.nombre_var = StringVar()
        self.precio_var = IntVar()
        self.cantidad_var = IntVar()
        self.categorias = StringVar()
        self.medida = StringVar()

    
        # -------------- Menu ---------------------------------------------------------------

        menubar=tk.Menu(self.master)
        menuotros=tk.Menu(menubar, tearoff=0)
        
        menuotros.add_command(label="Vaciar Base de Datos", command=lambda:self.objeto_vista.vaciar_base_datos())
        menuotros.add_command(label="Salir", command=lambda:self.objeto_vista.salir_aplicacion(self.master))
        menubar.add_cascade(label="Otros",menu=menuotros )

        menubase=tk.Menu(menubar, tearoff=0)
        menubase.add_command(label="Borrar campos", command=lambda:self.objeto_vista.limpiar_campos())
        menubar.add_cascade(label="Campos de Datos",menu=menubase )

        self.master.config(menu=menubar)

        # ---------------------- Frame comandos ----------------------------------------------------

        miFrame = Frame(self.master)
        miFrame.grid(row=0, column=0, rowspan=2, columnspan=1, pady=2, padx=2)        


        # ---------------------- Entry con label y label de medida y categoria ----------------------------------------------------

  
        # Etiquetas y Entry para ingresar datos
        self.label_1 = ttk.Label(miFrame, text="Nombre:").grid(row=1, column=0, padx=3, pady=4, sticky="w")
        self.nombre_entry = tk.Entry(miFrame, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=1, column=1, padx=3, pady=4, sticky="w")
        
        self.label_2=ttk.Label(miFrame, text="Precio:").grid(row=2, column=0, padx=3, pady=4, sticky="w")
        self.precio_entry = tk.Entry(miFrame, textvariable=self.precio_var)
        self.precio_entry.grid(row=2, column=1, padx=3, pady=4, sticky="w")

        self.label_3=ttk.Label(miFrame, text="Cantidad:").grid(row=3, column=0, padx=3, pady=4, sticky="w")
        self.cantidad_entry = tk.Entry(miFrame, textvariable=self.cantidad_var)
        self.cantidad_entry.grid(row=3, column=1, padx=3, pady=4, sticky="w")

        self.medida_combox=ttk.Label(miFrame, text="Medida:").grid(row=1, column=2, padx=3, pady=4, sticky="w")

        self.cateorias_combox=ttk.Label(miFrame, text="Elegir categoria del producto").grid(row=2, column=2, padx=2, pady=4, sticky="w")


        # ---------------------- Combox de medida, categoria y tema ----------------------------------------------------

        # Caegorias de producto

        categorias = ["Terminal giratorio macho", "Terminal giratorio Hembra", "Terminal virola macho", "Terminal virola Hembra","Manguera R2", "Manguera R4", "Manguera Aislada", "Otro"]
        self.cuadroCategoria = ttk.Combobox(miFrame, values=categorias, textvariable=self.categorias)
        self.cuadroCategoria.grid(row=2, column=3, padx=3, pady=4)

        # Combox y Temas

        self.estilo = ThemedStyle(self.master)

        # Obtener la lista de temas disponibles

        temas_disponibles = self.estilo.theme_names()
        self.combo_theme = ttk.Combobox(miFrame, values=temas_disponibles)
        self.combo_theme.grid(row=6, column=0, padx=3, pady=10)
        self.combo_theme.current(0) 

        # Medida de producto

        medidas = ["1/2", "1/4", "3/8", "1","2"]
        self.cuadro_medida = ttk.Combobox(miFrame, values=medidas, textvariable=self.medida)
        self.cuadro_medida.grid(row=1, column=3, padx=3, pady=4)


        # ---------------------- Treeview ----------------------------------------------------


        self.tree = ttk.Treeview(miFrame, columns=("ID", "Nombre","Categoria", "Medida", "Precio", "Cantidad", "Valor", "Fecha"), show="headings")
        self.tree.column("ID", width=90, minwidth=50, anchor= W)
        self.tree.column("Nombre", width=100, minwidth=100)
        self.tree.column("Categoria", width=100, minwidth=100)
        self.tree.column("Medida", width=100, minwidth=100)
        self.tree.column("Precio", width=100, minwidth=100)
        self.tree.column("Cantidad", width=100, minwidth=100)
        self.tree.column("Valor", width=100, minwidth=100)
        self.tree.column("#0", width=100, minwidth=100, anchor=E)
        # Encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre", command=lambda: Crud.sort_treeview(self.tree, "Nombre", False))
        self.tree.heading("Categoria", text="Categoria", command=lambda: Crud.sort_treeview(self.tree, "Categoria", False))
        self.tree.heading("Medida", text="Medida", command=lambda: Crud.sort_treeview(self.tree, "Medida", False))
        self.tree.heading("Precio", text="Precio", command=lambda: Crud.sort_treeview(self.tree, "Precio", False))
        self.tree.heading("Cantidad", text="Cantidad", command=lambda: Crud.sort_treeview(self.tree, "Cantidad", False))
        self.tree.heading("Valor", text="Valor", command=lambda: Crud.sort_treeview(self.tree, "Valor", False))
        self.tree.heading("Fecha", text="Fecha", command=lambda: Crud.sort_treeview(self.tree, "Fecha", False))
        self.tree.grid(row=5, column=0, columnspan=5, padx=3, pady=5)

        # ---------------------- Botones ----------------------------------------------------

        self.boton_crear=ttk.Button(miFrame, text="Crear Registro",  command=lambda:self.objeto_base.crear(self.tree, self.nombre_var.get(), self.categorias.get(), self.medida.get(), self.precio_var.get(), self.cantidad_var.get())).grid(row=4, column=0, padx=3, pady=4)
        self.boton_actual=ttk.Button(miFrame, text="Actualizar Vista", command=lambda:self.objeto_base.actualizar(self.tree)).grid(row=4, column=1, padx=3, pady=4)
        self.boton_modif=ttk.Button(miFrame, text="Modificar", command=lambda:self.objeto_base.modificar(self.tree, self.nombre_var.get(), self.categorias.get(), self.medida.get(), self.precio_var.get(), self.cantidad_var.get())).grid(row=4, column=2, padx=3, pady=4)
        self.boton_baja=ttk.Button(miFrame, text="Eliminar", command=lambda:self.objeto_base.eliminar(self.tree)).grid(row=4, column=3, padx=3, pady=4)
        self.boton_mostrar=ttk.Button(miFrame, text="Mostrar", command=lambda:FuncionesVentana.leer_producto(self, self.tree)).grid(row=4, column=4, padx=3, pady=4)

        self.boton_cambiar_tema = ttk.Button(miFrame, text="Cambiar Tema", command=lambda:cambiar_tema(self, self.master)).grid(row=7, column=0, padx=3, pady=5)

        # ---------------------- Funcion cambiar tema y decorador ----------------------------------------------------


        def decorador_cambiar_tema(funcion):
            @functools.wraps(funcion)
            def wrapper(*args, **kwargs):
                messagebox.askquestion("Cambiar tema", "¿Desea cambiar el tema?")
                texto = '######### LA VENTANA CAMBIO DE TEMA: '+ self.combo_theme.get() +' #########'
                print(texto ,end='!\n')
                return funcion(*args, **kwargs)
            return wrapper
        
        @decorador_cambiar_tema
        def cambiar_tema(self, master):
            tema_seleccionado = self.combo_theme.get()
            self.estilo.theme_use(tema_seleccionado)
            self.actualizar_fondo=miFrame.configure(bg=self.colores_fondo.get(tema_seleccionado, "white"))
            self.actualizar_fondo=master.configure(bg=self.colores_fondo.get(tema_seleccionado, "white"))




        # ---------------------- Colores de fondo ----------------------------------------------------


    colores_fondo = {
                "clam": "#dbdbdb",
                "alt": "#f0f0f0",
                "default": "#f0f0f0",
                "classic": "#d9d9d9",
                "winnative": "#ececec",
                "vista": "#d2d2d2",
                "xpnative": "#d2d2d2",
                "aquativo": "#d6e9f8",
                "arc": "#dae3f0",
                "black": "#b5b5b5",
                "blue": "#c8d7e1",
                "clearlooks": "#e5e5e5",
                "keramik": "#dcdcdc",
                "plastik": "#f5f5f5",
                "radiance": "#ededed",
                "scid themes": "#f4f4f4",
                "breeze": "#deeaf5",
                "equilux": "#2c3e50",
                "kroc": "#ff6961",
                "scid": "#ffdd54",
                "adapta": "#b8c9ff",
                "breeze-dark": "#232629",
                "blue": "#007bff",
                "dark": "#2c3e50",
                "elegance": "#ececec",
                "itft1": "#f5f5f5",
                "plastic": "#f0f0f0",
                "winxpblue": "#ffffff",
                "vista": "#d2d2d2"
                # Puedes agregar más temas y colores aquí
            }



    


class FuncionesVentana:
    """
    Esta clase contiene las funciones de la ventana, excepto la de cambiar tema.
    Cada funcion tiene como decorador "contar_llamadas" para contar las llamadas de la funcion.
    Ademas algunos poseen decoradores propios de la funcion.
    """

    def salir_aplicacion(self, master): 
        """
        Este metodo se encargar de cerrar la aplciacion y la conexion con la base.
        Ademas notifica al observador A
        """
        valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
        if valor=="yes":
            db.close()
            master.destroy()

    
    @contar_llamadas
    @decorador_limpiar_campos
    def limpiar_campos(self):
        """
        Esta funcoin vacia los campos.
        """
        self.nombre_var.set("")
        self.precio_var.set("")
        self.cantidad_var.set("")

   

    @contar_llamadas
    def vaciar_base_datos(self):
        """
        Este metodo permite vaciar por completo la tabla de la base de datos
        """
        confirm=messagebox.askquestion("Salir","¿Desea eliminar el contenido de la base de datos?")
        if confirm=="yes":
            try:
                with db.atomic():
                    # Obtener todos los registros de la tabla
                    registros = Producto.select()
    
                # Eliminar cada registro uno por uno
                for registro in registros:
                    registro.delete_instance()
                messagebox.showinfo("Base de datos", "Base de datos vaciada")
                Crud.actualizar(self, self.tree)
                print("Base de datos vaciada correctamente.")
            except DoesNotExist:
                print("La tabla está vacía o no existe.")


    @contar_llamadas
    @decorador_leer
    def leer_producto(self, tree):
        """
        Esta funcion muestra la informacion de un producto seleccionado
        del treeview y rellena los campos entry con la informacion
        de este producto.
        """
        producto = tree.selection()
        if producto:
            self.item = tree.item(producto)
            producto_seleccionado = tree.item(producto, "values" )
            self.nombre_entry.delete(0,tk.END)
            self.precio_entry.delete(0,tk.END)
            self.cantidad_entry.delete(0,tk.END)
            self.nombre_entry.insert(0, producto_seleccionado[1])
            self.precio_entry.insert(0, producto_seleccionado[4])
            self.cantidad_entry.insert(0, producto_seleccionado[5])

            mensaje = {"ID ": producto_seleccionado[0],
                "NOMBRE ": producto_seleccionado[1],
                "CATEGORIA ": producto_seleccionado[2],
                "MEDIDA ": producto_seleccionado[3],
                "PRECIO ": producto_seleccionado[4],
                "CANTIDAD ": producto_seleccionado[5],
                "VALOR ": producto_seleccionado[6],
                "FCHA DE INGRESO": producto_seleccionado[7]
            }
            contenido = "\n".join([f"{clave}: {valor}" for clave, valor in mensaje.items()])
            messagebox.showinfo("Producto Seleccionado", contenido)
            print("Campos completos")
            
        else:
            messagebox.showwarning("Error", "Por favor, seleccione un producto de la lista.")

    

        

            


 

    











