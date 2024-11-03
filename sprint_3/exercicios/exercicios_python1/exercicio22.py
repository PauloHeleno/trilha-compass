class Pessoa:
    def __init__(self, id):
        self.__nome = None  
        self.id = id        

    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor


pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal' 
print(pessoa.nome)             
