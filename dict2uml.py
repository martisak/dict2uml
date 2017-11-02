import json
import fileinput


def traverse(obj, parent):

    vertices = []
    edges = []

    for key, value in obj.iteritems():

        properties = []
        childobjects = {}
        childobjectsstr = []

        for k, v in value.iteritems():

            if isinstance(v, dict):
                (childobjectsstr
                    .append("{}: {}".format(k, "[object Object]")))
                childobjects[k] = v
            elif isinstance(v, list):

                for idx, a in enumerate(v):
                    (childobjectsstr
                        .append("{}: {}".format(k, "[List]")))
                    childobjects[idx] = a
            else:
                properties.append("{}: {}".format(k, v))

        vertices.append({
            "clsName": key,
            "clsNameFullReference": key,
            "clsProperties": properties,
            "clsObjects": childobjectsstr
        })

        if childobjects:
            p = "{}.{}".format(parent, key) if parent is not None else key
            tmpobj, tmprel = traverse(childobjects, p)

            for r in tmprel:
                edges.append(r)

            for o in tmpobj:
                o["clsNameFullReference"] = \
                    "{}.{}".format(key, o["clsNameFullReference"])
                vertices.append(o)

            for child in childobjects:
                if parent is not None:
                    edges.append("\"{}.{}\" -- \"{}.{}.{}\"".format(parent, key, parent, key, child ))
                else:
                    edges.append("\"{}\" -- \"{}.{}\"".format(key, key, child))

    return vertices, edges


def printClass(cls):
    print("class \"{}\" as {} {{"
          .format(cls["clsName"], cls["clsNameFullReference"]))

    print "\t" + ".. Properties .."
    if cls["clsProperties"]:
        for p in cls["clsProperties"]:
            print "\t" + p

    if cls["clsObjects"]:
        print "\t" + ".. Objects .."
        for o in cls["clsObjects"]:
            print "\t" + o

    print "}"

def dict2plantuml(d):
    if isinstance(d, dict):
        d = {"root": d}

        c, r = traverse(d, None)

        for cls in c:
            printClass(cls)

        for rel in r:
            print rel
    else:
        raise TypeError("The input should be a dictionary.")


if __name__ == "__main__":

    message = ""
    for line in fileinput.input():
        message += line

    d = json.loads(message)
    dict2plantuml(d)