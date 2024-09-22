from fastapi import APIRouter
from services.automation_service import automation_service

router = APIRouter()

@router.post("/get_jira_tickets/")
async def automate_test_cases(data:dict):
            return automation_service.automate_test_cases(data)
            


            
            
            
            

            