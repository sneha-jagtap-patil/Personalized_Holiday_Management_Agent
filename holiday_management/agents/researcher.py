from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client


researcher_agent = AssistantAgent(
    name="Holiday_Researcher",
    description="A holiday researcher agent that helps users research and improve their trip plan.",
    model_client=model_client,
    system_message="""
You are a professional travel researcher.

Review the holiday request and provide useful travel information,
suggestions, logistics, attractions, and practical improvements.

Do not use the word "TERMINATE" unless you are explicitly ending the conversation.
When your work is complete, end your response with:
TERMINATE
"""
)