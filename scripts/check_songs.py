#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This little script checks
which songs are considered finished,
i.e. which song has three files with the same
name with 3 extensions:
    - .txt (lyrics)
    - .ly
    - .pdf (score)
It updates a index: index.md
"""
import os
import pathlib

index = "index.md"
directory = "./songs/"

class Song:
    suffixes =  "f.txt txt pdf f.ly ly".split()
    def __init__(self, basename):
        self.basename = basename
        for suffix in self.suffixes:
            setattr(self, suffix.replace('.','_'), os.path.exists(basename.with_suffix(f'.{suffix}')))
        self._modified = None

    def __last_modif(self):
        """Return the epoch value for the last file modified"""
        return __time(os.path.getmtime,
                lambda x, y : x > y,
                '_modified')

    def statusof(self, name):
        """Status of txt, pdf, ly.
        Possible values:
            -1 (not found)
            0 unfinished
            1 finished"""
        if name == "txt":
            if self.f_txt:
                return 1
            if self.txt:
                return 0
        elif name == "ly":
            if self.f_ly:
                return 1
            if self.ly:
                return 0
        elif name == "pdf":
            if self.pdf:
                return 1
        return -1
    
    def link_of(self, name):
        """Return a link to the file matching with name"""
        if name in ("txt","ly"):
            if self.statusof(name) == 1:
                return self.basename + f"f.{name}"
            elif self.statusof(name) == 0:
                return self.basename + f".{name}"
        if self.statusof('pdf') == 1:
            return self.basename.with_suffix('pdf')
        return ''


    def __created(self):
        """Return the epoch value for the first file created"""
        # probably impossible on *nix
        pass
    
    def __time(self, func_time, func_compare, name):
        if getattr(self, name) is not None:
            return getattr(self, name)

        self._modified = 0
        for suffix, file_exists in self.__dict__.items():
            if file_exists:
                val = func_time(basename.with_suffix(f".{suffix.replace('_','.')}"))
                if func_compare(val, getattr(self,name):
                    setattr(self, name,val)
        return self._modified

    def _is_finished(self):
        """True if song is finished"""
        return self.statusof('txt') == self.statusof('pdf') == self.statusof('ly') == 1

    modification_time = property(self.__last_modif)
    is_finished = property(self._is_finished)


def analyse_content():
    """Analyse the content of the directory"""
    files = os.listdir(directory)
    basic_names = set([pathlib.Path(name).with_suffix('') for name in files ])
    return [Song(basename) for basename in basic_names]

def update_index(data):
    """Update index with a list of Songs"""
    # unordered list of songs in a string format
    str_data = {}

    status = ":white_check_mark: :heavy_check_mark: :x:".split()

    for song in data:
        txt_status = status[song.statusof('txt')]
        txt_link = song.link_of('txt')
        ly_status = status[song.statusof('ly')]
        ly_link = song.link_of('ly')
        pdf_status = status[song.statusof('pdf')]
        pdf_link = song.link_of('pdf')

        str_data[song] = f"{song.basename} | [{txt_status}](songs/{txt_link}) | [{ly_status}](songs/{ly_link}) | [{pdf_status}](songs/{pdf_link})"

    # alphabetical order
    alphabetical_order = ""
    for song, str_val in sorted(str_data.items(),key=lambda k,v:k.basename):
        alphabetical_order += str_val + '\n'

    # finished order
    finish_order = ""
    for song, str_val in sorted(str_data.items(),key=lambda k,v: k.modification_time):
        if song.is_finished is False:
            continue
        finish_order += str_val + '\n'

    # headers
    headers = """
TXT | LY | PDF
--- | -- | ---
"""

    str_value = """
# Liste alphabétique des chants
{headers}
{alphabetical_order}
#Listes des chants finis par ordre d'achèvement
{headers}
{finish_order}
"""
    with open(index,'w') as f:
        f.write(str_value)
        
    



