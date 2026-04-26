# PHB Balance & Polish Recommendations

**Date:** 2026-04-25
**Scope:** Four flagged design items remaining after the System Review Checklist completion pass.
**Status:** Applied 2026-04-25 — All recommendations implemented in `player's_handbook/` and `GM_Guide/` (if applicable).

---

## Context

The `System_Review_Checklist.md` was marked complete after Rounds 1–5 of the systemic review and the Monster Manual Improvement Plan reached "Definition of Done." During the post-completion balance/polish review, four items remained as genuinely open design questions distinct from the closed structural review:

1. Siege Incarnate vs Blood Tyrant parity (Blood Knight L20 capstones)
2. Crit frequency at Level 20 against low-DV targets
3. Glyphwright `Prime Weaver` (L20) vagueness
4. Wraith `+1 Will` attribute bonus at character creation

Each is documented below with the current source text, diagnosis, and a concrete proposed replacement.

---

## 1. Siege Incarnate vs Blood Tyrant Parity

**File:** `player's_handbook/03_Classes.md` line 91
**Sibling option:** line 90 (Blood Tyrant)

### Current Text
> `| 20 | *or* **Siege Incarnate** | You are immune to forced movement, knockback, and being **Grappled**. Your melee attacks ignore all Armor. Conscious allies within 15 feet of you gain +1 DV while they remain in the aura. | Passive |`

### Diagnosis
Blood Tyrant gates its peak power behind `1/long rest, 1 min`. Siege Incarnate grants armor-ignore as a permanent passive — strictly stronger than Blood Tyrant's per-attack ceiling because there is no duration limit and no resource cost. The asymmetry is structural, not numerical: one option is timed, the other is not. They are not comparable choices.

### Recommended Replacement
> `| 20 | *or* **Siege Incarnate** | Passive: You are immune to forced movement, knockback, and being **Grappled**. Conscious allies within 15 feet gain +1 DV while in the aura. Active (1/long rest, 1 min): Siege Stance — your melee attacks ignore all Armor, and you cannot be moved against your will by any effect short of Legendary force. | Passive + Action, 1/long rest |`

### Rationale
- Movement immunity and the +1 DV aura stay passive — these are flavor-defining battlefield-presence effects with low disruption.
- Armor-ignore moves into the activation window, parallel to Blood Tyrant's "1 min of overwhelming force."
- The Legendary-force clause gives the activation an extra ceiling so it does not feel like a strict downgrade for existing builds.
- Both L20 options now share the structure: permanent passive identity + timed activation peak.

---

## 2. Crit Frequency at Level 20

**Files:** `player's_handbook/03_Classes.md` lines 308 & 328; rule reference in `09_Combat.md`

### Current State
- Crit rule: exceed DV by 2+ successes
- L9 `Auto-Crit From Stealth` (Dreadblade): hit-from-Stealth = automatic Critical Hit
- L10 `Perfect Kill` (Dreadblade): x3 crit damage; once per short rest, mark a target so the next hit becomes a crit
- L14 `Vitals Seeker` (Dreadblade): always-on threshold reduction to DV+1

### Diagnosis
Probability sketch with a 14-die pool (p ≈ 1/3 per die):
- vs DV 6 (Boss): ~3% crit chance — appropriately rare
- vs DV 3 (mook): ~65% crit chance
- With Vitals Seeker active vs DV 3: ~80%

Stacked with Auto-Crit From Stealth and Perfect Kill, the L14+ Dreadblade effectively crits on every hit against rank-and-file enemies. No design note exists declaring this intentional, so it reads as oversight.

### Recommended Replacement (Vitals Seeker, line 328)
> `| 14 | **Vitals Seeker** | When you have Advantage on the attack roll OR have a marked target from Perfect Kill, your **Critical Hit** threshold is reduced by 1 (exceed DV by 1+ successes instead of 2+). | Passive |`

### Recommended Addition (`09_Combat.md` Critical Hits sidebar)
> *GM Note — Crit Scaling by DV:* The 2+ success crit threshold means high-level characters will crit frequently against low-DV enemies (mook tier, DV 2–3) and rarely against high-DV enemies (Boss/Legendary, DV 5–6). This is intentional — capstone characters should feel devastating against weaker foes while elite enemies remain a real threat. When designing encounters, calibrate enemy DV to the experience you want at the table: a swarm of DV 3 mooks is a victory lap; a DV 6 Boss is a real fight.

### Rationale
- Vitals Seeker remains impactful — Dreadblades routinely set up Advantage via Stealth, flanking, and Perfect Kill marks — but the bonus is no longer free, always-on.
- Anchoring on a setup condition creates positional play: players want Advantage *because* it unlocks the better crit math.
- The sidebar converts the open question into documented intent and gives GMs encounter-design guidance.
- No changes needed to the base crit rule, Auto-Crit From Stealth, or Perfect Kill — they remain the high-skill payoff for a stealth-built Dreadblade.

