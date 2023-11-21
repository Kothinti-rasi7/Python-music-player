import vlc
import os

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_track = None
        self.instance = vlc.Instance()

    def add_song(self, path):
        media = self.instance.media_new(path)
        self.playlist.append(media)

    def play(self):
        if self.current_track is None:
            self.current_track = self.playlist.pop(0)
            self.media_player = self.instance.media_player_new()
            self.media_player.set_media(self.current_track)
            self.media_player.play()
        else:
            self.media_player.play()

    def pause(self):
        self.media_player.pause()

    def stop(self):
        self.media_player.stop()
        self.current_track = None

    def next_track(self):
        self.stop()
        if len(self.playlist) > 0:
            self.play()

def browse_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    player = MusicPlayer()
    while True:
        print("\nAvailable commands: add, play, pause, stop, next, quit")
        command = input("Enter a command: ").lower()

        if command == "add":
            file_path = browse_file()
            player.add_song(file_path)
            print(f"Added: {file_path}")
        elif command == "play":
            player.play()
        elif command == "pause":
            player.pause()
        elif command == "stop":
            player.stop()
        elif command == "next":
            player.next_track()
        elif command == "quit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()