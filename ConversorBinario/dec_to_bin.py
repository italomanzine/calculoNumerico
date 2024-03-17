def decimal_para_binario(input_numero):
    try:
        # Substitui vírgulas por pontos e tenta converter para float
        numero = float(input_numero.replace(',', '.'))
    except ValueError:
        return "Erro: Entrada inválida. Por favor, digite um número decimal válido."
    
    parte_inteira = int(numero)
    parte_decimal = numero - parte_inteira
    binario_inteiro = bin(parte_inteira).replace("0b", "")
    
    binario_decimal = ""
    while parte_decimal > 0:
        parte_decimal *= 2
        if parte_decimal >= 1:
            binario_decimal += "1"
            parte_decimal -= 1
        else:
            binario_decimal += "0"
        if len(binario_decimal) > 10:  # Limita a precisão a 10 casas decimais.
            break
    
    return binario_inteiro + ("." + binario_decimal if binario_decimal else "")

