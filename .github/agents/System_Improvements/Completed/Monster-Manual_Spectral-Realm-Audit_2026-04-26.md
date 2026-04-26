# Monster Manual — Spectral Realm Mechanics Audit

**Date:** 2026-04-26
**Source:** Cross-reference of all nine Monster Manual chapters against the new Section 11.5 (The Spectral Realm — Full Rules) in `player's_handbook/11_Realms-Terrain-Arcane-Power.md`.
**Status:** Pass 1 and Pass 2 complete. Pass 3 (Monster Manual schema + stat block edits) open.

---

## Context

Section 11.5 was drafted as a full Spectral Realm rules expansion. Once added to the PHB, it created a set of formal definitions (Soul Bleed, Incorporeal interaction, Partial Shift, Affinity types, phase movement rules) that the Monster Manual chapters predating it do not align with. This document captures every discovered conflict, gap, and ambiguity across all nine chapters, organized by severity.

All nine Monster Manual chapters were audited. The primary problem areas are concentrated in:
- `Monster_Manual/02_Spectral-Entities.md` (entire chapter)
- `Monster_Manual/01_Undead-and-Vampiric.md` (Flamewraith, Banshee, Dimension-Walker, Void-Touched)
- `Monster_Manual/04_Beasts-and-Mutants.md` (Void-Stalker Cougar)
- `Monster_Manual/07_Elemental-and-Arcane.md` (SE-Feeder)
- `Monster_Manual/08_Ancient-Creatures.md` (Ancient Guardian)

---

## Issue A — Incorporeal vs 11.5 Combat Table: Direct Conflict

**Severity:** High
**Chapters Affected:** Ch. 1 (Flamewraith, Banshee, Void-Touched), Ch. 2 (all Spectral Entities), Ch. 7 (SE-Feeder), Ch. 8 (Ancient Guardian)

### The Conflict
Section 11.5.3 (Combat Across Realms) states that Physical damage (Bludgeoning, Piercing, Slashing) from a Material attacker against a Spectral target has **"No effect — passes through."** No distinction between magical and nonmagical weapons is made.

The Monster Manual defines **Incorporeal** as:
> *"Immune to nonmagical physical attacks. Magical weapons and spells affect normally."*

Under 11.5, a magical sword in the hands of a Material attacker still does nothing to a Spectral creature. Under the Incorporeal trait, it does full damage. These rules directly contradict each other.

### The Source of the Conflict
The Monster Manual was written before 11.5 existed. "Incorporeal" was the MM's own solution to the cross-realm problem — but it only partially addresses it and uses different logic than 11.5.

### Two Resolution Options

**Option A — Clarify Scope (Recommended):** The 11.5 table governs true cross-realm combat where attacker and target are in *different realms*. When a Spectral creature *manifests* in the Material Realm to engage in combat — which is what every MM encounter represents — the creature has partially crossed over and Incorporeal applies. The two rules cover different scenarios and do not conflict.

Add a clarifying paragraph to Section 11.5.3:
> *"The damage type table above governs combat where attacker and target are in different realms simultaneously — one in Spectral, one in Material. When a Spectral creature manifests in the Material Realm (as they do in all standard combat encounters), they are subject to their printed Incorporeal trait instead. Incorporeal is a partial-manifestation defense, not a cross-realm targeting rule."*

**Option B — Unify Under 11.5:** Update every Incorporeal entry in the MM to remove the magical/nonmagical distinction and state that all physical damage is blocked. Magical weapons must deal Spectral, Force, Entropic, or Radiant damage to bypass it. This is mechanically cleaner but requires editing every Incorporeal stat block across five chapters.

### Recommended Fix
Option A. It preserves the existing stat blocks, requires a single clarifying paragraph, and is narratively coherent — a Spectral creature that chooses to fight in your world has made itself partially real.

---

## Issue B — Banshee Incorporeal Weaker Than All Other Incorporeal Creatures

