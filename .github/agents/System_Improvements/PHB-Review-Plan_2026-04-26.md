# PHB Full System Review Plan — 2026-04-26

Structured multi-session audit plan for all 13 Player's Handbook chapters. Chapters are ordered by dependency — foundational systems first, reference last. Each chapter entry defines focus areas, cross-chapter interaction checks, complexity estimate, and known pre-existing issues spotted during earlier work.

**Completed:** Ch. 5 (Spellcasting & Magic) — 59 issues found and fixed. Ch. 11 (Realms, Terrain, Arcane Power) — core Spectral Realm rules written and audited.

---

## Dependency Map

```
Ch. 0 (Core Mechanics)
  └── Ch. 9 (Combat)
  └── Ch. 10 (Dice System)
  └── Ch. 2 (Lineages)
        └── Ch. 1 (Character Creation)
              └── Ch. 3 (Classes)
                    └── Ch. 4 (Perks)
                    └── Ch. 6 (Skills)
                    └── Ch. 8 (Corruption)
  └── Ch. 7 (Equipment)
  └── Ch. 12 (Glossary) ← review last
```

Ch. 5 ✅ and Ch. 11 ✅ are complete. All others are Open.

---

## Tier 1 — Foundation
*Review these first. Issues here cascade into every other chapter.*

---

### Ch. 0 — Core Mechanics
**Status:** Open | **Priority:** 1 | **Complexity:** Medium | **Estimated Passes:** 3

The d6 dice pool, 6 attributes, DR vs DV framework, and combat bonus form the mathematical spine of the entire game. Any errors or ambiguities here propagate into every other chapter.

**Focus Areas:**
- Dice pool math — is the average successes-per-die (≈0.33) consistent with the DR/DV ranges used throughout the game?
- Attribute caps and progression — is the max attribute (5 or 6?) consistent across Ch. 0, Ch. 2 (lineage paragons say "max 6"), and Ch. 3 (class ability language)?
- Combat Bonus — how it's defined, what it applies to, and whether Ch. 3 class abilities and Ch. 5 spells apply it correctly
- DR vs DV distinction — confirmed as consistent in Ch. 5; verify it's clean in Ch. 0's own definitions
- Stunt system — how extra successes create stunts, and whether this is defined completely (or left to GM interpretation)
- Push mechanic — how it interacts with Corruption Dice (Ch. 8 dependency); is the risk/reward defined here or only in Ch. 8?

**Cross-Chapter Checks:**
- Attribute modifier formula from Ch. 5 §5.2 (+0/+1/+2 by score) — does Ch. 0 define this same formula?
- "Half your level" calculations — used for SE/BP caps (Ch. 5), check if defined in Ch. 0 or only in Ch. 5
- Bloodied condition threshold — referenced in Ch. 2 lineage traits; defined where?

**Known Pre-existing Issues:**
- Attribute max of 6 referenced in Ch. 2 lineage paragons ("max 6") — Ch. 0 may state 5 as the cap; needs reconciliation

---

### Ch. 9 — Combat
**Status:** Open | **Priority:** 1 | **Complexity:** Very High | **Estimated Passes:** 5–6

The full combat ruleset: action economy, initiative, damage types, all conditions, critical hits, environmental combat. This chapter is the most likely to have undefined interactions, since Ch. 5's 59-issue audit repeatedly referenced conditions (Staggered, Paralyzed, Prone) and damage types (Spectral, Entropic, Radiant, Force) that live here.

