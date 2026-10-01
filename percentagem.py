total=300;
utilizado=150;
percentagem_utilizada = (utilizado / total) * 100
print("Espaço total:", total, "GB")
print("Espaço utilizado:", utilizado, "GB")
print("Percentagem utilizada:", percentagem_utilizada, "%")
if percentagem_utilizada > 80:
    print("Aviso: O espaço utilizado excedeu 80 do total.")
else:
        print("O espaço utilizado está dentro do limite aceitável.")
