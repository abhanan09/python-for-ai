
import pandas as pd

data = {
    "product": ["laptop" , "mouse", "keyboard"],
    "price": [500, 20, 45],
    "quantity": [2,5,3]
}

df = pd.DataFrame(data)
print(df)

print(df["price"])

df["total"] = df["price"] * df["quantity"]
print(df)

highest = df["total"].max()
print(highest)

highest_row = df[df["total"] == highest]
print(highest_row)

lowest = df["total"].min()
print(lowest)

lowest_row = df[df["total"] == lowest]
print(lowest_row)