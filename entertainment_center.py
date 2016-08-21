import json
import media
import os
import tobias_tomatoes

# All information is saved in a json file in order to keep it clean
# I ran into two problems when doing this.
# First was how to parse json files in python
# Second was how to access the index from a python list and json array
# Third was how to find the relative path of the file
# Found the answers in the three links below.
# http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
# http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
# http://stackoverflow.com/questions/1270951/python-how-to-refer-to-relative-paths-of-resources-when-working-with-code-repo


# Load the json file containing the information of the videos
json_video_file_location = os.path.join(
    os.path.dirname(__file__), 'videos.json')

with open(json_video_file_location) as data_file:
    videos = json.load(data_file)

# Creates the movies_list
movies_list = {}

# Loops through the json array for all movies and creates a movie for each
for index, movie in enumerate(videos["movies"]):
    movies_list[index] = media.Movie(movie["title"],
                                     movie["storyline"], movie["poster"],
                                     movie["trailer"], movie["duration"],
                                     movie["rating"])

# Creates the tvshows_list
tvhshows_list = {}

# Loops through the json array for all tv-shows and creates a tv-show for each
for index, tvhshow in enumerate(videos["tvshows"]):
    tvhshows_list[index] = media.TvShow(tvhshow["title"],
                                        tvhshow["storyline"],
                                        tvhshow["poster"],
                                        tvhshow["trailer"],
                                        tvhshow["duration"],
                                        tvhshow["rating"],
                                        tvhshow["episodes"],
                                        tvhshow["seasons"])

tobias_tomatoes.open_videos_page(movies_list, tvhshows_list)
