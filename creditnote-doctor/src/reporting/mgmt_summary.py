
def build_management_summary(kpis: dict) -> str:
    # Korte samenvatting zonder LLM voor MVP
    causes_sorted = sorted(kpis["by_cause"].items(), key=lambda x: -x[1])
    bullets = []
    for cause, n in causes_sorted[:3]:
        action = {
            "prijs": "Review prijstabellen en vergrendel tariefvelden in orderinvoer.",
            "hoeveelheid": "Controle op pick/pack versus factuur; zet automatische waarschuwing aan.",
            "leverdatum": "Herijk leverafspraken en voeg check toe bij planning.",
            "referentie": "Maak PO-veld verplicht en valideer formaat bij orderinvoer.",
            "anders": "Log detailredenen; plan handmatige triage."
        }.get(cause, "Plan gerichte analyse en kleine procesaanpassing.")
        bullets.append(f"- {cause}: {action} (verwacht: lagere aantallen en minder herstelkosten)")
    return "\n".join(bullets)
