from business.automation import Automation
from business.jira import JIRA
from business.watsonx import WatsonX
from business.test_write import TestWrite
from utils.system import System
import json
import subprocess

automation = Automation
jira = JIRA
class AutomationService:
    def __init__(self):
        self.value = 0
    def automate_test_cases(self, data:dict):
        story_id = data['story_id']
        tickets = self.get_jira_tickets(story_id)
        for ticket in tickets['tasks']:
            if ticket['task_status'] == 'Done':
                path = System.get_substring_between(ticket['task_description'],"~","~")
                print(path)
                if path != "": 
                    cleaned_str = path.replace('“', '"').replace('”', '"')
                    cleaned_str = cleaned_str.replace('[', '{').replace(']', '}')            
                    data_dict = json.loads(cleaned_str)
                    html_content = System.get_url_html(data_dict['URL'])
                else: 
                    data_dict = ""
                    html_content = ""
                print("Generating test cases with the help of GEN-AI ...")
                input_promt = f"<s>[INST] You are Mixtral Chat, an AI language model developed by Mistral AI. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior. [INST]</s> [INST]write a standalone python script for mac using only pip unittest, selenium version 4.25.0 , NoSuchElementException libraries with functions like self.driver.find_element('name', 'username'),self.driver.find_element('xpath', '//a[text()='Sign Up']') which doesnot halt on assertion failure . it should run all assertions and provide final result with test names. it should also include cases where provide invalid input and test for bugs . cover all the validations as per following task description: {ticket['task_description']}.html of the page is :{html_content}  Response should have only the syntax error free code, explanation is not required. correct the following code for syntax errors, depricated statements, missing dependencies etc. code should work with selenium version 4.25.0 . setup function should look like def setUp(self):\nself.driver = webdriver.Chrome()\n self.driver.get(). it should use self.driver.find_element() function to locate the elements .  [INST]</s> \n"
                task_data = {
                    "promt": f""" { input_promt } """,
                    "parameters" : {
                        "decoding_method": "greedy",
                        "max_new_tokens": 4000,
                        "min_new_tokens": 0,
                        "stop_sequences": [],
                        "repetition_penalty": 1.02
                    },
                    "ai_model_id":"mistralai/mistral-large"
                }
                raw_code = self.get_promt_reult(task_data)
                generated_text = raw_code['results'][0]['generated_text']
                
                automation_code = System.get_substring_between(generated_text,'```python','```')
                file_path = TestWrite.write_file(automation_code, ticket['task_title'], story_id)
                self.attach_test_case_to_issue(ticket['task_id'],file_path)
                print("Test cases prepared , executing test results ...")
                result = subprocess.run(f"python3 -m unittest {file_path}",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                output = result.stdout
                error = result.stderr
                if('Assertion failed' in output):
                    print("Found bugs , assigning to user ...")
                    bug = {
                        'summary': f'Found Bugs in {story_id} >> {ticket['task_id']}, Please check failed cases', 
                        'ticket_id': ticket['task_id'],
                        'description': output, 
                    }
                    self.assign_bug_to_developer(bug, ticket['task_assignee'])
               
                print("Output:", output)
                if error:
                    print("Error:", error)
               
        return True
    
    
    def get_jira_tickets(self, story_id):    
        return jira.get_tickets(story_id)
    
    def attach_test_case_to_issue(self,issue_id, file_path):
        return jira.attach_test_case_to_issue(issue_id, file_path)
    
    def get_promt_reult(self,task_data):
        return WatsonX.get_promt_result(task_data)
    
    def assign_bug_to_developer(self, bug, user_email):
        return jira.assign_bug_to_developer(bug, user_email)
           
automation_service = AutomationService()