**Severity:** Medium
**File:** `Monster_Manual/01_Undead-and-Vampiric.md` line 1271

### The Problem
Every Incorporeal creature in the MM uses the standard definition: "Immune to nonmagical physical attacks." The Banshee is the single exception:
> *"Nonmagical physical attacks deal half damage to the Banshee."*

Half damage — not immunity. This makes the Banshee substantially more vulnerable to physical attacks than any other Incorporeal creature. It is either an intentional design choice (the Banshee is more materialized than a true wraith) or an authoring error.

### Proposed Fix
Make a deliberate decision and document it. Two options:

**Option A — Intentional:** Add a one-line note to the Banshee's Incorporeal entry:
> *"(The Banshee's long years screaming in the Material Realm have partially anchored it to physical reality — its Incorporeal protection is weakened compared to purely Spectral entities.)"*

**Option B — Error:** Change the Banshee's Incorporeal to match the standard definition: "Immune to nonmagical physical attacks."

---

## Issue C — No Soul Bleed Exemption for Native Spectral Creatures

**Severity:** High
**File:** `player's_handbook/11_Realms-Terrain-Arcane-Power.md` Section 11.5.1

### The Problem
Section 11.5.1 defines Soul Bleed as: "At the start of each of your turns while fully manifested in the Spectral Realm, you lose 1 HP."

Exceptions exist for Wraith lineage (1 HP per 3 rounds) and Hybrid characters (immune first 3 rounds). There is no exception for **creatures native to the Spectral Realm** — things like Soul-Eater Shades, the Wraith of the Abyss, Echo Serpents, and every other Ch. 2 entity. Per the written rule, these creatures would suffer Soul Bleed in their own home realm, which makes no narrative or mechanical sense.

### Proposed Fix
Add one sentence to Section 11.5.1, after the Hybrid Exception:

> *"**Native Spectral Exception:** Creatures with **Spectral Affinity** as part of their stat block do not suffer Soul Bleed while in the Spectral Realm. The Spectral Realm is their natural state of existence — they do not dissolve there. Soul Bleed applies only to visitors."*

This fix is dependent on Issue G (Affinity field) — native Spectral creatures must be explicitly designated in their stat blocks for this exception to be enforceable.

---

## Issue D — Phase-Beast Partial Phase Conflicts With Partial Shift Condition

**Severity:** Medium
**File:** `Monster_Manual/02_Spectral-Entities.md` (Phase-Beast entry)

### The Problem
The Phase-Beast has a random state mechanic (roll 1d6 at the start of each turn):
- 1–2: Fully Material — normal combat
- 3–4: Partially phased — *Resistance to all damage*
- 5–6: Fully Spectral — *incorporeal, immune to physical damage, vulnerable to Radiant*

The 3–4 state is conceptually the **Partial Shift** condition defined in 11.5.5. But the mechanics are opposite: Partial Shift in 11.5 gives *no realm defenses* and makes the creature *targetable by both realms*. The Phase-Beast's partial phase gives *Resistance to all damage* — a significant defensive buff, not a vulnerability.

If a GM reads 11.5.5 and then looks at the Phase-Beast, they will assume these are the same thing and apply the wrong rules.

### Proposed Fix
Add a note to the Phase-Beast's Phase Shift entry:
> *"The Phase-Beast's 3–4 partial phase is a unique predatory adaptation and does not use the standard **Partial Shift** condition rules from Chapter 11. The Phase-Beast actively distorts dimensional boundaries as a defense mechanism, granting Resistance rather than the vulnerability of an involuntary partial crossing."*

---

## Issue E — Void-Touched "Partially Phases" Target Using Different Mechanics Than Partial Shift

**Severity:** Medium
**File:** `Monster_Manual/01_Undead-and-Vampiric.md` (Void-Touched entry, line ~1187)

