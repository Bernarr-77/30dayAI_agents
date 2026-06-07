
# 🤖 30 Dias de AI Agents: Do Zero ao Intermediário

**Objetivo Final:** Um AI Agent funcional e inteligente que pensa, usa ferramentas e toma decisões.

**Filosofia:** Projeto-driven, escalado progressivamente. Você constrói coisas reais, não faz tutoriais chatos. **Sem código entregue — você escreve tudo.**

---

## ⚡ Semana 1: Fundamentos + Chat Básico
**Meta:** Entender LLM básico. Sair com um agente conversacional simples.

### Dia 1: Setup Gemini API + Primeira Chamada
- Configure Google AI Studio: https://aistudio.google.com/app/apikeys
- Crie uma API Key
- Configure variável de ambiente `GEMINI_API_KEY`
- Instale biblioteca: `pip install google-generativeai`
- **Projeto:** Crie um script que chama Gemini uma vez com prompt fixo, imprime resposta

**Desafio:** API funciona e retorna resposta. Trate erro se API falhar.

**Entrega:** Script `agent_v1.py` que chama IA uma vez.

---

### Dia 2: Input do Usuário
- Leia entrada do terminal (input())
- Passe como prompt pra IA
- Imprima resposta
- **Projeto:** Chat simples — usuário digita, IA responde, fim

**Desafio:** Valide entrada vazia. Não deixe enviar prompt vazio.

**Entrega:** `agent_v2.py` interativo com usuário.

---

### Dia 3: Histórico de Conversa
- Entenda por que manter histórico: IA não tem memória entre calls
- Armazene em lista: `[{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]`
- Sempre envie histórico completo pra IA (ela precisa ver contexto)
- **Projeto:** Chat que lembra conversa anterior

**Desafio:** Histórico não cresce infinito. Implemente limite (últimas 10 mensagens).

**Entrega:** `agent_v3.py` com memória de conversa.

---

### Dia 4: System Prompt (Personalização)
- Entenda system prompt: instrução que define comportamento da IA
- Exemplos: "você é um professor", "você é sarcástico", "fale em português do Brasil"
- **Projeto:** Crie agente personalizado:
  - Escolha um personagem/papel (professor, programador, assistente, etc)
  - System prompt define o comportamento
  - Conversa mantém essa personalidade

**Desafio:** System prompt é ajustável via variável/arquivo config.

**Entrega:** `agent_v4.py` com personalidade definida.

---

### Dia 5: Tratamento de Erros
- Entenda erros possíveis: API falha, conexão perdida, token inválido, rate limit
- Trate cada um diferente (retry, mensagem clara, etc)
- **Projeto:** Adicione error handling robusto:
  - Tenta chamar IA
  - Se falhar, diz ao usuário por quê
  - Oferece retry ou encerra graciosamente

**Desafio:** Retry automático com backoff (espera progressiva entre tentativas).

**Entrega:** `agent_v5.py` com error handling profissional.

---

### Dia 6: Logging Estruturado
- Entenda logging: rastrear o que acontece (debug, info, error)
- Use `logging` nativo de Python
- **Projeto:** Adicione logs em tudo:
  - Quando API é chamada
  - Resposta recebida
  - Erros ocorrem
  - Histórico aumenta

**Desafio:** Logs podem ser salvos em arquivo também (não só console).

**Entrega:** `agent_v6.py` com logging completo.

---

### Dia 7: Testes com Pytest + Refactor
- Instale pytest: `pip install pytest`
- Aprenda estrutura: arquivo `test_agent.py`, funções `test_*`, usar `assert`
- **Projeto:** Escreva testes pra tudo dos dias 1-6:
  - Teste que API é chamada (sem chamar API de verdade, use mock)
  - Teste que entrada vazia é rejeitada
  - Teste que histórico cresce
  - Teste system prompt é respeitado
  - Teste error handling

**Desafio:** Roda `pytest` e todos os testes passam. Cobertura > 70%.

