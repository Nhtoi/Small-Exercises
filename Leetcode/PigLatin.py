def piglating(sentence):
    vowels = "a,e,i,o,u"
    blends = ["bl","cl","fl","gl","pl","sl","br","cr","dr","fr","gr","pr","tr","ch","sh","th","wh","sk","sm","sn","sp","st","sw","tw","wr","sc"]
    words = sentence.split(" ")
    pigsentence = []
    for word in words:
        w = word.lower()
        if w[0] in vowels:
            pigword = word + "way"
        elif w[:2] in blends:
            pigword = word[2:] + word[:2] + "ay"
        else:
            pigword = word[1:] + word[0] + "ay"
        pigsentence.append(pigword)
    return " ".join(pigsentence)

def getUserinpit():
    phrase = input("Say the prhase you want to translate: ")
    print(piglating(phrase))
getUserinpit()