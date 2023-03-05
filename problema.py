# Um gerente de uma empresa irá propor um aumento de salário aos seus funcionários que possuem salário inferior a R$ 2000,00, em 15%. Para isso, ele precisa de um programa que calcule o total dos salarios dos funcionarios, calcule quantos funcionários receberão o aumento e qual será o valor do aumento.


from functools import reduce
    
# Criando uma lista com os salarios dos funcionarios
salarios = [1000, 1800, 1750, 1900, 3000]
# Somando os salarios
somaSalarios = reduce(lambda x,y:x+y, salarios)
# Contando quantos funcionarios receberão o aumento
funcionariosAumento = len(list(filter(lambda x:x < 2000, salarios)))
# Fazendo o aumento de salario
salarioAumento = list(map(lambda x:x*1.15 if x < 2000 else x, salarios))
# Somando os salarios com o aumento
somaSalariosAumento = reduce(lambda x,y:x+y, salarioAumento)
# Calculando o valor do aumento
valorAumento = somaSalariosAumento - somaSalarios


print(f"O valor total dos salarios é de R$ {somaSalarios}")
print(f"O valor total dos salarios com o aumento é de R$ {somaSalariosAumento}")
print(f"O valor do aumento é de R$ {valorAumento}")
print(f"{funcionariosAumento} funcionários receberão o aumento")







