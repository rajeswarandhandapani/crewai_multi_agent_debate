#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_multi_agent_debate.crew import CrewaiMultiAgentDebate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'Fidelity Go is a good investment',
        'current_year': str(datetime.now().year)
    }
    
    try:
        debate_result = CrewaiMultiAgentDebate().crew().kickoff(inputs=inputs)
        print("Debate Result:")
        print(debate_result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
