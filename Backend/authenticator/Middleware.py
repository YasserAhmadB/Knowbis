from django.http import JsonResponse, HttpRequest
from jose import jwt
from rest_framework.request import Request

AUTH0_DOMAIN = 'dev-yw768gnr.us.auth0.com'
API_AUDIENCE = 'OG9L0zaI9TGTzro7U1QnpM7epjAIXeKf'
ALGORITHMS = "RS256"
CLIENT_SECRET = 'kl5rNIFagI8IzyUNkDFw45-FfQ-bp-7j6hR_9s_DroL7vqYd2Twmr8ZC-LxpRSXA'

"""
Cache the key available at https://{AUTH0_DOMAIN}/.well-known/jwks.json as a python dict
"""
AUTH0_PUBLIC_KEY = {"keys": [{"alg": "RS256", "kty": "RSA", "use": "sig",
                              "n": "uWT7g3dwSzX0qBqmtV1UJSmjaoZNQ9QaVdt19_cowBrMT5lnD9RNtI7aXEjawcx-j6JTriycLf4GGMVaJ3o6NEWJM1nltwC6vqeOSkPxbERxB9Ln5FXDROeAmXOKnks4gPk7qcc9-Ch3lJSUkxmdCwV78GfBQYL68_FCqSH9axGr8EM_uz8AiXACpeIzjaKomYs38j2Y1rvOsy4M2Fd7bdrty0eeeW1qXX1-i9-fbpMANAeFqzVrtPqCh4hgkr_7h6TyNWbkGh7cXW6B69Dc3gCkwSSxWHCh3Cw-i_SVw-Qd7YehplgZ0RUv5mcS0DTR1h-V76mnzVIJcBRwmrbe3Q",
                              "e": "AQAB", "kid": "96Z2FlLF3UwGQOjN_z6Bk", "x5t": "D1ZEeMQJ8rob8V0vh4G3qyHFNB4",
                              "x5c": [
                                  "MIIDDTCCAfWgAwIBAgIJFiHQ79dQUhAFMA0GCSqGSIb3DQEBCwUAMCQxIjAgBgNVBAMTGWRldi15dzc2OGduci51cy5hdXRoMC5jb20wHhcNMjIwMzEzMjA1OTUxWhcNMzUxMTIwMjA1OTUxWjAkMSIwIAYDVQQDExlkZXYteXc3NjhnbnIudXMuYXV0aDAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuWT7g3dwSzX0qBqmtV1UJSmjaoZNQ9QaVdt19/cowBrMT5lnD9RNtI7aXEjawcx+j6JTriycLf4GGMVaJ3o6NEWJM1nltwC6vqeOSkPxbERxB9Ln5FXDROeAmXOKnks4gPk7qcc9+Ch3lJSUkxmdCwV78GfBQYL68/FCqSH9axGr8EM/uz8AiXACpeIzjaKomYs38j2Y1rvOsy4M2Fd7bdrty0eeeW1qXX1+i9+fbpMANAeFqzVrtPqCh4hgkr/7h6TyNWbkGh7cXW6B69Dc3gCkwSSxWHCh3Cw+i/SVw+Qd7YehplgZ0RUv5mcS0DTR1h+V76mnzVIJcBRwmrbe3QIDAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBQqZGiUDBbwWlr7lQnYbm+V1hkdeDAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAHQwM6OzZ2inIQBAkwZGYWMInx7j2TU+ln+CIUYC9h/vKh43fi5YPj24WUK+b/8bFJtBiL4+POnErNCav06Om4uvhZvyYMuG/kPGNIbNn7p3cBum5MtALqwcm5hL9Dj71UFoDpx7gRrJU7eyS1q/jhiGjDlsoMIpdwa+C3/9Yl3e9RHo1MkyILtXuvZgzXltZvfnR32nMQxKgB71PKGXx+CcLbRV+PnHAhCr+u3AbziRUkPEgl7S3zwfDoI/wPawOwTf0aZTU5m3zf5O+TbJBYA+oaOuxEfOxXKKYPDmonw45mPVhcbCSxRKL7eH+I54ym6T1qXfljS5ypciIc1dYQI="]},
                             {"alg": "RS256", "kty": "RSA", "use": "sig",
                              "n": "wKzedmzu3hVRlXt-PSmIW4KvU7ZrXGtZPvTGGy_R27UVXat4zQwmAUT4sxqGVfDrNuNuYYPaWJv1NgHReAucVh6JGzzA5Ge5TrVH3I1wfOA3oAeMoiGb_NV0z5Ydtxl4Jt_G5ZjYnj94voebHIG-jyjgP6CqY1WoniJ4Xbc65lu3oCfRajCqahReIg8jKNpy4yr7eRD-EXbPJ6_kE_hkiwBkUQ6Gwj2T-sR-OThDRnoEyiOuARJTDVhGIJhYnzkcbQlnNm6oOhblOFLOiKiJhfC8pvwR0UwV1DhY9mPLGFse9Wqg5EQBNFlvaqxqW6X82HvA41U8CZSlw_yjrgfW2Q",
                              "e": "AQAB", "kid": "OXaQt6B1UwmXCv9CbaCuF", "x5t": "Hf8GHlyxMZ6ka_kfISDma0biBRk",
                              "x5c": [
                                  "MIIDDTCCAfWgAwIBAgIJTjOI54zfvu1WMA0GCSqGSIb3DQEBCwUAMCQxIjAgBgNVBAMTGWRldi15dzc2OGduci51cy5hdXRoMC5jb20wHhcNMjIwMzEzMjA1OTUyWhcNMzUxMTIwMjA1OTUyWjAkMSIwIAYDVQQDExlkZXYteXc3NjhnbnIudXMuYXV0aDAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwKzedmzu3hVRlXt+PSmIW4KvU7ZrXGtZPvTGGy/R27UVXat4zQwmAUT4sxqGVfDrNuNuYYPaWJv1NgHReAucVh6JGzzA5Ge5TrVH3I1wfOA3oAeMoiGb/NV0z5Ydtxl4Jt/G5ZjYnj94voebHIG+jyjgP6CqY1WoniJ4Xbc65lu3oCfRajCqahReIg8jKNpy4yr7eRD+EXbPJ6/kE/hkiwBkUQ6Gwj2T+sR+OThDRnoEyiOuARJTDVhGIJhYnzkcbQlnNm6oOhblOFLOiKiJhfC8pvwR0UwV1DhY9mPLGFse9Wqg5EQBNFlvaqxqW6X82HvA41U8CZSlw/yjrgfW2QIDAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBQkwPJMJEytmHHzr8x7mxjJsU4WhzAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAE/W35Q/72Cz6Hz7iPb2uHbr2ReAg6x4J0Ahp3iK1yEC74926J4ootijVCOkNbbAm+fcKwNV5gHOJVyIvmTSNqef36gdsQDSt1P6MZIBK8NrToIciQlFuciemDB4qSrWH08p4QVh0gzznhxB2oLFP/LYagIYlJ3wdcA1G/X8ndyERRd36Hqi1hb20aZIWVYcsnafOm0bavd/m8QgO5H8UvvlPhZf6+P/oZrSIcaapyRXnxeQJUtEwBYRNTPJ9ZjkYjLsdpXv9UZCmSp+8cSKuVYzO1V378kui9ceOQHYtq+dD6I/vc0ye2N/cggvzmqqld/JeFBEqe6CIJNTXUQ9Qz0="]}]}


