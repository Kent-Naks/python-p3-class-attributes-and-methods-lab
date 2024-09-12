from song import Song

def test_song_class():
    # Create Song instances
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Hotline Bling", "Drake", "Pop")
    song3 = Song("Single Ladies", "Beyonce", "Pop")
    song4 = Song("Shape of You", "Ed Sheeran", "Pop")
    song5 = Song("Rolling in the Deep", "Adele", "Pop")
    song6 = Song("Bohemian Rhapsody", "Queen", "Rock")
    song7 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    # Print total number of songs
    print(f"Total number of songs: {Song.count}")
    # Should print 7

    # Print unique genres
    print(f"Unique genres: {Song.genres}")
    # Should print ['Rap', 'Pop', 'Rock']

    # Print unique artists
    print(f"Unique artists: {Song.artists}")
    # Should print ['Jay-Z', 'Drake', 'Beyonce', 'Ed Sheeran', 'Adele', 'Queen', 'Nirvana']

    # Print count of songs per genre
    print(f"Genre count: {Song.get_genre_count()}")
    # Should print {'Rap': 1, 'Pop': 5, 'Rock': 2}

    # Print count of songs per artist
    print(f"Artist count: {Song.get_artist_count()}")
    # Should print {'Jay-Z': 1, 'Drake': 1, 'Beyonce': 1, 'Ed Sheeran': 1, 'Adele': 1, 'Queen': 1, 'Nirvana': 1}

if __name__ == "__main__":
    test_song_class()
