#install PyDictionary
from PyDictionary import PyDictionary
dictionary=PyDictionary()


while True:
    dictionary.translate('hear','french')

    word=input('Enter word:')
    if word=='':
        print('You did not enter any word')
    print(dictionary.getMeanings(word))
#multiple words
'''dictionary=PyDictionary('hear','wisdom','oop')
print(dictionary.printMeaning())
print(dictionary.getMeaning())'''