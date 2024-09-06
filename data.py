import pandas as pd
import matplotlib.pyplot as plt
from analysis import dataset_analysis


def load_dataset():
    """Load the dataset from CSV file."""
    return pd.read_csv('IMDB-Movie-Data.csv')


def display_movie_info(movie_data):
    """Display movie information."""
    for index, row in movie_data.iterrows():
        print(f"[{index}] {row['Title']} ({row['Year']}) - Rating: {row['Rating']} - Votes: {row['Votes']} | Director: {row['Director']}")


def filter_movies_by_rating(dataset, sort_order, num_movies):
    """Filter and display movies based on rating."""
    sorted_movies = dataset.sort_values(by='Rating', ascending=sort_order).head(num_movies)
    display_movie_info(sorted_movies)


def filter_movies_by_votes(dataset, sort_order, num_movies):
    """Filter and display movies based on votes."""
    sorted_movies = dataset.sort_values(by='Votes', ascending=sort_order).head(num_movies)
    display_movie_info(sorted_movies)


def filter_movies_by_genre(dataset, genre):
    """Filter and display movies based on genre."""
    filtered_dataset = dataset[dataset['Genre'].str.contains(genre, case=False, na=False)]
    display_movie_info(filtered_dataset)


def main():
    """Main function to interact with the user."""
    dataset = load_dataset()
    dataset.info()
    print("--Hello! Welcome to the Movies Dataset--")

    rules = ['Best Movies', 'Worst Movies', 'Most Votes', 'Less Votes', 'Movie Descriptions', 'Datasets Analysis']

    while True:
        print("\nOptions:")
        for i, rule in enumerate(rules):
            print(f'{i}: {rule}')
        user_choice = int(input("Enter your choice (0-5): "))

        if user_choice == 0:
            num_movies = int(input("How many top-rated movies do you want to see?: "))
            filter_movies_by_rating(dataset, False, num_movies)
        elif user_choice == 1:
            num_movies = int(input("How many lowest-rated movies do you want to see?: "))
            filter_movies_by_rating(dataset, True, num_movies)
        elif user_choice == 2:
            num_movies = int(input("Enter the number of top-voted movies you want to see?: "))
            filter_movies_by_votes(dataset, False, num_movies)
        elif user_choice == 3:
            num_movies = int(input("Enter the number of least-voted movies you want to see?: "))
            filter_movies_by_votes(dataset, True, num_movies)
        elif user_choice == 4:
            genre = input("Enter the genre you want to see?: ")
            filter_movies_by_genre(dataset, genre)
        elif user_choice == 5:
            column = input("Enter the column name for analysis (e.g., 'Rating', 'Genre'): ")
            num_movies = int(input("Enter the number of movies you want to see?: "))
            dataset_analysis(dataset, column, num_movies)
        else:
            print("[x] Invalid choice!")
            continue

        user_choice = input("Do you want to continue? (yes/no): ")
        if user_choice.lower() != 'yes':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
