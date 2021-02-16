import mysql.connector
import os


class Data:
    def __init__(self):
        self.crear()
        self.conn = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="base_crud"
        )
        self.cursor = self.conn.cursor()

    def crear(self):
        """ Crea la base de datos de nuestra aplicacion, en caso de que ya exista hace la excepcion"""
        try:
            mi_base = mysql.connector.connect(host="localhost", user="root", passwd="")
            mi_cursor = mi_base.cursor()
            mi_cursor.execute("CREATE DATABASE base_crud")

            mi_base = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="base_crud"
            )
            mi_cursor = mi_base.cursor()
            mi_cursor.execute(
                "CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta text COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL  )"
            )
        except:
            print("ya existe")

    def insert(self, elemnt):
        # inserta elemento a la tabla recibiendo como parametro los elementos enviados desde la clase my App
        sql = "INSERT INTO producto(titulo,ruta,descripcion) values(%s,%s,%s)"
        parameters = elemnt
        self.cursor.execute(sql, parameters)
        self.conn.commit()

    def mostrar(self):
        # obtiene todos los elementos de nuestra base de datos con el fetchall
        sql = "SELECT * FROM producto"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete(self, elemnt):
        # Elimina el elemento seleccionado y pasado por parametro desde my App
        dato = elemnt
        sql = "DELETE FROM `producto` WHERE titulo = %s"
        self.cursor.execute(sql, (dato,))
        self.conn.commit()

    def edit(self, elemnt, ref):
        """Edita el elemento seleccionado y pasado por parametro los elementos y
        una referencia del objeto seleccionado desde la clase my App y asignandolo al Query"""
        dato = elemnt
        r = ref
        print(dato, r)
        sql = "UPDATE producto SET titulo = '{}',ruta='{}',descripcion='{}' WHERE titulo='{}'".format(
            elemnt[0], elemnt[1], elemnt[2], ref
        )
        self.cursor.execute(
            sql,
        )
        self.conn.commit()
