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


URL_BASE='https://api.github.com/'
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

print(user.get('avatar_url'))