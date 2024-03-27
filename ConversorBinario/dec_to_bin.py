def decimal_para_binario(input_numero):
    try:
        # Substitui vírgulas por pontos e tenta converter a string para float
        numero = float(input_numero.replace(',', '.'))
    except ValueError:
        # Se a conversão falhar, retorna uma mensagem de erro
        return "Erro: Entrada inválida. Por favor, digite um número decimal válido."
    
    # Separa o número em parte inteira e parte decimal
    parte_inteira = int(numero)
    parte_decimal = numero - parte_inteira
    # Converte a parte inteira para binário e remove o prefixo '0b'
    binario_inteiro = bin(parte_inteira).replace("0b", "")
    
    # Inicializa a string da parte decimal binária
    binario_decimal = ""
    # Converte a parte decimal para binário
    while parte_decimal > 0:
        # Multiplica a parte decimal por 2 e adiciona '1' ou '0' dependendo do resultado
        parte_decimal *= 2
        if parte_decimal >= 1:
            binario_decimal += "1"
            parte_decimal -= 1
        else:
            binario_decimal += "0"
        # Limita a precisão da parte decimal binária a 10 dígitos
        if len(binario_decimal) > 10:
            break
    
    # Combina as partes inteira e decimal binárias para formar o número binário completo
    return binario_inteiro + ("." + binario_decimal if binario_decimal else "")
