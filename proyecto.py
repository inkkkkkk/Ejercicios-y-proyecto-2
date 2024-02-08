nombre = input('¿Cómo te llamas?: ')
ingreso = float(input('¿Cuánto has vendido este mes?:'))
print(f'Estimado/a {nombre}, tu ingreso de este mes ha sido {round(ingreso, 2)}€, y {round(ingreso*0.18, 2)}€ corresponde por la parte de comision.')