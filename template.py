import  os
from pathlib import Path
import logging  

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )

project_name = "holiday_management"


list_of_files = [
    #config
    f"{project_name}/config/settings.py",

    #agents
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/planner.py",
    f"{project_name}/agents/researcher.py",
    
    #teams  
    f"{project_name}/teams/__init__.py",
    f"{project_name}/teams/holiday_team.py",

    #utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",
    # f"{project_name}/utils/logging.py",
    # # Tests
    # f"{project_name}/tests/__init__.py",
    # f"{project_name}/tests/test_agents.py",

    # root files inside the projects folder
        "app.py",
        # f"{project_name}/requirements.txt",
        # f"{project_name}/.gitignore",
        # f"{project_name}/README.md"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is not empty. Skipping file creation.")