# -*- coding: utf-8 -*-
def commande(cara):
    com = cara[8:][0]
    i = 9
    while cara[i] != ":" and len(com) < len(cara):
        com += cara[i]
        i += 1
    return(com.rstrip(" "))

def reponse(cara):
    return(cara[11+len(commande(cara)):])

def question():
    with open('question.txt', 'r+') as f1:
            qst = f1.readline().strip()
            lines = f1.readlines()
            f1.seek(0)
            f1.writelines(lines[0:])
            f1.truncate()
            f1.close()
    return(qst)