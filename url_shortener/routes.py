from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .models import Link


shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    # Implement logic to redirect to the original URL associated with the 'shorten_url'
    return ""

@shortener.route('/create_link', methods=['POST'])  # Added missing slash in the route URL
def create_link():
    # Implement logic to create and store a new shortened URL
    original_url = request.form['original_url']
    link=Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    
    return render_template('link_success.html', 
        new_url=link.short_url,original_url=link.original_url)


@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('/analytics')
def analytics():
    # Implement logic to show analytics for shortened URLs
    return ""

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>Page not found 404</h1>', 404  # Fixed the syntax error in this line
