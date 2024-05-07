# 1) Dada a matriz com as informações sobre os times em um campeonato [codigo,nome,total de pontos,classificacao], faça uma função em Python que dado o código do time retorne o total de pontos. Faça também uma função que retorne o nome do time que ocupa uma dada posição.
def criar_matriz():
  matriz = [[1, "Time 1", 12, 1],
            [2, "Time 2", 5, 3],
            [3, "Time 3", 9, 2]]
  return matriz

def pontos(equipes):
  codigo = int(input("procurar equipe pelo codigo: "))
  for i in range(len(equipes)):
    if equipes[i][0] == codigo:
      pontuação = equipes[i][2]
      time = equipes[i][1]
      print(f"{time} possui {pontuação} pontos")



def pesquisa(equipes):
  posição = int(input("procurar time por posição: "))
  for time in equipes:
    if time[3] == posição:
      print(time[1])

def menu(equipes):
  while True:
    numero = int(input("Escolha um opção [0: SAIR], [1: TOTAL DE PONTOS], [2: PESQUISA]: "))
    if numero == 0:
      return None
    if numero == 1:
      pontos(equipes)
    if numero == 2:
      pesquisa(equipes)


def main():
  equipes = criar_matriz()
  menu(equipes)
  return

if __name__ == "__main__":
    main()

# 2) Crie uma aplicação de controle de estoque com os conhecimentos de função. A aplicação deve possuir as funções que permitam: 2.1) inserir materiais (codigo, descrição e quantidade); 2.2) remover material; 2.3) listar todos os materiais; 2.4) Calcular a quatidade de materiais em estoque; 2.5) Quais materiais cadastrado não tem no estoque (quantidade igual 0). Acrescente outras funções que achar pertinente.

# CRIANDO A MATRIZ DENTRO DA FUNÇÃO
def criar_estoque():
  matriz = [[1, "banana", 190],
            [2, "maça", 200],
            [3, "açaí", 50],
            [4, "kiwi", 160],
            [5, "pera", 100]]
  return matriz

# FUNÇÃO DE ADICIONAR PRODUTOS NO ESTOQUE
def adicionar(estoque):
  print("ADICIONAR PRODUTOS NO ESTOQUE!")
  add_estoque = input("ADICIONE: (CODIGO DO PRODUTO), (NOME DO PRODUTO) E (QUANTIDADE) EX: 1,ABACAXI,100: ").split(",") # .split(",") pra separar os novos produtos em uma nova lista
  estoque.append(add_estoque) # adicionando os novos produtos dentro da matriz
  print(add_estoque)
  print(estoque)
  return

# FUNÇÃO DE REMOVER PRODUTOS DO ESTOQUE
def remover(estoque):
  print("REMOVER PRODUTOS DO ESTOQUE!")
  print(estoque)
  msg = input("Qual Produto Você Deseja Remover? ")
  removido = False # esse passo é importante para manter a lógica futuramente
  for produto in estoque:
      if msg in produto: # verifica se o input que usuário colocou existe dentro do estoque
          estoque.remove(produto) # removendo o produto
          removido = True # se ele removeu, a variável se torna verdadeira
          print("Produto removido com sucesso!")
          break # acaba o loop e retorna para o menu
  if not removido: # caso não for removido, ele retorna com um print
      print("Produto não encontrado no estoque.")
  print("PRONTO!!", estoque)

# FUNÇÃO DE LISTAR PRODUTOS DO ESTOQUE
def listar(estoque):
    produtos = [linha[1] for linha in estoque] # list comprehesion para guardar os valores da segunda coluna (produtos) dentro de uma variável
    print("LISTAGEM DE PRODUTOS ATUAIS:" )
    for produto in produtos: # for loop para exibir dada um dos produtos
        print("-", produto)

# FUNÇÃO DE CALCULAR PRODUTOS DO ESTOQUE
def calcular_qntd(estoque):
  quantidade = [linha[2]for linha in estoque] # list comprehesion para guardar os valores da coluna 2 (qntd) dentro de outra variável
  quantidade_total = sum(quantidade) # somar com o sum() para obter o valor total
  print("QUANTIDADE TOTAL TO ESTOQUE:", quantidade_total)

# FUNÇÃO DE VERIFICAR SE O PRODUTO EXISTE NO ESTOQUE
def verificar(estoque):
  produtos = [linha[1] for linha in estoque] # list comprehesion novamente com a mesma funcionalidade da função listar()
  teste = input("QUAL PRODUTO VOCÊ GOSTARIA DE ACESSAR? ")
  if teste in produtos: # caso o input seja o mesmo que algum produto dentro da lista, o script inicia
    print(teste, "ESSE PRODUTO ESTÁ NO ESTOQUE!")
  else:
    print("ESSE PRODUTO NÃO ESTÁ NO ESTOQUE!") # caso contrário, o script questiona o se o usuário gostaria de adicionar o produto
    texto = input("GOSTARIA DE ADICIONAR ESSE PRODUTO NO ESTOQUE? S/N ")
    if texto == "S": # se sim, ele executa a função anterior adicionar()
      adicionar(estoque)

# FUNÇÃO DE VERIFICAR SE O PRODUTO ESTÁ EM FALTA
def em_falta(estoque):
  falta = False # mesma lógica do anterior
  for produto in estoque:
    if produto[2] == 0: # acessando a coluna de quantidade do estoque
      falta = True
      print(f"{produto} ESTÁ EM FALTA!!")
  if not falta:
    print("NENHUM PRODUTO EM FALTA!!")


def menu(estoque):
  while True:
    print("-" * 20)
    opção = int(input("Oque deseja fazer? [0: SAIR], [1: EDITAR], [2: CALCULAR A QUANTIDADE DOS ITENS], [3: VERIFICAR ITENS CADASTRADOS], [4: VERIFICAR ESTOQUE]: "))
    print("-" * 20)
    if opção == 0:
      return None
    if opção == 1:
      while True:
        opção_2 = int(input("Oque deseja fazer agora? [0: SAIR], [1: ADICIONAR], [2: REMOVER], [3: LISTAR]: "))
        if opção_2 == 0:
          break
        if opção_2 == 1:
          adicionar(estoque)
        if opção_2 == 2:
          remover(estoque)
        if opção_2 == 3:
          listar(estoque)
    if opção == 2:
      calcular_qntd(estoque)
    if opção == 3:
      verificar(estoque)
    if opção == 4:
      em_falta(estoque)

def main():
  estoque = criar_estoque()
  menu(estoque)
  return

if __name__ == "__main__":
  main()