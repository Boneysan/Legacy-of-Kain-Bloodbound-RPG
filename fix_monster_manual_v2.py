import os
import re

directory = '/mnt/h/GitHub/Legacy-of-Kain-Bloodbound-RPG/Monster_Manual/'
files = [f for f in os.listdir(directory) if f.endswith('.md')]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. saving throw -> save (case-insensitive)
    new_content = re.sub(r'saving throw', 'save', new_content, flags=re.IGNORECASE)

    # 3 & 4. Immunities/Resistances lists for Fear/Charm/Soul/Necrotic/Corruption/Void
    def list_fix(match):
        header = match.group(1)
        items = match.group(2)
        # Order of replacements matters to avoid partial hits
        items = re.sub(r'\bFear\b', 'Frightened', items, flags=re.IGNORECASE)
        items = re.sub(r'\bCharm\b', 'Charmed', items, flags=re.IGNORECASE)
        # Soul in lists -> Spectral (but not Soul Energy, etc. - though usually lists don't have those)
        items = re.sub(r'\bSoul\b(?![ \w]*(Energy|save|Drain|check|attribute))', 'Spectral', items, flags=re.IGNORECASE)
        items = re.sub(r'\bNecrotic\b', 'Entropic', items, flags=re.IGNORECASE)
        items = re.sub(r'\bCorruption\b', 'Entropic', items, flags=re.IGNORECASE)
        items = re.sub(r'\bVoid\b', 'Entropic', items, flags=re.IGNORECASE)
        return header + items

    new_content = re.sub(r'(Immunities:|Resistances:)(.*)', list_fix, new_content, flags=re.IGNORECASE)

    # 5. Threat Value -> TV
    new_content = re.sub(r'Threat Value', 'TV', new_content, flags=re.IGNORECASE)

    # 8. Damage types in descriptions/attacks
    # e.g., "10 Soul", "6 Necrotic", "7 Corruption", "5 Void"
    # But avoid "Soul Energy", "Soul save", etc.
    
    # Soul/Arcane -> Spectral/Force
    new_content = re.sub(r'Soul/Arcane', 'Spectral/Force', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'(\d+) Soul(?![ \w]*(Energy|save|Drain|check|attribute|pool))', r'\1 Spectral', new_content)
    new_content = re.sub(r'(\d+) Necrotic', r'\1 Entropic', new_content)
    new_content = re.sub(r'(\d+) Corruption', r'\1 Entropic', new_content)
    new_content = re.sub(r'(\d+) Void', r'\1 Entropic', new_content)
    new_content = re.sub(r'(\d+) Arcane', r'\1 Force', new_content)

    # Damage words
    new_content = re.sub(r'\bSoul damage\b', 'Spectral damage', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'\bNecrotic damage\b', 'Entropic damage', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'\bCorruption damage\b', 'Entropic damage', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'\bVoid damage\b', 'Entropic damage', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'\bArcane damage\b', 'Force damage', new_content, flags=re.IGNORECASE)

    # 7. DR as armor
    new_content = re.sub(r'DR (\d+) vs ([a-zA-Z]+)', r'Armor \1 vs \2', new_content)

    # 6. Resource lines consistency
    # First, fix stat blocks like "HP 120; SE 60; Armor 3"
    # Match any combination of HP, SE, BP, Armor, DV with numbers, separated by ; or , or |
    def resource_line_fix(match):
        parts = re.split(r'[;,|]', match.group(0))
        cleaned_parts = []
        for p in parts:
            p = p.strip()
            if not p: continue
            # Split label and value
            m = re.match(r'(HP|SE|BP|Armor|DV) ([\d/]+|N/A)', p, re.IGNORECASE)
            if m:
                cleaned_parts.append(f"{m.group(1).upper()}: {m.group(2)}")
            else:
                cleaned_parts.append(p)
        return " | ".join(cleaned_parts)

    # Target lines that look like resource lists (start with HP or SE or contain multiple of these)
    new_content = re.sub(r'\b(HP \d+|SE \d+)( [;,|] (HP|SE|BP|Armor|DV) ([\d/]+|N/A))+\b', resource_line_fix, new_content)

    # Also catch individual ones that might have missed the colon
    new_content = re.sub(r'\b(HP|SE|BP|Armor|DV) (\d+|N/A)\b(?![ \w]*:)', r'\1: \2', new_content)
    
    # Fix double colons if any
    new_content = re.sub(r'(\b(HP|SE|BP|Armor|DV)):+ ', r'\1: ', new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

for filename in files:
    process_file(os.path.join(directory, filename))
