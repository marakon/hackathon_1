import time

class Ekwipunek:
    def __init__(self):
        self._hajs = 20
        self._itemy = ['kompas', 'latarka', 'spiwor']
        self._jedzenie = ['jablko', 'woda', 'batonik', 'batonik']
        self._sakwa = {
            'cash': self._hajs,
            'items': self._itemy,
            'food': self._jedzenie
        }

    @property 
    def sakwa(self):
        return self._sakwa

    @property
    def itemy(self):
        return self._itemy

    @property
    def jedzenie(self):
        return self._jedzenie

    @property
    def hajs(self):
        return self._hajs

    @hajs.setter
    def hajs(self, hajs):
        self._hajs = hajs

    
class Sklep:
    def __init__(self):
        self._itemy = {
            'karimata': 29.99,
            'finka': 49.99,
            'batonik': 2.99,
            'guma': 0.99
        }

    @property
    def itemy(self):
        return self._itemy

def kupno(cena, rzecz, lista, hajsik, asortyment):
    if cena > hajsik:
        print("Nie masz kasy...")
        return
    asortyment.pop(rzecz)
    hajsik = hajsik - cena
    print('Zostało Ci w sakiewce: {0}'.format(hajsik))
    print("Kupujesz {0} za {1}.".format(rzecz, cena))
    lista.append(rzecz)

def main():
#========================================================================================================#
    ekwipunek_harcerza = Ekwipunek()
    sklep = Sklep()
    asortyment = sklep.itemy
    sakwa = ekwipunek_harcerza.sakwa
    (hajsik, jedzenie, rzeczy) = (sakwa['cash'], sakwa['food'], sakwa['items'])
#========================================================================================================#
    print('Ekwipunek bez formatowania: {0}'.format(ekwipunek_harcerza.sakwa))
    print("Wybierasz się na wyprawę harcerską!")
    print('Mamuśka zapakowała Ci do sakwy:\nHajsiku: {0}'.format(hajsik))
    print("Rzeczy: ")
    for cos in rzeczy:
        print('\t- {0}'.format(cos))
    print('Jedzenie:')
    for foodie in jedzenie:
        print('\t- {0}'.format(foodie))
    time.sleep(2)
    print("Ruszacie i trafiacie do sklepu.")
    time.sleep(1)
#========================================================================================================#
    action = input('Wchodzisz czy czekasz?: ')
    while True:
        if action.lower() == "wchodze":
            for item in asortyment:
                print('- {0}'.format(item))
            print("Kupujesz coś?")
            while True:
                dec = input("T/N: ")
                if dec.upper() == "T":
                    item = input("Co kupujesz?: ")
                    if item in asortyment:
                        cena = asortyment.get(item)
                        if item in ['batonik', 'guma']:
                            kupno(cena, item, jedzenie, hajsik, asortyment)
                        elif item in ['karimata', 'finka']:
                            kupno(cena, item, rzeczy, hajsik, asortyment)
                        break
                elif dec.upper() == 'N':
                    print("Wychodzisz")
                    break
                else:
                    
                    continue
            break
        if action.lower() == "czekam":
            time.sleep(5)
            print("Klasycznie kazdy potrzebuje 2 lata na zakupy...")
            time.sleep(5)
            print("Nareszcie... Ruszacie dalej...")
            break
        else:
            action = input('No wchodzisz czy czekasz?: ')
            continue
#========================================================================================================#
    time.sleep(3)
    print("Zgłodniałeś!")
    time.sleep(2)
    print("Zaglądasz do plecaka aby zobaczyć co masz.")
    time.sleep(2)
    print('W plecaku:')
    for food in jedzenie:
        print('- {0}'.format(food))
    for rzecz in rzeczy:
        print('- {0}'.format(rzecz))
    time.sleep(2)
    while True:
        rzecz = input("Co zjesz?: ")
        if rzecz in rzeczy:
            print("To jest niejadalne ziomek!")
            continue
        if rzecz not in jedzenie:
            print("Przeciez nie ma tego w plecaku!")
            continue
        elif rzecz == 'woda':
            print("Woda sie nie najesz...")
            continue
        elif rzecz == 'batonik':
            print("Mmmm pyszny batonik!")
            jedzenie.remove(rzecz)
            break
        elif rzecz == 'jablko':
            print("Mmmmm zdrowe jablko!")
            jedzenie.remove(rzecz)
            break
    time.sleep(3)
    print("Twoja sakwa zawiera: ")
    print("Jedzenie: ")
    for item in jedzenie:
        print('- {0}'.format(item))
    print("Rzeczy:")
    for item in rzeczy:
        print('- {0}'.format(item))
    time.sleep(4)
    print("I szliście daleko i szczęśliwie.")


main()
