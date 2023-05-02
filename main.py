import pandas as pd

data=pd.read_csv("./nato_phonetic_alphabet.csv")

data_frame=pd.DataFrame(data)

NATO_phonetic_dict={row.letter:row.code for (index,row) in data_frame.iterrows()}

def generate_phonetic():
    word=input("Enter a word: ")
    try:
        NATO_phonetic_list=[NATO_phonetic_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry Only Letters in Alphabets please....")
        generate_phonetic()
    else:    
        print(NATO_phonetic_list)

generate_phonetic()