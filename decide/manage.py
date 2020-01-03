#!/usr/bin/env python
import os
import requests
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "decide.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
"""
if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = {'nombre': 'pepe','curso': 'us','nivel':'intermedio'}
    response= requests.get(url,params=args)
    print(response.content)
    if response.status_code == 200:
        response_json=response.json()
        origin = response_json['origin']
        print(origin)
        header = response_json['headers']
        print(header['Host'])
"""