import requests

""" # CONSTANTS
URL_BASE='https://api.github.com/'
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    return None
username = input('Give the username:\t')
get_github_user(username) """

""" 
# CONSTANTS
URL_BASE='https://api.github.com/'
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
username = input('Give the username:\t')
user = get_github_user(username)


print(user) """


# CONSTANTS
""" URL_BASE='https://api.github.com/'
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
username = input('Give the username:\t')
user = get_github_user(username)
print(user.get('avatar_url')) """


""" URL_BASE='https://api.github.com/'
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


username = input('Give the username:\t')
user = get_github_user(username)

if user:
    user_avatar_url = user.get('avatar_url')
    print(user_avatar_url)
else: 
    "no encontrado"

print(user.get('avatar_url')) """
# CONSTANTS
URL_BASE = 'https://api.github.com/'

def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def download_user_avatar(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        response_content = response.content
        filename = 'tmp/useravatar.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

username = input('Give the user name:\t')
user = get_github_user(username)

if user:
    user_avatar_url = user.get('avatar_url')
    download_user_avatar(user_avatar_url)
else:
    print('User not found')