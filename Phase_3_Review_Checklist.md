# Phase 3 Review Checklist — Game Balance and Mechanics

Phase 1 audited clarity and terminology. Phase 2 audited document consistency and completeness. Phase 3 is the **quantitative and cross-system pass** — verifying that the numbers work, the resource economy holds under real play, and the six classes feel distinct and balanced relative to one another.

Work through items in priority order. Each item has a status field, a checklist of concrete tasks, design questions to resolve, and a recommendation to guide the work.

---

## Phase 3 Tracking Table

| # | Area | Status | Priority | Notes |
|---|---|---|---|---|
| P3-1 | Skills chapter audit | **Complete** | High | Fixed 14 issues: DR table example (attacks use DV not DR), Riposte ambiguous wording, condition bolding (Restrained/Prone/Frightened), Parley undefined delay mechanic, Terrify missing range, Blood Sense missing action type/duration, Field Medic missing range, Jammed undefined condition, Iron Mind wrong condition name (Fear→Frightened), once-per-scene→once-per-encounter (Phase Control, Tactical Archive, Field Medic, Lore), Push rule missing 2–4 outcome and declaration timing, Stunts alignment with Ch.9, Active Mastery gap for already-BA utilities, Skill Cap mid-level progression table added. |
| P3-2 | Level-scaling damage math | **Complete** | High | Three-tier spot-check done. No runaway damage spike found. Two issues fixed: (1) §3.2 Durability Milestone labels misleading — "High Durability" (Sangromancer, Dreadblade) yields less total HP than "Standard" Blood Knight due to +3 vs +4 HP/level; added clarifying note. (2) Nosgothian Revenant recommended level range changed from 2–6 to 4–8 (DV 4 is <5% hit rate for Level 1–3 characters). New GM Guide §2.11 added with hit probability table and DV-by-level-band calibration guide. |
| P3-3 | Save DR calibration | **Not started** | High | Player DRs and monster DRs have never been cross-checked |
| P3-4 | Action economy comparison | **Not started** | Medium | Per-class Bonus Action load never compared across all six classes |
| P3-5 | Corruption rate audit | **Not started** | Medium | Total Corruption exposure per session never totalled per class |
| P3-6 | Condition stacking rules | **Not started** | Medium | No explicit cap on simultaneous conditions exists in the rules |
| P3-7 | Lineage/class synergy outliers | **Not started** | Medium | Strong combos and dead-zone combos not mapped |
| P3-8 | Multi-target ability pricing | **Not started** | Low | AoE vs. single-target cost efficiency never compared |
| P3-9 | Play experience / fun pass | **Not started** | Low | Carry-forward from P2-8; qualitative read-through simulation |

---

## P3-1. Skills Chapter Audit

**Status:** `Not started`

**Primary file:** `player's_handbook/06_Skills.md`

**Why this matters:** `06_Skills.md` was not included in any Phase 1 or Phase 2 pass. It defines how skill checks work, what the 20 skills do, their Active Utility actions, skill point economy, and the Pushing/Stunts system. Several of these interact directly with combat resolution and Corruption. No one has checked whether the Active Utility wording is consistent with the Chapter 9 action economy, whether DR values in the skill table match Chapter 9 benchmarks, or whether the Pushing rules in Ch. 6 match Ch. 8.

**What needs to happen:**
- [ ] Confirm DR table in §6.1.1 matches the DR benchmarks used in Chapter 9 and the Glossary (DR 1–5 scale)
- [ ] Audit each Active Utility using the Ability Audit Template: action type, range, duration, save/DC, cost, refresh
- [ ] Confirm "once per scene" vs. "once per encounter" language is consistent with the rest of the PHB
- [ ] Confirm `Evasion: Riposte` — "misses you by 2+ successes" — uses correct combat language (2+ extra successes over DV, not a check vs. DR)
- [ ] Confirm `Tactics: Command` — "+2 dice" grant is not worded elsewhere as "+1 die" or "Advantage" elsewhere; confirm which is canonical for ally-buff grants
- [ ] Confirm `Ethereal Mastery: Phase Control` — "Resistance to Spectral damage" for 1 minute is consistent with how Resistance is defined in Ch. 9 (halves after Armor)
- [ ] Confirm `Forbidden Knowledge: Weakness Analysis` — "reveal a Boss's Vulnerability or AI Tag" — confirm AI Tags are defined in Monster Manual Introduction
- [ ] Confirm `Persuasion: Parley` — "delay a non-mindless enemy's turn to the end of the round" — define what "delay" means mechanically (does the enemy lose their turn entirely, or act last in initiative?)
- [ ] Confirm `Active Mastery` rule at rank 4 (Bonus Action upgrade) — verify no class ability already grants the same skill's Active Utility as a Bonus Action at an earlier level, creating redundancy
- [ ] Confirm §6.4 skill point economy matches Class chapter (§3.2): "5–6 starting points based on class" — verify each class entry states its starting skill point count
- [ ] Confirm `Pushing a Roll` in §6.3 matches Ch. 8 §8.2 exactly (same dice count, same Corruption gain trigger)
- [ ] Confirm `Stunts` in §6.3 matches Ch. 9 §9.6 exactly ("2 or more extra successes" threshold)

