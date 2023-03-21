class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    DARKCYAN = '\033[36m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    ENDC = '\033[0m'


quality = [
    bcolors.GREEN+"Boa"+bcolors.ENDC,
    bcolors.YELLOW+"Moderada"+bcolors.ENDC,
    bcolors.PURPLE+"Ruim"+bcolors.ENDC,
    bcolors.RED+"Muito Ruim"+bcolors.ENDC,
    bcolors.DARKCYAN+"Pessima"+bcolors.ENDC
    ]

description = [
    "",
    "Pessoas de grupos sensíveis (crianças, idosos e\npessoas com doenças respiratórias e cardíacas)\npodem apresentar sintomas como tosse seca e\ncansaço. A população, em geral, não é afetada.",
    "Toda a população pode apresentar sintomas como\ntosse seca, cansaço, ardor nos olhos, naris e\ngarganta. Pessoas de grupos sensíveis (crianças,\nidosos e pessoas com doenças respiratórias e\ncardíacas) podem apresentar efeitos mais sérios na\nsaúde.",
    "Toda a população pode apresentar agravamento dos\nsintomas como tosse seca, cansaço, ardor nos olhos,\nnariz e garganta e ainda falta de ar e respiração\nofegante. Efeitos ainda mais graves à saúde de\ngrupos sensíveis (crianças, idosos e pessoas com\ndoenças respiratórias e cardíacas).",
    "Toda a população pode apresentar sérios riscos de\nmanifestação de doenças respiratórias e\ncardiovasculares. Aumento de mortes prematuras\nem pessoas de grupos sensíveis."
]

def classify(data):
    res = []
    if (int(data[0]) <= 50): res.append(0)
    elif (int(data[0]) > 50 and int(data[0]) <= 100): res.append(1)
    elif (int(data[0]) > 100 and int(data[0]) <= 150): res.append(2)
    elif (int(data[0]) > 150 and int(data[0]) <= 250): res.append(3)
    elif (int(data[0]) > 250): res.append(4)

    if (int(data[1]) <= 25): res.append(0)
    elif (int(data[1]) > 25 and int(data[1]) <= 50): res.append(1)
    elif (int(data[1]) > 50 and int(data[1]) <= 75): res.append(2)
    elif (int(data[1]) > 75 and int(data[1]) <= 125): res.append(3)
    elif (int(data[1]) > 125): res.append(4)

    if (int(data[2]) <= 100): res.append(0)
    elif (int(data[2]) > 100 and int(data[2]) <= 130): res.append(1)
    elif (int(data[2]) > 130 and int(data[2]) <= 160): res.append(2)
    elif (int(data[2]) > 160 and int(data[2]) <= 200): res.append(3)
    elif (int(data[2]) > 200): res.append(4)

    if (int(data[3]) <= 9): res.append(0)
    elif (int(data[3]) > 9 and int(data[3]) <= 11): res.append(1)
    elif (int(data[3]) > 11 and int(data[3]) <= 13): res.append(2)
    elif (int(data[3]) > 13 and int(data[3]) <= 15): res.append(3)
    elif (int(data[3]) > 15): res.append(4)

    if (int(data[4]) <= 200): res.append(0)
    elif (int(data[4]) > 200 and int(data[4]) <= 240): res.append(1)
    elif (int(data[4]) > 240 and int(data[4]) <= 320): res.append(2)
    elif (int(data[4]) > 320 and int(data[4]) <= 1130): res.append(3)
    elif (int(data[4]) > 1130): res.append(4)

    if (int(data[5]) <= 20): res.append(0)
    elif (int(data[5]) > 20 and int(data[5]) <= 40): res.append(1)
    elif (int(data[5]) > 40 and int(data[5]) <= 365): res.append(2)
    elif (int(data[5]) > 365 and int(data[5]) <= 800): res.append(3)
    elif (int(data[5]) > 800): res.append(4)
        
    finalres = max(res)
    print("\nClassificação: "+quality[finalres])
    print(description[finalres])