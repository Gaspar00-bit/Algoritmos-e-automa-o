def procurar_palavra(nome_arquivo, palavra):

    resultados = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        for numero, linha in enumerate(arquivo, start=1):

            if palavra.lower() in linha.lower():

                resultados.append({
                    "linha": numero,
                    "texto": linha.strip()
                })

    return resultados

resultados = procurar_palavra(
    "servidor.log",
    "error"
)

for resultado in resultados:

    print(
        resultado["linha"],
        resultado["texto"]
    ) 
    resultados = procurar_palavra(
    "servidor.log",
    "warning"
)

for resultado in resultados:

    print(
        resultado["linha"],
        resultado["texto"]
    ) 