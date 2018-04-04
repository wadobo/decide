import urllib
import requests
from django.conf import settings


def query(modname, entry_point='/', method='get', baseurl=None, **kwargs):
    '''
    Function to query other votinus modules

    :param modname: is the module name, voting, mixnet, etc
    :param entry_point: is the path to query
    :param method: is the http method
    :param baseurl: used to override settings module, useful for auths

    This function returns the json returned. If there's a problem an
    execption will be raised.

    Optional parameters

    This function can receive optional parameters to complete the query,
    you can complete the query with GET params using the **params** keyword
    and with json data, using the **json** keyword.

    Examples

    >>> r = query('voting', params={'id': 1})
    >>> assert(r[0]['id'] == 1)

    >>> r = query('mixnet', entry_point='/shuffle/1/', json={'msgs': msgs, 'pk': pk})
    >>> assert(len(r) == len(msgs))
    '''

    if not baseurl:
        mod = settings.APIS.get(modname, settings.BASEURL)
    else:
        mod = baseurl

    q = getattr(requests, method)
    url = '{}/{}{}'.format(mod, modname, entry_point)

    params = kwargs.get('params', None)
    if params:
        url += '?{}'.format(urllib.parse.urlencode(params))

    if method == 'get':
        response = q(url)
    else:
        json_data = kwargs.get('json', {})
        response = q(url, json=json_data)

    return response.json()


def get(*args, **kwargs):
    return query(*args, method='get', **kwargs)


def post(*args, **kwargs):
    return query(*args, method='post', **kwargs)
