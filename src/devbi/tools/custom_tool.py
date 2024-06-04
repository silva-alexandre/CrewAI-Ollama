from crewai_tools import BaseTool
import os
import requests

class LocalLLMTool(BaseTool):
    name: str = "local_llm_tool"
    description: str = "Tool to interact with the local Ollama Openhermes model."

    def _run(self, prompt: str) -> str:
        url = os.getenv("OPENAI_API_BASE")
        model = os.getenv("OPENAI_MODEL_NAME")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        }
        payload = {
            "model": model,
            "prompt": prompt
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json().get("choices", [{}])[0].get("text", "").strip()
