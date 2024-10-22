import subprocess
from transformers import pipeline
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Load the llama model
nlp_model = pipeline("text-generation", model="gpt2")

# A dictionary mapping intents to commands  
commands = {
    "find a file": "find . -name '*.txt'",
    "list files": "ls -la",
    "show disk usage": "du -sh *",
}

def generate_command_from_llama(user_input):
    prompt_text = f"User: {user_input}\nLlama: "
    result = nlp_model(prompt_text)
    return result[0]["generated_text"]

def safe_command_check(command):
    """Basic check to ensure that the command is safe"""
    dangerous_commands = ["rm -rf", "dd if=", "del", ":(){ :|:& };:", "format"]    
    for danger in dangerous_commands:
        if danger in command:
            return False
    return True

