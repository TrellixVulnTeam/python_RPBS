nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionários.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("==============Verifique os tipos de dados abaixo:==============")

print("O tipo de dado na variável [nome] é: ", type(nome))
print("O tipo de dado na variável [empresa] é: ", type(empresa))
print("O tipo de dado na variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado na variável [mediaMensalidade] é: ", type(mediaMensalidade))
