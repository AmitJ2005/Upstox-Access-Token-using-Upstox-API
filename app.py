import streamlit as st
import requests

# Streamlit UI
st.title("Upstox API Authorization")
st.write("## Step 1: Enter Your API Credentials")

# Input fields for API credentials
client_id = st.text_input("Client ID", "")
client_secret = st.text_input("Client Secret", "")
redirect_uri = st.text_input("Redirect URI", "")

# Check if all credentials are provided
if client_id and client_secret and redirect_uri:
    st.write("## Step 2: Generate the Authorization URL")

    # Generate the authorization URL
    authorization_url = f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    st.write("Please go to the following URL and log in to get the authorization code:")
    st.write(authorization_url)
    
    # Input box for authorization code
    st.write("## Step 3: Enter the Authorization Code")
    auth_code = st.text_input("Authorization Code", "")
    
    # When the user inputs the authorization code, request for access token
    if st.button("Get Access Token"):
        if auth_code:
            # URL for generating access token (Upstox API v2 endpoint)
            url = 'https://api-v2.upstox.com/login/authorization/token'
            
            # Updated headers (with Api-Version for v2)
            headers = {
                'accept': 'application/json',
                'Api-Version': '2.0',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            # Request payload (data parameters)
            data = {
                'code': auth_code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            }
            
            # Make the POST request to get the access token
            response = requests.post(url, headers=headers, data=data)
            
            # Step 4: Parse the JSON response and store the access token
            if response.status_code == 200:
                json_response = response.json()
                access_token = json_response.get('access_token', None)
                
                if access_token:
                    st.write("## Step 4: Access Token Retrieved Successfully!")
                    st.success(f"Access Token: {access_token}")
                else:
                    st.error("Failed to retrieve the access token. Please check your inputs.")
            else:
                st.error(f"Failed to generate access token: {response.status_code} {response.text}")
        else:
            st.warning("Please enter the authorization code first.")
else:
    st.warning("Please enter your API credentials first.")
