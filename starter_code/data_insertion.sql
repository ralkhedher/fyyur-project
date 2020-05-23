INSERT INTO "Venue" VALUES ( 1,  'The Musical Hop', 'San Francisco', 'CA', '1015 Folsom Street',  '123-123-1234',  'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60',
 'https://www.facebook.com/TheMusicalHop', 'Jazz,Reggae,Swing,Classical,Folk', 0, 'We are on the lookout for a local artist to play every two weeks. Please call us.',
0, 'https://www.themusicalhop.com', True, null, null);


INSERT INTO "Venue" VALUES ( 2,  'The Dueling Pianos Bar', 'New York', 'NY', '335 Delancey Street',  '914-003-1132',  'https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
 'https://www.facebook.com/theduelingpianos', 'Classical, R&B, Hip-Hop', 0,  null,
0, 'https://www.theduelingpianos.com', False, null, null);


INSERT INTO "Venue" VALUES ( 3,  'Park Square Live Music & Coffee', 'San Francisco', 'CA', '34 Whiskey Moore Ave',  '415-000-1234',  'https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80',
 'https://www.facebook.com/ParkSquareLiveMusicAndCoffee', 'Rock n Roll, Jazz, Classical, Folk', 1,  null,
1, 'https://www.parksquarelivemusicandcoffee.com', False, null, null);


INSERT INTO "Artist" VALUES ( 4, 'Guns N Petals', 'San Francisco', 'CA', '326-123-5000', 'Rock n Roll','https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
'https://www.facebook.com/GunsNPetals', 1, 0, 'https://www.gunsnpetalsband.com', True, 'Looking for shows to perform at in the San Francisco Bay Area!', null, null );


INSERT INTO "Artist" VALUES ( 5, 'Matt Quevedo', 'New York', 'NY', '300-400-5000', 'Jazz','https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
'https://www.facebook.com/mattquevedo923251523', 1, 0, null, False, null, null, null );


INSERT INTO "Artist" VALUES ( 6, 'The Wild Sax Band', 'San Francisco', 'CA', '432-325-5432', 'Jazz, Classical','https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
null, 0, 3, null, True, null, null, null );


INSERT INTO "Show" VALUES ('2019-05-21T21:30:00.000Z', 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
 'Guns N Petal', 'The Musical Hop', 1, 4);


INSERT INTO "Show" VALUES ('2019-06-15T23:00:00.000Z', 'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
  'Matt Quevedo', 'Park Square Live Music & Coffee',3, 5);


INSERT INTO "Show" VALUES ('2035-04-01T20:00:00.000Z', 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
   'The Wild Sax Band', 'Park Square Live Music & Coffee' 3, 6);

INSERT INTO "Show" VALUES ('2035-04-08T20:00:00.000Z', 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
    'The Wild Sax Band', 'Park Square Live Music & Coffee', 3, 6);

INSERT INTO "Show" VALUES ('2035-04-15T20:00:00.000Z', 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
     'The Wild Sax Band', 'Park Square Live Music & Coffee',3, 6);
