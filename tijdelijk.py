from helper import decoreer

def print_aanbieding():

    prijzen = {
        "aardbei" : 3 ,
        "vanille" : 4 ,
        "chocolade" : 5 
    }

    aanbieding_prijs = prijzen["vanille"] * 0.8
    aanbieding = "3.20"
    reclame_tekst = ("Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts €" + aanbieding)
    # 4  * 0.8 geeft 3.2 - In het voorbeeld staat dat er 2.4... moet komen, maar dan zou het om aardbei moeten gaan die de waarde 3 heeft.

    reclame_tekst2 = (reclame_tekst[:62])
    reclame_tekst3 = (reclame_tekst2).upper()
    reclame_tekst4 = ['VANDAAG', 'IN', 'DE', 'AANBIEDING:', 'VANILLE-IJS,', '1', 'LITER', '–', 'SLECHTS', '€' + aanbieding]

    for el in reclame_tekst4:
        
        if el[4:]:
            print(el)
            
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()




