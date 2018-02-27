import pymongo
import json

#Our connection method works thus
#connect to homer
#create a db called PoGoDex
#make a collection called pokemon

#Dataset is already a list of dictionaries, so we can directly do insert_many with it
#Downloaded from https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
#Contains stats and info of all Pokemon

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.PoGoDex
collection = db.pokemon

def print_curs(cursor):
    l=[]
    for d in cursor:
        print d
        l.append(d)
    return l
        

def find(pokemon):
    data= collection.find({"name" : pokemon })
    return print_curs(data)


def findid(ID):
    data = collection.find({ "id" : ID})
    return print_curs(data)
   

def findevo(evo):
    data = collection.find({ "next_evolution.name"  :evo })
    return print_curs(data)
   
    


    










    
