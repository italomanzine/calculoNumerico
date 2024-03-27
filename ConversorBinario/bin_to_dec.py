def binario_para_decimal(input_numero):
    # Substitui vírgulas por pontos para aceitar ambos os formatos de números decimais
    numero = input_numero.replace(',', '.')
    
    # Verifica se a entrada é um número binário válido (contém apenas 0, 1 e no máximo um ponto)
    if not all(c in '01.' for c in numero) or numero.count('.') > 1:
        return "Erro: Entrada inválida. Por favor, digite um número binário válido."

    # Divide o número binário em parte inteira e parte decimal
    partes = numero.split(".")
    parte_inteira = int(partes[0], 2)  # Converte a parte inteira de binário para decimal
    
    parte_decimal = 0
    # Se houver uma parte decimal, converte-a de binário para decimal
    if len(partes) > 1:
        for indice, digito in enumerate(partes[1], start=1):
            parte_decimal += int(digito) * (2 ** -indice)
    
    # Soma as partes inteira e decimal para obter o número decimal completo
    return parte_inteira + parte_decimal
