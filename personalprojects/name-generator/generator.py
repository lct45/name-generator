import requests
from lxml import html

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"
LOGIN_URL = "https://ident.familysearch.org/cis-web/oauth2/v3/authorization?client_secret=qgyA0c1Q4s%2FFjVlEFu5K5yjq2vlXsD6lc40vIN1RS8O%2BtB7ymm%2Fhu0k0iMMTaHKYkbOuZqgn32UOnBpxYJA8wn0hguF6AuoqMsoXlFdtnhqDGWsS4t23UN0yp0cxVO5sMLL8Vg5dyaK0c2y9COCzQnSB0U2aLmIRqkdUZYxoAEI7lELOJ1wPPh9zMcxJfsuy9UAewy4TAm1lj%2BUACztlWuMht%2BVKNU5gKE53jNaevBKZTY9%2B%2FRHW6ypIvS3Fp%2BID67E6mzkugRU5NIrAEV4v%2FLU8DXC5%2FxP0Vmc37VZNnWGomLQOBdfEuBij9Yo6xHinIHjgqGQ%2Fcd%2BkQwWWI%2BPOhg%3D%3D&response_type=code&redirect_uri=https%3A%2F%2Fwww.familysearch.org%2Fauth%2Ffamilysearch%2Fcallback&state=%2F&client_id=3Z3L-Z4GK-J7ZS-YT3Z-Q4KY-YN66-ZX5K-176R"

def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='params']/@value")))[0]
    payload = {
    "userName": USERNAME,
    "password": PASSWORD,
    "params": authenticity_token
    }
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    print(result.status_code)

    





if __name__ == '__main__':
    main()