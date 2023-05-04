from algemene_functies import mijn_functie_2

# smaak prijs korting

def aanbieding_1(x,y,z):
    return ("Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak", x ,  ", van", y ,"euro voor 3,60 euro.")

print(aanbieding_1('aardbei', 4,0.1))


def inkomsten_totaal(inkomsten,btw):
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return ("Het totaal van alle inkomsten van deze week is", totaal,  "euro, waarover ",bedrag, "euro btw betaald dient te worden.")


print(inkomsten_totaal(1,0.09))

def laag_en_hoog(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    max_mijn_lijst = max(mijn_lijst)
    min_mijn_lijst = min(mijn_lijst)
    lijst = [max_mijn_lijst , min_mijn_lijst]
    return lijst

print(laag_en_hoog(1))

def gemiddelde(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    aantal = len(mijn_lijst)
    som = sum(mijn_lijst)
    gemiddelde_lijst = som / aantal
    return ("De gemiddelde inkomsten deze week zijn", gemiddelde_lijst , "euro.")

print(gemiddelde(1))

def meervoudig(invoer_lijst):
    x = laag_en_hoog(invoer_lijst)
    y = len(x)
    k = [10,5,3,2,1,2,9,y]
    max_w = max(k)
    min_w = min(k)
    waarde_lijst = [max_w , min_w]

    return waarde_lijst

# In de opdracht staat gebruik de functie hoog_en_laag(),""
# Ben er van uit gegaan dat dit de functie laag_en_hoog()"" uit de voorgaande' opdracht is.
print(meervoudig(1))

def combinatie(invoer_lijst_2):
    meervoudig(invoer_lijst_2)
    return meervoudig(invoer_lijst_2)
    


korte_lijst = combinatie(1)

print(mijn_functie_2(korte_lijst[0],korte_lijst[1]))





    





