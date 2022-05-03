import jwt
from cryptography.hazmat.primitives import serialization

AUTH0_DOMAIN = 'dev-yw768gnr.us.auth0.com'
API_AUDIENCE = 'OG9L0zaI9TGTzro7U1QnpM7epjAIXeKf'
ALGORITHMS = "RS256"
CLIENT_SECRET = 'kl5rNIFagI8IzyUNkDFw45-FfQ-bp-7j6hR_9s_DroL7vqYd2Twmr8ZC-LxpRSXA'


# token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk2WjJGbExGM1V3R1FPak5fejZCayJ9.eyJpc3MiOiJodHRwczovL2Rldi15dzc2OGduci51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU4OTEyNDgwNTgyMDY1MzA2NzUiLCJhdWQiOiJodHRwczovL2RyZi1hdXRoMC8iLCJpYXQiOjE2NDg2OTA0NTQsImV4cCI6MTY0ODY5NzY1NCwiYXpwIjoiT0c5TDB6YUk5VEdUenJvN1UxUW5wTTdlcGpBSVhlS2YiLCJzY29wZSI6IiJ9.UfcL2BOVvnJm7agrhpU8YgVT59LTCwBquzRZwszT5L7m8D4a4jSBxA7PRRwvIlcQ9ZznCV86NwCZ2KCCYisoxzjo9twWJ4eSoJpm9lJxdEw17sCRcsFAh9wuuRRkWXJrw3TH5Azj4TOHCT50nl_D6oEEEnuBrsbEpZG1PqzFZkqjusUsGJXJrAdQKtSxKhUyX-f6Am5HNXdESWqoIkFoeA1mKwmR-cPvndVKa0nW2z_WLWIBBMTm5wWr4p441rTF1tOjDgsldBG_AKoclTTBqNu4FZj24SyxERaLu_XIqwWPise6tUNz4WlKN84zaneXf_xIR7nkOBedbYd70Hd_lg"
# header_data = jwt.get_unverified_header(token)
# print(header_data)
# x = jwt.decode(
#     token,
#     key=CLIENT_SECRET,
#     # key=CLIENT_SECRET,
#     algorithms=[header_data['alg'], ]
#     # audience=API_AUDIENCE,
#     # issuer="https://" + AUTH0_DOMAIN + "/",
#
# )
# print(x)

def generate_token():
    payload_data = {
        "sub": "4242",
        "name": "Jessica Temporal",
        "nickname": "Jess"
    }

    my_secret = CLIENT_SECRET
    token = jwt.encode(
        payload=payload_data,
        key=my_secret
    )
    print(token)


generate_token()
private_key = open('.ssh/id_rsa', 'r').read()
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')
