from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

def get_credentials():
    SCOPE = ["https://www.googleapis.com/auth/calendar.readonly","https://www.googleapis.com/auth/gmail.readonly"]
    flow =InstalledAppFlow.from_client_secrets_file("client_secret.json",scopes=SCOPE)
    credentials = flow.run_console()
    pickle.dump(credentials,open('token.pkl',"wb"))
    
