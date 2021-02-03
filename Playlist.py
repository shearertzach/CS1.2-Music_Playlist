from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


def add_song(self, title):
        current = self.__first_song
        new_song = Song(title)

        if current == None:
            self.__first_song = new_song
        else:
            while current.get_next_song() != None:
                current = current.get_next_song()
            current.set_next_song(new_song)

    def find_song(self, title):
        current = self.__first_song
        found = False
        index = 0

        while current != None and not found:
            if current.get_title() == title:
                found = True
            else:
                current = current.get_next_song()
                index + 1

        return index

    def remove_song(self, title):
        current = self.__first_song
        prev = None
        found = False

        while not found:
            if current == None:
                print(f"Could not find song with name {title}")
                found = True
                return
            elif current.get_title() == title:
                found = True
            else:
                prev = current
                current = current.get_next_song()

        if prev == None:
            self.__first_song = current.get_next_song()
        else:
            prev.set_next_song(current.get_next_song())

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    pass


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    pass

  