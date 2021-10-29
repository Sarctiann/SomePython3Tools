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

if __name__ == "__main__":

    import tkinter as tk

    class Window(tk.Toplevel, metaclass=Singleton):

        def __init__(self, name, *args, **kwargs):
            super().__init__()
            self.protocol("WM_DELETE_WINDOW", lambda: Singleton.deleter(self))
            self.geometry('100x100+300+300')
            tk.Label(self, text=name).pack()

    class Root(tk.Tk):

        def __init__(self, *args, **kwargs):
            super().__init__()
            self.geometry('+300+200')
            tk.Button(
                self, text='Window A', command=lambda: Window("A")).pack()
            tk.Button(
                self, text='Window B', command=lambda: Window("B")).pack()

    root = Root()
    root.mainloop()
