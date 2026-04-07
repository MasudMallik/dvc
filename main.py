import pandas as pd
import os

data={
    "name":["a","b","c"],
    "age":[10,12,13],
}
df=pd.DataFrame(data)
df["height"]=[5,6,7]

os.makedirs("data",exist_ok=True)
path=os.path.join("data","sample.csv")
df.to_csv(path)