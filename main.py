import time
import io

class Mots:
    def __init__(self, mot, parent):
        self.__parent = parent
        self.__mot = mot
        self.__enfants = {}
        self.__compteur = 0

    def get_enfants(self):
        return self.__enfants

    def get_compteur(self):
        return self.__compteur

    def get_mot(self):
        return self.__mot

    def add_mot(self, mot):
        if mot not in self.__enfants:
            self.__enfants[mot] = Mots(mot, self)
        self.__enfants[mot].__compteur += 1

        #Ajouter à liste_mots
        if mot not in liste_mots:
            liste_mots[mot] = []
            liste_mots[mot].append(self.__enfants[mot])

def ajouter_phrase(phrase):
    liste = phrase.split()
    mot = mot_originel
    for i in range(len(liste)):
        mot.add_mot(liste[i])
        mot = mot.get_enfants()[liste[i]]

def ajouter_dic(dic_path):
    txt = io.open(dic_path, encoding='ISO-8859-1').read()
    txt = txt.splitlines()
    for i in txt:
        ajouter_phrase(i)

def prediction(phrase):
    if not phrase[-1] in liste_mots:
        return False
    liste_mots_prediction = {}
    for i in liste_mots[phrase[-1]]:
        enfants = i.get_enfants()
        print(i.get_mot())
        total = 0
        max = (None, 0)

        #Set total and max
        for j in enfants.values():
            total += j.get_compteur()
            if max[1] < j.get_compteur():
                max = (j, j.get_compteur())
        print(max[0].get_mot(),  max[1]/total)

liste_mots = {}
mot_originel = Mots(None, None)
ajouter_dic("/home/maledict/Téléchargements/disk1.txt")

while True:
    phrase = str(input("Entrez votre phrase en anglais : "))
    print("==============================================================")
    for i in mot_originel.get_enfants()["Why"].get_enfants().values():
        print(i.get_mot(), i.get_compteur())
    print("==============================================================")
    print(liste_mots["Why"])

    """
    L'ajout des mots à liste_mots ne marche sûrement pas correctement ? 
    A tester plus en détail
    """