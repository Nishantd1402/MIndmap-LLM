import subprocess
import os

# Define the bash commands to install and use nvm, npm, and npx
# Define the command as a string


commands = """
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.nvm/nvm.sh  # Load nvm into the current shell session
nvm install node   # Install Node.js version 14.17.1
npm install -g markmap-cli
"""

# Execute the commands using subprocess
result = subprocess.run(commands, shell=True, executable='/bin/bash')


import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit.components.v1 as components

import os
from groq import Groq

client = Groq(
    api_key="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"
)


chapter_name = {
    '1 - Observing the Armies on the Battlefield of Kurukṣetra': 1,
    '2 - Contents of the Gītā Summarized': 2,
    '3 - Karma Yoga': 3,
    '4 - Transcendental Knowledge': 4,
    '5 - Karma-yoga – Action in Kṛṣṇa Consciousness': 5,
    '6 - Dhyāna-yoga': 6,
    '7 - Knowledge of the Absolute': 7,
    '8 - Attaining the Supreme': 8,
    '9 - The Most Confidential Knowledge': 9,
    '10 - Opulence of the Absolute': 10,
    '11 - The Universal Form': 11,
    '12 - Devotional Service': 12,
    '13 - Nature, the Enjoyer and Consciousness': 13,
    '14 - The Three Modes of Material Nature': 14,
    '15 - The Yoga of the Supreme Person': 15,
    '16 - The Divine and Demoniac Natures': 16,
    '17 - The Divisions of Faith': 17,
    '18 - Conclusion – The Perfection of Renunciation': 18
}


chapter_verse_dict = {1: ('1', '10', '11', '12', '13', '14', '15', '16-18', '19', '2', '20', '21-22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32-35', '36', '37-38', '39', '4', '40', '41', '42', '43', '44', '45', '46', '5', '6', '7', '8', '9'), 10: ('1', '10', '11', '12-13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4-5', '40', '41', '42', '6', '7', '8', '9'), 11: ('1', '10-11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26-27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41-42', '43', '44', '45', '46', '47', '48', '49', '5', '50', '51', '52', '53', '54', '55', '6', '7', '8', '9'), 12: ('1', '10', '11', '12', '13-14', '15', '16', '17', '18-19', '2', '20', '3-4', '5', '6-7', '8', '9'), 13: ('1-2', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '4', '5', '6-7', '8-12'), 14: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22-25', '26', '27', '3', '4', '5', '6', '7', '8', '9'), 15: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '3-4', '5', '6', '7', '8', '9'), 16: ('1-3', '10', '11-12', '13-15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '4', '5', '6', '7', '8', '9'), 17: ('1', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26-27', '28', '3', '4', '5-6', '7', '8-10'), 18: ('1', '10', '11', '12', '13-14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36-37', '38', '39', '4', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '5', '50', '51-53', '54', '55', '56', '57', '58', '59', '6', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '7', '70', '71', '72', '73', '74', '75', '76', '77', '78', '8', '9'), 2: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42-43', '44', '45', '46', '47', '48', '49', '5', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '6', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '7', '70', '71', '72', '8', '9'), 3: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42', '43', '5', '6', '7', '8', '9'), 4: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42', '5', '6', '7', '8', '9'), 5: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27-28', '29', '3', '4', '5', '6', '7', '8-9', 'chapterview'), 6: ('1', '10', '11-12', '13-14', '15', '16', '17', '18', '19', '2', '20-23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42', '43', '44', '45', '46', '47', '5', '6', '7', '8', '9'), 7: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '4', '5', '6', '7', '8', '9'), 8: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '3', '4', '5', '6', '7', '8', '9'), 9: ('1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '4', '5', '6', '7', '8', '9')}



