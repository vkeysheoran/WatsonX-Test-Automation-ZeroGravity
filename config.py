from dotenv import load_dotenv

load_dotenv()
env = 'qa'

jira_config = {
    "JIRA_URL" : "https://yourdomain.atlassian.net",
    "USERNAME" : "email@example.com",
    "API_TOKEN" : "JIRA_API_TOKEN"
}
ibm_config = {
    "GENERATION_ENDPOINT_URL"  : "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29",
    "IBM_CLOUD_API_KEY" : "YOUR_IBM_CLOUD_API_KEY",
    "IBM_TOKEN_URL" : "https://iam.cloud.ibm.com/identity/token",
    "IBM_CLOUD_PROECT_ID" :"YOUR_IBM_CLOUD_PROECT_ID"
}
    



