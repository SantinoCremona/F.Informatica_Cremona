#cada chef tiene un atributo plato_del_dia;las instancias de Chef pueden picantear ese plato solo si no está demasiado picante, en caso de estarlo arrojan una excepción que dice El plato ya está demasiado picante;las instancias de AyudanteDeCocina no tienen atributos ya que pueden suavizar cualquier plato que reciban como argumento.
#Mientras que de los platos podemos contar lo siguiente:las Pastas tienen un atributo ajies que inicialmente es 0;están demasiado picantes cuando tienen más de 10 ajies;al ser picanteadas aumenta en 5 su cantidad de ajies y al ser suavizadas pierden 1. No te preocupes por si al suavizar queda una cantidad negativa de ajies, no vamos a considerar ese escenario;las Pizzas tienen condimento que inicialmente es "adobo";se considera que una pizza está demasiado picante si su condimento es "cayena";al suavizar una pizza su condimento pasa a ser "orégano" y al picantearla, "cayena".Los constructores en ambos platos solo deben tener self como parámetro porque sus atributos siempre se inicializan con el mismo valor. 
class Chef:
    def __init__(self, plato):
        self.plato_del_dia = plato

    def picantear(self):
        self.plato_del_dia.picantear()
   
class AyudanteDeCocina:
    def suavizar(self, plato):
        plato.suavizar()

class Pasta:
    def __init__(self):
        self.ajies = 0

    def picantear(self):
        if self.ajies <= 10:
            self.ajies += 5
        else:
            raise Exception("El plato ya está demasiado picante")
            
    def suavizar(self):
      self.ajies -= 1

class Pizza:
    def __init__(self):
        self.condimento = "adobo"

    def picantear(self):
        if self.condimento == "adobo":
            self.condimento = "cayena"
        else:
            raise Exception("El plato ya está demasiado picante")

    def suavizar(self):
        self.condimento = "orégano"

#Zombi y Superzombi
class Zombi:
  def __init__(self, un_hambre):
    self.hambre = un_hambre

  def sabe_correr(self):
    return True

  def es_un_peligro(self):
    return self.hambre > 50

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio * 2
   
  def descansar(self, minutos):
    self.hambre += minutos

class SuperZombi(Zombi):
  def es_un_peligro(self):
    return True

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio

  def regenerarse(self):
    self.hambre = 100

#listas de comprension: [numero * 2 for numero in numeros if numero > 5]
