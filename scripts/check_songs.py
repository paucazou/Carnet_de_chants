#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This little script checks
which songs are considered finished,
i.e. which song has three files with the same
name with 3 extensions:
    - .doc (lyrics)
    - .ly
    - .pdf (score)
It updates a index: index.md
"""
import os
import pathlib

index = "index.md"
finish = "finished"
directory = "./songs/"
with open("finished") as f:
    finish_content = f.read().split('\n')
    finish_content = [pathlib.Path(elt) for elt in finish_content]

class Song:
    suffixes =  "doc pdf ly".split()
    def __init__(self, basepath):
        self.basename = basepath.name
        self.basepath = basepath
        for suffix in self.suffixes:
            setattr(self, suffix, os.path.exists(basepath.with_suffix(f'.{suffix}')))
        self._modified = None

    def __repr__(self):
        return self.basename.__str__()

    def __last_modif(self):
        """Return the epoch value for the last file modified"""
        return self.__time(os.path.getmtime,
                lambda x, y : x > y,
                '_modified')

    def statusof(self, name):
        """Status of doc, pdf, ly.
        Possible values:
            -1 (not found)
            0 unfinished
            1 finished"""
        if not getattr(self,name):
            return -1
        if not (name == "pdf") and self.basepath.with_suffix('.'+name) not in finish_content:
            return 0
        return 1
    
    def link_of(self, name):
        """Return a link to the file matching with name"""
        return self.basename + "." + name if os.path.exists(self.basepath.with_suffix('.' + name)) else ''

    def __created(self):
        """Return the epoch value for the first file created"""
        # probably impossible on *nix
        pass
    
    def __time(self, func_time, func_compare, name):
        if getattr(self, name) is not None:
            return getattr(self, name)

        self._modified = 0
        for suffix in self.suffixes:
            if getattr(self,suffix.replace('.','_')):
                val = func_time(self.basepath.with_suffix(f".{suffix}"))
                if func_compare(val, getattr(self,name)):
                    setattr(self, name,val)
        return self._modified

    def _is_finished(self):
        """True if song is finished"""
        return self.statusof('doc') == self.statusof('pdf') == self.statusof('ly') == 1

    modification_time = property(__last_modif)
    is_finished = property(_is_finished)


def analyse_content():
    """Analyse the content of the directory"""
    files = os.listdir(directory)
    basic_names = set([pathlib.Path(directory + name).with_suffix('') for name in files  if name[0] != '.'])
    return [Song(basename) for basename in basic_names]

def update_index(data):
    """Update index with a list of Songs"""
    # unordered list of songs in a string format
    str_data = {}

    status = ":white_check_mark: :heavy_check_mark: :x:".split()

    for song in data:
        doc_status = status[song.statusof('doc')]
        doc_link = song.link_of('doc')
        ly_status = status[song.statusof('ly')]
        ly_link = song.link_of('ly')
        pdf_status = status[song.statusof('pdf')]
        pdf_link = song.link_of('pdf')

        str_data[song] = f"{song.basename} | [{doc_status}](songs/{doc_link}) | [{ly_status}](songs/{ly_link}) | [{pdf_status}](songs/{pdf_link})"

    # alphabetical order
    alphabetical_order = ""
    for song, str_val in sorted(str_data.items(),key=lambda x:x[0].basename):
        alphabetical_order += str_val + '\n'

    # finished order
    finish_order = ""
    for song, str_val in sorted(str_data.items(),key=lambda x: x[0].modification_time):
        if song.is_finished is False:
            continue
        finish_order += str_val + '\n'

    # headers
    headers = """Nom | DOC | LY | PDF
--- | --- | -- | ---"""

    str_value = f"""
# Liste alphabétique des chants
{headers}
{alphabetical_order}# Liste des chants finis par ordre d'achèvement
{headers}
{finish_order}"""

    with open(index,'w') as f:
        f.write(str_value)

if __name__ == "__main__":
    data = analyse_content()
    #from IPython import embed; embed()
    update_index(data)

        
    



