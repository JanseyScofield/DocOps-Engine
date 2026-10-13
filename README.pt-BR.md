# ⚙️ DocOps Engine

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.pt-BR.md"><b>🇧🇷 Português</b></a>
</p>

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Git Conflicts](https://img.shields.io/badge/Git-Zero%20Merge%20Conflicts-brightgreen.svg)]()
[![Documentation](https://img.shields.io/badge/Docs-Markdown%20%26%20DOCX-orange.svg)]()

> **DocOps Engine:** Uma solução completa, independente e reutilizável para **automação contínua da documentação técnica e arquitetural** em projetos de software orientados por IA e times ágeis.

---

## 🎯 Por que o DocOps Engine existe? (O Problema que ele resolve)

Em equipes com múltiplos desenvolvedores ou múltiplos agentes de inteligência artificial trabalhando em paralelo em branches Git separadas (ex: `feature/US-010` e `feature/US-025`), a documentação técnica centralizada tradicionalmente sofre com **conflitos frequentes de merge (`merge conflicts`)**.

O **DocOps Engine** implementa uma **Arquitetura de Documentação Modular Desacoplada**:
1. **Histórias de Usuário Isoladas (`historico_us/`)**: Cada entrega ou correção de bug é documentada em seu próprio arquivo individual (`US-XXX_slug.md`). O Git mescla novos arquivos automaticamente, gerando **ZERO conflito de merge**.
2. **Tópicos Arquiteturais Modulares (`topicos/`)**: Cada domínio técnico (Banco de Dados, Arquitetura, Setup) possui seu arquivo isolado.
3. **Compilador Automatizado (`scripts/main.py`)**: Reúne incrementalmente todos os módulos, gera a tabela de rastreabilidade e compila tanto o arquivo Markdown consolidado (Single Source of Truth para IA) quanto o documento oficial Microsoft Word (`.docx`) com estilização profissional e tipografia corporativa.
4. **Notificação Automática aos Stakeholders (`scripts/send_docs.py`)**: Disparo de e-mail com layout HTML corporativo contendo o resumo da entrega e o arquivo Word em anexo.

---

## 📁 Estrutura de Diretórios

```text
docops-engine/
├── .env.example                     # Modelo de variáveis de ambiente (copie para .env)
├── .gitignore                       # Regras de exclusão do Git (.env, .venv, etc.)
├── LICENSE                          # Licença MIT
├── README.md                        # Documentação em Inglês (Padrão do GitHub)
├── README.pt-BR.md                  # Documentação em Português
├── requirements.txt                 # Dependências Python (python-docx)
├── SKILL.md                         # Definição formal da skill para Agentes de IA
│
├── scripts/                         # Motor de automação em Python
│   ├── build_docs.py                # Compilador modular (Markdown -> DOCX estilizado)
│   ├── email_template.py            # Renderizador de e-mails (HTML e Texto Plano)
│   ├── load_env.py                  # Leitor nativo de variáveis de ambiente .env
│   ├── main.py                      # Ponto de entrada CLI (orquestrador)
│   ├── send_docs.py                 # Disparo de e-mail SMTP com anexo
│   └── templates/                   # Templates visuais desacoplados
│       └── email_notification.html  # Layout HTML responsivo com placeholders
│
└── documentacao/                    # Conteúdo da documentação do seu projeto
    ├── Technical_Documentation.md   # [Gerado] Markdown consolidado oficial
    ├── Technical_Documentation.docx # [Gerado] Word oficial estilizado
    │
    ├── topicos/                     # Tópicos arquiteturais isolados
    │   ├── 1_architecture.md        # Visão geral, camadas, ADRs
    │   ├── 2_database.md            # Modelagem, tabelas, migrações
    │   ├── 3_setup.md               # Pré-requisitos e setup do ambiente
    │   └── 4_skills.md              # Catálogo de ferramentas e IA
    │
    └── historico_us/                # Histórico de histórias de usuário (1 arquivo por US)
        └── US-001_initial_setup.md
```

---

## 🚀 Como Inicializar com Ambiente Virtual Python (`venv`)

Não é necessário utilizar Docker. A skill roda de forma 100% nativa com o interpretador Python.

### 1. Pré-requisitos
- **Python 3.10 ou superior** instalado na máquina.
- Git instalado.

### 2. Passo a Passo de Execução

#### Passo 2.1 — Criar o Ambiente Virtual (`venv`)
Abra o terminal na pasta do projeto e crie o ambiente virtual:

```bash
# Windows (PowerShell ou CMD)
python -m venv .venv

# Linux / macOS
python3 -m venv .venv
```

#### Passo 2.2 — Ativar o Ambiente Virtual

- **No Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Se o PowerShell bloquear a execução de scripts, execute uma única vez: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

- **No Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- **No Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

#### Passo 2.3 — Instalar as Dependências
Com o ambiente virtual ativado:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração das Variáveis de Ambiente (`.env`)

Copie o arquivo `.env.example` para `.env`:

```bash
# Windows (PowerShell)
Copy-Item .env.example .env

# Linux / macOS / Bash
cp .env.example .env
```

Abra o arquivo `.env` e configure suas preferências:

```ini
# Identificação do Projeto
PROJECT_NAME="Sistema de Exemplo"
DOC_TITLE="Documentação Técnica e Arquitetural"
OUTPUT_FILENAME="Technical_Documentation"
BRAND_COLOR="#005BAA"

# Identificação do Desenvolvedor Responsável
DEV_NAME="Seu Nome Completo"
DEV_EMAIL="seu.email@empresa.com.br"

# Servidor SMTP de Envio de E-mail
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu.email@empresa.com.br
SMTP_PASSWORD=sua_senha_de_aplicativo

# Stakeholders que receberão o aviso de documentação
DOC_EMAILS=lider.tecnico@empresa.com.br,product.owner@empresa.com.br
```

> ⚠️ **Dica de Segurança:** O arquivo `.env` nunca deve ser versionado no GitHub. Ele já está devidamente listado no `.gitignore`. Para envio via Gmail, gere uma **Senha de Aplicativo (App Password)** em sua Conta Google.

---

## 💻 Como Executar

Com o ambiente virtual ativado:

### 1. Apenas Compilar (Sem enviar e-mail) — Modo Ideal para Desenvolvimento Local
Utilize este comando durante o desenvolvimento ou refatoração interna de documentação:
```bash
python scripts/main.py --no-email
```
ou:
```bash
python scripts/main.py --skip-email
```

### 2. Compilar e Notificar Stakeholders por E-mail
Gera os arquivos `.md` e `.docx` e envia o relatório em HTML com o arquivo Word em anexo:
```bash
python scripts/main.py --send-email
```

### 3. Argumentos Opcionais do CLI
O script `main.py` oferece suporte a parâmetros adicionais:
- `--doc-dir <caminho>`: Especifica uma pasta personalizada contendo `topicos/` e `historico_us/`.
- `--output-name <nome>`: Modifica o nome do arquivo compilado gerado (ex: `--output-name Documentacao_Projeto_X`).
- `--project-name <nome>`: Altera o nome do projeto exibido nos cabeçalhos e no e-mail.

Exemplo:
```bash
python scripts/main.py --doc-dir "./minha-pasta-docs" --output-name "DocOficial" --no-email
```

---

## 🎨 Guia de Customização Completa (Cores, Mensagens e Estilo)

> 💡 **100% Flexível e Agnóstico:** Esta skill foi desenhada para se adaptar à identidade visual de qualquer empresa ou projeto pessoal. Você pode alterar cores corporativas, templates de e-mail e cabeçalhos em poucos segundos.

### 1. Como Alterar a Cor de Destaque da Sua Marca (`BRAND_COLOR`)
O projeto utiliza uma variável central de cor que estiliza automaticamente **tanto o documento Word (`.docx`) quanto o e-mail de notificação**.

No seu arquivo `.env`, altere o valor de `BRAND_COLOR`:
```ini
# Exemplo: Azul Corporativo
BRAND_COLOR="#005BAA"

# Outros exemplos comuns:
# BRAND_COLOR="#10B981"  # Verde Moderno / Fintech
# BRAND_COLOR="#6366F1"  # Roxo / Índigo Tech
# BRAND_COLOR="#FF6B00"  # Laranja Vibrante
# BRAND_COLOR="#0F172A"  # Slate / Dark Elegante
```

**Onde a cor é aplicada automaticamente:**
- **No Documento Word (`.docx`):** Cabeçalhos principais (`# H1` e `## H2`), títulos secundários (`### H3`) e fundo colorido da linha de títulos de todas as tabelas.
- **No E-mail HTML:** Banner superior, badges de identificação da US, borda lateral do box de destaque e botões de aviso.

---

### 2. Como Customizar as Mensagens e o Layout do E-mail
O layout do e-mail é completamente desacoplado do código Python e reside no arquivo:
📂 `scripts/templates/email_notification.html`

Você pode abrir esse arquivo em qualquer editor (como VS Code) e editá-lo diretamente com suporte completo a HTML e CSS.

#### 🏷️ Placeholders Disponíveis:
O script substitui dinamicamente os seguintes marcadores no template HTML:

| Placeholder | Descrição | Exemplo de Valor Preenchido |
|---|---|---|
| `{{PROJECT_NAME}}` | Nome configurado do projeto | `"Portal de Clientes"` |
| `{{BRAND_COLOR}}` | Cor hexadecimal da marca | `"#005BAA"` |
| `{{US_ID}}` | Identificador da entrega/US | `"US-010"` |
| `{{US_TITLE}}` | Título da funcionalidade | `"Integração com Gateway de Pagamento"` |
| `{{US_MODULE}}` | Módulo afetado | `"Financeiro"` |
| `{{US_GOAL}}` | Objetivo de negócio da entrega | `"Permitir cobrança via Pix e Cartão"` |
| `{{DEV_NAME}}` | Nome do desenvolvedor responsável | `"Jansey Scofield"` |
| `{{DEV_EMAIL}}` | E-mail do desenvolvedor | `"dev@empresa.com"` |
| `{{DATE_TIME}}` | Data e horário da compilação | `"2026-10-13 14:00"` |
| `{{DOCX_FILENAME}}` | Nome do arquivo Word em anexo | `"Technical_Documentation.docx"` |

#### ✍️ Como Inserir o Logotipo da Sua Empresa no E-mail:
Dentro de `scripts/templates/email_notification.html`, localize o bloco `.header` e adicione uma tag de imagem antes do título:
```html
<div class="header">
    <img src="https://sua-empresa.com/logo.png" alt="Logo" style="max-height: 40px; margin-bottom: 10px;" />
    <h1>Technical Documentation Update</h1>
    <p>{{PROJECT_NAME}}</p>
</div>
```

#### ✉️ Como Customizar a Mensagem em Texto Plano (Fallback):
Caso o destinatário utilize um leitor de e-mails em modo texto (sem suporte a HTML), a mensagem enviada pode ser personalizada diretamente no método `render_text()` do arquivo:
📂 `scripts/email_template.py`

---

### 3. Como Customizar Nomes de Projeto, Título e Arquivos de Saída
Você pode personalizar os nomes de exibição no `.env` ou diretamente via argumentos no terminal:

- **Via `.env`:**
  ```ini
  PROJECT_NAME="Meu Sistema ERP"
  DOC_TITLE="Documentação Oficial de Engenharia"
  OUTPUT_FILENAME="Manual_Tecnico_ERP"
  ```
- **Via Linha de Comando (CLI):**
  ```bash
  python scripts/main.py --project-name "Meu ERP" --output-name "Manual_Tecnico" --no-email
  ```
  Isso gerará os arquivos `Manual_Tecnico.md` e `Manual_Tecnico.docx` com os títulos customizados.

---

### 4. Como Customizar a Estrutura de Tópicos
A documentação aceita qualquer estrutura de módulos técnicos. Basta adicionar ou renomear arquivos em `documentacao/topicos/`:
- `1_visao_geral.md`
- `2_arquitetura_solucao.md`
- `3_modelo_dados.md`
- `4_seguranca_e_compliance.md`
- `5_apis_e_integracoes.md`

O compilador lê automaticamente todos os arquivos que começam com números (`[0-9]_*.md`) e os organiza em ordem crescente.

---

## 📝 Como Adicionar Novas Histórias de Usuário (`historico_us/`)

Para cada nova entrega, crie um arquivo com a convenção `US-XXX_slug.md` dentro de `documentacao/historico_us/`:

```markdown
### US-002: Implementação de Autenticação JWT
- **Status:** Concluído
- **Data de Conclusão:** 2026-10-13
- **Módulo:** Segurança / Autenticação
- **Responsável:** Maria Silva
- **Objetivo de Negócio:** Proteger os endpoints da API através de tokens assinados e renovação automática via refresh token.
- **Critérios de Aceite Atendidos:**
  - [x] Endpoint de login `/api/v1/auth/login` validando credenciais.
  - [x] Middleware de autorização aplicando validação de claims.
- **Alterações no Back-end:**
  - `src/Security/JwtTokenService.cs`: Geração e assinatura criptográfica dos tokens.
- **Alterações no Front-end:**
  - `src/services/api.ts`: Interceptor Axios para envio do Bearer token.
- **Testes Realizados & Validações:**
  - Cobertura de testes unitários atingida em 92%.
```

Ao rodar `python scripts/main.py`, a tabela geral de rastreabilidade é atualizada automaticamente com as informações desta nova US!

---

## 🤖 Como Reutilizar Esta Skill em Outros Projetos com IA

Esta pasta pode ser reaproveitada como uma **Skill de IA** em ferramentas como **Google Antigravity**, **Cursor AI**, **Claude Code**, **GitHub Copilot** ou **Windsurf**:

1. **Copiar os Arquivos:**
   Copie a pasta `scripts/`, a pasta `documentacao/` e o arquivo `SKILL.md` para a pasta de skills do seu projeto (por exemplo, `.ai/skills/documentacao/` ou `.cursor/skills/documentacao/`).

2. **O que Personalizar no `SKILL.md` para o seu Projeto (Checklist de Adaptação):**
   O arquivo `SKILL.md` já vem com uma seção dedicada no topo (`HOW TO ADAPT THIS SKILL FOR YOUR REPOSITORY`). Revise estes pontos:
   - **Caminho dos Scripts (Regra 3 e Passo 5):** Caso coloque os scripts em uma subpasta como `.ai/skills/documentacao/scripts/`, ajuste o comando no `SKILL.md` para refletir esse caminho (ex: `python .ai/skills/documentacao/scripts/main.py --no-email`).
   - **Módulos e Tópicos (Seção 1):** Ajuste os nomes dos tópicos em `documentacao/topicos/` para os domínios do seu projeto (ex: `1_architecture.md`, `2_database.md`, `3_apis.md`).
   - **Template de US (Seção 3):** Ajuste as pastas de alteração de código (`Backend Changes`, `Frontend Changes`, etc.) para os diretórios reais do seu projeto.
   - **Gatilho de Execução (Seção 4):** Defina se a documentação deve ser gerada automaticamente a cada US aprovada ou apenas antes de abrir um Pull Request.

3. **Comportamento Autônomo do Agente:**
   O agente de IA lerá o `SKILL.md` e saberá exatamente:
   - Que deve criar arquivos isolados em `documentacao/historico_us/US-XXX.md`.
   - Que nunca deve alterar arquivos de US de outros desenvolvedores (garantindo zero conflitos no Git).
   - Que deve compilar automaticamente a documentação ao finalizar cada tarefa através do comando `python scripts/main.py --no-email`.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
