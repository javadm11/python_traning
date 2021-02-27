    
class Permutation:
    def __init__(self,text):
        self.result = []
        self.text = text
        self.permutation(self.text)

       
    def __call__(self):
        return self.result
    def permutation(self,text,step=0):
        if step==len(text):
            self.result.append(''.join(text))
        for i in range(step,len(text)):
            text_copy=[c for c in text]

            text_copy[step],text_copy[i]=text_copy[i],text_copy[step]

            self.permutation(text_copy,step+1)
            
        
        
    
p=Permutation('ali')


print(p())