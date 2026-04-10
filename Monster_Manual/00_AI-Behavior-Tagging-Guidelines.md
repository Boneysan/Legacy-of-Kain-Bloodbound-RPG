# Monster Manual - AI Behavior Tagging Guidelines

**Purpose**

This document defines a light-touch tagging standard for Monster Manual entries that may be used by GM tools and Virtual Tabletop automation.

These tags exist to support encounter consistency, faster prep, and VTT AI handoff. They are **authoring metadata first**, not the primary identity of a creature. A Bloodbound creature should still be understood through its lore, abilities, and tactics before its tags.

---

## Design Intent

Bloodbound monsters are narrative instruments first and tactical units second.

Because of that, behavior tags should:

- Support the existing **Tactics** section rather than replace it.
- Stay visually restrained and easy to ignore during normal reading.
- Describe dominant battlefield tendencies, not every possible action.
- Help a VTT infer a creature's default behavior without flattening its personality.

If a creature's fiction and its tags ever disagree, the fiction and Tactics text win.

---

## Recommended Placement

Use a single, low-visibility metadata line in the stat block:

```markdown
**Behavior Tags:** soldier, controller
```

Place it near the core stat block, ideally after classification and before Tactics, so it remains available to downstream tools without becoming the centerpiece of the entry.

Do not add long explanations beside each tag inside the creature entry. The detailed meaning belongs in this guideline, not repeated in every stat block.

---

## Authoring Rules

1. Assign **2 to 4 tags** per creature in most cases.
2. Use only the creature's **dominant** behaviors.
3. Do not use tags as a substitute for writing a proper **Tactics** section.
4. Do not invent one-off tags casually; expand the shared vocabulary only when multiple creatures need the same behavior concept.
5. Boss and legendary creatures may use one broader encounter tag plus one or two role tags.

---

## Core Tag Vocabulary

### pack
Uses nearby allies to pressure the same target, swarm isolated enemies, or gain bonuses from group positioning.

Best for: ghouls, wolves, feral mobs, coordinated lesser undead.

### ambusher
Prefers stealth, surprise, flanking, terrain advantage, or opening-round momentum.

Best for: assassins, lurking horrors, cave predators, stealth cultists.

### soldier
Fights with discipline. Uses cover, focus fire, chokepoints, formation logic, or objective-minded tactics.

Best for: Sarafan units, Hylden shock troops, trained guards.

### brute
Prefers direct pressure, durability, and space control over finesse.

Best for: large undead, hulking mutants, executioners, fortress monsters.

### skirmisher
Relies on mobility, repositioning, harassment, and avoiding static melee.

Best for: fast beasts, agile vampires, spectral raiders.

### controller
Prioritizes debuffs, battlefield zones, movement denial, fear, or area manipulation.

Best for: casters, glyph users, spectral disruptors, lair-linked threats.

### summoner
Creates, calls, commands, or sustains additional creatures or battlefield constructs.

Best for: necromancers, brood-creators, Hylden flesh architects.

### phase_shifter
Changes realms, blinks, phases through terrain, or treats battlefield geometry differently from normal creatures.

Best for: wraiths, spectral entities, advanced Hylden manifestations.

### sentinel
Anchors to a place, object, ward, relic, or passage and prioritizes defense of that anchor over pursuit.

Best for: revenants, ruin guardians, ward-bound constructs.

### boss
Encounter centerpiece with layered behavior, pacing logic, special action economy, or fight-phase expectations.

Best for: named villains, arc anchors, legendary entities.

---

## Optional Extended Tags

These should be used sparingly and only when they materially help encounter behavior or VTT handoff.

### support
Prioritizes healing, ally buffs, protection, condition removal, or sustain over direct damage.

Use `support` only when this is the creature's dominant combat purpose, not just one useful ability.
If removing the creature first would noticeably reduce enemy durability, coordination, or resilience, `support` is likely justified.
Do not use `support` for units that merely have a morale aura, a single ally buff, or one incidental healing/protection rider.
`support` often pairs well with `soldier`, `controller`, `sentinel`, or `boss` when the creature both enables allies and fills another clear battlefield role.

### objective_holder
Treats an object, ritual, captive, or battlefield locus as the real priority of the encounter.

