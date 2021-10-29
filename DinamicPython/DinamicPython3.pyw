import builtins
import keyword
from os import linesep
from tkinter.constants import E
from tkinter.scrolledtext import ScrolledText
from tkinter import Tk, Button, StringVar
import tkinter.filedialog as fd
import tkinter.font as tkfont
from keyword import kwlist
import sys

# ########################### CONFIGURACION ####################################

DEBUG = False

EDITOR_FONT = 'Lucida\ Console 12 bold' # ("Lucida console", 12, "bold")
E_DEFAULT_HEIGHT = 18
E_BG_COLOR = '#e0e0e0'

OUTPUT_FONT = 'Lucida\ Console 11 bold'
O_HEIGHT = 12
O_COLORS = {
    "fg": "#f0f0f0", 
    "bg": "#505050"
}

 # don't change the keys of the pairs | The order matters
# tcl color names: http://patriciaemiguel.com/assets/tkinter_colores.png
tagsConf = [
            ("keyword",     "purple"),
            ("builtin",     "cyan3"),
            ("builtin2",    "deepskyblue3"),
            ("number",      "orange red"),
            ("operator",    "orange"),
            ("clousures",   "goldenrod"),
            ("string",      "springgreen3"),
            ("ml_string",   "springgreen3"),
            ("comment",     "grey35"),
        ]

################################################################################

builtins = [i for i in dir(__builtins__)]

