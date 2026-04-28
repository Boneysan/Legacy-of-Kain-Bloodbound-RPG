# Phase 3 Review Checklist — Game Balance and Mechanics

Phase 1 audited clarity and terminology. Phase 2 audited document consistency and completeness. Phase 3 is the **quantitative and cross-system pass** — verifying that the numbers work, the resource economy holds under real play, and the six classes feel distinct and balanced relative to one another.

Work through items in priority order. Each item has a status field, a checklist of concrete tasks, design questions to resolve, and a recommendation to guide the work.

---

## Phase 3 Tracking Table

| # | Area | Status | Priority | Notes |
|---|---|---|---|---|
| P3-1 | Skills chapter audit | **Complete** | High | Fixed 14 issues: DR table example (attacks use DV not DR), Riposte ambiguous wording, condition bolding (Restrained/Prone/Frightened), Parley undefined delay mechanic, Terrify missing range, Blood Sense missing action type/duration, Field Medic missing range, Jammed undefined condition, Iron Mind wrong condition name (Fear→Frightened), once-per-scene→once-per-encounter (Phase Control, Tactical Archive, Field Medic, Lore), Push rule missing 2–4 outcome and declaration timing, Stunts alignment with Ch.9, Active Mastery gap for already-BA utilities, Skill Cap mid-level progression table added. |
| P3-2 | Level-scaling damage math | **Complete** | High | Three-tier spot-check done. No runaway damage spike found. Two issues fixed: (1) §3.2 Durability Milestone labels misleading — "High Durability" (Sangromancer, Dreadblade) yields less total HP than "Standard" Blood Knight due to +3 vs +4 HP/level; added clarifying note. (2) Nosgothian Revenant recommended level range changed from 2–6 to 4–8 (DV 4 is <5% hit rate for Level 1–3 characters). New GM Guide §2.11 added with hit probability table and DV-by-level-band calibration guide. |
| P3-3 | Save DR calibration | **Complete** | High | Full audit done. DR range is 1–4 across all class abilities and monster stat blocks; DR 5 absent. Single broken ability fixed: Shadowmancer **Death from Below** (Level 17) had a fixed TV ≤ 4 cap, making it useless at level-appropriate play (Level 17 party fights TV 15+ enemies). Changed to "Cannot target Elite, Boss, or Legendary creatures." DR probability table + calibration guide added to GM Guide §2.12. |
| P3-4 | Action economy comparison | **Complete** | Medium | Full BA/Reaction audit done. Three fixes: (1) Sangromancer Vital Leech L2 Action→Bonus Action (0 BAs until L9 otherwise). (2) Warden Echo of Fate L6 Reaction→No Action (5 Reactions competing for 1 slot by L6; highest overload in system). (3) Hylden Warlock Madness Surge L3 Action→Bonus Action (0 BAs for entire class progression except L20 choice). |
| P3-5 | Corruption rate audit | **Complete** | Medium | Exposure modeled per class. Baseline Push pressure: ~0.33–0.67/session (well under 1.5 threshold). Only Hylden Warlock approaches threshold via Forbidden Truth (~0.5–1 net/session after Long Rest recovery — by design). Two bugs fixed: (1) Advanced Corruption Host "Spread Corruption" had no save — added DR 2 Blood save. (2) Two additional "Entropic point" instances in 06_Hylden-Forces.md corrected to "Corruption Level". Long Rest valve verified adequate for all classes. No involuntary path to Lost exists for non-Hylden-Warlock classes. |
| P3-6 | Condition stacking rules | **Complete** | Medium | Three rules written. (1) Same condition refreshes duration, does not stack effect (exception: Corrupted always applies). (2) Disadvantage does not stack from multiple sources. (3) Cap of 5 distinct simultaneous conditions; Paralyzed/Stunned/Dominated override on the 6th (replace least severe). Cap does not apply to Boss/Legendary. |
| P3-7 | Lineage/class synergy outliers | **Complete** | Medium | Full 6×8 matrix built. Two rule fixes applied (Wraith Lord rename + Hylden sidebar). Two dead zones documented. |
| P3-8 | Multi-target ability pricing | **Complete** | Low | Full AoE pass done. 2 fixes applied (Nightmare Chorus cost, Glyph of Quicksand cap). All others in acceptable 0.5–0.9× per-target range. |
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

