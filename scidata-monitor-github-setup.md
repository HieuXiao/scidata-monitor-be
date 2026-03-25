# 🔬 SciData Monitor — GitHub Repository Setup Guide

> **Project:** Global Research Intelligence Platform  
> **Focus:** Data Science × Radiogenomics  
> **Author:** Ngô Minh Hiếu  

---

## 📦 Overview: 2 Repositories

| Repository | Role | URL Convention |
|---|---|---|
| `scidata-monitor-fe` | React Frontend Dashboard | `github.com/<username>/scidata-monitor-fe` |
| `scidata-monitor-be` | FastAPI Backend + Data Pipeline | `github.com/<username>/scidata-monitor-be` |

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# REPOSITORY 1: scidata-monitor-fe (Frontend)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1.1 Repository Metadata

| Field | Value |
|---|---|
| **Name** | `scidata-monitor-fe` |
| **Description** | `Interactive research intelligence dashboard for SciData Monitor — built with React 18, TypeScript, and Sigma.js for collaboration graph visualization.` |
| **Visibility** | **Public** |
| **Reason** | Portfolio project; demonstrates frontend data visualization skills; no sensitive logic or API keys. |
| **Topics / Tags** | `react`, `typescript`, `vite`, `tailwindcss`, `shadcn-ui`, `data-visualization`, `sigmajs`, `recharts`, `tanstack-query`, `zustand`, `academic-research`, `portfolio` |

---

## 1.2 README.md — Frontend

```markdown
<div align="center">

  <img src="public/logo.svg" alt="SciData Monitor" width="80" />

  # SciData Monitor — Frontend

  **Interactive research intelligence dashboard for monitoring academic literature trends,
  author collaboration networks, and topic clusters in Data Science & Radiogenomics.**

  [![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)](https://reactjs.org/)
  [![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)](https://www.typescriptlang.org/)
  [![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?logo=vite)](https://vitejs.dev/)
  [![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-06B6D4?logo=tailwindcss)](https://tailwindcss.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  [Live Demo](https://scidata-monitor.vercel.app) · [Backend Repo](https://github.com/<username>/scidata-monitor-be) · [Report Bug](issues) · [Request Feature](issues)

</div>

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)

---

## Project Overview

SciData Monitor FE is the visual layer of the SciData Monitor platform. It provides:

- 📊 **Trend Dashboard** — Keyword growth charts over time using Recharts/Plotly.js
- 🕸️ **Collaboration Graph** — Interactive co-authorship networks rendered with Sigma.js + Graphology
- 🔍 **Topic Explorer** — Scatter plots of BERTopic-generated topic clusters
- 🏛️ **Institution Analytics** — Research output comparison across universities and labs
- 🔎 **Semantic Search** — Full-text search with real-time suggestions

---

## Tech Stack

| Category | Technology |
|---|---|
| Framework | React 18 + TypeScript |
| Build Tool | Vite 5 |
| Styling | Tailwind CSS 3 + shadcn/ui |
| Charts | Recharts + Plotly.js |
| Graph Viz | Sigma.js + Graphology |
| State Management | Zustand |
| Data Fetching | TanStack Query v5 (React Query) + Axios |
| Routing | React Router v6 |
| Testing | Vitest + React Testing Library |
| Linting | ESLint + Prettier |
| Deploy | Vercel |

---

## Getting Started

### Prerequisites

- Node.js >= 18.x
- npm >= 9.x (or pnpm/yarn)

### Installation

```bash
# 1. Clone repository
git clone https://github.com/<username>/scidata-monitor-fe.git
cd scidata-monitor-fe

# 2. Install dependencies
npm install

# 3. Copy environment variables
cp .env.example .env.local

# 4. Start development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Available Scripts

| Script | Description |
|---|---|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint |
| `npm run format` | Run Prettier |
| `npm run test` | Run unit tests |
| `npm run test:ui` | Run tests with Vitest UI |

---

## Folder Structure

