-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.names FROM cities, states WHERE states.state_id = state.id AND states.name = 'California' ORDER BY cities.id ASC;
