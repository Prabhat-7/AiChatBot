
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
try:
    llm =ChatGroq(model="llama-3.1-70b-versatile")
except:
    llm =ChatGroq(model="llama-3.1-8b-instant")
messages=[
    SystemMessage("You are a expert chatbot.And you are giving short answers(about 3 lines) until I ask for long ones."),
    ]

@api_view(['POST'])
def ask(request):
    try:
        query=request.data
        messages.append(HumanMessage(query))
        response =llm.invoke(messages)
        messages.append(AIMessage(response.content))
        


        return Response({"response":response.content}, status=status.HTTP_201_CREATED)
    except:
        return Response({"Error": "Could not recieve the prompt properly"})
    
# Create your views here.
