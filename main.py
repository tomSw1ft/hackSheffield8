import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    FILE_PATH = "data.csv"
    df = pd.read_csv(FILE_PATH)
    data = df.values
    means = np.empty((48,3))
    for i in range(1,49):
        settlement_dates = data[:,4] == i
        price = data[settlement_dates, 7]
        grid = data[settlement_dates, 8]
        means[i-1,0] = i
        means[i-1,1] = np.nanmean(price)
        means[i-1,2] = np.nanmean(grid)

    indices = np.argsort(means[:,1])
    sorted = means[indices]
    minPrice = sorted[0, 1]
    maxPrice = sorted[47, 1]
    indices = np.argsort(means[:,2])
    sorted = means[indices]
    minGrid = sorted[0, 2]
    maxGrid = sorted[47, 2]
    rangePrice = maxPrice - minPrice
    rangeGrid = maxGrid - minGrid
    adjustedMeans = np.empty((48,3))
    for i in range(1,49):
        adjustedMeans[i-1,0] = i

        adjustedMeans[i-1,1] = (means[i-1,1]-minPrice) / rangePrice
        adjustedMeans[i-1,2] = (means[i-1,2]-minGrid) / rangeGrid

    dates = adjustedMeans[:, 0]
    prices = adjustedMeans[:, 1]
    grids = adjustedMeans[:, 2]
    print(adjustedMeans)

    plt.plot(dates, prices, marker='o', label='prices')
    plt.plot(dates, grids, marker='s', label='grids')
    plt.xlabel('settlement dates')
    plt.ylabel('prices, grids')
    plt.legend()
    plt.grid(True)
    plt.show()
    



if __name__ == "__main__":
    main()