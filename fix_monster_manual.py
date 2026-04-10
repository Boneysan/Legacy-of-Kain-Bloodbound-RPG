import os
import re

directory = '/mnt/h/GitHub/Legacy-of-Kain-Bloodbound-RPG/Monster_Manual/'
files = [f for f in os.listdir(directory) if f.endswith('.md')]

replacements = [
    (re.compile(r'saving throw', re.IGNORECASE), 'save'),
    (re.compile(r'Immune to Fear', re.IGNORECASE), 'Immune to Frightened'),
    (re.compile(r'Immune to Charm', re.IGNORECASE), 'Immune to Charmed'),
    (re.compile(r'Threat Value', re.IGNORECASE), 'TV'),
    (re.compile(r'Soul damage', re.IGNORECASE), 'Spectral damage'),
    (re.compile(r'Necrotic damage', re.IGNORECASE), 'Entropic damage'),
    (re.compile(r'Corruption damage', re.IGNORECASE), 'Entropic damage'),
    (re.compile(r'Void damage', re.IGNORECASE), 'Entropic damage'),
]

# Specifically for immunity/resistance lists
list_replacements = [
    (re.compile(r'(Immunities:|Resistances:)(.*?)Fear', re.IGNORECASE), r'\1\2Frightened'),
    (re.compile(r'(Immunities:|Resistances:)(.*?)Charm', re.IGNORECASE), r'\1\2Charmed'),
    (re.compile(r'(Immunities:|Resistances:)(.*?)Soul(?![ \w]*(Energy|save|Drain|check|attribute))', re.IGNORECASE), r'\1\2Spectral'),
    (re.compile(r'(Immunities:|Resistances:)(.*?)Necrotic', re.IGNORECASE), r'\1\2Entropic'),
    (re.compile(r'(Immunities:|Resistances:)(.*?)Corruption', re.IGNORECASE), r'\1\2Entropic'),
    (re.compile(r'(Immunities:|Resistances:)(.*?)Void', re.IGNORECASE), r'\1\2Entropic'),
]

# DR as armor: "DR [Number] vs [Type]" -> "Armor [Number] vs [Type]"
dr_armor_regex = re.compile(r'DR (\d+) vs ([a-zA-Z]+)')

# Resource lines: "HP 90; SE 60; Armor 2" -> "HP: 90 | SE: 60 | Armor: 2"
# "SE 10 | BP 5" -> "SE: 10 | BP: 5"
resource_regex = re.compile(r'\b(HP|SE|BP|Armor) (\d+|N/A)\b')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # Apply simple replacements
    for pattern, replacement in replacements:
        new_content = pattern.sub(replacement, new_content)

    # Apply list replacements (repeat to handle multiple items in one list)
    for _ in range(5):
        changed = False
        for pattern, replacement in list_replacements:
            next_content = pattern.sub(replacement, new_content)
            if next_content != new_content:
                new_content = next_content
                changed = True
        if not changed:
            break

    # Apply DR as armor
    new_content = dr_armor_regex.sub(r'Armor \1 vs \2', new_content)

    # Apply resource formatting
    # First, let's normalize separators in resource lines if they look like stat blocks
    # e.g., "HP 120; SE 60; Armor 3" or "HP 120, SE 60, Armor 3"
    stat_line_regex = re.compile(r'(HP \d+)[;,] (SE (\d+|N/A))[;,] (BP (\d+|N/A))[;,] (Armor \d+)')
    new_content = stat_line_regex.sub(r'\1 | \2 | \4 | \6', new_content)
    
    stat_line_regex2 = re.compile(r'(HP \d+)[;,] (SE (\d+|N/A))[;,] (Armor \d+)')
    new_content = stat_line_regex2.sub(r'\1 | \2 | \4', new_content)

    # Now add colons
    new_content = resource_regex.sub(r'\1: \2', new_content)
    
    # Ensure " | " separator instead of ";" or "," between resources
    new_content = re.sub(r'(HP: \d+|SE: \d+|BP: \d+|Armor: \d+) [;,] ', r'\1 | ', new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

for filename in files:
    process_file(os.path.join(directory, filename))
