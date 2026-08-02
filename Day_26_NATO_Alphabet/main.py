import pandas as pd

with open("text1.csv") as data_file:
    data = pd.read_csv(data_file)
    name = input("What's your name?").upper()
    name_list = [letter for letter in name]
    filtered_df = {letter: data[(data['letter'] == letter)].code.iloc[0] for letter in name_list }
    print(filtered_df)
