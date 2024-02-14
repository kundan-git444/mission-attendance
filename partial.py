import requests
from bs4 import BeautifulSoup

login_url = 'https://samvidha.iare.ac.in'
username = '20951a1234'
password = 'kundansai1212'

session = requests.Session()

# Send a POST request to login
login_response = session.post(login_url, data={'txt_uname': username, 'txt_pwd': password})

# Check if login was successful
if login_response.status_code == 200:
    # Send a GET request to the biometric section
    biometric_url = 'https://samvidha.iare.ac.in/home?action=std_bio'
    biometric_response = session.get(biometric_url)
    print(biometric_response.text)
    # Parse the HTML response
    soup = BeautifulSoup(biometric_response.text, 'html.parser')
    # Now you can extract and process the required information from the biometric page
else:
    print("Login failed.")
