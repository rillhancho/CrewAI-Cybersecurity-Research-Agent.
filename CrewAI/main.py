from pathlib import Path
from datetime import datetime

from crewai import Agent, Task, Crew, Process, LLM



#Connecting CrewAI to the local Ollama model


llm = LLM(
    model="llama3.2:3b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    custom_openai=True,
    temperature=0.2,
)



# Define the agents


researcher = Agent(
    role="Cybersecurity Research Analyst",
    goal=(
        "Analyze cybersecurity topics and identify established "
        "security principles, threats, and defensive practices."
    ),
    backstory=(
        "You are a cybersecurity research analyst specializing in "
        "defensive security, security awareness, and threat analysis. "
        "You distinguish established facts from assumptions and never "
        "invent sources or claim to have performed live research."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

analyst = Agent(
    role="Security Risk Analyst",
    goal=(
        "Evaluate security risks, explain their potential impact, "
        "and recommend practical defensive mitigations."
    ),
    backstory=(
        "You assess cybersecurity risks using a structured approach. "
        "You prioritize recommendations according to risk, feasibility, "
        "and defensive value."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

report_writer = Agent(
    role="Cybersecurity Report Writer",
    goal="Produce a clear, actionable cybersecurity research report.",
    backstory=(
        "You write professional technical reports for IT professionals "
        "and security teams. You organize findings into clear sections "
        "and identify limitations in the available evidence."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)



#  Defining the tasks


research_task = Task(
    description=(
        "Analyze the following cybersecurity topic: {topic}\n\n"
        "Explain the topic, identify relevant threats, describe "
        "potential consequences, and summarize established defensive "
        "practices. Do not invent citations or claim to have accessed "
        "live websites. Clearly identify any uncertainty."
    ),
    expected_output=(
        "A structured research brief covering the topic, relevant "
        "threats, potential impacts, defensive practices, and limitations."
    ),
    agent=researcher,
)

risk_task = Task(
    description=(
        "Evaluate the research brief produced for this topic: {topic}.\n\n"
        "Identify the most important risks, explain their likely impact, "
        "and recommend prioritized mitigations. Separate established "
        "information from assumptions and avoid unsupported claims."
    ),
    expected_output=(
        "A risk assessment with prioritized risks, their potential impact, "
        "recommended mitigations, and remaining uncertainties."
    ),
    agent=analyst,
    context=[research_task],
)

report_task = Task(
    description=(
        "Create a professional cybersecurity report about {topic}.\n\n"
        "Use the research brief and risk assessment. Include:\n"
        "1. Executive summary\n"
        "2. Background\n"
        "3. Key security threats\n"
        "4. Risk assessment\n"
        "5. Recommended defensive controls\n"
        "6. Implementation priorities\n"
        "7. Limitations and conclusion\n\n"
        "Do not fabricate references, statistics, or live research."
    ),
    expected_output=(
        "A complete Markdown cybersecurity report with clear headings, "
        "practical recommendations, and explicit limitations."
    ),
    agent=report_writer,
    context=[research_task, risk_task],
)



# Assembling the Crew


security_crew = Crew(
    agents=[researcher, analyst, report_writer],
    tasks=[research_task, risk_task, report_task],
    process=Process.sequential,
    verbose=True,
)



# Runing the agent and save its report


def main():
    topic = input(
        "Enter a cybersecurity research topic: "
    ).strip()

    if not topic:
        print("Please enter a research topic.")
        return

    print(f"\nStarting cybersecurity analysis: {topic}\n")

    result = security_crew.kickoff(
        inputs={"topic": topic}
    )

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"security_report_{timestamp}.md"

    report_path.write_text(
        str(result),
        encoding="utf-8",
    )

    print("\nAnalysis completed!")
    print(f"Report saved to: {report_path.resolve()}")
    print("\nReport preview:\n")
    print(str(result))


if __name__ == "__main__":
    main()