def binario_para_decimal(input_numero):
    # Substitui ',' por '.' para aceitar ambos os formatos de parte decimal
    numero = input_numero.replace(',', '.')
    
    # Verifica se a entrada é um número binário válido
    if not all(c in '01.' for c in numero) or numero.count('.') > 1:
        return "Erro: Entrada inválida. Por favor, digite um número binário válido."

    partes = numero.split(".")
    parte_inteira = int(partes[0], 2)
    
    parte_decimal = 0
    if len(partes) > 1:
        for indice, digito in enumerate(partes[1], start=1):
            parte_decimal += int(digito) * (2 ** -indice)
    
    return parte_inteira + parte_decimal
