from abc import ABC, abstractmethod
class MusicPlayer(ABC):
    @abstractmethod
    def play(self,filename:str):
        pass

# For Multiple Audio format.
class Mp3Player(MusicPlayer):
    def play(self,file_name:str):
        print (f"Playing Mp3..{file_name}")
    
class WavPlayer(MusicPlayer):
    def play(self,file_name:str):
        print(f" Playing wav file : {file_name}")

class FlacPlayer(MusicPlayer):
    def play(self,file_name:str):
        print(f"Play Flac file : {file_name}")

#  Strategy Pattern..
class Sound_enhancement(ABC):
    @abstractmethod
    def sound_enabled(self,file_name:str):
        pass

class BassBoost(Sound_enhancement):
    def sound_enabled(self, file_name):
        print(f"Sound for Bassound : {file_name}")


class Surround_sound(Sound_enhancement):
    def sound_enabled(self,file_name):
        print(f"Sound for Surround : {file_name}")

#  Factory Method..
class Factoy_method(ABC):
    @staticmethod
    def get_player(file_name):
        players={
            'mp3': Mp3Player(),
            'wav':WavPlayer(),
            'Flac':FlacPlayer()
        }
        return players.get(file_name,None)

class Music:
    def __init__(self,strategy):
        self.straegy=strategy
    
    def play_music(self,filename:str):
        extension = filename.split('.')[-1]
        player=Factoy_method.get_player(extension)

        if player:
            player.play(filename)
            self.straegy.sound_enabled(filename)
        else:
            print(f"File unsupported..")

if __name__=="__main__":
    # factory = Factoy_method()
    # file = factory.get_player('ddlj.wav')
    # print(file)

    system=Music(BassBoost())
    system.play_music('songs.wav')

    system1 = Music(Surround_sound())
    system1.play_music('surround.wav')