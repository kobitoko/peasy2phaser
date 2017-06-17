import sys
import json

class Converter():
    def __init__(self, json):
        self._json = json
        if not "rigidBodies" in self._json:
            print("Json is not in a peasy or Box2D format.")
            exit(0)
        self.checkWhich()

    def checkWhich(self):
        test = self._json["rigidBodies"][0]
        self._isPeasy = False

        # Check if it's Peasy format
        if "height" in test and "width" in test:
            self._width = test["width"]
            self._height = test["height"]
            self._isPeasy = True

        # exit, format not recognized.
        else:
            print("Json is not in a peasy format.")
            exit(0)
        print("Image is of size " + str(self._width) + "x" + str(self._height))

    def convert(self, density=2, friction=0, bounce=0,categoryBits=1, maskBits=65535):
        # rigitBodies contains a list of dictionaries which are the objects.
        # Each these objects have a name. In Peasy you cannot name them yet so they're all called "shape"
        # These objects have a polygon entry which contains a list that has a list of dictionaries containing x and y points.
        # Normalized coordinates in Peasy's is top left.
        # Phaser is a dictionary of objects which has a list of dicts containing shape info etc.
        phaser = {}
        filter = {"categoryBits": categoryBits, "maskBits": maskBits}
        for eachObject in self._json["rigidBodies"]:
            phaser[eachObject["name"]] = []
            for eachShape in eachObject["polygons"]:
                shape = []
                for eachPoint in eachShape:
                    if self._isPeasy:
                        shape.append(eachPoint["x"]*self._width)
                        shape.append(eachPoint["y"]*self._height)
                phaser[eachObject["name"]].append({"density": density, "friction": friction, "bounce": bounce, "filter": filter,"shape": shape})
        print("converting done.")
        return phaser

if __name__ == "__main__":
    print("Argument 1 is the json file to convert.\nArgument2 is density, 3 is friction, 4 is bounce, 5 is categoryBits, 6 is maskBits.")
    print("Defaults are 2 0 0 1 65535")
    if len(sys.argv) < 2:
        print("Needs at least 1 argument: the file to convert.")
        exit()
    elif len(sys.argv) >2:
        for each in sys.argv[2:]:
            if not each.isdigit():
                print("One of the arguments after the input file isn't a number.")
                exit()
    f = open(sys.argv[1], "r")
    newFile = open("Converted_" + sys.argv[1], 'w')
    jsonLoaded = json.loads(f.read())
    f.close()
    json.dump(Converter(jsonLoaded).convert(), newFile)
    newFile.close()
    print("File saved as Converted_" + sys.argv[1])
