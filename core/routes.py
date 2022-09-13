from datetime import datetime
from core.database import URLs
from core import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['shortUrl']

        if short_id and URLs.query.filter_by(short_id=short_id).first() is not None:
            flash('Please enter another short ID!')
            return redirect(url_for('index'))

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = URLs(
            long_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<string:short_id>')
def baby_url(short_id):
    if (URLs.query.filter_by(short_id=short_id).first()):
        return redirect(URLs.query.filter_by(short_id=short_id).first().long_url)
    else:
        flash("Invalid URL")
        return redirect(url_for('index'))