import requests
import json
from config import ibm_config

class System:
    def __init__(self):
        self.value = 0
    
    def get_ibm_cloud_token():
        IBM_TOKEN_URL = ibm_config['IBM_TOKEN_URL']
        IBM_CLOUD_API_KEY = ibm_config['IBM_CLOUD_API_KEY']

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
            'apikey': IBM_CLOUD_API_KEY
        }

        response = requests.post(IBM_TOKEN_URL, headers=headers, data=data)

        if response.status_code == 200:
            token_data = response.json()    
        else:
            return False
        
        return token_data['access_token']  
    
    def get_url_html(url):
        response = requests.get(url)
        html_content = response.text
        return html_content
    
    def get_substring_between(s, start_char, end_char):
        try:
            start_index = s.index(start_char) + len(start_char)
            end_index = s.index(end_char, start_index)
            
            return s[start_index:end_index]
        except ValueError:
            return ""
        
    
    

            