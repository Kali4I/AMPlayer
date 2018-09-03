from tkinter import (Tk,
                    LEFT,
                    RIGHT,
                    DoubleVar,
                    HORIZONTAL,
                    BOTH,
                    IntVar)
from easyttk import *
from tkinter.filedialog import askopenfilename
from sys import (platform, 
                argv)
from PIL import ImageTk, Image
import webbrowser
import os.path
import pygame

class Application:

    version = '1.3'

    def __init__(self):

        try:
            self.track = argv[1]

        except:
            self.track = None

        self.open_img           = Image.open('data/open.png').resize((16, 16), Image.BILINEAR)
        self.play_img           = Image.open('data/play.png').resize((16, 16), Image.BILINEAR)
        self.pause_img          = Image.open('data/pause.png').resize((16, 16), Image.BILINEAR)
        self.stop_img           = Image.open('data/stop.png').resize((16, 16), Image.BILINEAR)
        self.github_img         = Image.open('data/github.png').resize((16, 16), Image.BILINEAR)

        pygame.mixer.pre_init(44100, -16, 2, 1648)
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        pygame.mixer.init(freq, size, chan, 3072)
        pygame.mixer.init()

        self._window()

            
    def _play(self, file, loops=-1, offset=0):
        pygame.mixer.music.load(file)
        return pygame.mixer.music.play(loops,offset)


    def _open(self):
        filename = askopenfilename(filetypes=(
                                ('Все файлы',  '.*'),
                                ('WAVE Audio', '*.wav'),
                                ('MP3 Audio',  '*.mp3'),
                                ('OGG Audio',  '*.ogg')))
        self.root.title('AMPlayer v' + self.version + ' ' + os.path.basename(filename))
        if filename == '':
            return False
        return self._play(filename)

    def _window(self):
        self.root = Tk()

        open_img    = ImageTk.PhotoImage(self.open_img)
        stop_img    = ImageTk.PhotoImage(self.stop_img)
        pause_img   = ImageTk.PhotoImage(self.pause_img)
        play_img    = ImageTk.PhotoImage(self.play_img)
        github_img  = ImageTk.PhotoImage(self.github_img)

        music_volume_ = DoubleVar()
        music_volume_.set(1)

        def change_volume(event):
            pygame.mixer.music.set_volume(music_volume_.get())
            toolbar_volume['text'] = '{}%'.format(int(music_volume_.get() * 100))

        toolbar = WToolbar(self.root)
        WButton(toolbar, LEFT,   image=open_img,    command=lambda:  self._open())
        WButton(toolbar, LEFT,   image=pause_img,   command=lambda:  pygame.mixer.music.pause())
        WButton(toolbar, LEFT,   image=play_img,    command=lambda:  pygame.mixer.music.unpause())
        WButton(toolbar, LEFT,   image=stop_img,    command=lambda:  pygame.mixer.music.fadeout(1))
        WButton(toolbar, RIGHT,  image=github_img,  command=lambda:  webbrowser.open('https://github.com/AkiraSumato-01'))

        toolbar_volume = WLabel(toolbar, RIGHT, text='{}%'.format(int(music_volume_.get() * 100)), width=6)

        set_volume = WScale(toolbar, 
                            RIGHT, 
                            length=10, 
                            from_=0.0, 
                            to=1.0, 
                            orient=HORIZONTAL, 
                            variable=music_volume_, 
                            fill=BOTH, 
                            expand=True)

        set_volume.bind('<B1-Motion>', change_volume)

        if self.track is not None:
            play(track)

        self.root.geometry('420x26')
        self.root.resizable(False, False)
        self.root.title('AMPlayer v' + self.version)
        self.root.mainloop()

    
if __name__ == '__main__':
    Application()