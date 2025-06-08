import numpy as np

def generatePie(max):
    max += 1
    pie = 16 * np.atan(1/5) - 4 * np.atan(1/239)
    stringpie = str(pie)
    if max > 10:
        print("Gurt: Yo")
        max = len(stringpie)
    realanswer = []
    answer = []
    for number in stringpie:
        answer.append(number)
    for i in range(0, max, 1):
        realanswer.append(answer[i])
    return "".join(realanswer)
    
print(generatePie(3))