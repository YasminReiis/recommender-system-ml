class Recommender:
    def __init__(self):
        self.data = None

    def train(self, df):
        self.data = df

    def recommend(self, user_id):
        return self.data[self.data["user_id"] == user_id]["item_id"].tolist()
