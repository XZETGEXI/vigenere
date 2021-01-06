import itertools as it

ALPHAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_d():
    """ generates the dicts between alpha and number """
    d_letter_n = {}
    d_n_letter = {}
    
    for n, letter in enumerate(ALPHAS):
        d_letter_n[letter] = n
        d_n_letter[n] = letter
    
    return d_letter_n, d_n_letter



def sanitize_str(string):
    """ Sanitize string to uppercase alpha only """
    
    return filter(str.isalpha, string.upper())



def encode(message, mask):
    """ Vigenere enconding """
    result = ""
    
    # Get valid strings
    message = sanitize_str(message)
    mask = sanitize_str(mask)
    
    d_letter_n, d_n_letter = generate_d()
    mask_cycle = it.cycle(mask)
    
    for letter in message:
        new_n = d_letter_n[letter] + d_letter_n[next(mask_cycle)]
        result += d_n_letter[new_n % 26]
    
    return result
    
    
    
def decode(message, mask):
    """ Vigenere decoding """
    result = ""
    
    # Get valid strings
    message = sanitize_str(message)
    mask = sanitize_str(mask)
    
    d_letter_n, d_n_letter = generate_d()
    mask_cycle = it.cycle(mask)
    for letter in message:
        new_n = d_letter_n[letter] - d_letter_n[next(mask_cycle)]
        result += d_n_letter[new_n % 26]
    
    return result
