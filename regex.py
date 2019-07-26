import re
def matchvow(w):
    
    match =re.compile(r'^ha')
    mtch =re.compile(r'\w+\s\d+')
    mch =re.compile(r'es$')
    res = match.findall(msg)
    outp = mch.findall(msg)
    resul = mtch.findall(msg)
    print(res,resul,outp)
msg = input("Enter word: ")
matchvow(msg)
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
