#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import (Flask, render_template, request, Response, flash, redirect, url_for)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import datetime
from sqlalchemy import Column, Integer, DateTime
from flask import jsonify
import sys
from flask import Flask, abort


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# TODO: connect to a local postgresql database


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Please find data insertion in data_insertion.sql file

joinTable= db.Table(
   'joinTable',
   db.Column( 'Venue.id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
   db.Column( 'Artist.id',db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
)

class Show(db.Model):
    __tablename__ = 'Show'

    start_time = db.Column(db.String(120), primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
    artist_image_link = db.Column(db.String(500))
    artist_name = db.Column(db.String)
    venue_name = db.Column(db.String)
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500),  default=None)
    facebook_link = db.Column(db.String(120),  default=None)
    genres = db.Column(db.String(120), nullable=False)
    past_shows_count = db.Column(db.Integer, default=0)
    website = db.Column(db.String(120),  default=None)
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500), default=None)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    past_shows = db.Column(db.String(500), default=None )
    upcoming_shows = db.Column(db.String(500),  default=None )
    show = db.relationship('Artist', secondary=joinTable, backref=db.backref('Venues', lazy=True))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500),  default=None )
    facebook_link = db.Column(db.String(120),  default=None )
    website = db.Column(db.String(120),  default=None )
    seeking_venue = db.Column(db.Boolean,  default=False )
    seeking_description = db.Column(db.String(500),  default=None )
    upcoming_shows_count = db.Column(db.Integer,  default=0)
    past_shows_count = db.Column(db.Integer,  default=0)
    past_shows = db.Column(db.String(500),  default=None )
    upcoming_shows = db.Column(db.String(500),  default=None )
    show = db.relationship('Venue', secondary=joinTable, backref=db.backref('Artists', lazy=True))


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


 

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------
def takeThird(elem):
    return elem[2]

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
 
  data = []
  city_list = db.session.query( Venue.city, Venue.state, Venue.id ).distinct(Venue.city).all()
  city_list.sort(key=takeThird)


  for city in city_list:
    venues = []
    venue_list = Venue.query.filter(Venue.city== city.city).order_by('id').all()
    for v in venue_list:
      upcoming_shows =  Venue.query.filter(Show.venue_id==city.id).count()
      venue = {"id": v.id , "name": v.name, "num_upcoming_shows": upcoming_shows}
      venues.append(venue)
    city_venue = {"city": city.city , "state": city.state, "venues": venues}
    data.append(city_venue)

  return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

  search_1=request.form.get('search_term', '')
  searchAndResult = Venue.query.filter(Venue.name.ilike('%'+search_1+'%'))
  data = []

  for r in searchAndResult:
      venue = {"id": r.id , "name": r.name, "num_upcoming_shows": r.upcoming_shows_count}
      data.append(venue)
  
  response={ "count": len(data), "data": data}

  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id

  return render_template('pages/show_venue.html', venue=Venue.query.get(venue_id))

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  #DONE
  # TODO: modify data to be the data object returned from db insertion

  error = False
  body = {}
  try:
    name = request.form['name'] 
    city = request.form['city'] 
    state = request.form['state'] 
    address = request.form['address'] 
    phone = request.form['phone'] 
    genres = request.form['genres'] 
    facebook_link = request.form['facebook_link']

    venue = Venue( name=name, city=city, state=state, address=address, phone=phone, genres=genres, facebook_link=facebook_link)
    
    db.session.add(venue)
    db.session.commit()

  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
    flash('An error occurred. Venue ' + name + ' Must be not listed.')
  finally:
    db.session.close()
  if error:
    flash('An error occurred. Venue ' + name + ' could not be listed.')
  else:
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
    
  # # TODO: on unsuccessful db insert, flash an error instead.
  # # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')



@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  try:
      Venue.query.filter_by(id=venue_id).delete()
      db.session.commit()
  except:
      db.session.rollback()
  finally:
      db.session.close()
  return render_template('pages/home.html')
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  
  result_1 = Artist.query.all()
  data = []

  for result in result_1:
      artist = {"id": result.id , "name": result.name }
      data.append(artist)
  
  return render_template('pages/artists.html', artists=data)


@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  

  search_1=request.form.get('search_term', '')
  searchAndResult = Artist.query.filter(Artist.name.ilike('%'+search_1+'%'))
  data = []

  for r in search_1:
      artist = {"id": r.id , "name": r.name, "num_upcoming_shows": r.upcoming_shows_count}
      data.append(artist)
  
  response={ "count": len(data), "data": data}
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  
  return render_template('pages/show_artist.html', artist=Artist.query.get(artist_id))


#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  result = Artist.query.get(artist_id)
  form = ArtistForm(obj=result)
  # TODO: populate form with fields from artist with ID <artist_id>
  # facebooklink is not working
  return render_template('forms/edit_artist.html', form=form, artist=result)



@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes


  artist = Artist.query.get(artist_id)

  artist.name = request.form['name'] 
  artist.city = request.form['city']  
  artist.state = request.form['state']  
  artist.phone = request.form['phone'] 
  artist.genres = request.form['genres'] 
  artist.facebook_link = request.form['facebook_link']  

  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  db.session.commit()

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  # TODO: populate form with values from venue with ID <venue_id>
  # facebooklink is not working

  result = Venue.query.get(venue_id)
  form = VenueForm(obj=result)

  return render_template('forms/edit_venue.html', form=form, venue=result)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes

  venue = Venue.query.get(venue_id)

  venue.name = request.form['name'] 
  venue.city = request.form.get('city') 
  venue.state = request.form.get('state')
  venue.address = request.form.get('address')
  venue.phone = request.form.get('phone')
  venue.genres = request.form.get('genres')
  venue.facebook_link = request.form.get('facebook_link')

  flash('Venue ' + request.form['name'] + ' was successfully listed!')
  db.session.commit()

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion


  error = False
  body = {}
  try:
    name = request.form.get('name')
    city = request.form.get('city')
    state = request.form.get('state') 
    phone = request.form.get('phone') 
    genres = request.form.get('genres')
    facebook_link = request.form.get('facebook_link')

    artist = Artist( name=name, city=city, state=state, phone=phone, genres=genres, facebook_link=facebook_link)
    
    db.session.add(artist)
    db.session.commit()

  except:
    error = True
    db.session.rollback()
    flash('An error occurred. Artist ' + name + ' could not be listed.')
  finally:
    db.session.close()
  if error:
    flash('An error occurred. Artist ' + name + ' could not be listed.')
  else:
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # on successful db insert, flash success
  # TODO: on unsuccessful db insert, flash an error instead.

  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
 
  return render_template('pages/shows.html', shows=Show.query.all())

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead

  error = False
  body = {}
  try:
    artist_id = request.form['artist_id'] 
    venue_id = request.form['venue_id'] 
    start_time = request.form['start_time'] 

    show = Show( artist_id=artist_id, venue_id=venue_id, start_time=start_time )
    
    db.session.add(show)
    db.session.commit()

  except:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
  if error:
    flash('Show was successfully listed!')
  else:
    flash('Show was successfully listed!')

  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
