# Abrindo o arquivo para leitura
with open("arquivo.txt", "r") as arquivo:
    # Lendo o conteúdo do arquivo
    conteudo = arquivo.read()
    # Imprimindo o conteúdo lido
    print(conteudo)

# Abrindo o arquivo para escrita
with open("arquivo_saida.txt", "w") as arquivo:
    # Escrevendo conteúdo no arquivo
    arquivo.write("Este é um arquivo de saída.\n")
    arquivo.write("Contendo algumas linhas de texto.\n")
    arquivo.write("Python é incrível!\n")

# abrindo o arquivo para escrever
with open("dados.txt", "a") as dados:
  # escrevendo os dados no arquivo
  dados.write("DADO 1: a \n")
  dados.write("DADO 2: b \n")
  dados.write("DADO 3: c \n")

# Inserindo dados com um loop 

  with open("dados.txt", "a") as dados:
    contador = 3
    while True:
      msg = input("INSIRA OS DADOS: (digite (x) para encerrar)")
      contador + 1
      if msg == "x":
        break
      dados.write(f"DADO {contador}: {msg}\n")
      contador += 1

num = int(input("quantos dados serão inseridos? "))
with open("dados.txt", "a") as dados:
  for i in range(num):
    msg = input("INSIRA OS DADOS: (digite (x) para encerrar)")
    if msg == "x":
      break
    dados.write(f"DADO {contador}: {msg}\n")
    contador += 1

# e se eu quisesse procurar palavras dentro do arquivo?
with open("dados.txt", "r") as dados:
  conteudo = dados.read()
  achou = False
  if "1" in conteudo:
    print(f"O numero {1} existe no arquivo")
    achou = True
  elif not achou:
    print(f"O numero {1} não existe no arquivo")

# DESAFIO: Modificar o programa para adicionar uma nova linha de texto ao final do arquivo "dados.txt" 

def ler_dado():
  with open("dados.txt","r") as dados:
    conteudo = dados.readlines()
    print(conteudo)

def adicionar_dado():
  with open("dados.txt", "a") as dados:
    contador = 3
    while True:
      msg = input("INSIRA OS DADOS: (digite (x) para encerrar)")
      contador + 1
      if msg == "x":
        break
      dados.write(f"DADO {contador}: {msg}\n")
      contador += 1
  ler_dado()
    
def main():
  print("MENU")
  while True:
    opc = int(input("OQUE DESEJA FAZER? [1: LER DADO], [2: ADICIONAR DADO] [3: SAIR] "))
    if opc == 1:
      ler_dado()
    if opc == 2:
      adicionar_dado()
    if opc == 3:
      break

if __name__ == "__main__":
  main()
