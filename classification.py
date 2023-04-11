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

def grade(data, reg1, reg2, reg3, reg4):
    if (int(data) <= reg1): return 0
    elif (int(data) > reg1 and int(data) <= reg2): return 1
    elif (int(data) > reg2 and int(data) <= reg3): return 2
    elif (int(data) > reg3 and int(data) <= reg4): return 3
    elif (int(data) > reg4): return 4

def classify(data):
    res = []
    res.append(grade(data[0], 50, 100, 150, 250))
    res.append(grade(data[1], 25, 50, 75, 125))
    res.append(grade(data[2], 100, 130, 160, 200))
    res.append(grade(data[3], 9, 11, 13, 15))
    res.append(grade(data[4], 200, 240, 320, 1130))
    res.append(grade(data[5], 20, 40, 365, 800))
        
    finalres = max(res)
    print("\nClassificação: "+quality[finalres])
    print(description[finalres])

testData = [
    [0, 0, 0, 0, 0, 0],
    [50, 25, 100, 9, 200, 20],
    [51, 0, 0, 0, 0, 0],
    [100, 26, 0, 0, 0, 0],
    [0, 0, 131, 0, 0, 0],
    [0, 0, 160, 12, 0, 0],
    [0, 0, 0, 0, 321, 0],
    [0, 0, 0, 0, 1130, 366],
    [251, 0, 0, 0, 0, 0],
    [251, 126, 0, 0, 0, 0]
]

for data in testData:
    classify(data)