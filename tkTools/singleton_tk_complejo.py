import tkinter as tk


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def deleter(cls, instance):
        indice = list(cls._instances.values()).index(instance)
        key = list(cls._instances.keys())[indice]
        del cls._instances[key]
        instance.destroy()


class A(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()
        tk.Button(self, text='VentanaA', command=lambda: Ventana("A")).pack()
        tk.Button(self, text='VentanaB', command=lambda: Ventana("B")).pack()


class Ventana(tk.Toplevel, metaclass=Singleton):

    def __init__(self, nombre, *args, **kwargs):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", lambda: Singleton.deleter(self))
        tk.Label(self, text=nombre).pack()


a = A()
a.mainloop()