### realm_hunter
Actively exploits Material/Spectral interaction, anti-phase pressure, or planar tracking.

### coward
Breaks, flees, bargains, or collapses once the encounter turns against it.

Use these only when they are central to the monster's identity in play, not just situational possibilities.

---

## Relationship to Tactics

Tags are not the tactics paragraph.

The tags answer: "What kind of battlefield logic does this creature usually follow?"

The tactics paragraph answers: "How does this specific creature feel and behave in this fight?"

Example:

```markdown
**Behavior Tags:** pack, brute

### Tactics
These ghouls rush the nearest living creature mindlessly. They overwhelm isolated prey,
pile onto wounded targets, and keep tearing at anything that falls.
```

The tags provide reusable structure. The Tactics section preserves voice and scene texture.

---

## Recommended VTT Mapping

For downstream VTT use, the expected relationship is:

- **Base Profile** comes from the creature's main combat posture.
- **Behavior Tags** refine how that posture is expressed.
- **Scripted Triggers** still handle special-case behavior such as reinforcements, retreats, phase changes, and encounter scripts.
- **GM Override** remains the final authority for edge cases and dramatic timing.

This means a creature should not be forced to encode all of its behavior in tags alone.

---

## How to Decide Scripted Triggers

Scripted triggers should be determined by **authored monster intent**, not by generic AI convenience.

Use them when a creature or encounter would feel wrong if its special behavior were left to default posture and tags alone.

### Primary Sources for Triggers

1. **Explicit mechanics in the stat block**
	If the creature has a bloodied ability, phase change, summon threshold, death burst, lair action, retreat clause, or once-per-fight escalation, that should usually become a scripted trigger.

2. **The Tactics section**
	If the tactics text says the creature flees when wounded, swarms isolated prey, protects a ward, targets casters first, or changes behavior after losing allies, that is strong trigger material.

3. **Encounter role or battlefield anchor**
	If the monster is guarding a relic, sustaining a ritual, obeying a controller, holding a choke point, or tethered to a specific object or location, those obligations should inform scripted behavior.

4. **Boss pacing and dramatic structure**
	Elite, boss, and legendary creatures often need scripted transitions for reinforcements, desperation phases, reaction budgeting, lair timing, or escape logic.

5. **Scene-specific GM authoring**
	Some triggers belong to a specific encounter rather than the creature itself, such as "if the ward takes damage" or "if two cultists die." Those should live in encounter prep rather than permanently in the creature entry.

### Practical Rule

Use:

- **Base Profile** for default turn-to-turn posture.
- **Behavior Tags** for recurring tactical identity.
- **Scripted Triggers** for authored behavior that changes the feel or flow of the encounter.

If removing the trigger would make the creature feel generic, it probably deserves to be scripted.

---

## Example Mappings

### Feralslave Ghoul

```markdown
**Behavior Tags:** pack, brute
```

Reasoning: It swarms with allies, presses the nearest living target, and wins by direct mauling pressure.

### Hylden Shock Trooper

```markdown
**Behavior Tags:** soldier, controller
```

Reasoning: It uses discipline, flanking, and focus fire while also disrupting enemy positioning and action flow.

### Nosgothian Revenant

```markdown
**Behavior Tags:** sentinel, brute
```

Reasoning: Its real identity is tied to what it guards, avenges, or remains bound to, even if it also fights directly.

### Legendary Time-Bound Antagonist

```markdown
**Behavior Tags:** boss, phase_shifter, controller
```

Reasoning: The encounter depends on staged pacing, positional dominance, and altered battlefield rules.

---

## Tone Safeguard

If a tag line starts making an entry feel clinical, reduce it.

Bloodbound's bestiary should still read like a record of cursed things, broken loyalties, predatory instincts, and metaphysical horrors. The tags are there to support play and tooling, not to become the creature's voice.

---

## Final Recommendation

Use behavior tags in the Monster Manual, but keep them restrained.

- One metadata line per creature.
- Two to four tags in most entries.
- Stable shared vocabulary.
- Tactics text remains the primary behavioral expression.
- VTT systems may consume the tags, but the Monster Manual should never read like a technical export.

That balance preserves Bloodbound's tone while making the bestiary much easier to use at the table and in a digital VTT.