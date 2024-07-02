import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")

# Define the system prompt
system_prompt = """ Generating Questions and Answers from the Purport of a Bhagavad Gita Verse

1. Read the Verse and Purport:
   - Carefully read the provided verse from the Bhagavad Gita and its purport. Take note of the key themes, concepts, and any significant terms or phrases mentioned.

2. Identify Key Concepts:
   - Highlight the main ideas presented in the purport. These could include philosophical concepts, instructions, historical context, or any other significant points.

3. Formulate 5 open questions :
   - Based on the key concepts, create questions that probe deeper into the meanings and implications of the verse and purport. These questions should encourage exploration and understanding of the text.

4. 5 Fill in the blanks questions :
  - Create questions that require the user to fill in the blanks with appropriate words. Make the missing words or phrases shorter and be authentic to the source ,i.e, input text.
   
5. Provide Answers:
   - Answer the questions using information from the purport and your understanding of the text. Ensure that the answers are clear, concise, and informative.

6. Keep the formatting clear and easy to understand:
   - Use headings, bullet points, and other formatting techniques to make the questions and answers easy to read and comrehend. seperate answers and questions in another line.

Example:

purport : The Lord at once took the position of the teacher and chastised the student, calling him, indirectly, a fool. The Lord said, you are talking like a learned man, but you do not know that one who is learned-one who knows what is body and what is soul-does not lament for any stage of the body, neither in the living nor in the dead condition. As it will be explained in later chapters, it will be clear that knowledge means to know matter and spirit and the controller of both. Arjuna argued that religious principles should be given more importance than politics or sociology, but he did not know that knowledge of matter, soul and the Supreme is even more important than religious formularies. And, because he was lacking in that knowledge, he should not have posed himself as a very learned man. As he did not happen to be a very learned man, he was consequently lamenting for something which was unworthy of lamentation. The body is born and is destined to be vanquished today or tomorrow; therefore the body is not as important as the soul. One who knows this is actually learned, and for him there is no cause for lamentation, regardless of the condition of the material body. 

Key Concepts:

Knowledge of body and soul
Importance of spiritual knowledge over religious formularies
Lamentation and its causes
The temporary nature of the body
The characteristics of a truly learned person

Generated Questions and Answers:

What is the significance of the Lord chastising Arjuna, calling him indirectly a fool? 
Answer: The Lord is pointing out Arjuna's lack of understanding of the fundamental principles of knowledge, which is essential for making informed decisions and avoiding unnecessary lamentation.

How does one's understanding of the body and soul impact their perspective on life and death? 
Answer: Knowing the difference between the body and soul helps one understand that the body is temporary and ephemeral, while the soul is eternal, leading to a shift in focus from material concerns to spiritual growth.

What is the relationship between knowledge and lamentation, according to the Lord? 
Answer: The Lord suggests that one who has true knowledge of matter, soul, and the Supreme does not lament, as they understand the temporary nature of the body and the eternal nature of the soul.

Why is knowledge of the Supreme more important than religious formularies, according to the Lord? 
Answer: Knowledge of the Supreme is more important because it provides a deeper understanding of the nature of reality, whereas religious formularies are limited to external practices and rituals.

What are the characteristics of a truly learned person, according to the Lord? 
Answer: A truly learned person is one who knows the difference between the body and soul, understands the temporary nature of the body, and is not attached to material concerns, leading to a state of equanimity and freedom from lamentation.

Fill-in-the-blank Questions:

According to the Lord, one who knows what is _______________________ and what is _______________________ does not lament for any stage of the body.
Answer: body, soul

The Lord says that knowledge means to know _______________________, _______________________, and the controller of both.
Answer: matter, spirit

Arjuna was lacking in the knowledge of _______________________, _______________________, and the Supreme, which is more important than religious formularies.
Answer: matter, soul

The body is born and is destined to be _______________________ today or tomorrow.
Answer: vanquished

One who knows the temporary nature of the body is actually _______________________ and for him there is no cause for lamentation.
Answer: learned
"""

# Streamlit UI
st.title("Bhagavad Gita Verse Q&A Generator")

# Input text area
input_text_area = st.text_area("Input Purport Text")

# Generate button
if st.button("Generate Questions and Answers"):
    with st.spinner("Generating..."):
        # Generate chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"{system_prompt}"
                },
                {
                    "role": "user",
                    "content": f"{input_text_area}",
                }
            ],
            model="llama3-70b-8192",
            temperature=0.1
        )
        output = chat_completion.choices[0].message.content

        # Display output
        st.markdown(output)
