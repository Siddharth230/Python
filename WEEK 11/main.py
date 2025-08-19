# f = open("scores.csv", "r")
# scores = f.readlines()[1:]
# max = 0
# for record in scores:
#     fields = record.split(",")
#     if int(fields[8]) > max:
#         max = int(fields[8])
# print(max)

import pandas as pd

scores = pd.read_csv("scores.csv")
print(scores["Total"].max())
print(scores["Total"].min())
print(scores["Total"].mean())
print(scores["Total"].sum())
print(scores["Total"].sort_values())
print(scores["Total"].sort_values(ascending=False))
# print(scores)
# print(scores.shape)
# print(scores.count())
