class SingleTk(type):

    _instance = set()

    def __call__(cls, *args, **kwargs):
        if cls._instance == set():
            cls._instance.add(super().__call__(*args, **kwargs))
        for instance in cls._instance:
            instance.protocol("WM_DELETE_WINDOW", cls.deleter)
        return instance

    @classmethod
    def deleter(cls):
        cls._instance.pop().destroy()


class TrigSingleTk(type):

    _instance = set()

    def __call__(cls, *args, **kwargs):
        if cls._instance == set():
            cls._instance.add(super().__call__(*args, **kwargs))
        else:
            cls.deleter()
            cls._instance.add(super().__call__(*args, **kwargs))
        for instance in cls._instance:
            instance.protocol("WM_DELETE_WINDOW", cls.deleter)
        return instance

    @classmethod
    def deleter(cls):
        cls._instance.pop().destroy()


if __name__ == "__main__":

    import tkinter as tk

    class TestA(tk.Toplevel, metaclass=TrigSingleTk):
        def __init__(self, nombre, *args, **kwargs):
            super().__init__()
            tk.Label(self, text=nombre).pack()

    class TestB(tk.Toplevel, metaclass=SingleTk):
        def __init__(self, nombre, *args, **kwargs):
            super().__init__()
            tk.Label(self, text=nombre).pack()

    class Ventana(tk.Tk):
        def __init__(self, *args, **kwargs):
            super().__init__()
            tk.Button(self, text='Ventana >>> A', command=lambda: TestA("A")).pack()
            tk.Button(self, text='Ventana >>> B', command=lambda: TestA("B")).pack()
            tk.Button(self, text='Ventana Unica', command=lambda: TestB("C")).pack()

    a = Ventana()
    a.mainloop()
