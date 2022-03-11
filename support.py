import re
import random
import os
from time import sleep



rand_numbs = []
names = []
site_imgfiles = ["dna.png","download.svg","icon.png","logo.ico"]


def rand_number():
    while True:
        x = int(random.randrange(0, 1000))
        if x not in rand_numbs:
            rand_numbs.append(x)
            return x 


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def duplicate_name_check(name):
    global final_name
    final_name = ''
    if str(name) in names:
        new_name = str(name) + str(rand_number())
        names.append(new_name)
        final_name = new_name
        return new_name
    else:
        names.append(name)
        final_name = name
        return name 

def deletion():
    try:
        rand_numbs.pop()
        names.pop()

    except:
        files = os.listdir(".\static\images")
        
        for filename in files:
            if filename not in site_imgfiles:
                os.remove(".\static\images\\"+str(filename))

    else:
        return "path clear"

