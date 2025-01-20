from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.output_parser import StrOutputParser
import topics
import random

load_dotenv()

def CallGroq(what = "post", model="llama-3.3-70b-versatile", temp = 0.7):
    try:
        llm = ChatGroq(temperature=temp, model= model)
        prompt = f"""
            Generate a reddit {what} on the topic {random.choice(topics.topics_list)}
            Generate only {what}, like a human would type"""
        
        chain = llm | StrOutputParser()
        return chain.invoke(prompt)

    except Exception as e:
        return f"Error: {str(e)}"

# text = CallGroq()  
# print(text)


def CommentGroq(post, what = "comment", model="llama-3.3-70b-versatile", temp = 0.7):
    try:
        llm = ChatGroq(temperature=temp, model= model)
        prompt = f"""
        Generate a reddit {what} to reply the {post}
        Generate only {what}, like a human would type"""

        chain = llm | StrOutputParser()
        return chain.invoke(prompt)

    except Exception as e:
        return f"Error: {str(e)}"
    
# print(CommentGroq())