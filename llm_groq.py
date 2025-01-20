from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

def CallGroq(model="llama-3.3-70b-versatile", temp = 0.7, given_prompt = "Hi"):
        try:
            llm = ChatGroq(temperature=temp, model= model)
            system = "You are a helpful assistant."
            human = "{text}"
            prompt = PromptTemplate.from_template(human)
            chain = prompt | llm | StrOutputParser()
            return chain.invoke({"text": given_prompt})

        except Exception as e:
            return f"Error: {str(e)}"
        
print(CallGroq())