
# RUN ON AGENTVERSE
# GRADE SUBMISSION AGENT IN CHARGE OF SENDING ALL PROCESSED DATA (GRADES) TO LOCAL AGENT FOR SAVE TO DB

from uagents import Model
from typing import List
import json
import requests
from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low

LOCAL_AGENT_ADDRESS='agent1qvrynkgrn2fkqthehxjw67l698hduzxuede8sfpspfwj60zl0l9lq34fw09'

SUBMISSION_SEED = "submission really secret phrase"

submission_agent_client = Agent(
    name="submission_agent",
    port=8006,
    seed=SUBMISSION_SEED,
    endpoint=["http://127.0.0.1:8006/submit"]
)


class Data(Model):
    value: float
    timestamp: str
    confidence: float
    details: str
    notes: str

class DataAll(Model):
    grades: List[Data]



# Message handler for data requests sent to this agent
@submission_agent_client.on_message(model=DataAll)
async def handle_data(ctx: Context, sender: str, data: DataAll):
    ctx.logger.info(f"Got response from AI model agent: {data}")
    print("Sender: " + sender)
    await ctx.send(LOCAL_AGENT_ADDRESS, data)

    
if __name__ == "__main__":
    print(submission_agent_client.address)
    submission_agent_client.run()        