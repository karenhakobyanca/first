def levenshtein_dist(word1,word2):

    sub = 0
    if len(word1) > len(word2):
        sub += len(word1) - len(word2)
    elif len(word1) < len(word2):
        sub += len(word2) - len(word1)

    ord1 = [ord(letter1) for letter1 in word1]
    ord2 = [ord(letter2) for letter2 in word2]
    match_ords = zip(ord1,ord2)
    lst_levenshtein = []
    count = 0

    for a,b in match_ords:
        if a != b :
            count = 1
            lst_levenshtein.append(count)
        if a == b :
            continue

    levenshtein_distance = sum(lst_levenshtein) + sub
    return levenshtein_distance

word1 = input()
word2 = input()
print(levenshtein_dist(word1,word2))



def soundex(word:str):
    first_letter = word[0].capitalize()
    letters = [char for char in word[1:]]

    zero_val = {('a','e','i','0','u','h','w','y'): 0 }
    letters_values = {('b', 'f', 'p', 'v'): 1
                     ,('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'): 2,
                  ('d', 't'): 3, ('l',): 4, ('m', 'n'): 5, ('r',): 6}
    soundex_str = "".join(first_letter)
    if len(word) == 1:
        soundex_str +="000"
    for char in range(len(letters) - 1):
        if letters[char] == letters[char + 1]:
            same_letter = letters[char]
            letters.remove(same_letter)
            break

    new_letters = letters


    for i in range(len(new_letters)):
        for j in letters_values.keys():
            if new_letters[i] in j:
                key = letters_values[j]
                soundex_str+=str(key)
            if len(soundex_str) == 4:
                        break

    if len(soundex_str) < 4:
        soundex_str += "0"



    return soundex_str



word = input()
print(soundex(word))