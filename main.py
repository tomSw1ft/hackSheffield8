import pandas as pd
import numpy as np

def main():
    FILE_PATH = "data.csv"
    df = pd.read_csv(FILE_PATH)
    data = df.values
    temp = data[:, 8]
    print(np.nanmean(temp))


if __name__ == "__main__":
    main()