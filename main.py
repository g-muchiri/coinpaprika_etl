from extract import extract_coin_data
from transform import transform_coin_data
from load import load_coin_data

def main():
    new_data = extract_coin_data()
    trans_data = transform_coin_data(new_data)
    load_coin_data(trans_data)

    print("Modularized ETL Process very much complete")

if __name__ == "__main__":
    main()