**Questions to answer:**
- Does `Parley` (delay enemy's turn) interact with initiative reinsertion? If the delayed enemy would now act after someone who hasn't acted yet, what happens?
- Does `Expose` (reveal exact HP and DV) create any balance concern at high level when enemy HP totals are very high? Is it still worth a full Action?
- Should `Lore: Tactical Archive` (+1 Armor vs. a type for the scene) stack with Armor from equipment, or is it a separate layer?
- The rank-4 Active Mastery rule says the Active Utility becomes a Bonus Action "if it was an Action." What happens to utilities that are already Bonus Actions at rank 4?

**Recommendation:**
Run the standard Ability Audit Template across all 20 Active Utilities — it takes roughly one pass through the table. The most likely issues are `once per scene` vs. `once per encounter` inconsistency, Parley's missing initiative reinsertion rule, and the Pushing rule potentially diverging from Ch. 8 after the Ch. 8 corruption-dice rewrite. Fix those four and the chapter is likely clean.

---

## P3-2. Level-Scaling Damage Math

**Status:** `Complete`

**Files modified:**
- `player's_handbook/03_Classes.md` — §3.2 Durability Milestones: added clarifying note on HP-per-level vs. milestone-bonus distinction
- `Monster_Manual/01_Undead-and-Vampiric.md` — Nosgothian Revenant: updated Recommended Levels from 2–6 to 4–8; added callout directing Level 2–3 GMs to the Weakened Revenant scaling option
- `GM_Guide/02_Encounter-Design.md` — Added §2.11 "Attack Pool vs. DV Calibration" with hit-probability table and DV-by-level-band reference

**Findings:**

**No runaway damage spike found.** Weapon damage (+1 at each milestone, max +4) and Combat Bonus (+1 die at each milestone, max +4) are both additive and linear. No multiplicative compounding occurs. At Level 20, a base-3 weapon deals 7 damage — meaningful against Level 20 monsters (HP 80–210+) because high-DV monsters still require Pushing and the party is 4 characters.

**Life Drain cap is not binding in normal combat.** At Level 15 with Endless Hunger, expected heal rate is ~2–5 HP/round vs. a cap of Blood(4) + Level(15) = 19 HP/turn. The cap only matters against swarms (many low-HP targets per round). No adjustment needed.

**Issue 1 — Durability label mismatch (FIXED):** §3.2 labels Sangromancer and Dreadblade "High Durability" (+3 milestone), but these classes gain only +3 HP/level. Blood Knight ("Standard Durability") gains +4 HP/level and ends up with ~18 more HP at Level 20. "High Durability" implies more HP, but the math inverts that expectation. Fixed by adding a note to §3.2 explaining that the label describes milestone bonus size only, and that HP-per-level rate also varies by class.

**Issue 2 — Nosgothian Revenant early-level recommendation (FIXED):** Revenant is TV 4 Standard with DV 4. At Level 2–3, characters have 4–5 dice; hit rate vs. DV 4 is 1–5%. Changed Recommended Levels to 4–8 and added a callout for GMs to use Weakened Revenant (TV 2, DV 3) for earlier play.

**Issue 3 — DV calibration guidance was missing from the GM Guide (FIXED):** Added §2.11 with a hit-probability table and recommended DV ranges by level band. Key callouts: DV 4 requires Combat Bonus (Level 5+); DV 5 requires Pushing or special abilities at all practical levels; DV 6 is intentionally boss-tier and not expected to be hit without resource expenditure.

**Spot-checks passed:**
- Soul Reaver armor-ignore (Soul Blade): most valuable Levels 5–12 when enemy Armor 2–3 is common. After Level 12, damage scaling increases raw damage enough that armor-ignore is still powerful but less decisive.
- Skirmisher HP survivability: Soul Reaver and Warden have ~6 fewer HP than Blood Knight at Level 20, but the difference is small. Survivability differentiation comes from class features, not HP totals.
- DV 5 Elite enemies (e.g., Hunger-Warped Vampire TV 7, Hylden Shock Trooper TV 9) are correctly calibrated for Level 5–9 play when Pushing is used; bare hit rates of 9–15% are by design.

---

## P3-3. Save DR Calibration

**Status:** `Not started`

---

## P3-5. Corruption Rate Audit

**Status:** `Not started`

**Primary files:**
- `player's_handbook/08_Corruption.md`
- `player's_handbook/03_Classes.md`
- `player's_handbook/04_Perks.md`
- `Monster_Manual/` (monster abilities that deal Corruption)

**Why this matters:** Individual Corruption sources were fixed in isolation across Phase 1. But no one has totalled Corruption exposure across a typical session for each class. A Hylden Warlock pushing rolls and activating Tier 2 Corrupted Perks may reach Corruption 7 (Deeply Corrupted) within two sessions without any deliberate narrative choice. A Blood Knight may barely touch Corruption across a full arc. The design intent is that reaching `Lost` (Corruption 15) should require player choice — it should not be inevitable for any build.

**What needs to happen:**
- [ ] Estimate Corruption gain per session for each class under normal play:
  - Count Push rolls likely per session (how often does the class fail checks it cares about?)
  - Count Corrupted Perk activations likely per session (Tier 1 = 1 CD, Tier 2 = 2 CD)
  - Count monster abilities that deal flat Corruption (common in Spectral and Cultist chapters)
  - Assume 1-in-6 chance each Corruption Die shows a 1 (flat ~16.7%)
- [ ] Flag any class whose expected Corruption gain per session exceeds 1.5 under normal play (this would reach Lost in ~10 sessions without cleansing)
- [ ] Verify the Long Rest cleansing valve defined in Ch. 8 §8.6 is sufficient to offset the gain rate for high-Corruption classes
- [ ] Check Hylden-Blooded lineage specifically — their unique trait costs include Corruption Dice; stack this against Hylden Warlock class Corruption exposure
- [ ] Check whether any Corrupted Perk at Tier 3 has a cost high enough that activating it once could push a character within striking distance of Lost in one session
- [ ] Verify that `Touched by Corruption` (levels 1–2) feels like a meaningful early warning rather than something that gets traversed accidentally in Session 1

**Questions to answer:**
- If a player never voluntarily chooses a Corrupted Perk and never Pushes rolls, can they still be pushed to Lost purely by monster Corruption effects? If yes, that is a design problem.
- Is there a session count where a player who takes one Tier 2 Corrupted Perk and Pushes twice per session reaches Corruption 11 (Abyss-Bound)? Should that feel dramatic or alarming?
- Does the narrative of "temptation toward Lost" hold when some classes are essentially immune to passive Corruption pressure?

**Recommendation:**
Build a Corruption exposure table: rows = classes/lineages, columns = Passive pressure (monster effects), Push pressure (failed rolls × Push frequency), and Active pressure (Corrupted Perk use). Sum these per session and verify the total stays below ~1.5 for standard play and below ~3 for heavy corruption-leaning builds. Adjust either monster Corruption outputs, the Long Rest valve, or Corrupted Perk costs to hit that window. The system already has the right philosophy (tempting but not inevitable) — this is a numbers calibration pass, not a redesign.

---

## P3-6. Condition Stacking Rules

**Status:** `Not started`

**Primary files:**
- `player's_handbook/12_Glossary.md` (condition definitions)
- `player's_handbook/09_Combat.md` (combat resolution)
- `player's_handbook/03_Classes.md` (conditions applied by class abilities)

**Why this matters:** The Glossary defines conditions such as Prone, Frightened, Stunned, Blinded, Bleeding, Restrained, Paralyzed, Charmed, and several more. There is no explicit rule stating whether multiple instances of the same condition stack, and no cap on how many distinct conditions can apply to one target simultaneously. At Level 15, a Shadowmancer + Sangromancer party can layer Frightened, Bleeding, Restrained, Prone, and Disadvantage on a single target in one round. Against monsters without Legendary Resistance, this reduces high-tier combat to a condition-application checklist.

**What needs to happen:**
- [ ] Audit every condition defined in the Glossary: does it stack with itself if applied twice? (e.g., two sources of Bleeding — does the target bleed twice?)
- [ ] Define whether the same condition applied by two different sources refreshes duration or does nothing
- [ ] Define a maximum number of distinct conditions that can apply to one target simultaneously, or explicitly state there is no cap
- [ ] Identify the highest-condition-density scenario achievable by a party of 4 in one round at Level 15 — list every condition and its source
- [ ] Determine whether the existing Legendary Resistance framework (from MM Introduction) provides sufficient counterplay to multi-condition lockdown at that tier
- [ ] Check whether `Disadvantage` is treated as a condition (can it stack from two sources?) or a modifier state
- [ ] Verify that conditions with similar effects (`Prone` + `Restrained` both limit movement) do not create ambiguity when both apply

**Questions to answer:**
- Should the same condition from two different sources stack, refresh, or be ignored?
- Is a hard condition cap (e.g., maximum 3 distinct conditions per target) needed, or is Legendary Resistance sufficient counterplay?
- Does `Prone` + `Frightened` + `Restrained` simultaneously create an "I can't do anything" state that removes player agency? Is that appropriate only for enemies, or should PCs be protected?

**Recommendation:**
Add a single paragraph to Glossary §12.2 under "Conditions" or to Chapter 9 §9.5 covering three rules: (1) a condition applied twice refreshes its duration but does not stack its effect; (2) Disadvantage does not stack — two sources of Disadvantage is still one Disadvantage; (3) a target can have at most [4–5] distinct conditions simultaneously, with each new condition above the cap replacing the weakest current condition or being ignored. These three sentences close the gap without overhauling individual conditions.

---

## P3-7. Lineage/Class Synergy Outliers

**Status:** `Not started`

**Primary files:**
- `player's_handbook/02_Lineages-and-Race.md`
- `player's_handbook/03_Classes.md`

**Why this matters:** No matrix exists mapping likely lineage/class combinations against mechanical synergy. Some combinations are likely overtuned (strong synergy creating outlier power) and some are likely dead zones (no meaningful interaction, reducing the character's identity). Identifying the extremes doesn't require playtesting — it requires reading both files together.

**What needs to happen:**
- [ ] Build a 6×8 combination matrix (6 lineages × 8 classes) and note synergy level: Strong / Neutral / Weak
- [ ] Flag any Strong combinations where shared attribute bonuses, affinity, or trait stacking create noticeably better characters than average — candidates:
  - Wraith + Soul Reaver: both Spectral affinity, Soul Blade + Wraith Phasing + Phase Shift — potentially double-spectral-immune and nearly untargetable
  - Hylden-Blooded + Hylden Warlock: both already use Corruption offensively — Corruption cost doubled but power potentially more than doubled
  - Human + Blood Knight: Humans have no attribute that boosts Fury or Blood above baseline — may be a dead zone
  - Rahabim + Sangromancer: both Blood-primary; Rahabim blood recovery traits stack with Sangromancer blood economy
- [ ] Flag any Weak combinations where a lineage's primary attribute and a class's core attributes don't overlap at all — this produces slower leveling and weaker saves
- [ ] Verify that Wraith's spectral-phasing traits do not trivially replicate Soul Reaver's Phase Shift cost-free at early levels
- [ ] Verify that Human's extra perk access does not outpace the lineage-specific trait value of vampiric lineages at Tier 1 play (Levels 1–5)

**Questions to answer:**
- Is Wraith + Soul Reaver intended to be the "maximum spectral" combo, and if so, is there a designed counter to it in the game (certain monster types, environmental hazards, anti-phase effects)?
- Should the Hylden-Blooded lineage have an explicit note cautioning that pairing with Hylden Warlock concentrates Corruption pressure?
- Are there any two-class feel-alike combos (e.g., a Dumahim Vampire + Sangromancer vs. a Melchiahim Vampire + Blood Knight) where the playstyle difference is insufficient to justify choosing both?

**Recommendation:**
A full matrix is a two-hour read-through — assign synergy ratings, then focus edits only on the two or three most extreme outliers. The Wraith + Soul Reaver combo is the most likely to need a note or a limiting clause (e.g., "Phase Shift costs 1 SE even for Wraith-lineage Soul Reavers — the class ability and lineage trait represent the same underlying power"). Other outliers can be documented in a GM sidebar rather than changing the rules.

---

## P3-8. Multi-Target Ability Pricing

**Status:** `Not started`

**Primary files:**
- `player's_handbook/03_Classes.md`
- `player's_handbook/04_Perks.md`
- `player's_handbook/05_Spellcasting-and-Magic.md`

**Why this matters:** AoE abilities have not been systematically compared to single-target abilities at the same cost. If a 1 SE multi-hit attack deals the same total expected damage as a 1 SE single-target attack, there is no cost for the flexibility advantage. Conversely, if AoE abilities cost twice as much for similar output, they will rarely be used.

**What needs to happen:**
- [ ] Identify all multi-target abilities across Classes and Perks (e.g., Blood Knight `Bloodstorm`, Soul Reaver `Soul Storm`, Shadowmancer `Fear` AoEs, Glyphwright AoE glyphs)
- [ ] For each, calculate expected total damage output vs. a group of 3 targets vs. a single target at the same level
- [ ] Compare to the best single-target ability at the same cost and level — is the AoE version dealing roughly 1.5–2× the single-target damage total to justify hitting multiple enemies? Or is it more efficient per target than single-target options?
- [ ] Flag any AoE ability where expected damage per target exceeds the equivalent single-target ability at the same cost — this is overtuned
- [ ] Flag any AoE ability where expected damage per target is less than half the single-target option — this is undertuned (no reason to use except for riders or conditions)
- [ ] Check AoE condition riders (e.g., AoE Frightened, AoE Corruption gain) — apply the same test to rider value: does the AoE rider + damage justify the cost vs. single-target?

**Questions to answer:**
- Is `Bloodstorm` (1/short rest, hits all enemies in 5 ft) significantly better than a single melee attack at the same level because of the area, even if damage per target is lower?
- Do any glyph-based AoE effects (Glyphwright, Warden) become dramatically stronger when encounter design places multiple enemies in close proximity?

**Recommendation:**
This pass is mostly arithmetic. For each AoE ability, calculate: (single-target expected damage) vs. (AoE expected damage per target × average number of targets). A healthy ratio is approximately 0.6–1.0× the single-target value per target (you get breadth, not depth). Above 1.0× per target is overtuned; below 0.4× per target is undertuned. Any ability outside that range should have its cost, damage, or cooldown adjusted.

---

## P3-9. Play Experience / Fun Pass

**Status:** `Not started`

**Carry-forward from P2-8.** This is a qualitative simulation pass, not a document audit.

**Primary files:** All player-facing chapters

**What needs to happen:**
- [ ] Pick one character of each class at Level 5, Level 10, and Level 15. Walk through three rounds of combat mentally and answer: does each class feel distinct? Does each one have a clear moment of "this is what my character does"?
- [ ] Check Corruption temptation: at Level 10, does a player who has never used a Corrupted Perk feel like they are missing out — or does the game feel complete without it?
- [ ] Check whether any class feels meaningfully worse in solo encounters vs. group encounters (some controllers, like Sangromancer, may be much weaker when there is only one enemy)
- [ ] Verify that Master Tier (Level 16–20) abilities feel epic without invalidating encounter design — specifically, confirm the GM has tools (Legendary Resistance, Immunity to conditions, high DV) to make encounters feel threatening
- [ ] Confirm that the hard-control abilities (Banish, Puppet, Soul Storm) have visible counterplay documented in the player-facing rules, not just in the Monster Manual
- [ ] Read the opening of each class description and confirm a new player can explain what the class does in one sentence

**Design questions:**
- Is there any class that, when played optimally at Level 10, removes meaningful decisions from other players at the table?
- Does the Warden of Balance (support) have a session where it feels powerful rather than merely enabling? Is there a moment that belongs to this class?
- Does the Hylden Warlock's Corruption synergy feel like a character arc, or like a liability to manage?

**Recommendation:**
Run the simulation as a written three-round combat narrative for each class — not a full playtest, but a mental "what do I do on round 1, 2, 3?" exercise. This surfaces ability ordering, tempo issues, and whether the class feels coherent. For the Warden specifically, check whether its support kit can "win" a difficult encounter that would have been lost without it — if yes, the class has its identity moment.

---

## Definition of Done (Phase 3)

A Phase 3 item is complete when:

- The specific numbers or mechanics in question have been calculated or explicitly verified against in-document values.
- Any imbalance found is either corrected in the relevant document or documented as an intentional design choice with a note explaining why.
- No assumption about player power, monster threat, or encounter outcome is left unverified at Levels 5, 10, and 15 (the three key play tiers).
- Every condition, save, and multi-target effect has a stated stacking rule or an explicit "no cap" note.
- The six classes can each be described with a distinct one-sentence identity, and no two classes produce the same play feel in a three-round combat.