```
scidata-monitor-fe/
├── public/
│   ├── logo.svg
│   └── favicon.ico
│
├── src/
│   ├── api/                    # Axios instances & API call functions
│   │   ├── axiosClient.ts      # Base axios config + interceptors
│   │   ├── papers.api.ts       # Papers & search endpoints
│   │   ├── authors.api.ts      # Author & network endpoints
│   │   ├── topics.api.ts       # Topic modeling endpoints
│   │   └── trends.api.ts       # Trend time-series endpoints
│   │
│   ├── assets/                 # Static assets (icons, images)
│   │
│   ├── components/
│   │   ├── ui/                 # shadcn/ui base components (auto-generated)
│   │   ├── charts/             # Reusable chart components
│   │   │   ├── TrendLineChart.tsx
│   │   │   ├── TopicScatterPlot.tsx
│   │   │   └── PublicationBarChart.tsx
│   │   ├── graph/              # Sigma.js graph components
│   │   │   ├── CollaborationGraph.tsx
│   │   │   ├── GraphControls.tsx
│   │   │   └── NodeTooltip.tsx
│   │   ├── layout/             # App shell components
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Topbar.tsx
│   │   │   └── PageWrapper.tsx
│   │   └── shared/             # Generic reusable UI components
│   │       ├── SearchBar.tsx
│   │       ├── FilterPanel.tsx
│   │       ├── StatCard.tsx
│   │       └── LoadingSpinner.tsx
│   │
│   ├── hooks/                  # Custom React hooks
│   │   ├── usePapers.ts        # TanStack Query hooks for papers
│   │   ├── useAuthorGraph.ts   # Graph data fetching hook
│   │   ├── useTopics.ts        # Topic cluster data hook
│   │   └── useTrends.ts        # Trend time-series hook
│   │
│   ├── pages/                  # Route-level page components
│   │   ├── DashboardPage.tsx   # Main overview dashboard
│   │   ├── TrendPage.tsx       # Keyword trend explorer
│   │   ├── TopicPage.tsx       # Topic cluster explorer
│   │   ├── NetworkPage.tsx     # Collaboration graph view
│   │   ├── SearchPage.tsx      # Full-text search results
│   │   └── NotFoundPage.tsx
│   │
│   ├── store/                  # Zustand global state stores
│   │   ├── filterStore.ts      # Active filters (year, topic, institution)
│   │   ├── graphStore.ts       # Graph selection state
│   │   └── searchStore.ts      # Search query state
│   │
│   ├── types/                  # TypeScript interfaces & enums
│   │   ├── paper.types.ts
│   │   ├── author.types.ts
│   │   ├── topic.types.ts
│   │   └── graph.types.ts
│   │
│   ├── utils/                  # Pure utility functions
│   │   ├── formatters.ts       # Date, number formatters
│   │   ├── graphTransform.ts   # Transform API data → Graphology format
│   │   └── colorScales.ts      # D3 color scale helpers
│   │
│   ├── constants/              # App-wide constants
│   │   ├── routes.ts
│   │   └── queryKeys.ts
│   │
│   ├── App.tsx                 # Root component with router
│   ├── main.tsx                # React DOM entry point
│   └── vite-env.d.ts
│
├── .env.example                # Example environment variables
├── .eslintrc.cjs
├── .prettierrc
├── .gitignore
├── index.html
├── package.json
├── tailwind.config.ts
├── tsconfig.json
├── vite.config.ts
└── README.md
```

---

## Environment Variables

Copy `.env.example` to `.env.local` and fill in the values:

```env
# === Backend API ===
VITE_API_BASE_URL=http://localhost:8000/api/v1

# === Feature Flags ===
VITE_ENABLE_GRAPH_ANALYTICS=true
VITE_ENABLE_SEMANTIC_SEARCH=false

# === Analytics (optional) ===
VITE_POSTHOG_KEY=
```

> ⚠️ Never commit `.env.local` — it is already in `.gitignore`.

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Quick summary:**
1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Commit using Conventional Commits: `feat: add topic scatter plot`
4. Push and open a Pull Request to `develop`

