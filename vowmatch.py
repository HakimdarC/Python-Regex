import re
def matchvow(w):
    
    match =re.compile(r'[aeiouAEIOU]')
    mtch =re.compile(r'\w+\s\d+')
    mch =re.compile(r'[^aeiouAEIOU]')
    vowel = match.findall(msg)
    consonant = mch.findall(msg)
    other = mtch.findall(msg)
    search = match.search(msg)
    result = search.group()
    print(vowel,consonant,other,result)
msg = input("Enter word: ")
matchvow(msg)


