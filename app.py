from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool

from Gradio_UI import GradioUI

@tool
def my_custom_tool(arg1:str, arg2:int)-> str: #it's import to specify the return type
    """A tool that fetches the important events according to the given location and year.
    Args:
        arg1: A string that representing a valid city.
        arg2: An integer that respresenting a year.
        
    """
    query = "important events in 2023"
    results = ddg_answers(query)
    limited_results = results[:3]  

    # Return only the 3 most important events
    return f"The top 3 events in {arg1} for {arg2} are:\n" + "\n".join(limited_results)

final_answer = FinalAnswerTool()

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='https://.us-east-1.aws.endpoints.huggingface.cloud',
custom_role_conversions=None,
)


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
agent = CodeAgent(
    model=model,
    tools=[final_answer, my_custom_tool, get_current_time_in_timezone],
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()