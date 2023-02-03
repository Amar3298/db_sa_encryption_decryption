from random import choice
alpha_bets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryptionDB(mes):
    mes = mes.lower()
    if(len(mes)<3):
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

def decryptionDB(mes):
    if(len(mes)<3):
        res =  mes[::-1]
        res = res.capitalize()
        return res
    elif(len(mes)>=3):
        new_str = ""
        new_str += mes[3:-3]
        res = ""
        res += new_str[-1]
        res += new_str[:-1]
        res = res.capitalize()
        return res
# check = encryptionDB("Dragon")
# print(check)
# print(decryptionDB(check))
def encryptString(mesS):
    list1 = mesS.split(" ")
    res_list = list(map(lambda x:encryptionDB(x),list1))
    join_db = " "
    res = join_db.join(res_list)
    # print(res_list)
    return res
# check = encryptString("Dragon Ball")
def decryptString(mesS):
    list1 = mesS.split(" ")
    res_list = list(map(lambda x:decryptionDB(x),list1))
    join_db = " "
    res = join_db.join(res_list)
    return res

# Manual Testing
# check = encryptString("Dragon Ball")
# print(check)
# print(decryptString("tacragondehh qacallbpue si ym yleavfosu"))

if __name__ == __name__:
    while(True):
        user_choice =int(input("Enter operation to perform\n\t1.Encryption\n\t2.Decryption\n\t3.Exit\n"))
        if(user_choice==1):
            user_msg = input("Enter the text here:- ")
            encrypted_msg = encryptString(user_msg)
            print(f"Encrypted Message:- {encrypted_msg}")
        elif(user_choice==2):
            user_encrypted_msg = input("Enter Encrypted message here:- ")
            decrypted_msg = decryptString(user_encrypted_msg)
            print(f"Encrypted Message:- {decrypted_msg}")
        elif(user_choice==3):
            print("Thanks for using our encryption decryption!!!")
            break