from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre

class Item_Factura(models.Model):
    subtotal = models.FloatField()
    cantidad = models.IntegerField()
    producto= models.ForeignKey(Producto, related_name='item_factura', on_delete=models.CASCADE)

    def _str_(self):
        return self.producto.nombre

    def calcular_subtotal(self):
        return self.cantidad * self.producto.precio

    def calcular_total(self):
        return self.subtotal

class Factura(models.Model):
    numero= models.CharField(max_length=20)
    fecha = models.DateField()
    impuesto= models.FloatField()
    descuento = models.FloatField()
    total= models.FloatField()

    item_factura_list = models.ForeignKey(Item_Factura, related_name='factura', on_delete=models.CASCADE)

    def _str_(self):
        return self.numero

    def calcular_impuesto(self):
        return Item_Factura.subtotal*Factura.impuesto

    def calcular_descuento(self):
        return Item_Factura.subtotal*Factura.descuento

    def calcular_total(self):
        return Item_Factura.subtotal + self.calcular_impuesto() - self.calcular_descuento()



class Mesa(models.Model):
    cantidad_uso = models.IntegerField()
    codigo = models.CharField(max_length=20)

    def _str_(self):
        return self.codigo

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre

class Mesero(Persona):
    pedidosAtentidos = models.IntegerField()

    def actualizar_pedidos_atendidos(self):
        return self.pedidosAtentidos + 1

class Estadistica(models.Model):
    titulo= models.CharField(max_length=50)

class estadistica_mesero(Estadistica):
    mejor_mesero = models.CharField(max_length=50)

class estadistica_mesa(Estadistica):
    mesa_mas_usada = models.CharField(max_length=50)

class estadistica_producto(Estadistica):
    producto_mas_vendido = models.CharField(max_length=50)

class Reporte(models.Model):
    titulo = models.CharField(max_length=50)
    estadistica_list = models.CharField(max_length=200)

    class TipoReporte(models.TextChoices):
        DIARIO = 'DIARIO'
        SEMANAL = 'SEMANAL'
        MENSUAL = 'MENSUAL'

    class TipoArchivo(models.TextChoices):
        PDF = 'PDF'
        IMAGEN = 'IMAGEN'

class Grafico(models.Model):
    titulo = models.CharField(max_length=50)