import pandas as pd


class Search:
    # This class provides utility functions to work with Rick and Morty database
    def __init__(self, what):
        """Provide "character" or "episode" or "location" as a valid argument"""
        self.df = pd.read_csv(f"rick_and_morty_{what}s.csv")
        self.schema = self.df.columns

    def get_all_names(self):
        print(self.df.name)

    def find_ID_by_name(self, name):
        print(self.df[self.df.name == name].id)

    def find_by_id(self, id):
        if id is None:
            print("You need to pass id of character to get output.")
            print("To get list of all characters, use getall() method.")
            return
        return self.df[self.df.id == id]
