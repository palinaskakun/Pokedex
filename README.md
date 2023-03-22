# Pokedex

Pokemon is cult classic video game introduced in the 1990s. In these games, there are different creatures, called pokemon, that a player can catch, collect, train, and battle with. Each of these pokemon have different names, weights, heights, attack/defenses, abilities, etc. Because of this complexity, there is a lot of information surrounding each pokemon, and all that data needs to be kept track of somewhere. The in-game solution to store this data is the pokedex.

In this program, the program is given a csv file filled with all the information you could ever dream of for every pokemon. Using that data, the program creates a pokedex for the user to interact with. On startup, the user is provided an interactive menu in which they can enter various options to gather information, presented to them in a clean, human-readable format.

Example use:
Input:
```
pokemon.csv
3
Ledyba
super weak
1
Squirtle
2
Swift Swim, Storm Drain
Q
```
Output:
```
Welcome to your personal Pokedex!

Please enter a pokemon filename: pokemon.csv

To make a selection, please enter an option 1-3:
    OPTION 1: Find Pokemon
    OPTION 2: Find Pokemon From Abilities
    OPTION 3: Find Matchups

Enter an option: 3
Enter a pokemon name: Ledyba
Enter a matchup type: super weak
Aerodactyl: rock, flying
Aggron: steel, rock
Amaura: rock, ice
Anorith: rock, bug
Archen: rock, flying
Archeops: rock, flying
Armaldo: rock, bug
Aron: steel, rock
Aurorus: rock, ice
Barbaracle: rock, water
Bastiodon: rock, steel
Binacle: rock, water
Boldore: rock
Bonsly: rock
Carbink: rock, fairy
Carracosta: water, rock
Corsola: water, rock
Cradily: rock, grass
Cranidos: rock
Crustle: bug, rock
Diancie: rock, fairy
Dwebble: bug, rock
Geodude: rock, ground
Gigalith: rock
Golem: rock, ground
Graveler: rock, ground
Kabuto: rock, water
Kabutops: rock, water
Lairon: steel, rock
Larvitar: rock, ground
Lileep: rock, grass
Lunatone: rock, psychic
Lycanroc: rock
Magcargo: fire, rock
Minior: rock, flying
Nihilego: rock, poison
Nosepass: rock
Omanyte: rock, water
Omastar: rock, water
Onix: rock, ground
Probopass: rock, steel
Pupitar: rock, ground
Rampardos: rock
Regirock: rock
Relicanth: water, rock
Rhydon: ground, rock
Rhyhorn: ground, rock
Rhyperior: ground, rock
Rockruff: rock
Roggenrola: rock
Shieldon: rock, steel
Shuckle: bug, rock
Solrock: rock, psychic
Sudowoodo: rock
Terrakion: rock, fighting
Tirtouga: water, rock
Tyranitar: rock, dark
Tyrantrum: rock, dragon
Tyrunt: rock, dragon

To make a selection, please enter an option 1-3:
    OPTION 1: Find Pokemon
    OPTION 2: Find Pokemon From Abilities
    OPTION 3: Find Matchups

Enter an option: 1

Enter a list of pokemon names, separated by commas: Squirtle

Squirtle
    Gen: 1
    Types: water
    Abilities: Rain Dish, Torrent
    HP: 44
    Capture Rate: 45
    Weight: 9.0
    Speed: 43
    Not Legendary

To make a selection, please enter an option 1-3:
    OPTION 1: Find Pokemon
    OPTION 2: Find Pokemon From Abilities
    OPTION 3: Find Matchups

Enter an option: 2
Enter a list of abilities, separated by commas: Swift Swim, Storm Drain
Pokemon: Finneon, Lumineon
```