class root(Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Dinamic Python')
        self.resizable(True, True)
        self.geometry('+100+25')
        self.editor = ScrolledText(self,
            height= E_DEFAULT_HEIGHT, bg= E_BG_COLOR, tabs=8, font=EDITOR_FONT)
        font = tkfont.Font(font=self.editor['font'])
        tab_width = font.measure(' ' * 4)
        self.editor.config(tabs=(tab_width,))
        self.editor.focus()
        self.configureColors()
        self.out = ScrolledText(self,
            height= O_HEIGHT, fg= O_COLORS["fg"], bg= O_COLORS["bg"],
            font=OUTPUT_FONT, state='disabled')
        self.out.config(tabs=(tab_width,))
        ###--------------------------------------------------------------------
        Button(self, bg='#55ddaa', activebackground="#33bb88", 
            command= lambda: root.ejecutar(self),
                
            text='Ctrl\n+\nR\n\n\nRUN'
            ).pack(fill='y', side='left')

        self.editor.bind('<KeyRelease>', lambda *args: self.setColors())
        self.editor.bind('<Control_L>'+'<R>', lambda *args: root.ejecutar(self))
        self.editor.bind('<Control_L>'+'<r>', lambda *args: root.ejecutar(self))
        ###--------------------------------------------------------------------
        self.editor.pack(expand=True, fill='both', side='top')
        self.out.pack(fill='x', side='top')
        ###--------------------------------------------------------------------
        Button(self, text= 'Save Script <Ctrl+s>', bg= '#55aadd',
            activebackground="#3388bb",
            command= lambda: root.guardar(self, self.editor)).pack(
                expand=True, fill='x', side='left')
        self.editor.bind('<Control_L>'+'<s>',
                      lambda *args: root.guardar(self, self.editor))
        ###--------------------------------------------------------------------
        Button(self, text= 'Save Output <Crl+d>', bg= '#55aadd',
            activebackground="#3388bb",
            command= lambda: root.guardar(self, self.out)).pack(
                expand=True, fill='x', side='left')
        self.editor.bind('<Control_L>'+'<d>',
                      lambda *args: root.guardar(self, self.editor))
        ###--------------------------------------------------------------------
        Button(self, text= 'Close <Ctrl+Shift+Q>', bg= '#dd6666',
            activebackground="#bb3333",
            command= lambda: root.salir(self)).pack(
                expand=True, fill='x', side='left')

        self.editor.bind('<Control_L>'+'<Shift_L>'+'<Q>', 
            lambda *args: root.salir(self))
        self.editor.bind('<Control_L>'+'<Shift_L>'+'<q>',
            lambda *args: root.salir(self))

        if not DEBUG:
            sys.stdout = RedirectText(self.out)
            sys.stderr = RedirectText(self.out)

        ###--------------------------------------------------------------------
        self.mainloop()

    def ejecutar(self, *args):

        self.out.config(state='normal') # enable console for write
        self.out.delete(1.0, 'end') # clear the output

        if DEBUG: 
            self.out.insert(1.0, "You need to set DEBUG to False "
                + "in the PythonDin.pyw file!")
        exec(
            self.editor.get(1.0, 'end'), 
            globals(), 
            locals()
        )

        self.out.config(state='disabled')
    
    def configureColors(self):

        
        for tagName, tagColor in tagsConf:
            self.editor.tag_config(tagName, foreground=tagColor)

        kw_regexs = "|".join(
            [rf"\y{x}\y" for x in kwlist]
            )
        b1_regexs = "|".join(
            [rf"@?\y{x}\y" for x in builtins if not x.startswith("__")]
            )
        b2_regexs = "|".join(
            [rf"\y{x}\y" for x in builtins if x.startswith("__")]
            )

        strings = "|".join([
            r"(\"{1}[^\"]*\"{1})",
            r"(\'{1}[^\']*\'{1})",
        ])

        """ I can't find a regular expression
            to highlight multiline strings
            like this correctly :(
            but logically they work anyway.

            All because of the TCL regex are not
            like those of Python ...
        """
        ml_strings = "|".join([
            r"(\"{3}[[:print:][:space:]]*\"{3})",
            r"(\'{3}[[:print:][:space:]]*\'{3})",
        ])

        # tcl rules: http://tcl.tk/man/tcl8.5/TclCmd/re_syntax.html
        # https://www.regular-expressions.info/tcl.html
        # https://www.regular-expressions.info/posixbrackets.html
        self.patterns = [
            (kw_regexs, "keyword"),
            (b1_regexs, "builtin"),
            (b2_regexs, "builtin2"),
            (r"[0-9\.]+", "number"),
            (r"[\+\*\-/%]", "operator"),
            (r"[\(\)\[\]\<\>\{\}]", "clousures"),
            (strings, "string"),
            (ml_strings, "ml_string"),
            (r"#.*\n", "comment"),
        ]
        if DEBUG: 
            print(f"{kw_regexs =}\n")
            print(f"{b1_regexs =}\n")
            print(f"{b2_regexs =}\n")
            print(f"{strings =}\n")
            print("\nTAGS:")
            for t in tagsConf:
                print(f"\t {t}")
            print("\nPATTERNS:")
            for b in self.patterns:
                print(f"\t {b}")

        self.length = StringVar()
        
    def setColors(self):
        if DEBUG: print("\nKEY PRESSED")
        for regex, tag in self.patterns:
            if DEBUG: print(f"CLEARING TAGS")
            self.editor.tag_remove(tag, 1.0, 'end')
            idx = '1.0'
            while True:
                if DEBUG: print(f"buscando: {regex}")
                idx = self.editor.search(
                    regex, idx, 'end', count= self.length, regexp=True,
                )
                if not idx: break
                idx_end = '% s+% sc' % (idx, self.length.get())
                if DEBUG:
                    print(f"MATCH from: {idx =} to {idx_end =}, adding {tag =}")
                self.editor.tag_add(tag, idx, idx_end)
                idx = idx_end


    def guardar(self, que):
        ruta = fd.asksaveasfilename(
            initialdir= "/",
            initialfile= "PythonSarc",
            title= "Guardar",
            filetypes= (
                ("Python","*.py"),
                ("Python GUI", "*.pyw"),
                ("todos","*.*")
            )
        )
        if ruta != '':
            archivo = open(ruta, mode='w')
            archivo.write(que.get(1.0, 'end'))
            archivo.close()

    def salir(self, *args):
        self.destroy()

class RedirectText(object):

    def __init__(self, text_ctrl):
        self.output = text_ctrl

    def write(self, string):
        self.output.insert("end", string) # write on the output
        self.output.see('end') # set the scroll position to the end

if __name__ == '__main__':
    root()
