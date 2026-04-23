import pandas as pd
from model import Recommender

df = pd.read_csv("data.csv")

model = Recommender()
model.train(df)

print("Sistema rodando!")
print(model.recommend(1))
