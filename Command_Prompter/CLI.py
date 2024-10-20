import subprocess
from transformers import pipeline
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Load the llama model
nlp_model = pipeline("text-generation", model="gpt2")

commands = {
    "find a file": "find . -name '*.txt'",
    "list files": "ls -la",
    "show disk usage": "du -sh *",
}