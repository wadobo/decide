#!/bin/bash

curl -X POST -d '{ "voting": 1, "auths": [ { "name": "auth1", "url": "http://localhost:8000" }, { "name": "auth2", "url": "http://localhost:9000" } ] }' -H "Content-Type: application/json" http://localhost:8000/mixnet/
