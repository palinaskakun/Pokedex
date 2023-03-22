# =============================================================================
# Programming Project 9 
# Algorithm:
#   read a file with information on pokemon video game
#   build a nested dictionary 
#   loop prompting for a valid option
#   call the specific function to display the data corresponding to the option
# 
# =============================================================================
import csv,copy


EFFECTIVENESS = {0.25: "super effective", 0.5: "effective", 1:"normal",
                 2:"weak", 4:"super weak", 0:"resistant"}
MATCHUP_TYPES = {"resistant", "super effective", "effective", "normal",
                 "weak", "super weak"}
PROMPT = '''
\nTo make a selection, please enter an option 1-3:\n
\tOPTION 1: Find Pokemon
\tOPTION 2: Find Pokemon From Abilities
\tOPTION 3: Find Matchups
\nEnter an option: '''

def open_file(s):
    '''
    Opens a file, if it exists. If file name is not found, prints the
        error message
    s: Value to be processed (str)
    Returns: fp (file pointer)
    '''
    while True:
         try:
             fp=open(input('Please enter a {} filename: '.format(s)), encoding="utf-8")
             return fp
         except FileNotFoundError:
             print('This {} file does not exist. Please try again.'.format(s))


def read_file(fp):
    """
    Reads data from the the file, organises data into a master dictionary
    fp: File pointer
    name_dict: A dictionary with pokemon names as keys and their values in a
        list as values (dict)
    against: List of all type values to find the one corresponding to pokemon
        effectiveness (list)
        
    Returns: Master dictionary (D)
    """
    reader = csv.reader(fp)
    D={}
    name_dict={}
    next(reader,None) #skipping header line
    against=['bug', 'dark', 'dragon', 'electric', 'fairy', 'fight',
                  'fire', 'flying', 'ghost', 'grass', 'ground', 'ice',
                  'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
    #loop to go through the lines in a file 
    for column in reader:

        gen=int(column[39])
        abilities1=column[0]
        abilities1=abilities1.strip('[]').replace("'","").split(',')
        abilities2=[]
        for word in abilities1:
            word=word.strip(' ')
            abilities2.append(word)
        #assigning pokemon values according to the given column number
        abilities2=set(abilities2)
        hp=int(column[28])
        capture_rate=int(column[23])
        base_weight=float(column[38])
        base_speed=int(column[35])
        #if statement to make legendary value true if value of the column is 1
        #or false if value of the column is 0
        if column[40]=='1':
            legendary=True
        elif column[40]=='0':
            legendary=False
        name = column[30]
        type1=column[36]
        type2=column[37]
        #if the second type value is empty, make a tuple with None value 
        if type2=='':
            types=(type1,None)
        else:
            types=(type1,type2)
        
        #effectiveness part
        effect_dict={}
        eff_values = column[1:19]
        #making new list for every matchup type
        sup_eff=[]
        eff=[]
        normal=[]
        weak=[]
        sup_weak=[]
        resistant=[]
        #assigning index value to go through the values of against list
        index=0
        for value in eff_values:
            if value=="0.25": #super effective value
                sup_eff.append(against[index])
            elif value=="0.5": #effective value
                eff.append(against[index])
            elif value=="1": #normal value
                normal.append(against[index])
            elif value=="2": #weak value
                weak.append(against[index])
            elif value=="4": #super weak value
                sup_weak.append(against[index])
            elif value=="0": #resistant value
                resistant.append(against[index])
            #adding +1 to index so that it iterates through every element of against list
            index+=1 
        #transforming all effectiveness lists into sets 
        sup_eff=set(sup_eff)
        eff=set(eff)
        normal=set(normal)
        weak=set(weak)
        sup_weak=set(sup_weak)
        resistant=set(resistant)
        #creating a dictionary with matchup types as keys and effectiveness 
        #sets as values
        dict3={"super effective":sup_eff, "effective":eff, "normal":normal,
               "weak":weak, "super weak":sup_weak, "resistant":resistant}
        #the list of all values of a pokemon
        L=[dict3, abilities2,hp,capture_rate,base_weight,
           base_speed,legendary]
        #updating dictionary with pokemon name and its list of values
        name_dict[name]=L

        #building a nested dictionary generation->types->name of pokemon->
        # ->list of pokemon values
        if gen not in D: #if generation key is not in a dictionary yet
            D[gen]={} #creating an empty dict
            
            if types not in D[gen]: #if type key is not in a dictionary yet
                D[gen][types]={} #creating an empty dict
                D[gen][types][name]=L
            else:
                D[gen][types][name]=L
                
        else:
            #if type key is not in a dictionary yet
            if types not in D[gen]:
                D[gen][types]={} #creating an empty dict
                D[gen][types][name]=L
            else:
                D[gen][types][name]=L
                
    return D


def find_pokemon(pokedex, names):
    """
    Takes in the master dictionary and a set of names of the pokemon It
    searches the dict for those pokemon and returns a corresponding dictionary
    of information for each of those pokemon, with each key being a pokemon’s
    name and each value being their list of corresponding information
    associated with said pokemon
    pokedex: Master dictionary that is being processed (dict)
    names: Pokemon names to search for(set)
    Returns: dictionary (dict)
    """

    dictionary={}
    #goes through names in a set
    for name in names:
        #iterating over nested dict pokedex starting with generation keys
        for gen in pokedex:
            #iterating over type keys
            for types in pokedex[gen]:
                #iterating over pokemon name keys
                for pok_name in pokedex[gen][types]:
                    #if name from the given set is in the pokedex name keys
                    if name in pokedex[gen][types]:
                        #building a list of pokemon values
                        stats=pokedex[gen][types][name]
                        stats=stats[1:]+[gen,types]

                        dictionary[name]=stats
                        
    return dictionary
    
def display_pokemon(name, info):
    """
    Takes in a pokemon name and a list of information about said pokemon
    and displays a pokedex entry for a single pokemon by building up a string
    gen: Generation value (int)
    name: Pokemon name (str)
    info: List of pokemon values to be processed (list)
    ab: List of abilities
    abilities: String of pokemon abilities (str)
    
    Returns: str
    """
    
    gen=info[-2]
    #gets rid of Nonetype element
    if info[-1][1]==None:
        types=info[-1][0]
    else:
        types=", ".join(info[-1])

    ab=list(info[0])
    #sorts abilities list
    ab=sorted(ab)
    #makes a string out of abilities list 
    abilities=", ".join(ab)
    
    hp=info[1]
    capture_rate=info[2]
    weight=info[3]
    speed=info[4]
    #if statement to decide whether the pokemon is legendary or not legendary
    if info[5]==True:
        is_legen="Legendary"
    else:
        is_legen="Not Legendary"
    
    return ("\n{}\n\tGen: {}\n\tTypes: {}\n\tAbilities: {}\n\tHP: {}"
        "\n\tCapture Rate: {}\n\tWeight: {}\n\tSpeed: {}\n\t{}".format(name,
   gen,types,abilities,hp,capture_rate,weight,speed,is_legen))

def find_pokemon_from_abilities(pokedex, abilities):
    """
    Takes in a set of abilities and finds all pokemon who have all those
    abilities specified in the parameter. It then returns a set of those
    pokemon’s names who had all of those abilities.
    pokedex: The master dictionary to be processed(dict)
    abilities: Abilities to find matches with (set)
    Returns: The names of the pokemon who have all the abilities
    in the parameter (set)
    """
    #new list that is used to collect pokemon names
    matches_list=[]
    
    for gen in pokedex:
        for types in pokedex[gen]:
            for name in pokedex[gen][types]:
                value=pokedex[gen][types].get(name)
                ab_set = value[1]
                
                if ab_set.issuperset(abilities):
                    matches_list.append(name)
    matches_set=set(matches_list)
    return matches_set
                   
def find_matchups(pokedex, name, matchup_type):
    """
    This function takes in a pokedex dictionary, a pokemon name and a type
    effectiveness (super effective, effective, normal, etc.),finds the
    corresponding set of types that affect that pokemon based on the type
    effectiveness. It then finds all other pokemon who have who have at least
    one of their 2 types that is in that set.Returns a list of tuples, with
    each tuple containing 2 elements. The first element is the name of a
    pokemon who has at least one of their types in the type effectiveness’
    set found above. The 2d element is the tuple of the types of said pokemon.
    pokedex: Master dictionary of pokemon data (dict)
    name: Pokemon name to be processed (str)
    matchup_type: Pokemon type to look matchups for (str)
    true_false: Value used to manipulate the loops (bool)
    
    Return: list_of tup (list)
    """
    
    
    
    list_of_tup=[]
    true_false=False
    #iterating through the master dictionary 
    for gen in pokedex:
        for types in pokedex[gen]:
            if name in pokedex[gen][types]:
                #extracting a set out of a list inside a nested dictionary
                pok_set_dict=pokedex[gen][types][name][0]
                #try-except so the program doesn't crash if key is not valid 
                try:
                    matchup_values=pok_set_dict[matchup_type]
                    #setting true_false to true to use it in if-statement
                    true_false=True 
                except KeyError:
                    pass
    #iterating through the master dictionary
    if true_false:
        for gen in pokedex:
            for types in pokedex[gen]:
                for pok_type in matchup_values:
                    if pok_type in types:
                        for pok in pokedex[gen][types]:
                            #if a list is empty meaning nothing was added yet
                            if list_of_tup==[]:
                                #iterating through the tuple to check if there
                                #is a nonetype value to get rid of it
                                for item in types:
                                    if item==None:
                                        #tuple with just one type value
                                        types = (types[0],)
                                #tuple with name and types tuple
                                pok_tuple=(pok,types)
                                #adding tuple to the list
                                list_of_tup.append(pok_tuple)
                            
                            else:
                                temp_true_false=True
                                #iterates through the list of tuples
                                for item in list_of_tup:
                                    #checks if the pokemon already in the list
                                    if pok== item[0]:
                                        temp_true_false=False
                                #gets rid of nonetype element
                                for the_type in types:
                                    if the_type==None:
                                        #tuple with only one type value
                                        types=(types[0],)
                                #if the value is not in the list, appends it 
                                #to the list of tuples
                                if temp_true_false:
                                    pok_tup=(pok,types)
                                    list_of_tup.append(pok_tup)
    if true_false:
        #sorts the list
        list_of_tup=sorted(list_of_tup)
        return list_of_tup
    #return none if invalid type
    else:
        return None

def main():
    print("Welcome to your personal Pokedex!\n")
    fp = open_file("pokemon")  #opening the file
    pokedex = read_file(fp) #building a dict with the data from the file
    option=''
    while option.lower()!='q': #loop that quits only if ooptin is Q or q
        
        option =input(PROMPT)
        if option =='1' or option == '2' or option == '3':
            if option =='1':
                names_string = input (("\nEnter a list of pokemon names,"
                                       " separated by commas: "))
                #edits the string,strips it of commas and spaces, splits into 
                #the list
                names_list=names_string.strip(",").replace(" ", "").split(",")
                #transforming list into set
                names_set=set(names_list)
                #dictionary that is returned from a function
                pok_dict=find_pokemon(pokedex, names_set)
                print_list=[]
                #loop to go through the dictionary
                for name in pok_dict:
                    #returns string from a function
                    pok_string=display_pokemon(name, pok_dict[name])
                    #appends string to the list to print it later
                    print_list.append (pok_string)
                
                print_list=sorted(print_list)#sorts the list
                for item in print_list:
                    print (item)
                
            elif option =='2':
                ab=input('Enter a list of abilities, separated by commas: ')
                #edits the string,strips it of commas and spaces, splits into 
                #the list
                ab_list = ab.strip(",").strip(" ").split(",")
                
                ab_strip=[]
                #strips strings of whitespaces and adds to the list
                for word in ab_list:
                    word=word.strip(' ')
                    ab_strip.append(word)
    
                abilities=set(ab_strip)
                #calling a function to get a set
                pok_set=find_pokemon_from_abilities(pokedex, abilities)
                #turns set into the list 
                pok_list=list(pok_set)
                #sorts the list
                pok_list=sorted(pok_list)
                #.join method to turn a list into a string for printing
                print("Pokemon:",", ".join(pok_list))

            elif option =='3':
                
                pok_name=input('Enter a pokemon name: ')
                matchup_type=input("Enter a matchup type: ")
                #getting a list from a function
                matchup_list=find_matchups(pokedex, pok_name, matchup_type)
                #if the return is empty, than the input was invalid, so it
                #prints the error message
                if not matchup_list:
                    print ("Invalid input")
                else:
                    for tup in matchup_list:
                        #.join method to turn list into a string for printing
                        print ("{}:".format(tup[0]), ", ".join(tup[1]))
        #if option is not 1-3 or 'Q' or 'q', prints error message
        elif option.lower()!='q':
            print ('Invalid option {}'.format(option))

if __name__ == "__main__":
    main()