movies = {
"M1": {"title": "The Last Signal", "year": 2018, "rating": 8.4,
"genre": ["Sci-Fi", "Thriller"],
"cast": ("Rehan Kapoor", "Meera Sen")},
"M2": {"title": "Monsoon Diaries", "year": 2021, "rating": 7.6,
"genre": ["Drama", "Romance"],
"cast": ("Ananya Rao", "Vikram Joshi")},
"M3": {"title": "Code Red", "year": 2015, "rating": 6.9,
"genre": ["Action", "Thriller"],
"cast": ("Arjun Malhotra", "Divya Nair")},
"M4": {"title": "Silent Orbit", "year": 2023, "rating": 9.0,
"genre": ["Sci-Fi", "Drama"],
"cast": ("Kabir Singh", "Isha Verma")},
}

# 1. Print the cast (the tuple) of "M4".
print(movies["M4"]['cast'])
# 2. List the titles of all movies with "Sci-Fi" in their genre.
for k,v in movies.items():
    if 'Sci-Fi' in (v['genre']):
        print(k,v)

# 3. Find and print the title of the highest-rated movie.
rant = 0
for k,v in movies.items():
    rating = (v["rating"])
    if rating > rant:
        rant = rating

print(k,v['title'],rant)

# 4. Print all genres listed for "M2".
print(movies["M2"]['genre'])

# 5. Count how many movies were released after the year 2018.
count = 0
for k,v in movies.items():
     year = (v['year'])
     if 2018 == year:
         count+=1
    

print(count)

# 6. Add "Mystery" to the genre list of "M3".
movies["M3"]['genre'].append('Mystery')

print(movies)