**Focus Areas:**
- **Condition definitions** — are all conditions from the Glossary (Ch. 12) actually defined with mechanical text here? We found Staggered was missing from Ch. 12; verify the source definitions in Ch. 9 are complete
- **Damage type interactions** — Spectral, Entropic (Void), Radiant, Force, Elemental subtypes (Fire/Cold/Lightning), Physical subtypes (Bludgeoning/Piercing/Slashing). Each has a distinct interaction pattern with Armor, Resistance, and Immunity; check they are all defined consistently
- **Action economy** — Action, Bonus Action, Reaction, Free Action. Is "Free Action" formally defined? (Used in Ch. 5 spells like Glyph of Unmaking's command trigger)
- **Initiative** — how it's determined, what attributes/skills contribute, tie-breaking
- **Critical hits** — 3+ successes or DV exceeded by 2+; do these match Ch. 5's §5.4 Critical Spell Effects language?
- **Bloodied threshold** — what HP percentage triggers it? Referenced in Ch. 2 lineage traits and Ch. 5 spells but may only be defined here
- **Environmental combat** — how terrain interacts with attack/defense; cross-reference Ch. 11 terrain types
- **Opportunity attacks** — when triggered, how resolved; several Ch. 5 spells suppress them (Wraithwalk, Soul Flicker)
- **Death and dying** — 0 HP rules, stabilization, death saves (if any)
- **Two-weapon fighting, grappling, shoving** — are these defined with complete mechanics?

**Cross-Chapter Checks:**
- Every condition used in Ch. 5 spells — verify each has a definition in Ch. 9 or Ch. 12
- Damage type resistance/immunity table from Ch. 11 §11.5.3 — does it align with Ch. 9's damage type rules?
- Ch. 5 Mastery Piercing (ignores 3 Armor) and Mastery Bypass (treats Immunity as Resistance) — do Ch. 9's Armor and Immunity rules accommodate these overrides?
- "TV" (Threat Value) — used in Ch. 5 §5.7 feeding economy; defined where?

**Known Pre-existing Issues:**
- "Free Action" used in multiple Ch. 5 spells; may not be defined in Ch. 9
- "Bloodied" condition used in Ch. 2 and Ch. 5 but never explicitly defined with a percentage threshold in anything reviewed so far

---

### Ch. 10 — Dice System
**Status:** Open | **Priority:** 1 | **Complexity:** Low | **Estimated Passes:** 1–2

Quick reference chapter that largely overlaps Ch. 0 and Ch. 9. Primary risk is consistency drift — if Ch. 0 or Ch. 9 was updated since Ch. 10 was written, Ch. 10 may have stale examples or different numbers.

**Focus Areas:**
- Does every rule described in Ch. 10 match the current text in Ch. 0 and Ch. 9?
- Are the worked examples accurate given current attribute caps and DR ranges?
- Is there any content in Ch. 10 not present in Ch. 0 or Ch. 9 that should be migrated?

**Cross-Chapter Checks:**
- DR formula, DV definition, combat bonus — verify against Ch. 0
- Stunt examples — verify against Ch. 9 critical hit rules

---

## Tier 2 — Character Building
*Review after Tier 1. These define what characters are.*

---

### Ch. 2 — Lineages & Race
**Status:** Open | **Priority:** 2 | **Complexity:** Medium | **Estimated Passes:** 3

Six lineages with subtypes, affinity assignments, and paragon abilities at levels 10 and 20. We read this chapter fully during the Spectral Realm session and made one fix (Revenant Soul Bleed cross-reference). Closer audit is still needed.

**Focus Areas:**
- **Lineage balance** — compare each lineage's trait bundle: movement, stealth bonus, movement effects, unique trait, and 2 paragon levels. Are they roughly equivalent in power? (Wraith gets +1 Will on top of +1 Possession, +1 Observation — three bonus skill/attribute points vs. Vampire's +1 Weapon Mastery, +1 Stealth)
- **Paragon ability language** — "max 6" appears in paragon text for attribute gains. Does Ch. 0 confirm 6 as the maximum? "Your X bonus increases to +2" at level 20 — what does this mean exactly for traits like Predatory Perfection?
- **Unique trait economy** — once-per-round BP gain for Vampires, Wraith Phasing uses, Unbound Probability Shift. Are these balanced against each other?
- **Subtype features** — each vampire subtype has 1–2 features. Check for undefined mechanics (e.g., Melchiahim's Corruption-on-failure, Rahabim dryness vulnerability per-hour damage)
- **Affinity assignments** — Wraith (Spectral → Hybrid at Level 20), Revenant (Spectral), Unbound (Hybrid). Do these match Ch. 11's Hybrid Affinity rules for realm-shifting?
- **"+1 die" language** — several lineage features grant "+1 die" to specific rolls. Is "die" consistently used throughout (vs. "success" or "bonus")?
- **Anchor mechanic (Wraith)** — "Full rules: Lineage Lore - Wraiths" referenced but that document may not exist. Is the Anchor mechanic fully defined in Ch. 2 or does it rely on a missing document?

**Cross-Chapter Checks:**
- Wraith Phasing vs. Ch. 11 §11.5.2 Voluntary Shift rules — Wraith Phasing is defined as a "brief controlled dip" that doesn't trigger Soul Bleed. Verify the Ch. 2 and Ch. 11 descriptions are mutually consistent
- Revenant Unyielding Purpose ("once per arc, when reduced to 0 HP, drop to 1 HP instead") — does Ch. 9 define "arc"?
- Hylden-Blooded movement effect ("roll 1 Corruption Die, on 1 gain 1 Corruption") — verify this is consistent with Ch. 8 Corruption Dice rules

**Known Pre-existing Issues:**
- Wraith gets +1 Will in addition to +1 Possession and +1 Observation — three bonus allocations vs. other lineages' two. May be intentional given Wraith's physical fragility, but unacknowledged.
- "Lineage Lore - Wraiths" referenced for Anchor mechanic full rules — this document may not exist.

---

### Ch. 3 — Classes
**Status:** Open | **Priority:** 2 | **Complexity:** Very High | **Estimated Passes:** 5–6

Seven classes, each with level progression tables, signature abilities, and spell access tags. This is the largest chapter in the PHB and the most likely source of undocumented interactions. Every Ch. 5 spell access tag was verified against these class lists; now we need to go the other direction — verify class abilities against the spell compendium, Ch. 9 combat rules, and Ch. 4 perks.

**Focus Areas:**
- **Signature Upgrades** — each class has Signature Upgrade versions of base Ch. 5 spells. Do all Signature Upgrades reference the correct base spell? Do they add defined mechanics or use undefined shorthand?
- **Level progression tables** — check that every ability entry has a definition somewhere (in the class entry or cross-referenced to another chapter)
- **Class-specific resource rules** — Soul Reaver's SE generation from kills, Sangromancer's feeding mechanics, Shadowmancer shadow-step rules. Are these fully defined or do they reference undefined game terms?
- **Passive vs. active abilities** — which class features require an Action/Bonus Action, and which are passive? Are all action types specified?
- **Spell access tags** — we already confirmed Ch. 5 tags match class lists during the Pass 8 audit. Do a reverse check: does every spell-tag in Ch. 3 class lists exist in Ch. 5?
- **Class-specific conditions or mechanics** — e.g., the Soul Reaver's Soul Meter (if it has one), the Sangromancer's Bloodied synergy. Are these fully defined here?
- **Multiclass rules** (if any) — does the system support multiclassing, and if so, how are class ability prerequisites handled?

**Cross-Chapter Checks:**
- Every Signature Upgrade vs. its base Ch. 5 spell — verify the upgrade adds defined mechanical benefit, not just "improved version"
- Ch. 4 perk access — do class entries list which perk tiers they unlock and at what levels?
- Ch. 8 Corruption interaction — classes that use Forbidden spells (HW, SM) have implied Corruption risk; verify the class entries acknowledge this

**Known Pre-existing Issues:**
- Shadowmancer's glyph access added during Ch. 5 fix (Glyph of Displacement, Glyph of Entropy, Glyph of Silence) — verify Ch. 3 Shadowmancer class list was updated to match
- Sangromancer's Spectral restriction added to Ch. 5 §5.7 — verify Ch. 3 Sangromancer entry acknowledges this

---

### Ch. 1 — Character Creation
**Status:** Open | **Priority:** 2 | **Complexity:** Medium | **Estimated Passes:** 2–3

The end-to-end character creation process: point buy, starting stats, lineage and class selection. This chapter largely assembles rules from other chapters — its main risks are procedural gaps, incorrect cross-references, and starting power imbalance.

**Focus Areas:**
- **Point buy math** — how many points, what each attribute costs, what the starting floor and ceiling are. Does the budget produce viable characters across all lineage/class combos?
- **Starting resources** — starting SE, starting BP, starting HP. Do these match the formulas in Ch. 5 §5.7?
- **Starting spells** — the creation process should specify how many starting spells each caster gets and from which tiers. Does Ch. 1 direct players to their class entry, or define this here?
- **Lineage + class compatibility** — are there any lineage/class combos that are functionally broken at character creation? (e.g., Sangromancer Wraith — all spells BP-locked in Spectral Realm, Wraith has Spectral Affinity)
- **Starting perk allocation** — does Ch. 1 specify starting perks, or only list them at level 1 in Ch. 4?
- **Creation sequence** — is the step-by-step sequence complete and unambiguous? Are there steps that reference unavailable information?

**Cross-Chapter Checks:**
- Starting HP vs. Ch. 9 death rules — is starting HP high enough that level 1 characters are viable?
- Attribute modifier table from Ch. 5 §5.2 — is this (or an equivalent) reproduced in Ch. 1 or Ch. 0 for character creation use?

---

## Tier 3 — Character Options
*Review after Tier 2. These define what characters can do.*

---

### Ch. 8 — Corruption
**Status:** Open | **Priority:** 3 | **Complexity:** High | **Estimated Passes:** 3–4

Corruption levels 0–15, Corruption Dice, Corrupted Perks, pushing rolls, and purification paths. This chapter was referenced constantly during the Ch. 5 audit — we patched Corruption-related issues in spells without reading Ch. 8 directly. Now it needs a standalone review.

**Focus Areas:**
- **Corruption level tiers** — what effects trigger at each threshold? Are all 16 levels (0–15) defined with consequences, or are there gaps?
- **Corruption Dice mechanics** — the d6 roll, 1 = +1 Corruption. Does Ch. 8 define this the same way as Ch. 5 §5.5? Any conflict?
- **Corrupted Perks** — are they balanced relative to Universal Perks (Ch. 4)? Do they have consistent access conditions?
- **Purification paths** — the Corruption removal mechanics. We flagged that Ceremony of Sorrow (Ch. 5) needed a DR check to be consistent with Ch. 8 purification costs. Verify the fix aligns with what Ch. 8 actually says.
- **NPC takeover threshold** — we referenced "Corruption Level 15 = NPC monster under GM control" during Ch. 5. Is this rule fully defined in Ch. 8?
- **Corruption from pushing** — the interaction between Ch. 5's push mechanic and Ch. 8's Corruption rules. Are the results consistent?
- **Corruption as a resource vs. penalty** — some Ch. 4 Corrupted Perks may require reaching specific Corruption thresholds to unlock. Is this an intentional dual-use of Corruption?

**Cross-Chapter Checks:**
- Rotmind Rift (Ch. 5) Corruption cap of 3 — does this interact correctly with Ch. 8 Corruption level rules?
- Ceremony of Sorrow (Ch. 5) DR 2 check → remove 1 Corruption — is this consistent with Ch. 8's defined purification path costs?
- Hylden-Blooded lineage unique trait (Ch. 2) — "once per long rest, cast without BP/SE cost; after spell resolves, gain 1 Corruption" — does this interact correctly with Ch. 8?

---

### Ch. 4 — Perks System
**Status:** Open | **Priority:** 3 | **Complexity:** High | **Estimated Passes:** 4

Universal Perks (Tiers 1–4) and Corrupted Perks. Perks are the primary character customization system outside class abilities. They have the most potential for power inconsistency across tiers and the most cross-system interactions.

**Focus Areas:**
- **Tier scaling** — do perks genuinely escalate in power from Tier 1 to Tier 4? Or do some Tier 1 perks outperform Tier 3?
- **Unique reaction perks** — Ch. 5 §5.6 notes "Perks may grant unique reactions." Verify these reaction perks have defined triggers and costs
- **Perk prerequisites** — are all prerequisites clearly stated, and are they achievable via the level progression in Ch. 3?
- **Corrupted Perks** — access conditions (requires reaching specific Corruption threshold?), power relative to Universal Perks, whether they create death spirals
- **Perk interaction with class abilities** — perks that enhance spell damage, class-specific perks, perks that interact with specific conditions (Bleeding, Frightened, etc.)
- **"+X dice" language** — check for the same "+2 bonus" ambiguity we fixed in Ch. 5 (Issue 23). Perks were not in that sweep.
- **"Once per scene/rest" consistency** — verify all usage limits use the standardized terms from Ch. 5 §5.8

**Cross-Chapter Checks:**
- Corrupted Perks vs. Ch. 8 Corruption — do the unlock thresholds match what Ch. 8 defines as Corruption tier boundaries?
- Combat-modifying perks vs. Ch. 9 — do perks that modify attack rolls, saves, or conditions use correct terminology?

---

### Ch. 6 — Skills
**Status:** Open | **Priority:** 3 | **Complexity:** Medium | **Estimated Passes:** 3

Twenty skills across 5 categories. Each skill has an **Active Utility** combat action — this is the least-reviewed system in the PHB and likely has the most placeholder content.

**Focus Areas:**
- **Active Utility actions** — each skill has a defined combat use. Are all 20 defined with: action cost, DR, range, effect, and duration? Or are some still placeholder?
- **Skill/attribute pairing** — does each skill pair with a reasonable attribute? Verify these match the Save Types table in Ch. 5 §5.2
- **Skill coverage** — are there obvious gameplay needs not covered by any skill? (e.g., a social skill for intimidation in combat, a crafting skill for field-expedient weapons)
- **Skill rank progression** — how do characters gain skill ranks? Is this defined in Ch. 6 or only in Ch. 1/Ch. 3?
- **Skill checks vs. saves** — Ch. 5 uses Attribute + Skill for saves. Does Ch. 6 define when a roll is a "check" vs. a "save," and does Ch. 9 use the same distinction?
- **"+1 die" skill bonuses from lineages** — Ch. 2 gives "+1 die" to specific skills (e.g., Vampire gets +1 Weapon Mastery, +1 Stealth). Does Ch. 6 define how bonus skill dice interact with skill ranks?

**Cross-Chapter Checks:**
- Save type table from Ch. 5 §5.2 — does each save type's listed skill(s) exist as a defined skill in Ch. 6?
- Skill ranks referenced in Ch. 5's Concentration check — "Will attribute + Concentration skill rank successes" — verify "skill rank" is a defined term in Ch. 6

---

### Ch. 7 — Equipment
**Status:** Open | **Priority:** 3 | **Complexity:** High | **Estimated Passes:** 3–4

Weapons, armor, lineage gear, rarity tiers, crafting rules, and damage scaling. Referenced in Ch. 5 §5.7 for BP relics (cross-reference added but Ch. 7 §7.X placeholders remain). This chapter must align with Ch. 9's combat math.

**Focus Areas:**
- **Damage scaling** — weapon damage scales by level. Does this table align with the general damaging-ability scaling rule from Ch. 5 §5.4 and Ch. 9?
- **BP relics** — Ch. 5 §5.7 added "see Ch. 7 §7.X" cross-references. Verify the actual relic entries exist and restore the correct section numbers (§7.X is a placeholder)
- **Soul shards** — Ch. 5 §5.7 added "found as treasure or crafted by Glyphwrights; see Ch. 7 §7.X." Same placeholder issue.
- **Armor types and Armor mitigation** — does the Armor value system match Ch. 9's damage resolution? Master spells ignore 3 Armor (Ch. 5 §5.4) — does the Armor range make this meaningful?
- **Lineage gear (§7.4)** — referenced from Ch. 2 for each lineage. Does this section exist and contain entries for all six lineages?
- **Rarity tiers** — how do they affect availability and cost? Are they used consistently across all item categories?
- **Crafting rules** — are they complete? Do they reference skills from Ch. 6 correctly?
- **Weapon special properties** — if weapons have tags (silvered, sunblessed, etc.), are these defined here or only in Ch. 9?

**Cross-Chapter Checks:**
- Ch. 5 §5.7 placeholder references (§7.X for relics, soul shards) — replace with actual section numbers once Ch. 7 is verified
- Ch. 2 lineage kit cross-references — verify §7.4 covers all six lineages

**Known Pre-existing Issues:**
- §7.X placeholder cross-references in Ch. 5 §5.7 need to be updated with real section numbers after this review

---

## Tier 4 — Reference
*Review last. Check that all terms used across all chapters are defined here.*

---

### Ch. 12 — Glossary
**Status:** Open | **Priority:** 4 | **Complexity:** Low | **Estimated Passes:** 2

The master reference for all game terms, conditions, and traits. Review after all other chapters are audited — by then you'll have a complete list of every term used across the PHB that needs a definition here.

**Focus Areas:**
- **Completeness sweep** — compile every named condition, term, and trait used across Ch. 0–11 and verify each has a Glossary entry
- **Definition accuracy** — verify each definition matches the mechanical text in its source chapter (Ch. 9 for conditions, Ch. 8 for Corruption terms, etc.)
- **Circular definitions** — definitions that use other undefined terms
- **Missing trait entries** — tags like "Incorporeal," "Legendary," "Bloodied" — are these defined as traits in the Glossary or only as conditions?

**Known Pre-existing Issues:**
- Staggered condition added during Ch. 5 fix — confirm it's now in the Glossary with correct text ✅ (done)
- "Bloodied" used across Ch. 2 and Ch. 5 but no Glossary entry confirmed during audit

---

## Session Execution Map

| Session | Chapter(s) | Why This Order |
|---|---|---|
| **Session 1** | Ch. 0 + Ch. 10 | Foundation math + quick reference consistency check. Short. |
| **Session 2** | Ch. 9 | Combat rules — the most interconnected chapter. Full multi-pass audit. |
| **Session 3** | Ch. 2 | Lineages — read mostly already; focused pass on balance and undefined mechanics. |
| **Session 4** | Ch. 3 | Classes — largest chapter, most cross-references. Plan for 2 sessions if needed. |
| **Session 5** | Ch. 1 | Character creation validates Tier 1 + Tier 2 output. |
| **Session 6** | Ch. 8 | Corruption — upstream of Ch. 4 perks. Must precede perk audit. |
| **Session 7** | Ch. 4 | Perks — full Tier 1–4 pass, Corrupted Perks balance. |
| **Session 8** | Ch. 6 | Skills — Active Utility actions, attribute/skill pairings. |
| **Session 9** | Ch. 7 | Equipment — damage scaling, relic cross-references, lineage gear. |
| **Session 10** | Ch. 12 | Glossary — final completeness sweep across all chapters. |

---

## Audit Method (Reuse From Ch. 5)

Each chapter gets multiple passes, each from a different angle:

1. **Pass 1 — Cross-chapter conflicts** (does this chapter contradict rules from Tier 1 chapters?)
2. **Pass 2 — Internal consistency** (does this chapter contradict itself?)
3. **Pass 3 — Undefined terms and placeholders** (are there mechanics that assume rules written elsewhere that don't exist?)
4. **Pass 4 — Description quality** (can every mechanic be run at the table as written?)
5. **Pass 5 — Balance and power outliers** (are there options that trivialize others or break the expected power curve?)
6. **Pass 6+** — additional passes as the chapter warrants (Ch. 9 and Ch. 3 may need 6–7 passes each)

Findings from each chapter are documented in a new Mechanics Pass file following the same format as `Mechanics-Pass_2026-04-26.md`. When all issues in a pass file are resolved, it moves to `Completed/`.
