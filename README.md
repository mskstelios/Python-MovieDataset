
<body>
    <h1>Movie Dataset Analyzer</h1>
    <p>
        This Python script allows users to interactively explore a movie dataset. It offers options to filter movies by 
        rating, votes, and genre, as well as to perform custom data analysis. The dataset used is the 
        <strong>IMDB-Movie-Data.csv</strong> file, which includes various attributes like movie titles, ratings, votes, 
        directors, and genres.
    </p>

  <h2>Key Features:</h2>
    <ul>
        <li><strong>Load Dataset</strong>: The dataset is loaded from a CSV file.</li>
        <li><strong>Display Movie Info</strong>: Movie titles, ratings, votes, and directors are printed in a user-friendly format.</li>
        <li><strong>Filter by Rating</strong>: Users can display the best or worst-rated movies.</li>
        <li><strong>Filter by Votes</strong>: Users can view movies with the most or fewest votes.</li>
        <li><strong>Filter by Genre</strong>: Movies can be filtered based on a specific genre.</li>
        <li><strong>Custom Analysis</strong>: Users can perform custom analysis by specifying a column (e.g., 'Rating' or 'Genre').</li>
    </ul>

  <h2>Code Overview:</h2>
    <h3>1. Imports:</h3>
    <ul>
        <li><code>pandas</code> for data manipulation.</li>
        <li><code>matplotlib.pyplot</code> for potential visualizations (not yet used in this version).</li>
        <li><code>dataset_analysis</code> from the <code>analysis</code> module, which provides custom data analysis.</li>
    </ul>

  <h3>2. Functions:</h3>
    <ul>
        <li><code>load_dataset()</code>: Loads the movie dataset from a CSV file.</li>
        <li><code>display_movie_info()</code>: Displays formatted information about the movies.</li>
        <li><code>filter_movies_by_rating()</code>: Filters and displays movies based on their ratings.</li>
        <li><code>filter_movies_by_votes()</code>: Filters and displays movies based on the number of votes.</li>
        <li><code>filter_movies_by_genre()</code>: Filters and displays movies based on a specified genre.</li>
        <li><code>main()</code>: The main interactive function where users select options to filter or analyze the dataset.</li>
    </ul>

  <h3>3. User Interaction:</h3>
    <p>
        Users are prompted to choose options like viewing top-rated movies, lowest-rated movies, movies by votes, or filtering by genre. 
        They can also request a custom analysis by selecting a column for deeper insights.
    </p>
</body>
</html>
