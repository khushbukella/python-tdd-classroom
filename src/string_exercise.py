class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, string):
        string = string[::-1] 
        return string 
       

    def is_english_vowel(self, ch):
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        longest = max(sentence.split(), key=len)
        return longest

    def get_word_lengths(self, str):
        str = str.split (' ')
        result=[]
        for words in str:
            result.append(len(words))
        return result