**Status:** `Complete`

**Files modified:**
- `player's_handbook/03_Classes.md` — Shadowmancer **Death from Below** (Level 17): TV cap changed from "TV ≤ 4" to "not Elite, Boss, or Legendary"
- `GM_Guide/02_Encounter-Design.md` — Added §2.12 "Save DR Calibration" with player pass-probability table and recommended DR ranges by effect severity

**Findings:**

**DR range across the system: DR 1–4.** DR 5 is absent. The full DR map across all 8 classes and all Monster Manual Ch. 1 entries shows:
- DR 1: Used only for trivial on-hit grapples and Bone-Pyre Skeleton's death burst
- DR 2: Core reliable effects — Sangromancer Hemorrhage/Blood Puppet, Glyphwright Flame Sigil, Seal of Fire, standard monster Frightened/Bleeding triggers
- DR 3: Universal mid-tier DR — the default for Status effects (Stun, Prone, Frightened, Dominate) from Level 3 through Level 20
- DR 4: High-stakes/signature effects — Soul Reaver Banish (Level 5), Spirit Rend stun (Level 13), Shadowmancer Apotheosis (Level 20), Vampire Overlord Dominate (Boss)

**Structural assessment: the system is consistent.** DR never scales with level, but the d6 pool grows slowly enough that:
- DR 2 saves: 41–65% pass rate at the tier where they appear (mid-level enemies vs. early player abilities). Correctly calibrated for cheap, repeatable effects.
- DR 3 saves: 4–32% pass rate against Standard enemies at the level abilities appear. Appropriately reliable against Standard monsters; gets slightly easier against Legendary-tier bosses (~43–53% pass at Will 7, 7–8d6), but remains meaningful because Legendary Resistance provides counterplay.
- DR 4 saves: 1–17% pass rate even for Elite enemies. Correctly reserved for signature, high-cost, or once-per-encounter effects.

**Issue found — Death from Below (FIXED):** Shadowmancer Level 17, 5 SE, instant-kill on fail. Old text: "Cannot target creatures with a Threat Value of 4 or higher." At Level 17, all level-appropriate enemies (Standard and above) have TV 15–19. The TV ≤ 4 cap meant this 5 SE Level 17 ability could only target the equivalent of Level 1 fodder — a dead ability in any meaningful encounter. Fixed to "Cannot target Elite, Boss, or Legendary creatures" — consistent with the Boss/Legendary immunity pattern used elsewhere in the class chapter (Phase Anchor, Phase Anchor Level 15 variant explicitly names this exception). This lets Death from Below function as intended — a costly, dramatic instant-removal of Standard-tier enemies — without allowing it to delete Boss fights.

**Spot-checks passed:**
- **DR 3 at Level 3 Madness Surge (Hylden Warlock):** Standard enemy Will 2 = 2d6 → 0% pass. Reliable, but costs 1 SE and inflicts Confused (1 round), not permanent. Acceptable.
- **DR 2 on Sangromancer Hemorrhage/Blood Puppet (Level 1):** Enemies with Blood 0–1 = 0–1d6 → 0% pass. These are the Sangromancer's core early abilities; they should be reliable at low tier. At Level 10+, typical Boss Blood 3–4 = 3–4d6 → 11–26% pass vs DR 2. Correctly gets harder as enemies scale up.
- **Passive Fear Auras (Terror Aura L15, Crimson Terror L15, Aura of Despair L14) all use DR 3:** Against Legendary entities with Will 7–8 = 7–8d6, DR 3 pass rate is 43–53%. GMs should expect passive fear auras to fail about half the time against Legendary enemies — this creates appropriate stakes without making auras useless.
- **Death's Whisper (Dreadblade Level 9, DR 3 Blood, kills target below 10 HP):** Requires HP threshold AND melee reach AND a hit. The DR 3 save is nearly cosmetic — Standard enemies with Blood 2 = 2d6 → 0% pass. The real gatekeeping is the 10 HP threshold and positioning. Fine.

