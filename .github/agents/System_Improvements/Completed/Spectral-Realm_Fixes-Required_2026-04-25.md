# Spectral Realm — Fixes Required

**Date:** 2026-04-25
**Source:** Section 11.5 authoring review (Chapter 11: Realms, Terrain, and Arcane Power)
**Status:** Applied 2026-04-25 — All requested fixes implemented across PHB.

---

## Context

Section 11.5 (The Spectral Realm — Full Rules) was drafted as a major expansion to Chapter 11. During post-draft review, seven issues were identified where the new section introduces terms, tags, or mechanics that have no anchor elsewhere in the system. Each issue is documented below with the affected files and a concrete proposed resolution.

---

## Issue 1 — `crosses realms` Tag Not Applied to Any Ability

**Severity:** High — rules are unenforceable without it.

**Problem:** Section 11.5.3 (Combat Across Realms) and 11.5.6 (Spectral Action Restrictions) both reference abilities *"explicitly tagged crosses realms"* as exceptions to the cross-realm damage and targeting rules. No ability in Chapter 3 (Classes) or Chapter 2 (Lineages) currently carries this tag. A player looking at their Soul Reaver ability sheet would find nothing tagged, making the exception unenforceable at the table.

**Files Affected:**
- `player's_handbook/03_Classes.md` — Soul Reaver class abilities (primary)
- `player's_handbook/02_Lineages-and-Race.md` — Wraith Phasing (secondary, brief dip already exempt but tag clarifies edge cases)

**Proposed Fix:**
Audit Chapter 3 for abilities that should cross realms and add the tag inline. Minimum candidates:
- Soul Reaver: *Soul Storm*, *Reaver Drain*, *Spectral Lash*, any ability that explicitly targets souls or spectral essence
- Soul Reaver Blade item description (wherever it is formally defined — see Issue 7)
- Glyphwright: Glyphs already cross realms per 11.5.3, but abilities that *deploy* or *trigger* glyphs may need the tag for clarity

Tag format (consistent with existing ability tags in the table): add *(crosses realms)* to the ability description column.

---

## Issue 2 — `Spectral only` / `Material only` Tags Not Applied to Any Ability

**Severity:** Medium — Partial Shift rules reference them; without the tags the Partial Shift restriction has no teeth.

**Problem:** Section 11.5.5 (The Partial Shift State) states that while Partially Shifted, a character *"cannot use abilities tagged Spectral only or Material only."* Neither tag exists on any ability in the current PHB. The restriction is meaningless until abilities are tagged.

**Files Affected:**
- `player's_handbook/03_Classes.md` — all classes with realm-specific abilities
- `player's_handbook/02_Lineages-and-Race.md` — Wraith Phasing (Spectral only), Vampire subtype features (Material only candidates)

**Proposed Fix:**
Two options — pick one:

**Option A — Tag abilities:** Audit all class and lineage abilities. Apply *(Spectral only)* to abilities that require the Spectral Realm to function (e.g., Wraith Phasing extensions, soul-touch abilities) and *(Material only)* to abilities requiring physical presence (e.g., blood-feeding, physical grapples). This is thorough but requires a full audit pass.

**Option B — Rewrite 11.5.5 to avoid tags:** Replace the tag-based restriction with a functional description:
> *"You cannot use abilities that require you to be fully in one realm — for example, abilities that phase through walls, feed on blood, or require physical contact with a creature."*
This is lower maintenance but slightly less precise at the table. Recommended if a full ability audit is not planned immediately.

---

## Issue 3 — Soul Sight Not Referenced in the Wraith Lineage Entry

**Severity:** Medium — players read their lineage first; if it isn't there, they won't find it.

**Problem:** Section 11.5.4 defines **Soul Sight** as an automatic trait for all Spectral and Hybrid characters. The Wraith lineage in Chapter 2, Section 2.3 does not mention Soul Sight anywhere. A Wraith player reading their lineage entry would see nothing about it, then encounter it unexpectedly in Chapter 11.

