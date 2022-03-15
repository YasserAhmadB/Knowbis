# import http.client
#
# conn = http.client.HTTPSConnection("dev-yw768gnr.us.auth0.com")
#
# payload = "{\"client_id\":\"GvZttqdfhxI2kc3gqpKb9PoXOK6xFlof\",\"client_secret\":\"zQbaaXjZWXA_J30rZCkvP1nhvjubYCZoNFav8kTHNXLerKEJefGMME0vN3x5tojf\",\"audience\":\"https://users/\",\"grant_type\":\"client_credentials\"}"
#
# headers = {'content-type': "application/json"}
#
# conn.request("POST", "/oauth/token", payload, headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))

import http.client

conn = http.client.HTTPConnection("http://users/")

headers = {
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk2WjJGbExGM1V3R1FPak5fejZCayJ9.eyJpc3MiOiJodHRwczovL2Rldi15dzc2OGduci51cy5hdXRoMC5jb20vIiwic3ViIjoiR3ZadHRxZGZoeEkya2MzZ3FwS2I5UG9YT0s2eEZsb2ZAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vdXNlcnMvIiwiaWF0IjoxNjQ3MjEwMjY4LCJleHAiOjE2NDcyOTY2NjgsImF6cCI6Ikd2WnR0cWRmaHhJMmtjM2dxcEtiOVBvWE9LNnhGbG9mIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.sMPrgH_0igzMe2xac5RcqqKO_mr-mYtiEDRNM7mDqsxkwYSH_bhYDFos6Kc48k3pHHHIxOtLHawy4bhrzZKwtjaAABYwE39lubRUThb82uY_R5Jfw-GdBvOyqC60DrGqICew2I7PlDWQ8zF9vg0Ox3cNiJoyuzdj5HFUXcoMolqD9qKIOI5QSiNuNowOX4vc5qBKJXLQRA33CClhfcf3mU93_RkSrQZktUEirng3OSMRDHMqsIV4BfIj0aD1yB7nVwSszuof9R4grBj78LVzzU24IqHy3FKu0M4FHAGpFxUuTZPvHy12ycJWuJmaYuAGqMqjspymTtrYPq2u1yB43g",

}

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