# access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk2WjJGbExGM1V3R1FPak5fejZCayJ9.eyJpc3MiOiJodHRwczovL2Rldi15dzc2OGduci51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU4OTEyNDgwNTgyMDY1MzA2NzUiLCJhdWQiOiJodHRwczovL2RyZi1hdXRoMC8iLCJpYXQiOjE2NDg2ODI3NzQsImV4cCI6MTY0ODY4OTk3NCwiYXpwIjoiT0c5TDB6YUk5VEdUenJvN1UxUW5wTTdlcGpBSVhlS2YiLCJzY29wZSI6IiJ9.eSC8Dy8I5CepXqyUjr_I765y-9Udwhr1FJZn6_M4H9qK2yBrs1gpY2A39ZkEqMOQmMkRlxY2UgBnrzVoKrqP1NObNxqGcbvcfmM9GQPCgzwf1O4Y17iZqZYY-CBC2f6QWdhm7I8xHS89CSH0DlnlV66KUqyP3iJ1wVXx31hoZVFr7NZfhQAyXvx8G29mR6mCbRWms8FBhiKAO_dltW12CWYzEXfWi8Uzjklzi7ose-NXaMiQooDjMoBobuuHlNbh4dRkDBzM7FKNaRcTGojb2JSR9G4Smnqyl2cpd6AsryyFIkjYjOCfe5fjUJiSXYvlOAbAfBt61LvcwjiENfaquw&expires_in=7200&token_type=Bearer

