import openai
from textblob import TextBlob
from tkinter import *

# OpenAI API key
openai.api_key = "your_openai_api_key"

# Function to correct spelling using TextBlob and improve grammar using OpenAI GPT
def hybrid_correction():
    user_input = text.get().strip()  # Get the text entered by the user
    if not user_input:
        correctedText.set("Please enter a word or sentence!")
        return

    try:
        # Step 1: Use TextBlob for basic spelling correction
        text_blob_corrected = str(TextBlob(user_input).correct())

        # Step 2: Use OpenAI to refine grammar and context
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[{
                "role": "user",
                "content": f"Correct the grammar and improve the sentence: '{text_blob_corrected}'"
            }]
        )
        # Extract the refined text
        gpt_corrected = response['choices'][0]['message']['content']
        correctedText.set(f"Corrected Text: {gpt_corrected}")

    except Exception as e:
        correctedText.set(f"Error: {e}")

# Creating the main window
wn = Tk()
wn.title("Group 5 Spell & Grammar Checker")

# Set window size
win_width = 800
win_height = 500

# Get screen width and height
screen_width = wn.winfo_screenwidth()
screen_height = wn.winfo_screenheight()

# Calculate position for center alignment and move it down
x_position = (screen_width - win_width) // 2
y_position = (screen_height - win_height) // 2 + 100  # Added 100px to move it downward

# Set window size and position
wn.geometry(f"{win_width}x{win_height}+{x_position}+{y_position}")
wn.config(bg='SlateGray1')

# Creating the variables to get the word and set the correct word
text = StringVar(wn)
correctedText = StringVar(wn)

# Main Label
Label(wn, text='Group 5 Spell & Grammar Checker', bg='SlateGray1',
      fg='gray30', font=('Times', 20, 'bold')).pack(pady=10)

# Input Label
Label(wn, text='Please enter the text:', bg='SlateGray1',
      font=('calibre', 13, 'normal')).pack()

# **Bigger Input Box (5x the original size)**
entry_box = Entry(wn, textvariable=text, width=80, font=('calibre', 13, 'normal'), bd=5, relief=RIDGE)
entry_box.pack(pady=10, ipady=50)  # Increased ipady for height

# Button to perform the hybrid correction
Button(wn, text="Correct Text", bg='SlateGray4', font=('calibre', 13),
       command=hybrid_correction, width=15, height=2).pack(pady=10)

# Output Label
Label(wn, textvariable=correctedText, bg='SlateGray1',
      font=('calibre', 13, 'normal'), wraplength=700, justify="center").pack(pady=10)

# Run the application
wn.mainloop()
