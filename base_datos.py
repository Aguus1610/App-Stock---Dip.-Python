from peewee import *


db = SqliteDatabase("Stock.db")
class BaseModel(Model):
    """
    Clase base para la base de datos con peewee.
    """
    class Meta:
        """
        Meta clase para la base de datos con peewee.
        """
        database = db
class Producto(BaseModel):
    """
    Clase que define las columnas de la tabla "productos" en la base de datos.
    """
    id = AutoField(primary_key=True)
    nombre = CharField(unique=True)
    categoria = CharField()
    medida = CharField()
    precio = CharField()
    cantidad = CharField()
    valor = IntegerField()
    fecha_in = DateTimeField()


