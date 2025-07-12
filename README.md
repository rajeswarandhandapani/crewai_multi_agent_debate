# CrewaiMultiAgentDebate Crew

Welcome to the CrewaiMultiAgentDebate Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/crewai_multi_agent_debate/config/agents.yaml` to define your agents
- Modify `src/crewai_multi_agent_debate/config/tasks.yaml` to define your tasks
- Modify `src/crewai_multi_agent_debate/crew.py` to add your own logic, tools and specific args
- Modify `src/crewai_multi_agent_debate/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the crewai-multi-agent-debate Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The crewai-multi-agent-debate Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Supported LLMs

This project demonstrates multi-agent debate using several different Large Language Models (LLMs). Each agent can be configured to use a different LLM, allowing for diverse perspectives and capabilities. The following LLMs are used by default (see `src/crewai_multi_agent_debate/config/agents.yaml`):

- **Anthropic Claude 3.5 Haiku** (`anthropic/claude-3-5-haiku-latest`): Used by the proposer agent to generate arguments in favor of the motion.
- **OpenAI GPT-4.1 Mini** (`openai/gpt-4.1-mini-2025-04-14`): Used by the opposer agent to generate arguments against the motion.
- **Google Gemini 2.5 Flash** (`gemini/gemini-2.5-flash`): Used by the judge agent to evaluate arguments and decide the winner.

You can customize which LLM each agent uses by editing the `llm` field in the agents configuration file.

