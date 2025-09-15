
def explain_cause(cause: str) -> str:
    mapping = {
        "prijs": "Prijsafspraak of tariefafwijking t.o.v. de originele factuur.",
        "hoeveelheid": "Hoeveelheid wijkt af van de oorspronkelijke levering/factuur.",
        "leverdatum": "Aflevering vond plaats buiten de afgesproken datum/venster.",
        "referentie": "Ontbrekende of foutieve referentie (PO/klantref).",
        "anders": "Niet in de standaard categorieën te plaatsen."
    }
    return mapping.get(cause, "Onbekend")
