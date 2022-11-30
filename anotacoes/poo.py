# Programação orientada a objeto

# classes
# utilizadas para criar objetos (instances)
# Objetos são partes dentro de uma Class (instancias)
# Classes são utilizadas para agrupar dados e funções, podendo reutilizar.

# ex
# classe:frutas
# objetos: Abacate, Banana...
'''
#Criando a primeira class
#obs: O nome da classe tem que iniciar com a letra maiúscula.
#ex:
class Funcionarios:
  nome = 'Elena'
  sobrenome = 'Cabral'
  data_nascimento = '12/01/2009'

usuario1 = Funcionarios()
print(usuario1.nome)
print(usuario1.sobrenome)


#Criando objetos dentro de uma classe
#Criar a classe
class Funcionarios:
  pass

#Criar o objeto
usuario1 = Funcionarios()

#crias os parâmetros
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/10/2009'

#print
print(usuario1.nome)

#obs: Colocando os dados de forma 'Individual' conseguimos criar um 'usuário2'

#Construtores (self -Gira dentro de todos os objetos que for criado)

#Criando a class
class Funcionarios:
  def __init__(self, nome, sobrenome, data_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.data_nascimento = data_nascimento

#Criando o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2000')
usuario2 = Funcionarios('Carol', 'Silvia','15/10/2000')

print(usuario1.nome)
print(usuario2.nome)
'''
'''
#Adicionando mais funções a classe
class Funcionarios:
  def __init__(self, nome, sobrenome, data_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.data_nascimento = data_nascimento

  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome

usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2000')
usuario2 = Funcionarios('Carol', 'Silvia','15/10/2000')

print(usuario1.nome_completo())
#ou
print(Funcionarios.nome_completo(usuario1))
'''
'''
#importando módulos
import funcoes #Importa tudo
funcoes.somar()
 #ou 
from funcoes import somar, multiplicar

somar()
'''