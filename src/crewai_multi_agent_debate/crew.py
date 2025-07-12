from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CrewaiMultiAgentDebate():
    """CrewaiMultiAgentDebate crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'],
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True
        )

    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'],
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'],
            output_file='report.md'
        )
    
    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiMultiAgentDebate crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
