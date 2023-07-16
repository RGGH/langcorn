from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# Set up the turbo LLM
turbo_llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

from langchain.tools import DuckDuckGoSearchRun

# from langchain.tools import DuckDuckGoSearchTool
from langchain.agents import Tool
from langchain.tools import BaseTool

search = DuckDuckGoSearchRun()


from langchain.chat_models import ChatOpenAI
from langchain.experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

search = DuckDuckGoSearchRun()

from langchain import LLMMathChain

llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)


tools = [
    Tool(
        func=llm_math_chain.run,
        name="Calculator",
        description="Useful for when you need to answer questions about math. This tool is only for calculating answers to numeric/math questions and nothing else. Only input math expressions.",
    ),
    # ),
    Tool(
        name="search",
        func=search.run,
        description="useful for when you need to answer questions about current events, dates, news. You should ask targeted questions",
    ),
]

model = ChatOpenAI(temperature=0)

planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)


if __name__ == "__main__":
    agent.run(
        input="Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
    )
