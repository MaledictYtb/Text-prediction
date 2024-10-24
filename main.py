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

    def get_parent(self):
        return self.__parent

    def get_compteur(self):
        return self.__compteur

    def get_mot(self):
        return self.__mot

    def add_mot(self, mot):
        if mot not in self.__enfants:
            self.__enfants[mot] = Mots(mot, self)
            if mot not in liste_mots:
                liste_mots[mot] = []
            liste_mots[mot].append(self.__enfants[mot])

        self.__enfants[mot].__compteur += 1

def ajouter_phrase(phrase):
    liste = (phrase
                .replace('"', '')
                .replace('[noise]', '')
            .split())
    mot = mot_originel
    for i in range(len(liste)):
        mot.add_mot(liste[i])
        mot = mot.get_enfants()[liste[i]]

def ajouter_dic(dic_path, lines=0):
    txt = io.open(dic_path, encoding='utf-8').read().replace('.', '').lower().splitlines()
    if lines == 0:
        lines = len(txt)

    for i in range(lines):
        ajouter_phrase(txt[i])

def most_probable_word(phrase):
    liste_mots_prediction = []  # (class mot, probabilité, mot)
    for i in liste_mots[phrase[-1]]:
        enfants = i.get_enfants()
        total = 0
        max = (None, 0)

        # Check if there's enfants, because of errors if there's none
        if enfants == {}:
            continue

        # Set total and max
        for j in enfants.values():
            total += j.get_compteur()
            if max[1] < j.get_compteur():
                max = (j, j.get_compteur())
        liste_mots_prediction.append([max[0], max[1] / total, max[0].get_mot()])
    return liste_mots_prediction

def nb_correspondances(phrase, mot):
    compteur = 0
    mot = mot.get_parent()
    for i in range(len(phrase) - 1, -1, -1):
        if phrase[i] == mot.get_mot():
            compteur += 1
        if mot.get_parent() is None:
            break
        mot = mot.get_parent()
    return compteur

def prediction(phrase):
    phrase = phrase.split()
    #Pre condition
    if not phrase:
        return False
    if not phrase[-1] in liste_mots:
        return False

    #List all most probable words
    liste_mots_prediction = most_probable_word(phrase)

    #Ajoute le nombre de mots précédents qui correspondent à la phrase à liste_mots_prediction
    for i in range(len(liste_mots_prediction)):
        mot = liste_mots_prediction[i][0]
        liste_mots_prediction[i].append(nb_correspondances(phrase, mot))

    liste_mots_prediction.sort(key=lambda x: (x[3], x[1]), reverse=True)

    if liste_mots_prediction is None:
        return False
    return liste_mots_prediction[0][2], liste_mots_prediction[0][3]




liste_mots = {}
mot_originel = Mots(None, None)
start = time.time()

ajouter_dic("data/french/FR_CID_train.txt")
ajouter_dic("data/french/FR_CLAPI_train.txt")
ajouter_dic("data/french/FR_ESLO_free_train.txt")
ajouter_dic("data/french/FR_LINAGORA_free_train.txt")
ajouter_dic("data/french/FR_OFROM_train.txt")
ajouter_dic("data/french/FR_ORFEO_coralrom_train.txt")
ajouter_dic("data/french/FR_ORFEO_crfp_train.txt")
ajouter_dic("data/french/FR_ParisStories_train.txt")
ajouter_dic("data/french/FR_PFC_free_train.txt")
ajouter_dic("data/french/FR_Rhapsodie_train.txt")

ajouter_dic("data/english/sms.txt", 1000000)

stop = time.time()
print(stop-start)



while True:
    phrase = str(input("Entrez votre phrase en français : "))
    print(prediction(phrase))
