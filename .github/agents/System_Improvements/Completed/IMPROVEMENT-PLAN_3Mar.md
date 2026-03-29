# Bloodbound TTRPG — Lore Improvement Implementation Plan

*Based on `lore/Lore-Improvement-Notes.md` cross-referenced against all system files.*
*Generated: 2026-03-03*

---

## Audit Summary

Many improvements from the Lore-Improvement-Notes have **already been applied** in earlier passes to the lore files. What remains is a set of concrete, scoped tasks. This plan lists every outstanding item, which files it touches, and the recommended execution order.

### Already Resolved (no further action)
- ✅ Melchiahim & Rahabim **lore** — full entries in `Lineage-Lore.md`
- ✅ Warden of Balance **depth** — extensively expanded in `Class-Lore.md`
- ✅ Nomad Memory-Threads — full rewrite in `Lineage-Lore.md`
- ✅ Unbound grounding — splinter-soul origin in `Lineage-Lore.md`
- ✅ Clan count in `World-Primer.md` — all 6 clans listed
- ✅ Cultural touchstones per lineage — present for all clans
- ✅ Per-lineage Goals/Problems table — present in `Lineage-Lore.md`
- ✅ Crimson Fracture — described in `World-Primer.md`
- ✅ Pale Accord — explained as reformed Circle
- ✅ Zephonim → Shadowmancer connection — explained in `Lineage-Lore.md`

---

## Phase 1 — Critical Gaps (Mechanics & Consistency)
> These are blocking inconsistencies where lore exists but the mechanical system hasn't caught up.

### Task 1.1 — Add Melchiahim & Rahabim Mechanical Stats
**Priority:** 🔴 Critical
**Files:**
- `player's_handbook/02_Lineages-and-Race.md` — Add full mechanical stat blocks for Melchiahim and Rahabim vampire subtypes, matching the format of Razielim/Turelim/Dumahim/Zephonim.
- `assets/CONTEXT.md` — Add Melchiahim and Rahabim to the Lineages section under Vampire subtypes.

**Source material:** `lore/Lineage-Lore.md` (Melchiahim: flesh-weaving, decay resistance, graft mechanics; Rahabim: aquatic adaptation, amphibious movement, current-based communication).

**Design notes:**
- Melchiahim traits should reflect flesh-shaping survivability (e.g., bonus to Fortitude, unique "Graft" ability, penalty to social interactions due to decay).
- Rahabim traits should reflect aquatic mastery (e.g., swim speed, water breathing, bonus in flooded/wet environments, penalty in arid environments).

### Task 1.2 — Add Revenants & Unbound to Character Creation
**Priority:** 🟡 Medium
**Files:**
- `player's_handbook/01_Character-Creation.md` — Step 2 (Choose a Race) currently lists only Vampire, Human, Wraith, Hylden-Blooded. Add **Revenant** and **Unbound** to match Chapter 02 and lore files.

---

## Phase 2 — Missing World Content
> Locations, factions, and creatures that the Lore-Improvement-Notes identified as absent.

### Task 2.1 — Add Iconic Locations to World-Primer
**Priority:** 🟡 Medium
**Files:**
- `lore/World-Primer.md` — Key Locations section.

**Locations to add (5):**
1. **The Sanctuary of the Clans** — Ancient neutral meeting place, built around the tomb of the original Pillar Guardians.
2. **Avernus Cathedral** — Once-holy, corrupted by demonic influence and home to the cult of Hash'ak'gik.
3. **Dumah's Fortress** — Silent, ruinous seat of the Dumahim; site for rediscovery or plunder.
4. **Uschtenheim** — Mountain home of the original Vampire Hunters; significant for Sarafan and vampire history.
5. **The Chronoplast** — Moebius's time-streaming chamber; source of temporal paradoxes.

Also: formalize **Pillar geography** — name the physical location (e.g., "The Heart of Nosgoth" or "Pillar Heath") and anchor it on the regional map in the west.

### Task 2.2 — Add Hash'ak'gik as Faction/Threat
**Priority:** 🟡 Medium
**Files:**
- `lore/World-Primer.md` — Add as a subfaction or independent threat entry. A powerful, manipulative demon and "B-plot" antagonist.
- `GM_Guide/02_Encounter-Design.md` — Consider adding Hash'ak'gik cult encounter seeds.
- `Monster_Manual/03_Mortals-and-Cultists.md` — Add cult of Hash'ak'gik stat blocks (acolytes, possessed, cult leader).

