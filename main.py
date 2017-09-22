import random
import pygame
import sys
abeceda = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
def preveriZnak(ime,stevec = []):#ŽL-Preverjanje znakov v stringu abeceda
    for i in range(len(ime)):
        for j in range(len(abeceda)):
            if(ime[i] == abeceda[j]) or (ime[i] == abeceda.lower()[j]): #ŽL-Preverja abecedo in abecedo lower case
                stevec[j] = stevec[j] + 1

    return stevec

def izracun(podobnost,stevecFant, stevecPunca):
    #ŽL-For zanka za ugotavljanje kolikokrat se določena črka ponovi
    for i in range(len(abeceda)):
        if((stevecFant[i] > 0) and (stevecPunca[i] > 0)): #ŽL-Preverimo če se obe črki pojavita
            if(stevecFant[i] == stevecPunca [i]):#ŽL-Preverimo če se pojavita istokrat
                podobnost = podobnost + ((stevecFant[i]+stevecPunca[i]) * 10)#ŽL-če se, dodamo vrednost k podobnosti
            else:
                if(stevecFant[i]-stevecPunca[i] > 0):#ŽL-če se ne pojavita istokrat, preverjamo katera se pojavi večkrat da ne dobimo negatvnega števila
                    podobnost = podobnost +(stevecFant[i] - stevecPunca[i])
                else:
                    podobnost = podobnost + (stevecPunca[i] - stevecFant[i])
        else:#ŽL-pogledamo za znake ki se pojavijo samo v enem imenu
            if((stevecFant[i] > 0) and (stevecPunca == 0)):#ŽL-znaki se pojavijo le pri fantu
                podobnost = podobnost - stevecFant[i]
            elif((stevecPunca[i] > 0) and (stevecFant == 0)):#ŽL-znaki se pojavijo le pri punci
                podobnost = podobnost - stevecPunca[i]
            if(podobnost > 100):
                podobnost = 100
    return podobnost
def main():
    stevecFant = []
    stevecPunca = []
    for i in range(25):
        stevecFant.append(0)
        stevecPunca.append(0)
    imeFant = input("Vnesi ime fanta: \n")
    imePunca = input("Vnesi ime punce: \n")
    preveriZnak(imeFant,stevecFant)
    preveriZnak(imePunca,stevecPunca)
    podobnost = int(round((len(imeFant) + len(imePunca)) * random.uniform(1, 2)))
    print(izracun(podobnost,stevecFant,stevecPunca))
    besedilo = "Vajina ljubezen je: " + str(izracun(podobnost,stevecFant,stevecPunca)) + "%"#ŽL-int v string
    #ŽL-PyGame knjižnica za izris grafa
    pygame.init()
    ozadje = (203, 218, 242)
    velikost = sirina, dolzina, = 600,300
    okno = pygame.display.set_mode((velikost))
    pygame.display.set_caption("Love Meter")
    okno.fill(ozadje)
    pisava = pygame.font.SysFont("comicsans", 60)
    tekst = pisava.render(besedilo,1,(239, 11, 7))
    ime1 = pisava.render(imeFant,1,(239,11,7))
    ime2 = pisava.render(imePunca,1,(239,11,7))
    ura = pygame.time.Clock()
    pygame.display.update()
    while 1:
        ura.tick(70)
        events = pygame.event.get()
        okno.blit(tekst,(85,230))
        okno.blit(ime1,(85,100))
        okno.blit(ime2, (310, 100))
        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.update()
if __name__ == "__main__":
    main()