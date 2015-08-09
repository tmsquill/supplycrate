__author__ = 'Zivia'

import json
import urllib


max_request_size = 200


def pull_data(url=None):

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    return data


def pretty_json(data=None):

    return json.dumps(data, indent=4, sort_keys=True)
