import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/lity.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.matchHeight/0.7.0/jquery.matchHeight-min.js"></script>
    <script src="js/lity.min.js"></script>
    <script src="js/app.js"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Tobias Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {video_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 video-tile type-movie">
    <a href="{trailer_url}" data-lity>
        <div class="video-tile-inner">
            <div class="video-tile-top">
                <h2 class="video-tile-title"><span class="video-type"><i class="fa fa-film" aria-hidden="true"></i></span> {title}</h2>
            </div>
            <div class="video-tile-poster" style="background-image: url({poster_url});"></div>
            <p>{storyline}</p>
            <div class="extra-info">
                <span><i class="fa fa-star" aria-hidden="true"></i> {rating}</span>
                <span><i class="fa fa-clock-o" aria-hidden="true"></i> {duration}</span>
            </div>
        </div>
    </a>
</div>
'''

# A single tvshow entry html template
tvshows_tile_content = '''
<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 video-tile type-tvshow">
    <a href="{trailer_url}" data-lity>
        <div class="video-tile-inner">
            <div class="video-tile-top">
                <h2 class="video-tile-title"><span class="video-type"><i class="fa fa-tv" aria-hidden="true"></i></span> {title}</h2>
            </div>
            <div class="video-tile-poster" style="background-image: url({poster_url});"></div>
            <p>{storyline}</p>
            <div class="extra-info">
                <span><i class="fa fa-star" aria-hidden="true"></i> {rating}</span>
                <span><i class="fa fa-clock-o" aria-hidden="true"></i> {duration}</span>
            </div>
            <div class="extra-info">
                <span>{episodes} episodes</span>
                <span>{seasons} seasons</span>
            </div>
        </div>
    </a>
</div>
'''


def create_video_tiles_content(movies, tvshows):
    # The HTML content for this section of the page
    # Loops through the list of movies and the lists of tvshows
    content = ''
    for movie in movies:

        # Creats the content for movies
        content += movie_tile_content.format(
            title=movies[movie].title,
            storyline=movies[movie].storyline,
            poster_url=movies[movie].poster,
            trailer_url=movies[movie].trailer,
            duration=movies[movie].duration,
            rating=movies[movie].rating
        )

    for tvshow in tvshows:
        # Creates the content for tv-shows
        content += tvshows_tile_content.format(
            title=tvshows[tvshow].title,
            storyline=tvshows[tvshow].storyline,
            poster_url=tvshows[tvshow].poster,
            trailer_url=tvshows[tvshow].trailer,
            duration=tvshows[tvshow].duration,
            rating=tvshows[tvshow].rating,
            episodes=tvshows[tvshow].episodes,
            seasons=tvshows[tvshow].seasons
        )
    return content


def open_videos_page(movies, tvshows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the video tiles placeholder generated content
    rendered_content = main_page_content.format(
        video_tiles=create_video_tiles_content(movies, tvshows)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
