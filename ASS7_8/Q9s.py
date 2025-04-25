import re
class Tokenizer:
    
    def __init__(self,text):
        self.text = text

    def tokenize(self):

        return


text = str(input("Enter the:\n"))
#We will make a pattern for finding a what we have given in question

pattern = r""

final_res = re.findall(pattern,text)
print(final_res)