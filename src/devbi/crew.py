import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Configuração das variáveis de ambiente
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
os.environ["OPENAI_API_KEY"] = "NA"

# Configuração do LLM
llm = ChatOpenAI(
    model="crewai-llama2",
    base_url="http://localhost:11434/v1"
)

# Definição do Agente e Tarefas
general_agent = Agent(
    role="Science Educator",
    goal="Educate people on the importance and benefits of water.",
    backstory="You are a passionate science educator who loves to share knowledge about the vital role of water in human life.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

task = Task(
    description="Write a detailed report on the benefits of water for humanity, focusing on health, environment, and daily life. Format the report in Markdown.",
    agent=general_agent,
    expected_output="A Markdown file with a detailed report on the benefits of water.",
    output_file='benefits_of_water.md'
)

crew = Crew(
    agents=[general_agent],
    tasks=[task],
    verbose=2
)

def kickoff():
    result = crew.kickoff()
    print(result)
