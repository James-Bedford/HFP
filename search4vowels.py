def search4vowels(word:str) -> set:
    '''Return any vowels'''
    vowels = set('aeiou')
    vowels2 = {'a','e','i','o'}
    #vowels2 = set('a','e')
    found = vowels2.intersection(word)
    return bool(found)
    #for i in found:
        #print(i)

a = search4vowels('Tesco')
print(a)

