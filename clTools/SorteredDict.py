def sort_dict(
        dic: dict, 
        sortIDX: int = None, 
        FilterIDX: int = None,
        GreaterThan = None,
        SmallerThan = None
    ):

    """ Recive:
        A DICTIONARY to sort [,
            sortIDX =>      sort index criteria.  None => for key,
            FilterIDX =>    filter index criteria. None => for key,
            GreaterThan =>  (for filter) greater or equal,
            SmallerThan =>  (for filter) smaller or equal 
        ]
    
        Return: the sort dictionary by passed criteria.
    """

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
    if FilterIDX != None and (GT != '' or ST != ''):
        Filt = '''filter(lambda x: {} x[1][{}] {},
                        list({}.items()))'''.format(GT, FilterIDX, ST, dic)
        
    elif GT != '' or ST != '':
        Filt = '''filter(lambda x: {} x[0] {},
                        list({}.items()))'''.format(GT, ST, dic)
        
    else: Filt = 'list({}.items())'.format(dic)

    ###########################################################################
    if sortIDX != None:
        OrdS = 'sorted({}, key= lambda y: y[1][{}])'.format(Filt, sortIDX)
        
    else: OrdS = 'sorted({}, key= lambda y: y[0])'.format(Filt)

    ###########################################################################
    SortedDict = 'dict({})'.format(OrdS)

    ###########################################################################
    return eval(SortedDict)


if __name__ == '__main__' or __name__ == '__console__': # for *bpython*

    print("Make sure to run in interactive mode (python3 -i SorteredDict.py)")
    
    a: str('for testing') = {
        4: ['e', 30], 
        5: ['c', 20], 
        6: ['a', 10],
        1: ['b', 60],
        2: ['d', 50],
        3: ['f', 40]
    }
