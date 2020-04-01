convertirMeses = {
    'Ene': 'Enero',
    'Feb': 'Febrero',
    'Mar': 'Marzo',
    'Abr': 'Abril',
    'May': 'Mayo',
    'Jun': 'Junio',
    'Jul': 'Julio',
    'Ago': 'Agosto',
    'Sep': 'Septiembre',
    'Oct': 'Octubre',
    'Nov': 'Noviembre',
    'Dic': 'Diciembre'
}

print(convertirMeses['Mar'])
print(convertirMeses.get('Dic', 'No es valido...'))
