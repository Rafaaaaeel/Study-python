my_list = [5,1,3,7,2]
print(my_list, 'Original')

 

print(my_list, 'New')
my_dict = {'car':4,'dog':2,'add':3,'bee':1}

my_tuple = ('d','c','e','a','b')

my_string = 'python'

print(tuple(sorted(my_tuple)))
# List
#Sorted vai criar uma nova lista com os valores crescentes, mas a lista original manetem
#Sort ira deixar lista com os valores em ordem crescente

#Tuple
#Sorted Na tuple ele ordena os valores mas transforma em uma lista

#String
#O sorted ira crirar uma lista com os valores do texto separdos em ordem crescente

#Dicionario
#Em um dicionario sera excluido o valor, apenas sera mantido o valor do indice
#Para manter os valores sera preciso usar .items() dessa forma sera criado uma lista separando cada valor de cada indice em uma tuple

#Reversed
#Atalho [::-1]

#Outros exemplos

#Uso da Key

my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = abs))

#Lambda function

print(sorted(my_llist, key = lambda item :item[2] ))


