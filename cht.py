import requests
from bs4 import BeautifulSoup

# Login endpoint and credentials
login_url = 'https://samvidha.iare.ac.in'
username = '20951a1234'
password = 'kundansai1212'

# Create a session to persist the cookie
session = requests.Session()

# Send a POST request to login
login_response = session.post(login_url, data={'txt_uname': username, 'txt_pwd': password})
print(login_response.text)
# Check if login was successful
if "Dashboard" in login_response.text:
    # Send a GET request to the biometric section
    biometric_url = 'https://samvidha.iare.ac.in/home?action=std_bio'
    biometric_response = session.get(biometric_url)
    print(biometric_response.text)
    # Parse the HTML response
    soup = BeautifulSoup(biometric_response.text, 'html.parser')
    absents = soup.select('table#dataTable tbody tr td:nth-child(3):contains("Absent")')
    
    # Count the number of absents
    num_absents = len(absents)
    
    print(f"Number of absents: {num_absents}")
else:
    print("Login failed.")
