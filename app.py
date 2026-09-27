#Pesquisa de Opinião

#Contador de opiniões
Excelente_count = 0
Ruim_count = 0

#Número de pesquisas a serem realizadas
for i in range(50):

#Informações dos clientes
    nome = input("Nome:")
    idade = int(input("Idade:"))
    opinião = input("Opinião sobre nosso atendimento? (\"Excelente\", \"Bom\", \"Ruim\"): ")

#Estrutura
    if opinião == "Excelente":
        Excelente_count += 1
    elif opinião == "Bom":
        pass
    elif opinião == "Ruim":
        Ruim_count += 1
print("Número de opiniões Excelente:", Excelente_count, 
      "Número de opiniões Ruim:", Ruim_count)