**Entrega do Dia 7:**
- `agent_v7.py` refatorado e estruturado
- `test_agent.py` com testes abrangentes
- `SEMANA_1_REVIEW.md` explicando arquitetura
- Commit no GitHub com tag `semana-1-completa`

---

## 🎯 Semana 2: Controle Fino + Parsing
**Meta:** Dominar parâmetros da IA e extrair dados estruturados.

### Dia 8: Parâmetros da IA (Temperature, Top P, Max Tokens)
- **Temperature:** criatividade (0 = determinístico, 1 = criativo)
- **Top P:** diversidade de palavras
- **Max Tokens:** limite de resposta
- **Projeto:** Crie agente com controle fino:
  - Diferentes "modos": criativo (temp 1), profissional (temp 0.3), balanceado (temp 0.7)
  - Usuário pode escolher modo
  - Parâmetros ajustam automaticamente

**Desafio:** Modo afeta qualidade de resposta. Teste em casos reais.

**Entrega:** `agent_v8.py` com seleção de modo.

---

### Dia 9: Multi-Turn Conversation Otimizado
- Entenda trade-offs: histórico longo = contexto melhor, mas custo maior + latência
- Implemente "sliding window": manter últimas N mensagens (não todas)
- Resumo opcional: se histórico fica muito grande, resuma e continue
- **Projeto:** Otimize conversa:
  - Histórico automático: manter últimas 5 turnos
  - Se exceder, remove turnos antigos
  - Mensagens muito longas são truncadas

**Desafio:** Conversa flui naturalmente mesmo com histórico limitado.

**Entrega:** `agent_v9.py` com multi-turn otimizado.

---

### Dia 10: Parsing de Resposta (Extração de Dados)
- IA retorna text puro, mas você pode extrair padrões (JSON, listas, etc)
- Técnicas: regex, JSON parsing, split por delimitadores
- **Projeto:** Agente que extrai dados estruturados:
  - Peça pra IA retornar em formato específico (JSON, lista, etc)
  - Parse resposta
  - Estruture dados para uso

**Desafio:** Resposta pode não ser exatamente no formato pedido. Trate fallback.

**Entrega:** `agent_v10.py` que extrai dados estruturados.

---

### Dia 11: Validação de Entrada Avançada
- Entenda segurança: prompt injection, inputs maliciosos
- Valide tipos, tamanho, conteúdo de entrada
- **Projeto:** Adicione validação robusta:
  - Rejeita prompts muito longos (evita abuse)
  - Rejeita caracteres especiais perigosos
  - Mensagem clara de por que foi rejeitado

**Desafio:** Validação não é restritiva demais (usuário legítimo consegue usar).

**Entrega:** `agent_v11.py` com validação de segurança.

---

### Dia 12: Streaming de Resposta
- Entenda streaming: IA retorna resposta palavra por palavra (mais rápido sentir resposta)
- Implemente visualização em tempo real (não espera tudo pronto)
- **Projeto:** Agente que faz streaming:
  - Começa imprimir resposta conforme IA gera
  - Usuário vê resposta aparecendo em tempo real
  - Sente mais rápido

**Desafio:** Streaming não quebra histórico. Resposta completa ainda é salva.

**Entrega:** `agent_v12.py` com streaming.

---

### Dia 13: Rate Limiting e Error Recovery
- Entenda rate limit: API permite N requisições por minuto
- Implemente contador local
- Recovery automático: espera e retry
- **Projeto:** Proteja sua app:
  - Contador de requisições
  - Se exceder limite, avisa usuário
  - Espera automaticamente
  - Retry quando possível

**Desafio:** User experience não sofre. Feedback claro de quando pode usar de novo.

**Entrega:** `agent_v13.py` com rate limiting.

---

### Dia 14: Refactor em Estrutura Profissional + Testes
- Organize código em módulos: `agent.py`, `api.py`, `utils.py`, `config.py`
- Cada módulo tem responsabilidade clara
- **Projeto:** Refatore tudo pra estrutura real:

