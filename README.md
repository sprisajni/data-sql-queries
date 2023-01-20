## Background & Objectives

The goal of this challenge is to query fetch information from multiple tables using `JOIN`.

To acquire instant Jedi skills in `JOIN` queries, [read this](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) - the picture is really helpful.

## Data
We will work with the `movies.sqlite` database available at this URL:  
`https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite`

Using your preferred method, place the `movies.sqlite` file in the `data` directory of this challenge.

## Specs

Complete the code in `queries.py`. Each function takes a `db` argument, which is a cursor connected to the database, on which you can call the `execute` function. Exactly like in the previous exercise.

### Detailed movies

- Implement `detailed_movies` to get all the movie titles with the corresponding genre and director name.
- This function should return a list of tuples like (`title`, `genre`, `name`).

### Late released movies

- Implement `never_watched_movies` to get the list of all movies which were released after their director passed away.
- This function should return a list of movie `titles`.

### Statistics

- Implement `stats_on` to get the statistics on a given genre, i.e. the number of movies and the average movie length (in minutes).
- This function should return a dictionary of statistics like:

```python
results = stats_on(db, "Action,Adventure,Comedy")
print(results)
=> {
    'genre': 'Action,Adventure,Comedy',
    'number_of_movies': 153,
    'avg_length': 100.98
}
```

### Top 5

- Implement `top_five_directors_for` to get the top 5 directors that made the most movies for a given genre.
- This function should return a list of tuples like (`name`, `number_of_movies`).
- In case of a tie, directors should be sorted in alphabetical order.

```python
results = top_five_artists(db, "Action,Adventure,Comedy")
print(results[0])
=> [
    ('Robert Rodriguez', 5),
    ('Jonathan Frakes', 4),
    ('Anthony C. Ferrante', 3),
    ('Barry Sonnenfeld', 3),
    ('Jackie Chan', 3)
]
```

### Movie duration buckets

To **'bin'** (or **'bucket'**) the range of values means to divide the entire range of values into a series of intervals, and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal width. Data binning is used for example for histograms(https://en.wikipedia.org/wiki/Histogram).

- Implement `movie_duration_buckets` to get the buckets of the movies according to duration.
- The widh of each bucket should be **30 min**
- For example, the bucket **30** will contain the count of all the movies with a duration between **0 min** and **30 min**.
- Or, in terms of an SQL query, the value for bucket **30** should be equal to `SELECT COUNT(*) FROM movies WHERE minutes < 30`
- This method should return a list of tuples like (`max_duration`, `movie_count`):

```python
movie_duration_buckets(db)
=> [(30, 292), (60, 764), (90, 1362), [...],(690, 2), (900, 1), (1020, 1)]
```

### Top 5 youngest newly directors

- Implement `top_five_youngest_newly_directors` to get the top 5 youngest directors when directing their first movie.
- This function should return a list of tuples like (`name`, `age_when_first_time_director`).
