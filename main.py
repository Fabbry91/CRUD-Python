from tkinter import messagebox
from validation import *
from tkinter import ttk
from database import *
from tkinter import *
import random


class App:
    def __init__(self, window):
        self.wind = window
        self.Labels()
        self.Entrada()
        self.Buttons()
        self.Tabla()

    # PINTAR LABES EN LAS VENTANAS
    def Labels(self):
        # Frame
        self.frame = Label(
            self.wind,
            text="Ingrese sus datos",
            background="#9D1EEB",
            fg="white",
            width=75,
        ).grid(padx=0, pady=0, row=0, column=0, columnspan=4)

        # Framejr
        self.frame_jr = LabelFrame(self.wind).grid(
            padx=1, pady=1, row=1, column=0, columnspan=4
        )
        # LAbels
        self.titulo = Label(self.frame_jr, text="Titulo:").grid(row=1, column=0)
        self.ruta = Label(self.frame_jr, text="Ruta:").grid(row=2, column=0)
        self.descripcion = Label(self.frame_jr, text="Descripción:").grid(
            row=3, column=0
        )

    # PINTAR ENTRIES
    def Entrada(self):
        self.titulo = StringVar()
        self.ruta = StringVar()
        self.descri = StringVar()
        self.txt_titulo = Entry(self.wind, textvar=self.titulo).grid(row=1, column=1)
        self.txt_ruta = Entry(self.wind, textvar=self.ruta).grid(row=2, column=1)
        self.txt_descri = Entry(self.wind, textvar=self.descri).grid(row=3, column=1)

    # PINTAR BOTONES
    def Buttons(self):
        self.btn_Guardar = Button(
            self.wind, text="Guardar", command=lambda: self.guardar()
        ).grid(row=4, column=1)
        self.btn_Sorpresa = Button(
            self.wind, text="Sorpresa", command=lambda: self.sorpresa()
        ).grid(row=4, column=2)
        self.btn_Delete = Button(
            self.wind, text="Delete", command=lambda: self.delete()
        ).grid(row=6, column=2)
        self.btn_Edit = Button(
            self.wind, text="Edit", command=lambda: self.edit()
        ).grid(row=6, column=1)

    # PINTAR TABLA

    def Tabla(self):
        # Tabla
        """Se dibuja la tabla en el frame y luego de pintar el formato
        de la tbla se llama al metodo get de la base de datos para pintar
        los datos en filas y colunas"""
        self.tree = ttk.Treeview(self.wind, height=10, columns=(1, 2))
        self.tree.grid(row=5, column=0, columnspan=3)
        self.tree.heading("#0", text="Titulo", anchor=CENTER)
        self.tree.heading("#1", text="Ruta", anchor=CENTER)
        self.tree.heading("#2", text="Descripción", anchor=CENTER)
        self.Get()

    # METODO GET BASE DE DATOS
    def Get(self):
        # limpia table
        """Limpia la tabla de los datos cargados"""
        records = self.tree.get_children()
        for obj in records:
            self.tree.delete(obj)
        # realiza la consulta y pinta los datos nuevamente
        d = Data()
        elemnt = d.mostrar()
        for i in elemnt:
            self.tree.insert("", 0, text=i[1], values=(i[2], i[3]))
            # print(i)

    # METODO ALTA
    def guardar(self):
        """Se llama la funcion validar la cual corrobora que los
        tres input no esten vacios"""
        if self.validar():
            t = self.titulo.get()
            v = Valid()
            aux = v.esAlpha(t)

            """ luego de llamar a la clase valid corrobora que el campotitulo sea alfanumerico
            en caso contrario emite una alerta"""
            if aux == TRUE:
                dato = (self.titulo.get(), self.ruta.get(), self.descri.get())
                print(dato)
                d = Data()
                d.insert(dato)
                self.titulo.set("")
                self.ruta.set("")
                self.descri.set("")
                self.Get()
            else:
                messagebox.showinfo(
                    title="Error", message="El campo titulo tiene que ser Alfanumerico"
                )
        else:
            messagebox.showinfo(
                title="Error", message="Todos los campos son obligatorios"
            )
        self.Get()

    def validar(self):
        """comprueba que los campos no esten vacios"""
        return (
            len(self.titulo.get()) != 0
            and len(self.ruta.get()) != 0
            and len(self.descri.get()) != 0
        )

    # METODO BAJA
    def delete(self):
        try:
            # validmos que se haya seleccionado un elemento de la taabla
            self.tree.item(self.tree.selection())
        except IndexError as e:
            print("error")
            return
        """Llamamos a la clase de base.py y usamos el metodo borrar pasandole por parametro
        el item seleccionado por el nombre text y se indica que el proceso es correcto"""
        d = Data()
        dato = self.tree.item(self.tree.selection())["text"]
        d.delete(dato)
        messagebox.showinfo(
            title="Eliminado", message="Se elimino el dato correctamente"
        )
        self.Get()

    # METODO EDITAR
    def edit_records(self, tittle, new_tittle, new_ruta, new_descrip):
        """metodo editar recibe por parametro los tres input y la referencia del objeto
        a editar, son los parametros que en la clase Data se le asignan al query"""
        d = Data()
        dato = [new_tittle, new_ruta, new_descrip]
        d.edit(dato, tittle)
        self.edit_wind.destroy()
        messagebox.showinfo(
            title="Actualizacion", message="Se actualizo la base de Datos"
        )
        self.Get()

    # SORPRESA
    def sorpresa(
        self,
    ):
        # metodo que selecciona un color a azar para la ventana tkinter
        colors = [
            "blue",
            "red",
            "white",
            "pink",
            "black",
            "purple",
            "#FFFF00",
            "#808000",
            "#00FF00",
        ]
        i = random.choice(colors)
        self.wind.configure(background=i)

    # Seleccion de fila a editar en tabla
    def edit(self):
        """metodo edit nos comprueba que hayamos seleccionado un elemento de la tabla
        al precionar el boton edit se habre una nueva ventana tkinter la cual muesta
        los campos del producto seleccionado e formato solo lectura y nos permite colocar
        los nuevos datos en nuevos input"""
        try:
            self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            messagebox.showinfo(
                title="Seleccion", message="Porfavor seleccione un item de la tabla"
            )
            return

        tittle = self.tree.item(self.tree.selection())["text"]
        ruta = self.tree.item(self.tree.selection())["values"][0]
        descrip = self.tree.item(self.tree.selection())["values"][1]
        self.edit_wind = Toplevel()

        Label(
            self.edit_wind,
            text="Editar datos",
            background="#9D1EEB",
            fg="white",
        ).grid(padx=0, pady=0, row=0, column=1, columnspan=2)

        # Label de datos cargados con el item seleccionado de la tabla
        Label(self.edit_wind, text="Titulo anterior").grid(row=1, column=1)
        Label(self.edit_wind, text="Ruta anterior").grid(row=3, column=1)
        Label(self.edit_wind, text="Descripcion anterior").grid(row=5, column=1)

        # Entries de datos cargados con el item seleccionado de la tabla (solo lectura)
        Entry(
            self.edit_wind,
            textvar=StringVar(self.edit_wind, value=tittle),
            state="readonly",
        ).grid(row=1, column=2)
        Entry(
            self.edit_wind,
            textvar=StringVar(self.edit_wind, value=ruta),
            state="readonly",
        ).grid(row=3, column=2)
        Entry(
            self.edit_wind,
            textvar=StringVar(self.edit_wind, value=descrip),
            state="readonly",
        ).grid(row=5, column=2)

        # Labels de datos nuevos a cargar para editar
        Label(self.edit_wind, text="Nuevo Titulo").grid(row=2, column=1)
        Label(self.edit_wind, text="Nueva Ruta").grid(row=4, column=1)
        Label(self.edit_wind, text="Nueva Descripcion").grid(row=6, column=1)
        new_tittle = StringVar()
        new_ruta = StringVar()
        new_descrip = StringVar()
        self.txt_new_titulo = Entry(self.edit_wind, textvar=new_tittle).grid(
            row=2, column=2
        )
        self.txt_new_ruta = Entry(self.edit_wind, textvar=new_ruta).grid(
            row=4, column=2
        )
        self.txt_new_descrip = Entry(self.edit_wind, textvar=new_descrip).grid(
            row=6, column=2
        )

        # Boton Acturalizar con el metodo de la tabla de datos
        Button(
            self.edit_wind,
            text="Actualizar",
            command=lambda: self.edit_records(
                tittle, new_tittle.get(), new_ruta.get(), new_descrip.get()
            ),
        ).grid(row=7, column=1, columnspan=2)


root = Tk()
root.title("App CRUD")
application = App(root)
root.mainloop()
