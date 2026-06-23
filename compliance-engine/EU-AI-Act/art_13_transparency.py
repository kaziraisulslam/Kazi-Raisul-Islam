import json

def generate_transparency_manifest(model_name, capabilities, limitations):
    """
    Generates a technical manifest required by Art 13 for end-users.
    """
    manifest = {
        "model_name": model_name,
        "compliance_article": "Art-13-Transparency",
        "capabilities": capabilities,
        "limitations": limitations,
        "human_readable": True
    }
    
    with open('compliance-engine/artifacts/art_13_manifest.json', 'w') as f:
        json.dump(manifest, f, indent=4)
    print(f"[GENERATED] Article 13 Transparency Manifest for {model_name}")

if __name__ == "__main__":
    generate_transparency_manifest("TalentOptimizer", ["CV-Parsing", "Ranking"], ["Not designed for salary negotiation"])
