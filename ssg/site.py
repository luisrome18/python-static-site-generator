## import Path from pathlib
from pathlib import Path

##create a class called Site
class Site:
    ##create a Site class constructor that accepts three arguments self, source, and dest
    def __init__(self, source, dest):
        ##convert source to a Path object.
        self.source = Path(source)
        ##Repeat these steps for dest
        self.dest = Path(dest)

    ##Find root directory
    ##create a method called create_dir() that accepts two parameters, self and path
    def create_dir(self, path):
        ##create a variable called directory
        ###variable will need to contain the full path to the destination folder
        directory = self.dest / path.relative_to(self.source) ## first part of the path is self.dest. The second part of the path needs to be relative to self.sourc
        ##Make a directory
        ##call the mkdir() method on directory ##we want directory to be replaced if it exists.
        direcroty.mkdir(parents=True, exist_ok=True)

    ##Make the destination directory
    ##Create a new method called build() in the Site class
    def build(self):
        ##Call the mkdir() method on self.dest
        self.dest.mkdir(parents=True, exist_ok=True)##pass the following keyword arguments to mkdir(): "parents set to True" "exist_ok set to True"
        ##Recreate all paths
        for path in self.source.rglob("*"): ##create a for loop that iterates through the paths of self.source.rglob("*"). Call the current iteration path.
            if path.is_dir():##test if the current path is a directory.
                self.create_dir(path)##If it is a directory, call the create_dir() method of the class, and pass in the current path
