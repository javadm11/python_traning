import random

class OneTime:
    def encrypt(self,text):
        plain=[ord(i) for i in text]
        key=[]
        cipher=[]
        for i in plain:
            k=random.randint(1,300)
            c=(i+k)*k
            key.append(k)
            cipher.append(c)

        return key,cipher

    def decrypt(self,chiper,key):
        text=[]
        for (k,c) in zip(key,chiper):
            f=(c/k)-k
            text.append(chr(f))
        
        return ''.join(text)
