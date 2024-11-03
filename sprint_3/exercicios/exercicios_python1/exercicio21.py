class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Emitindo som...")

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

    def exibir_info(self):
        print("Pato")
        self.voar()
        self.emitir_som()

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

    def exibir_info(self):
        print("Pardal")
        self.voar()
        self.emitir_som()



pato = Pato()
pato.exibir_info()



pardal = Pardal()
pardal.exibir_info()
