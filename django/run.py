import streamlit as st
import streamlit_authenticator as stauth
import requests

# Configure the authenticator
# https://github.com/mkhorasani/Streamlit-Authenticator
# https://www.youtube.com/watch?v=8X1OidYYVQw
config = {
    'credentials': {
        'usernames': {}
    },
    'cookie': {
        'expiry_days': 1,
        'key': 'some_signature_key',
        'name': 'streamlit-auth'
    },
    'preauthorized': {
        'emails': []
    }
}

# This should ideally be a secure endpoint with token authentication
def get_django_users():
    response = requests.get('http://127.0.0.1:8000/api/get_users/')
    if response.status_code == 200:
        return response.json()
    return {}


def authenticate(username, password):
    response = requests.post(
        'http://127.0.0.1:8000/api/authenticate/',
        data = {
            'username': username,
            'password': password
        }
    )
    return response.json()


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

## https://stackoverflow.com/questions/78016150/streamlit-authenticate-login-giving-error
# name, authentication_status, username = authenticator.login('Login', 'main')
name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'Login'})
users = get_django_users()
config['credentials']['usernames'] = users

if authentication_status:
    st.write(f'Welcome {name}')
    authenticator.logout('Logout', 'sidebar')
    st.write('Your Streamlit app content goes here.')

elif authentication_status == False:
    st.error('Username or password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')
