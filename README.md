# Group 5 Spell & Grammar Checker

This is a Python-based Spell & Grammar Checker that uses TextBlob for spell correction and OpenAI's GPT API for grammar improvement. The user enters a sentence, and the tool corrects spelling errors before refining grammar.

## Features
- Uses TextBlob to correct spelling mistakes.
- Uses OpenAI GPT-3.5-turbo to refine grammar and sentence structure.
- Built using Tkinter for a simple user interface.

## Prerequisites
Before running the program, make sure you have the following installed on your system:

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/)
- Ensure Python is added to your system PATH.
- To check if Python is installed, run:
  ```sh
  python --version
  ```

### 2. Install Required Libraries
Open a terminal or command prompt and install the required Python libraries using the following command:
```sh
pip install openai textblob tkinter
```
Please note, TextBlob requires the nltk dataset:
```sh
python -m textblob.download_corpora
```

## How to Run the Application

### 1. Clone or Download the Project
If you have Git installed, you can clone the project:
```sh
git clone https://github.com/your-repo/spell-grammar-checker.git
cd spell-grammar-checker
```
Otherwise, download the script manually and save it to a folder.

### 2. Open and Edit the Code
- Open the `spell_checker.py` file in any text editor (VS Code, PyCharm, or Notepad++).
- Replace `your_openai_api_key` with your actual OpenAI API key.

### 3. Run the Application
In the terminal or command prompt, navigate to the project folder and run:
```sh
python spell_checker.py
```
This will launch a Tkinter GUI where you can input text and get corrected output.

## Code Overview

### 1. Importing Required Libraries
The code imports:
- OpenAI (for AI-based grammar correction)
- TextBlob (for spell checking)
- Tkinter (for GUI creation)

### 2. Function for Correction
1. It first uses TextBlob to correct spelling errors.
2. The corrected text is sent to OpenAI GPT for grammatical refinement.
3. The final corrected output is displayed in the GUI.

### 3. Creating the GUI
- Tkinter is used to create a simple UI.
- The input box is enlarged to improve usability.
- The window is centered and positioned lower for better placement.
- A button triggers the text correction function.

## Expected Output
1. The application window opens.
2. The user enters a sentence with errors.
3. Clicking "Correct Text" processes the text.
4. Corrected text appears below the input box.

## Troubleshooting

### 1. OpenAI API Errors
- Ensure you have a valid API key from OpenAI.
- If you get an error like `Invalid API Key`, double-check your key.

### 2. Module Not Found Error
If you see an error like:
```sh
ModuleNotFoundError: No module named 'openai'
```
Install the missing module using:
```sh
pip install openai
```

### 3. TextBlob Errors
If TextBlob gives errors, try reinstalling it and downloading the dataset:
```sh
pip install --upgrade textblob
python -m textblob.download_corpora
```

## Author
**Group 5**
- **ADESIDA JOHN** [220210017]  
- **Ajayi Samuel .O** [220202044]  
- **Daniel Daniel Unekwu** [220210015]  
- **Ogunlaja Ayomikun Victor** [210202022]  
- **Ayanwola Rachel Omolabake** [210210002]  
- **Kehinde Favour** [210202016]  

**Course:** Artificial Intelligence  
**Supervisor:** Dr. Oladapo
