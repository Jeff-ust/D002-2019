def checker(sentence, letter):
    result = []
    for i in range(0, len(sentence)):
        if sentence[i] == letter:
            result.append(i)                   
    return result

    
a = print(checker("Apple", "p")) # a = [1, 2]   
b = print(checker("Banana", "p")) # b = []
c = print(checker("Cat", "a")) # c = [1]