---

## P3-4. Action Economy Comparison

**Status:** `Complete`

**Files modified:**
- `player's_handbook/03_Classes.md` — Sangromancer Vital Leech (L2): Action → Bonus Action
- `player's_handbook/03_Classes.md` — Warden Echo of Fate (L6): Reaction → No Action
- `player's_handbook/03_Classes.md` — Hylden Warlock Madness Surge (L3): Action → Bonus Action

**Method:** Built a Bonus Action / Reaction matrix across all 8 classes at Level 5, Level 10, Level 15. Counted abilities with explicit Action/Cost tags of "Bonus Action" or "Reaction" in each class's perk table and Core Abilities.

**Bonus Action summary by class:**

| Class | L1–4 BAs | L5–9 BAs | L10–14 BAs | L15 BAs |
|---|---|---|---|---|
| Blood Knight | 1 (Bloodrush) | +1 (Crimson Avatar) | — | — |
| Soul Reaver | 1 (Spectral Strike) | — | — | +1 opt (Phase Anchor) |
| Shadowmancer | 1 (Cloak of Mist) | +1 (Shade Pact opt) | +1 (Doppelganger) | +1 (Shadow Court opt) |
| Sangromancer | 0 (**gap**) | — | — | +1 (Sanguine Transfig. L9) |
| Glyphwright | 1 (Glyph Recall) | — | +1 (Glyph Surge) | +1 (Resonant Overload opt) |
| Dreadblade | 1 (Venom Edge) | — | +1 (Perfect Kill) | — |
| Warden | 2 (Edict of Order + Guardian's Edict) | — | +1 (Mark of Equilibrium) | +1 (Scales of Ret. opt) |
| Hylden Warlock | 0 (**gap**) | — | — | — (only Final Unraveling L20 opt) |

**Reaction summary by class:**

| Class | Total Reactions by L6 | Notes |
|---|---|---|
| Blood Knight | 2 (Brutal Counter, Deathbound) | Clean — different triggers, no competition |
| Soul Reaver | 1 (Ghost Parry L8) | Low; gains Abyssal Anchor L14 |
| Shadowmancer | 1 (Silhouette) | Fine |
| Sangromancer | 0 | Fine (no Reaction abilities designed; resource system acts as gate) |
| Glyphwright | 1 (Temporal Anchor L15) | Fine |
| Dreadblade | 2 (Lethal Flow L5, Blur Step L8) | Fine — different triggers |
| Warden | **5** (Foresight L2, Fate Align L4, Cycle Cmd L5, J's Edge L5, Echo L6) | **Overloaded** — 5 Reactions by L6 |
| Hylden Warlock | 2 (Dark Insight L1, Premonitions L13) | Fine |

**Issues found and fixed:**

**Issue 1 — Sangromancer BA drought (FIXED):** 0 Bonus Actions from Level 1 through Level 8. All 8 levels of play before Sanguine Transfiguration (L9) are Action-locked. `Vital Leech` (L2, 1 BP, 3 damage/heal) is a simple single-target effect with no riders — changed to Bonus Action. This gives Sangromancer their first BA at Level 2, matching all other classes.

**Issue 2 — Warden Reaction overload (FIXED):** 5 Reactions competing for 1 slot per round by Level 6. Foresight, Fate Align, Cycle Command, Judgment's Edge, and Echo of Fate all trigger off different conditions but only one can fire per round. `Echo of Fate` (L6, reroll own failed roll, once per scene) changed to **No Action** — it fires when you fail a roll without consuming your Reaction, making it a passive luck valve. This leaves 4 Reactions, which is still high but 3 of them (Cycle Command, Judgment's Edge, Echo) are once-per-scene effects that rarely compete in the same round.

**Issue 3 — Hylden Warlock BA drought (FIXED):** 0 Bonus Actions for the entire class progression unless the player picks Final Unraveling at Level 20. Every offensive ability (Madness Surge, Decay Field, Nether Binding, Mind Rupture, etc.) is an Action. `Madness Surge` (L3, 1 SE, inflict Confused via DR 3 Will save) is a pure debuff with no damage — it is a setup/combo piece designed to precede Void Shard or Entropic Curse. Changed to Bonus Action. This gives Hylden Warlock their first BA at Level 3, consistent with Soul Reaver (Spectral Strike L1), and lets the class use Madness Surge + spell on the same turn.

**Spot-checks passed (no issue):**
- Soul Reaver BA load is lean (Spectral Strike is the main one through Level 11) but this is intentional — Phase Shift already costs an Action, and the class is designed around the SE-expenditure decision rather than BA chaining.
- Glyphwright BA load is appropriate — Glyph Recall (L3 BA) lets them reposition glyphs as a BA, which pairs cleanly with glyph placement Actions.
- Dreadblade has balanced Action/BA/Reaction split across all tiers.

---

## P3-5. Corruption Rate Audit

**Status:** `Complete`

**Files modified:**
- `Monster_Manual/06_Hylden-Forces.md` — Corruption Host Corrupted Touch crit: "1 Entropic point" → "1 Corruption Level"
- `Monster_Manual/06_Hylden-Forces.md` — Advanced Corruption Host Spread Corruption: no-save aura → DR 2 Blood save required

**Method:** Modeled expected Corruption gain per session for each class under standard play assumptions (3–4 combats, ~2 Pushes per session at 1–2 CDs each). Verified Long Rest recovery valve. Checked all monster Corruption sources across Monster Manual.

**Corruption exposure table (expected gross gain per session, before Long Rest recovery):**

| Class | Push pressure | Class-specific pressure | Total/session | Notes |
|---|---|---|---|---|
| Blood Knight | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Soul Reaver | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Shadowmancer | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Sangromancer | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Glyphwright | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Dreadblade | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Warden | ~0.33–0.67 | 0 | **0.33–0.67** | No voluntary Corruption mechanics |
| Hylden Warlock | ~0.33–0.67 | Forbidden Truth ~1–2/scene used | **1.3–2.7** | By design — Warlock trades SE for Corruption |

**Long Rest recovery valve:** DR 2 Will+Concentration/Insight check. Expected pool = 5–7d6 for most classes. Expected recovery of 2 recently-gained Corruption points ≈ 1.65 points. Recovery-capped at "since previous long rest." Valve is adequate — even a Hylden Warlock using Forbidden Truth twice/session nets only ~0.5–1 Corruption after a long rest.

**Corrupted Perk cost check (Tier 3):** Most expensive single activation is T3 perks (gain 1 Corruption + roll 1 CD = expected 1.17/activation) and major transformations (gain 1 + roll 2 CD = expected 1.33/activation). A single T3 activation cannot push a character within striking distance of Lost unless they're already at Abyss-Bound (11+). No fix needed.

**`Touched by Corruption` (1–2) check:** Threshold is crossed at Corruption 1, so the first Push that generates a 1 (expected 1-in-6) puts a character at Touched. This is an appropriate early warning. Players who never Push will never cross it involuntarily except from monsters.

**Monster Corruption pressure:** All identified monster sources require saves (DR 1–3). Only two non-save exceptions existed — both fixed this pass. No involuntary path to Lost exists via monster exposure alone in a single session.

**Hylden-Blooded + Hylden Warlock stacking:** HB Unique Trait (+1/long rest when free spell used) + Host to the Void perk (+1/long rest, max 3 total campaign) = +2 passive Corruption per long rest. This is deliberate choice stacking — both require explicit player decisions. GMs should note this combination to players as high-risk during character creation; no mechanical change warranted.

**Issues found and fixed:**

**Issue 1 — Advanced Corruption Host no-save aura (FIXED):** Elite TV 8 monster with "Spread Corruption" gave all enemies within 10 feet automatic +1 Corruption Level per turn with no save. Against a 4-PC party in melee range for 3 rounds = 12 total Corruption with zero counterplay. This violated the design principle that Corruption should require player choice or a meaningful save. Added DR 2 Blood save — consistent with other ambient-Corruption auras (Corrupted Raptor DR 1, Pillar-Decay Sentinel DR 3). DR 2 is appropriate for a TV 8 Elite.

**Issue 2 — Corruption Host Corrupted Touch crit (FIXED):** Standard Corruption Host crit effect read "gains 1 Entropic point" — the same terminology bug fixed in 6 other monsters last pass. Corrected to "1 Corruption Level."

**Spot-checks passed (no issue):**
- Tier 1 Corrupted Perk `Spectral Whisper` drawback (Spectral Realm extended stay = 1 Corruption/minute) is time-gated and opt-in — fine.
- `Host to the Void` (+1 Corruption/long rest) caps at 3 total over campaign — fine, not a runaway source.
- `Forbidden Truth` once-per-scene limit means maximum 3–4 Corruption from that source per session — within manageable range for a class designed around Corruption accumulation.

---

## P3-6. Condition Stacking Rules

**Status:** `Complete`

**Files modified:**
- `player's_handbook/12_Glossary.md` — Added "Condition Rules" block before Common Combat Conditions table: same-condition refresh rule, Disadvantage non-stacking, 5-condition cap
- `player's_handbook/09_Combat.md` — Added "Stacking" subsection to §9.9: Advantage and Disadvantage do not stack from multiple sources of the same type

**Findings:**

*Conditions in the system (18 total):*
- Status effects (8): Bleeding, Burning, Decay, Prone, Slowed, Shocked, Staggered, Corrupted
- Combat conditions (10): Grappled, Pinned, Frightened, Charmed, Dominated, Paralyzed, Stunned, Incapacitated, Confused, Suppressed

*Worst-case stacking scenario at Level 15 (4-person party, 1 round):*
- Frightened (Shadowmancer L15 Terror Aura / Shadow Court command)
- Bleeding (Sangromancer Hemorrhage)
- Confused (Hylden Warlock Madness Surge)
- Disadvantage on attacks (Dreadblade Venom Edge)
- Prone or Stunned (Blood Knight Crushing Blow / Juggernaut)

Without a cap, a non-Boss Standard creature in Round 1 faces 4–5 conditions simultaneously with no counterplay. Legendary Resistance (2–3 uses/encounter) cannot cover this volume.

*Disadvantage stacking check:* §9.9 defined Advantage + Disadvantage cancellation but said nothing about two Disadvantage sources. Several abilities (Venom Edge, Frightened, Confused, Shocked, Blinded) all independently impose Disadvantage. Without an explicit rule, a strict reading allows Disadvantage×5 to be mechanically distinct from Disadvantage×1.

**Rules written:**

1. **Same condition → refresh:** Applying the same condition a second time refreshes duration only; the mechanical effect does not stack. *Corrupted is the explicit exception* — each application is a discrete, permanent Corruption Level gain and always resolves fully.

2. **Disadvantage non-stacking:** Multiple sources of Disadvantage (or Advantage) from different abilities are still only one Disadvantage (or Advantage). Added to both §12.4 Condition Rules block and §9.9 Stacking subsection.

3. **5-condition cap:** A target can hold at most 5 distinct conditions simultaneously. A 6th condition has no effect unless it is Paralyzed, Stunned, or Dominated — these override by replacing the least severe current condition (GM judgment). Cap explicitly does not apply to Boss or Legendary creatures, preserving full condition pressure as a tool against high-tier enemies.

*Rationale for 5 (not 3 or 4):* Standard creatures have 3–4 abilities, so a 4-person party realistically reaches 4 conditions in one round. Allowing 5 leaves room for one more layered effect (e.g., a lingering Hemorrhage bleed) without capping out normal play. A hard cap of 3 would break too many designed synergies.

---

## P3-7. Lineage/Class Synergy Outliers

**Status:** `Complete`

**Files modified:**
- `player's_handbook/03_Classes.md` — Soul Reaver L19 perk renamed "Wraith Lord" → "Undying Resonance"; added alternate benefit for Wraith lineage characters (+2 Max SE instead of redundant Physical Resistance)
- `player's_handbook/02_Lineages-and-Race.md` — Added GM Note sidebar under Hylden-Blooded warning about Corruption-inversion with Hylden Warlock

**6×8 Synergy Matrix** *(S = Strong / N = Neutral / W = Weak / ! = Outlier)*

| Lineage | Blood Knight | Soul Reaver | Shadowmancer | Sangromancer | Glyphwright | Dreadblade | Warden of Balance | Hylden Warlock |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Vampire** | S | N | S | S | W | S | W | N |
| **Wraith** | W | **S!** | S | **W!** | N | N | S | N |
| **Hylden-Blooded** | **W!** | N | N | N | S | **W!** | N | **S!** |
| **Human** | N | N | N | W | N | W | S | W |
| **Revenant** | N | N | N | N | S | N | S | N |
| **Unbound** | N | **N!** | N | N | N | N | S | N |

**Synergy rationale (highlights):**

*Strong combos (S):*
- **Vampire + Blood Knight**: Weapon Mastery bonus + BP from Bloodied/kills feeds Life Drain loop. Best Fury/Blood coverage.
- **Vampire + Shadowmancer**: Stealth-in-darkness bonus + Backstab + Zephonim sub-type Cling = highest damage output from ambush at Tier 1.
- **Vampire + Sangromancer**: BP generation from Bloodied/kills fuels Hemorrhage/Crimson Bind BP costs. Rahabim sub-type is especially strong (Blood attribute alignment).
- **Vampire + Dreadblade**: Stealth bonus + Auto-Crit From Stealth = consistent critical output. Probably the intended "vampire assassin" fantasy pairing.
- **Wraith + Shadowmancer**: Wraith Phasing immunity to Grapple/Restrained protects Shadowmancer during Shadow Form Concentration. Observation bonus helps stealth gameplay. Spectral/shadow aesthetic alignment.
- **Wraith + Warden of Balance**: Will/Soul overlap; Phasing's +1 Will bonus enhances Guardian's Edict temp HP; both fate-adjacent thematically.
- **Hylden-Blooded + Glyphwright**: Glyphcasting lineage bonus directly improves every Glyphwright ability. Free glyph cast (1 Corruption) is a real trade-off for a non-Corruption-focused class.
- **Human + Warden of Balance**: Oracle-Blooded (Insight/Forbidden Knowledge) matches Warden's fate-casting. Extra Universal Perks at L6/12/18 fill Warden's limited in-class utility. Strong support build.
- **Revenant + Glyphwright / Warden**: Concentration + Ritualism bonuses directly target both classes' core mechanics.
- **Unbound + Warden of Balance**: Probability Shift + Fate Align = two dice-manipulation tools. Thematic resonance (both manipulate chance and fate).

*Outliers requiring attention (!):*

**1. Wraith + Soul Reaver (S!) — NAMING CONFLICT + REDUNDANCY**
- Wraith Phasing (Bonus Action, free, Will×/long rest) provides: Spectral damage, Resistance to Physical, immunity to Grapple/Restrained, +1 Will to DV
- Soul Reaver L19 perk "Wraith Lord" also grants permanent Resistance to Physical damage
- **Naming conflict**: Wraith Lineage L20 Paragon is *also* called "Wraith Lord" (Hybrid Affinity + dual-realm existence) — identical name, different effects
- **Fix applied**: Soul Reaver L19 renamed to "Undying Resonance"; added rule that Wraith lineage Soul Reavers get +2 Max SE instead (since Phasing provides Physical Resistance in combat from L10)
- Secondary note: Wraith Lineage L20 Paragon grants Hybrid Affinity — Soul Reaver already has this from Level 1 (class trait). Wasted paragon milestone if taken as Soul Reaver. No rule fix needed; document for GMs.

**2. Hylden-Blooded + Hylden Warlock (S!) — CORRUPTION COST INVERTED**
- Hylden Warlock Entropic Surge (+1 die at Corruption 7+) and Voidborn Ascendancy (L15: +1 die per 3 Corruption, max +4) convert Corruption into bonus dice
- Hylden-Blooded Unique Trait: free spell cast 1/long rest, costs 1 Corruption
- Combined: the "cost" of the free cast becomes a benefit. Intended risk becomes reward.
- L10 Paragon (take damage instead of Corruption) is mechanically *worse* for this build — players should be aware before leveling
- **Fix applied**: GM Note sidebar added to Hylden-Blooded in `02_Lineages-and-Race.md` flagging the inversion and recommending narrative Corruption consequences

**3. Wraith + Sangromancer (W!) — FUNDAMENTAL REALM CONFLICT**
- Sangromancer: "All Blood-tag spells and BP pool inaccessible in Spectral Realm" (class sidebar)
- Wraith: Spectral Realm is home; Wraith Phasing shifts the character into a phased state
- A Wraith Sangromancer who phases or crosses to Spectral loses their entire toolkit
- No rule fix needed (the existing sidebar already documents this); document here for GMs as a known dead zone

**4. Unbound + Soul Reaver (N!) — WASTED CORE TRAIT**
- Soul Reaver has Hybrid Affinity from Level 1 (class feature)
- Unbound's primary unique trait at L1 is Hybrid Affinity — identical, completely wasted
- Unbound L20 Paragon (Fate-Breaker) is the long-term payoff, but L1–L9 is a wasted lineage trait
- No rule fix needed; document for players choosing this combo that their L1 lineage trait has no effect

*Dead zones (W) documented, no fixes required:*
- **Hylden-Blooded + Blood Knight**: Free spell wasted; Glyphcasting/Forbidden Knowledge irrelevant; no attribute overlap (Soul/Focus vs Fury/Blood)
- **Hylden-Blooded + Dreadblade**: Same issue (Shadow/Fury vs Soul/Focus); free cast wasted
- **Human + Sangromancer**: No Blood attribute bonus; extra perks don't compensate for missing Blood scaling
- **Human + Dreadblade**: No Shadow/Fury boost; Sarafan anti-undead is highly situational

---

## P3-8. Multi-Target Ability Pricing

**Status:** `Complete`

**Files modified:**
- `player's_handbook/03_Classes.md` — Nightmare Chorus (Shadowmancer L10): AoE burst now costs 1 additional BP (total 2 BP)
- `player's_handbook/05_Spellcasting-and-Magic.md` — Glyph of Quicksand: added explicit 3-target cap to match Glyph of Binding

**Method:** Single-target baseline at each resource cost, then per-target ratio test. Acceptable range: 0.6–1.0× (breadth not depth). Above 1.0× = overtuned; below 0.4× = undertuned (unless Rider saves it).

**Single-target baselines by resource cost:**

| Cost | Reference ability | Damage |
| :--- | :--- | :--- |
| 1 SE | Void Shard (HW): 3 Entropic, 30 ft | 3 damage |
| 1 BP | Pulse Spike (SG): 3 Spectral + Disadvantage ×2 | 3 damage + condition |
| 2 SE | Glyph of Severance: 4 Spectral + item sever | 4 damage + utility |
| 2 BP | Blood Puppet: full action control (Bleeding target) | full control |
| 3 SE | Spectral Nova (AoE itself) / Nether Binding (control) | 6 damage AoE or control |
| 4 SE | Soul Storm (L18 capstone) | 12 damage + Frightened AoE |
| Free/1 Action | L10 melee attack, base 4 damage + combat bonus | ~6–7 with scaling |

**Full AoE inventory with verdict:**

| Ability | Cost | Area | Per-Target Dmg | Ratio | Rider | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Glyph of Flame** (GW spell) | 1 SE | 5 ft radius | 1.5 avg (halved) | 0.50 | Set-trap; no attack roll | Borderline; trap placement justifies it |
| **Flame Sigil** (GW core) | 1 SE | 5 ft burst | 1.5 avg | 0.50 | Same | Same |
| **Eldritch Gasp** (HW spell) | 1 SE | 15 ft cone | 0.5 avg | 0.17 | Silenced 1 rd | Damage-undertuned; Silenced rescues it at 3+ targets |
| **Dissonant Pulse** (HW/WB) | 1 SE | 10 ft radius | 0 | — | End concentration | Niche (concentrating enemies only); well-scoped |
| **Hemorrhage Halo** (SG spell) | 2 BP | 10 ft radius | 1.5 avg + Bleeding | 0.50 | Bleeding | Acceptable; Bleeding synergizes with Sangromancer toolkit |
| **Sangral Lance** (SG spell) | 2 BP | 60 ft line | 5 primary + 5 secondary | conditional | Bleeding | Secondary hit requires extra successes; fine |
| **Crimson Bind** (SG core/spell) | 2 BP | 10 ft sphere | 0 damage | — | Rooted + Slowed | Pure control; 2 BP for multi-target is efficient but bounded by 10 ft radius |
| **Seal of Fire** (GW L8) | 2 SE | 10 ft radius | 2.5 avg (halved) | 0.63 | — | In range |
| **Glyph of Cinders** (GW spell) | 2 SE | 10 ft area | 6 total (3 rnds ×2) | — | Difficult terrain | Sustained AoE; Glyphwright zone-control identity justifies it |
| ~~**Glyph of Quicksand**~~ **(fixed)** | 2 SE | 15 ft square | — | — | Restrained + Corruption | **Pre-fix:** no target cap vs. Glyph of Binding's explicit 3-target cap at same cost; FIXED: capped at 3 targets |
| **Spectral Nova** (SR L9) | 3 SE | 10 ft radius | 4.5 avg | 0.75 | — | In range; no attack roll adds value |
| **Soul Storm** (SR L18) | 4 SE | 10 ft radius | 9 avg | 1.5 | Frightened | Capstone L18, 4 SE, largest pool drain — high but appropriate for tier |
| **Bloodstorm** (BK L10) | 0 (1/short rest) | 5 ft reach | Full weapon | 1.0 | — | Free multiattack 1/short rest; requires clustering; bounded and acceptable |
| ~~**Nightmare Chorus**~~ **(fixed)** | ~~1 BP~~ → 2 BP | 5 ft burst | — | — | Frightened | **Pre-fix:** multi-target Fear at single-target price (1 BP); FIXED: 1 additional BP for the burst |
| **Terror Aura** (SM L15) | Passive (no cost) | 10 ft aura/turn | — | — | Frightened | Passive save-or-fear aura; balanced by once-per-scene immunity on success |
| **Crimson Terror** (BK L15) | Passive (sub-feature) | 10 ft while Crimson Avatar active | — | — | Frightened | Piggybacks on existing 1/long rest transformation; limited scope |
| **Zone of Judgment** (WB L7) | 2 SE | 15 ft radius | 0 damage | — | -1 DV to enemies | Buff/debuff zone; no damage; purely utility pricing — fine |
| **Judgment Wheel** (WB L9) | 3 SE | 30 ft radius | 0 | — | Random buffs/debuffs | Chaotic; cost justified by scale |

**Summary:**
- 22 multi-target or area abilities reviewed across classes and core spells
- 2 abilities outside acceptable range: **Nightmare Chorus** (free upscale) and **Glyph of Quicksand** (no cap). Both fixed.
- Most AoE abilities correctly sit at 0.5–0.75× per-target ratio — you buy breadth, not depth
- **Soul Storm** (L18) at 1.5× per-target is the only above-range entry; justified as a Level 18 capstone at 4 SE, the highest spell cost in the game
- Passive auras (Terror Aura, Crimson Terror) and once-per-rest abilities (Bloodstorm) are excluded from the ratio test — their limiting mechanics replace the resource cost

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
