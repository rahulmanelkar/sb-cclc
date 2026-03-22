# Module Dependency Map

Shows which modules import from which. No circular dependencies were found.

```mermaid
flowchart LR
    %% ── Entry Point ──────────────────────────────────────────────
    subgraph entry["Entry Point"]
        MAIN["second_brain/__main__.py"]
    end

    %% ── Core Package ─────────────────────────────────────────────
    subgraph core["second_brain (core)"]
        CLI["cli.py"]
        APP["app.py"]
        NOTES["notes.py"]
    end

    %% ── Tests ────────────────────────────────────────────────────
    subgraph tests["tests/"]
        CONF["conftest.py"]
        TCLI["test_cli.py"]
        TAPP["test_app.py"]
        TNOTES["test_notes.py"]
    end

    %% ── Scripts ──────────────────────────────────────────────────
    subgraph scripts["scripts/"]
        SERVE["serve_docs.py"]
    end

    %% ── External dependencies ────────────────────────────────────
    subgraph ext["Third-party / stdlib"]
        CLICK["click"]
        LOGURU["loguru"]
        PYTEST["pytest"]
        STDLIB["stdlib\nos · pathlib · re · datetime · subprocess · sys"]
    end

    %% ── Edges: local imports ─────────────────────────────────────
    MAIN  --> CLI
    CLI   --> APP
    CLI   --> NOTES

    TCLI   --> CLI
    TAPP   --> APP
    TNOTES --> NOTES

    %% ── Edges: external imports ──────────────────────────────────
    CLI    --> CLICK
    APP    --> LOGURU
    CLI    --> STDLIB
    APP    --> STDLIB
    NOTES  --> STDLIB
    SERVE  --> STDLIB

    TCLI   --> CLICK
    TCLI   --> STDLIB
    TAPP   --> STDLIB
    TNOTES --> STDLIB
    CONF   --> PYTEST
    TCLI   --> PYTEST
    TAPP   --> PYTEST
    TNOTES --> PYTEST

    %% ── Styles ───────────────────────────────────────────────────
    classDef entryStyle  fill:#4a90d9,stroke:#2c6fad,color:#fff
    classDef coreStyle   fill:#27ae60,stroke:#1e8449,color:#fff
    classDef testStyle   fill:#8e44ad,stroke:#6c3483,color:#fff
    classDef scriptStyle fill:#e67e22,stroke:#b9770e,color:#fff
    classDef extStyle    fill:#7f8c8d,stroke:#5d6d7e,color:#fff

    class MAIN entryStyle
    class CLI,APP,NOTES coreStyle
    class CONF,TCLI,TAPP,TNOTES testStyle
    class SERVE scriptStyle
    class CLICK,LOGURU,PYTEST,STDLIB extStyle
```

## Dependency summary

| Module | Imports from | Imported by |
|---|---|---|
| `__main__` | `cli` | *(entry point)* |
| `cli` | `app`, `notes`, click, stdlib | `__main__`, `test_cli` |
| `app` | loguru, stdlib | `cli`, `test_app` |
| `notes` | stdlib only | `cli`, `test_notes` |
| `test_cli` | `cli`, click, pytest, stdlib | — |
| `test_app` | `app`, pytest, stdlib | — |
| `test_notes` | `notes`, pytest, stdlib | — |
| `serve_docs` | stdlib only | — |

## What you can safely change

| Module | Risk level | Notes |
|---|---|---|
| `notes.py` | **Low** — only stdlib deps | Only `cli.py` and `test_notes.py` depend on it. Changes to its public API (`create_note`, `build_note_path`, `slugify`) require updating both. |
| `app.py` | **Low** — only stdlib + loguru | Only `cli.py` and `test_app.py` depend on it. Changing the logging API (`configure_logging`, `console_format`, `main`) requires updating both. |
| `cli.py` | **Medium** | Sits in the middle of the chain. Changes ripple to `__main__` and `test_cli`. The CLI command interface is also the user-facing contract. |
| `__main__.py` | **Low** | Only imports `cli`; changing it only affects the `python -m second_brain` entry point. |
| `tests/*` | **Low** | No production code imports tests; all changes are isolated. |
| `serve_docs.py` | **Low** | Fully isolated — no local imports. |

> **No circular dependencies detected.** The dependency graph is a strict DAG.
