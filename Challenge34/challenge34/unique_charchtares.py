from hashtable import HashTable
def areCharactersUnique(string):
    if type(string) != str:
        raise Exception("Argument must be a string")
    char = ''
    hashmap = HashTable()
    for char in string:
        if ord(char) in range(ord('a'), ord('z') + 1):
            if hashmap.contains(char):
                return False
            else:
                if not hashmap.contains(char):
                    hashmap.set(char, None)
                    char = ''
    return True
   
if __name__=="__main__":
    # h=HashTable()
    # [h.set(c) for c in "The quick brown fox jumps over the lazy dog"]
    print(areCharactersUnique("The quick brown fox jumps over the lazy dog"))
    print(areCharactersUnique("I love cats"))
    print(areCharactersUnique("Donald the duck"))
