
if __name__ == '__main__':
    
    p = pokemon_database()
    pok = p.load_pokemon()


    r = requests.get(p.URL)
    vals = r.text.splitlines()
    vals = vals[0].split(',')[1:-2]

    #print(pok)
    command = 'empty'
    stat = ''
    mon = ''
    print("Welcome to the pokedex!")
    while command and command != 'exit':
        command = input("Please enter a function, choices are: 'breed', 'highest', 'pokemon', 'stat', and 'post'. Enter 'exit' to quit: ")
        command = command.lower()
        if command == 'exit':
            print("Thank you for using DEX, have a good day!")
            break
        elif command == 'breed':
            isInt = True
            mon = input("What pokemon would you like to breed: ")
            try:
                mon = int(mon)
            except:
                isInt = False

            if isInt:
                if mon not in pok[0].keys():
                    print("Sorry, I couldn't find that pokemon")
                    continue
                num = mon
                mon = pok[0][num][0][1]
            else:
                if mon not in pok[1].keys():
                    print("Sorry, I couldn't find that pokemon")
                    continue
                mon = mon.lower()
                num = int(pok[1][mon][0][0][1:])
                mon = pok[0][num][0][1]

            mates = p.find_breedable(num, pok[0])
            sys.stdout.write("{} can breed with: ".format(mon))
            print(', '.join(mates))
        elif command == 'highest':
            stat = input("What stat would you like to find the highest holder of? (Enter 'all' or 'total' for total base stats): ")
            if stat == 'all' or stat == 'total':
                guys = p.get_highest("", pok[0])