---

## License

MIT © 2026 Ngô Minh Hiếu
```

---

## 1.3 .gitignore — Frontend

```gitignore
# Dependencies
node_modules/
.pnp
.pnp.js

# Build outputs
dist/
dist-ssr/
build/

# Environment variables — NEVER commit these
.env
.env.local
.env.*.local
.env.production

# Logs
*.log
npm-debug.log*
yarn-debug.log*
pnpm-debug.log*

# Editor / OS
.DS_Store
Thumbs.db
.idea/
.vscode/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Testing
coverage/
.vitest-cache/

# Vite cache
.vite/

# TypeScript
*.tsbuildinfo
```

---

## 1.4 Folder Structure (Frontend) — Expanded Explanation

```
src/api/
  axiosClient.ts        → Base Axios instance: sets baseURL, timeout,
                          attaches JWT token from localStorage via interceptor,
                          handles 401 errors globally (redirect to /login)

src/components/graph/
  CollaborationGraph.tsx → Sigma.js canvas renderer; receives graphology Graph
                           object as prop; handles node hover → shows NodeTooltip
  GraphControls.tsx      → UI controls: zoom in/out, reset layout, filter by degree

src/hooks/
  useAuthorGraph.ts      → Calls GET /authors/{id}/graph, transforms response
                           using graphTransform.ts, returns graphology Graph

src/store/
  filterStore.ts         → Zustand store: { yearRange, selectedTopics,
                           selectedInstitution, setFilter, resetFilters }

src/utils/
  graphTransform.ts      → Converts API nodes/edges JSON into graphology
                           MultiGraph; assigns visual attributes (size, color)
                           based on citation_count and community_id
