from django.shortcuts import render
from django.db.models import Count, Sum
from datetime import datetime, timedelta
from datetime import date
from .models import  Item_Factura, Factura
def estadistica(request):
    return render(request, 'estadisticas/estadistica.html')

def estadisticas_meseros(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de meseros
    facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    meseros = (
        facturas.values('mesero__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'estadisticas/meseros.html', {
        'meseros': meseros,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

# Estadísticas de Mesas
def estadisticas_mesas(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de mesas
    facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    mesas = (
        facturas.values('mesa__codigo')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'estadisticas/mesas.html', {
        'mesas': mesas,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

# Estadísticas de Productos
def estadisticas_productos(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de productos
    item_facturas = Item_Factura.objects.filter(factura__fecha__range=[fecha_inicio, fecha_fin])
    productos = (
        item_facturas.values('producto__nombre')
        .annotate(total_vendido=Sum('cantidad'))
        .order_by('-total_vendido')
    )

    return render(request, 'estadisticas/productos.html', {
        'productos': productos,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime, timedelta
from .models import Factura

from datetime import datetime, timedelta
from django.shortcuts import render
from django.db.models import Sum
from .models import Factura

def ventas_totales(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Si no se seleccionan fechas, se usan los valores por defecto (hoy)
    if not fecha_inicio:
        fecha_inicio = datetime.today().strftime('%Y-%m-%d')
    if not fecha_fin:
        fecha_fin = datetime.today().strftime('%Y-%m-%d')

    # Convertir a tipo datetime para poder operar con fechas
    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')

    # Obtener datos de ventas
    facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    total_ventas = facturas.aggregate(total=Sum('total'))['total'] or 0

    # Obtener ventas diarias para el gráfico
    etiquetas = []
    datos = []

    dias_rango = (fecha_fin_dt - fecha_inicio_dt).days + 1
    for i in range(dias_rango):
        dia = fecha_inicio_dt + timedelta(days=i)
        etiquetas.append(dia.strftime('%Y-%m-%d'))
        ventas_dia = Factura.objects.filter(fecha=dia).aggregate(total=Sum('total'))['total'] or 0
        datos.append(ventas_dia)

    return render(request, 'estadisticas/ventas_totales.html', {
        'total_ventas': total_ventas,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'etiquetas': etiquetas,
        'datos': datos,
    })


