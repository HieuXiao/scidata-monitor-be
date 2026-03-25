<div align="center">
  <br />

  <img src="https://github.com/user-attachments/assets/eab8f085-a4e2-45f2-a7d4-38ce0b6c7037" alt="SciData Monitor Logo" width="72" height="72" />

  <h1>SciData Monitor — Backend</h1>

  <p>
    FastAPI-powered research intelligence engine: automated ETL pipelines from arXiv & PubMed,<br />
    NLP topic modeling with BERTopic, co-authorship graph analytics via Neo4j,<br />
    and a fully async REST API serving the <strong>SciData Monitor</strong> dashboard.
  </p>

  <p>
    <a href="https://scidata-monitor-api.render.com/docs" target="_blank">
      <img src="https://img.shields.io/badge/API%20Docs-Swagger%20UI-009688?style=for-the-badge&logo=fastapi" alt="API Docs" />
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+" />
    <img src="https://img.shields.io/badge/FastAPI-0.111+-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL 16" />
    <img src="https://img.shields.io/badge/Neo4j-AuraDB-008CC1?style=flat-square&logo=neo4j&logoColor=white" alt="Neo4j AuraDB" />
    <img src="https://img.shields.io/badge/Celery-5.x-37814A?style=flat-square" alt="Celery" />
    <img src="https://img.shields.io/badge/Redis-7.x-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
    <img src="https://img.shields.io/badge/BERTopic-latest-FF6F00?style=flat-square" alt="BERTopic" />
    <img src="https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" alt="MIT License" />
  </p>

  <p>
    <a href="https://scidata-monitor-api.render.com/docs">API Docs (Swagger)</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/HieuXiao/scidata-monitor-fe">Frontend Repo</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/HieuXiao/scidata-monitor-be/issues">Report Bug</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/HieuXiao/scidata-monitor-be/issues">Request Feature</a>
  </p>

  <br />
