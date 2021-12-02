import logging
import pandas as pd

def run_part_one(input):
    data = pd.read_csv(input, header=None, names=["data"])

    return sum(data["data"] > data["data"].shift(1))


def run_part_two(input):
    data = pd.read_csv(input, header=None, names=["data"])

    rolling_data = data.rolling(3).sum()

    return sum(rolling_data["data"] > rolling_data["data"].shift(1))

def main():

    result = run_part_one("./input.txt")
    logging.info("The result of part one is: %s", result)

    result = run_part_two("./input.txt")
    logging.info("The result of part two is: %s", result)

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO
    )
    main()