import time
import random
import profiles.models as pro_models

from string import ascii_letters, punctuation

six_hrs_in_milli_time = 21600

def current_milli_time():
    return int(round(time.time() * 1000))

def random_string_generator():
    generated_string = ''
    allowed_chars = ascii_letters + punctuation + '0123456789';
    size_of_str = random.randrange(5, 31)

    for i in range(0, size_of_str):
        generated_string += random.choice(allowed_chars)
    return(generated_string)

def token_generator():
    for i in range(0, 100000):
        generated_string = random_string_generator();
        if(not(pro_models.Profile.objects.filter(token = generated_string))):
            return(generated_string)
    return('42');

def TokenAuthenticate(request):
    profile_id = request.headers['Id']
    profile_token = request.headers['Authorization']
    profile = pro_models.Profile.objects.filter(id = profile_id, token = profile_token)
    if(profile):
        profile = profile[0]
        temp = int(profile.time_token_created) + six_hrs_in_milli_time
        if(temp > current_milli_time()):
            return(True, profile)
    return(False, None)
