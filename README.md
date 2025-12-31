# 🔥 Chatbot Whatsapp
Chatbot de Whatsapp com Integração com IA. O projeto inclui também a aplicação de contexto 
ao nossa IA para contextualizar nosso modelo, essa estratégia é conhecida como RAG, ou <i>Retrieval-augmented generation</i>

<p align="center">
    <img src="/images/arquitetura_projeto.webp" alt="Logo">
</p>

# 🛠️ Tecnologias Envolvidas

- Flask: Webhook para manipular eventos de mensagens.
- Waha: Integração com Whatsapp
- Python: Linguagem de Programção
- LangChain: Framework para criação e manipulação de modelos LLMs

# 🚀 Rodar Projeto

Para rodar aplicação você deve seguir os seguintes passos:

- Subi os containers da aplicação
```bash
$ docker-compose up -d --build
```

- Conectar seu dipositivo ao Waha pelo dashboard `http://localhost:3000/dashboard`

