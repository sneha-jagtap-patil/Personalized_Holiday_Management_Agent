from autogen_agentchat.teams import RoundRobinGroupChat

from holiday_management.agents.planner import planner_agent
from holiday_management.agents.researcher import researcher_agent
from holiday_management.utils.utils import get_termination_condition


def create_team():
    team = RoundRobinGroupChat(
        participants=[
            planner_agent,
            researcher_agent
        ],
        termination_condition=get_termination_condition(),
        max_turns=2
    )

    return team