```
ai_agent/
├── agent.py (lógica do agent)
├── api.py (chamadas pra Gemini)
├── models.py (estruturas de dados)
├── config.py (configurações)
├── utils.py (funções auxiliares)
├── main.py (entry point)
└── tests/
    ├── test_agent.py
    ├── test_api.py
    └── test_utils.py
```

**Desafio:** Código está pronto pra crescer. Testes passam. Sem duplicação.

**Entrega do Dia 14:**
- Código refatorado em módulos
- Testes pra cada módulo
- `SEMANA_2_REVIEW.md` documentando decisões
- Commit com tag `semana-2-completa`

---

## 🔧 Semana 3-4: Agent Avançado + Produção
**Meta:** Agente que pensa, usa ferramentas e toma decisões.

### Dia 15: Função Calling (Agent Chama Ferramentas)
- Entenda function calling: IA decide chamar função Python (não só text)
- Define disponibilidade de funções pra IA ("aqui estão ferramentas que posso usar")
- IA escolhe chamar ou não
- **Projeto:** Defina primeira ferramenta:
  - Crie função simples (ex: `get_weather()`, `search_web()`, `calculate()`)
  - Descreva pra IA: "você pode usar essa função se precisar"
  - IA decide chamar ou não conforme contexto

**Desafio:** IA só chama função quando faz sentido. Não chama desnecessariamente.

**Entrega:** `agent_v15.py` com function calling.

---

### Dia 16: Execução de Função + Parsing de Resultado
- IA chama função → você executa → passa resultado de volta pra IA
- IA refina resposta com resultado
- **Projeto:** Implemente loop:
  1. Usuário pergunta
  2. IA decide chamar função (ou não)
  3. Você executa
  4. IA recebe resultado
  5. IA responde baseado em resultado

**Desafio:** Função pode falhar. Trata erro e passa pra IA ("função falhou com erro X").

**Entrega:** `agent_v16.py` com execução de função.

---

### Dia 17: Múltiplas Funções (Tools)
- Agora IA tem várias ferramentas disponíveis
- Cada tool tem: nome, descrição, parâmetros
- IA escolhe qual tool chamar (ou chamar várias)
- **Projeto:** Adicione 3-5 tools diferentes:
  - Ex: `get_weather()`, `search_wikipedia()`, `calculator()`, `check_email()`, etc
  - IA pensa e escolhe qual usar conforme pergunta

**Desafio:** Tools são independentes. Cada um falha de forma diferente. IA sabe lidar.

**Entrega:** `agent_v17.py` com múltiplos tools.

---

### Dia 18: Chains (Sequência de Chamadas)
- Às vezes IA precisa chamar ferramenta A, depois ferramenta B, depois refinar
- Entenda chains: sequência de steps que levam a resultado final
- **Projeto:** Crie cadeia de ferramentas:
  - Pergunta: "qual é a capital da França e qual é a população?"
  - Cadeia: search → get resultado → search novamente → refine resposta

**Desafio:** Chain não é hardcoded. IA decide a sequência dinamicamente conforme pergunta.

**Entrega:** `agent_v18.py` com chains.

---

### Dia 19: Database Integration (Agent Salva/Lê Dados)
- Agent não vive só em memória. Persiste informações em banco
- Crie simples: SQLite com tabela de conversas/dados
- **Projeto:** Agente que salva dados:
  - Usuário fala: "meu nome é Bernardo"
  - Agent salva em DB
  - Próxima conversa, agent lembora: "Olá Bernardo"
  - Agent pode buscar dados antigos se perguntado

**Desafio:** DB não quebra se agent chamar múltiplas vezes. Transações tratadas.

**Entrega:** `agent_v19.py` com persistência em DB.

---

