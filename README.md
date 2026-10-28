# 🛡️ CrewAI Cybersecurity Research Agent

A multi-agent cybersecurity research system built with **CrewAI, Python, and Ollama**. The project uses specialized AI agents to research cybersecurity topics, assess security risks, recommend defensive mitigations, and generate structured cybersecurity reports.

The system demonstrates how multiple AI agents can collaborate through a sequential workflow, with each agent contributing a specialized part of the final result.

## 📌 Project Overview

Cybersecurity analysis involves understanding threats, evaluating risks, and communicating practical security recommendations. This project organizes these responsibilities into three specialized AI agents.

The user enters a cybersecurity topic, and the CrewAI system coordinates the agents to produce a structured report. The report is displayed in the terminal and saved as a Markdown file in the `reports/` directory.

### Key Features

- **Multi-agent collaboration:** Three specialized agents work together on a shared task.
- **Cybersecurity research:** Analyzes security topics, threats, and defensive practices.
- **Risk assessment:** Evaluates potential impacts and prioritizes mitigations.
- **Automated report generation:** Produces structured cybersecurity reports.
- **Local LLM integration:** Configured to use Ollama with the `llama3.2:3b` model.
- **Timestamped reports:** Saves generated reports for later review.
- **Sequential execution:** Uses CrewAI's `Process.sequential` to coordinate task execution.
- **Reduced dependence on hosted AI APIs:** Designed to run inference locally through Ollama without requiring an OpenAI API key.

> **Note:** The project is configured for local Ollama inference. It does not automatically guarantee that every generated claim is verified against current external sources.

## 🏗️ System Architecture

The project uses three agents with distinct responsibilities.

```text
                  User
                    |
                    v
          Enter Cybersecurity Topic
                    |
                    v
       +---------------------------+
       | Cybersecurity Research    |
       | Analyst                   |
       +---------------------------+
                    |
                    v
             Research Brief
                    |
                    v
       +---------------------------+
       | Security Risk Analyst     |
       +---------------------------+
                    |
                    v
          Risk Assessment
                    |
                    v
       +---------------------------+
       | Cybersecurity Report      |
       | Writer                    |
       +---------------------------+
                    |
                    v
          Final Security Report
                    |
          +---------+---------+
          |                   |
          v                   v
    Terminal Output     reports/*.md
```

The sequential workflow allows downstream tasks to build on the outputs of earlier tasks.

## 🤖 AI Agents

### 1. Cybersecurity Research Analyst

**Role:** Cybersecurity Research Analyst

**Responsibilities:**
- Analyze the cybersecurity topic provided by the user.
- Identify relevant security threats and vulnerabilities.
- Explain potential consequences.
- Summarize established defensive practices.
- Produce a structured research brief.

This agent establishes the foundation for the subsequent risk assessment.

### 2. Security Risk Analyst

**Role:** Security Risk Analyst

**Responsibilities:**
- Evaluate the research brief produced by the research analyst.
- Identify and prioritize important security risks.
- Explain potential impacts.
- Recommend practical defensive mitigations.
- Produce a structured risk assessment.

This agent receives the research task as context, allowing it to build on the preceding agent's work.

### 3. Cybersecurity Report Writer

**Role:** Cybersecurity Report Writer

**Responsibilities:**
- Organize the research and risk assessment into a professional report.
- Present key findings in clearly defined sections.
- Summarize recommended security controls.
- Identify implementation priorities.
- Document limitations and remaining uncertainties.

The report writer transforms the preceding analysis into a final document suitable for review.

## 🔄 How the Agents Collaborate

The project uses CrewAI's sequential process:

```python
security_crew = Crew(
    agents=[researcher, analyst, report_writer],
    tasks=[research_task, risk_task, report_task],
    process=Process.sequential,
    verbose=True,
)
```

The collaboration follows three stages:

1. **Research:** The research analyst investigates the topic and produces a research brief.
2. **Risk evaluation:** The risk analyst receives the research task as context and evaluates the identified risks.
3. **Report generation:** The report writer organizes the preceding outputs into a structured cybersecurity report.

This design demonstrates that multi-agent systems can divide a complex task into smaller responsibilities. Each agent has its own role, goal, and backstory, while CrewAI coordinates task execution.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CrewAI | Agent creation, task management, and orchestration |
| Ollama | Local language model runtime |
| Llama 3.2 3B | Configured local language model |
| Markdown | Generated report format |
| pathlib | File and directory management |
| datetime | Timestamped report filenames |

## 📁 Project Structure

```text
CrewAI/
│
├── main.py
├── reports/
│   ├── security_report_<timestamp>.md
│   └── ...
│
├── .venv/
│
└── README.md
```

**Files and directories:**

- `main.py` — Defines the language model configuration, agents, tasks, sequential crew, and execution logic.
- `reports/` — Stores generated cybersecurity reports.
- `.venv/` — Local Python virtual environment. This directory should generally not be committed to GitHub.
- `README.md` — Project documentation.

