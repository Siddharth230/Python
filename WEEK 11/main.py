import pandas as pd

scores = pd.read_csv("scores.csv")
print(scores, type(scores))
print(scores["Name"], type(scores["Name"]))
print(scores.head())
print(scores.tail())
print(scores[scores["Name"] == "Siddharth"])
print(scores[scores["Gender"] == "M"]["Total"].max())
print(scores[scores["Gender"] == "F"]["Total"].max())
subject = ["Mathematics", "Physics", "Chemistry"]
for sub in subject:
    print(f"Above 85 in {sub}")
    print(scores[(scores["Gender"] == "F") & (scores[sub] > 85)].shape[0])
    print(scores[(scores["Gender"] == "M") & (scores[sub] > 85)].shape[0])
print(scores[scores["Physics"].between(70, 85)].shape[0])
print(scores[scores["Physics"].between(60, 70)].shape[0])
print(scores[scores["Physics"] < 60].shape[0])
for sub in subject:
    print(f"Above average {sub}")
    avg = scores[sub].mean()
    print(scores[(scores["Gender"] == "F") & (scores[sub] > avg)].shape[0])
    print(scores[(scores["Gender"] == "M") & (scores[sub] > avg)].shape[0])
print(scores.groupby("Gender").groups)
for sub in subject:
    print(f"Above average {sub}")
    avg = scores[sub].mean()
    print(scores[(scores[sub] > avg)].groupby("Gender").groups)
