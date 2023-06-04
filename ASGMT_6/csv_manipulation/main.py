from convert_csv_to_list import convert_to_list
from sql_connector import DatabaseConnector
from database_credentials import database_credentials

'''
1. check if table exists
2. if table does not exists, create table
3. if table exists, insert data
'''

def main(db_connector):
    # check if table exists
    res = db_connector.connect_to_db("SELECT * FROM even_distribution;", False)
    if res is None:
        print("Sorry this table does not exists")
        db_connector.connect_to_db("CREATE TABLE `even_distribution`( `id` int(11) NOT NULL AUTO_INCREMENT, `user_id` VARCHAR(200) NOT NULL, `track_id` VARCHAR(100) NOT NULL, `active` int(11) NOT NULL,`campaign_type` VARCHAR(100) NOT NULL,`user_type` VARCHAR(2) NOT NULL, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=utf8", True)
    else:
        print("yeah the table exists", res)
        apple = convert_to_list("csvs/even.csv")
        print(len(apple), list(apple[0].keys()))
        # Apply filters => This is the filter the data and only permit entries of filters that match the rest we will ignore that data
        apple = list(filter(lambda a: a['active']=="0", apple))

        
        # apple = list(map(lambda a: a, apple))
        # insert data
        for entry in apple:
            print(entry)
            # before making entry into even_distribution (table), we need to add the track into the spotify_track
            track_id = make_entry_for_spotify_track(db_connector, entry)
            print("track_id", track_id[0][0])
            track_id = track_id[0][0]
            db_connector.connect_to_db(f"INSERT INTO even_distribution (user_id, track_id, active, campaign_type, user_type) VALUES ('{entry['user_id']}', '{track_id}', '{entry['active']}', '{entry['campaign_type']}', '{entry['user_type']}')", True)

    pass


def make_entry_for_spotify_track(db_connector, entry):
    res = db_connector.connect_to_db(f"SELECT id FROM spotify_tracks WHERE track_uid='{entry['track_id']}';", False)
    if res:
        print("Has data")
        return res
    print("Has NO data")
    db_connector.connect_to_db(f"INSERT INTO spotify_tracks (track_uid) VALUES ('{entry['track_id']}')", True)
    return db_connector.connect_to_db(f"SELECT id FROM spotify_tracks WHERE track_uid='{entry['track_id']}';", False)

if __name__ == "__main__":
    database = database_credentials
    db_connector = DatabaseConnector(database["db_name"], database["db_user"], database["db_password"], database["db_host"], database["db_port"])
    main(db_connector)
