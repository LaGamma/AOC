import sys                                                  
from functools import reduce                                
                                                             
LINES = [i.strip() for i in open("day21.txt").readlines()]

                                                             
def one():                                                  
    allergens = dict()                                      
    all_count = []                                          
    ings = []                                               
    for line in LINES:                                      
        a, b = line.split(" (contains ")                    
        ing = a.split()                                     
        ings += ing                                         
        alg = [i.strip() for i in b[:-1].split(",")]        
        all_count += alg                                    
        for a in alg:                                       
            if a not in allergens:                          
                allergens[a] = set(ing)                     
            else:                                           
                allergens[a] = set(ing) & allergens[a]      
                                                             
    while any([len(i) > 1 for i in allergens.values()]):    
        for a, i in allergens.items():                      
            if len(i) == 1:                                 
                alg = list(i)[0]                            
                for a2, i2 in allergens.items():            
                    if a2 == a:                             
                        continue                            
                    if len(i2) > 1:                         
                        if alg in i2:                       
                            allergens[a2].remove(alg)       
                                                             
                                                             
    algs = reduce(lambda x, y: x | y, allergens.values())   
    print(allergens)                                        
    print(len([i for i in ings if i not in algs]))          
                                                             
    names = list(allergens.keys())                          
    names.sort()                                            
    print(",".join([",".join(allergens[i]) for i in names]))
one()   