---

## 3. Prime Weaver Vagueness

**File:** `player's_handbook/03_Classes.md` line 292
**Sibling option:** line 293 (Living Matrix)

### Current Text
> `| 20 | **Prime Weaver** | Enhance all glyphs (Max damage, Harder Saves). | Action, 1/long rest |`

### Diagnosis
Compared to its sibling `Living Matrix` (which fully specifies glyph count, detection rules, trigger type, and refresh), Prime Weaver defines none of its parameters:
- "Max damage" is ambiguous — max die face vs. max possible roll vs. flat ceiling?
- "Harder Saves" gives no DR magnitude.
- No duration is stated.
- No rule for whether new glyphs placed during the effect benefit.

The ability is not runnable at the table without GM improvisation.

### Recommended Replacement
> `| 20 | **Prime Weaver** | For 10 minutes, you reach absolute glyph mastery: all of your active glyphs treat their damage dice as if they rolled their highest face (maximum base damage), and the save DR of all your active glyphs increases by **+1**. New glyphs you place during this duration also benefit. | Action, 1/long rest |`

### Rationale
- **Duration:** 10 minutes — bounded, matches typical Action-activated capstone windows.
- **Damage definition:** Maximum die face (not max possible result) — keeps the upper bound predictable and prevents stacking with other multipliers from blowing up the math.
- **Save magnitude:** +1 DR — modest, fits within the existing save-target curve without invalidating boss saves.
- **Scope:** Newly placed glyphs benefit — rewards mid-fight redeployment without forcing pre-combat setup.
- Prime Weaver is now mechanically distinct from Living Matrix (sustained burst vs. permanent stealth-deployment) so the L20 choice is meaningful.

---

## 4. Wraith `+1 Will` at Creation

**File:** `player's_handbook/02_Lineages-and-Race.md` line 73

### Current Text
> `- **Bonuses**: +1 Possession, +1 Observation, +1 Will.`

### Diagnosis
Wraiths are the only lineage receiving an attribute bonus at character creation. Every other lineage receives skill/movement/utility bonuses. Will feeds directly into DV, so a Level 1 Wraith begins with structurally higher resilience than every other PC at the table. The disparity softens over time as other PCs gain attribute increases, but it is most pronounced at Levels 1–5 — the most-played tier.

### Recommended Replacement — Two Options

#### Option A — Keep, Document Intent (Recommended)
> `- **Bonuses**: +1 Possession, +1 Observation, +1 Will. *(The Will bonus reflects the Wraith's innate spiritual resonance and is intentional — Wraiths begin more resistant to mental and spiritual effects in exchange for their physical fragility, low base movement, and Soul Energy dependency.)*`

#### Option B — Strict Parity Rebalance
> `- **Bonuses**: +1 Possession, +1 Observation, and +1 to one Skill of your choice.`

### Rationale
- **Option A** is the recommended path. Wraith fragility is genuine: Soul Energy needs, the Anchor mechanic with Corruption risk, the lowest base movement among lineages. The +1 Will is a real counterweight, and documenting it converts the flag from "open question" to "owned design choice" with zero mechanical revision risk.
- **Option B** drops the attribute cascade entirely and matches Human-style flexibility. Players who want a Phasing-heavy build still pump Will at level-up like any other class invests into its key attribute. Use this option only if early-game playtests confirm Wraith DV is meaningfully outperforming other lineages at Levels 1–5.

---

## Implementation Order

| Priority | Item | Risk | Effort |
|---------|------|------|--------|
| 1 | Prime Weaver rewrite | None — pure clarity fix | One-line table replacement |
| 2 | Siege Incarnate split | Low — restores parity, predictable impact | One-line table replacement |
| 3 | Vitals Seeker condition + GM sidebar | Low — small behavior anchor | Two small edits |
| 4 | Wraith bonus (Option A) | None — parenthetical clarification | One-line edit |

All four are low-risk text edits with no cascading revisions to the Monster Manual, encounter math, or DV tables.

---

## Status

- **No source-file edits applied.** This document captures recommendations only.
- **Approval required** before any of the above changes are made to `02_Lineages-and-Race.md`, `03_Classes.md`, or `09_Combat.md`.
- **Playtest dependency:** Item 4 (Wraith bonus) recommendation is conditional on early-tier playtest data; default to Option A absent contrary evidence.

---

*Reviewed against:* `System_Review_Checklist.md`, `Jack_Notes.md`, `player's_handbook/02_Lineages-and-Race.md`, `player's_handbook/03_Classes.md`, `player's_handbook/09_Combat.md`.