### The Problem
The Void-Touched inflicts a partial phase effect on targets via Critical Hit:
> *"The target partially phases out of alignment. While partially phased, it can pass through solid objects but takes 3 Spectral damage at the start of each of its turns. The effect lasts until the target uses an Action and succeeds on a DR 3 Will save."*

Under 11.5.5, the **Partial Shift** condition causes:
- Targetable by creatures in both realms
- No realm-based defenses
- Soul Bleed at 1 HP/turn (not 3 Spectral damage)
- Exit via Bonus Action + 1 SE (not Action + DR 3 Will save)

The Void-Touched effect is mechanically different on four points. Without a note, GMs will either apply 11.5.5 Partial Shift rules (wrong) or the stat block rules (right but undocumented).

### Proposed Fix
Update the Void-Touched crit effect to name the condition and clarify its deviation:
> *"The target gains the **Partial Shift** condition (see Ch. 11 §11.5.5) with the following modifications: instead of standard Soul Bleed, the target takes **3 Spectral damage** at the start of each of its turns while Partially Shifted. The condition ends when the target uses an **Action** and succeeds on a **DR 3 Will** save, or by the standard Bonus Action + 1 SE stabilization from 11.5.5, whichever comes first."*

---

## Issue F — Phase Movement Abilities Not Referenced by 11.5 Framework

**Severity:** Low
**Chapters Affected:** Ch. 1, 2, 4, 5, 6, 8

### The Problem
Eleven creatures across six chapters have abilities that allow movement through solid objects: Phase Movement, Phase Step, Phase Strike, Phase Runner, Realm Shift. These abilities are self-contained in each stat block and predate 11.5. Now that 11.5 exists, GMs running encounters in or near the Spectral Realm will ask:

- Does Phase Movement work in the Spectral Realm?
- Does Phase Movement count as a `Spectral only` ability under Partial Shift rules?
- Does a creature using Realm Shift trigger Soul Bleed during the brief crossing?

None of these questions are answered anywhere.

### Creatures Affected

| Creature | Chapter | Ability Name |
| :--- | :--- | :--- |
| Echo Serpent | Ch. 2 | Phase Strike, Phase Movement |
| Mirror Wraith | Ch. 2 | Phase Step |
| Soul-Eater Shade | Ch. 2 | Phase Movement (implied by Incorporeal) |
| Spectral Wolves | Ch. 2 | Phase Runner |
| Bound Sorrow Spirit | Ch. 2 | Phase Movement (implied by Incorporeal) |
| Phase-Beast | Ch. 2 | Phase Shift (1d6 state) |
| Wraith of the Abyss | Ch. 2 | Phase Shift (invisibility variant) |
| Revenant Shade | Ch. 2 | Phase Step |
| Flamewraith | Ch. 1 | Phase Movement |
| Banshee | Ch. 1 | Phase movement (Incorporeal) |
| Dimension-Walker | Ch. 1 | Realm Shift |
| Void-Touched | Ch. 1 | Phase movement (innate) |
| Void-Stalker Cougar | Ch. 4 | Phase Shift (3/encounter) |
| Glyphfused Automaton | Ch. 5 | Phase Step |
| Bio-Sigil Reaver | Ch. 6 | Phase Strike, Phase Movement |
| Ancient Guardian | Ch. 8 | Phase Step |

### Proposed Fix
Add one paragraph to the Monster Manual Introduction (Monster Ability and Resistance Baseline section):

> *"**Phase Abilities and Realm Rules:** Phase Movement, Phase Step, Phase Strike, Phase Runner, and similar abilities that allow creatures to move through solid objects are innate Spectral traits. For creatures with **Spectral Affinity**, these abilities function in both realms by nature — moving through walls is what they do, regardless of which side of the veil they are on. For creatures with **Material Affinity** that have phase abilities through mutation, glyphs, or technology (constructs, mutants, certain Hylden), these abilities function in the Material Realm only and cannot be used while the creature is fully shifted to the Spectral Realm. Brief transits (such as Realm Shift) do not trigger standard Soul Bleed — the ability's listed cost covers the entire crossing and return."*

