"""
Recommender Systems Practice
----------------------------
This script builds an Item-Based Collaborative Filtering 
Recommender System using the MovieLens dataset. It calculates 
similarities between movies based on user rating correlations.

Datasets: u.data, Movie_Id_Titles
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Suppress runtime warnings for dividing by zero in correlation calculations
warnings.filterwarnings('ignore')

def get_recommendations(movie_title: str, moviemat: pd.DataFrame, ratings: pd.DataFrame, min_ratings: int = 60) -> pd.DataFrame:
    """
    Calculates movie recommendations based on correlation with user ratings.
    Filters out movies with fewer than `min_ratings` to ensure reliability.
    """
    print(f"\nFinding recommendations for: {movie_title} (Min Ratings: {min_ratings})")
    
    # Grab user ratings for the specific movie
    user_ratings = moviemat[movie_title]
    
    # Calculate correlation with all other movies
    similar_to_movie = moviemat.corrwith(user_ratings)
    
    # Clean data and create a dataframe
    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    
    # Join with the number of ratings to allow filtering
    corr_movie = corr_movie.join(ratings['num of ratings'])
    
    # Filter by minimum ratings and sort by highest correlation
    recommendations = corr_movie[corr_movie['num of ratings'] > min_ratings].sort_values('Correlation', ascending=False)
    
    return recommendations.head()


def main():
    # 1. Load and Merge Data
    print("Loading MovieLens datasets...")
    columns_name = ['user_id', 'item_id', 'rating', 'timestamp']
    df = pd.read_csv('u.data', sep='\t', names=columns_name)
    movie_titles = pd.read_csv('Movie_Id_Titles')
    
    df = pd.merge(df, movie_titles, on='item_id')
    
    # 2. Aggregate Ratings Data
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
    
    # 3. Exploratory Data Analysis (EDA)
    sns.set_style('white')
    
    plt.figure(figsize=(10, 6))
    sns.jointplot(x='rating', y='num of ratings', data=ratings, alpha=0.5)
    plt.suptitle("Jointplot: Average Rating vs Number of Ratings", y=1.02)
    plt.show()

    # 4. Create User-Item Matrix
    print("Building User-Item Matrix...")
    moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

    # 5. Generate Recommendations
    # Star Wars (1977)
    star_wars_recs = get_recommendations('Star Wars (1977)', moviemat, ratings, min_ratings=70)
    print(star_wars_recs)
    
    # Liar Liar (1997)
    liar_liar_recs = get_recommendations('Liar Liar (1997)', moviemat, ratings, min_ratings=60)
    print(liar_liar_recs)


if __name__ == "__main__":
    main()
