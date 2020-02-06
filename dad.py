
#Variables
Messures_L = float(input("Entrer la longeure: "))     
Messures_H = float(input("Entrer la hauteure: "))       
Quantity = float(input("Entrer la quantite: ")) 



#Functions & Main Loop
def Dormant():
    Dormant = 2 * float(Messures_L) + 2 * float(Messures_H)
    print("Tu aurra besoin de: " +str(Dormant) + " Dormant")
    return     
Dormant()

def Chicass():
    Chicass = 2 * float(Messures_H)
    print("Tu aurra besoin de: " + str(Chicass) + " Chicasses")
    return
Chicass() 

def Hoja():
    Hoja = str(Dormant) + str(Chicass)
    print("Tu aurra besoin de: " + str(Hoja) + " Hoja")
    return
Hoja()

def TJ():
    str(TJ) == str(Dormant)
    print("Tu aurra besoin de: " + str(TJ) + " TapaJontas")
    return
TJ()

def Kit():
    str(Kit) == str(Quantity)
    print("Tu aurra besoin de: " + str(Kit) + " Kit")
    return
Kit()

def Roullettes():
    str(Roullettes) == 4 * str(Quantity)
    print("Tu aurra besoin de: " + str(Roullettes) + " Roullettes")
    return

def Fermeture():
    str(Fermeture) == 2 * str(Quantity)
    print("Tu aurra besoin de: " + str(Fermeture) + " Fermetures")
    return
Fermeture()

def Equerre_D():
    str(Equerre_D) == 4 * str(Quantity)
    print("Tu aurra besoin de: " + str(Equerre_D) + "Equerres D")
    return
Equerre_D()

def Equerre_H():
    str(Equerre_H) == 8 * str(Quantity)
    print("Tu aurra besoin de: " + str(Equerre_H) + " Equerres H")
    return
Equerre_H()

def Equerre_TJ():
    str(Equerre_TJ) == 4 * str(Quantity)
    print("Tu aurra besoin de: " + str(Equerre_TJ) + " Equerres TJ")
    return
Equerre_TJ()

def Grappa():
    str(Grappa) == str(Messures_L) * 4 + str(Messures_H) * 4
    print("Tu aurra besoin de: " + str(Grappa) + " Grappas")
    return
Grappa()

def Brosse(): 
    str(Brosse) == float(str(Messures_H)) * 6.4 * 3 + float(str(Chicass)) * 6.4 * 3
    print("Tu aurra besoin de: " + str(Brosse) + " Brosses")
    return
Brosse()

def Juint_Vitrage():
    str(Juint_Vitrage) == int(Messures_H) * 6.4
    print("Tu aurra besoin de: " + str(Juint_Vitrage) + " Juint_Vitrage")
    return 
Juint_Vitrage()

