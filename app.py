from turtle import title

from certifi import contents

from fastapi import FastAPI , HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import team

class PlanRequest(BaseModel):
    content: str
    source: str = "user"

    app = FastAPI(title="HOliday Planner API")



    