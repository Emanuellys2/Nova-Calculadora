valormodelo = 1024
listadeunidades = ["bit", "byte", "kilobyte","megabyte", "gigabyte", "terabyte", "petabyte"]

def conversao(valorinicial, unidadeone, unidadetwo):
    print(f'resultado:({unidadeone} para {unidadetwo})')
    valorfinal = valorinicial
    if(unidadeone == "bit"):
        valorfinal = valorfinal / 8
        unidadeone = "byte"
    if(listadeunidades.index(unidadeone) < listadeunidades.index(unidadetwo)):
        for i in range(listadeunidades.index(unidadeone), listadeunidades.index(unidadetwo)):
            valorfinal = valorfinal / valormodelo
    else:
        for i in range(listadeunidades.index(unidadeone), listadeunidades.index(unidadetwo),-1):
            valorfinal = valorfinal * valormodelo
        if(unidadetwo == "bit"):
            valorfinal = (valorfinal / valormodelo) *8
            return print (valorfinal)
        
        valormodelo = input("insira um valor: ")
        unidadeone = input(f"insira a unidade necessaria: {listadeunidades}: ")

        while not unidadeone in listadeunidades:
            unidadeone = input(f"insira a unidade inicial {listadeunidades}: ")
        
        unidadetwo = input(f"insira a unidade a ser convertida {listadeunidades}: ")

        while not unidadetwo in listadeunidades:
            unidadetwo = input(f"insira a unidade final {listadeunidades}: ")

            valorfinal = conversao(int (valormodelo) , unidadeone , unidadetwo)            
