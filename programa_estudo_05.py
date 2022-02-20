# escreva um programa que leia a distancia de uma viajem calcule:
# em KILOMETROS, HEQUITOMETROS, DECAMETROS, DECIMETROS, CENTIMETROS, MILIMETROS.
print('# Exemplo 01')
d = float(input(' Uma distancia em metros: '))  # distancia
km = d / 1000
hm = d / 100
deca = d / 10
deci = d * 10
cm = d * 100
mm = d * 100
print('''A medida de {} Metros, corresponde a.
{} KILOMETROS
{} HEQUITOMETROS
{} DECAMETROS
{:.0f} DECIMETROS
{:.0f} CENTIMETROS
{:.0f} MILIMETROS'''.format(d, km, hm, deca, deci, cm, mm))

print('# Exemplo 02')
d = float(input(' Uma distancia em metros: '))
print('''A medida de {} Metros, corresponde a.
{} KILOMETROS
{} HEQUITOMETROS
{} DECAMETROS
{:.0f} DECIMETROS
{:.0f} CENTIMETROS
{:.0f} MILIMETROS'''.format(d, d / 1000, d / 100, d / 10, d * 10, d * 100, d * 1000))
