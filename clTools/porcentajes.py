'''
	*** Operaciones con porcentajes ***:

	Parece sencillo, pero a veces nos encontramos con la necesidad de hacer
	calculos poco usuales. Por eso escribo este modulo que contiene una
	clase instanciable: "Porcentron" que cuenta con operaciones sencillas
	y otras no tan sencillas para operar con valores (val) y porcentajes (por)
	sumando y restando, aumentos y descuentos.

	1) Inicie este modulo en el 'Python Shell' => python3 -i porcentajes.py
	2) Instancie Porcentron ( Ej: p = Porcentron(...) ).
	3) Opere con sus metodos ( Ejs:
	                           precio_actual = p.val_sum_aum(15)
	                           desc_especiales = p.por_sum_des(10, val=30) ).
	4) Para mas información => Porcentron.ayuda() | help(Porcentron)

	                                                        Sebastián Atlántico
	'''

class Porcentron:
	'''Clase instanciable para realizar operaciones con porcentajes.

	Opcionalmente recibe los valores con los que se va a trabajar,
	estos pueden ser valores para operar con porcentajes, o pueden ser
	porcentajes para operar con ellos'''

	def __init__(self, *args):
		if args !=():
			self.val = []
			for i in args:
				if isinstance(i, (int, float)):
					self.val.append(i)
				elif isinstance(i, (list, tuple, set)):
					self.val.extend(i)
				else:
					raise TypeError('Solo recibe números')

	@classmethod
	def ayuda(cls):
		ayuda = '\n'.join(
		       ['\n.val_sum_aum(p, *,val):\n\t', cls.val_sum_aum.__doc__,
		        '\n.val_sum_des(p, *,val):\n\t', cls.val_sum_des.__doc__,
		        '\n.val_res_aum(p, *,val):\n\t', cls.val_res_aum.__doc__,
				'\n.val_res_des(p, *,val):\n\t', cls.val_res_des.__doc__,
				'\n.por_sum_aum(p, *,val):\n\t', cls.por_sum_aum.__doc__,
				'\n.por_sum_des(p, *,val):\n\t', cls.por_sum_des.__doc__,
				'\n.por_res_aum(p, *,val):\n\t', cls.por_res_aum.__doc__,
				'\n.por_res_des(p, *,val):\n\t', cls.por_res_des.__doc__,
    '\nRecuerde que el argumento "val" debe ser nombrado para su asignación\n']
	)
		print(ayuda)

	def __check_val(self):
		if self.__dict__ != {}:
			return True
		else:
			print('\n Este Porcentron no contiene valores,\n',
                'debería incluir el parametro "val" asignandole el valor\n',
				'con el que desea realizar la operación.')
			return False

	def val_sum_aum(self, p:float, *,val:float=None):
		'''SUMA un AUMENTO porcentual a los valores:

		p: porcentaje que se aumentará a los valores
		val(param nombrado, opcional): valor a operar'''

		if val != None:
			return round(val*(1+p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.val_sum_aum(p, val=i))
				return result

	def val_sum_des(self, p:float, *,val:float=None):
		'''SUMA un DESCUENTO porcentual a los valores:

		p: porcentaje que se descontará a los valores
		val(param nombrado, opcional): valor a operar'''

		if val != None:
			return round(val*(1-p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.val_sum_des(p, val=i))
				return result

	def val_res_aum(self, p:float, *,val:float=None):
		'''RESTA un AUMENTO porcentual a los valores:

		p: porcentaje que se aumentó a los valores
		val(param nombrado, opcional): valor a operar'''

		if val != None:
			return round(val/(1+p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.val_res_aum(p, val=i))
				return result

	def val_res_des(self, p:float, *,val:float=None):
		'''RESTA un DESCUENTO porcentual a los valores:

		p: porcentaje que se descontó a los valores
		val(param nombrado, opcional): valor a operar'''

		if val != None:
			return round(val/(1-p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.val_res_des(p, val=i))
				return result

	###---------------------------------------------------------------------###

	def por_sum_aum(self, p:float, *,val:float=None):
		'''(asume que los valores son porcentajes) SUMA AUMENTOS sucesivos:

		p: porcentaje que se sumará a los aumentos iniciales
		val(param nombrado, opcional): aumentos a operar'''

		if val != None:
			return round(val+p+(val*p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.por_sum_aum(p, val=i))
				return result

	def por_sum_des(self, p:float, *,val:float=None):
		'''(asume que los valores son porcentajes) SUMA DESCUENTOS sucesivos:

		p: porcentaje que se sumará a los descuentos iniciales
		val(param nombrado, opcional): aumentos a operar'''

		if val != None:
			return round(val+p-(val*p/100), 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.por_sum_des(p, val=i))
				return result

	def por_res_aum(self, p:float, *,val:float=None):
		'''(asume que los valores son porcentajes) RESTA AUMENTOS sucesivos:

		p: porcentaje que se restará a los aumentos iniciales
		val(param nombrado, opcional): aumentos a operar'''

		if val != None:
			z = (val-p)/(1+p/100)
			return round(z, 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.por_res_aum(p, val=i))
				return result

	def por_res_des(self, p:float, *,val:float=None):
		'''(asume que los valores son porcentajes) RESTA DESCUENTOS sucesivos:

		p: porcentaje que se restará a los descuentos iniciales
		val(param nombrado, opcional): aumentos a operar'''

		if val != None:
			z = (val-p)/(1-p/100)
			return round(z, 2)
		else:
			if self.__check_val():
				result = []
				for i in self.val:
					result.append(self.por_res_des(p, val=i))
				return result

	def __repr__(self):
		if self.__dict__ != {}:
			return 'Objeto Porcentron Cargado'
		else:
			return 'Objeto Porcentron Vacío'

	def __str__(self):
		if self.__dict__ != {}:
			return 'valores del Porcentron:\n {}'.format(self.val)
		else:
			return 'Sin Valores asignados'



if __name__ == '__main__':
	print(__doc__)
