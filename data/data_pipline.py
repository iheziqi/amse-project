from get_data import get_data
from meta_data import get_germany_county_list, get_age_group, get_activity_dest
from load_to_sqlite import load_to_database

trip_info_url ='https://mobilithek.info/mdp-api/files/aux/573360269906817024/trip_count_matrix_county_by_age_activity_2022.csv' 

# load trip info to database
load_to_database(get_data(trip_info_url), 'trip_count_matrix_country_by_age_activity')
print('loading trip info done!')

# load metadata county of Germany to database
load_to_database(get_germany_county_list(), 'county_id')
print('loading county list done!')

# load metadata age group to database
load_to_database(get_age_group(), 'age_group')
print('loading age group done!')

#load metadata dest_activity to database
load_to_database(get_activity_dest(), 'activity_dest')
print('loading destination activity done!')