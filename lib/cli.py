# lib/cli.py

from helpers import (
    exit_program,
    list_pokemon_all,
    add_starter,
    greeting,
    list_all_in_team,
    list_current_party,
    list_all_in_team,
    change_nickname,
    remove_pokemon_from_party,
    add_pokemon_to_party,
    catch_pokemon,
    release_team,
    create_new_pokemon
)
from models.team import Team


money = 1000
pokeballs = 5

def main():
    global money, pokeballs
    Team.drop_table()
    Team.create_table()
    starter_is_chosen = False
    print("Welcome to the Pokemon World!")
    while True:
        #start with asking user to pick one starter pokemon
        #starter will be added to the team and party automatically
        #print 3 options of pokemon, Bulbasaur, Charmander, Squirtle

        #afterwards, show menu of new options
        #user has a certain amount of pokeballs (5)
        #user can choose to catch new pokemon
        #   user will get a random battle encounter
        #   can run away from battle
        #   chance of success will be random
        #   new pokemon will be random
        #user can choose to release existing pokemon
        #   cannot release first pokemon
        #   cannot release all pokemon
        #user can change around pokemon in party
        #user can ask to view current party
        
        #user has a certain amount of money
        #can get more money by releasing pokemon, higher level pokemon are worth more
        #can spend money on pokeballs for better chances
        #if they choose to catch new pokemon, show a list of available pokemon
        #if they choose to release existing pokemon, show a list of their current team


        if not starter_is_chosen:
            greeting()
            starter_is_chosen = add_starter()
            
        else:
            menu()
            choice = input("> ")
        
            if choice == "0":
                exit_program()
            elif choice == "1":
                print("")
                print("Current Team:")
                list_all_in_team()
                print("0. Back")
                print("1. Change nickname of pokemon")    
                print("2. Remove pokemon from current party")
                print("3. Add pokemon to current party")
                print("4. Release a Pokemon for money")
                while True:
                    choice2 = input("> ")
                    if choice2 == "0":
                        break
                    if choice2 == "1":
                        change_nickname()
                        break
                    elif choice2 == "2":
                        remove_pokemon_from_party()
                        break
                    elif choice2 == "3":
                        add_pokemon_to_party()
                        break
                    elif choice2 == "4":
                        released_money = release_team()
                        money += released_money
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "2":
                if pokeballs >  0:
                    pokeball_used = catch_pokemon()
                    if pokeball_used:
                        pokeballs += -1
                else:
                    print("You don't have enough pokeballs.")
            elif choice == "3":
                print("")
                print("All Pokemon in the Pokedex:")
                list_pokemon_all()
            elif choice == "4":
                buy_pokeballs()
            elif choice == "5":
                create_new_pokemon()


        
def menu():
    global money, pokeballs
    print("")
    print(f"You currently have ${money}.")
    print(f"You have {pokeballs} pokeballs.")
    list_current_party()
    print("0. Exit")
    print("1. View full team configuration")
    print("2. Catch a new Pokemon")
    print("3. View the Pokedex")
    print("4. Buy more pokeballs")
    print("5. Create a new pokemon")


def buy_pokeballs():
    global money, pokeballs
    price = 10
    print("Pokeballs cost $5. How many would you like to buy?")
    while True:
        amount = input("> ")
        if amount.isnumeric():
            amount = int(amount)
            if money >= amount * price:
                money -= amount * price
                print(f"You bought {amount} pokeballs for ${price * amount}.")
                pokeballs += amount
                return
            else:
                print("You don't have enough money.")
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
