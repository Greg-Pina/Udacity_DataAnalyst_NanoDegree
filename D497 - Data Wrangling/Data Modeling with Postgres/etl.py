import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Process a single song file and insert data into the songs and artists tables.
    
    - Reads JSON song data from `filepath`
    - Extracts and inserts data into the `songs` and `artists` tables.
    """
    # Open song file
    df = pd.read_json(filepath, lines=True)

    # Insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)

    # Insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Process a single log file and insert data into time, users, and songplays tables.
    
    - Reads JSON log data from `filepath`
    - Filters for 'NextSong' page actions
    - Extracts and inserts data into the `time`, `users`, and `songplays` tables.
    """
    # Open log file
    df = pd.read_json(filepath, lines=True)

    # Filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # Convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')

    # Insert time data records
    time_df = pd.DataFrame({
        'start_time': df['ts'],
        'hour': df['ts'].dt.hour,
        'day': df['ts'].dt.day,
        'week': df['ts'].dt.isocalendar().week,
        'month': df['ts'].dt.month,
        'year': df['ts'].dt.year,
        'weekday': df['ts'].dt.weekday
    })

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, row.tolist())

    # Load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']].drop_duplicates()

    # Rename columns to match schema
    user_df.rename(columns={'userId': 'user_id', 'firstName': 'first_name', 'lastName': 'last_name'}, inplace=True)

    # Insert user records
    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, row.tolist())

    # Insert songplay records
    for _, row in df.iterrows():
        # Get songid and artistid from songs and artists tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        song_id, artist_id = results if results else (None, None)

        # Insert songplay record
        songplay_data = (
            row.ts, row.userId, row.level, song_id, artist_id,
            row.sessionId, row.location, row.userAgent
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Processes all JSON files in a directory using a specified function.

    - Retrieves all JSON files from `filepath`
    - Iterates through each file and applies the `func`
    - Commits transactions and prints progress
    """
    # Get all files matching extension from directory
    all_files = get_files(filepath)

    # Get total number of files found
    num_files = len(all_files)
    print(f'{num_files} files found in {filepath}')

    # Iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print(f'{i}/{num_files} files processed.')


def get_files(filepath):
    """
    Returns a list of all JSON files in a directory and its subdirectories.
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files


def main():
    """
    - Establishes database connection
    - Processes song_data and log_data
    - Closes the connection
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()