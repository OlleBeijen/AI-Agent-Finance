
def answer_with_snippets(question: str, snippets: list[dict]) -> str:
    # Geen LLM nodig voor MVP: bouw een kort antwoord opgebouwd uit snippets.
    lines = [f"Vraag: {question}", "", "Relevante stukken:"]
    for s in snippets:
        lines.append(f"- {s['source']} — score {s['score']:.3f}")
    return "\n".join(lines)