class Auth0Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        print('__call__')
        print('__call__')
        print('__call__')
        print('__call__')
        # GET TOKEN
        print(request.GET)
        # print(request.headers)
        # auth = request.META.get('HTTP_AUTHORIZATION')

        # if not auth:
        #     return JsonResponse(data={"code": "1authorization_header_missing",
        #                               "description":
        #                                   "Authorization header is expected"}, status=401)

        # parts = auth.split()
        token_type = request.GET.get('token_type', 'WTF')
        print("token_type:", token_type)
        if token_type.lower() != "bearer":
            return JsonResponse(data={"code": "invalid_header",
                                      "description":
                                          "Authorization header must start with"
                                          "Bearer"}, status=401)
        # elif len(parts) == 1:
        #     return JsonResponse(data={"code": "invalid_header",
        #                               "description": "Token not found"}, status=401)
        # elif len(parts) > 2:
        #     return JsonResponse(data={"code": "invalid_header",
        #                               "description": "Authorization header must be"
        #                                              "Bearer token"}, status=401)

        # token = parts[1]
        token = request.GET.get('access_token', '')
        # VALIDATE TOKEN

        jwks = AUTH0_PUBLIC_KEY
        try:
            unverified_header = jwt.get_unverified_header(token)
        except jwt.JWTError:

            return JsonResponse(data={"code": "invalid_header",
                                      "description": "Invalid header. "
                                                     "Use an RS256 signed JWT Access Token"}, status=401)

        if unverified_header["alg"] == "HS256":
            return JsonResponse(data={"code": "invalid_header",
                                      "description": "Invalid header. "
                                                     "Use an RS256 signed JWT Access Token"}, status=401)

        rsa_key = {}
        print("jwks")
        print("jwks")
        print("jwks")
        print("jwks")
        print("jwks")
        # print(jwks)
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                print('token:', token)
                print('rsa_key:', rsa_key)
                print('ALGORITHMS:', ALGORITHMS)
                print('API_AUDIENCE:', API_AUDIENCE)
                print('AUTH0_DOMAIN:', "https://" + AUTH0_DOMAIN + "/")
                jwt.decode(
                    token,
                    key=rsa_key,
                    # key=CLIENT_SECRET,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://" + AUTH0_DOMAIN + "/",

                )

            except jwt.ExpiredSignatureError:
                return JsonResponse(data={"code": "token_expired",
                                          "description": "token is expired"}, status=401)
            except jwt.JWTClaimsError:
                return JsonResponse(data={"code": "invalid_claims",
                                          "description": "incorrect claims,"
                                                         " please check the audience and issuer"}, status=401)
            except Exception:
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Unable to parse authentication"
                                                         " token."}, status=400)
            else:
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Unable to find appropriate key"}, status=401)

        response = self.get_response(request)
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        print('RES[PONSE:')
        # print('RES[PONSE:', response)
        # return response
