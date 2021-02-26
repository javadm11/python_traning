from string import ascii_letters

def encrypt(string , step):
    asci=ascii_letters
    result=''
    for i in string:
        if i not in asci:
            result+=i
        else:
            for j in asci:
                if j==i:
                    index=asci.index(j)
                    index=(index+step)%len(asci)
                    result+=asci[index]
    return result

def decrypt(string, step):
    asci=ascii_letters
    result=''
    for i in string:
        if i not in asci:
            result+=i
        else:
            for j in asci:
                if j==i:
                    index=asci.index(j)
                    index=(index-step)%len(asci)
                    result+=asci[index]
    return result


