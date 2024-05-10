def escreva(txt):
  print("_" * 12)
  print(txt)
  print("_" * 12)


escreva("algumacoisa")

def contador(* núm):
  tam = len(núm)
  print(f"recebi os valores {núm} e são ao todo {tam} números")


contador(2, 1, 3)
contador(4, 0)
contador(1 ,2 ,3 ,4 ,5 ,6)

def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos] *= 2
    pos += 1

# Programa Central
valores = [7,2,5,0,4]
dobra(valores)
print(valores)

def soma(* valores):
  s = 0
  for num in valores:
    s += num
  print(f'Somando os valores  {valores} temos {s}')



soma(3, 5)
soma(3, 2, 1)

class Computador:
  def __init__(self, marca, memoria_ram, placa_de_video):
    self.marca = marca
    self.memoria_ram = memoria_ram
    self.placa_de_video = placa_de_video

  def Ligar(self):
    print("LIGANDO")

  def Desligar(self):
    print("DESLIGANDO")

  def ExibirInformaçõesDesteComputador(self):
    print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = Computador("asus", "16gb", "RTX 550")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformaçõesDesteComputador()

class Carro:
  def __init__(self, marca, motor, modelo):
    self.marca = marca
    self.motor = motor
    self.modelo = modelo

  def Ligar(self):
    print("LIGANDO")

  def Desligar(self):
    print("DESLIGANDO")

  def ACELERAR(self):
    print("ACELERANDO")

  def ExibirInformaçõesDesteCarro(self):
    print(self.marca, self.motor, self.modelo)


carrao = Carro("MERCEDES", "1.3, 163cv, 27kgfm", "MERCEDES-BENZ A-200")
carrao.Ligar()
carrao.Desligar()
carrao.ACELERAR()
carrao.ExibirInformaçõesDesteCarro()