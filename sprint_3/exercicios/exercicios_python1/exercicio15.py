class Lampada:
    def __init__(self, estado_inicial):
        self.ligada = estado_inicial

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        if self.ligada:
            return True
        else:
            return False



lampada = Lampada(True)

lampada.liga()

print(f'A lâmpada está ligada? {lampada.esta_ligada()}')

lampada.desliga()

print(f'A lâmpada está ligada? {lampada.esta_ligada()}')