### Task 2.3 — Add The Sluagh to Monster Manual
**Priority:** 🟡 Medium
**Files:**
- `Monster_Manual/02_Spectral-Entities.md` — Add the Sluagh (carrion-feeders of the Spectral Realm). Include stat block, lore, tactics, and encounter guidance. Essential for any party interacting with the spirit world.

### Task 2.4 — Add Vampire Thralls/Worshippers Social Layer
**Priority:** 🟢 Low
**Files:**
- `lore/Lineage-Lore.md` — Add a subsection under Vampires describing the human servant class within vampire society (blood-bound thralls, willing worshippers, forced servants).
- `lore/World-Primer.md` — Reference thralls in the Vampire Clans faction description.
- Optionally: `Monster_Manual/03_Mortals-and-Cultists.md` — Vampire Thrall NPC stat block.

---

## Phase 3 — Internal Inconsistencies
> Contradictions or disconnects that weaken the system's coherence.

### Task 3.1 — Sharpen Dreadblade vs. Shadowmancer Distinction
**Priority:** 🟡 Medium
**Files:**
- `lore/Class-Lore.md` — Dreadblade entry. Explicitly address why a Zephonim could be either class and what makes them different.

**Recommended approach:** Dreadblade = **martial executioner** shaped by *war and trauma* (Sarafan past or battlefield curse). Shadowmancer = **arcane manipulator** shaped by *Zephonim culture and shadow philosophy*. A Zephonim Dreadblade rejected the web-spire life; a Shadowmancer *embodies* it. Add a "Distinguishing the Two" callout box.

### Task 3.2 — Connect Hylden Remnants to Hylden Rationalism
**Priority:** 🟢 Low
**Files:**
- `lore/World-Primer.md` — Add cross-references between the Hylden Remnants faction entry and the Hylden Rationalism religion entry. Clarify: Rationalism is the *philosophical framework* of the Remnants, but not all who adopt Rationalist thought are Hylden loyalists (some human scholars subscribe to it).

---

## Phase 4 — Class-Lineage Integration
> Deepening how classes connect to their lineage origins.

### Task 4.1 — Sharpen Glyphwright vs. Hylden Warlock Distinction
**Priority:** 🟡 Medium
**Files:**
- `lore/Class-Lore.md` — Both entries.

**Recommended approach from Improvement Notes:**
- **Glyphwright → Engineer/Scholar.** Not channeling Hylden power but reverse-engineering ancient *technology*. Risk = madness from incomprehensible physics, not corruption from malevolent forces.
- **Hylden Warlock → Conduit/Apostate.** Direct pacts with Hylden entities or the entropic void. Power = raw, chaotic, deeply corrupting.
- Add a "Distinguishing the Two" callout, similar to Task 3.1.

### Task 4.2 — Add Soul Reaver In-Game Origin Pathway
**Priority:** 🟢 Low
**Files:**
- `lore/Class-Lore.md` — Soul Reaver entry.
- `GM_Guide/03_Character-Progression.md` — Add guidance for mid-campaign class change to Soul Reaver.

