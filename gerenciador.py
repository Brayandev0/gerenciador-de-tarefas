# Criador         : Brayan vieira 
# função          : Cria uma lista de tarefas com varias funções de adicionar e deletar 
# versão          : 1.0
# data da criação : 10/2/2024
import os
import platform 
#-------------------------------------------------------------------------------------------------------
#                                            Definindo variaveis padrão e lista 
tarefas = []
PADRAO = "Aperte Enter para continuar : "
#-------------------------------------------------------------------------------------------------------
#                                                  Identificando o sistema para o clear 
sistema_operacional = platform.system()
if sistema_operacional == "Windows":
     limpador = "cls"
elif sistema_operacional == "Linux" or "Mac":
     limpador = "clear"
#-------------------------------------------------------------------------------------------------------
#                                                    Função adicionar tarefas 
def add():
        os.system(limpador)
        item = input(" \n insira a tarefa que deseja adicionar e a hora \n \n Ex : Acordar 5:30 \n \n adicionar : ")
        if item:
          tarefas.insert(0,item)
          os.system(limpador)
          print(f"\n sua lista de tarefas atual e : {tarefas} \n")
          return input(PADRAO)
        os.system(limpador)
        print("você não inseriu nada \n ")
        return input(PADRAO)
#-------------------------------------------------------------------------------------------------------
#                                                    Função remover tarefas 
def remover():
      try:
          os.system(limpador)
          print(" \n Numero das tarefas para a remoção : \n ")
          for indice, tarefas_for in enumerate(tarefas):
               print(f"id = {indice} : {tarefas_for} \n ")
               continue
          numero = int(input("Insira o id da tarefa para remove-la \n \n id : "))
          tarefas.pop(numero)
          return input(f" \n {PADRAO}")
#-------------------------------------------------------------------------------------------------------
#                                                   Tratando Erros  na remoção 
      except IndexError: 
           print(" \n id inexistente \n ")
           return input(PADRAO)
      except ValueError:
           print("\n \n Você inseriu um caracter invalido, insira somente numeros \n ")
           return input(f"\n \n {PADRAO}")
#-------------------------------------------------------------------------------------------------------
#                                                  Função Ver tarefas 
def ver_tarefas():
     for tarefas_da_lista in tarefas:
          os.system(limpador)
          print(f"\n Sua lista atual e : \n \n {tarefas_da_lista} \n ")
          continue 
     return input(PADRAO)
#-------------------------------------------------------------------------------------------------------
#                                                      Menu do programa 
while True:
    os.system(limpador)
    print("Bem vindo ao menu de tarefas diarias \n ")
    decisao1 = input(" [A] adicionar tarefas \n \n [R] remover tarefas \n\n [V] ver tarefas \n \n Insira : ").lower()
#-------------------------------------------------------------------------------------------------------
#                                                      Menu de escolha 
    match decisao1:
        case "r":
            remover()
        case "a": 
            add()
        case "v":
#-------------------------------------------------------------------------------------------------------
#                                            Erro de lista vazia e caracter invalido  
            if tarefas: 
               ver_tarefas()
            else:
               os.system(limpador)
               print("\nErro : sua lista esta vazia \n \n ")
               input(PADRAO)
               continue
        case _:
              input(f"\n Cracter inserido invalido \n \n {PADRAO}")
