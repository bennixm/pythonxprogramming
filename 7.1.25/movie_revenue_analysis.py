import pandas as pd

class MovieRevenueAnalysis:
    def __init__(self, movies_file, netflix_file):
        self.movies_file = movies_file
        self.netflix_file = netflix_file
        self.movies_df = None
        self.netflix_df = None
        self.merged_df = None

    def load_data(self):
        self.movies_df = pd.read_csv(self.movies_file)
        self.netflix_df = pd.read_csv(self.netflix_file)

    def clean_data(self):
        self.movies_df['title'] = self.movies_df['title'].str.strip().str.lower()
        self.netflix_df['title'] = self.netflix_df['title'].str.strip().str.lower()

    def merge_data(self):
        self.merged_df = pd.merge(self.movies_df, self.netflix_df, how='left', on='title')

    def calculate_profit(self):
        self.merged_df['Profit'] = self.merged_df['revenue'].fillna(0) - self.merged_df['budget'].fillna(0)

    def get_top_profitable_movies(self):
        ranked_movies = self.merged_df.sort_values(by='Profit', ascending=False)
        return ranked_movies[['title', 'Profit']].head(10)

    def get_profitable_genres(self):
        genre_profit = self.merged_df.groupby('genres')['Profit'].mean().reset_index()
        return genre_profit.sort_values(by='Profit', ascending=False)

    def analyze(self):
        self.load_data()
        self.clean_data()
        self.merge_data()
        self.calculate_profit()
        
        top_movies = self.get_top_profitable_movies()
        profitable_genres = self.get_profitable_genres()
        
        print("\nTop 10 Most Profitable Movies:\n", top_movies)
        print("\nMost Profitable Genres:\n", profitable_genres)

if __name__ == "__main__":
    movie_analysis = MovieRevenueAnalysis('7.1.25/movie_dataset.csv', '7.1.25/netflix_titles.csv')
    movie_analysis.analyze()
