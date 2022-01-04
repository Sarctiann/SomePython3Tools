'''
	*** Percentage operations ***:

	1) Start this module in interactive mode (python3 -i Percentages.py)
	2) Instantiate Percentron ( Eg. p = Percentron(...) ).
	3) More Info => Percentron.help() | help(Percentron)

	                                                        Sebastián Atlántico
'''


class Percentron:
    '''
    Recive zero, one or many defualt values. These can be values to operate with
    percentages, or percentages to operate with other percentages.

    Return an Percentron object.
    '''

    def __init__(self, *args):
        if args != ():
            self.val = []
            for i in args:
                if isinstance(i, (int, float)):
                    self.val.append(i)
                elif isinstance(i, (list, tuple, set)):
                    self.val.extend(i)
                else:
                    raise TypeError('Only accept numbers')

    @classmethod
    def help(cls):
        help = ''.join(
            ["\nvalues (val) and percentages (per) operations\n",
             '\n.val_increase(p, *,val):\n\t', cls.val_increase.__doc__,
                '\n.val_discount(p, *,val):\n\t', cls.val_discount.__doc__,
                '\n.val_from_increase(p, *,val):\n\t', cls.val_from_increase.__doc__,
             '\n.val_from_discount(p, *,val):\n\t', cls.val_from_discount.__doc__,
             '\n.per_addition(p, *,val):\n\t', cls.per_addition.__doc__,
             '\n.per_subtraction(p, *,val):\n\t', cls.per_subtraction.__doc__,
             '\n.per_from_addition(p, *,val):\n\t', cls.per_from_addition.__doc__,
             '\n.per_from_subtraction(p, *,val):\n\t', cls.per_from_subtraction.__doc__,
             '\n.per_from_val_increase(p, *,val):\n\t', cls.per_from_val_increase.__doc__,
             '\n.per_from_val_discount(p, *,val):\n\t', cls.per_from_val_discount.__doc__,
                "\nRemember, val and per are keyword arguments\n"]
        )
        print(help)

    def __check_val(self):
        if self.__dict__ != {}:
            return True
        else:
            print('\n This Percentron is Empty,\n',
                  'you must include "val" argument for each operation')
            return False

    def val_increase(self, p: float, *, val: float = None):
        ''' Increase values a "p" percent
                Eg. 100(val) + 20%(p) = 120
        '''
        if val != None:
            return round(val*(1+p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.val_increase(p, val=i))
                return result

    def val_discount(self, p: float, *, val: float = None):
        ''' Discounts "p" percent to values
                Eg. 100(val) - 20%(p) = 80
        '''
        if val != None:
            return round(val*(1-p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.val_discount(p, val=i))
                return result

    def val_from_increase(self, p: float, *, val: float = None):
        ''' Obtains the value resulting from increase "p" percent to values
                Eg. 100(val) from increase 20%(v) = 83.33...
        '''
        if val != None:
            return round(val/(1+p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.val_from_increase(p, val=i))
                return result

    def val_from_discount(self, p: float, *, val: float = None):
        ''' Obtains the value resulting from discount "p" percent to values
                Eg. 100(val) from discount 20%(p) = 125
        '''
        if val != None:
            return round(val/(1-p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.val_from_discount(p, val=i))
                return result

    ###---------------------------------------------------------------------###

    def per_addition(self, p: float, *, per: float = None):
        ''' (assumes values are percentages)
                Add the percentage "p" to percentages (values)
                Eg. 100%(per) + 10%(p) = 120%
        '''
        if per != None:
            return round(per+p+(per*p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.per:
                    result.append(self.per_addition(p, per=i))
                return result

    def per_subtraction(self, p: float, *, per: float = None):
        ''' (assumes values are percentages)
                Subtract the percentage "p" to percentages (values)
                Eg. 100%(per) - 10%(p) = 80%
        '''
        if per != None:
            return round(per-p-(per*p/100), 2)
        else:
            if self.__check_val():
                result = []
                for i in self.per:
                    result.append(self.per_subtraction(p, per=i))
                return result

    def per_from_addition(self, p: float, *, per: float = None):
        ''' (assumes values are percentages)
                Obtains the percentage resulting from addition of "p" percent 
                to percentages (values)
                Eg. 100%(per) from addition 10%(p) = 81.83...%
        '''
        if per != None:
            z = (per-p)/(1+p/100)
            return round(z, 2)
        else:
            if self.__check_val():
                result = []
                for i in self.per:
                    result.append(self.per_from_addition(p, per=i))
                return result

    def per_from_subtraction(self, p: float, *, per: float = None):
        ''' (assumes values are percentages)
                Obtains the percentage resulting from subtraction of "p" percent 
                to percentages (values)
                Eg. 100%(per) from subtraction 10%(p) = 122.22...%
        '''
        if per != None:
            z = (per+p)/(1-p/100)
            return round(z, 2)
        else:
            if self.__check_val():
                result = []
                for i in self.per:
                    result.append(self.per_from_subtraction(p, per=i))
                return result

    ###---------------------------------------------------------------------###

    def per_from_val_increase(self, v: float, *, val: float = None):
        ''' Obtains the percentage from "v" 
            as resulting increase to values
                Eg. 100(val) increased to 110(v) = 10%
        '''
        if val != None:
            z = (v/val-1)*100
            return round(z, 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.per_from_val_increase(v, val=i))
                return result

    def per_from_val_discount(self, v: float, *, val: float = None):
        ''' Obtains the percentage from "v" 
            as resulting discount to values
                Eg. 100(val) discounted to 90(v) = 10%
        '''
        if val != None:
            z = 100-(v/val*100)
            return round(z, 2)
        else:
            if self.__check_val():
                result = []
                for i in self.val:
                    result.append(self.per_from_val_discount(v, val=i))
                return result

    def per_from_per_addition(self, p: float, *, per: float = None):
        ''' Obtains the percentage from "p" 
            as resulting addition of percentages
                Eg. 100(per) increased to 120(p) = 10%
        '''
        if per != None:
            z = (p - per)/2
            return round(z, 2)
        else:
            if self.__check_per():
                result = []
                for i in self.per:
                    result.append(self.per_from_per_increase(p, per=i))
                return result

    def per_from_per_subtraction(self, p: float, *, per: float = None):
        ''' Obtains the percentage from "p" 
            as resulting subtraction of percentages
                Eg. 100(per) discounted to 80(p) = 10%
        '''
        if per != None:
            z = (per - p)/2
            return round(z, 2)
        else:
            if self.__check_per():
                result = []
                for i in self.per:
                    result.append(self.per_from_per_discount(p, per=i))
                return result

    def __repr__(self):
        if self.__dict__ != {}:
            return 'Percentron object loaded'
        else:
            return 'Percentron object empty'

    def __str__(self):
        if self.__dict__ != {}:
            return 'Percentron values:\n {}'.format(self.val)
        else:
            return 'No values loaded'


if __name__ == '__main__':
    print(__doc__)
