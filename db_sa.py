from random import choice
alpha_bets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encodingDB(mes):
    mes = mes.lower()
    if(len(mes)<=2):
        return mes[::-1]
    elif(len(mes)>=3):
        new_str = ""
        new_str += choice(alpha_bets)
        new_str += choice(alpha_bets)
        new_str += choice(alpha_bets)
        temps = mes[0]
        new_str += mes[1:]
        new_str += temps
        new_str += choice(alpha_bets)
        new_str += choice(alpha_bets)
        new_str += choice(alpha_bets)
        return new_str
# print(encodingDB("Dragon"))

