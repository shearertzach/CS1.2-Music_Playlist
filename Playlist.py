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

    def length(self):
        current = self.__first_song
        counter = 0
        if current == None:
            print(f"There are no songs in this list")
        else:
            while current.get_next_song() != None:
                counter += 1
                current = current.get_next_song()

        return counter + 1


    def print_songs(self):
        current = self.__first_song
        counter = 1

        if current == None:
            print("No songs found!")
        else:
            while current != None:
                print(f'#{counter} {current.get_title()}')
                counter += 1
                current = current.get_next_song()

  