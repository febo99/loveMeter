import random

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

        if(podobnost > 100):#ŽL-varovalka, da ne presežemo 100%
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
    podobnost = int(round((len(imeFant)+len(imePunca)) * random.uniform(1,2)))
    print(izracun(podobnost,stevecFant,stevecPunca))


if __name__ == "__main__":
    main()