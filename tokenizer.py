from tokenized.dict_models import LongMatchingTokenizer

def getText(txtFileName):
    file = open(txtFileName, 'r', encoding="utf-8")
    return file.read()

newCorpusDir = 'output/'
covid = getText("covid.txt")

lm_tokenizer = LongMatchingTokenizer()
tokens = lm_tokenizer.tokenize("Thuế thu nhập cá nhân")
tokens = lm_tokenizer.tokenize(covid)

print(tokens)