---

## Issue G — No Affinity Field on Any Monster Stat Block

**Severity:** High
**Files:** All nine Monster Manual chapters, `Monster_Manual/00_Introduction.md`

### The Problem
Monster stat blocks have no Affinity designation. Section 11.5 ties multiple rules to Affinity type:
- Soul Bleed exemption for native Spectral creatures (Issue C — requires Spectral Affinity designation)
- Cross-realm combat targeting (11.5.3 — requires knowing attacker and target affinity)
- Voluntary Shift availability (11.5.2 — Hybrid Affinity only)
- Phase ability behavior (Issue F — differs by Affinity)

Without an Affinity field, GMs cannot apply any of these rules without making judgment calls.

### Proposed Fix — Two Steps

**Step 1:** Add **Affinity** to the canonical stat block schema in the MM Introduction. It should appear after Type and before HP, formatted as:
> `**Affinity:** Spectral` or `**Affinity:** Material` or `**Affinity:** Hybrid`

**Step 2:** Designate every creature. Initial mapping:

| Affinity | Creatures |
| :--- | :--- |
| **Spectral** | All Ch. 2 creatures; Flamewraith (Ch. 1); Banshee (Ch. 1); SE-Feeder (Ch. 7) |
| **Hybrid** | Phase-Beast (Ch. 2 — native to the boundary between realms); Dimension-Walker (Ch. 1 — trained to cross realms); Void-Touched (Ch. 1 — body phases involuntarily) |
| **Material** | All Ch. 3 Mortals; All Ch. 5 Constructs; All Ch. 4 Beasts including Void-Stalker Cougar (phase ability is mutation, not true Spectral affinity); All Ch. 6 Hylden; All Ch. 7 Elementals (except SE-Feeder); All Ch. 8 Ancient Creatures (except where noted); All Ch. 9 Legendary Entities (review individually) |

Ch. 9 Legendary Entities require individual review — several (Elder God fragments, ancient wraith-lords) may warrant Spectral or Hybrid designation.

---

## Issue H — "Spectral Wilderness" Not in Glossary

**Severity:** Medium
**File:** `Monster_Manual/02_Spectral-Entities.md` (multiple entries), `player's_handbook/12_Glossary.md`

### The Problem
**Spectral Wilderness** is a recurring passive trait in Chapter 2, used on at least five creatures:
> *"Cannot be Grappled, Restrained, or knocked Prone by physical means. Immune to poison, disease."*

It functions as a keyword trait — the same text repeated verbatim — but it is never added to the Glossary. GMs and players have no single reference point for it, and it cannot be cross-referenced from class abilities or other chapters.

### Proposed Fix
Add a Glossary entry to `12_Glossary.md`:

> **Spectral Wilderness** *(Creature Trait)*
> The creature cannot be **Grappled**, **Restrained**, or knocked **Prone** by physical means. It is immune to poison and disease. Abilities that inflict these conditions via magical or Spectral means still function normally unless the stat block says otherwise.

Once the entry exists, individual stat blocks can reference it by name rather than repeating the full text.

---

## Issue I — "Spectral Sight" Not in Glossary; Naming Conflicts With "Soul Sight"

**Severity:** Medium
**Files:** `Monster_Manual/01_Undead-and-Vampiric.md`, `Monster_Manual/02_Spectral-Entities.md`, `player's_handbook/12_Glossary.md`

### The Problem
Multiple creatures have **Spectral Sight**: the ability to perceive creatures and features in both realms simultaneously, detecting living creatures through walls at a listed range.

Players and GMs also have **Soul Sight** (defined in Ch. 11 §11.5.4): the ability to perceive in the Spectral Realm's complete darkness as if in dim light.

These are two different abilities with similar names serving different functions. Neither is in the Glossary. At the table, "Spectral Sight" and "Soul Sight" will be confused by anyone who hasn't memorized both definitions.

