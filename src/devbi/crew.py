import os
from crewai import Agent, Task, Crew
from devbi.tools.custom_tool import LocalLLMTool

# Configuração das variáveis de ambiente
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
os.environ["OPENAI_API_KEY"] = "NA"

# Configuração da ferramenta
local_llm_tool = LocalLLMTool()

# Definição do Agente e Tarefas
general_agent = Agent(
    role = "Math Professor",
    goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
    backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
    allow_delegation = False,
    verbose = True,
    tools = [local_llm_tool]
)

task = Task(
    description = """What is 3 + 5?""",
    agent = general_agent,
    expected_output = "A numerical answer."
)

crew = Crew(
    agents = [general_agent],
    tasks = [task],
    verbose = 2
)

def kickoff():
    result = crew.kickoff()
    print(result)
