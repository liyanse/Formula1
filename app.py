from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from llama_index import GPTSimpleVectorIndex
from llama_index import download_loader
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

doc_path = 'data/'
index_file = 'index.json'

if 'response' not in st.session_state:
    st.session_state.response = ''


def send_click():
    st.session_state.response = index.query(st.session_state.prompt)


index = None
st.title("PDF chatbot")

max_file_size = 1024 * 1000
max_num_files = 2
st.warning(
    'Maximum file size allowed is 100 KB. Maximum number of files allowed is 2.')
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

if len(uploaded_files) == 0:
    st.warning("Please upload a file.")
    st.stop()

if uploaded_files is not None:
    if (len(uploaded_files) > max_num_files):
        st.warning(
            f"Maximum number of files allowed is {max_num_files}.")
        st.stop()
    else:
        doc_files = os.listdir(doc_path)
        for doc_file in doc_files:
            os.remove(doc_path + doc_file)

        for uploaded_file in uploaded_files:
            if uploaded_file.size > max_file_size:
                st.warning(
                    f"File {uploaded_file.name} is larger than the maximum allowed size of {max_file_size / 1024} KB.")
                st.stop()
            else:
                bytes_data = uploaded_file.read()
                with open(f"{doc_path}{uploaded_file.name}", 'wb') as f:
                    f.write(bytes_data)

    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

    loader = SimpleDirectoryReader(
        doc_path, recursive=True, exclude_hidden=True)

    documents = loader.load_data()

    max_input_size = 4096
    num_output = 256
    max_chunk_overlap = 20
    chunk_size_limit = 600
    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0.3, model_name="gpt-3.5-turbo", max_tokens=num_output))

    prompt_helper = PromptHelper(
        max_input_size, num_output, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context
    )

    index.save_to_disk(index_file)


elif os.path.exists(index_file):
    index = GPTSimpleVectorIndex.load_from_disk(index_file)

    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
    loader = SimpleDirectoryReader(
        doc_path, recursive=True, exclude_hidden=True)
    documents = loader.load_data()
    doc_filename = os.listdir(doc_path)[0]

if index != None:
    st.text_input("Your question ", key='prompt')
    st.button("Ask", on_click=send_click)
    if st.session_state.response:
        st.subheader("Response: ")
        st.success(st.session_state.response, icon="🤖")