import flask
import json

chestsBackend = flask.Flask(__name__)

with open('chests.json') as f:
    data = json.load(f)
    locations = [d["coordinates"] for d in data if d["type"] == "loot"]


@chestsBackend.route('/locations')
def getLocations():
    resp = flask.Response(str(locations))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@chestsBackend.route('/distance')
def findDistances():
    locs = flask.request.args.getlist('endpoints')
    locs = [int(loc) for loc in locs]
    k = int(flask.request.args.get('numChests'))
    resp = flask.Response(str(path(locs[0], k, getEdgeTo(locs[1]))))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def getEdgeTo(v):
    with open('distances/distance' + str(v)) as f:
        edgeTo = f.read()[2:-2].split('], [')
        edgeTo = [[int(num) for num in line.split(",")] for line in edgeTo]
        return edgeTo



def path(u, k, edgeTo):
    if not edgeTo[u][k]:
        return []
    p = [u]
    while k > 0:
        u = edgeTo[u][k]
        k -= 1
        p.append(u)
    print(p)
    return p



