# Importa funções de conversão de outros arquivos
from dec_to_bin import decimal_para_binario
from bin_to_dec import binario_para_decimal

# Função para converter de decimal para binário
def opcao_decimal_para_binario():
    input_numero = input("Digite um número decimal: ")  # Solicita ao usuário um número decimal
    resultado = decimal_para_binario(input_numero)  # Converte o número decimal para binário
    print(f"Resultado Binário: {resultado}")  # Exibe o resultado da conversão

# Função para converter de binário para decimal
def opcao_binario_para_decimal():
    input_numero = input("Digite um número binário: ")  # Solicita ao usuário um número binário
    resultado = binario_para_decimal(input_numero)  # Converte o número binário para decimal
    print(f"Resultado Decimal: {resultado}")  # Exibe o resultado da conversão

# Função para sair do programa
def sair():
    print("Saindo do programa...")  # Exibe uma mensagem de despedida
    exit()  # Encerra o programa

# Função chamada quando uma opção inválida é escolhida
def opcao_invalida():
    print("Opção inválida! Tente novamente.")  # Informa ao usuário que a opção escolhida é inválida

# Função que exibe o menu principal e lida com a navegação do usuário
def exibir_menu():
    opcoes = {
        '1': opcao_decimal_para_binario,  # Opção de conversão de decimal para binário
        '2': opcao_binario_para_decimal,  # Opção de conversão de binário para decimal
        '3': sair  # Opção de saída do programa
    }
    while True:  # Loop infinito para manter o programa em execução
        print("\nConversor Decimal ↔ Binário")
        print("1. Decimal para Binário")
        print("2. Binário para Decimal")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção
        
        # Executa a função correspondente à escolha ou opcao_invalida se não encontrada
        opcoes.get(escolha, opcao_invalida)()

# Ponto de entrada do programa; se este arquivo for executado, exibir_menu() será chamado
if __name__ == "__main__":
    exibir_menu()
