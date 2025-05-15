# CADE - Sistema de Gestão e Chatbot

## 📋 Descrição
Sistema web desenvolvido para o Conselho Administrativo de Defesa Econômica (CADE), integrando gestão de documentos e atendimento automatizado via chatbot. O sistema oferece suporte multilíngue (Português, Inglês e Espanhol) e interface intuitiva para consulta de processos e documentos.

## 🚀 Funcionalidades

### Principais Features
- 🤖 Chatbot inteligente para atendimento
- 🌐 Suporte multilíngue (PT, EN, ES)
- 📄 Gestão de documentos e processos
- 📱 Interface responsiva
- 🔍 Busca avançada de processos
- 📝 Newsletter por email

## 🛠️ Tecnologias Utilizadas

### Backend
- Python 3.11
- Django 5.1.2
- PostgreSQL

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5.3

### Infraestrutura
- Docker
- Docker Compose

## 📦 Instalação e Uso

### Pré-requisitos
- Python 3.11+
- Docker e Docker Compose
- PostgreSQL

### Configuração Local
1. Clone o repositório:
```bash
git clone https://github.com/dutra-felipe/cade_project.git
cd cade-project
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
DEBUG=True
SECRET_KEY=sua-chave-secreta
DATABASE_URL=postgres://usuario:senha@localhost:5432/CADE_DB
```

### Rodando com Docker
```bash
docker-compose up -d
```

### Configuração do Banco de Dados
```bash
python manage.py migrate
python manage.py setup_faq_data  # Configura dados iniciais do chatbot
```

## 📚 Documentação

### Estrutura do Projeto
```bash
Copycade_project/
├── app/                 # Configurações principais
├── chatbot/             # Aplicação do chatbot
├── documentos/          # Gestão de documentos
├── usuarios/            # Gestão de usuários
├── static/              # Arquivos estáticos
├── templates/           # Templates HTML
├── nltk_data/           # Treinamento chatbot
├── build.sh             # Arquivo de permissões
├── Dockerfile           # Dockerfile
├── docker-compose.yml   # Configurações de containers
├── manage.py            # Arquivo principal do projeto
└── requirements.txt     # Dependências
```

## 🚀 Deploy

### Render

- Configure as variáveis de ambiente no Render
- Conecte ao repositório GitHub
- Configure o build command
- Configure o start command

## 👥 Contribuição

- Faça um Fork do projeto
- Crie uma branch para sua feature
- Faça commit das alterações
- Push para a branch
- Abra um Pull Request

## ✒️ Autor

Felipe Dutra

## 📞 Contato

- GitHub: [Felipe Dutra](https://github.com/dutra-felipe)
- Linkedin: [Felipe Dutra](https://www.linkedin.com/in/felipepdutra/)
