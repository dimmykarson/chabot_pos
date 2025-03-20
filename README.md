# Chat Bot Pós iCEV

Este é um chatbot desenvolvido com **Streamlit** e **OpenAI** para auxiliar os alunos da Pós-Graduação do iCEV. O chatbot, chamado **Rebeca**, interage com os usuários respondendo perguntas e oferecendo suporte.

## 📌 Funcionalidades
- Interface interativa usando **Streamlit**
- Armazena histórico de mensagens na sessão
- Cria threads para manter a continuidade das conversas
- Integração com a API da OpenAI
- Personalização com imagens e layout responsivo

## 🚀 Tecnologias Utilizadas
- **Python 3.12**
- **Streamlit**
- **OpenAI API**
- **Pillow (PIL)**
- **dotenv** (para carregar variáveis de ambiente)

## 📂 Estrutura do Projeto
```plaintext
├── imgs/
│   ├── bird_2.jpg  # Imagem usada como ícone e logotipo
├── openai_utils.py  # Módulo que gerencia a interação com a API da OpenAI
├── home.py  # Arquivo principal com a interface do chatbot
├── .env  # Arquivo de variáveis de ambiente contendo as credenciais
├── requirements.txt  # Dependências do projeto
```

## 🔧 Configuração e Execução
### 1️⃣ Instalar dependências
Certifique-se de ter o **Python 3.12** instalado e, em seguida, rode:
```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais da OpenAI:
```ini
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o
OPENAI_ASSISTANT_ID=asst_...
OPENAI_VECTOR_STORE_ID=vs_...
```

### 3️⃣ Executar o Chatbot
Inicie a aplicação com o seguinte comando:
```bash
streamlit run home.py
```

## 📝 Funcionamento
1. O chatbot inicia com uma mensagem de boas-vindas.
2. O usuário pode digitar perguntas no campo de chat.
3. As mensagens são processadas pelo **OpenClient**, que interage com a OpenAI.
4. A resposta do chatbot é exibida na interface do Streamlit.
5. O histórico da conversa é armazenado na sessão do usuário.

## 📷 Captura de Tela (Exemplo de Interface)
![Chatbot Interface](imgs/bird_2.jpg)

## 🔗 Referências
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/)

## 📌 Autor
Projeto desenvolvido por **Dimmy Magalhães**.