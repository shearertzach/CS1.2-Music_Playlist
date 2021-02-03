class Song:

    def __init__(self, title):
      self.__title = title
      self.__next_song = None

    def __init__(self, title):  
        self.__title = title
        self.__next_song = None

    def get_title(self):
        return self.__title

    def set_title(self, title):
        old_title = self.__title
        self.__title = title
        return f"You have renamed {old_title} to {title}"

    def get_next_song(self):
        if self.__next_song != None:
            return self.__next_song
        else:
            return None


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    pass


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    pass