## ⚙️ Prerequisites

Before running the project, install the following:

- Python 3.12 recommended for this setup.
- [Ollama](https://ollama.com/) installed and running.
- The `llama3.2:3b` model downloaded.
- Git, if you intend to clone and manage the project through GitHub.

## 🚀 Installation and Setup

### 1. Clone the Repository

Replace the placeholder URL with your actual GitHub repository URL.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Alternatively, open the project directory you already created.

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks virtual-environment activation, you can invoke the environment's Python executable directly or adjust your execution policy according to your organization's security requirements.

### 3. Install Dependencies

Upgrade pip and install CrewAI:

```powershell
python -m pip install --upgrade pip
python -m pip install crewai
```

Verify the installation:

```powershell
python -c "import crewai; print('CrewAI installed successfully')"
```

### 4. Install and Start Ollama

Install Ollama from its official website:

https://ollama.com/

Download the configured model:

```powershell
ollama pull llama3.2:3b
```

Confirm that the model is installed:

```powershell
ollama list
```

Ollama should be running locally before you execute the CrewAI application.

### 5. Verify the LLM Configuration

The project configures CrewAI to connect to Ollama through an OpenAI-compatible local endpoint:

```python
llm = LLM(
    model="llama3.2:3b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    custom_openai=True,
    temperature=0.2,
)
```

The model name, endpoint, and compatibility options must match the versions of CrewAI and Ollama installed in your environment.

No OpenAI API key is required for this local configuration.

## ▶️ Running the Application

Activate the virtual environment, ensure Ollama is running, and execute:

```powershell
python main.py
```

When prompted, enter a cybersecurity topic.

Example:

```text
Enter a cybersecurity research topic: Best practices for securing Windows workstations
```

The application then runs the sequential crew, displays the generated report, and saves the result to the `reports/` directory.

The output filename follows a timestamped pattern similar to:

```text
reports/security_report_20261027_203000.md
```

The exact filename depends on when the report is generated.

## 📄 Report Contents

The generated report is designed to include the following sections:

1. Executive summary
2. Background
3. Key security threats
4. Risk assessment
5. Recommended defensive controls
6. Implementation priorities
7. Limitations and conclusion

The content depends on the topic entered and the language model's response.

## 🧪 Example Research Topics

You can test the system with topics such as:

- Best practices for securing Windows workstations
- Multi-factor authentication in enterprise environments
- Network access control and endpoint security
- Ransomware prevention and recovery planning
- Secure configuration of enterprise servers
- Identity and access management
- Backup strategies for business continuity
- Security awareness and phishing prevention

Use these topics to compare how the agents structure their research, prioritize risks, and develop recommendations.

## 🔐 Security and Responsible Use

This project is intended for cybersecurity research, defensive analysis, and educational purposes.

Important considerations:

- Treat generated recommendations as a starting point for analysis, not as a substitute for professional security review.
- Validate important claims against authoritative documentation and current vendor guidance.
- Do not include passwords, API keys, confidential reports, or other sensitive information in prompts or public repositories.
- Review generated reports before applying recommendations to production systems.
- The current configuration does not establish that live web research or automatic source verification is being performed.

## ⚠️ Limitations

- **Model limitations:** A locally hosted language model may generate incomplete or inaccurate information.
- **Source verification:** The current workflow does not inherently guarantee citations or independent verification of claims.
- **Current threat intelligence:** Without a configured research or retrieval tool, the agents cannot be assumed to have access to live threat intelligence.
- **Hardware requirements:** Local inference performance depends on the computer's available CPU, RAM, and GPU resources.
- **Output quality:** Report depth and accuracy depend on the model, task instructions, and quality of the preceding agent outputs.

## 🔮 Potential Future Improvements

Possible extensions include:

- Adding web search and trusted-source retrieval.
- Requiring citations for factual security claims.
- Adding structured severity ratings, such as Critical, High, Medium, and Low.
- Implementing retries and recovery for model failures.
- Adding human approval before high-impact recommendations are finalized.
- Exporting reports to PDF or DOCX.
- Creating automated tests for task outputs and report structure.
- Evaluating the quality and consistency of reports across multiple cybersecurity topics.

## 🎓 Learning Objectives

This project demonstrates practical concepts in agentic AI:

- Defining specialized AI agents with roles, goals, and backstories.
- Decomposing a complex task into smaller tasks.
- Passing task outputs between agents using context.
- Orchestrating multiple agents with a sequential process.
- Connecting CrewAI to a locally hosted language model.
- Generating and saving structured output programmatically.

## 👨‍💻 Author

**Michael Rill Okanda**

Computer Science | AI Engineering | Agentic AI | Cybersecurity Research

## 📜 Disclaimer

This project is intended for educational and defensive cybersecurity research. Generated output may contain errors and should be independently reviewed before being used for operational security decisions.# CrewAI-Cybersecurity-Research-Agent.
