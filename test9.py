import pandas as pd
data = pd.read_csv("tweets.csv")

from collections import Counter
Counter(" ".join(data["tweet"]).split()).most_common(10)