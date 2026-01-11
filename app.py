from scripts.functions import greet, load_data, show_data

if __name__ == "__main__":
    data_path = "data/db.csv"
    data = load_data(data_path)
    show_data(data)
