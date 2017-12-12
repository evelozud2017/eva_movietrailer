import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
                        
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

godfather = media.Movie("The Godfather",
                        "A story about the trials of the Corleone family",
                        "https://upload.wikimedia.org/wikipedia/en/4/47/The_Godfather.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")


hunger_games = media.Movie("Hunger Games",
                        "A really real reality show",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63a7H0bo")

up = media.Movie("Up",
                "A 78 year old balloon salesman, is about to fulfill a lifelong dream",
                "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

shining = media.Movie("The Shining",
                "A chilling movie about a writer who becomes a winter hotel caretaker",
                "https://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",
                "https://www.youtube.com/watch?v=3b726feAhdU")

movies = [toy_story, avatar, godfather, hunger_games, up, shining]
fresh_tomatoes.open_movies_page(movies)