### Dia 20: Agentic Loop (Pensamento Iterativo)
- Entenda o loop: IA pensa → chama tool → recebe resultado → pensa novamente → repete
- IA itera até resolver problema (ou atingir limite)
- **Projeto:** Implemente loop robusto:
  - IA tenta resolver problema
  - Se não conseguir, chama tool
  - Processa resultado
  - Tenta novamente
  - Loop até: sucesso, erro fatal, ou max iterations

**Desafio:** Loop não é infinito. Limite de iterações (ex: máximo 10 steps).

**Entrega:** `agent_v20.py` com agentic loop.

---

### Dia 21: Validação de Tool Calls (Segurança)
- IA pode chamar função errada ou com parâmetros ruins
- Valide antes de executar
- **Projeto:** Adicione camada de validação:
  - IA quer chamar tool X com parâmetros Y
  - Você valida: função existe? parâmetros são válidos? é seguro?
  - Se tudo OK, executa. Se não, retorna erro pra IA refinar.

**Desafio:** Validação não para o agent. IA consegue refinar e tentar de novo.

**Entrega:** `agent_v21.py` com validação de tools.

---

### Dia 22: RAG Básico (Agent com Knowledge Base)
- RAG = Retrieval-Augmented Generation
- Agent tem acesso a knowledge base (documentos, dados estruturados)
- Quando perguntado, busca documento relevante e usa como contexto
- **Projeto:** Crie knowledge base simples:
  - Arquivo com informações (sobre você, seu negócio, documentação)
  - Agent busca informação relevante quando perguntado
  - Responde baseado em knowledge base (não halucina)

**Desafio:** Busca retorna documento relevante. Se nenhum relevante, agent sabe dizer "não tenho essa informação".

**Entrega:** `agent_v22.py` com RAG.

---

### Dia 23: Testing Tools (Pytest Integração)
- Teste tools: chamam o certo? retornam formato certo? tratam erro?
- Mock chamadas (não testa API de verdade durante teste)
- **Projeto:** Escreva testes completos:
  - Teste cada tool isolado
  - Teste agentic loop
  - Teste RAG busca
  - Teste validação
  - Teste chains

**Desafio:** Testes não dependem de API externa. Rápidos e confiáveis.

**Entrega:** `test_agent_v23.py` com cobertura completa.

---

### Dia 24: Logging e Monitoring
- Trace o que agent faz: qual tool chamou, quando, com quais parâmetros, resultado
- Monitoring: detect erros, performance issues
- **Projeto:** Adicione logging profissional:
  - Cada step do agentic loop é logado
  - Tool calls são registrados
  - Erros incluem contexto completo
  - Pode exportar logs (arquivo, dashboard)

**Desafio:** Logs são úteis pra debug. Mostram exatamente o que agent fez.

**Entrega:** `agent_v24.py` com logging completo.

---

### Dia 25: Performance e Otimização
- Entenda latência: onde IA gasta tempo?
- Caching: salvar resultados pra não computar novamente
- **Projeto:** Otimize performance:
  - Cache respostas da IA (mesma pergunta = resposta em cache)
  - Cache tool calls (mesmos parâmetros = resultado em cache)
  - Monitore latência

**Desafio:** Otimização não quebra corretude. Resultados ainda são precisos.

**Entrega:** `agent_v25.py` otimizado.

---

### Dia 26: Deployment Básico
- Deploy em produção: app roda em servidor, não no seu laptop
- Simples: railway, render, heroku, ou VPS
- **Projeto:** Deploy agent como API:
  - Crie endpoint: `POST /chat` (recebe mensagem, retorna resposta)
  - Deploy em plataforma escolhida
  - Teste chamando via HTTP

**Desafio:** Agent roda 24/7 online. Logs são accessíveis.

**Entrega:** Agent online, accessível via URL.

---

