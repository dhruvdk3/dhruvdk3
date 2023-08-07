import pandas

data_dic = {value.letter: value.code for _, value in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
phonetic_code = [data_dic[i] for i in input("Enter a word : ").upper()]
print(phonetic_code)
