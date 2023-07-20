

 
def presenteer(totaal):
    #totaal = {'vis' : 10, 'vlees': 25, 'overig' : 15}
    for k, v in dict.items(totaal):  
        print(k, v,"euro")
    try:
        totaal = sum(dict.values(totaal))
    except:
        print("error")
    #for k, v in mijn_dict.items():  
       # print(k, v,"euro")
    print('==========================')
    print('Totaal =',totaal, 'euro')
    return totaal

x = {'vis' : 10, 'vlees': 25, 'overig' : 15}

presenteer(x)

    
    


   





