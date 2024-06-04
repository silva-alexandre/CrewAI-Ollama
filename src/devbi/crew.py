import os
from crewai import Agent, Task, Crew

# Importando a ferramenta personalizada
from src.devbi.tools.custom_tool import LocalLLMTool

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

# Função para iniciar a equipe
def kickoff():
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    kickoff()
