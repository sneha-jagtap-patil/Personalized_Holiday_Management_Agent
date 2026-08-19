from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import team
import asyncio
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


async def main():
    print("1. Main started")

    task = TextMessage(
        content="I want to plan a trip to Paris for 5 days. Can you help me with that?",
        source="user"
    )

    print("2. Sending task to team...")

    response = await team.run(task=task)

    print("3. Team response received")

    for message in response.messages:
        line = f"{message.source}: {message.content}"
        try:
            print(line)
        except UnicodeEncodeError:
            encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
            print(line.encode(encoding, errors="replace").decode(encoding, errors="replace"))


if __name__ == "__main__":
    asyncio.run(main())
