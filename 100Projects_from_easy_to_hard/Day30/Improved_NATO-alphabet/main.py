import pandas

data_dic = {value.letter: value.code for _, value in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
while True:
    try:
        phonetic_code = [data_dic[i] for i in input("Enter a word : ").upper()]
    except KeyError:
        print("Sorry only letter in alphabate please.")
    else:
        print(phonetic_code)
        break
