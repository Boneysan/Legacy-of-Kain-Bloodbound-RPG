# Mechanics Pass — Foundation (Ch. 0, 9, 10) — 2026-04-26

This document tracks foundational mechanical issues identified during the system audit of Chapters 0, 9, and 10.

---

## Pass 1 — Foundation Consistency

### Issue 1 — Success Threshold Conflict
**Status:** Completed
**Problem:** Ch. 0 uses an absolute scale (2 = Standard), while Ch. 10 uses a relative scale (Target + 1 = Standard). Both conflict with the phrase "DR represents the number of successes needed."
**Recommended Fix:** Unify all chapters to a relative scale:
- **Successes < Target:** Failure
- **Successes = Target:** Standard Success (Meets the target cleanly)
- **Successes = Target - 1:** Marginal Success (Only if Target > 1. Accomplished with a cost/complication)
- **Successes >= Target + 2:** Critical Success/Hit

---

### Issue 2 — Attribute Cap Reconciliation
**Status:** Completed
**Problem:** Ch. 0 states an absolute maximum of 5, but Ch. 2 Lineage Paragons allow a maximum of 6.
**Recommended Fix:** Update Ch. 0 and Ch. 10 to state: "Attribute maximum is 5 (6 for characters with the Lineage Paragon feature)."

---

### Issue 3 — Combat Bonus & Spell Attacks
**Status:** Completed
**Problem:** Ch. 0 and Ch. 10 say Combat Bonus applies to "attacks only" and "not skill checks," but don't explicitly include spell attacks. Ch. 5 §5.10 says spell attacks *do* count.
**Recommended Fix:** Clarify in Ch. 0, 9, and 10 that "Combat Bonus applies to all attack rolls, including melee, ranged, and spell attacks."

---

### Issue 4 — Critical Hit Benefits Inconsistency
**Status:** Completed
**Problem:** Ch. 0 uses "+2 or +3 damage," while Ch. 10 uses "+1 per extra success (max +3)." Ch. 10's model is more granular and rewards high rolls better.
**Recommended Fix:** Unify both chapters and Ch. 9 to use:
- **Bonus Damage:** +1 damage per extra success (maximum +3).
- **Status Effect:** Inflict condition from damage type table.
- **Bypass Armor:** Ignore 1 point of Armor per extra success (maximum equal to the weapon's base damage).
- **Tactical Advantage / Multi-strike:** GM discretion / narrative benefit.

---

### Issue 5 — Push Mechanic Conflict
**Status:** Completed
**Problem:** Ch. 5 §5.5 describes pushing a Forbidden spell as a reroll, while Ch. 0 and Ch. 8 describe pushing as adding 1-3 Corruption Dice.
**Recommended Fix:** Standardize on the "Add 1-3 Corruption Dice" model for all pushes. (This will be implemented in Ch. 0 and Ch. 10 now; Ch. 5 will be updated in its next pass).

---

### Issue 6 — "Free Action" vs "Free Interaction"
**Status:** Completed
**Problem:** Ch. 5 spells use "Free Action," but Ch. 9 uses "Free Interaction."
**Recommended Fix:** Unify terminology to **Free Action**. Define it in Ch. 0 and Ch. 9 as: "Minor activities that don't consume your primary Action, Bonus Action, or Reaction (e.g., dropping an item, speaking briefly, drawing a weapon as part of an attack)."

---

### Issue 7 — Short Rest Duration Conflict
**Status:** Completed
**Problem:** Ch. 0 says 1 hour. Ch. 9 says 10-20 minutes.
**Recommended Fix:** Standardize on **1 hour** for a Short Rest. Nosgoth is an unforgiving world; 10 minutes is too brief for significant recovery.

---

### Issue 8 — Attribute Modifier Formula Missing
**Status:** Completed
**Problem:** The +0/+1/+2 modifier formula used for Save DRs in Ch. 5 is missing from the core attribute definitions in Ch. 0.
**Recommended Fix:** Add the following to Ch. 0:
> **Attribute Modifiers:** For certain effects (like spell Save DRs or specific perks), your attribute provides a modifier based on its score:
> - **Score 1–2:** +0
> - **Score 3–4:** +1
> - **Score 5–6:** +2

---

### Issue 9 — Success vs Extra Success Terminology
**Status:** Completed
**Problem:** Ch. 10 uses "+1 damage per extra success," but "extra success" isn't formally defined in Ch. 0 relative to the target.
**Recommended Fix:** Define **Extra Successes** in Ch. 0 and Ch. 10 as "any successes rolled beyond the amount required to meet the target number (DR or DV)."

---

### Issue 10 — Bloodied Threshold Missing from Ch. 0
**Status:** Completed
**Problem:** Foundational clarity. "Bloodied" is a key state used across lineages and spells but is only defined in Ch. 9.
**Recommended Fix:** Add the Bloodied definition (50% HP or lower) to Ch. 0's resource section.

---

## Pass 2 — Chapter 9 Combat Audit

### Issue 11 — Spectral Damage & Realm Crossing
**Status:** Completed
**Problem:** §9.7.4 defined Spectral damage but didn't state it crosses realms freely (Ch 11 rule).
**Recommended Fix:** Added "Crosses Realms" bullet to §9.7.4.

---

### Issue 12 — Action Economy - Free Action usage
**Status:** Completed
**Problem:** "Opening an unlocked door" was listed as a Free Action but might be too significant.
**Recommended Fix:** Refined Free Action examples to include "speaking briefly (up to 10 words)" and "drawing a weapon as part of an attack action."

---

### Issue 13 — Death Saves - Vampiric Frenzy & Feeding
**Status:** Completed
**Problem:** Unclear if feeding during Frenzy restores HP.
**Recommended Fix:** Clarified that successful feeding during Frenzy restores HP equal to target TV (min 1) and ends the dying state.

---

### Issue 14 — Two-Weapon Fighting (TWF)
**Status:** Completed
**Problem:** No rule for wielding two weapons.
**Recommended Fix:** Added TWF to §9.10: Bonus Action for a second attack with a Light weapon (base damage + extra successes only).

---

### Issue 15 — Grappling & Shoving
**Status:** Completed
**Problem:** Full mechanics were lacking.
**Recommended Fix:** Added specific procedures to §9.10 (contested Fury/Shadow rolls, speed 0 for Grappled, Pushed/Prone for Shove).

---

### Issue 16 — Arc Definition
**Status:** Completed
**Problem:** "Arc" used for refreshes but undefined.
**Recommended Fix:** Added §9.14 "Story Arcs and Sessions" defining an Arc as ~5 levels/milestone-based.

---

### Issue 17 — Opportunity Attacks & Disengage
**Status:** Completed
**Problem:** Lack of clarity on triggers and how to avoid them.
**Recommended Fix:** Defined Disengage in §9.10 and updated Opportunity Attack trigger in §9.8.

---

### Issue 18 — Threat Value (TV) Reference
**Status:** Completed
**Problem:** Used in other chapters but undefined here.
**Recommended Fix:** Added TV note to §9.5 (Damage and Health).
