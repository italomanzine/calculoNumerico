from dec_to_bin import decimal_para_binario
from bin_to_dec import binario_para_decimal

def opcao_decimal_para_binario():
    input_numero = input("Digite um número decimal: ")
    resultado = decimal_para_binario(input_numero)
    print(f"Resultado Binário: {resultado}")

def opcao_binario_para_decimal():
    input_numero = input("Digite um número binário: ")
    resultado = binario_para_decimal(input_numero)
    print(f"Resultado Decimal: {resultado}")

def sair():
    print("Saindo do programa...")
    exit()

def opcao_invalida():
    print("Opção inválida! Tente novamente.")

def exibir_menu():
    opcoes = {
        '1': opcao_decimal_para_binario,
        '2': opcao_binario_para_decimal,
        '3': sair
    }
    while True:
        print("\nConversor Decimal ↔ Binário")
        print("1. Decimal para Binário")
        print("2. Binário para Decimal")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        # Executa a função correspondente à escolha ou opcao_invalida se não encontrada
        opcoes.get(escolha, opcao_invalida)()

if __name__ == "__main__":
    exibir_menu()