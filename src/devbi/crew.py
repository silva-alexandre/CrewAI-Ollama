import os
from crewai import Agent, Task, Crew, Process
from src.devbi.tools.custom_tool import LocalLLMTool

# Ferramentas
local_llm_tool = LocalLLMTool()

# Configurar agentes e tarefas aqui se necessário
# (Ou eles serão carregados dos arquivos YAML)

# Função para iniciar a equipe
def kickoff():
    researcher = Agent(
        role='Senior Researcher',
        goal='Uncover groundbreaking technologies in {topic}',
        verbose=True,
        memory=True,
        backstory="Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world.",
        tools=[local_llm_tool],
        allow_delegation=True
    )

    writer = Agent(
        role='Writer',
        goal='Narrate compelling tech stories about {topic}',
        verbose=True,
        memory=True,
        backstory="With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.",
        tools=[local_llm_tool],
        allow_delegation=False
    )

    research_task = Task(
        description="Identify the next big trend in {topic}. Focus on identifying pros and cons and the overall narrative. Your final report should clearly articulate the key points, its market opportunities, and potential risks.",
        expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
        tools=[local_llm_tool],
        agent=researcher,
    )

    write_task = Task(
        description="Compose an insightful article on {topic}. Focus on the latest trends and how it's impacting the industry. This article should be easy to understand, engaging, and positive.",
        expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
        tools=[local_llm_tool],
        agent=writer,
        async_execution=False,
        output_file='new-blog-post.md'
    )

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    print(result)

if __name__ == "__main__":
    kickoff()
