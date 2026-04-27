# Mechanics Pass — Classes (Ch. 3) — 2026-04-26

This document tracks issues identified during the system audit of Chapter 3: Classes.

---

## Pass 1 — Class Balance & Clarity

### Issue 1 — Blood Knight: Life Drain Mitigation Clarification
**Status:** Completed
**Problem:** *Life Drain* (Passive) heals "equal to half the damage dealt." It is unclear if this refers to the raw roll or damage after Armor and Resistance.
**Recommended Fix:** Clarify: "...heal HP equal to half the damage dealt after all mitigation (round up)."

---

### Issue 2 — Soul Reaver: Spectral Nova Balance
**Status:** Completed
**Problem:** *Spectral Nova* deals 9 Spectral damage at Level 9. This exceeds the base damage of most Master-tier spells and ignores Armor.
**Recommended Fix:** Reduce base damage to **6 Spectral damage**. The level 18 *Soul Storm* upgrade can then increase this to 10 or 12.

---

### Issue 3 — Dreadblade: Perfect Kill Triple Damage Clarification
**Status:** Completed
**Problem:** "Critical Hits deal x3 damage instead of the normal critical bonus." It is unclear if this triples the base damage or the final total (which would be catastrophic).
**Recommended Fix:** Clarify: "Your **Critical Hits** deal triple your weapon's **base damage** (before Extra Success bonuses or other modifiers) instead of adding the normal critical bonus damage."

---

### Issue 4 — Warden of Balance: Arbiter of Finality Scaling
**Status:** Completed
**Problem:** "damage equal to that ally's max HP." Against high-HP allies (e.g., Level 20 Blood Knight with 80+ HP), this is an automatic kill for almost any boss.
**Recommended Fix:** Cap the damage: "...damage equal to that ally's max HP, up to a maximum of **40 damage** (bypasses Armor)."

---

### Issue 5 — Hylden Warlock: Forbidden Truth Scaling
**Status:** Completed
**Problem:** Payer gains only 1 Corruption to bypass a 5 SE Master spell. At Level 15+, 1 Corruption is a very small price for free Master magic.
**Recommended Fix:** Scale the cost: "...gain Corruption equal to half the SE cost of the spell (rounded up)."

---

### Issue 6 — "Blood Damage" undefined in Sangromancer
**Status:** Completed
**Problem:** *Bloodburst* deals "Blood damage," which is not a defined type.
**Recommended Fix:** Standardize to **Physical (Internal)** or simply **Spectral** damage depending on lore intent. Recommended: **Physical damage (bypasses Armor)** to reflect internal blood rupturing.

---

### Issue 7 — Action Economy for Minions (Shadowmancer/Sangromancer)
**Status:** Completed
**Problem:** *Shade Pact*, *Doppelganger*, and *True Fleshcrafting* minions "act on your Bonus Action." It is unclear if commanding them *consumes* your Bonus Action or if they simply share your initiative and take their turn then.
**Recommended Fix:** Clarify: "Commanding an active minion requires a **Bonus Action** on your turn. If you have multiple minions, a single Bonus Action allows you to command all of them."
