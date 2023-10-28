import os

import supervisely as sly

from dotenv import load_dotenv

if sly.is_development():
    # * For convinient development, has no effect in the production.
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


# * Creating an instance of the supervisely API according to the environment variables.
api: sly.Api = sly.Api.from_env()


# * To avoid global variables in different modules, it's better to use g.STATE (g.AppState) object
# * across the app. It can be accessed from any module by importing globals module.
class State:
    def __init__(self):
        # * This class should contain all the variables that are used across the app.
        # * For example selected team, workspace, project, dataset, etc.
        self.selected_team = sly.io.env.team_id()
        self.selected_workspace = sly.io.env.workspace_id()


# * Class object to access from other modules.
# * import src.globals as g
# * selected_team = g.STATE.selected_team
STATE = State()
