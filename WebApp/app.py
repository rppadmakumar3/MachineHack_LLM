import streamlit as st
from transformers import pipeline

# Load the Hugging Face question-answering pipeline
pipe = pipeline("question-answering", model="sivapriyakumar16/machinehack_updated")

# Set the title and description of your app
st.title("Question Answering Web App")
st.write("This app uses Hugging Face's Transformers to answer questions using the sivapriyakumar16/machinehack_updated model.")

# Create a text input box for user input
question = st.text_input("Ask a question:", "")

# Create a textarea for the passage or context
context = st.text_area("Provide the context or passage:", "")

# Add a button to trigger the question answering process
if st.button("Answer"):
    if not question:
        st.warning("Please enter a question.")
    elif not context:
        st.warning("Please provide a context or passage.")
    else:
        # Use the Hugging Face pipeline to answer the question
        answer = pipe(question=question, context=context)

        # Display the answer
        st.subheader("Answer:")
        st.write(answer['answer'])

        # Display the confidence score
        st.write("Confidence Score:", answer['score'])

# Add a reset button to clear the input fields
if st.button("Reset"):
    question = ""
    context = ""