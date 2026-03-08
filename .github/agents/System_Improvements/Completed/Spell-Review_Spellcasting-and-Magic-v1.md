# Bloodbound RPG: Spellcasting and Magic Review
**Scope:** Chapter 5 spell system, class spell support, and spell-to-class fit across the Player's Handbook  
**Date:** March 8, 2026  
**System Version:** 1.0 (In Development)

---

**Document Note:** This review captures the pre-implementation assessment that led to the spell-system revision pass. The handbook has since been updated. Use this file as design rationale and historical context, not as the current source of truth for Chapter 3 or Chapter 5.

---

**Status Legend:**
- ✅ **APPROVED** — No issue found; ready for playtesting.
- ⚠️ **MINOR REVISION** — Fundamentally sound; needs wording, access mapping, or moderate tuning.
- 🔴 **MAJOR REVISION** — Significant structural or balance problem requiring revision before reliable playtesting.

---

## Table of Contents
- [Executive Verdict](#executive-verdict)
- [Cross-Cutting System Findings](#cross-cutting-system-findings)
- [Class Coverage Review](#class-coverage-review)
- [Spell and Feature Collisions](#spell-and-feature-collisions)
- [High-Risk Numerical Balance Issues](#high-risk-numerical-balance-issues)
- [Priority Fix List](#priority-fix-list)

---

## Executive Verdict

**Overall Result at Review Time:** 🔴 **MAJOR REVISION**

At review time, the spell compendium was large enough in aggregate, but the spell system was not yet ready for clean playtesting. The main blocker was not raw quantity. The blocker was that Chapter 5 promised class spell access, spell progression, and school mapping that Chapter 3 did not actually provide. On top of that, the rules conflicted on whether spell damage scaled, several hard-control spells lasted too long for the game's action economy, and several class abilities duplicated or overshadowed generic spells instead of interacting with them cleanly.

**Short Verdict by Class Bucket:**
- **Sufficient raw support once access is formalized:** Glyphwright, Sangromancer, Hylden Warlock.
- **Partial support but identity needs clearer spell mapping:** Warden of Balance.
- **Under-supported by the compendium relative to class fantasy:** Soul Reaver, Shadowmancer.

---

## Cross-Cutting System Findings

### 1. Class Spell Access Is Promised but Not Defined — 🔴 MAJOR REVISION

**Rules Issue:**
Chapter 5 states that characters know spells by class and level, gain new spells from class lists, and that class access by school is detailed in Chapter 3. But the class chapter does not actually provide spell access blocks, known spell counts, prepared spell counts, or per-level spell gain rules for the caster-leaning classes.

**Why This Matters:**
The spell list may be numerically large, but it is not operational in play. Players and GMs cannot determine what a Soul Reaver, Glyphwright, Warden, or Hylden Warlock can legally cast without inventing access rules at the table.

**Relevant Rules:**
- Chapter 5 promises class-based starting spells and level-up spell gain.
- Chapter 5 says school access is detailed in Chapter 3.
- Chapter 3 does not actually provide those sections.

**Recommendation:**
Add a compact spell access block to every spell-using class:
- Spell schools available
- Starting known or prepared spell count
- Spells gained per level or per tier
- Whether the class knows spells permanently, prepares from a list, or freely casts from school access

---

### 2. Spell Damage Scaling Contradiction — 🔴 MAJOR REVISION

**Rules Issue:**
Core progression says all damaging abilities gain +1 base damage at levels 5, 10, 15, and 20. The spell chapter then says spell damage is static.

**Why This Matters:**
This makes the entire compendium numerically unstable. A spell such as a mid-tier burst is either appropriately bounded or dramatically stronger depending on which rule is applied.

**Design Risk:**
If spells scale under the global damage rule, several Expert and Master tier damage spells become much more dangerous than their listed values suggest. If they do not scale, spell attacks may fall behind weapon users and class abilities that do scale.

**Recommendation:**
State one rule clearly in Chapter 5. Best fit for the current system:
- Direct combat spells and attack spells scale with the global damaging-ability rule.
- Persistent hazards, summons, and long-form rituals do not scale unless they say so explicitly.

---

### 3. Save-Based Spells Scale Worse Than Attack Spells — 🔴 MAJOR REVISION

**Rules Issue:**
Attack spells inherit the combat attack framework and gain Combat Bonus over time. Save-based spells mostly rely on flat tier DR values. In addition, the target may choose a contextually appropriate skill unless the spell specifies one.

**Why This Matters:**
This pushes spellcasters toward attack-roll spells because those grow with the system, while save-based control spells remain flat and sometimes too easy to resist. It also creates table variance because the same spell may be defended with different skill pairings depending on GM interpretation.

**Recommendation:**
Replace flat tier DR as the default for combat spells with a scaling formula, then specify the defending skill on every save-based spell.

Suggested direction:
- Base spell DR by tier
- Add the caster's relevant attribute or mastery modifier
- Lock each spell to one defending skill pairing unless the spell explicitly offers a choice

---

### 4. Hard Control Durations Are Too Long for the Combat Economy — 🔴 MAJOR REVISION

**Rules Issue:**
Several spells remove major actions, movement, spellcasting, or targeting for 1 minute or longer on a single failed save, with inconsistent concentration and repeat-save language.

**Why This Matters:**
This game runs on tight action economy: one Action, limited Bonus Actions, and one Reaction per round. A one-failure lockout of 1 minute is usually not battlefield control. It is encounter removal.

**Recommendation:**
Normalize combat hard control using one of these structures:
- Concentration plus end-of-turn repeat save
- Fixed 1 to 3 round duration for major disables
- Longer durations only on long-cast rituals or scene-scale non-combat magic

---

## Class Coverage Review

### Glyphwright — ⚠️ MINOR REVISION

**Coverage Assessment:**
Glyphwright has enough raw material in the compendium. Glyph spells, wards, triggers, and utility rituals all support the class well.

**Problem:**
The class is mechanically well-served, but its access is not formalized. It also collides with several generic glyph entries in ways that make it unclear whether core abilities are class-only or shared spell options.

**Recommendation:**
Keep the total spell count roughly as-is. Formalize access and convert duplicated effects into explicit Signature Upgrades or class-specific upgrades.

---

### Sangromancer — ⚠️ MINOR REVISION

**Coverage Assessment:**
Sangromancer also has enough raw support. The Blood spell list is broad enough to sustain class identity if access is formalized.

**Problem:**
Several of the class's defining abilities are duplicates or stronger versions of compendium Blood spells. That blurs whether the class is using unique blood sorcery or simply getting free access to common entries.

**Recommendation:**
Preserve the blood spell count, but convert duplicated entries into one of two models:
- Generic spell plus class-specific upgrade
- Class feature with a distinct name and role

---

### Hylden Warlock — ⚠️ MINOR REVISION

**Coverage Assessment:**
Hylden Warlock has enough raw material once Forbidden and selected Ritual or Glyph access is clearly assigned.

**Problem:**
The class overlaps with the Forbidden list heavily, but several of its iconic abilities are duplicated by generic spell entries. This weakens the sense that the Warlock has distinct Hylden mastery.

**Recommendation:**
Keep the spell count, but mark Warlock-exclusive upgrades or rename class-defining abilities so the generic Forbidden list remains distinct.

---

### Warden of Balance — ⚠️ MINOR REVISION

**Coverage Assessment:**
Warden has partial support, but not enough direct identity support. The class fantasy is time, judgment, balance, and Pillar authority. The current compendium only partially supports that through a mix of Ritual and control effects.

**Problem:**
The class feels perk-driven rather than spell-driven. Signature concepts like time stasis, judgment zones, fate rebalance, or anti-corruption magic are not strongly represented as a coherent spell lane.

**Recommendation:**
Add a targeted balance-time cluster of spells rather than a whole new school. Around 8 to 12 spells would likely be enough if paired with class access tags.

Suggested themes:
- Temporal restraint
- Fate marking
- Pillar resonance
- Protective adjudication
- Corruption cleansing

---

### Soul Reaver — 🔴 MAJOR REVISION

**Coverage Assessment:**
Soul Reaver is under-served by the compendium relative to class fantasy.

**Problem:**
The class identity is spectral aggression, realm-shifting, soul rupture, and phase warfare. Most of that exists in class perks and abilities rather than in a supported spell lane. The generic compendium has some spectral and forbidden effects, but not a sufficiently coherent spectral list for this class.

**Recommendation:**
Add a focused spectral package and assign explicit access. Soul Reaver does not need many more spells than a full caster, but it does need enough spectral techniques to make its magic side feel real rather than incidental.

Suggested themes:
- Short-range realm displacement
- Spectral wounds
- anti-teleport or anti-phase locks
- soul disruption
- realm vision and traversal

---

### Shadowmancer — 🔴 MAJOR REVISION

**Coverage Assessment:**
Shadowmancer is also under-served by the compendium relative to class fantasy.

**Problem:**
The class identity is darkness, fear, stealth magic, and shadow entities. Most of that identity currently lives in class perks rather than in Chapter 5. The clearest sign of this gap is that the class includes Darkness as a spell-facing ability, but the compendium does not contain a Darkness spell at all.

**Recommendation:**
Add a formal Darkness spell, then expand shadow and fear support enough that the class is not entirely perk-defined.

Suggested themes:
- darkness fields
- vision denial
- fear propagation
- shadow movement
- temporary shade summons

---

## Spell and Feature Collisions

### 1. Shadowmancer: Darkness Gap in the Original Draft — 🔴 MAJOR REVISION

**Problem at Review Time:**
Shadowmancer gained Darkness, and Living Darkness later modified the Darkness spell, but Chapter 5 did not contain a Darkness spell entry.

**Why This Matters:**
This prevents clean interaction with dispels, counters, shared access, and future spell reference text.

**Recommendation at Review Time:**
Either:
- Add Darkness to the compendium and tag it for Shadowmancer access, or
- Reframe Darkness as a pure class feature with no compendium dependency

---

### 2. Sangromancer Duplicate Entries — ⚠️ MINOR REVISION

**Collisions:**
- Blood Puppet
- Crimson Bind
- Hemodominate

**Problem:**
These appear both as class abilities or perks and as general Blood spells, with overlapping but not identical roles.

**Why This Matters:**
It is unclear whether the class is receiving free spell access, upgraded versions, or unique class-only expressions of a shared magical technique.

**Recommendation:**
Choose one of the following:
- Treat the compendium entry as the base spell and the class feature as an enhancement
- Rename the class features to distinct signature abilities

---

### 3. Glyphwright Duplicate Entries — ⚠️ MINOR REVISION

**Collisions:**
- Glyph of Flame
- Chrono-Ward
- Nexus Glyph

**Problem:**
Glyphwright's core identity overlaps with shared glyph entries, but the rules do not define whether these are baseline spells, free known effects, or exclusive upgrades.

**Recommendation:**
Mark these as Signature Upgrades if the class is meant to own them, or keep them generic and rewrite the class abilities as upgrades.

---

### 4. Hylden Warlock Duplicate Entries — ⚠️ MINOR REVISION

**Collisions:**
- Madness Surge
- Mind Rupture

**Problem:**
Warlock identity is weakened when iconic Hylden-style powers are presented as both class features and generic compendium spells without a hierarchy.

**Recommendation:**
Reserve the stronger version for the class and let the generic spell remain a weaker baseline, or rename the class features.

---

### 5. Soul Reaver: Class Feature Overshadows Generic Spell — ⚠️ MINOR REVISION

**Collision:**
Soul Reaver's Level 18 Soul Storm substantially outclasses the generic Master-tier Soul Storm entry.

**Problem:**
This is not automatically bad, but it needs clear intent. As written, it reads less like an upgrade path and more like two competing versions of the same effect.

**Recommendation:**
Label the class version explicitly as an empowered or signature version of the generic spell, or rename it to preserve compendium clarity.

---

## High-Risk Numerical Balance Issues

### 1. Cursed Equation — 🔴 MAJOR REVISION

**Problem:**
Disadvantage on Will and Soul checks plus loss of Reactions for 1 minute is too oppressive on a single failed save for this system.

**Why It Overreaches:**
Removing Reactions in a one-reaction economy is already strong. Adding broad defensive and magical suppression on top of that pushes it into encounter-removal territory.

**Recommendation:**
Reduce duration, require concentration, and add repeat saves.

---

### 2. Unravel Mind — 🔴 MAJOR REVISION

**Problem:**
Blocking spells and complex actions for 1 minute on one failed save is too punishing for a combat spell.

**Why It Overreaches:**
This can effectively delete enemy casters and many elite foes from a fight with little ongoing cost.

**Recommendation:**
Cap the effect to 1 to 3 rounds, require concentration, and grant end-of-turn repeat saves.

---

### 3. Invocation of Chains — 🔴 MAJOR REVISION

**Problem:**
Restrained plus no external targeting for 1 minute is extremely close to full battlefield removal.

**Why It Overreaches:**
It is a combat spell masquerading as a scene-ending control effect.

**Recommendation:**
Either shorten it to a brief combat lock with repeat saves or reframe it as a ritual-grade binding effect with longer cast time.

---

### 4. Astral Shackle — 🔴 MAJOR REVISION

**Problem:**
Paralysis with potential banishment over a 1-hour duration is too punishing for a standard combat-resolution spell.

**Why It Overreaches:**
Even before banishment resolves, long-duration paralysis is enough to decide most encounters.

**Recommendation:**
Limit combat use to short duration with repeat saves. Reserve long-form exile for rituals, boss-tech, or scene-scale effects.

---

### 5. Annihilation Pulse — 🔴 MAJOR REVISION

**Problem:**
A 20-foot no-save burst for 10 Entropic damage is overtuned, especially if global damage scaling also applies.

**Why It Overreaches:**
No-save burst damage at this size and value leaves too little counterplay for a system built around rolls, reactions, and positioning.

**Recommendation:**
Add a save for half, reduce damage, or introduce a stronger drawback such as ally harm or self-risk beyond the HP cost.

---

### 6. Heartburst — 🔴 MAJOR REVISION

**Problem:**
Heartburst combines an execution threshold, scaling heavy damage, and stun in one spell.

**Why It Overreaches:**
It performs too many premium combat functions at once: finisher, nuke, and hard control.

**Recommendation:**
Choose one primary role:
- Execute below threshold, or
- Fixed heavy damage plus a rider

Do not keep all three functions at current strength.

---

### 7. Black Spiral — 🔴 MAJOR REVISION

**Problem:**
Black Spiral layers area damage, forced movement, restrain, and a stun rider into one cast.

**Why It Overreaches:**
This produces too much battlefield swing for one action, especially in a system where movement and actions are limited and disables are already strong.

**Recommendation:**
Drop one major rider. The cleanest cut is to remove either the restrain or the stun component.

---

## Priority Fix List

### Immediate Revisions Before Playtesting
1. Add class spell access and progression text to every spell-using class.
2. Resolve the spell-damage scaling contradiction.
3. Standardize save-based spell DR and defending skills.
4. Rework long-duration combat hard control.
5. Add Darkness to the compendium or redefine it as a class feature.

### Secondary Revisions
1. Tag or rewrite duplicate spell and class-feature names into a clear Signature Upgrade model.
2. Add targeted spectral support for Soul Reaver.
3. Add targeted shadow support for Shadowmancer.
4. Add targeted balance-time support for Warden of Balance.
5. Retune the worst individual outlier spells after the scaling rule is settled.

### Recommended Structural Model
- **Generic Spells:** Available through class access lists.
- **Signature Upgrades:** Generic spell plus class-only rider or upgrade.
- **Class Features:** Unique powers that do not need to appear in the compendium unless they intentionally interact with generic spell rules.

Under that model, the current compendium likely does not need a massive expansion. It needs clearer access rules, better identity mapping, and a focused set of missing spells for the under-served classes.