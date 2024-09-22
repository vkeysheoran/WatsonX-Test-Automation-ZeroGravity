from config import ibm_config
from utils.system import System
import requests
import logging

logger = logging.getLogger(__name__)

class WatsonX():
    def get_promt_result(task_data):
        logger.info("Getting promt result...")
        GENERATION_ENDPOINT_URL = ibm_config['GENERATION_ENDPOINT_URL']
        logger.info("Getting ibm cloud access token...")
        ibm_cloud_token = System.get_ibm_cloud_token()
        logger.info("Finished getting ibm cloud access token...")
        body=  {
                "input": task_data['promt'],
                "parameters": task_data['parameters'],
                "model_id": task_data['ai_model_id'] ,
                "project_id": ibm_config["IBM_CLOUD_PROECT_ID"]
            }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ibm_cloud_token}"
        }
        
        try:
            response = requests.post(
                GENERATION_ENDPOINT_URL,
                headers=headers,
                json=body
            )       
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return False
        
        
    
       