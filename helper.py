def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):     
    bedrag_pp = bedrag/personen           
    return "Het bedrag per persoon is" , bedrag_pp , "euro"

b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))


print(fooi_pp(b,p))

def onderstreep(tekst):
    uit = []
    uit.append(tekst)
    try:
        uit.append(len(tekst) * "=")
    except:
        uit.append((tekst) * "=")
    return uit
    

print(onderstreep(10))

def som(x):

    try:
        x = sum(dict.values(x))
    except:
        print("niet mogelijk?")

    return x
