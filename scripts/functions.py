import pandas as pd

def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def load_data(file_path):
    db = pd.read_csv(file_path)
    return db

def show_data(dataframe):
    print(dataframe)