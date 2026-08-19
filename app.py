from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import create_team


class PlanRequest(BaseModel):
    content: str
    source: str = "User"


app = FastAPI(title="Holiday Management API")


# Serve static files from ./static
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# Generate holiday management plan
@app.post("/plan")
async def plan(req: PlanRequest):
    print("\n========== /PLAN CALLED ==========")
    print("Request:", req)

    try:
        # Create a NEW team for every request
        team = create_team()
        print("1. New team created")

        task = TextMessage(
            content=req.content,
            source=req.source
        )

        print("2. TextMessage created")

        result = await team.run(task=task)

        print("3. Team run completed")

        messages = [
            {
                "source": m.source,
                "content": m.content
            }
            for m in result.messages
            if hasattr(m, "content")
        ]

        print("4. Messages created")

        return {"messages": messages}

    except Exception as e:
        import traceback

        print("\n========== ACTUAL ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        traceback.print_exc()
        print("==================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
# Run application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )