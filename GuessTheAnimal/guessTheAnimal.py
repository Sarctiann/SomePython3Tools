""" Example of a binary tree adapted to Python3
    originally written in Python (2), taken from the book:
        
        "Aprenda a Pensar como Un Programador"
    
    by:
        Allen Downey
        Jeffrey Elkner
        Chris Meyers

    Spanish translation by:
        Miguel Angel Vilella
        Angel Arnal
        Ivan Juanes
        Litza Amurrio
        Efrain Andia
        Cesar Ballardini
"""
# https://argentinaenpython.com/quiero-aprender-python/aprenda-a-pensar-como-un-programador-con-python.pdf

class Tree:
    def __init__(self, content, left=None, right=None):
        self.content = content
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.content)

# Remember from pck:
def recuerdo(default="a Dog"):
    try:
        import pickle
        m_file = open("memory.pck", "rb")
        learned = pickle.load(m_file)
        m_file.close()
        return learned
    except:
        return Tree(default)

# Funcion para memorizar
def remember(what):
    import pickle
    import os
    if os.path.isfile("memory.pck"):
        os.remove("memory.pck")
    m_file= open("memory.pck", "wb")
    pickle.dump(what, m_file)
    m_file.close()

def animal():

    global root

    # Title:
    print("\n |=|=|=| GUESS THE ANIMAL |=|=|=|")

    while 1:
        print("\n")
        if not iHopeYes("Think of an animal! ¿Ready? (y/n) "): break

        tree = root                       
        while tree.left != None:

            yesORno = f"It's {tree.content}? (y/n) "
            if iHopeYes(yesORno):
                tree = tree.right
            else:
                tree = tree.left

        guess = tree.content 

        yesORno = f"It's {guess}? (y/n) "
        if iHopeYes(yesORno):
            print("\nI WIN!!!, and i'm learning \n... let's try again")
            continue

        print("\n Ohh...")

        yesORno = "...what animal were you thinking of? "
        animal = input(yesORno)
        yesORno = "What would distinguish %s from %s? "

        tree.content = input(yesORno % (animal,guess))
        yesORno = "If the animal were %s, what would be the answer? (y/n) "
        if iHopeYes(yesORno % animal):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

        print("...Ok, let me try again")

def iHopeYes(preg):
    rsp = input(preg).lower()
    while rsp[0] != "n" and rsp[0] != "y":
        
        rsp = input("I need a yes or no ").lower()     
    return rsp[0] == 'y'

if __name__ == '__main__':

    root = recuerdo()

    animal()

    yesORno = "\nDo you want me to remember what i learned? (y/n) "
    if iHopeYes(yesORno):
        remember(root)

