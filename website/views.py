from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/albums', methods=['GET'])
def albums():
    return render_template('albums.html')

@views.route('/videos', methods=['GET'])
def videos():
    return render_template('videos.html')

@views.route('/images', methods=['GET'])
def images():
    return render_template('images.html')
