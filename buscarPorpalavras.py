def buscar_por_palavras(palavras):
    quantidade_erros = 0
    with open('servidor.log', 'r') as f:
        for line in f:
            if any(palavra in line for palavra in palavras):
                quantidade_erros += 1
    return quantidade_erros
quantidade_erros = buscar_por_palavras(['error', 'warning'])
print(f'Quantidade de erros encontrados: {quantidade_erros}')