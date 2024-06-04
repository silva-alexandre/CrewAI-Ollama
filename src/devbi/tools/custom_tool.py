from crewai_tools import BaseTool
import subprocess

class LocalLLMTool(BaseTool):
    name: str = "local_llm_tool"
    description: str = "Tool to interact with the local Ollama Openhermes model."

    def _run(self, prompt: str) -> str:
        result = subprocess.run(['ollama', 'run', 'openhermes', '-p', prompt], capture_output=True, text=True)
        return result.stdout.strip()
