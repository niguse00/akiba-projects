word = input("Enter the word: ")

def count_word(word):
    return len(word.split())

def count_characters(word):
    return len(word.strip(".").replace(" ",""))

def count_vowels_and_consonants(word):
    vowels = ["a","e","i","o","u"]
    vowel = []
    for s in word:
       if s in vowels:
          vowel.append(s)
    num_of_vowel = len(vowel)
    num_of_consonants = count_characters(word) - num_of_vowel 
    return num_of_vowel, num_of_consonants
def find_longest_word(word):
    my_word = word.strip('.').split()
    longest = my_word[0]
    for s in my_word:
        if len(s) > len(longest):
            longest = s
    return longest

def count_each_word_appear(word):
    my_word = word.strip(".").split()
    return my_word
       

def repeated_word(word):
    repeated = []
    my_word = word.strip(".").split()
    for s in my_word:
        if my_word.count(s) > 1:
           repeated.append(s)
    dist_list = list(set(repeated))
    return dist_list
        

def text_analyzer(word):
    print(f"""
           {word}
     ================================================
      Words: {count_word(word)}
      Longest word: {find_longest_word(word)}
      
    """)
    my_word = count_each_word_appear(word)
    for s in my_word:
        print(s,my_word.count(s))
    repeated = repeated_word(word)
    for s in repeated: 
        print(f'    {s}', end=" ")
    


text_analyzer(word)