def extract_purport(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    purport_start = "===== Purport ====="
    purport_end = "====="
    
    purport_lines = []
    inside_purport = False
    
    for line in lines:
        if purport_start in line:
            inside_purport = True
            continue
        if purport_end in line and inside_purport:
            inside_purport = False
            break
        if inside_purport:
            purport_lines.append(line.strip('\n'))

    purport_text = '\n'.join(purport_lines)  
    return purport_text

def create_markdown_file(pre_written_text, user_text, output_file_path):
    combined_text = pre_written_text + "\n\n" + user_text
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(combined_text)

pre_written_text = """---    
markmap:
    colorFreezeLevel: 2
    maxWidth: 200
    embedAssets: true
    initialExpandLevel: 3
---
    """

system_prompt = "You will be given a purport of a verses from bhagavada-Gita. Your task is to analyse it and help the user by extracting all the information about the teachings and examples from the purport and provide it in the form of a mind map.\
            Give only markdown code without any other text with using only '#' symbol and no indentation at the start of each line for creating a mind map. The mind map should visually represent the relationships and hierarchy of all the complete information in the given input.\
            Use meaningful connections between the concepts and organize them logically.\
            Instructions:\
                1. Give only markdown code without any other text. Use only '#' symbol. No indentation at the start of each line.\
                2. Use all the concepts from the inputs and make it lengthy.\
                3. Identify the main topics and subtopics.\
                4. Create a dense lengthy hierarchical relationships between these topics.\
                6. Explain the concepts of the text for clear understanding and be authentic to the given input.\
            Example text : Artificial Intelligence (AI) is a branch of computer science. It includes machine learning, where computers learn from data.\
                Deep learning is a subset of machine learning involving neural networks. AI is used in various fields such as healthcare, finance, and transportation.\
                In healthcare, AI helps in diagnosing diseases. In finance, AI is used for fraud detection.\
                In transportation, AI powers autonomous vehicles.\
            output:\
            # Mind Map\
            ## Artificial Intelligence (AI)\
            ### Branches\
            #### Machine Learning\
            ##### Computers learn from data\
            #### Deep Learning\
            ##### Subset of machine learning\
            ##### Involves neural networks\
            ### Applications\
            #### Healthcare\
            ##### Diagnosing diseases\
            #### Finance\
            ##### Fraud detection\
            #### Transportation\
            ##### Autonomous vehicles"


## streamlit framework

# Title of the app
# Ensure folder exists for HTML files
html_folder = "generated_html"
os.makedirs(html_folder, exist_ok=True)

st.title('Langchain Demo With LLAMA3:latest API')

# Select chapter number
chapter = st.selectbox("Enter chapter number:", chapter_name.keys(), key=1, index=None, placeholder="Select chapter number...")

if chapter:
    # Select verses number
    verses = st.multiselect("Enter verses number:", chapter_verse_dict[chapter_name[chapter]], key=2)
    chapter = chapter_name[chapter]

    if chapter and verses:
        for verse in verses:
            with st.expander(f"Chapter number: {chapter}, Verse: {verse}" , expanded=True):
                file_path = f"Bhagvada-Gita/{chapter}/{verse}.txt"
                input_text = extract_purport(file_path)

                st.write(f"Chapter number: {chapter}, Verse: {verse}")

                # Initialize the Ollama LLM
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": f"{system_prompt}"
                        },
                        {
                            "role": "user",
                            "content": f"{input_text}",
                        }
                    ],
                    model="llama3-70b-8192",
                    temperature=0.01
                )

                if input_text:
                    output = chat_completion.choices[0].message.content

                    # Generate file names
                    file_name = f"mark_{chapter}_{verse}.md"
                    html_file = f"{html_folder}/mark_{chapter}_{verse}.html"  # Store in the html_folder

                    # Create markdown file
                    create_markdown_file(pre_written_text, output, file_name)

                    # Convert markdown to HTML using markmap
                    command = f'markmap-cli {file_name} -o {html_file}'
                    subprocess.run(command, shell=True , executable='/bin/bash')

                    # Read the generated HTML file
                    with open(html_file, "r", encoding="utf-8") as file:
                        html_content = file.read()

                    # Embed the HTML content in Streamlit
                    components.html(html_content , height=400)
                    st.write(input_text)

            
        
            
