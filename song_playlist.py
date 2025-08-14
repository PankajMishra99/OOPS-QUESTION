from collections.abc import Iterable,Iterator
class Playlist(Iterable):
    def __init__(self):
        self._songs=[]
    
    def add_song(self,title):
        self._songs.append(title)
        print(f"Song {title} has been added successfully..")
    
    def __len__(self):
        return len(self._songs)
    
    def __iter__(self):
        return iter(self._songs)
    
    def __getitem__(self,index):
        return self._songs[index]
    
    def __reversed__(self)->Iterator[str]:
        return reversed(self._songs)

if __name__=="__main__":
    system = Playlist()
    system.add_song('A')
    system.add_song('B')

    len(system)
    print(system[0])
    for i in system:
        print(i)
    print(reversed(system))
