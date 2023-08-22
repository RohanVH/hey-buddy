import tkinter as tk
import subprocess
from tkinter import scrolledtext

def run_script():
    global input_text  # Declare input_text as a global variable

    script_path = "Software\heybuddy.py"  # Replace with the actual path to your script

   # Get the user input
    user_input = input_text.get("1.0", tk.END).strip()

    # Run the command using subprocess
    command = ["python", script_path] + user_input.split()
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output to the console
    print("Command:", " ".join(command))
    print("Output:", result.stdout)
    print("Error:", result.stderr)

    # Display the command and output in the console
    console_text.insert(tk.END, f"Input: {user_input}\n")
    console_text.insert(tk.END, result.stdout)
    console_text.insert(tk.END, result.stderr)

root = tk.Tk()
root.title("Script Runner")

# Load and set the logo (replace with your image file)
logo_image = tk.PhotoImage(file="Software\ytvoicesearch.png")
root.iconphoto(False, logo_image)

# Input area for user commands
input_text = scrolledtext.ScrolledText(root, height=3, width=50)
input_text.pack()

run_button = tk.Button(root, text="Run Command", command=run_script)
run_button.pack()

# Console area to display command input and outputs
console_text = scrolledtext.ScrolledText(root, height=10, width=50)
console_text.pack()

root.mainloop()
