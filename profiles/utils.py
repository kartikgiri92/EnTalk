import time
import random

from string import ascii_letters, punctuation

def random_string_generator():
    generated_string = ''
    allowed_chars = ascii_letters + punctuation + '0123456789'

    for i in range(0, 30):
        generated_string += random.choice(allowed_chars)
    return(generated_string)

def current_milli_time():
    return int(round(time.time() * 1000))
