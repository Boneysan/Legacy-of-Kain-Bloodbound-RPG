# Bloodbound RPG: Spellcasting Implementation Checklist
**Scope:** Implementation record for revising `05_Spellcasting-and-Magic.md` and `03_Classes.md` based on the spell review  
**Date:** March 8, 2026  
**Depends On:** `Spell-Review_Spellcasting-and-Magic-v1.md`

---

## Purpose

This checklist turned the spell review into a concrete execution order.

The goal was not to rewrite every spell immediately. The goal was to fix the structural blockers first so Chapter 5 and Chapter 3 stopped contradicting each other and the spell system became safe for targeted balance tuning.

This document is now an implementation record. All checklist items below are complete and remain useful as an audit trail for the spell-system pass.

---

## Implementation Order

### Phase 1: Lock the Core Spell Rules in Chapter 5

These decisions must be made before individual spell tuning.

- [x] Define the class spell-access model in one short system block.
  - Decide whether classes use `known spells`, `prepared spells`, or `school access with free choice`.
  - Keep the model compact enough to fit every spell-using class without adding a full Vancian subsystem.

- [x] Resolve the spell-damage scaling contradiction.
  - Update Chapter 5 so it no longer conflicts with the global `damaging abilities gain +1 base damage` rule.
  - Decide explicitly which spell types scale and which do not.
  - Recommended split: direct combat spells scale; hazards, summons, and long-form rituals do not unless specified.

- [x] Replace flat save logic with a clearer spell DR model.
  - Decide whether combat spell DR is `tier only` or `tier plus caster scaling`.
  - If scaling is used, write the formula once in Chapter 5 and apply it consistently.

- [x] Tighten the save rules.
  - Remove or narrow the rule that lets defenders choose any contextually appropriate skill by default.
  - For each save type, define the default defending skill pairing or require every spell to specify one.

- [x] Standardize hard-control rules.
  - Add a short Chapter 5 design note that combat disables should generally use concentration, repeat saves, or short durations.
  - Reserve 1-minute and longer lockouts for rituals, scene powers, or special exceptions.

---

### Phase 2: Add Class Spell Access Blocks to Chapter 3

Do this after the Phase 1 rules are locked.

- [x] Add a spell access subsection to **Soul Reaver**.
  - Define schools available.
  - Define starting spell count and gain rate.
  - Clarify whether its spectral techniques are class features, spells, or both.

- [x] Add a spell access subsection to **Shadowmancer**.
  - Define access to shadow, fear, and stealth-magic effects.
  - Clarify whether Darkness is a spell, a class feature, or both.

- [x] Add a spell access subsection to **Sangromancer**.
  - Define Blood spell access clearly.
  - Clarify which class abilities are signature upgrades versus generic Blood spells.

- [x] Add a spell access subsection to **Glyphwright**.
  - Define Glyph and Ritual access.
  - Clarify whether core glyph abilities are free baseline spells or unique class features.

- [x] Add a spell access subsection to **Warden of Balance**.
  - Define access to balance, time, warding, and cleansing effects.
  - Note that this class likely needs a narrower curated list rather than broad school access.

- [x] Add a spell access subsection to **Hylden Warlock**.
  - Define Forbidden access and any secondary school access.
  - Clarify which iconic Warlock effects remain class-exclusive.

- [x] Add one short class-access summary table near the top of Chapter 3 or Chapter 5.
  - Class
  - Spell schools or tags
  - Casting model
  - Starting spells
  - Gain rate

---

### Phase 3: Clean Up Spell and Feature Collisions

Do this once class access is visible in the class chapter.

- [x] Choose one terminology model for duplicated entries.
  - `Generic Spell + Signature Upgrade`
  - `Signature Upgrade`
  - `Pure Class Feature`

- [x] Resolve the Sangromancer collisions.
  - Blood Puppet
  - Crimson Bind
  - Hemodominate

- [x] Resolve the Glyphwright collisions.
  - Glyph of Flame
  - Chrono-Ward
  - Nexus Glyph

- [x] Resolve the Hylden Warlock collisions.
  - Madness Surge
  - Mind Rupture

- [x] Resolve the Soul Reaver Soul Storm overlap.
  - Decide whether the class version is a named upgrade of the generic spell or a separate ability.

- [x] Resolve the Shadowmancer Darkness gap.
  - Add `Darkness` to Chapter 5 if it is meant to be a spell.
  - Otherwise remove language that calls it a spell and make the class text self-contained.

---

### Phase 4: Fill the Class-Identity Spell Gaps in Chapter 5

Do not expand the compendium broadly. Add only what is needed to make the under-served classes function.

