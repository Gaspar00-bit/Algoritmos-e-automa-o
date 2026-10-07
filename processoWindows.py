processo=[("chrome",55,2),("safari",10,1),("php",60,3),("sql",70,4)]
for nome,cpu,ram in processo:
   
    if cpu>50 & ram>2:
        print(nome,"usa",cpu,"e ram",ram, "% de cpu ")
        print("Alerta de consumo de cpu")
    else:
        print(nome,"usa",cpu,"e ram",ram,"% de cpu ")
        print("CPU Estavel") 