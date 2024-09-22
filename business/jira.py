from jira import JIRA
from config import jira_config
import logging

logger = logging.getLogger(__name__)
JIRA_URL = jira_config['JIRA_URL']
USERNAME = jira_config['USERNAME']
API_TOKEN = jira_config['API_TOKEN']
jira = JIRA(server=JIRA_URL, basic_auth=(USERNAME, API_TOKEN))

class JIRA():
    def get_tickets(story_id):
        logger.info("Getting tickets...")
        story = jira.issue(story_id)
    
        story_data = {
            "story_id": story.key,
            "story_title": story.fields.summary,
            "tasks": []
        }
        jql_query = f'parent = {story_id} AND issuetype = "subtask"'
        tasks = jira.search_issues(jql_query)
        
        for task in tasks:
            task_data = {
                "task_id": task.key,
                "task_title": task.fields.summary,
                "task_description": task.fields.description if task.fields.description else "No description",
                "task_assignee": task.fields.assignee.emailAddress if task.fields.assignee else "Unassigned",
                "task_status": task.fields.status.name
            }
            
            story_data["tasks"].append(task_data)
        logger.info("Finished getting tickets...")
        return story_data
    
    def attach_test_case_to_issue(issue_id, file_path):
        with open(file_path, 'rb') as file:
            jira.add_attachment(issue=issue_id, attachment=file)
            print(f"File {file_path} attached to issue {issue_id}") 
        return True   
    
    def assign_bug_to_developer(bug, user_email):
        user = jira.search_users(query=user_email)
        account_id = user[0].accountId
        issue_dict = {
            'project': {'key': bug['ticket_id'].split('-')[0]},   
            'summary': bug['summary'], 
            'description': bug['description'],
            'issuetype': {'name': 'Bug'},  
            'assignee': {'accountId': account_id}
        }
        new_issue = jira.create_issue(fields=issue_dict)
        print(f"Created sub-task {new_issue.key} under {bug['ticket_id']} and assigned it to {user_email}.")