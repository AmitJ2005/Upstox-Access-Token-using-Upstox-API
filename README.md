GET Access Token using Upstox-API
=================================

The purpose of this tool is to help users quickly generate an access token for Upstox's API v2. It uses Streamlit for the front-end UI and allows you to input your client credentials, authorize your application, and retrieve the access token in a few simple steps.

Prerequisites
-------------

Before using this application, you need to have the following Steps:

1.  **Set-up Upstox API:**
    
    Go to the Upstox.com after log-in navigate to **My Account > Apps** to [create a new app](https://account.upstox.com/developer/apps/createapp).
    
    *   **Client ID** (Example: `e123456b-f123-4384-3caa-00eb0a1ebb2b`)
    *   **Client Secret** (Example: `b12345sdvk`)
    *   **Redirect URI** (Example: `https://127.0.0.1:5000/`)
    
    **Note:** The `Redirect URI` should be match the URI registered with Upstox.
    
    For more information, refer to the [Upstox Documentation](https://upstox.com/developer/api-documentation/open-api).
    

Setup and Running the Application
---------------------------------

1.  **Clone the Repository:**
    
        git clone https://github.com/AmitJ2005/Upstox-Access-Token-using-Upstox-API.git
    
2.  **Navigate into the Project Directory:**
    
        cd Upstox-Access-Token-using-Upstox-API

3.  **Install Required Libraries:**
    
    You will need to install the required libraries. You can do this by running in command prompt:
    
        pip install streamlit requests
    
4.  **Run the Application:**
    
    Use Streamlit to launch the app:
    
        streamlit run app.py
    
    This will start a local server.
    

Usage Guide
-----------

1.  **Step 1: Enter Your API Credentials**
    
    Input your **Client ID**, **Client Secret**, and **Redirect URI** obtained from Upstox.
    
2.  **Step 2: Generate Authorization URL**
    
    Once you have entered the credentials, the app will generate an authorization URL. Click on the generated URL to go to the Upstox login page and authorize the app.
    
3.  **Step 3: Retrieve Authorization Code**
    
    After logging in and authorizing, you will be redirected to your specified `Redirect URI` along with an authorization code (Example: `yKdxp8` ) in the URL. Copy this authorization code from the URL.
    
4.  **Step 4: Get Access Token**
    
    Paste the copied authorization code into the **Authorization Code** input box and click on **Get Access Token**. If everything is correct, your access token will be displayed.
    

Important Notes
---------------

*   **Keep your API credentials secure** and do not share them publicly.
*   This application only retrieves the access token and does not handle further API requests or trading functionalities.
*   Make sure your `Redirect URI` matches exactly with the one registered in the Upstox developer console, including the trailing `/`.


Contact
-------

If you have any questions or run into any issues, feel free to reach out!

*   Email: [amitjaiswal369143@gmail.com](mailto:amitjaisawal0123@gmail.com)
*   LinkedIn: [Amit Jaiswal](https://www.linkedin.com/in/amitjaiswal369143)
