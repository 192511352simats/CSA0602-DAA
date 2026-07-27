def insert_song(playlist, song):
    playlist.append(song)
    i = len(playlist) - 2

    while i >= 0 and playlist[i][1] > song[1]:
        playlist[i + 1] = playlist[i]
        i -= 1

    playlist[i + 1] = song
    return playlist

n = int(input("Enter number of songs: "))
playlist = []

for i in range(n):
    name = input("Enter song name: ")
    duration = int(input("Enter duration (seconds): "))
    playlist.append((name, duration))

new_name = input("Enter new song name: ")
new_duration = int(input("Enter new song duration: "))

print("Updated Playlist:")
for song in insert_song(playlist, (new_name, new_duration)):
    print(song)
