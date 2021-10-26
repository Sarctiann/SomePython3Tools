def SortDictFor(dic:dict, OrdSort:int=None, FiltOrd:int=None,
                                            GreaterThan: str('or equal')=None,
                                            SmallerThan: str('or equal')=None):

    """ Recibe un diccionario y 4 parametros opcionales,
    y retorna un diccionario ordenado.

    OrdSort =>      indice de criterio de orden.  None => por clave.
    FiltOrd =>      indice de criterio de filtro. None => por clave.
    GreaterThan =>  mayor o igual a este parametro es aceptado.
    SmallerThan =>  menor o igual a este parametro es aceptado. """

    ###########################################################################
    if GreaterThan != None:
        if isinstance(GreaterThan, str):
            GT = '"{}"<='.format(GreaterThan)
        else: GT = '{}<='.format(GreaterThan)
    else: GT = ''
 
    if SmallerThan != None:
        if isinstance(SmallerThan, str):
            ST = '<="{}"'.format(SmallerThan)
        else: ST = '<={}'.format(SmallerThan)
    else: ST = ''

    ###########################################################################
    if FiltOrd != None and (GT != '' or ST != ''):
        Filt = '''filter(lambda x: {} x[1][{}] {},
                        list({}.items()))'''.format(GT, FiltOrd, ST, dic)
        
    elif GT != '' or ST != '':
        Filt = '''filter(lambda x: {} x[0] {},
                        list({}.items()))'''.format(GT, ST, dic)
        
    else: Filt = 'list({}.items())'.format(dic)

    ###########################################################################
    if OrdSort != None:
        OrdS = 'sorted({}, key= lambda y: y[1][{}])'.format(Filt, OrdSort)
        
    else: OrdS = 'sorted({}, key= lambda y: y[0])'.format(Filt)

    ###########################################################################
    SortedDict = 'dict({})'.format(OrdS)

    ###########################################################################
    return eval(SortedDict)


if __name__ == '__main__' or __name__ == '__console__': # Para *bpython*

    print("Asegurese de ehecutar en modo interactivo (python3 -i sort_dict.py)")
    a: str('para pruebas') = {4: ['e', 30], 5: ['c', 20], 6: ['a', 10],
                        1:['b',60],2:['d',50],3:['f',40]}
