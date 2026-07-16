# Core Execution Engines & Orchestration

This directory serves as the centralized computational core of the **VortexArt88** repository. It houses the automation frameworks and master pipeline orchestrators responsible for managing, executing, and validating your self-contained component modules.

## ⚙️ The Orchestration Architecture

Instead of requiring users or hardware developers to manually run multiple individual scripts, this directory unifies your codebase into a single automated pipeline:

```text
    ┌─────────────────────────────────────────────────────┐
    │     core_engines/run_all_simulations.py             │
    └──────────────────┬──────────────────────────────────┘
                       │
                       ├─► [1] Validates: /config/data-card.json
                       │
                       ├─► [2] Triggers:  /transcendental-flow-regulator
                       │
                       ├─► [3] Triggers:  /flower-of-life-mesh
                       │
                       └─► [4] Triggers:  /figure-eight-mixer
```

### 🗂️ Core Engine Modules

* **`run_all_simulations.py`**
  * **Function:** The master pipeline orchestrator. It uses a controlled subprocess pipeline to sequentially launch each component's calculation engine within its own isolated working directory. This completely prevents local file reference mismatches or path failures.
  * **Environment Safeguards:** It tracks the active runtime environment using the native system python interpreter, ensuring cross-platform compatibility across Windows, macOS, and Linux without package drift.

## 🚀 System Execution

To initiate a full computational sweep of the entire structural framework, execute the master script from the repository's root directory:

```bash
python core_engines/run_all_simulations.py
```

### Automation & Fallback Defenses
Upon startup, the engine performs a pre-flight validation check to locate your universal standard configuration files. If your master settings files are ever misplaced, the core orchestrator prevents a system crash by automatically enforcing default hardware constraints, logging the warnings, and continuing the pipeline smoothly.
