import os

from decouple import config

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.3-70b-versatile')
        self.__retriever = self.__build_retriever()

    def __build_retriever(self):
        persist_directory = '/app/chroma_data'
        embedding = HuggingFaceEmbeddings()

        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding,
        )

        return vector_store.as_retriever(
            search_kwargs={'k': 30}
        )
    
    def __build_messages(self, history_messages, question):
        messages = []

        for message in history_messages:
            message_class = HumanMessage if message.get('fromMe') else AIMessage

            messages.append(message_class(content=message.get('body')))

        messages.append(HumanMessage(content=question))

        return messages        

    def invoke(self, history_messages, question):
        SYSTEM_TEMPLATE = '''
        Responda as perguntas dos usuários com base no contexto abaixo.
        Seu nome é Vinicius Perrone, é desenvolvedor Python. Aqui está sua descrição,
        
        Experiência atuando com consultoria. Participação em diferentes projetos para diferentes empresas, sistemas de gestão empresarial (ERP), CRM, CMS para Landing Pages e Sites dinâmicos. No dia a dia, atuo na análise e desenvolvimentos de novos projetos, participação em revisão de MR (Merge Request), deploy para produção de aplicações, e manutenção de serviços já existentes.

        - Django/Python;
        - React/React Native/Next.js;
        - Javascript/Typescript/Node.js;
        - Banco de Dados NoSQL e SQL: MySQL, Postgress, SQLite, MongoDB e ElasticSearch
        - Teste unitários/integração com Pytest;
        - AWS (EC2, Lambda, S3) com Boto3;
        - Conteinerização com Docker;
        - Gerenciamento de projetos e ordenação de tarefas com Slack/Clickup;

        Responda pergunta baseadas nisso da forma mais humana possível.
        <context>
        {context}
        </context>
        '''

        docs = self.__retriever.invoke(question)
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    SYSTEM_TEMPLATE
                ),
                MessagesPlaceholder(variable_name='messages')
            ]
        )

        document_chain = create_stuff_documents_chain(self.__chat, question_answering_prompt)
        response = document_chain.invoke(
            {
                'context': docs,
                'messages': self.__build_messages(history_messages, question)
            }
        )

        return response
    