import pandas as pd
import numpy as np

def main():
    FILE_PATH = "data.csv"
    df = pd.read_csv(FILE_PATH)
    data = df.values
    means = np.empty((48,4))
    for i in range(1,49):
        settlement_dates = data[:,4] == i
        price = data[settlement_dates, 7]
        power = data[settlement_dates, 5]
        grid = data[settlement_dates, 8]
        means[i-1,0] = i
        means[i-1,1] = np.nanmean(price)
        means[i-1,2] = np.nanmean(power)
        means[i-1,3] = np.nanmean(grid)
    indices = np.argsort(means[:, 1])
    sorted = means[indices]
    print(sorted)



if __name__ == "__main__":
    main()