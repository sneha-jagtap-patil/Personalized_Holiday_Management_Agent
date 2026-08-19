from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client


planner_agent = AssistantAgent(
    name="Holiday_Planner",
    description="A holiday planner agent that helps users plan their trip.",
    model_client=model_client,
    system_message="""
You are a professional travel holiday planner.

Create a practical and personalized holiday itinerary based on the user's request.

Do not use the word "TERMINATE" unless you are explicitly ending the conversation.
When your work is complete, end your response with:
TERMINATE
"""
)