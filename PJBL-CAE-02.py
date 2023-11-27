Bibliotecas e módulos
"""

'''
É necessário executar o seguinte comando:
	pip install english-words
'''
# !pip install english-words

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import string
from english_words import english_words_lower_alpha_set as en_words

"""Funções que estruturam o programa"""

'''
Lê o dataset 'SMSSpamCollection', e realiza um processamento no texto.
Adiciona duas colunas, 'length' e 'valid_words', onde a length é referente ao tamanho das mensagens,
enquanto a valid_words busca por palavras que façam sentidos de serem avaliadas.
retorna: Dataframe referente aos dados lidos
'''
def inicializa_dataset() -> pd.DataFrame:
  messages = pd.read_csv('SMSSpamCollection.csv')
  messages['length'] = messages['messages'].apply(len)
  messages['valid_words'] = messages['messages'].apply(count_valid_words)
  return messages


'''
Conta o número de palavras válidas em uma determinada string:
retorna: Qtd. de palavras válidas
'''
def count_valid_words(strs):
  count = 0
  for str in strs:
    nopunc = [char for char in str if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    if str.lower() in en_words:
      count += 1
  return count

def menu():
  print("\n")
  print("1 - Gráfico em barra por tamanho da mensagem (spam/ham)")
  print("2 - Gráfico em barra da quantidade de mensagens por categoria")
  print("3 - Gráfico em linha com densidade em tamanho de mensagens")
  print("4 - Gráfico de linha com as distribuições de palavras válidas e tamanho")
  print("0 - Sair do programa")

'''
  Executa as operações principais do programa, como printar os gráficos e etc.
  e operações de indexação
  retorna: Um booleano indicando o status do programa (True para OK)
'''
def main(df: pd.DataFrame) -> bool:
  try:
    while (True):
      menu()
      opcao = int(input("Insira a opção desejada: "))
      if (opcao == 1):
        color = input("Insira a cor desejada (ex: 'red', 'blue'): ")
        flag = True
        while (flag):
          try:
            df.hist(column='length', by='label', bins=60, figsize=(12,4), color=color)
            plt.show()
            flag = False
          except:
           color = input("Valor inválido! Tente novamente: ")
      
      elif (opcao == 2):
        while (True):
          color = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 1: ")
          color0 = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 2: ")
          try:
            #ax = plt.subplot(111)
            aux = {"spam_size": [len(df[df['label'] == 'spam'])], "ham_size": [len(df[df['label'] == 'ham'])]} 
            aux_df = pd.DataFrame(aux)
            aux_df.plot.bar(color={"spam_size": color, "ham_size": color0})
            plt.show()
            break
        
          except:
            print("Alguma cor está incorreta. Insira novamente.")
            color = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 1: ")
            color0 = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 2: ")

      elif (opcao == 3):
        while (True):
          color = input("Insira a cor desejada (ex: 'red', 'blue'): ")
          try:
            ax = plt.subplot(111)
            df.plot.hist(by='label', ax=ax, bins=60, figsize=(12,4), color='w')
            df['length'].plot(kind='kde', secondary_y=True, color=color)
            plt.xlim(0, 600)
            plt.show()
            break
          except:
            color = input("Valor inválido! Tente novamente: ")
          
      elif (opcao == 4):
        while (True):
          color = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 1: ")
          color0 = input("Insira a cor desejada (ex: 'red', 'blue') para a barra 2: ")
          try:
            sns.lineplot(data=df, 
                x='valid_words', 
                y='length', 
                hue='label',
                palette=[color, color0])
            plt.show()
            break
          except:
            print("Alguma cor está incorreta. Insira novamente.")
            color = input("Insira a cor desejada (ex: 'red', 'blue') para a linha 1: ")
            color0 = input("Insira a cor desejada (ex: 'red', 'blue') para a linha 2: ")
      
      elif (opcao == 0):
        break

      else:
        print("Opção não identificada. Tente novamente.")

    # Fora do while
    print("O programa foi encerrado.")
    return True
  except:
    print("O programa foi finalizado de forma abrupta.")
    return False

"""Parte executável do código"""

if __name__ == '__main__':
  df = inicializa_dataset()
  main(df)

