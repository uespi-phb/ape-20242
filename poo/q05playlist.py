
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song_name):
        self.songs.append(song_name)

    def remove_song(self, song_name):
        self.songs.remove(song_name)

    def show_songs(self):
        digits = len(str(len(self.songs)))

        print(f'Playlist: {self.name}')
        for song_no, song_name in enumerate(self.songs):
            print('%0*d.%s' % (digits, song_no + 1, song_name))


playlist = Playlist('Minhas Músicas')

for k in range(15):
    playlist.add_song(f'Música #{k + 1}')

playlist.show_songs()
