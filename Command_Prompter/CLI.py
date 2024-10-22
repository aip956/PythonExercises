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

def main():
    while True:
        # Step 1: Get user input
        user_input = prompt("Describe what you wan to do: ")

        # Step 2: Generate a command from the user input
        suggested_command = generate_command_from_llama(user_input)

        # Step 3: Provide shadow typing with confirmation; check if safe
        if safe_command_check(suggested_command):
            completer = WordCompleter([suggested_command], ignore_case=True)
            selected_command = prompt("Suggested Command: ", completer=completer, complete_while_typing = True)


            # Execute the selected command or let user modify
            if selected_command == suggested_command:
                output = subprocess.run(selected_command, shell=True, capture_output=True, text=True)
                print(output.stdout)
            else:
                print(f"Modified command: {selected_command}")
        else:
            print("Command is not safe. Please review before executing.")

if __name__ == "__main__":
    main()

    