- [x] Add a targeted **Spectral** support package for Soul Reaver.
  - Goal: enough entries to make hybrid casting feel real rather than incidental.
  - Suggested themes: realm displacement, spectral wounds, soul disruption, anti-phase locks, spectral vision.

- [x] Add a targeted **Shadow** support package for Shadowmancer.
  - Goal: enough entries to support darkness, fear, concealment, and shade manipulation.
  - Suggested themes: darkness fields, fear spread, shadow movement, sight denial, temporary shadow entities.

- [x] Add a targeted **Balance / Time** package for Warden of Balance.
  - Goal: enough entries to support judgment, temporal restraint, protective balance, and corruption-cleansing.
  - Suggested themes: time stop fragments, fate marks, anti-corruption wards, Pillar resonance, protective adjudication.

- [x] Keep Glyphwright, Sangromancer, and Hylden Warlock additions minimal unless access review shows a real hole.

---

### Phase 5: Retune the Highest-Risk Spells

Do this after the scaling and access rules are settled.

- [x] Rework **Cursed Equation**.
  - Reduce duration.
  - Add concentration and repeat-save logic if it remains a combat spell.

- [x] Rework **Unravel Mind**.
  - Reduce lockout duration.
  - Add repeat-save logic.

- [x] Rework **Invocation of Chains**.
  - Decide whether it is a short combat disable or a ritual-grade prison effect.

- [x] Rework **Astral Shackle**.
  - Split combat restraint from long-form banishment if necessary.

- [x] Rework **Annihilation Pulse**.
  - Add a save, reduce damage, or increase drawback.

- [x] Rework **Heartburst**.
  - Choose one main job: execute or heavy damage.
  - Remove the current overloaded role compression.

- [x] Rework **Black Spiral**.
  - Remove one major rider so it is not damage, pull, restrain, and stun in one cast.

---

## File-by-File Editing Checklist

### `05_Spellcasting-and-Magic.md`

- [x] Update the spellcasting basics and process sections to reflect the final scaling and save model.
- [x] Update the learning and preparing spells section so it matches the Chapter 3 class-access text.
- [x] Add missing spell entries required by class support, especially Darkness if retained as a spell.
- [x] Reword hard-control spells to match the new control-duration standard.
- [x] Rebalance the highest-risk numerical outliers.
- [x] Add class-access tags or a short notation model if the compendium is meant to show class availability directly.

### `03_Classes.md`

- [x] Add spell access blocks to all spell-using classes.
- [x] Clarify which effects are class features versus spells.
- [x] Rename or relabel duplicated spell names where necessary.
- [x] Ensure class-defining abilities do not silently obsolete generic spells unless that is intentional and stated.

---

## Recommended Decision Defaults

Use these defaults unless a later design pass finds a better model.

- [x] **Spell access model:** light curated-list model rather than free access to all spells in a school.
- [x] **Damage scaling model:** direct combat spells scale; persistent hazards and rituals do not by default.
- [x] **Save model:** each spell specifies its defending skill or uses a strict default by save type.
- [x] **Control model:** combat hard disables usually last 1 to 3 rounds and use repeat saves unless explicitly exceptional.
- [x] **Duplication model:** prefer `Generic Spell + Signature Upgrade` over keeping two unrelated abilities with the same name.

---

## Definition of Done

This implementation pass is complete when all of the following are true:

- [x] Chapter 5 and Chapter 3 no longer contradict each other on spell access.
- [x] Chapter 5 and the global rules no longer contradict each other on damage scaling.
- [x] Every spell-using class has a visible spell access rule.
- [x] Shadowmancer, Soul Reaver, and Warden of Balance each have enough spell support to express class fantasy without relying almost entirely on perks.
- [x] Duplicated spell and feature names are resolved into a consistent model.
- [x] The highest-risk control and burst spells are no longer obvious encounter-breakers.
- [x] The spell system is stable enough for targeted playtesting rather than structural repair.

---

## Recommended Next Pass

Implementation is complete. The next useful pass is targeted playtesting review in this order:

1. Stress-test the new class spell-access model at Levels 1, 5, 10, and 15.
2. Track whether the new class-access tags in Chapter 5 match actual play expectations for each spell-using class.
3. Watch the retuned control and burst spells for encounter swing, especially `Heartburst`, `Astral Shackle`, `Black Spiral`, `Cursed Equation`, and `Unravel Mind`.
4. Collect wording or glossary drift that appears during play and fold it into a later consistency pass rather than reopening the structure immediately.

That order keeps future iteration focused on playtest evidence rather than reopening the structural repair work that this pass completed.