</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
  - [Option A: Docker Compose](#option-a-docker-compose-recommended)
  - [Option B: Local Setup](#option-b-local-setup)
  - [Available Commands](#available-commands)
- [Folder Structure](#-folder-structure)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Data Pipeline](#-data-pipeline)
- [Data Science Modules](#-data-science-modules)
- [Database Design](#-database-design)
- [Background Tasks](#-background-tasks)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [Branch Strategy](#-branch-strategy)
- [Commit Convention](#-commit-convention)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🔬 Project Overview

SciData Monitor Backend is the data and intelligence engine of the [SciData Monitor](https://github.com/HieuXiao/scidata-monitor-fe) platform — a Global Research Intelligence Platform focused on **Data Science** and **Radiogenomics**.

The backend solves the information overload problem faced by researchers and students by:

1. **Automatically harvesting** structured metadata from arXiv, PubMed, and OpenAlex on a daily schedule
2. **Semantically analyzing** paper abstracts using NLP — extracting biomedical entities (spaCy NER) and grouping publications into coherent topic clusters (BERTopic)
3. **Building a knowledge graph** of co-authorship relationships stored in Neo4j, enabling collaboration network queries
4. **Serving all insights** through a fully async, documented REST API consumed by the React frontend

> 📄 For frontend dashboard and visualization documentation, see the [Frontend Repository](https://github.com/HieuXiao/scidata-monitor-fe).

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **🔄 ETL Pipeline** | Automated multi-source ingestion from arXiv (OAI-PMH), PubMed (E-Utilities), and OpenAlex (REST). Incremental loading with rate limiting and fault tolerance |
| **🧠 NLP Engine** | BERTopic topic modeling on paper abstracts; scispaCy NER for biomedical terms and methodology extraction; sentence-transformers for semantic embeddings |
| **🕸️ Graph Analytics** | Co-authorship network construction with NetworkX; centrality metrics (PageRank, betweenness, degree); graph stored and queried in Neo4j AuraDB |
| **📈 Trend Detection** | Prophet-based time-series forecasting on keyword frequency across publication years |
| **🔎 Semantic Search** | Vector similarity search over paper abstract embeddings |
| **⚙️ Task Queue** | Celery + Redis for long-running ML jobs (topic modeling, graph rebuild) as non-blocking background tasks |
| **🔐 Auth** | JWT-based authentication with `python-jose` and `passlib` |
| **📖 Auto Docs** | FastAPI auto-generates Swagger UI (`/docs`) and ReDoc (`/redoc`) from route definitions |

---

## 🛠️ Tech Stack

### Core API

| Technology | Version | Purpose |
|---|---|---|
| [Python](https://python.org/) | 3.11+ | Primary language |
| [FastAPI](https://fastapi.tiangolo.com/) | 0.111+ | Async web framework; auto OpenAPI docs |
| [Uvicorn](https://www.uvicorn.org/) | latest | ASGI server |
| [Pydantic v2](https://docs.pydantic.dev/latest/) | 2.x | Request/response validation and serialization |
| [python-jose](https://github.com/mpdavis/python-jose) | latest | JWT token creation and verification |
| [passlib](https://passlib.readthedocs.io/) | latest | Password hashing (bcrypt) |

### Data Layer

| Technology | Version | Purpose |
|---|---|---|
| [SQLAlchemy](https://www.sqlalchemy.org/) | 2.0 (async) | ORM for PostgreSQL with async support |
| [Alembic](https://alembic.sqlalchemy.org/) | latest | Database schema migration management |
| [asyncpg](https://magicstack.github.io/asyncpg/) | latest | Async PostgreSQL driver |
| [neo4j-driver](https://neo4j.com/developer/python/) | 5.x | Official Python driver for Neo4j AuraDB |
| [redis-py](https://github.com/redis/redis-py) | latest | Redis client (Celery broker + result backend) |

### Data Pipeline & NLP

| Technology | Version | Purpose |
|---|---|---|
| [httpx](https://www.python-httpx.org/) | latest | Async HTTP client for API ingestion |
| [APScheduler](https://apscheduler.readthedocs.io/) | 3.x | Cron-style scheduling for periodic ingestion |
| [Celery](https://docs.celeryq.dev/) | 5.x | Distributed task queue for background ML jobs |
| [spaCy](https://spacy.io/) + [scispaCy](https://allenai.github.io/scispacy/) | 3.x | NER for biomedical entities |
| [BERTopic](https://maartengr.github.io/BERTopic/) | latest | Neural topic modeling with BERT embeddings |
| [sentence-transformers](https://www.sbert.net/) | latest | Semantic text embeddings |
| [HuggingFace Transformers](https://huggingface.co/transformers/) | latest | Pre-trained language model loading |
| [NetworkX](https://networkx.org/) | 3.x | In-memory graph construction and centrality metrics |
| [Prophet](https://facebook.github.io/prophet/) | latest | Time-series forecasting for keyword trends |
| [pandas](https://pandas.pydata.org/) | 2.x | Data manipulation and transformation |
| [numpy](https://numpy.org/) | 1.x | Numerical operations |

### Testing & Code Quality

| Technology | Purpose |
|---|---|
| [pytest](https://pytest.org/) + [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) | Async unit and integration tests |
| [httpx](https://www.python-httpx.org/) | Async test client for FastAPI endpoints |
| [pytest-cov](https://pytest-cov.readthedocs.io/) | Test coverage reporting |
| [Ruff](https://docs.astral.sh/ruff/) | Extremely fast Python linter (replaces flake8/isort) |
| [Black](https://black.readthedocs.io/) | Opinionated code formatter |
| [mypy](https://mypy.readthedocs.io/) | Static type checking |

### Infrastructure & Deployment

| Service | Purpose |
|---|---|
| [Docker](https://www.docker.com/) + Docker Compose | Local dev environment and production image |
| [Render](https://render.com/) / [Railway](https://railway.app/) | Backend hosting (free tier eligible) |
| [Supabase](https://supabase.com/) | Managed PostgreSQL 16 |
| [Neo4j AuraDB](https://neo4j.com/cloud/platform/aura-graph-database/) | Managed graph database (free tier) |
| [Upstash Redis](https://upstash.com/) | Serverless Redis (Celery broker, free tier) |
| [GitHub Actions](https://github.com/features/actions) | CI: lint, type-check, and test on every PR |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        External Data Sources                         │
│   ┌──────────┐    ┌──────────────┐    ┌─────────────┐               │
│   │  arXiv   │    │    PubMed    │    │  OpenAlex   │               │
│   │ OAI-PMH  │    │ E-Utilities  │    │  REST API   │               │
│   └────┬─────┘    └──────┬───────┘    └──────┬──────┘               │
└────────┼─────────────────┼──────────────────┼──────────────────────┘
         │                 │                  │
         ▼                 ▼                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│                   Data Ingestion Layer (pipeline/)                   │
│                                                                      │
│   arxiv_client.py    pubmed_client.py    openalex_client.py          │
│         └──────────────────┬────────────────────┘                   │
│                            ▼                                         │
│              cleaner.py → normalizer.py → entity_resolver.py         │
│                            │                                         │
│              APScheduler (daily cron) + Celery tasks                 │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐
   │  PostgreSQL  │  │    Neo4j     │  │   Redis Cache    │
   │  (Supabase)  │  │  (AuraDB)    │  │   (Upstash)      │
   │              │  │              │  │                  │
   │  papers      │  │  (:Author)   │  │  API response    │
   │  authors     │  │  (:Institution│  │  cache (5 min)   │
   │  institutions│  │  [:CO_AUTHORED│  │                  │
   │  topics      │  │  [:AFFILIATED│  │  Celery broker   │
   │  trends      │  │              │  │  + result store  │
   └──────┬───────┘  └──────┬───────┘  └──────────────────┘
          │                 │
          └────────┬────────┘
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    FastAPI Application (app/)                        │
│                                                                      │
│   GET /api/v1/papers          ← Paper search & retrieval             │
│   GET /api/v1/topics          ← Topic cluster list & scatter data    │
│   GET /api/v1/authors/{id}/graph  ← Co-authorship graph (nodes+edges)│
│   GET /api/v1/trends          ← Keyword time-series data             │
│   GET /api/v1/search          ← Semantic full-text search            │
│   GET /api/v1/institutions    ← Research output analytics            │
│   POST /api/v1/auth/token     ← JWT login                            │
│                                                                      │
└─────────────────────────────┬────────────────────────────────────────┘
                              │ HTTP REST
                              ▼
                 ┌────────────────────────┐
                 │   scidata-monitor-fe   │
                 │   (React Dashboard)    │
                 └────────────────────────┘
```

### Medallion Architecture (Data Lake Pattern)

```
Raw API Response (JSON/XML)
        │
        ▼
🥉 BRONZE Layer  →  Raw JSON stored as-is. No transformation.
        │             Partitioned by source + date.
        ▼
🥈 SILVER Layer  →  Cleaned, deduplicated, normalized.
        │             Schema validated via Pydantic.
        ▼
🥇 GOLD Layer    →  Analytics-ready. Topic tags attached.
                      Author ORCID resolved. Ready for ML.
```

---

## 🚀 Getting Started

### Option A: Docker Compose (Recommended)

The fastest way to get the full stack running locally.

**Prerequisites:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

```bash
# 1. Clone repository
git clone https://github.com/HieuXiao/scidata-monitor-be.git
cd scidata-monitor-be

# 2. Copy environment variables
cp .env.example .env
# Edit .env with your Neo4j AuraDB credentials (see Environment Variables section)

# 3. Start all services
docker-compose up --build
```

This starts:

| Service | Port | Description |
|---|---|---|
| `api` | `8000` | FastAPI application |
| `postgres` | `5432` | PostgreSQL 16 database |
| `redis` | `6379` | Redis (Celery broker + cache) |
| `celery_worker` | — | Celery worker for background ML tasks |
| `celery_beat` | — | Celery beat scheduler for periodic ingestion |

**Verify the setup:**

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Interactive API docs
open http://localhost:8000/docs
```

**Useful Docker commands:**

```bash
# View logs for a specific service
docker-compose logs -f api
docker-compose logs -f celery_worker

# Run migrations inside container
docker-compose exec api alembic upgrade head

# Manually trigger ingestion pipeline
docker-compose exec api python -m app.pipeline.run_ingestion --source arxiv

# Stop all services
docker-compose down

# Stop and remove volumes (full reset)
docker-compose down -v
```

---

### Option B: Local Setup

For contributors who prefer running services natively.

**Prerequisites:**

- Python 3.11+ — verify with `python --version`
- PostgreSQL 16 running locally (or use a Supabase connection string)
- Redis 7 running locally (or use an Upstash connection string)

```bash
# 1. Clone repository
git clone https://github.com/HieuXiao/scidata-monitor-be.git
cd scidata-monitor-be

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# For development (adds pytest, ruff, black, mypy)
pip install -r requirements-dev.txt

# 4. Install spaCy biomedical model
python -m spacy download en_core_sci_md

# 5. Copy and configure environment variables
cp .env.example .env

# 6. Apply database migrations
alembic upgrade head

# 7. (Optional) Seed database with sample data
python scripts/seed_data.py

# 8. Start FastAPI development server
uvicorn app.main:app --reload --port 8000
```

**In separate terminals, start background workers:**

```bash
# Terminal 2 — Celery worker
celery -A app.worker.celery_app worker --loglevel=info --concurrency=2

# Terminal 3 — Celery beat (periodic scheduler)
celery -A app.worker.celery_app beat --loglevel=info
```

---

### Available Commands

| Command | Description |
|---|---|
| `uvicorn app.main:app --reload` | Start dev server with hot reload |
| `alembic upgrade head` | Apply all pending migrations |
| `alembic downgrade -1` | Roll back one migration |
| `alembic revision --autogenerate -m "description"` | Generate new migration from model changes |
| `celery -A app.worker.celery_app worker` | Start Celery worker |
| `celery -A app.worker.celery_app beat` | Start Celery beat scheduler |
| `celery -A app.worker.celery_app flower` | Start Flower task monitoring UI at `:5555` |
| `pytest` | Run all tests in watch mode |
| `pytest --cov=app tests/ --cov-report=html` | Run tests with HTML coverage report |
| `ruff check app/` | Lint the codebase |
| `ruff check app/ --fix` | Lint and auto-fix |
| `black app/` | Format code |
| `mypy app/` | Type check |
| `python -m app.pipeline.run_ingestion` | Manually run full ingestion pipeline |
| `python -m app.pipeline.run_ingestion --source arxiv --limit 500` | Run ingestion for one source |
| `python scripts/seed_data.py` | Seed DB with sample papers for development |
| `python scripts/export_graph.py` | Export Neo4j graph to JSON file |

---

## 📁 Folder Structure

```
scidata-monitor-be/
│
├── app/
│   │
│   ├── api/                              # FastAPI route definitions
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py                 # Aggregates all v1 sub-routers into one
│   │   │   ├── papers.py                 # GET /papers  GET /papers/{id}
│   │   │   │                             # Supports filters: year, topic, institution,
│   │   │   │                             # author; pagination via limit/offset
│   │   │   ├── authors.py                # GET /authors/{id}
│   │   │   │                             # GET /authors/{id}/graph
│   │   │   │                             # Returns { nodes, edges } for Sigma.js
│   │   │   ├── topics.py                 # GET /topics
│   │   │   │                             # GET /topics/{id}/papers
│   │   │   │                             # GET /topics/scatter  ← UMAP 2D points
│   │   │   ├── trends.py                 # GET /trends?keywords=x,y&year_start=2019
│   │   │   │                             # Returns time-series { date, count }[]
│   │   │   ├── search.py                 # GET /search?q=radiogenomics&limit=20
│   │   │   │                             # Full-text + optional semantic search
│   │   │   ├── institutions.py           # GET /institutions
│   │   │   │                             # GET /institutions/{id}/stats
│   │   │   ├── auth.py                   # POST /auth/token  ← JWT login
│   │   │   │                             # POST /auth/refresh
│   │   │   └── health.py                 # GET /health  ← liveness probe
│   │   └── deps.py                       # FastAPI Depends() providers:
│   │                                     # get_db_session(), get_current_user(),
│   │                                     # get_neo4j_driver(), get_redis_client()
│   │
│   ├── core/                             # Application-wide configuration
│   │   ├── config.py                     # Pydantic BaseSettings — reads all values
│   │   │                                 # from environment variables with type coercion
│   │   │                                 # and validation; singleton via @lru_cache
│   │   ├── security.py                   # create_access_token(), verify_token(),
│   │   │                                 # hash_password(), verify_password()
│   │   ├── logging.py                    # structlog setup: JSON logs in production,
│   │   │                                 # colored console logs in development
│   │   └── exceptions.py                 # Custom exception classes +
│   │                                     # @app.exception_handler() registrations
│   │                                     # for structured error responses
│   │
│   ├── db/
│   │   ├── postgres/
│   │   │   ├── session.py                # AsyncEngine + AsyncSessionLocal factory
│   │   │   │                             # get_async_session() async generator
│   │   │   ├── base.py                   # SQLAlchemy DeclarativeBase
│   │   │   └── models/
│   │   │       ├── paper.py              # Paper(id, doi, title, abstract, year,
│   │   │       │                         # source, source_id, created_at)
│   │   │       │                         # PaperKeyword(paper_id, keyword)
│   │   │       ├── author.py             # Author(id, name, orcid, affiliation_id)
│   │   │       │                         # PaperAuthor(paper_id, author_id, position)
│   │   │       ├── institution.py        # Institution(id, name, ror_id, country)
│   │   │       └── topic.py              # TopicCluster(id, label, keywords[])
│   │   │                                 # TopicAssignment(paper_id, topic_id, score)
│   │   └── neo4j/
│   │       ├── driver.py                 # Neo4j AsyncDriver singleton;
│   │       │                             # connect() called in app lifespan
│   │       └── queries.py                # Cypher query functions:
│   │                                     # get_author_subgraph(author_id, depth=2)
│   │                                     # get_institution_network(institution_id)
│   │                                     # get_top_authors_by_centrality(limit=50)
│   │
│   ├── schemas/                          # Pydantic v2 models — API contract
│   │   ├── paper.py                      # PaperSummary, PaperDetail, PapersListResponse
│   │   ├── author.py                     # AuthorProfile, AuthorBrief
│   │   ├── topic.py                      # TopicCluster, TopicScatterPoint
│   │   ├── trend.py                      # TrendDataPoint, KeywordTrendResponse
│   │   ├── graph.py                      # GraphNode, GraphEdge, GraphResponse
│   │   ├── institution.py                # InstitutionSummary, InstitutionStats
│   │   └── auth.py                       # TokenResponse, LoginRequest
│   │
│   ├── services/                         # Business logic — called by route handlers
│   │   ├── paper_service.py              # list_papers(filters, pagination),
│   │   │                                 # get_paper_by_id(id),
│   │   │                                 # search_papers(query, limit)
│   │   ├── author_service.py             # get_author_profile(id),
│   │   │                                 # build_author_graph(id, depth) → GraphResponse
│   │   ├── topic_service.py              # list_topics(), get_topic_papers(topic_id),
│   │   │                                 # get_scatter_data() → TopicScatterPoint[]
│   │   ├── trend_service.py              # get_keyword_trends(keywords, year_range)
│   │   │                                 # → TrendDataPoint[] per keyword
│   │   ├── institution_service.py        # list_institutions(), get_institution_stats(id)
│   │   └── graph_service.py              # Wraps neo4j/queries.py with error handling;
│   │                                     # converts Neo4j Record → GraphResponse schema
│   │
│   ├── pipeline/                         # ETL & Data Science — the intelligence core
│   │   │
│   │   ├── ingestion/                    # Data harvesting from external APIs
│   │   │   ├── base_client.py            # Abstract BaseAPIClient:
│   │   │   │                             # async fetch_batch(from_date, limit)
│   │   │   │                             # built-in rate limiter (asyncio.Semaphore)
│   │   │   │                             # and exponential backoff on 429/503
│   │   │   ├── arxiv_client.py           # arXiv OAI-PMH harvester + REST API client
│   │   │   │                             # Parses Atom XML response → RawPaper model
│   │   │   ├── pubmed_client.py          # PubMed E-Utilities (esearch + efetch)
│   │   │   │                             # Parses MEDLINE XML → RawPaper model
│   │   │   └── openalex_client.py        # OpenAlex Works API (cursor-based pagination)
│   │   │                                 # Maps OpenAlex schema → RawPaper model
│   │   │
│   │   ├── transform/                    # Data cleaning and standardization
│   │   │   ├── cleaner.py                # remove_html_tags(), normalize_whitespace(),
│   │   │   │                             # handle_missing_fields() — assigns defaults
│   │   │   │                             # instead of crashing on None fields
│   │   │   ├── normalizer.py             # normalize_author_name() (unicode → ASCII),
│   │   │   │                             # standardize_date_format() → ISO 8601,
│   │   │   │                             # detect_and_filter_language() via langdetect
│   │   │   └── entity_resolver.py        # resolve_author_orcid(name, affiliation)
│   │   │                                 # resolve_institution_ror(name, country)
│   │   │                                 # dedup_papers_by_doi(papers[]) — fingerprint
│   │   │                                 # comparison for DOI-less preprints
│   │   │
│   │   ├── nlp/                          # Natural Language Processing modules
│   │   │   ├── preprocessor.py           # clean_abstract() — removes LaTeX math,
│   │   │   │                             # special chars; sentence tokenization
│   │   │   ├── ner_extractor.py          # scispaCy NER pipeline:
│   │   │   │                             # extract_biomedical_entities(abstract)
│   │   │   │                             # → { DISEASE, GENE, CHEMICAL, METHOD }
│   │   │   ├── topic_modeler.py          # BERTopicModel wrapper:
│   │   │   │                             # train(abstracts[]) → saves model to disk
│   │   │   │                             # predict(abstract) → (topic_id, score)
│   │   │   │                             # get_topic_info() → topic labels + keywords
│   │   │   └── embedder.py               # SentenceTransformer wrapper:
│   │   │                                 # embed(texts[]) → np.ndarray (batch)
│   │   │                                 # Used for semantic search similarity
│   │   │
│   │   ├── graph/                        # Co-authorship graph construction
│   │   │   ├── builder.py                # build_coauthor_graph(papers[]):
│   │   │   │                             # Creates NetworkX MultiGraph where
│   │   │   │                             # nodes = authors, edges = shared papers
│   │   │   │                             # edge weight = number of shared papers
│   │   │   ├── metrics.py                # compute_centrality(graph):
│   │   │   │                             # PageRank, betweenness_centrality,
│   │   │   │                             # degree_centrality → dict[author_id, score]
│   │   │   └── neo4j_loader.py           # load_graph_to_neo4j(graph):
│   │   │                                 # MERGE (:Author) and (:Institution) nodes
│   │   │                                 # MERGE [:CO_AUTHORED] and [:AFFILIATED] edges
│   │   │                                 # Uses batched Cypher UNWIND for performance
│   │   │
│   │   ├── trends/
│   │   │   └── prophet_analyzer.py       # analyze_keyword_trend(keyword, df):
│   │   │                                 # Fits Prophet model on yearly paper counts;
│   │   │                                 # returns historical + 3-year forecast
│   │   │
│   │   └── run_ingestion.py              # CLI entry point:
│   │                                     # python -m app.pipeline.run_ingestion
│   │                                     # --source [arxiv|pubmed|openalex|all]
│   │                                     # --limit N  --from-date YYYY-MM-DD
│   │
│   ├── worker/                           # Celery async task definitions
│   │   ├── celery_app.py                 # Celery() instance with Redis broker config;
│   │   │                                 # task serialization: JSON
│   │   │                                 # worker_prefetch_multiplier = 1 (ML tasks)
│   │   ├── tasks/
│   │   │   ├── ingestion_tasks.py        # @celery_app.task trigger_arxiv_ingest()
│   │   │   │                             # trigger_pubmed_ingest()
│   │   │   │                             # trigger_openalex_ingest()
│   │   │   ├── nlp_tasks.py              # @celery_app.task run_topic_modeling()
│   │   │   │                             # Trains BERTopic on all unprocessed abstracts
│   │   │   │                             # Updates topic_assignments table on completion
│   │   │   └── graph_tasks.py            # @celery_app.task rebuild_coauthor_graph()
│   │   │                                 # Calls builder.py → metrics.py → neo4j_loader
│   │   └── scheduler.py                  # APScheduler job registration:
│   │                                     # arXiv/PubMed ingest: daily at 02:00 UTC
│   │                                     # Topic modeling: weekly (Sunday 03:00 UTC)
│   │                                     # Graph rebuild: weekly (Sunday 04:00 UTC)
│   │
│   ├── tests/
│   │   ├── conftest.py                   # pytest fixtures:
│   │   │                                 # async_client (httpx.AsyncClient)
│   │   │                                 # test_db_session (uses separate test DB)
│   │   │                                 # mock_neo4j_driver
│   │   ├── unit/
│   │   │   ├── test_cleaner.py           # Tests for transform/cleaner.py functions
│   │   │   ├── test_normalizer.py        # Tests for author name / date normalization
│   │   │   ├── test_entity_resolver.py   # Tests for ORCID / ROR resolution logic
│   │   │   ├── test_topic_modeler.py     # Tests BERTopic wrapper with mock model
│   │   │   ├── test_graph_metrics.py     # Tests centrality computation on known graph
│   │   │   └── test_graph_builder.py     # Tests co-authorship edge construction
│   │   └── integration/
│   │       ├── test_papers_api.py        # Tests GET /papers with filter combinations
│   │       ├── test_authors_api.py       # Tests GET /authors/{id}/graph response shape
│   │       ├── test_topics_api.py        # Tests GET /topics/scatter data format
│   │       ├── test_trends_api.py        # Tests GET /trends time-series output
│   │       └── test_search_api.py        # Tests GET /search pagination + scoring
│   │
│   └── main.py                           # FastAPI app factory:
│                                         # lifespan() — startup: DB connect, load models
│                                         #               shutdown: close connections
│                                         # CORS middleware with ALLOWED_ORIGINS
│                                         # Include router at /api/v1
│                                         # Register exception handlers
│
├── alembic/
│   ├── versions/                         # Auto-generated migration files
│   │   └── 001_initial_schema.py
│   └── env.py                            # Alembic env with async SQLAlchemy support
│
├── scripts/
│   ├── seed_data.py                      # Inserts ~100 sample papers, authors,
│   │                                     # institutions for local development
│   └── export_graph.py                   # Exports Neo4j graph as JSON
│                                         # for frontend Sigma.js mock data
│
├── docs/
│   └── assets/
│       └── logo.svg
│
├── docker-compose.yml                    # Local dev: api + postgres + redis + workers
├── Dockerfile                            # Multi-stage: builder + slim runtime image
├── .env.example                          # Environment variable template
├── .gitignore                            # Python template + custom additions
├── requirements.txt                      # Production dependencies (pinned versions)
├── requirements-dev.txt                  # Dev-only: pytest, ruff, black, mypy, httpx
├── alembic.ini                           # Alembic configuration
├── pyproject.toml                        # Tool config: Black, Ruff, mypy, pytest
└── README.md
```

---

## 🔐 Environment Variables

Copy `.env.example` to `.env` for local development. For production, set these as environment variables on Render/Railway.

```env
# ─────────────────────────────────────────────
# Application
# ─────────────────────────────────────────────

# Runtime environment: development | staging | production
APP_ENV=development

# Enable verbose debug logging and auto-reload
APP_DEBUG=true

# Secret key for JWT signing — use a long random string in production
# Generate: python -c "import secrets; print(secrets.token_hex(32))"
SECRET_KEY=change-this-to-a-long-random-secret-key-in-production

# JWT token expiry in minutes (default: 30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Allowed origins for CORS (comma-separated)
ALLOWED_ORIGINS=http://localhost:5173,https://scidata-monitor.vercel.app

# ─────────────────────────────────────────────
# PostgreSQL (Supabase or local Docker)
# ─────────────────────────────────────────────

# asyncpg driver prefix required for SQLAlchemy async
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/scidata

# Connection pool settings
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20

# ─────────────────────────────────────────────
# Neo4j AuraDB
# ─────────────────────────────────────────────

# Connection URI from Neo4j AuraDB console
NEO4J_URI=neo4j+s://xxxxxxxx.databases.neo4j.io

# AuraDB credentials
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-aura-db-password

# ─────────────────────────────────────────────
# Redis (Upstash or local Docker)
# ─────────────────────────────────────────────

# Used as Celery broker, result backend, and API response cache
REDIS_URL=redis://default:password@localhost:6379/0

# API response cache TTL in seconds (default: 300 = 5 minutes)
REDIS_CACHE_TTL=300

# ─────────────────────────────────────────────
# Celery
# ─────────────────────────────────────────────

CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}

# Max concurrent ML tasks per worker (keep low — BERTopic is memory-intensive)
CELERY_WORKER_CONCURRENCY=2

# ─────────────────────────────────────────────
# External Data Source APIs
# ─────────────────────────────────────────────

# PubMed E-Utilities API key (free — increases rate limit from 3 to 10 req/s)
# Register at: https://www.ncbi.nlm.nih.gov/account/
PUBMED_API_KEY=your-pubmed-api-key

# arXiv API — no key required (public access)
# OpenAlex API — no key required; add email for polite pool (higher rate limit)
OPENALEX_EMAIL=your-email@example.com

# ─────────────────────────────────────────────
# Rate Limiting (requests per second per source)
# ─────────────────────────────────────────────

PUBMED_RPS=10          # 10/s with API key, 3/s without
ARXIV_RPS=1            # arXiv terms of service: max 1 req/s
OPENALEX_RPS=10        # Polite pool: 10/s with email set

# ─────────────────────────────────────────────
# NLP Models
# ─────────────────────────────────────────────

# scispaCy biomedical NER model (must be downloaded separately)
# Run: python -m spacy download en_core_sci_md
SPACY_MODEL=en_core_sci_md

# sentence-transformers model for semantic embeddings
# Downloaded automatically on first run from HuggingFace Hub
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Directory to persist trained BERTopic model (local or mounted volume)
TOPIC_MODEL_PATH=./models/bertopic_model

# ─────────────────────────────────────────────
# Pipeline Scheduling (cron expressions)
# ─────────────────────────────────────────────

# Daily ingestion from arXiv and PubMed (02:00 UTC)
INGEST_CRON=0 2 * * *

# Weekly topic model re-training (Sunday 03:00 UTC)
TOPIC_MODEL_CRON=0 3 * * 0

# Weekly graph rebuild in Neo4j (Sunday 04:00 UTC)
GRAPH_REBUILD_CRON=0 4 * * 0
```

> ⚠️ **Security:** Never commit `.env` to Git. The `.gitignore` already excludes it. Only commit `.env.example` with placeholder values and no real credentials.

---

## 📡 API Reference

Full interactive documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc) when the server is running.

### Base URL

```
Local:       http://localhost:8000/api/v1
Production:  https://scidata-monitor-api.render.com/api/v1
```

### Endpoints Overview

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/health` | Liveness probe — returns service status | No |
| `POST` | `/auth/token` | Login and receive JWT access token | No |
| `GET` | `/papers` | List papers with filters and pagination | No |
| `GET` | `/papers/{id}` | Get full detail of a single paper | No |
| `GET` | `/authors/{id}` | Get author profile | No |
| `GET` | `/authors/{id}/graph` | Get co-authorship subgraph (nodes + edges) | No |
| `GET` | `/topics` | List all topic clusters with labels | No |
| `GET` | `/topics/{id}/papers` | List papers assigned to a topic cluster | No |
| `GET` | `/topics/scatter` | Get UMAP 2D scatter data for all papers | No |
| `GET` | `/trends` | Get keyword frequency time-series | No |
| `GET` | `/search` | Full-text semantic search across papers | No |
| `GET` | `/institutions` | List institutions ranked by output | No |
| `GET` | `/institutions/{id}/stats` | Get detailed stats for one institution | No |

### Example Requests

**List papers filtered by topic and year range:**

```bash
curl "http://localhost:8000/api/v1/papers?topic_id=3&year_start=2021&year_end=2024&limit=20&offset=0"
```

**Get co-authorship subgraph for an author:**

```bash
curl "http://localhost:8000/api/v1/authors/a1b2c3d4/graph?depth=2&min_papers=2"
```

Response shape consumed by Sigma.js on the frontend:

```json
{
  "author_id": "a1b2c3d4",
  "nodes": [
    {
      "id": "a1b2c3d4",
      "label": "Nguyen Van A",
      "institution": "VNU Hanoi",
      "paper_count": 42,
      "citation_count": 310,
      "community_id": 2
    }
  ],
  "edges": [
    {
      "source": "a1b2c3d4",
      "target": "b2c3d4e5",
      "weight": 7
    }
  ]
}
```

**Keyword trend time-series:**

```bash
curl "http://localhost:8000/api/v1/trends?keywords=radiogenomics,deep+learning&year_start=2018&year_end=2024"
```

```json
{
  "keywords": [
    {
      "keyword": "radiogenomics",
      "series": [
        { "year": 2018, "count": 12 },
        { "year": 2019, "count": 18 },
        { "year": 2020, "count": 27 }
      ]
    }
  ]
}
```

---

## 🔄 Data Pipeline

### Ingestion Sources

| Source | Protocol | Update Freq | Coverage |
|---|---|---|---|
| **arXiv** | OAI-PMH + REST API | Daily | CS, AI, Statistics, Math preprints |
| **PubMed / MEDLINE** | E-Utilities API | Daily | Biomedical & clinical literature |
| **OpenAlex** | REST API (cursor pagination) | Weekly | Cross-discipline; citation data; institution metadata |
| **Crossref** | REST API (on-demand) | On-demand | DOI metadata, funding information |
| **ORCID** | Public API | Monthly | Researcher profiles and ID disambiguation |

### ETL Flow

```
1. Extract   → arxiv_client / pubmed_client / openalex_client
               Rate-limited async fetch in batches of 500 records
               Incremental: only records updated since last run

2. Transform → cleaner.py
               - Strip HTML / LaTeX artifacts from abstracts
               - Assign NULL for missing optional fields (do not crash)
               - Filter non-English papers (langdetect)

               normalizer.py
               - Normalize author name encoding (unicode → NFC)
               - Standardize dates to ISO 8601 (YYYY-MM-DD)

               entity_resolver.py
               - Map author names to ORCID IDs
               - Map institution names to ROR IDs
               - Deduplicate papers by DOI fingerprint

3. Load      → PostgreSQL (Supabase)
               SQLAlchemy bulk insert with ON CONFLICT DO NOTHING
               Index on: doi, source_id, year, topic_id

4. Enrich    → nlp/ner_extractor.py
               scispaCy NER: tag each abstract with entity types

               nlp/topic_modeler.py
               BERTopic inference: assign topic_id + score to each paper

5. Graph     → graph/builder.py + graph/neo4j_loader.py
               Build co-authorship edges from PaperAuthor table
               MERGE nodes and edges into Neo4j AuraDB
```

### Fault Tolerance

- Individual record failures are logged and skipped — the batch continues
- Failed Celery tasks are retried up to 3 times with exponential backoff
- API 429 responses trigger automatic backoff + resume using `asyncio` `Semaphore`
- Missing required fields (title, year) → paper is skipped with a warning log
- Missing optional fields (abstract, institution) → assigned `NULL` / empty default

---

## 🧠 Data Science Modules

### Topic Modeling — BERTopic

BERTopic is used to automatically cluster paper abstracts into coherent research topics without requiring manual label definitions.

**Pipeline:**

```
Paper abstracts
      │
      ▼
sentence-transformers (all-MiniLM-L6-v2)
      │  Generates dense 384-dim embeddings
      ▼
UMAP (dim reduction: 384 → 5)
      │  Preserves local + global structure
      ▼
HDBSCAN (density-based clustering)
      │  Finds clusters of similar papers
      ▼
c-TF-IDF (topic label extraction)
      │  Extracts representative keywords per cluster
      ▼
Topic labels: { "radiogenomics", "GAN image synthesis", "federated learning", ... }
```

**Key decisions:**

- Model is trained weekly (not daily) — training on ~50k abstracts takes ~20 min
- Inference (predict topic for new paper) runs in <100ms per paper
- UMAP 2D projection (separate from clustering UMAP) is stored for the scatter plot
- Model artifact is persisted to `TOPIC_MODEL_PATH` and loaded on worker startup

### Named Entity Recognition — spaCy + scispaCy

`en_core_sci_md` (scispaCy biomedical model) is used to extract domain entities from abstracts:

| Entity Type | Examples |
|---|---|
| `DISEASE` | carcinoma, glioblastoma, NSCLC |
| `GENE_OR_GENE_PRODUCT` | BRCA1, TP53, EGFR |
| `CHEMICAL` | cisplatin, gadolinium |
| `CANCER` | lung cancer, breast cancer |

Extracted entities are stored as paper keywords and used to power filtered search.

### Graph Analytics — NetworkX + Neo4j

**Construction:** For each paper with N authors, N×(N-1)/2 co-authorship edges are created (complete subgraph). Edge weight = number of papers shared.

**Centrality metrics computed:**

| Metric | Interpretation |
|---|---|
| `PageRank` | Overall influence in the collaboration network |
| `Betweenness Centrality` | Acts as bridge between research communities |
| `Degree Centrality` | Number of direct collaborators |

Centrality scores are stored in PostgreSQL and used to size nodes in the Sigma.js graph (higher PageRank → larger node).

### Trend Detection — Prophet

For each tracked keyword, a yearly paper count time-series is fitted to a Prophet model. The API returns both historical data and a 3-year forecast with confidence intervals.

---

## 🗄️ Database Design

### PostgreSQL Schema (simplified)

```sql
-- Core tables
papers         (id, doi, title, abstract, year, source, source_id, created_at)
authors        (id, name, orcid, affiliation_id)
institutions   (id, name, ror_id, country, city)
topic_clusters (id, label, keywords[], created_at)

-- Relationship tables
paper_authors      (paper_id, author_id, author_position)
paper_keywords     (paper_id, keyword, entity_type)
topic_assignments  (paper_id, topic_id, score)

-- Analytics tables
keyword_trends  (keyword, year, count, updated_at)
```

### Neo4j Schema

```cypher
-- Nodes
(:Author   { id, name, orcid, paper_count, pagerank_score })
(:Institution { id, name, ror_id, country })

-- Relationships
(:Author)-[:CO_AUTHORED { weight: int, papers: [doi] }]->(:Author)
(:Author)-[:AFFILIATED_WITH { since_year: int }]->(:Institution)
```

---

## ⚙️ Background Tasks

Long-running operations (NLP training, graph rebuild) are offloaded to Celery workers to prevent blocking the API.

| Task | Trigger | Duration (est.) | Description |
|---|---|---|---|
| `trigger_arxiv_ingest` | Daily 02:00 UTC | ~5 min | Fetch and store new arXiv papers |
| `trigger_pubmed_ingest` | Daily 02:30 UTC | ~8 min | Fetch and store new PubMed papers |
| `run_topic_modeling` | Weekly Sun 03:00 UTC | ~20 min | Retrain BERTopic on all abstracts |
| `rebuild_coauthor_graph` | Weekly Sun 04:00 UTC | ~10 min | Rebuild NetworkX graph → push to Neo4j |

**Monitor tasks** with Celery Flower:

```bash
celery -A app.worker.celery_app flower
# Open: http://localhost:5555
```

---

## 🧪 Testing

Tests are organized into **unit** (fast, no DB) and **integration** (requires test DB + Redis).

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app tests/ --cov-report=html
open htmlcov/index.html

# Run only unit tests (fast, no external dependencies)
pytest tests/unit/

# Run only integration tests
pytest tests/integration/

# Run a specific test file
pytest tests/unit/test_topic_modeler.py -v

# Run tests matching a pattern
pytest -k "test_graph" -v
```

**Test database** is a separate PostgreSQL database (`scidata_test`) created automatically via the `conftest.py` fixture. It is dropped and recreated for each test session.

**Coverage targets:**

| Module | Target |
|---|---|
| `app/api/` | > 90% |
| `app/services/` | > 85% |
| `app/pipeline/transform/` | > 95% |
| `app/pipeline/nlp/` | > 70% |
| `app/pipeline/graph/` | > 80% |

---

## 🚢 Deployment

### Backend — Render (recommended free tier)

```yaml
# render.yaml (add to repo root for Infrastructure as Code)
services:
  - type: web
    name: scidata-monitor-api
    runtime: python
    buildCommand: pip install -r requirements.txt && alembic upgrade head
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: APP_ENV
        value: production
      - key: DATABASE_URL
        fromDatabase:
          name: scidata-postgres
          property: connectionString
      - key: SECRET_KEY
        generateValue: true

  - type: worker
    name: scidata-celery-worker
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: celery -A app.worker.celery_app worker --loglevel=info
```

### Database — Supabase (PostgreSQL)

1. Create project at [supabase.com](https://supabase.com)
2. Copy the **Transaction pooler** connection string (port 6543)
3. Set as `DATABASE_URL` in Render environment variables

### Graph DB — Neo4j AuraDB (Free tier)

1. Create a Free instance at [neo4j.com/cloud/aura](https://neo4j.com/cloud/aura/)
2. Copy the connection URI and credentials
3. Set `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`

### Cache / Broker — Upstash Redis (Free tier)

1. Create database at [upstash.com](https://upstash.com)
2. Copy the `REDIS_URL` (TLS-enabled URL)
3. Set as `REDIS_URL` and let `CELERY_BROKER_URL=${REDIS_URL}` inherit it

### Docker (Production Image)

```bash
# Build production image
docker build -t scidata-monitor-be:latest .

# Run with production env
docker run -p 8000:8000 --env-file .env scidata-monitor-be:latest
```

---

## 🤝 Contributing

### 1. Fork & Clone

```bash
git clone https://github.com/HieuXiao/scidata-monitor-be.git
cd scidata-monitor-be
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 2. Create a Feature Branch

Always branch from `develop`:

```bash
git checkout develop && git pull origin develop
git checkout -b feature/your-feature-name
```

### 3. Make Changes and Validate

Before committing, ensure all checks pass:

```bash
ruff check app/          # Linting must pass
black --check app/       # Formatting must be clean
mypy app/                # Type checking must pass
pytest tests/unit/ -v    # Unit tests must pass
```

### 4. Commit and Push

```bash
git commit -m "feat(pipeline): add OpenAlex citation graph ingestion"
git push origin feature/your-feature-name
```

### 5. Open a Pull Request

- Target: **`develop`** — never `main` directly
- Fill in the PR template
- Ensure all CI checks pass

### Code Style Rules

- All functions must have **type annotations** on parameters and return values
- Use `async def` for any function that does I/O (DB queries, HTTP calls, file reads)
- Pydantic schemas are used for **all** API input and output — never raw `dict`
- Services must not import from `api/` — dependency flow: `api → services → db`
- Pipeline modules must not import from `api/` or `services/` — they are independent
- All database queries go through SQLAlchemy ORM or raw `text()` — no raw string interpolation
- Secrets are accessed only via `get_settings()` from `core/config.py` — never `os.environ` directly

---

## 🌿 Branch Strategy

```
main
  └── develop
        ├── feature/openalex-ingestion
        ├── feature/bertopic-topic-modeling
        ├── fix/pubmed-xml-parsing-edge-case
        ├── chore/upgrade-sqlalchemy-2.0
        └── release/v1.1.0
```

| Branch | Purpose | Merge target | Direct push |
|---|---|---|---|
| `main` | Production | — | ❌ Protected |
| `develop` | Integration | `main` via release | ❌ Protected |
| `feature/*` | New features | `develop` | ✅ |
| `fix/*` | Bug fixes | `develop` | ✅ |
| `chore/*` | Deps, config, docs | `develop` | ✅ |
| `release/*` | Release prep | `main` + `develop` | ✅ |

---

## 📝 Commit Convention

Format: `<type>(<scope>): <short imperative description>`

```bash
feat(pipeline): add OpenAlex cursor-based pagination for full dataset harvest
fix(pubmed): handle missing MeSH terms field in E-Utilities XML response
feat(nlp): implement BERTopic weekly retraining Celery task
fix(api): return 404 instead of 500 when author graph node not found in Neo4j
refactor(services): extract graph node scoring to dedicated centrality module
test(api): add integration tests for GET /trends with multiple keywords
chore(deps): pin sqlalchemy to 2.0.30 for async compatibility
ci(github-actions): add mypy type-check step to PR workflow
docs(readme): add data pipeline section with medallion architecture diagram
perf(db): add composite index on (paper_id, topic_id) for faster joins
```

**Scope values** for this repo: `pipeline`, `nlp`, `graph`, `api`, `services`, `db`, `worker`, `auth`, `config`, `deps`, `ci`, `docs`

---

## 🗓️ Roadmap

### v1.0.0 — Foundation (Current)
- [x] FastAPI project scaffold with async SQLAlchemy + Alembic
- [x] Pydantic v2 schemas for all API contracts
- [x] JWT authentication
- [x] Docker Compose for local development
- [ ] arXiv and PubMed ingestion clients
- [ ] Database seed script
- [ ] Core API endpoints: `/papers`, `/health`

### v1.1.0 — NLP Pipeline
- [ ] scispaCy NER entity extraction
- [ ] BERTopic topic modeling + weekly retraining task
- [ ] sentence-transformers abstract embeddings
- [ ] `/topics` and `/topics/scatter` endpoints

### v1.2.0 — Graph Analytics
- [ ] Co-authorship graph construction (NetworkX)
- [ ] Centrality metric computation
- [ ] Neo4j AuraDB loader
- [ ] `/authors/{id}/graph` endpoint with depth parameter

### v1.3.0 — Trends & Search
- [ ] OpenAlex integration for citation data
- [ ] Prophet keyword trend forecasting
- [ ] `/trends` endpoint with multi-keyword comparison
- [ ] Semantic search via vector similarity

### v1.4.0 — Production Hardening
- [ ] Redis response caching on expensive graph queries
- [ ] Celery Flower monitoring setup
- [ ] Structured JSON logging (structlog)
- [ ] Full test coverage (>85% across all modules)
- [ ] Render deployment with auto-deploy on `main` push

---

## 📄 License

MIT License — Copyright © 2026 **Ngô Minh Hiếu**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

See [LICENSE](LICENSE) for the full text.

---

<div align="center">
  <sub>
    Built with ☕ and curiosity by <a href="https://github.com/HieuXiao">Ngô Minh Hiếu</a>
    &nbsp;·&nbsp;
    Part of the <a href="https://github.com/HieuXiao/scidata-monitor-fe">SciData Monitor</a> project
  </sub>
</div>