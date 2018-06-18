import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

data = pd.read_csv("data/wpd_datasets.csv")
cols = [x for x in data.columns.tolist() if x.startswith("M")]

series = {}
for i in range(len(cols)):
    d = data.iloc[1:, [i * 2, i * 2 +1]].dropna().astype(np.float32)
    d.columns = ["x", cols[i]]
    d = d.set_index("x").squeeze()

    plt.scatter(d.index, d)

    xs = np.arange(round(d.index.min(), -1), round(d.index.max(), -1), 5)

    ys = spline(xnew=xs, xk=d.index, yk=d, order=3)

    interp = pd.Series(index=xs, data=ys).replace(0, np.nan).dropna()

    plt.scatter(interp.index, interp)

    print(interp)



    break

plt.show()
