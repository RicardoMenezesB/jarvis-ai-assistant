# Configurações do projeto PC

## Visão geral
PC é um assistente de IA de voz e produtividade com arquitetura inspirada em um copiloto premium tipo Jarvis.

Ele pode:
- conversar por voz e texto
- pesquisar na web
- escrever código, roteiros e estratégias
- lembrar preferências do usuário
- usar múltiplos agentes especializados
- evoluir para automações e tarefas mais avançadas

## Stack recomendada
- Frontend: React + Vite + TypeScript
- Backend: FastAPI + Python
- IA: Groq, OpenRouter, OpenAI, Ollama
- Busca: Tavily, Brave
- Voz: Web Speech API + TTS
- Memória: sessão local em MVP e evolução para banco + embeddings

## Estrutura do projeto
- `backend/` — API e lógica dos agentes
- `frontend/` — interface do assistente
- `.env.example` — modelo de variáveis de ambiente

## Configuração das chaves
Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`.

```bash
cp .env.example .env
```

Preencha os valores conforme o provedor que você quiser usar.

### Exemplos de chave por provedor
- Groq: `GROQ_API_KEY`
- OpenRouter: `OPENROUTER_API_KEY`
- OpenAI: `OPENAI_API_KEY`
- Tavily: `TAVILY_API_KEY`
- Brave: `BRAVE_API_KEY`
- ElevenLabs: `ELEVENLABS_API_KEY`
- Azure Speech: `AZURE_SPEECH_KEY`

## Variáveis principais
```env
APP_NAME=PC
APP_MODE=development
DEFAULT_LANGUAGE=pt-BR

GROQ_API_KEY=your_key_here
GROQ_MODEL=llama-3.1-70b-versatile

OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini

OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1

TAVILY_API_KEY=your_key_here
BRAVE_API_KEY=your_key_here

ELEVENLABS_API_KEY=your_key_here
ELEVENLABS_VOICE_ID=your_voice_id

AZURE_SPEECH_KEY=your_key_here
AZURE_SPEECH_REGION=eastus
```

## Como rodar

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Próximas evoluções planejadas
- wake word e ativação por voz automática
- banco real com memória persistente
- agentes mais especializados por tarefa
- busca em tempo real com resumo e fontes
- automações locais e tarefas do sistema
- integração com ferramentas e APIs externas
- painel de configuração dentro do app para trocar chaves em runtime

## Observação importante
Sem chaves, o app continua funcionando em modo local com respostas simuladas. Para pesquisa real, voz de IA e respostas com modelos externos, configure os providers no `.env`.
