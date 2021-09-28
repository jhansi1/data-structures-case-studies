from Queue import Queue
from Stack import Stack

# Add songs to the playlist queue
def add_to_playlist(song):
    playlist_queue.enqueue(song)
    print ("Loading to playlist - " + song)

# Dequeue the front song from the playlist queue and start playing it
# Also push it the played stack
def play_song():
    song = playlist_queue.dequeue()
    if song:
        played_stack.push(song)
        print("Playing " + song)
    else:
        print("Error: No more songs left in the playlist")

# Dequeues the front song from the playlist queue and start playing it
# Also push it the played stack
def next_song():
    song = playlist_queue.dequeue()
    if song:
        played_stack.push(song)
        print("Playing " + song)
    else:
        print("Error: No more songs left in the playlist")

# Pop the current song and then play the previous one without removing it from the stack
# Actually, the previous song is removed from the stack but then has to be immediately put back again 
# since it's playing now as the current song. So we just do a peek instead of removing and adding back again
def prev_song():
    current_song = played_stack.pop()
    if (current_song == None):
        print("Error: No more songs left in the played stack")
    else:
        previous_song = played_stack.peek()
        if (previous_song):
            print("Playing " + previous_song)
        else:
            print("Error: No more songs left in the played stack")


if __name__ == '__main__':
    # Instantiating the playlist and played stack objects.
    playlist_queue = Queue()
    played_stack = Stack()

    # Building a playlist
    add_to_playlist("Stairway to Heaven - Led Zepplin")
    add_to_playlist("Bohemian Rhapsody - Queen")
    add_to_playlist("We will rock you - Queen")
    add_to_playlist("Back in Black - AC/DC")
    add_to_playlist("Chop Suey - System of a down")

    # Start playing
    play_song()

    # Play next and previous songs
    next_song()
    next_song()
    prev_song()
    next_song()
    prev_song()
    prev_song()
    prev_song()
    next_song()
    next_song()

