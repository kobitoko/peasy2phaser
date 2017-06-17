import sys
import json
hasPillow = False
try:
    from PIL import Image
    hasPillow = True
except ImportError:
    print("pillow library not found. \nCan ignore this if you want to convert a Peasy file.")

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

        # Check if it's physics-body-editor-box2d-2.9.2 format.
        elif "imagePath" in test and "origin" in test:
            if not hasPillow:
                print("Trying to convert a Physics Body Editor (Box2D) file, needs Python Imaging Library (https://python-pillow.org/).\nWill exit now.")
                exit(0)
            img = Image.open(test["imagePath"])
            self._width = img.size[0]
            self._height = img.size[1]

        # exit, format not recognized.
        else:
            print("Json is not in a peasy or Box2D format.")
            exit(0)
        print("Image is of size " + str(self._width) + "x" + str(self._height))

    def convert(self):
        # rigitBodies contains a list of dictionaries which are the objects.
        # Each these objects have a name. In Peasy you cannot name them yet so they're all called "shape"
        # These objects have a polygon entry which contains a list that has a list of dictionaries containing x and y points.
        # Origin normalized coordinates start at bottom left for Physics Body Editor Box2D. Peasy's is i assume top right.
        #
        # Phaser is a dictionary of objects which has a list of dicts containing shape info etc.
        phaser = {}
        density = 2
        friction = 0
        bounce = 0
        filter = { "categoryBits": 1, "maskBits": 65535 }
        for eachObject in self._json["rigidBodies"]:
            phaser[eachObject["name"]] = []
            if self._isPeasy:
                objects = eachObject["polygons"]
            else:
                objects = eachObject["shapes"]
            for eachShape in objects:
                """
                From [
                    {
                        "x": 0.510416686534882,
                        "y": 1.40625
                    },
                    {
                        "x": 0.458333343267441,
                        "y": 1.36458337306976
                    },
                    {
                        "x": 0.447916656732559,
                        "y": 0.46875
                    }
                ]
                TO
                {
					"density": 2, "friction": 0, "bounce": 0, 
					"filter": { "categoryBits": 1, "maskBits": 65535 },
					"shape": [   10, 191  ,  26, 158  ,  25, 186  ,  13, 204  ]
				}  """
                shape = []
                if self._isPeasy:
                    shapeList = eachShape
                else:
                    shapeList = eachShape["vertices"]
                for eachPoint in shapeList:
                    if self._isPeasy:
                        shape.append(eachPoint["x"]*self._width)
                        shape.append(eachPoint["y"]*self._height)
                    else:
                        # Physics Body Editor For some reason it normalise on width
                        shape.append(eachPoint["x"]*self._width)
                        oldY = eachPoint["y"]*self._width
                        shape.append(self._height - oldY)
                        #shape.append(oldY)

                phaser[eachObject["name"]].append({"density": density, "friction": friction, "bounce": bounce, "filter": filter,"shape": shape})
        print("converting done.")
        return phaser

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Needs at least 1 argument, the file to convert.")
        exit()
    f = open(sys.argv[1], "r")
    newFile = open("Converted_" + sys.argv[1], 'w')
    jsonLoaded = json.loads(f.read())
    f.close()
    json.dump(Converter(jsonLoaded).convert(), newFile)
    newFile.close()