**Content:** Characters who die and are resurrected under specific soul-scarring circumstances (consumed by the Abyss, dying near a shattered Pillar, surviving a Soul Reaver's feeding) could become Soul Reavers. This creates an organic progression hook rather than requiring it at character creation.

---

## Phase 5 — Faction Coherence
> Making factions more GM-usable with explicit conflict relationships.

### Task 5.1 — Add "Conflicts With:" to Each Faction
**Priority:** 🟡 Medium
**Files:**
- `lore/World-Primer.md` — All 7 faction entries.

**Format (per improvement notes):**
> **Sarafan Order.** *Conflicts with: Vampire Clans (eradication goal), Pale Accord (branded heretics), Hylden Remnants (unholy alien presence). Zealotry makes negotiation nearly impossible, but individual commanders may be corruptible.*

Apply to: Sarafan Order, Vampire Clans, Hylden Remnants, Circle of Nine / Pale Accord, Crimson Fracture, Elder God / Cult of the Wheel, Outcasts & Guilds.

### Task 5.2 — Expand Faction NPCs in GM Guide
**Priority:** 🟢 Low
**Files:**
- `GM_Guide/05_NPC-Compendium.md` — Add representative NPCs for each major faction (Sarafan commander, Crimson Fracture elder, Pale Accord scholar, Hylden agent, Guild contact). Follow the existing legendary NPC format but scaled to "faction leader" tier.

Also consider adding NPC entries for: Ariel, Janos Audron, Mortanius, Nupraptor (mentioned in World-Primer but not in Compendium).

---

## Phase 6 — Tone & Voice Polish
> Improving the evocative quality of specific entries.

### Task 6.1 — Darken Glyphwright Voice
**Priority:** 🟢 Low
**Files:**
- `lore/Class-Lore.md` — Glyphwright entry. Replace functional language like "engineers of structured magic" with more evocative text. Consider applying the rewrite from Improvement Notes Section 8.
- `player's_handbook/03_Classes.md` — Update the Glyphwright flavour blurb to match.

**Optional:** Consider renaming to *Glyphwright* or *Rune Scourge* (per improvement notes). This would be a sweeping rename across all files — **only do this if the team agrees on the new name**.

### Task 6.2 — Expand Hylden Rationalism
**Priority:** 🟢 Low
**Files:**
- `lore/World-Primer.md` — Hylden Rationalism religion entry. Current version is 4 lines. Expand to match the gothic weight of Defiant Creed and Razielite Martyrdom (both ~6–8 lines with rituals and emotional depth). Add: what Rationalists believe about souls, their relationship to the Pillars, why other factions find them threatening.

---

## Execution Order (Recommended)

| Order | Task | Phase | Priority | Estimated Scope | Status |
|:---:|:---|:---:|:---:|:---|:---:|
| 1 | 1.1 — Melchiahim/Rahabim stats | 1 | 🔴 | ~80 lines across 2 files | ✅ Done |
| 2 | 1.2 — Character Creation races | 1 | 🟡 | ~10 lines in 1 file | ✅ Done |
| 3 | 2.1 — Iconic locations | 2 | 🟡 | ~50 lines in 1 file | ✅ Done |
| 4 | 3.1 — Dreadblade/Shadowmancer | 3 | 🟡 | ~15 lines in 1 file | ✅ Done |
| 5 | 4.1 — Glyphwright/Warlock | 4 | 🟡 | ~20 lines in 1 file | ✅ Done |
| 6 | 5.1 — Faction "Conflicts With" | 5 | 🟡 | ~30 lines in 1 file | ✅ Done |
| 7 | 3.2 — Hylden Remnants/Rationalism | 3 | 🟢 | ~10 lines in 1 file | ✅ Done |
| 8 | 2.2 — Hash'ak'gik | 2 | 🟡 | ~40 lines across 2–3 files | ✅ Done |
| 9 | 2.3 — Sluagh | 2 | 🟡 | ~40 lines in 1 file | ✅ Done |
| 10 | 4.2 — Soul Reaver origin pathway | 4 | 🟢 | ~15 lines across 2 files | ✅ Done |
| 11 | 6.1 — Glyphwright voice | 6 | 🟢 | ~15 lines across 2 files | ✅ Done |
| 12 | 6.2 — Hylden Rationalism tone | 6 | 🟢 | ~10 lines in 1 file | ✅ Done |
| 13 | 2.4 — Vampire Thralls | 2 | 🟢 | ~20 lines across 2 files | ✅ Done |
| 14 | 5.2 — Faction NPCs | 5 | 🟢 | ~100 lines in 1 file | ✅ Done |

**Total estimated scope:** ~450–500 lines of new or revised content across ~10 files.

> **Implementation complete — 2026-03-03.** All 14 tasks executed across 10+ files. ~600 lines of new content added. No renaming of Glyphwright was applied (requires team approval).

---

## Agent Workflow

When using an AI agent to execute this plan:

1. **Work phase-by-phase, task-by-task.** Complete one task fully before moving to the next.
2. **For each task:**
   - Read the target file(s) and the relevant section of `Lore-Improvement-Notes.md`.
   - Read the corresponding lore source (`Lineage-Lore.md`, `Class-Lore.md`, `World-Primer.md`) for canonical tone and format.
   - Draft content matching the existing file's structure, heading level, and voice.
   - Apply edits and verify no new inconsistencies are introduced.
3. **Cross-reference after each phase.** After completing a phase, verify that `CONTEXT.md` and `World-Primer.md` remain consistent with all changes.
4. **Do not rename "Glyphwright"** without explicit approval — it requires a global find-and-replace across every file.
5. **Preserve existing mechanical balance.** Melchiahim/Rahabim stats should mirror the power level of existing vampire subtypes, not exceed them.
6. **Flag decisions for review.** Where the Improvement Notes suggest multiple directions (e.g., Crimson Fracture: feral nihilism vs. realm-merging), note the choice made and why.

---

*Source: `lore/Lore-Improvement-Notes.md` — cross-referenced against all system files as of 2026-03-03.*
