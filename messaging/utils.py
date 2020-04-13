import time
import random
import profiles.models as pro_models
import messaging.models as mssg_models

def encrypt_message(friend_profile, mssg):
    enc_mssg = ''
    ascii_num_list = [ord(i) for i in mssg]
    public_key, public_key_2 = int(friend_profile.public_key), int(friend_profile.public_key_2)

    for i in ascii_num_list:
        num = str((i ** public_key_2) % public_key)
        enc_mssg += str(len(num)) + num

    return(enc_mssg)

def decrypt_message(friend_profile, mssg):
    i, dcy_mssg = 0, ''
    private_key, public_key = int(friend_profile.private_key), int(friend_profile.public_key)

    while(i < len(mssg)):        
        num = int(mssg[i + 1 : i + 1 + int(mssg[i])])
        dcy_mssg += chr((num ** private_key) % public_key)
        i = i + 1 + int(mssg[i])

    return(dcy_mssg)
