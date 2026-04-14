import re

# Precios correctos redondeados a .50
precios = {
    'p1': 7250, 'p2': 12250, 'p3': 10250, 'p4': 16250, 'p5': 19250, 'p6': 11250,
    'p7': 8250, 'p8': 10250, 'p9': 10250, 'p10': 12250, 'p11': 2250, 'p12': 9250,
    'p13': 8250, 'p14': 14250, 'p15': 18250, 'p16': 12250, 'p17': 14250, 'p18': 11250,
    'p19': 12250, 'p20': 9850, 'p21': 7250, 'p22': 16050, 'p23': 32250, 'p24': 19850,
    'p25': 7650, 'p26': 7250, 'p27': 6250, 'p28': 10250, 'p29': 11450, 'p30': 9250,
    'p31': 11650, 'p32': 8850, 'p33': 17000, 'p34': 6000
}

with open('index.html', 'r', encoding='utf-8') as f:
    contenido = f.read()

# Reemplazar cada precio
for prod_id, precio in precios.items():
    # Usar una función para evitar problemas con referencias de grupo
    patron = f'(id: "{prod_id}".*?price:\\s*)(\\d+)(,)'
    def repl_func(match):
        return f'{match.group(1)}{precio}{match.group(3)}'
    contenido = re.sub(patron, repl_func, contenido, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(contenido)

print('✓ Precios actualizados correctamente')
