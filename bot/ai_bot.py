import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')

    def invoke(self, question):
        prompt = PromptTemplate(
            input_variables=['texto'],
            template='''
            Você um tradutor de textos que traduz o texto do usuário
            para Italiano.
            <texto>
            {texto}
            </texto>
            '''
        )

        chain = prompt | self.__chat | StrOutputParser()
        
        response = chain.invoke({
            'texto': question
        })

        return response
    