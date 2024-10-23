import time
import io

mots = {}
# Dictionnaire de mots qui contient un dictionnaire des mots qui suivent

txt = io.open("/home/maledict/Téléchargements/disk1.txt", encoding='ISO-8859-1').read()
txt = txt.splitlines()


for i in range(len(txt)):
    liste = txt[i].split()
    for j in range(1, len(liste)):
        if liste[j-1] not in mots :
            mots[liste[j-1]] = {liste[j]: 0}

        if liste[j] not in mots[liste[j-1]]:
            mots[liste[j - 1]][liste[j]] = 0
        mots[liste[j-1]][liste[j]] += 1

while True:
    preprediction = str(input("Saisissez un mot en anglais : ")).split()[0]
    mots = mots[preprediction]
    print(mots)
    mots = sorted(mots.items(), key=lambda item: item[1], reverse=True)
    print(mots)