


def search(parameters, name):
        return next((parameters[key] for key in parameters.keys() if name in key), None)
        
class Automation():     
    def get_jira_tickets( event_body):
        response = event_body
        return response
    
    