import HeyBuddy_v1.0 as voice_assistant
import tkinter as tk

def start_voice_assistant():
    # Call the necessary functions from your voice assistant script
    voice_assistant.initialize()  # Replace with your actual initialization code
    voice_assistant.run()         # Replace with the function that starts your voice assistant

def main():
    root = tk.Tk()
    root.title("HeyBuddy v1.0")

    # Call the start_voice_assistant function
    start_voice_assistant()

    root.mainloop()

if __name__ == "__main__":
    main()