**File Affected:**
- `player's_handbook/02_Lineages-and-Race.md` — Section 2.3 (Wraiths), Bonuses/Unique Trait block

**Proposed Fix:**
Add a single bullet to the Wraith entry under Bonuses or append to the Unique Trait block:
> *"**Soul Sight** (Passive): While in the Spectral Realm, you perceive your surroundings in complete darkness as if in dim light. See [Chapter 11, Section 11.5.4](./11_Realms-Terrain-Arcane-Power.md#1154-environmental-mirroring)."*

Also consider adding a shorter note to the Revenant lineage (Section 2.6) if Revenants are treated as Spectral-affined.

---

## Issue 4 — Partial Shift Not in the Conditions List or Glossary

**Severity:** Medium — functions as a named condition but has no glossary entry.

**Problem:** **Partial Shift** is a named state with specific mechanical restrictions (targetable by both realms, no realm defenses, restricted ability use, defined exit mechanic). All other named conditions in the game (Stunned, Grappled, Slowed, Frightened, etc.) have Glossary entries in Chapter 12. Partial Shift does not. GMs and players would have no single reference point for it.

**File Affected:**
- `player's_handbook/12_Glossary.md` — Conditions section

**Proposed Fix:**
Add a Glossary entry under Conditions:

> **Partial Shift:** A creature is Partially Shifted when it occupies both the Material and Spectral Realms simultaneously. While Partially Shifted: the creature is visible and targetable by creatures in both realms; all incoming damage applies regardless of type; abilities tagged *Spectral only* or *Material only* cannot be used; Soul Bleed applies at 1 HP per turn with no exceptions. A Partially Shifted creature may spend a Bonus Action and 1 SE to stabilize into one realm of its choice, ending this state. If it cannot, the state ends at the start of its next turn; it snaps into the realm it can best sustain (Spectral if below 50% HP, Material if above). Full rules: [Chapter 11, Section 11.5.5](./11_Realms-Terrain-Arcane-Power.md#1155-forced-realm-shifts).

---

## Issue 5 — "Full Action" Is Not a Defined Action Type

**Severity:** Low — clear intent, wrong term.

**Problem:** The Soul Portal crossing rule in Section 11.5.2 reads: *"Spend 1 SE and use a Full Action."* The game's defined action types are **Action, Bonus Action, Reaction, and Free Action**. "Full Action" does not exist. The intent is clear (it costs your Action for the turn and requires concentration), but the terminology is inconsistent with the rest of the system.

**File Affected:**
- `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.5.2, Soul Portals rule block

**Proposed Fix:**
Replace *"use a Full Action"* with *"use your Action"*:
> *"Spend **1 SE** and use your **Action**. This requires concentration — if you take damage before the start of your next turn, make a **DR 2 Will** save or the crossing fails and the SE is lost."*

---

## Issue 6 — Hybrid Affinity Has No Designated Owners

**Severity:** High — the Voluntary Shift rules in 11.5.2 are entirely gated on Hybrid Affinity, but no lineage or class is explicitly designated as Hybrid.

**Problem:** Section 11.5.2 (Voluntary Shift) opens with: *"Characters with Hybrid Affinity or specific abilities that allow voluntary realm-shifting."* Section 11.1 defines Hybrid as a third affinity type but lists no examples beyond *"Wraiths with Glyph-marked traits or ancient vampires like Kain."* No lineage in Chapter 2 is explicitly designated Hybrid Affinity. No class in Chapter 3 grants Hybrid Affinity. Players cannot determine whether their character qualifies for Voluntary Shift rules without GM arbitration.

**Files Affected:**
- `player's_handbook/02_Lineages-and-Race.md` — Lineage entries (primarily Wraith, possibly Revenant and Unbound)
- `player's_handbook/03_Classes.md` — Soul Reaver class (most likely Hybrid candidate)
- `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.1 (Hybrid definition) and Section 11.5.2 (Voluntary Shift)

**Proposed Fix:**
Two steps:

1. **Designate Hybrid Affinity owners explicitly** in Chapter 2 and/or Chapter 3. Candidates:
   - Soul Reaver (class) — manipulates souls across realms, uses Spectral weapons; strong Hybrid candidate
   - Wraith Lineage Paragon Level 20 (Wraith Lord) — *"exist in both realms simultaneously"* is a literal Hybrid description; Wraith Lord should grant Hybrid Affinity at Level 20
   - Unbound lineage — *"anomalies outside fate's pattern"*; possible Hybrid candidate
   - Any character with the *Phase Slip* universal perk — already lets you pass through solid objects; could trigger limited Hybrid rules

2. **Add a sidebar to Section 11.1** listing which lineages and classes have each affinity, so there is one canonical reference:
   > *Affinity by Lineage and Class: Material — Vampires, Humans, Hylden-Blooded, Revenants (default). Spectral — Wraiths. Hybrid — Wraith Lord (Level 20 Paragon), Soul Reaver class, Unbound lineage, characters with specific Hybrid-granting perks or abilities.*

---

## Issue 7 — Soul Reaver Blade Not Formally Defined

**Severity:** Medium — referenced in 11.5.3 as a special-case item but has no stat block or item entry.

**Problem:** Section 11.5.3 states: *"The Soul Reaver Blade and any ability explicitly tagged crosses realms deal full damage regardless of the attacker's or target's realm, and count as both Physical and Spectral for this table."* The Soul Reaver Blade is treated as a canonical named item with unique mechanical properties, but it has no item entry in the equipment chapter, no stat block in the Monster Manual, and no formal definition anywhere in the PHB. GMs and players cannot verify its base damage, damage type, special rules, or acquisition method.

**Files Affected:**
- Equipment chapter (wherever weapons are defined — confirm file path)
- `player's_handbook/03_Classes.md` — Soul Reaver class (should reference the blade)
- `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.5.3 (currently the only mechanical definition)

**Proposed Fix:**
Define the Soul Reaver Blade as a named legendary weapon in the equipment chapter with:
- Base damage and damage type (Spectral + Physical, crosses realms)
- Acquisition method (Soul Reaver class feature, or found/forged via narrative)
- Cross-reference to 11.5.3 for cross-realm combat rules
- Any additional properties (soul-drain on hit, interaction with Blood Points or Soul Energy)

Until formally defined, add an interim note to 11.5.3:
> *(The Soul Reaver Blade is a legendary weapon associated with the Soul Reaver class. Full item definition: [Chapter X: Equipment].)*

---

## Fix Priority Order

| Priority | Issue | Effort | Blocking |
|---|---|---|---|
| 1 | Issue 5 — "Full Action" terminology | Trivial (one-line edit) | No |
| 2 | Issue 3 — Soul Sight in Wraith lineage | Small (one bullet added) | No |
| 3 | Issue 4 — Partial Shift in Glossary | Small (one entry added) | No |
| 4 | Issue 6 — Hybrid Affinity owners | Medium (lineage + class audit) | Yes — Voluntary Shift rules are unusable without it |
| 5 | Issue 1 — `crosses realms` tag | Medium (class ability audit) | Yes — cross-realm exceptions are unenforceable without it |
| 6 | Issue 2 — `Spectral/Material only` tags | Medium (ability audit or 11.5 rewrite) | Partial — Partial Shift restriction is weakened without it |
| 7 | Issue 7 — Soul Reaver Blade definition | Large (new item entry) | No — interim note in 11.5.3 covers table use |

---

## Status

- **No source-file edits applied.** This document captures issues only.
- Issues 1, 2, and 6 require an ability audit pass across Chapters 2 and 3 before they can be closed.
- Issues 3, 4, and 5 are standalone edits that can be applied immediately without an audit.
- Issue 7 is a larger design task (equipment chapter) and may be deferred to a dedicated equipment pass.

---

*Identified during review of:* `player's_handbook/11_Realms-Terrain-Arcane-Power.md` Section 11.5, cross-referenced against `player's_handbook/02_Lineages-and-Race.md`, `player's_handbook/03_Classes.md`, `player's_handbook/12_Glossary.md`.
