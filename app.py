from flask import Flask, render_template, request

from helpers import get_movie_info

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/moviesearch")
def movie_search():
    return render_template('moviesearch.html')


@app.route('/search_movie', methods=['POST'])
def search_movie():
    movie_title = request.form.get('movie_title')
    movie_found, movie_list = get_movie_info(movie_title)
    print(f"Searching for movie: {movie_title}")
    print(f"Movie found: {movie_found}")
    print(f"Number of movies found: {len(movie_list)}")
    print(f"Movie list: {movie_list}")

    return render_template('moviesearch.html', movie_found=movie_found, movie_list=movie_list)

if __name__=="__main__":
    app.run(debug=True)