### Dia 27: API REST Completo
- Agora agent é mais que um endpoint
- Endpoints: chat, histórico, tools disponíveis, reset conversa, etc
- **Projeto:** Construa API profissional:
  - `POST /chat` → enviar mensagem
  - `GET /history` → buscar conversa
  - `GET /tools` → listar tools disponíveis
  - `DELETE /reset` → resetar conversa

**Desafio:** API é stateless ou stateful? Como gerencia múltiplos usuários?

**Entrega:** API REST funcionando.

---

### Dia 28: Persistência e Multi-Usuário
- Agent agora atende múltiplos usuários
- Cada usuário tem próprio histórico, preferências, dados
- **Projeto:** Implemente multi-usuário:
  - Usuário faz login (simples)
  - Histórico isolado por usuário
  - Agent lembra contexto entre sessions
  - Dados permanecem separados

**Desafio:** Sem bugs de segurança. Usuário A não vê dados do usuário B.

**Entrega:** `agent_v28.py` multi-usuário.

---

### Dia 29: Documentação e CLI
- Interface command-line pra testar agent localmente
- Documentação clara (README, docstrings, exemplos)
- **Projeto:** Prepare pra entrega:
  - CLI com commands: `chat`, `history`, `reset`, etc
  - README explicando: setup, uso, deployment
  - Docstrings em todas as funções
  - Exemplos de chamadas

**Desafio:** Alguém novo consegue usar seu agent sem sua ajuda.

**Entrega:** CLI funcional, README completo.

---

### Dia 30: Projeto Final + Publicação
**Meta:** Publicar agente completo, pronto pra produção.

- Escolha use case real (assistente pessoal, bot de suporte, pesquisador, criador de conteúdo, etc)
- Integre tudo dos dias 1-29
- Deploy online
- Documente tudo
- Teste end-to-end

**Entrega Final do Dia 30:**
- Agent funcional online
- GitHub repo com estrutura profissional
- README com instruções (setup, rodagem, deployment)
- `PROJETO_FINAL.md` explicando:
  - Arquitetura (módulos, responsabilidades)
  - Decisões técnicas
  - Tools disponíveis
  - Trade-offs
  - Possíveis melhorias
- Suite de testes (pytest, > 70% cobertura)
- Logs estruturados
- API documentada (Swagger ou similar)

---

## 📊 Checklist de Completion

Ao final dos 30 dias, você deve ter:

- ✅ LLM API fluente (Gemini setup, parâmetros, chamadas)
- ✅ Chat conversacional com histórico e memória
- ✅ Personalização (system prompt, temperature, etc)
- ✅ Error handling robusto
- ✅ Function calling (agent chama funções Python)
- ✅ Multiple tools (agent escolhe qual usar)
- ✅ Chains (sequência de calls)
- ✅ Agentic loop (pensamento iterativo)
- ✅ RAG básico (knowledge base)
- ✅ Database persistence
- ✅ Testes completos (pytest)
- ✅ Logging e monitoring
- ✅ Performance otimizado
- ✅ API REST
- ✅ Multi-usuário
- ✅ Deployment online
- ✅ Documentação profissional

**Resultado:** Um AI Agent production-ready que você construiu do zero.

---

## 🛠️ Setup Inicial (Antes do Dia 1)

- Crie pasta: `mkdir 30-days-ai-agents && cd 30-days-ai-agents`
- Git init: `git init`
- Venv: `python -m venv venv` + activate
- Dependências: `pip install google-generativeai pytest python-dotenv`
- Crie `.env`: `GEMINI_API_KEY=sua_chave_aqui`
- Primeiro commit: "Initial commit"

---

## 💡 Dicas Finais

1. **Comita diariamente** — Força disciplina, cria histórico
2. **Teste constantemente** — Roda seu agent, vê se responde
3. **Leia a docs** — Google AI documentação é sua bíblia
4. **Comunidade** — Reddit r/LanguageModels, Discord, GitHub discussions
5. **Não overthink** — Comece simples, evolua incrementalmente

---

**Você consegue. Bora construir um agent inteligente.**
