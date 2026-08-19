from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

researcher_agent = AssistantAgent(
    name="Holiday_Researcher",
    description="a holiday Researcher agent that helps users plan thier trip",
    model_client=model_client,
    system_message="you are a travel holiday Researcher agent"
)
