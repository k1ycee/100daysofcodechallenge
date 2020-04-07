def coffee_bot():
    print("Welcome to cafe!")
    user = input("Would you be so kind as to tell me your name: ")
    print("Thanks "+user+" "+"your "+size()+" "+get_brew_type()+" will be ready shortly!")

def size():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>")
    if res == 'a' or res == 'A':
         return 'small'
    elif res == 'b' or res == 'B':
        return 'medium'
    elif res == 'c' or res == 'C':
        return 'Large'
    else:
        print("What you just selected is not in the options :(, Use a valid input")
        return size()
    return res

def get_brew_type():
    res = input("What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n>")
    if res == 'a' or res == 'A':
         return 'Brewed Coffee'
    elif res == 'b' or res == 'B':
        return 'Mocha'
    elif res == 'c' or res == 'C':
        return order_latte()
    else:
        print("What you just selected is not in the options :(, Use a valid input")
        return get_brew_type()
    return res
def order_latte():
    res = input("And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n>")
    if res == 'a' or res == 'A':
        return '2% milk'
    elif res == 'b' or res == 'B':
        return 'Non-fat milk'
    elif res == 'c' or res == 'C':
        return 'Soy milk'
    else:
        print("What you just selected is not in the options :(, Use a valid input")
        return order_latte()
    return res
    

coffee_bot()