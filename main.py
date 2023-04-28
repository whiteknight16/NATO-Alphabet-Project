import pandas as pd

data=pd.read_csv("./nato_phonetic_alphabet.csv")

data_frame=pd.DataFrame(data)

NATO_phonetic_dict={row.letter:row.code for (index,row) in data_frame.iterrows()}


word=input("Enter a word: ")
NATO_phonetic_list=[NATO_phonetic_dict[letter.upper()] for letter in word]
print(NATO_phonetic_list)