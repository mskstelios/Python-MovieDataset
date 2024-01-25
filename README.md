

  <h1>Movies Dataset Analysis</h1>

  <p>This Python script interacts with a dataset of movies to provide various functionalities to the user:</p>

  <h2>Functions:</h2>

  <ul>
    <li>
      <h3>load_dataset():</h3>
      <p>Loads the movie dataset from a CSV file using pandas.</p>
    </li>
    <li>
      <h3>display_movie_info(movie_data):</h3>
      <p>Iterates through the dataset and displays information about each movie, including its index, title, year, rating, number of votes, and director.</p>
    </li>
    <li>
      <h3>filter_movies_by_rating(dataset, sort_order, num_movies):</h3>
      <p>Sorts the movies in the dataset based on their rating in either ascending or descending order and then displays the top or bottom 'num_movies' movies accordingly.</p>
    </li>
    <li>
      <h3>filter_movies_by_votes(dataset, sort_order, num_movies):</h3>
      <p>Sorts the movies based on the number of votes they received and displays the top or bottom 'num_movies' movies accordingly.</p>
    </li>
    <li>
      <h3>filter_movies_by_genre(dataset, genre):</h3>
      <p>Filters the dataset based on the provided genre and displays information about the movies that belong to that genre.</p>
    </li>
    <li>
      <h3>main():</h3>
      <p>Main function to interact with the user. Presents a menu of options for the user to choose from:</p>
      <ul>
        <li>Option 0: Displays the top-rated movies.</li>
        <li>Option 1: Displays the lowest-rated movies.</li>
        <li>Option 2: Displays the top-voted movies.</li>
        <li>Option 3: Displays the least-voted movies.</li>
        <li>Option 4: Allows the user to filter movies by genre.</li>
        <li>Option 5: Performs analysis on the dataset based on a user-specified column (e.g., 'Rating', 'Genre').</li>
      </ul>
      <p>After each operation, the user is prompted whether they want to continue or exit.</p>
    </li>
  </ul>

  <p>Users can choose from various options such as viewing top-rated or top-voted movies, analyzing datasets, and more.</p>

</body>
</html>