```

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# REPOSITORY 2: scidata-monitor-be (Backend)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 2.1 Repository Metadata

| Field | Value |
|---|---|
| **Name** | `scidata-monitor-be` |
| **Description** | `FastAPI backend for SciData Monitor — ETL pipelines, NLP topic modeling, co-authorship graph analytics, and REST API serving academic research intelligence.` |
| **Visibility** | **Public** |
| **Reason** | Portfolio; demonstrates data engineering, NLP pipeline design, and API architecture. Sensitive credentials managed via environment variables only. |
| **Topics / Tags** | `fastapi`, `python`, `postgresql`, `neo4j`, `celery`, `bertopic`, `spacy`, `networkx`, `data-pipeline`, `nlp`, `academic-research`, `radiogenomics`, `portfolio` |

---

## 2.2 README.md — Backend

```markdown
<div align="center">

  # SciData Monitor — Backend

  **FastAPI-powered research intelligence engine: ETL pipelines, NLP topic modeling,
  co-authorship graph construction, and REST API for academic data analysis.**

  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
  [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql)](https://postgresql.org/)
  [![Neo4j](https://img.shields.io/badge/Neo4j-AuraDB-008CC1?logo=neo4j)](https://neo4j.com/)
  [![Celery](https://img.shields.io/badge/Celery-5.x-37814A?logo=celery)](https://docs.celeryq.dev/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  [Frontend Repo](https://github.com/<username>/scidata-monitor-fe) · [API Docs](https://scidata-monitor-api.render.com/docs) · [Report Bug](issues)

</div>

---

## Project Overview

The SciData Monitor backend is a modular Python service providing:

- 🔄 **ETL Pipeline** — Automated ingestion from arXiv, PubMed, and OpenAlex APIs
- 🧠 **NLP Engine** — BERTopic topic modeling + spaCy NER on research abstracts
- 🕸️ **Graph Analytics** — Co-authorship network construction and centrality scoring in Neo4j
- 📈 **Trend Detection** — Time-series analysis of keyword growth using Prophet
- 🚀 **REST API** — FastAPI with async endpoints, JWT auth, and auto-generated Swagger docs
- ⚙️ **Task Queue** — Celery + Redis for background ML job processing

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.11+ |
| API Framework | FastAPI 0.111+ |
| ORM | SQLAlchemy 2.0 (async) |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Task Queue | Celery 5 + Redis |
| Scheduler | APScheduler |
| HTTP Client | httpx + asyncio |
| Auth | python-jose (JWT) + passlib |
| Relational DB | PostgreSQL 16 |
| Graph DB | Neo4j AuraDB (neo4j-driver) |
| Cache | Redis (Upstash) |
| NLP | spaCy 3, HuggingFace Transformers, BERTopic, sentence-transformers |
| Graph Analysis | NetworkX |
| Forecasting | Prophet |
| Data | pandas, numpy |
| Testing | pytest + pytest-asyncio + httpx |
| Deploy | Render / Railway + Docker |

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (recommended)
- PostgreSQL 16 (or use Docker)
- Redis (or use Docker)

### Option A: Docker Compose (Recommended)

```bash
# 1. Clone repo
git clone https://github.com/<username>/scidata-monitor-be.git
cd scidata-monitor-be

# 2. Copy env file
cp .env.example .env

# 3. Start all services (API, PostgreSQL, Redis, Celery worker)
docker-compose up --build

# API available at: http://localhost:8000
# Swagger docs:     http://localhost:8000/docs
```

### Option B: Local Setup

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run database migrations
alembic upgrade head

# 4. Start FastAPI server
uvicorn app.main:app --reload --port 8000

# 5. Start Celery worker (new terminal)
celery -A app.worker.celery_app worker --loglevel=info

# 6. Start Celery beat scheduler (new terminal)
celery -A app.worker.celery_app beat --loglevel=info
```

### Available Commands

| Command | Description |
|---|---|
| `uvicorn app.main:app --reload` | Dev server |
| `alembic upgrade head` | Apply migrations |
| `alembic revision --autogenerate -m "msg"` | Create new migration |
| `celery -A app.worker.celery_app worker` | Start Celery worker |
| `pytest` | Run all tests |
| `pytest --cov=app tests/` | Run tests with coverage |
| `python -m app.pipeline.run_ingestion` | Manually trigger ETL |

---

## Folder Structure

```
scidata-monitor-be/
│
├── app/
│   ├── api/                        # FastAPI route definitions
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py           # Aggregates all v1 routers
│   │   │   ├── papers.py           # GET /papers, GET /papers/{id}
│   │   │   ├── authors.py          # GET /authors/{id}/graph
│   │   │   ├── topics.py           # GET /topics, GET /topics/{id}/papers
│   │   │   ├── trends.py           # GET /trends?keyword=...
│   │   │   ├── search.py           # GET /search?q=...
│   │   │   └── health.py           # GET /health
│   │   └── deps.py                 # Dependency injection (DB session, auth)
│   │
│   ├── core/                       # App-wide configuration
│   │   ├── config.py               # Pydantic BaseSettings → reads from .env
│   │   ├── security.py             # JWT creation & verification
│   │   ├── logging.py              # Structured logging setup (structlog)
│   │   └── exceptions.py           # Custom HTTPException handlers
│   │
│   ├── db/                         # Database layer
│   │   ├── postgres/
│   │   │   ├── session.py          # Async SQLAlchemy engine & session factory
│   │   │   ├── base.py             # DeclarativeBase
│   │   │   └── models/             # ORM models
│   │   │       ├── paper.py        # Paper, Abstract, Keyword tables
│   │   │       ├── author.py       # Author, Affiliation tables
│   │   │       ├── institution.py  # Institution table
│   │   │       └── topic.py        # TopicCluster, TopicAssignment tables
│   │   └── neo4j/
│   │       ├── driver.py           # Neo4j async driver singleton
│   │       └── queries.py          # Cypher query functions
│   │
│   ├── schemas/                    # Pydantic v2 schemas (API request/response)
│   │   ├── paper.py
│   │   ├── author.py
│   │   ├── topic.py
│   │   ├── trend.py
│   │   └── graph.py                # Node/Edge schemas for graph API
│   │
│   ├── services/                   # Business logic layer
│   │   ├── paper_service.py        # CRUD + search logic
│   │   ├── author_service.py       # Author lookup + graph building
│   │   ├── topic_service.py        # Topic retrieval & cluster assignment
│   │   ├── trend_service.py        # Keyword time-series aggregation
│   │   └── graph_service.py        # NetworkX / Neo4j graph query logic
│   │
│   ├── pipeline/                   # ETL & Data Science pipeline modules
│   │   ├── ingestion/
│   │   │   ├── base_client.py      # Abstract base class for API clients
│   │   │   ├── arxiv_client.py     # arXiv OAI-PMH / API harvester
│   │   │   ├── pubmed_client.py    # PubMed E-Utilities harvester
│   │   │   └── openalex_client.py  # OpenAlex REST API harvester
│   │   │
│   │   ├── transform/
│   │   │   ├── cleaner.py          # Deduplication, null handling
│   │   │   ├── normalizer.py       # Author name, institution normalization
│   │   │   └── entity_resolver.py  # ORCID/ROR mapping
│   │   │
│   │   ├── nlp/
│   │   │   ├── preprocessor.py     # Text cleaning, tokenization
│   │   │   ├── ner_extractor.py    # spaCy NER for biomedical terms
│   │   │   ├── topic_modeler.py    # BERTopic model training & inference
│   │   │   └── embedder.py         # sentence-transformers embedding generation
│   │   │
│   │   ├── graph/
│   │   │   ├── builder.py          # Constructs NetworkX graph from co-authorship
│   │   │   ├── metrics.py          # Degree, betweenness, PageRank centrality
│   │   │   └── neo4j_loader.py     # Loads nodes/edges into Neo4j
│   │   │
│   │   ├── trends/
│   │   │   └── prophet_analyzer.py # Prophet forecasting on keyword time-series
│   │   │
│   │   └── run_ingestion.py        # CLI entry point for full pipeline run
│   │
│   ├── worker/
│   │   ├── celery_app.py           # Celery app configuration + Redis broker
│   │   ├── tasks/
│   │   │   ├── ingestion_tasks.py  # Celery tasks: trigger_arxiv_ingest, etc.
│   │   │   ├── nlp_tasks.py        # Celery tasks: run_topic_modeling, etc.
│   │   │   └── graph_tasks.py      # Celery tasks: rebuild_coauthor_graph
│   │   └── scheduler.py            # APScheduler periodic job definitions
│   │
│   ├── tests/
│   │   ├── conftest.py             # pytest fixtures (test DB, async client)
│   │   ├── unit/
│   │   │   ├── test_cleaner.py
│   │   │   ├── test_topic_modeler.py
│   │   │   └── test_graph_metrics.py
│   │   └── integration/
│   │       ├── test_papers_api.py
│   │       ├── test_authors_api.py
│   │       └── test_search_api.py
│   │
│   └── main.py                     # FastAPI app factory + middleware + routers
│
├── alembic/                        # Database migrations
│   ├── versions/
│   └── env.py
│
├── scripts/
│   ├── seed_data.py                # Seed DB with sample data for development
│   └── export_graph.py             # Export Neo4j graph to JSON for testing
│
├── docker-compose.yml              # Local dev: API + PostgreSQL + Redis
├── Dockerfile                      # Production Docker image
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt            # Dev-only: pytest, black, ruff, etc.
├── alembic.ini
├── pyproject.toml                  # Black, Ruff, mypy config
└── README.md
```

---

## Environment Variables

```env
# === App ===
APP_ENV=development               # development | staging | production
APP_DEBUG=true
SECRET_KEY=your-super-secret-key-change-this

# === PostgreSQL (Supabase) ===
DATABASE_URL=postgresql+asyncpg://user:password@host:5432/scidata

# === Neo4j AuraDB ===
NEO4J_URI=neo4j+s://xxxxxxxx.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-neo4j-password

# === Redis (Upstash) ===
REDIS_URL=redis://default:password@host:port

# === Celery ===
CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}

# === External APIs ===
PUBMED_API_KEY=your-pubmed-api-key
# arXiv and OpenAlex are free — no key required

# === NLP Models ===
SPACY_MODEL=en_core_sci_md        # scispaCy biomedical model
EMBEDDING_MODEL=all-MiniLM-L6-v2  # sentence-transformers model name

# === CORS ===
ALLOWED_ORIGINS=http://localhost:5173,https://scidata-monitor.vercel.app

# === Rate Limiting ===
PUBMED_REQUESTS_PER_SECOND=3
ARXIV_REQUESTS_PER_SECOND=1
OPENALEX_REQUESTS_PER_SECOND=10
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT © 2026 Ngô Minh Hiếu
```

---

## 2.3 .gitignore — Backend

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
*.egg
*.egg-info/
dist/
build/
.eggs/
.Python

# Virtual environments
.venv/
venv/
ENV/
env/

# Environment variables — NEVER commit
.env
.env.local
.env.*.local
.env.production
.env.staging

# Database
*.sqlite3
*.db

# ML Models — too large for Git, use Git LFS or external storage
models/
*.pkl
*.bin
*.safetensors
*.pt
*.onnx

# Logs
logs/
*.log

# Coverage
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Editor / OS
.DS_Store
Thumbs.db
.idea/
.vscode/
*.swp

# Docker volumes (if mounted locally)
postgres_data/
redis_data/

# Alembic (keep versions, ignore cache)
alembic/__pycache__/
```

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SHARED: Git & GitHub Conventions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Branch Strategy

```
main            ← Protected. Production-ready. Deploy triggers automatically.
develop         ← Integration branch. All features merge here first.
feature/*       ← New features (e.g. feature/collaboration-graph)
fix/*           ← Bug fixes (e.g. fix/neo4j-connection-timeout)
chore/*         ← Config, deps, docs (e.g. chore/update-dependencies)
release/*       ← Release preparation (e.g. release/v1.0.0)
```

**Rules:**
- `main` and `develop` are protected — no direct push
- All work happens on `feature/*` branches cut from `develop`
- PRs require at least 1 reviewer approval before merging into `develop`
- Merge `develop` → `main` only for releases via a `release/*` branch

---

## Commit Message Convention (Conventional Commits)

**Format:** `<type>(<scope>): <short description>`

```
feat(graph): add sigma.js co-authorship network renderer
fix(api): handle null abstract field in PubMed response
feat(pipeline): implement BERTopic topic modeling module
chore(deps): upgrade fastapi to 0.111.0
docs(readme): add environment variable table
refactor(service): extract graph centrality to separate module
test(api): add integration tests for /authors/{id}/graph
ci(github-actions): add pytest step to PR workflow
perf(db): add index on papers.publication_date column
style(fe): format with prettier
```

**Types:**
| Type | Use when |
|---|---|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring, no behavior change |
| `test` | Adding or fixing tests |
| `chore` | Dependency updates, config, tooling |
| `ci` | CI/CD pipeline changes |
| `perf` | Performance improvements |
| `style` | Formatting, whitespace (no logic change) |

---

## GitHub Repository Settings

### Labels (create these in both repos)

| Label | Color | Description |
|---|---|---|
| `type: feature` | `#0075ca` | New functionality |
| `type: bug` | `#d73a4a` | Something isn't working |
| `type: docs` | `#cfd3d7` | Documentation only |
| `type: refactor` | `#e4e669` | Code restructuring |
| `type: chore` | `#fef2c0` | Maintenance tasks |
| `priority: critical` | `#b60205` | Blocks release |
| `priority: high` | `#e99695` | Important |
| `priority: medium` | `#f9d0c4` | Normal |
| `priority: low` | `#fef2c0` | Nice to have |
| `status: in-progress` | `#0e8a16` | Being worked on |
| `status: blocked` | `#e4e669` | Waiting on external dependency |
| `status: needs-review` | `#006b75` | PR ready for review |
| `module: pipeline` | `#5319e7` | Data ingestion & ETL (BE) |
| `module: nlp` | `#5319e7` | NLP & topic modeling (BE) |
| `module: graph` | `#5319e7` | Graph analytics (BE/FE) |
| `module: api` | `#1d76db` | API endpoints |
| `module: ui` | `#1d76db` | Frontend components |

---

### Issue Templates

Create `.github/ISSUE_TEMPLATE/` folder with these files:

**`bug_report.md`:**
```markdown
---
name: Bug Report
about: Report a reproducible bug
labels: "type: bug"
---

## Bug Description
<!-- Clear description of the bug -->

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
<!-- What should happen -->

## Actual Behavior
<!-- What actually happens -->

## Environment
- OS: 
- Python/Node version: 
- Browser (if FE): 

## Logs / Screenshots
<!-- Paste relevant logs or attach screenshots -->
```

**`feature_request.md`:**
```markdown
---
name: Feature Request
about: Propose a new feature or enhancement
labels: "type: feature"
---

## Problem / Motivation
<!-- What problem does this feature solve? -->

## Proposed Solution
<!-- Describe your proposed solution -->

## Acceptance Criteria
- [ ] 
- [ ] 

## Additional Context
<!-- Mockups, references, related issues -->
```

---

### Pull Request Template

Create `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Summary
<!-- What does this PR do? Link related issue: Closes #<issue_number> -->

## Type of Change
- [ ] `feat` — New feature
- [ ] `fix` — Bug fix
- [ ] `refactor` — Code cleanup (no behavior change)
- [ ] `docs` — Documentation only
- [ ] `chore` — Dependency / config update
- [ ] `test` — Tests only

## Changes Made
<!-- Bullet points of key changes -->
- 
- 

## How to Test
<!-- Steps for the reviewer to test -->
1. 
2. 

## Checklist
- [ ] Code follows project conventions
- [ ] Self-reviewed my own code
- [ ] Added/updated relevant tests
- [ ] Docs updated (if applicable)
- [ ] No `.env` or secrets committed
- [ ] PR targets `develop` (not `main`)

## Screenshots (if UI change)
<!-- Before / After screenshots -->
```

---

### GitHub Actions CI/CD

**`.github/workflows/ci-fe.yml` (Frontend):**
```yaml
name: CI — Frontend

on:
  push:
    branches: [develop, main]
  pull_request:
    branches: [develop, main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run test -- --run
      - run: npm run build
```

**`.github/workflows/ci-be.yml` (Backend):**
```yaml
name: CI — Backend

on:
  push:
    branches: [develop, main]
  pull_request:
    branches: [develop, main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: testuser
          POSTGRES_PASSWORD: testpass
          POSTGRES_DB: scidata_test
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      redis:
        image: redis:7
        ports: ['6379:6379']

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: alembic upgrade head
        env:
          DATABASE_URL: postgresql+asyncpg://testuser:testpass@localhost:5432/scidata_test
      - run: pytest --cov=app tests/ --cov-report=xml
        env:
          DATABASE_URL: postgresql+asyncpg://testuser:testpass@localhost:5432/scidata_test
          REDIS_URL: redis://localhost:6379
```

---

## Quick Start Checklist

### Repository initialization (run for each repo):

```bash
# 1. Create on GitHub with the metadata above, then:
git clone https://github.com/<username>/scidata-monitor-fe.git
cd scidata-monitor-fe

# 2. Set up branch protection (do via GitHub web UI):
#    Settings → Branches → Add rule
#    Branch name: main and develop
#    ✅ Require pull request reviews (1 reviewer)
#    ✅ Require status checks to pass (CI workflow)
#    ✅ Restrict who can push to matching branches

# 3. Create initial commit structure
git checkout -b develop
# ... add all files ...
git add .
git commit -m "chore: initial project scaffold"
git push -u origin develop

# 4. Create main from develop
git checkout main
git merge develop
git push origin main
```

---

*Document generated: 2026 | SciData Monitor Project by Ngô Minh Hiếu*
