class AnimalAlado:
  def esta_feliz(self):
    return self.energia > 500

class Entrenador:
  def __init__(self,dragones, aves):
    self.dragones = dragones
    self.aves = aves
  
  def aceptar_dragones(self, dragon):
    self.dragones.append(dragon)
  
  def aceptar_aves(self, ave):
    self.aves.append(ave)

  def entrenamiento(self):
    for i in range(20):
        self.volar_en_circulos() 
    self.comer()

  def entrenamiento_intensivo(self):
    while not self.esta_debil():
      self.volar_en_circulos()

class AveNoVoladora(Entrenador):
  def __init__(self, energia):
    self.energia = energia

  def come_alpiste(self, gramos):
    self.come_alpiste(gramos)

  def comer(self):
    self.come_alpiste(3)

  def corre_en_circulos(self):
    self.energia -= 25

class Golondrina(AnimalAlado, Entrenador):
  def __init__(self, energia):
    self.energia = energia
#el init es el constructor del objeto
  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def comer(self):
    self.comer_alpiste(3)

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia < 10

class Dragon(AnimalAlado, Entrenador):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def comer(self):
    self.comer_peces(3)

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia < 50

pepita = Golondrina(100)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)
hipo = Entrenador
caro = AveNoVoladora(100)