### Proposed Fix
Add both to the Glossary with clear, distinct definitions:

> **Soul Sight** *(Character Trait)*
> While in the Spectral Realm, the character perceives their surroundings in complete darkness as if in dim light. Soul Sight is automatic for all Spectral and Hybrid Affinity characters. Material characters shifted into the Spectral Realm must spend a Bonus Action to attune their senses before gaining this benefit. *(Ch. 11 §11.5.4)*

> **Spectral Sight** *(Creature Trait)*
> The creature can perceive living creatures, Spectral entities, and hidden features in both the Material and Spectral Realms simultaneously, ignoring walls and obstacles within the listed range. This is a passive, always-on trait. It does not grant invisibility detection or bypass magical concealment unless the stat block states otherwise.

---

## Fix Priority Order

| Priority | Issue | Effort | Blocking |
| :--- | :--- | :--- | :--- |
| 1 | **C** — No Soul Bleed exemption for native Spectral creatures | Trivial — one sentence in 11.5.1 | Yes — all Ch. 2 encounters in the Spectral Realm are broken without it |
| 2 | **A** — Incorporeal vs 11.5 conflict | Small — one clarifying paragraph in 11.5.3 | Yes — GMs will apply wrong rules in every Spectral encounter |
| 3 | **G** — No Affinity field on stat blocks | Large — schema change + field on every Spectral/Hybrid creature | Yes — Issues C and F depend on it |
| 4 | **H** — Spectral Wilderness not in Glossary | Small — one Glossary entry | No |
| 5 | **I** — Spectral Sight / Soul Sight not in Glossary | Small — two Glossary entries | No |
| 6 | **D** — Phase-Beast partial phase note | Trivial — one note in stat block | No |
| 7 | **E** — Void-Touched partial phase uses different mechanics | Small — stat block update | No |
| 8 | **F** — Phase ability framework note | Small — one paragraph in MM Introduction | No |
| 9 | **B** — Banshee Incorporeal weaker than all others | Trivial — one-line decision | No |

---

## Recommended Fix Sequence

**Pass 1 — Rules Clarifications (PHB only, no MM edits):** ✅ Complete
- Issue C: Native Spectral Exception added to 11.5.1 (`11_Realms-Terrain-Arcane-Power.md` line 180)
- Issue A: Incorporeal clarification blockquote added to 11.5.3 (`11_Realms-Terrain-Arcane-Power.md` line 238)

**Pass 2 — Glossary (PHB only):** ✅ Complete
- Issue H: Spectral Wilderness entry added to 12.10 (`12_Glossary.md` line 482)
- Issue I: Soul Sight and Spectral Sight entries added to 12.10 (`12_Glossary.md` lines 476, 479)

**Pass 3 — MM Schema and Stat Blocks:**
- Issue G: Add Affinity field to MM Introduction schema, then designate every Spectral/Hybrid creature
- Issue B: Decide on Banshee Incorporeal — intentional or error
- Issue D: Add Phase-Beast note
- Issue E: Update Void-Touched crit effect
- Issue F: Add phase ability paragraph to MM Introduction

---

## Status

- **No source-file edits applied.** This document captures audit findings only.
- Pass 1 (Issues A and C) can be applied immediately — PHB-only changes, no stat block edits.
- Pass 2 (Issues H and I) can be applied immediately — Glossary additions only.
- Pass 3 requires a decision on Affinity designation before stat block edits begin.
- Ch. 9 Legendary Entities require individual review for Affinity designation before Pass 3 is complete.

---

*Audited against:* `Monster_Manual/00_Introduction.md` through `Monster_Manual/09_Legendary-Entities.md`, cross-referenced with `player's_handbook/11_Realms-Terrain-Arcane-Power.md` §11.5, `player's_handbook/12_Glossary.md`, `player's_handbook/02_Lineages-and-Race.md`, `player's_handbook/03_Classes.md`.
