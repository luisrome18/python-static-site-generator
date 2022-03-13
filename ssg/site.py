## import Path from pathlib
from pathlib import Path

##create a class called Site
class Site:
    ##create a Site class constructor that accepts three arguments self, source, and dest
    ###parameter to the constructor parameter list called parsers. Set the default value to of parsers to None
    def __init__(self, source, dest, parsers=None):
        ##convert source to a Path object.
        self.source = Path(source)
        ##Repeat these steps for dest
        self.dest = Path(dest)
        ##instance variable called parsers to the expression parsers or []
        self.parsers = parsers or []

    ##Find root directory
    ##create a method called create_dir() that accepts two parameters, self and path
    def create_dir(self, path):
        ##create a variable called directory
        ###variable will need to contain the full path to the destination folder
        directory = self.dest / path.relative_to(self.source) ## first part of the path is self.dest. The second part of the path needs to be relative to self.sourc
        ##Make a directory
        ##call the mkdir() method on directory ##we want directory to be replaced if it exists.
        directory.mkdir(parents=True, exist_ok=True)

    ##Make the destination directory
    ##Create a new method called build() in the Site class
    ##Recreate all paths
    ##create a for loop that iterates through the paths of self.source.rglob("*"). Call the current iteration path.
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.isfile():
                self.run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, source)
        else:
            print("Not Implemented")
