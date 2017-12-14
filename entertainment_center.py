import fresh_tomatoes
import media

""" Create Movie instances """

# Toy Story Movie : movie title, story line, poster image and image trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
# Avatar Movie : movie title, story line, poster image and image trailer
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")

# The Godfather Movie : movie title, story line, poster image and image trailer
godfather = media.Movie(
    "The Godfather",
    "A story about the trials of the Corleone family",
    "https://upload.wikimedia.org/wikipedia/en/4/47/The_Godfather.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA")

# Hunger Games : movie title, story line, poster image and image trailer
hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Up : movie title, story line, poster image and image trailer
up = media.Movie(
    "Up",
    "A 78 year old balloon salesman, is about to fulfill a lifelong dream",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

# The Shining : movie title, story line, poster image and image trailer
shining = media.Movie(
    "The Shining",
    "A chilling movie about a writer who becomes a winter hotel caretaker",
    "https://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",
    "https://www.youtube.com/watch?v=3b726feAhdU")

# Set the movies that will be passed to the media file
movies = [toy_story, avatar, godfather, hunger_games, up, shining]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
