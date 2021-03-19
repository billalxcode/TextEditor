from os.path import splitext
from os.path import basename

class Core:
    def __init__(self):
        pass

    def readfile(self, path):
        reads = open(path, mode="r").read()
        return reads

    def writeFile(self, path, text=""):
        write = open(path, mode="w")
        write.write(text)
        write.close()
        
    def get_filename(self, path):
        base = basename(path)
        splits = splitext(base)
        return splits

    def get_info(self):
        info_dict = {
            "info": {
                "author": "Billal Fauzan",
                "version": 1.0,
                "source": ""
            }
        }

        return info_dict