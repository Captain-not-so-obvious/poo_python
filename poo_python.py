class Pessoa:
  def __init__(self, nome, endereco):
    self.set_nome(nome)
    self.set_endereco(endereco)

    def set_nome(self, nome):
      self.nome=nome

    def set_endereco(self, endereco):
      self.endereco=endereco
    
    def get_nome(self):
      return self.nome

    def get_endereco(self):
      return self.endereco  
