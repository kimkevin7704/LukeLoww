from flask import (
    Flask,
    render_template, 
    )


app = Flask(__name__)


@app.route('/home', methods=['GET'])
def view_home():
    return render_template('/home.html')


@app.route('/contact', methods=['GET'])
def view_contact():
    return render_template('/contact.html')


@app.route('/gallery', methods=['GET'])
def view_gallery():
    return render_template('/gallery.html')


@app.route('/music', methods=['GET'])
def view_music():
    return render_template('/music.html')


@app.route('/index', methods=['GET'])
def view_index():
    return render_template('/index.html')
