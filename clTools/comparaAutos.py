"""Programa para compara Autos usados según su kilometraje,
 su modelo y su precio.
 Las Constantes representan posibilidades en Agosto del 2019.
 Pueden ser redefinidas."""

KMS     = {'bueno': 0,    'malo': 100000}
MODELO  = {'bueno': 2019, 'malo': 2013}
PRECIO  = {'bueno': 0,    'malo': 280000}

PRIORIDAD: str('porcentaje') = {'K': 50, 'M': 30, 'P': 20}


class Auto:
    def __init__(self, nombre, kms, mod, pre):
        self.nombre = nombre
        self.kms = self._puntaje(*KMS.values(),kms)
        self.mod = self._puntaje(*MODELO.values(),mod)
        self.pre = self._puntaje(*PRECIO.values(),pre)

    def puntaje(self):
        punt=(( self.kms*PRIORIDAD['K']
               +self.mod*PRIORIDAD['M']
               +self.pre*PRIORIDAD['P'])/100)
        return punt

    def _puntaje(self, maxi, mini, x):
        porcentaje = (x-mini)*100/(maxi-mini)
        return porcentaje

    def __str__(self):
        return self.nombre
        

def comparar(autos):
    print('\n\n')
    for auto in autos:
        nom = auto.nombre
        kms = auto.kms
        mod = auto.mod
        pre = auto.pre
        print(
        f'Pts de {nom}:\n\tKms => {kms}\n\tModelo => {mod}\n\tPrecio => {pre}'
        )
    print()
    for auto in autos:
        print(f'Puntaje de {auto} = {auto.puntaje()}')

if __name__ == '__main__':

    print(
          '\nEntonces consideremos los siguientes parametros de comparación:')
    print(f"Kilometraje Mejor: {KMS['bueno']} Peor: {KMS['malo']}")
    print(f"Modelo Mejor: {MODELO['bueno']} Peor: {MODELO['malo']}")
    print(f"Precio Mejor: {PRECIO['bueno']} Peor: {PRECIO['malo']}")
    print('\nCon la siguiente prioridad:')
    print("Kilometros: {}%, Modelo: {}%, Precio {}%\n".format(
           PRIORIDAD['K'],PRIORIDAD['M'],PRIORIDAD['P'])
          )
        
    if input('Quiere redefinir los parametros? (s/cualquiera): ') == 's':
        print()
        KMS['bueno'] = int(input('Cual sería el mejor kilometraje? '))
        MODELO['bueno'] = int(input('Cual sería el mejor modelo (año)? '))
        PRECIO['bueno'] = int(input('Cual sería el mejor precio? '))
        KMS['malo'] = int(input('Cual sería el peor kilometraje? '))
        MODELO['malo'] = int(input('Cual sería el peor modelo (año)? '))
        PRECIO['malo'] = int(input('Cual sería el peor precio? '))
        print('\n Defina la prioridad de cada parametro\n',
              '(la suma total debería dar 100)\n')
        PRIORIDAD['K'] = int(input('Kilometros: '))
        PRIORIDAD['M'] = int(input('Modelo: '))
        PRIORIDAD['P'] = int(input('Precio: '))

        print(
          '\nEntonces consideremos los siguientes parametros de comparación:')
        print(f"Kilometraje Mejor: {KMS['bueno']} Peor: {KMS['malo']}")
        print(f"Modelo Mejor: {MODELO['bueno']} Peor: {MODELO['malo']}")
        print(f"Precio Mejor: {PRECIO['bueno']} Peor: {PRECIO['malo']}")
        print('\nCon la siguiente prioridad:')
        print("Kilometros: {}%, Modelo: {}%, Precio: {}%\n".format(
                PRIORIDAD['K'],PRIORIDAD['M'],PRIORIDAD['P'])
              )

    autos = []
    cond = 's'
    while cond == 's':
        autos.append(Auto(
            input('Ingrese el Nombre del auto: '),
            int(input('Ingrese su Kilometraje: ')),
            int(input('Ingrese su Modelo: ')),
            int(input('Ingrese su precio: '))
        ))
        
        cond = input('Quiere agregar otro auto? (s/cualquiera) ')

    comparar(autos)

    input('\n\nPresione una tecla para salir ')
