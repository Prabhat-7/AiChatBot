from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
PROJECT_ID="langchain-26b97"
llm =ChatGroq(model="llama-3.1-70b-versatile")
messages=[
("system","You are a facts expert who knows facts about {animal}"),
("human","Tell me {facts_count} facts")
]
prompt_template=ChatPromptTemplate.from_messages(messages)
chain=prompt_template | llm

response =chain.invoke({
    "animal":"cat",
    "facts_count":"3"
})
print(response.content)
