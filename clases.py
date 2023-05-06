class Conjunto:
    def __init__(self, elementos=None):
        self.elementos = set(elementos) if elementos else set()
    
    def __str__(self):
        return "{" + ", ".join(str(elem) for elem in self.elementos) + "}"
    
    def __add__(self, other):
        return Conjunto(self.elementos.union(other.elementos))
    
    def __sub__(self, other):
        return Conjunto(self.elementos.difference(other.elementos))
    
    def __eq__(self, other):
        return len(self.elementos) == len(other.elementos) and self.elementos == other.elementos

