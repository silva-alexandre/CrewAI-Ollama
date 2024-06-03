#!/usr/bin/env python
from devbi.crew import DevbiCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    DevbiCrew().crew().kickoff(inputs=inputs)