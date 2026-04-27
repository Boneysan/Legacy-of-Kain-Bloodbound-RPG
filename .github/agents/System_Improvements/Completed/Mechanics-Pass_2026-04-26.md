# Mechanics Pass — 2026-04-26

This document tracks issues identified during mechanical review sessions. Each entry includes the problem, its location, and the recommended fix. Items are marked with their status as work progresses.

---

## Pass 1 — Spectral Realm Rules (Ch. 11 §11.5)

Issues identified during review of Section 11.5 after it was written and committed.

---

### Issue 1 — Direct Conflict: Return Threshold (11.1 vs 11.5)

**Status:** Completed

**Location:** `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.1 (Shifting Realms)

**Problem:**
Section 11.1 currently reads:
> *"A character must be at full HP (or SE) to attempt the return, which takes one full round of concentration."*

Section 11.5.1 and the Quick Reference (11.5.7) define the Return Threshold as **50% of maximum HP**. A reader hitting Section 11.1 first encounters the wrong rule. These directly contradict each other.

**Recommended Fix:**
Update Section 11.1 Material Return bullet to read:
> *"Returning to the Material Realm requires a **Soul Portal** or a specific Energy Focus. A character must be at or above **50% of their maximum HP** (the Return Threshold) to attempt the crossing. See [Section 11.5.2](./11_Realms-Terrain-Arcane-Power.md#1152-crossing-the-veil) for full crossing mechanics."*

---

### Issue 2 — Contradiction: Native Spectral Exception Scope (11.5.1)

**Status:** Completed

**Location:** `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.5.1 (Native Spectral Exception paragraph)

**Problem:**
The Native Spectral Exception reads:
> *"Creatures with Spectral Affinity as part of their stat block do not suffer Soul Bleed while in the Spectral Realm."*

Wraith and Revenant are both designated **Spectral Affinity** in Section 11.1's affinity table. As written, this exception makes both PC lineages immune to Soul Bleed — which contradicts the Wraith-specific "1 HP per 3 rounds" exception written three sentences earlier, and leaves Revenants with no defined Soul Bleed rate at all.

The intent of the Native Spectral Exception is to cover **Monster Manual creatures** that truly inhabit the Spectral Realm (Phase Wraith, Silent Mourner, etc.) — not PC lineages who are caught between worlds. That intent is not expressed in the current wording.

**Recommended Fix:**
Update the Native Spectral Exception to scope it to MM/NPC creatures explicitly:

> *"Creatures with **Affinity: Spectral** printed in their Monster Manual stat block do not suffer Soul Bleed while in the Spectral Realm. The Spectral Realm is their natural state of existence — they do not dissolve there. Soul Bleed applies only to visitors: Material and Hybrid characters who have crossed the veil, and PC lineages (including Wraiths and Revenants) whose Spectral Affinity reflects a nature caught between worlds rather than true native habitation. If a native Spectral creature is somehow forced into the Material Realm and then returns to the Spectral Realm, it does not suffer Soul Bleed on that return."*

---

### Issue 3 — Gap: Revenant Soul Bleed Rate Undefined

**Status:** Completed

**Location:** `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.5.1 (Soul Bleed); `player's_handbook/02_Lineages-and-Race.md` — Section 2.6 (Revenants)

**Problem:**
Wraiths have an explicitly defined Soul Bleed rate (1 HP per 3 rounds). Revenants are also Spectral Affinity and are described as "half-wraith, half-corpse beings" — but no Soul Bleed rate is defined for them anywhere in Section 11.5.1 or in the Revenant lineage entry. As written, the default rate (1 HP per turn) would apply, which is inconsistent with the Revenant's nature and lore proximity to the Wraith lineage.

**Recommended Fix:**

Add a **Revenant Exception** paragraph to Section 11.5.1 immediately after the Wraith Exception:

> *"**Revenant Exception:** Revenants are partially anchored to the Spectral Realm by their undead nature. Their Soul Bleed rate is **1 HP per 3 rounds**, the same as the Wraith lineage. They belong to the threshold between worlds — they cannot survive the Spectral Realm indefinitely, but they dissolve more slowly than the fully living."*

Also add a note to the Revenant lineage entry in Chapter 2 (Section 2.6), alongside the Undead Biology bullet, referencing the Soul Bleed rate:
> *"**Soul Bleed:** While in the Spectral Realm, Revenants suffer Soul Bleed at 1 HP per 3 rounds. See [Chapter 11, Section 11.5.1](./11_Realms-Terrain-Arcane-Power.md#1151-the-soul-economy)."*

---

## Pass 2 — Spellcasting & Magic (Ch. 5) vs. Spectral Realm Rules

Issues identified during initial pass of Chapter 5 against the new §11.5 Spectral Realm full rules.

---

### Issue 4 — Reference Drift: Five Spells Point to §11.1 Instead of §11.5

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Spell Compendium (§5.10)

**Problem:**
Every realm-shift reference in the spell compendium uses `Chapter 11, Section 11.1` (the basic Affinity overview). §11.5 is now the authoritative ruleset for crossing the veil, with §11.5.2 governing voluntary shifts and Soul Portals, and §11.5.5 governing forced realm shifts. All five affected spells send the reader to an outdated section.

**Affected Spells:**
| Spell | Line | Should Reference |
|---|---|---|
| **Glyph of Anchoring** | 132 | §11.5.2 — the shift mechanics it blocks |
| **Phase Snare** | 226 | §11.5.2 — the shift mechanics it restricts |
| **Spectral Crossing** | 267 | §11.5 — general Spectral movement rules |
| **Realmshift** | 319 | §11.5 — full rules for realm overlays |
| **Astral Shackle** | 325 | §11.5.5 — forced realm shifts |

**Recommended Fix:**
Update each spell's §11.1 link to the correct §11.5 subsection as listed above.

---

### Issue 5 — BP Suspension Gap: §5.7 Has No Awareness of the Spectral BP Rule

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Section 5.7 (Resource Pools); `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — Section 11.5.6 (What You Cannot Do)

**Problem:**
§11.5.6 establishes that Blood Points cannot be spent while fully manifested in the Spectral Realm:
> *"Use Blood Points (BP). BP is a physical resource tied to living blood. While Spectral, all BP costs are suspended; abilities requiring BP cannot be activated."*

Ch. 5's Resource Pools section (§5.7) has no mention of this rule. Sangromancer players — whose entire spell list runs on BP — need to know that crossing into the Spectral Realm effectively suspends every spell they have. There is no callout, note, or cross-reference anywhere in Ch. 5 to warn them.

**Recommended Fix:**
Add a note to §5.7 under the BP entry:

> *"**While in the Spectral Realm:** BP is suspended — it cannot be spent and abilities requiring it cannot be activated. Your BP pool is preserved intact and becomes available again when you return to the Material Realm. See [Chapter 11, Section 11.5.6](./11_Realms-Terrain-Arcane-Power.md#1156-spectral-action-restrictions)."*

---

### Issue 6 — Undefined Terminology: "Ethereal" in Lantern Rite

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 159 (Lantern Rite, Initiate Ritual Spells)

**Problem:**
Lantern Rite reads: *"30-foot light reveals Invisible/Ethereal for concentration up to 10 minutes."*

"Ethereal" is not a defined condition, trait, or term anywhere in the system. The two valid terms for partially-present Spectral beings are:
- **Incorporeal** — the creature trait for Spectral creatures partially manifested in the Material Realm (defined in the MM and §11.5.3)
- **Spectral creatures** — creatures fully in the Spectral Realm

Given the spell creates a light source in the Material Realm to reveal hidden presences, **Incorporeal** is the correct term (you cannot reveal a fully Spectral creature with a Material-realm light — they're in a different realm entirely).

**Recommended Fix:**
Update Lantern Rite to read: *"30-foot light reveals **Invisible** or **Incorporeal** creatures for Concentration, up to 10 minutes."*

---

### Issue 7 — Astral Shackle: Forced Shift Cost Not Addressed

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 325 (Astral Shackle, Master Forbidden Spells)

**Problem:**
Astral Shackle includes a banishment rider: *"banished to an adjacent realm... until the end of its next turn."* This is a forced realm shift. §11.5.5 defines forced shift consequences:
- Material/Hybrid creature forced into Spectral Realm → loses **1d6 HP** (shock of crossing)
- Spectral creature forced into Material Realm → takes **1d6 Radiant damage**, **Stunned** 1 round

The spell text does not acknowledge these costs. A GM reading both rules has no guidance on whether the spell's banishment applies the §11.5.5 shock cost, waives it (treating the spell as a controlled transit), or triggers something different. Two GMs will rule this oppositely.

**Recommended Fix:**
Add a clause to the Astral Shackle banishment rider explicitly resolving the interaction. Recommended approach — treat it as a controlled banishment that bypasses the shock cost, since a Master-tier spell exerting precise dimensional control should not also randomly damage its target for 1d6:

> *"...it is also banished to an adjacent realm (see [Chapter 11, §11.5.5](./11_Realms-Terrain-Arcane-Power.md#1155-forced-realm-shifts)) until the end of its next turn. This banishment is controlled — the target does not suffer the standard forced-shift shock damage from §11.5.5. Legendary creatures are immune to this banishment rider."*

---

### Issue 8 — Soul Storm: Cross-Realm Tag Inconsistency Between Ch. 3 and Ch. 5

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 330 (Soul Storm, Master Forbidden Spells); `player's_handbook/03_Classes.md` — Soul Reaver class (Soul Storm class feature)

**Problem:**
The Soul Reaver class feature **Soul Storm** in Ch. 3 carries the `*(crosses realms)*` tag applied during the Monster Manual spectral audit. The base spell version in Ch. 5 (§5.10.4) does not have this tag.

Per §5.10's note, the Ch. 5 version is the "generic base" and the class feature is the Signature Upgrade. However, Soul Storm deals Spectral damage — and per the §11.5.3 damage table, Spectral damage crosses realms freely regardless of tags. The tag is primarily a clarity marker for players. A player who learns Soul Storm via scroll discovery (§5.9) rather than the Soul Reaver class would have no explicit guidance that it crosses realms.

**Recommended Fix:**
Add `*(crosses realms)*` tag to the base Soul Storm spell in §5.10.4:

> *"**Soul Storm** [SR, HW]: Cost: 5 SE. 30-ft radius in 120 ft; 6 Spectral damage + **Frightened** (DR 3 Will) + obscured 3 rounds. *(crosses realms)* The Soul Reaver's **Soul Storm** class feature is the Signature Upgrade of this spell."*

---

---

## Pass 3 — Spellcasting & Magic (Ch. 5) Internal Consistency

Issues identified during second pass of Chapter 5 — checking Combat Control Duration compliance, save type correctness, undefined mechanics, and cross-system gaps.

---

### Issue 9 — Combat Control Duration Violations: Three Spells Lock for 1 Minute With No Escape

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md`

**Problem:**
§5.4 states: *"a combat spell that denies actions, spellcasting, movement, or targeting should either last no longer than 3 rounds, require Concentration, or allow an end-of-turn repeat save."*

Three spells violate this rule — they deny movement or actions for a full minute, require no Concentration, and offer no repeat save:

| Spell | Line | Violation |
|---|---|---|
| **Glyph of Chains** [GW, WB, HW] | 182 | **Restrained** + no teleport for **1 minute**. No Concentration, no repeat save. |
| **Glyph of Ruin** [GW, HW] | 242 | Disadvantage on **all saves** + -5 max HP for **1 minute**. No Concentration, no repeat save. Disadvantage on saves directly impairs all spellcasting saves. |
| **Viscera Torrent** [SG] | 255 | **Poisoned** for **1 minute**. No Concentration, no repeat save. Poisoned imposes Disadvantage on attacks and checks. |

**Recommended Fix:**
Add an end-of-turn repeat save to each spell. Suggested additions:
- **Glyph of Chains:** *"A Restrained creature may repeat the save at the end of each of its turns, ending the effect on a success."*
- **Glyph of Ruin:** *"A creature in the aura may repeat the save at the end of each of its turns; on a success, it leaves the aura's effect and is immune to this casting for 1 minute."*
- **Viscera Torrent:** *"The target may repeat the Blood save at the end of each of its turns, ending the Poisoned condition on a success."*

---

### Issue 10 — Soulweave Damage Loop: No Anti-Ping-Pong Clause

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 215 (Soulweave, Adept Ritual Spells)

**Problem:**
Soulweave reads: *"Whenever one linked creature takes damage, half of that damage, rounded down, is also dealt to the other as Spectral damage."*

The secondary Spectral damage dealt to the second creature is itself a damage event. As written, this could trigger the link again — the second creature just took damage, so half goes back to the first, which triggers it again, creating a recursive loop. In a strict RAW reading, two linked creatures taking any damage could infinitely chain until both die.

**Recommended Fix:**
Add a clause: *"This secondary Spectral damage does not itself trigger additional Soulweave transfers."*

---

### Issue 11 — Ceremony of Sorrow: Corruption Removal Has No Check

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 205 (Ceremony of Sorrow, Adept Ritual Spells)

**Problem:**
Ceremony of Sorrow reads: *"10 min; group mourning; remove 1 Corruption or recall memory."*

No skill check or DR is required. The Corruption system (Ch. 8) defines Corruption removal as a significant narrative and mechanical event — the Purification paths in §8.6 involve DR checks, resources, or major story beats. An Adept-tier ritual that automatically removes 1 Corruption with just 10 minutes and group roleplay has no mechanical cost to balance it against the other purification methods.

**Recommended Fix:**
Add a DR check requirement. Suggested:
> *"10 min; group mourning ritual; make a DR 2 Soul + Ritualism check. On a success, one participant of your choice removes 1 Corruption or recalls a suppressed memory. On a failure, the ritual provides emotional catharsis but no mechanical benefit."*

---

### Issue 12 — Spirit Echo: Automatic Spiritual Sensing With No Check

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 163 (Spirit Echo, Initiate Ritual Spells)

**Problem:**
Spirit Echo reads: *"1 min; self; sense spiritual traces in 30-ft area (number, emotion)."*

No check, no DR. For 1 SE, the caster automatically and infallibly senses every spiritual presence in a 30-ft radius. This functions as a free auto-detect of Spectral creatures, spirits, and undead — which would normally be a significant perception feat requiring a check. Most sensing abilities in the system require at least a DR 1 check.

**Recommended Fix:**
Add a check:
> *"1 min; self; make a Soul + Observation or Soul + Forbidden Knowledge check (DR 1). On a success, sense the number and general emotional state of spiritual traces in a 30-ft area. On a failure, sense only that spiritual traces are or are not present."*

---

### Issue 13 — Hemostatic Pulse: "(1/min limit)" Is Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 149 (Hemostatic Pulse, Initiate Blood Spells)

**Problem:**
Hemostatic Pulse reads: *"Touch; heal 2 HP (1/min limit)."*

The "(1/min limit)" restriction is unexplained. It is unclear whether this means:
- The caster can only cast it once per minute, OR
- The target can only benefit from it once per minute

If it's a once-per-minute casting restriction, that's an unusual mechanic not used anywhere else in the compendium and needs a proper definition. If it's a target restriction (can't be repeatedly healed on the same wound), that needs to say so. As written, a GM and player will interpret this differently.

**Recommended Fix:**
Rewrite the restriction with explicit language:
> *"Touch; heal 2 HP. A creature can benefit from Hemostatic Pulse only once per minute — casting it again on the same target before that time has elapsed has no effect."*

---

### Issue 14 — Blood Mark: Touch Clause Is Redundant and Confusing

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 144 (Blood Mark, Initiate Blood Spells)

**Problem:**
Blood Mark reads: *"30 ft; one creature you can see. Until the end of your next turn, the first attack made against the target each round has Advantage. If you touch a willing target while casting, you may instead place the mark through contact."*

The second sentence is confusing. The spell already targets at 30 ft with no stated requirement for touch. The touch option doesn't appear to grant anything the 30-ft cast doesn't already provide — same effect, same target type (willing target for marking an ally). If the touch option is meant to allow casting the spell without verbal or somatic components (useful for stealth), or to bypass some other restriction, that's not stated.

**Recommended Fix:**
Either remove the redundant touch clause, or clarify what the touch version provides that the ranged version doesn't:
> *"If you touch a willing target while casting instead of targeting at range, the mark lasts until the end of the scene rather than until the end of your next turn."*

---

### Issue 15 — Glyph of Displacement: Wrong Save Type

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 184 (Glyph of Displacement, Adept Glyph Spells)

**Problem:**
Glyph of Displacement reads: *"Touch; triggers on touch; DR 2 Will or teleport 15 feet random."*

Per the Save Types table (§5.2), **Will saves** resist mental effects: fear, charm, confusion, psychic intrusion. A random physical teleportation is not a mental effect — it is a physical displacement, which should be resisted with an **Evasion save** (dodge effects: area blasts, traps, sweeping hazards) or a **Blood save** (physical effects: knockback, binding, bodily manipulation). A character with high Will but low physical agility should not be inherently resistant to being flung 15 feet.

**Recommended Fix:**
Change the save type:
> *"Touch; triggers on touch; DR 2 **Evasion** save or teleport 15 feet in a random direction."*

---

### Issue 16 — Glyph of Anchoring: Blocks Soul Portals in Both Realms — Not Addressed

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 132 (Glyph of Anchoring, Initiate Glyph Spells); `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — §11.5.3

**Problem:**
§11.5.3 states: *"A placed glyph affects creatures in both the Material and Spectral Realm simultaneously unless the glyph's text specifies otherwise."*

Glyph of Anchoring blocks any creature from teleporting or shifting realms through the designated square. Because glyphs cross both realms, this means a placed Glyph of Anchoring also blocks Spectral characters from using a Soul Portal to return to the Material Realm — if the Soul Portal occupies or is adjacent to that square.

For 1 SE, a Glyphwright or Warden of Balance can effectively trap any Spectral character at a Soul Portal, preventing their return indefinitely. This is a powerful tactical interaction that exists entirely due to the §11.5.3 cross-realm glyph rule — and the spell text has no guidance on it.

**Recommended Fix:**
Add a note to the spell clarifying the cross-realm interaction:
> *"Because glyphs affect both realms simultaneously (Ch. 11 §11.5.3), this glyph also blocks realm-shift crossing attempts at Soul Portals from the Spectral side. A Spectral creature attempting to use a Soul Portal in the affected square must still succeed on the DR 2 Will save or the crossing fails."*

---

---

## Pass 4 — Spellcasting & Magic (Ch. 5) Description Quality

Issues identified during third pass of Chapter 5 — checking spell descriptions for runability, clarity, undefined effects, setting consistency, and bonus type ambiguity.

---

### Issue 17 — Unrunnable Spells: Effects Are Placeholder Notes, Not Definitions

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Multiple spells across all tiers

**Problem:**
A significant number of spells — particularly at Adept, Expert, and Master tiers — have descriptions so terse they cannot be run at the table without the GM inventing the mechanics. These are bullet-point notes masquerading as spell definitions. A GM should never have to guess what a spell does.

**Affected Spells (by tier):**

| Spell | Line | What Is Undefined |
|---|---|---|
| **Echo Word** [GW, SM] | 158 | "store phrase, echoes on trigger" — what kind of trigger? Any sound? A specific keyword? Proximity? |
| **Warding Circle** [GW, WB] | 164 | "blocks chosen type + bonuses for 1 hr" — what creature types can be blocked? What bonuses does it provide? |
| **Chrono-Ward Ritual** [GW, WB] | 206 | "delay trigger by time condition + Initiate effect" — what is a "time condition"? Which Initiate effect is added? |
| **Glyph of Echoes** [GW] | 185 | "records/copies halved Initiate/Adept glyph 1 round later" — what does "halved" mean? Half damage? Half area? Half duration? |
| **Glyph of Entropy** [GW, HW] | 186 | "equipment flaw 1 minute" — what is an equipment flaw mechanically? -1 damage? Weapon breaks? |
| **Bloodrite Brand** [SG] | 249 | "permanent brand (fealty, outcast, or suffering)" — all three brand types are undefined. What does each actually do? |
| **Beckon of the Deep** [HW] | 258 | "summon abyssal creature" — no stats, no HP, no duration, no control mechanic. Completely unrunnable. |
| **Sanctify Ground** [WB] | 265 | "damage/penalties to Undead/Corrupted + ally bonuses 24 hours" — no damage value, no penalty definition, no ally bonus definition. |
| **Dark Reflection** [SM, HW] | 273 | "summon reflection (your stats, Spectral damage attacks, menace/teleport)" — "menace/teleport" is undefined. Can the reflection die? Does it act on your turn? Does it have your HP? |
| **Fatebind Curse** [WB, HW] | 275 | "auto-fail/crit hit once/session until removed" — ambiguous subject. Auto-fail *what save*? Crit hit *by whom*? Against *whom*? |
| **Vital Dominion** [SG] | 308 | "choose siphon/deaccelerate/puppet effects 1 min" — three named effects with no definitions. |
| **Crimson Godseed** [SG] | 302 | "+1 attribute/spell" — "+1 spell" is not a defined term. +1 spell known? +1 die to all spells? |
| **Throne of Veins** [SG] | 307 | "+1 save DR 10 min" — whose saves? The caster's spell DRs? All allies' saves? Ambiguous. |
| **Curse of the Nine Moons** [HW] | 314 | "madness/transformation/withering" — three undefined curse options. |
| **Ritual of Eclipse** [SM, WB, HW] | 320 | "weaken sunlight users + empower shadows 1 hr" — who are "sunlight users"? What is the mechanical weakening? What does "empower shadows" grant? |
| **Eternal Sigil** [GW, WB] | 316 | "elemental bane" — this ward effect is not defined anywhere in the system. |
| **Reaver Unleashed** [SR, HW] | 329 | "Reaver boost 1 min" — what is the Reaver boost? No stats, no effect definition. |

**Recommended Fix:**
Each of these spells requires a full effect description before the compendium is table-ready. These should be flagged for a dedicated expansion pass where each spell receives a complete mechanical definition — not a summary.

---

### Issue 18 — "Limited Actions" Is Undefined Across Two Master Spells

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 292 and 313

**Problem:**
Two separate spells use "limited actions" as a condition with no definition:
- **Glyph of Time Sever** [GW, WB] (line 292): "DR 4 Will or limited actions/reactions in 15-ft area 3 rounds"
- **Chrono Collapse** [WB, HW] (line 313): "DR 4 Will save or limited actions 3 rounds"

"Limited actions" is not a defined condition in the system. Does it mean: one action only (no Bonus Action)? No Reactions? Only movement? Reduced to a single die roll? Two GMs will read this completely differently.

**Recommended Fix:**
Define the effect explicitly. Suggested standard:
> *"The target may take only one Action or one Bonus Action on each of its turns (not both), and cannot take Reactions. Movement is unaffected."*

---

### Issue 19 — "Risky Roll" in Omen Tether Is Not a Defined Game Term

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 225 (Omen Tether, Adept Forbidden)

**Problem:**
Omen Tether reads: *"DR 2 Will or suffer Disadvantage on one risky roll (Reaction to impose)."*

"Risky roll" is not defined anywhere in the system. This is entirely GM-subjective — one GM might apply it to any roll the player attempts, another only to attack rolls, another only when the GM narratively deems a roll "risky." The Reaction-to-impose timing also needs clarification: does the caster declare which roll is the "risky" one before or after the triggering roll is declared?

**Recommended Fix:**
Replace "risky roll" with a specific trigger:
> *"DR 2 Will save or suffer Disadvantage on the next attack roll, spell attack, or skill check the target makes before the end of its next turn (Reaction to impose after the target declares its action but before it rolls)."*

---

### Issue 20 — Eyes Beyond: "See Invisible" Does Not Explicitly Say "Invisible Creatures"

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 222 (Eyes Beyond, Adept Forbidden)

**Problem:**
Eyes Beyond reads: *"1 min; self; see in darkness/invisible +1 Observation for 10 min (-1 social)."*

"See invisible" is shorthand. It's unclear whether this means: see creatures that are currently invisible, see objects that are invisible, see invisible magical effects, or all of the above. In a system with Wraith Phasing, Incorporeal creatures, and Spectral realm mechanics, this distinction matters — can Eyes Beyond see a phased Wraith? A fully Spectral creature? An invisible trap?

**Recommended Fix:**
> *"For 10 minutes, you can see **invisible creatures** and objects within your normal sight range. This does not grant Spectral sight or the ability to perceive creatures in a different realm."*

---

### Issue 21 — Soul Flicker: "(No Offensive Actions)" Is Ambiguous

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 162 (Soul Flicker, Initiate Ritual)

**Problem:**
Soul Flicker reads: *"Self; attacks against you have Disadvantage until your next turn (no offensive actions)."*

The "(no offensive actions)" restriction is buried as a parenthetical and reads ambiguously — does it mean *the caster* cannot take offensive actions, or *attackers* cannot? The placement suggests it's a restriction on the caster (you become evasive but cannot attack), but it's not stated explicitly. "Offensive actions" is also not a defined term — does it include casting a damaging spell? Using an ability? Pushing?

**Recommended Fix:**
> *"Self; until the start of your next turn, all attacks against you are made with Disadvantage. While this effect is active, you cannot make attack rolls, cast damaging spells, or take any action that directly targets another creature with harm."*

---

### Issue 22 — Binding of the Starborn: "Celestial Entity" Is Setting-Inconsistent

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 312 (Binding of the Starborn, Master Ritual)

**Problem:**
Binding of the Starborn reads: *"1 hr under stars; summon celestial entity for task (DR 4 Soul + Rituals)."*

In Nosgoth, there are no benevolent celestial beings to summon. The only known divine presence is the Elder God — a malevolent cosmic parasite. The Pillars are shattered. The Ancients are dead or imprisoned. "Celestial entity" is generic high fantasy that does not exist in Legacy of Kain's cosmology. A Warden of Balance summoning a "celestial entity for a task" has no lore foundation.

**Recommended Fix:**
Reframe the spell around Nosgoth's actual cosmology:
> *"1 hr under open sky at a site of ancient power; you call upon a **Bound Guardian** — an ancient pre-Vampire spirit once tasked with protecting a sacred place or object. The spirit manifests to perform one task within its domain (DR 4 Soul + Ritualism). It is not benevolent; it is bound. It will fulfill the letter of your request but resents the summons. It departs when the task is complete or at dawn, whichever comes first."*

---

### Issue 23 — "+2 Bonus" Ambiguity Across Multiple Spells

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Multiple spells

**Problem:**
The system uses dice pools — bonuses are expressed as "+X dice" or "+X successes." Several spells use plain "+2" with no qualifier, which makes the bonus type ambiguous:

| Spell | Line | Ambiguous Text |
|---|---|---|
| **Pillar Resonance** | 211 | "+2 related skill check 1 hr" |
| **Rite of Echoes** | 213 | "+2 Social check related to echoes 1 hr" |
| **Sanctify Blade** | 214 | "magical +2 vs. Undead/Corrupted" |
| **Communion of Shadows** | 207 | "+2 Stealth in dim light" |
| **Spiritforge Circle** | 268 | "+2 Craft for magic items 8 hours" |

+2 dice is a meaningful mechanical benefit. +2 successes is enormous (essentially guaranteeing success on most checks). These need standardizing.

**Recommended Fix:**
Standardize all instances to **"+2 dice"** unless a specific spell intends to grant successes (which should say "+2 successes"). Review each spell and confirm the intended amount is +2 dice.

---

### Issue 24 — Corruption Crown: "Dread Aura" Is Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 327 (Corruption Crown, Master Forbidden)

**Problem:**
Corruption Crown reads: *"Self; +2 Intimidation/Deception + Charmed on damage (DR 3 Will save) + dread aura 10 min."*

"Dread aura" is listed as a third effect with no mechanical definition. It's not a defined condition, trait, or term anywhere in the system. As written, the GM must invent what the dread aura does — which defeats the purpose of a written spell.

**Recommended Fix:**
Define the dread aura explicitly:
> *"While this spell is active, you emit a **Dread Aura** in a 10-foot radius. Creatures of your choice in the aura that start their turn there must succeed on a DR 2 Will save or suffer Disadvantage on attack rolls against you until the start of their next turn."*

---

---

## Pass 5 — Spellcasting & Magic (Ch. 5) Resource Costs, Undefined Terms, and Edge Cases

Issues identified during fourth pass of Chapter 5 — checking resource cost consistency, undefined conditions and triggers, balance edge cases, and structural gaps.

---

### Issue 25 — Counterspell Is Defined as a Reaction But Does Not Appear in the Compendium

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Section 5.6 (Reactions to Spells)

**Problem:**
§5.6 lists **Counterspell** as a standard Reaction available to casters:
> *"Counterspell: Contested roll (Relevant Attribute + Magical Skill) vs. incoming spell's DR or caster's roll."*

Counterspell does not appear anywhere in the §5.10 Spell Compendium. It is treated as a universal ability available to any caster, with no class restriction, no SE cost, and no access tag. This raises several unanswered questions:
- Is every character with any spellcasting ability allowed to Counterspell, or only specific classes?
- What is the SE cost, if any?
- Can non-casters with a single utility spell (e.g., via a perk) Counterspell?
- If it has no cost, it is effectively a free reaction that every caster always has available — a significant and never-stated mechanical benefit.

**Recommended Fix:**
Add a formal Counterspell entry to §5.6 with explicit access conditions, cost, and limits:
> *"**Counterspell** (Reaction): Available to any character who can cast spells. Cost: 1 SE. Trigger: You see a creature within 60 feet begin casting a spell. Roll your relevant casting Attribute + Magical Skill (e.g., Soul + Glyphcasting, Will + Forbidden Knowledge). Contested against the caster's roll or, for non-attack spells, against the spell's DR. On a success, the spell is disrupted and fails. The SE cost is lost regardless of outcome."*

---

### Issue 26 — Rotmind Rift: Corruption Escalation Rate Is Potentially Game-Breaking

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 279 (Rotmind Rift, Expert Forbidden)

**Problem:**
Rotmind Rift reads: *"DR 3 Will or gain 1 Corruption at the start of each turn + random madness effect 1 minute."*

If the target fails the initial save and fails repeat saves, they gain 1 Corruption per turn for up to 10 rounds (1 minute). That is potentially +10 Corruption Levels from a single spell. Per Ch. 8, a character at Corruption Level 15 becomes an NPC monster under GM control. Starting from 0, a player character who fails every save against this spell would hit 10 Corruption before the spell ends — going from Uncorrupted to Abyss-Bound (Tier 3 Corrupted Perks) in a single combat encounter.

Against player characters, this spell can functionally destroy a character without killing them. The only balancing mechanic is the repeat DR 3 Will save each turn.

**Recommended Fix:**
Add a total Corruption cap to the spell:
> *"...gain 1 Corruption at the start of each turn + random madness effect for 1 minute. This spell cannot cause a target to gain more than 3 Corruption Levels total, regardless of duration."*

---

### Issue 27 — Soulforge Resurrection: "5 SE/BP" Cost Is Ambiguous

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 321 (Soulforge Resurrection, Master Ritual)

**Problem:**
Soulforge Resurrection reads: *"Cost: 5 SE/BP."*

The "/" is ambiguous. This could mean:
- 5 SE **or** 5 BP (the caster pays whichever resource they use)
- 5 SE **and** 5 BP (a dual cost)
- The cost varies by class (Sangromancer pays BP; others pay SE)

Given the access tags [SG, WB, HW] — Sangromancer (BP caster), Warden of Balance (SE caster), Hylden Warlock (SE caster) — "or" is likely the intent, but this needs to be stated explicitly.

**Recommended Fix:**
> *"Cost: 5 SE **or** 5 BP (choose based on your primary casting resource; a Sangromancer pays 5 BP, all other classes pay 5 SE)."*

---

### Issue 28 — The God's Rebuttal: "Reaction on Divine" Trigger Is Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 331 (The God's Rebuttal, Master Forbidden)

**Problem:**
The God's Rebuttal reads: *"Reaction on divine; opposed check to counter + 4 Entropic (Void) damage backlash."*

"Reaction on divine" specifies the trigger as a "divine" effect, but "divine" is not a defined tag, category, or trait anywhere in the system. In Nosgoth's world, the only recognized divine force is the Elder God (malevolent) and the Pillars of Nosgoth (neutral/destroyed). What qualifies as "divine"?

Does "divine" mean:
- Any spell cast by a Warden of Balance?
- Any ability tagged or flavored as holy/radiant?
- Any ability that deals Radiant damage?
- Any ability from a creature designated as a god or divine entity?

Without a definition, this Reaction has no reliable trigger.

**Recommended Fix:**
Define "divine" in context:
> *"Reaction: Trigger — a creature within 60 feet uses a **Radiant** damage ability, casts a Ritual or Warden of Balance spell, or invokes a holy or divine effect. Roll an opposed check (your Soul + Forbidden Knowledge vs. the triggering roll or effect's DR). On a success, the effect is partially countered (halve its damage or duration). Regardless of success, the triggering creature takes 4 Entropic (Void) damage."*

---

### Issue 29 — Mind Spike: "Paranoia" Is Not a Defined Condition

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 280 (Mind Spike, Expert Forbidden)

**Problem:**
Mind Spike reads: *"4 Spectral damage + DR 3 Will or Corruption Die/paranoia 1 round."*

"Paranoia" is not a defined condition in the Glossary or anywhere in the system. It is used here as if it has mechanical weight, but there are no rules for what paranoia imposes. Is it a flavor note? Does it cause Disadvantage on something? Does it cause the target to suspect allies? Does it impose the Confused condition?

The "Corruption Die/paranoia" notation is also unusual — does rolling the Corruption Die cause the paranoia? Or is "paranoia" an alternative effect to the Corruption Die?

**Recommended Fix:**
Define the effect explicitly:
> *"DR 3 Will save or roll 1 Corruption Die and suffer **paranoia** for 1 round: the target treats all creatures within 30 feet (including allies) as potential threats, suffering Disadvantage on all social checks and Reactions. If an ally of the target attempts to touch them, the target may immediately make one basic attack against that ally as a free Reaction."*

---

### Issue 30 — Cacophonic Flare: Slash Notation Makes Conditions Unreadable

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 272 (Cacophonic Flare, Expert Forbidden)

**Problem:**
Cacophonic Flare reads: *"DR 3 Will or Deafened/Stunned + Blinded/-1 die on Will rolls for 1 minute."*

The slash notation makes it genuinely unclear what the target suffers on a failed save. There are four effects listed with two "/" separators and a "+" — does failure cause:
- **Deafened** AND **Stunned** AND **Blinded** AND -1 die on Will rolls?
- **Deafened** OR **Stunned** (choose one) AND **Blinded** AND -1 die?
- **Deafened** (1 round) THEN **Stunned** (1 round) AND separately **Blinded** AND -1 die?

The "for 1 minute" at the end applies to everything, or only the last effect? This spell cannot be run consistently from its current text.

**Recommended Fix:**
Rewrite with explicit condition listing:
> *"DR 3 Will save or the target is **Stunned** until the end of its next turn, then **Deafened** and **Blinded** for 1 minute. While Deafened and Blinded by this spell, the target also suffers -1 die on Will saves. The target may repeat the save at the end of each of its turns, ending the Deafened and Blinded conditions on a success (the Stun ends normally)."*

---

### Issue 31 — Staggered Is Referenced But Has No Standalone Condition Entry

**Status:** Completed

**Location:** `player's_handbook/12_Glossary.md` — §12.4 Damage and Status Effects; `player's_handbook/09_Combat.md` (likely)

**Problem:**
The Stunned condition entry references **Staggered** as a lesser condition: *"More severe than Staggered (Reactions only); less severe than Paralyzed."*

Staggered also appears in the damage type table as a Physical damage rider. However, Staggered has no standalone definition entry in §12.4 — it is only defined implicitly via the Stunned comparison ("Reactions only"). If a player asks "what does Staggered mean?" they must infer the definition from a parenthetical in another condition's entry. This is a documentation gap, not a spell gap, but it directly affects spell resolution for any ability that inflicts Staggered.

**Recommended Fix:**
Add a Staggered entry to the condition table in §12.4:
> *"**Staggered** | 1 round unless source specifies otherwise | The target cannot take Reactions. Actions, Bonus Actions, and movement are unaffected. Less severe than Stunned (which also removes Actions and Bonus Actions)."*

---

### Issue 32 — Sanguine Eclipse: Exhaustion Stacks Not Specified

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 305 (Sanguine Eclipse, Master Blood)

**Problem:**
Sanguine Eclipse reads: *"obscured + 3 Spectral damage + exhaustion (DR 3 Blood) + halved healing 1 min."*

The Exhaustion condition stacks up to 3 (per §12.4 Glossary): each stack imposes -1 die on all rolls, and 3 stacks also cause Incapacitation. Sanguine Eclipse doesn't specify how many Exhaustion stacks are applied on a failed DR 3 Blood save. Is it 1 stack? 2 stacks? This omission means two different rulings are equally valid.

**Recommended Fix:**
Specify the stack count:
> *"...exhaustion (**1 Exhaustion stack**, DR 3 Blood save negates) + halved healing for 1 minute."*

---

### Issue 33 — Vital Hook: "Bonus Pull" Is Ambiguous Phrasing

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 202 (Vital Hook, Adept Blood)

**Problem:**
Vital Hook reads: *"30 feet; spell attack, 2 Spectral damage + Bonus pull 10 feet (DR 2 Blood) for concentration 1 minute."*

"Bonus pull" is ambiguous. It could mean:
- The pull happens as a **Bonus Action** (separate from the attack Action)
- The pull is a **bonus effect** that occurs in addition to the damage on a hit
- The pull repeats each turn as a bonus effect while concentration is maintained

The "for concentration 1 minute" at the end also introduces confusion — does the pull repeat every turn? Or does the concentration maintain the tether (like Blood Leash), requiring DR saves to escape?

**Recommended Fix:**
Rewrite for clarity:
> *"30 feet; spell attack, 2 Spectral damage. On a hit, the target must succeed on a DR 2 Blood save or be pulled 10 feet toward you. While you maintain Concentration (up to 1 minute), the target is tethered — at the start of each of your turns you may pull the tethered target 10 feet toward you as a free effect (no additional save)."*

---

---

## Pass 6 — Spellcasting & Magic (Ch. 5) Interactions, Coverage Gaps, and Balance

Issues identified during fifth pass — checking spell interactions, class coverage gaps, DR scaling consistency, and balance outliers.

---

### Issue 34 — Fixed DR vs. Scaling DR: Listed DRs Can Conflict With the §5.2 Formula

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Section 5.2 and throughout §5.10

**Problem:**
§5.2 defines a scaling DR formula: tier base (Initiate 1, Adept 2, Expert 3, Master 4) plus caster attribute modifier (+0, +1, or +2 based on casting attribute score). This means a high-attribute caster's Initiate spells should reach DR 3.

However, spells in §5.10 list specific fixed DRs. §5.10's preamble states these override the formula ("unless a spell says otherwise, use the DR model in Section 5.2"). As a result:

- **Blood Leash** (Initiate): listed DR 2. A Soul 5 Sangromancer would normally get DR 3, but the fixed DR 2 caps it lower.
- **Bloodlash Field** (Expert, 3 BP): listed DR 2 Evasion for a control effect. Expert base is DR 3 — this is a below-tier DR on a resource-costing Expert spell.
- Most Adept spells list DR 2–3; most Expert spells list DR 3. This is generally consistent with the formula, but hardcoding these values removes the benefit of investing in high casting attributes.

The root problem: there is no declared design intent. Is it intended that listed DRs are fixed (attribute investment doesn't improve them), or are they example values that should scale? Without a clear statement, high-attribute casters are silently nerfed on spells with listed DRs.

**Recommended Fix:**
Add a design note to §5.10 preamble:
> *"Spells that list a specific DR use that as a **floor**, not a fixed value. If the §5.2 formula would produce a higher DR for your casting attribute, use the higher value. The listed DR represents the minimum a caster of that tier achieves."*

---

### Issue 35 — Sangromancer Has Zero SE Spells: Completely Non-Functional While Spectral

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — §5.10 (all Sangromancer entries); `player's_handbook/11_Realms-Terrain-Arcane-Power.md` — §11.5.6

**Problem:**
The Sangromancer [SG] has **42 spell entries** in the compendium. Every single one costs **Blood Points (BP)**. There are zero SE-cost options for a Sangromancer.

§11.5.6 establishes that BP cannot be spent while in the Spectral Realm. The consequence: if a Sangromancer is forced into, voluntarily shifts to, or begins combat in the Spectral Realm, they have **no spells whatsoever**. All 42 spells are suspended. A level 20 Sangromancer in the Spectral Realm is a melee fighter with no magical options.

This may be intentional — Sangromancers are blood-and-body casters who do not belong in the Spectral Realm — but it is never stated as such. A player building a Sangromancer who also takes Spectral-adjacent lineage traits or encounters Spectral terrain will discover this mid-session with no warning.

**Recommended Fix:**
Two options:
1. **Design acknowledgement**: Add a sidebar to the Sangromancer class entry in Ch. 3 and to §5.7: *"Sangromancers are wholly Material-realm casters. Their spells require living blood and cannot function in the Spectral Realm. A Sangromancer who crosses the veil retains their BP pool but cannot access it until they return."*
2. **One SE fallback**: Give the Sangromancer one SE-cost spell at Adept or Expert tier as a Spectral emergency option (thematically, a desperate blood-memory or soul-echo ability).

---

### Issue 36 — Darkness + Eyes Beyond: Interaction Unresolved

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 220 (Darkness) and 222 (Eyes Beyond)

**Problem:**
**Darkness** [SM, HW] creates magical darkness. Its text says: *"Creatures without a feature that explicitly lets them see through magical darkness are effectively Blinded while inside it."*

**Eyes Beyond** [SM, HW] (as currently written) lets you "see in darkness." The obvious player intent: cast Darkness, then cast Eyes Beyond to see while all enemies are Blinded. However, Darkness specifies that creatures need a feature that "explicitly lets them see through **magical** darkness." Eyes Beyond says "see in darkness" — which is ambiguous on whether it applies to magical or only natural darkness.

If Eyes Beyond does work in magical darkness, the Shadowmancer/Hylden Warlock gains a reliable "Blinded enemies, I can see" combo from two Adept spells. If it does not, the combo is blocked and players need to know this.

**Recommended Fix:**
Clarify Eyes Beyond's text to explicitly resolve the interaction:
> *"For 10 minutes, you can see **invisible creatures** and objects, and can see normally in both natural and **magical darkness** as if in bright light."*

(If the intent is that Eyes Beyond does NOT pierce magical darkness, instead write: *"...and can see normally in natural darkness. This does not allow you to see through magical darkness created by spells or abilities."*)

---

### Issue 37 — Realmshift + Glyph of Anchoring: Interaction Not Addressed

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 132 (Glyph of Anchoring) and 319 (Realmshift)

**Problem:**
**Realmshift** [SR, WB, HW] creates a 60-ft overlay of the Spectral Realm over a physical location. Any creature or object within the area is simultaneously present in both realms.

**Glyph of Anchoring** prevents any realm-shifting or teleportation through the designated square. Per §11.5.3, glyphs affect both realms simultaneously.

If a Glyph of Anchoring is placed within the area where Realmshift is cast, does the glyph trigger? Realmshift doesn't move creatures — it overlays the realm onto them. Is an overlay a "shift"? If the glyph does trigger, Realmshift would fail in any area where Anchoring glyphs have been pre-placed — a 1 SE Initiate glyph countering a 5 SE Master ritual, which is a dramatic cost disparity.

**Recommended Fix:**
Clarify the interaction in one of the two spells:
> *"Realmshift: This spell overlays the Spectral Realm across an area rather than shifting individual creatures. Glyph of Anchoring glyphs within the area do not trigger against Realmshift's overlay — it is not a creature shifting realms. However, any creature who attempts to voluntarily cross the veil within the Realmshift area must still contend with active Anchoring glyphs."*

---

### Issue 38 — Nightmare Seed: Initiate-Tier Spell With Disproportionate Duration

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 174 (Nightmare Seed, Initiate Forbidden)

**Problem:**
Nightmare Seed reads: *"Touch sleeping; nightmares deny rest + DR 2 Will or Frightened 10 min."*

For 1 SE and no Corruption cost, a caster who touches a sleeping creature can inflict **Frightened for 10 minutes** on a failed DR 2 Will save. Compare to:
- **Hex of Pain** (Initiate, 1 SE): Disadvantage on attacks for **1 round**
- **Dread Chain** (Adept, 2 SE): Frightened for **up to 1 minute**, with repeat saves

Nightmare Seed grants 10 minutes of Frightened — ten times longer than Dread Chain — at a lower tier and half the cost, with no repeat save. The "Touch sleeping" requirement is the sole limiter. In ambush scenarios, dungeon delves, or any scene involving resting enemies, this condition is routinely satisfiable.

**Recommended Fix:**
Either reduce the duration to 1 minute (matching Adept-tier Frightened effects) or add a repeat save:
> *"...DR 2 Will or Frightened for up to 1 minute. The target may repeat the save at the end of each of its turns, ending the effect on a success."*

---

### Issue 39 — "Once Per Long Rest" Restriction Exists Only on Sangromancer Spells

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 254 (Heartburst) and 304 (Hemodominate)

**Problem:**
Only two spells in the entire compendium carry a "once per long rest" usage restriction — **Heartburst** and **Hemodominate**, both Sangromancer spells. No other class's spells carry this restriction, including comparably powerful Master-tier spells:

- **Soul Storm** [SR, HW] (Master): 6 Spectral AoE + Frightened + obscured — no usage limit
- **Astral Shackle** [SR, HW] (Master): Paralyzed 3 rounds + forced realm banishment — no usage limit
- **Annihilation Pulse** [HW] (Master): 8 Entropic AoE to all nearby — no usage limit
- **Mind Rupture** [HW] (Master): Madness until cured — no usage limit

The "once per long rest" restriction on Sangromancer spells implies intentional balance gating on the most powerful blood effects, but the same logic is not applied to equivalently powerful effects from other classes. This is either an inconsistency (other classes should also have usage-limited high-end spells) or it's intentional asymmetry that should be documented as such.

**Recommended Fix:**
Audit Master-tier spells across all classes and apply "once per long rest" to any instant-death, permanent-effect, or scene-ending abilities. Candidates: **Heartburst** (already has it), **Hemodominate** (already has it), **Blood Oblivion** (permanent memory erasure), **Mind Rupture** (madness until cured), potentially **Wound Reversal** (HP swap — could be game-breaking in the right conditions).

---

### Issue 40 — Blood Puppet + Hemodominate: No Ruling on Simultaneous Active Control

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 195 (Blood Puppet) and 304 (Hemodominate)

**Problem:**
**Blood Puppet** (Adept) controls a Bleeding creature's next turn only. **Hemodominate** (Master) controls a Bleeding creature for 1 minute. A Sangromancer could cast Hemodominate to establish 1-minute control, then cast Blood Puppet on the same target (it's still Bleeding). Blood Puppet says the caster "controls the target's movement, action, and bonus action on its next turn." Hemodominate says "full control 1 min."

If both are active simultaneously on the same creature, which takes precedence? Does Blood Puppet's specific single-turn control interrupt or reinforce Hemodominate's sustained control? Does casting Blood Puppet while Hemodominate is active waste the BP cost (since you already have control)?

**Recommended Fix:**
Add a note to Hemodominate:
> *"While a target is under Hemodominate's control, casting Blood Puppet on the same target has no additional effect — the level of control granted by Hemodominate already encompasses Blood Puppet's scope."*

---

### Issue 41 — Soul Lock vs. Temporary HP: Interaction Unresolved

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 150 (Minor Bloodshield) and 228 (Soul Lock)

**Problem:**
**Soul Lock** prevents the target from "regaining HP." **Minor Bloodshield** grants temporary HP ("the target gains temporary HP equal to 3 + your Soul, applied before the triggering damage if cast as a Reaction").

Temporary HP is mechanically distinct from HP — it's a buffer that absorbs damage before HP is reduced. In most systems, temporary HP is not the same as "regaining HP." If that distinction holds here, Minor Bloodshield can still be applied to a Soul Locked target, providing protection despite the lock.

However, this may not be the intended ruling, and no guidance exists in Ch. 5 or the Glossary to confirm either way.

**Recommended Fix:**
Add a clarification to Soul Lock:
> *"...the target cannot regain HP and cannot be returned to life until the end of its next turn. Temporary HP granted by external effects **does not count** as regaining HP and can still be applied while Soul Lock is active."*

---

### Issue 42 — Reaver Unleashed: "60-ft Cone/30-ft Burst" Area Is Ambiguous

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 329 (Reaver Unleashed, Master Forbidden)

**Problem:**
Reaver Unleashed reads: *"60-ft cone/30-ft burst; 7 Spectral damage (DR 3 Soul save halves) + Reaver boost 1 min."*

The "/" between "60-ft cone" and "30-ft burst" could mean:
1. The caster **chooses** between a 60-ft cone and a 30-ft radius burst when casting
2. The spell **always** creates both — a 60-ft cone AND a 30-ft burst simultaneously
3. "Cone/burst" is a single descriptor for one oddly-shaped area

Option 2 would make this the largest-area Master spell in the compendium by far. Option 1 is likely the intent but needs to be stated explicitly. The "Reaver boost 1 min" undefined issue (Issue 17) compounds the problem.

**Recommended Fix:**
Clarify the area as a choice:
> *"Choose one area when you cast: a **60-foot cone** or a **30-foot radius burst** centered on yourself..."*

---

---

## Pass 7 — Spellcasting & Magic (Ch. 5) Glyph Triggers, AoE Rules, Resource Definitions, and Power Outliers

Issues identified during sixth pass — checking glyph trigger consistency, AoE friendly fire, undefined resource terms, permanent costs, and spell power outliers.

---

### Issue 43 — Multiple Glyphs Have No Trigger Condition

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 238, 240, 242, 291, 292, 295 and others

**Problem:**
Initiate and Adept glyphs consistently specify their triggers: "triggers on approach," "triggers on entry," "triggers on touch," "triggers on spellcast," "triggers on sound/entry," "triggers on large creature." This pattern is clean and usable.

Several Expert and Master glyphs simply say **"triggers"** with no condition — a GM must invent the trigger:

| Spell | Line | Trigger Listed |
|---|---|---|
| **Glyph of Drowning** | 238 | "Touch near water; **triggers**" — no condition |
| **Glyph of Gravity** | 240 | "Touch; **triggers**" — no condition |
| **Glyph of Ruin** | 242 | "Touch; **triggers**" — no condition |
| **Glyph of Obliteration** | 291 | "Touch; **triggers**" — no condition |
| **Glyph of Time Sever** | 292 | "Touch; **triggers**" — no condition |
| **Glyph Vortex** | 295 | "Touch; **triggers**" — no condition |
| **Glyph of Echo Memory** | 239 | "10 min; touch; records 2 rounds of sensory data **on trigger**" — no trigger specified |

Additionally, two glyphs have vague triggers that need definition:
- **Glyph of Judgment** (line 290): "triggers on **aggression**" — what constitutes aggression? Attacking? Drawing a weapon? Any hostile action?
- **Glyph of Unmaking** (line 293): "**command trigger**" — what is a command trigger? How does the caster issue the command? Range? Action cost?

**Recommended Fix:**
Define a trigger condition for each affected glyph, following the established pattern. Suggested triggers based on spell effect:
- Glyph of Gravity / Drowning / Ruin / Obliteration / Time Sever: **"triggers on entry"** (a creature enters the glyph's square)
- Glyph Vortex: **"triggers on approach"** (within 10 ft)
- Glyph of Echo Memory: **"triggers on any creature passing through the inscribed area"**
- Glyph of Judgment: define "aggression" as "any attack roll, spell attack, or hostile ability targeting a creature within 10 ft of the glyph"
- Glyph of Unmaking: define "command trigger" as "the caster speaks a chosen command word within 60 ft as a Free Action"

---

### Issue 44 — AoE Spells Inconsistently Specify Whether Allies Are Affected

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Multiple AoE spells throughout §5.10

**Problem:**
Some AoE spells explicitly state who they affect; most do not. Without a clear convention, a GM must rule whether each AoE spell hits allies. The inconsistency is evident across spells at every tier:

**Spells that DO specify:**
- **Dissonant Pulse**: "Creatures **of your choice** in the area" ✅
- **Pillar Ward**: "**allies** in the ward" ✅
- **Judgment Sigil**: "**allies** in the area / **enemies** in the area" ✅
- **Annihilation Pulse**: "**all other creatures** in a 20-ft radius" ✅ (explicitly hits allies)
- **Invocation of Chains**: Does NOT specify despite being a 20-ft radius ❌

**Spells that do NOT specify (and affect allies in ambiguous ways):**

| Spell | Area | Problem |
|---|---|---|
| **Blood Cyclone** [SG] | Self; 20-ft radius | Does it hit your allied Sangromancer 10 ft away? |
| **Hemorrhage Halo** [SG] | Self; 10-ft radius | Deals Spectral damage — hits allies? |
| **Crimson Surge** [SG] | Self; 15-ft cone | Bludgeoning cone — does it knock allies Prone? |
| **Viscera Torrent** [SG] | Self; 30-ft cone | Poisons everyone in the cone? |
| **Crimson Reaping** [SG] | Self; 15-ft radius | Executes creatures below 25% HP — could kill low-HP allies |
| **Starving Veil** [SR, SM, HW] | Self; 15-ft aura | Deals Spectral damage per turn to "creatures" — including allies |
| **Descent of Teeth** [SM, HW] | 10-ft radius in 60 ft | Hits all creatures in radius? |
| **Dirge of Ruin** [WB, HW] | 60-ft radius | -1 die to actions — does this affect allies? |
| **Cacophonic Flare** [HW] | Self; 20-ft radius | Stuns/Blinds everyone nearby — including allies? |

**Recommended Fix:**
Establish a universal rule in §5.4 and apply explicit targeting language to each affected spell:
> *"AoE spells that do not specify targeting affect **all creatures** in the area, including allies, unless the spell text says 'creatures of your choice,' 'enemies,' or 'allies.' If a spell says 'creatures' without qualification, it hits everything."*

Then review each unspecified spell and add "creatures of your choice" where clearly intentional (e.g., Starving Veil probably isn't meant to drain allied HP) or "all creatures" where it should be dangerous to allies (e.g., Annihilation Pulse already states this).

---

### Issue 45 — Resource Regeneration Terms Are Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Section 5.7 (Resource Pools); Section 5.3

**Problem:**
Both resource pools use undefined terms for regeneration:

**Soul Energy (SE):** *"Regain via rest, soul shards, or channeling."*
- **Soul shards**: Not defined anywhere in Ch. 5, Ch. 7 (Equipment), or the Glossary. How are they obtained? How much SE do they restore? Can they be crafted?
- **Channeling**: Not defined. What is channeling? Is it a skill? An action? Is it the Energy Foci attunement from Ch. 11?

**Blood Points (BP):** *"Regain via feeding or relics."* (§5.3) / *"Regain via feeding or relics."* (§5.7)
- **Feeding**: How much BP does feeding restore? How long does it take? Can you feed in combat? On a dead creature vs. a living one? Does feeding work differently for Vampires vs. Sangromancers?
- **Relics**: Which relics restore BP? Where are they defined? Ch. 7 (Equipment) presumably covers this, but §5.7 gives no cross-reference.

A player running a Sangromancer has no way to know how to restore their only resource without digging through other chapters with no guidance.

**Recommended Fix:**
Expand §5.7 with basic regeneration definitions or cross-references:
> *"**SE Regeneration:** SE restores fully after a **long rest**. **Soul shards** (found as treasure or crafted by Glyphwrights) restore 1–2 SE as an Action (see Ch. 7 §7.X). **Channeling** at an Energy Foci (Ch. 11 §11.3) restores 1 SE after a successful attunement check during a short rest.*
> *"**BP Regeneration:** BP restores fully after a **long rest** during which the character can feed. **Feeding** on a living or recently dead (within 1 hour) creature restores BP equal to half that creature's TV, rounded up, as an Action. Feeding on a willing creature restores 1 BP and takes 1 minute. **Relics** that restore BP are listed in Ch. 7 §7.X."*

---

### Issue 46 — Permanent Max HP Reduction Has No Recovery Mechanism

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 301 (Blood Resurrection) and 302 (Crimson Godseed)

**Problem:**
Two Master Blood spells impose **permanent maximum HP reduction** as a casting cost:
- **Blood Resurrection**: *"5 BP (-1 max HP)"* — permanent
- **Crimson Godseed**: *"5 BP (-3 max HP)"* — permanent

No rule anywhere in Ch. 5, Ch. 7, Ch. 8, or the Glossary defines how permanent max HP loss can be recovered. A Sangromancer who uses Blood Resurrection loses 1 max HP forever with no recourse — or does the "permanent" language just mean until a specific recovery is found?

If max HP reduction is truly permanent with no recovery, these spells have a character-degrading cost that compounds over time — a Sangromancer who revives three allies loses 3 max HP permanently. Over a campaign, this could be crippling.

Additionally: does the **Glyph of Ruin** (line 242) "-5 max HP for 1 min" interact correctly with these permanent reductions? If a character is already at reduced max HP, can the temporary reduction drop them below their current HP and kill them?

**Recommended Fix:**
Define max HP recovery explicitly. Suggested approach:
> *"Permanent maximum HP reduction can only be restored by a **Soulforge Resurrection** ritual performed on the affected character (restoring all lost max HP), or by a **long rest** at a location with healing properties designated by the GM (restoring 1 lost max HP). Temporary max HP reduction (like Glyph of Ruin) cannot reduce a character's current HP below 1 — if a creature's max HP would drop below their current HP, their current HP drops to match the new maximum."*

---

### Issue 47 — Pulse Spike: Negligible Damage Floor Makes It a Near-Useless Resource Spend

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 151 (Pulse Spike, Initiate Blood)

**Problem:**
Pulse Spike reads: *"Cost: 1 BP. 30 ft; spell attack, 1 Spectral damage + DR 2 Blood save or Disadvantage on the target's next attack or check."*

Base damage of **1 Spectral** means even at level 20 (with +4 scaling) it deals 5 damage. For 1 BP, a resource that cannot be recovered in combat without feeding, this deals the same as a basic unarmed strike from most characters. The Disadvantage rider is the only meaningful effect, and it only applies to one roll.

Compare to **Sanguine Dart** (same tier, same cost): 3 Physical (Piercing) damage with Advantage against Bleeding targets — 3x the base damage with no Disadvantage rider needed. Pulse Spike is strictly weaker in damage and its rider effect is conditional and single-use.

**Recommended Fix:**
Increase the base damage or strengthen the rider to make it a meaningful choice:
> *"1 BP. 30 ft; spell attack, **3** Spectral damage + DR 2 Blood save or Disadvantage on the target's next **two** attack rolls or checks."*

---

### Issue 48 — AoE Scaling Asymmetry Creates Growing Power Gap Between Burst and Aura Builds

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Section 5.4 (Spell Damage Scaling)

**Problem:**
§5.4 correctly states that "ongoing hazards, persistent auras, summons, and long-form rituals do not gain this automatic scaling." However, this creates a compounding power gap as characters level up:

| Spell | Type | Damage at Level 1 | Damage at Level 20 |
|---|---|---|---|
| **Glyph of Flame** (Initiate) | Instantaneous | 3 Fire | 7 Fire (+4 scaling) |
| **Starving Veil** (Expert) | Ongoing aura | 2 Spectral/turn | 2 Spectral/turn (no scaling) |
| **Hemorrhage Halo** (Adept) | AoE trigger | 2 Spectral | 2 Spectral (no scaling) |
| **Blood Cyclone** (Expert) | Instantaneous | 5 Slashing | 9 Slashing (+4 scaling) |

By level 20, an instantaneous Expert spell does +4 more damage than its written value, while an ongoing Expert aura does the same damage as it did at level 11. Concentration/aura builds are functionally weaker at high levels than burst builds, despite typically requiring more resource investment (Concentration locks out other spells, auras are canceled on failed saves).

This may be intentional — preventing endless-aura builds from becoming too powerful — but it is never acknowledged as a design tradeoff. Players investing in aura-based Sangromancer or Soul Reaver builds will discover mid-campaign that their strategy plateaus while opponents scale up.

**Recommended Fix:**
Either acknowledge this as intentional design (add a note to §5.4: *"This asymmetry is intentional — ongoing auras are designed for tactical setup, not sustained damage scaling"*), or add a partial scaling rule:
> *"Ongoing auras and persistent hazards gain **+1 damage at levels 10 and 20** only (maximum +2), representing the caster's growing mastery but preventing runaway sustained-damage builds."*

---

### Issue 49 — "Feeding or Rituals" vs. "Feeding or Relics": Inconsistent BP Regeneration Text

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Lines 67 and 107

**Problem:**
BP regeneration is described in two places with different text:

- **§5.3** (line 67): *"Blood Points (BP): For Blood spells; costs 1–3+ based on tier. Regain via **feeding or rituals**."*
- **§5.7** (line 107): *"Blood Points (BP): Maximum = 4 + Shadow + (Level / 2). Start combat at maximum (if not starved); regain via **feeding or relics**."*

One says "rituals," the other says "relics." These are different things. "Rituals" implies performing blood rites (potentially the Ritual Spells category), while "relics" implies equipment items (Ch. 7). A player reading both sections gets contradictory information about how to recover their only resource.

**Recommended Fix:**
Standardize both entries and resolve which is correct — or if both are valid, list both in both locations:
> *"Regain via **feeding**, **blood relics** (see Ch. 7), or **blood rituals** performed during a short or long rest."*

---

---

## Pass 8 — Spellcasting & Magic (Ch. 5) Control Violations, Save Ambiguity, Coverage Gaps, and Tuning

Issues identified during seventh pass — checking for §5.4 violations missed in Pass 3, save mechanics clarity, class architecture gaps, undertuned Master-tier DRs, and unrunnable summons not caught in Issue 17.

---

### Issue 50 — Hemodominate: Full 1-Minute Control With No Concentration and No Repeat Save

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 304 (Hemodominate, Master Blood)

**Problem:**
Hemodominate reads: *"30 ft Bleeding; DR 3 Will or full control 1 min (once/long rest)."*

This is a §5.4 Combat Control Duration violation identical in structure to the three spells caught in Issue 9. §5.4 requires that a combat spell denying actions either lasts ≤3 rounds, requires Concentration, or allows an end-of-turn repeat save. Hemodominate:
- Denies all agency ("full control") for **1 full minute**
- Has **no Concentration requirement** stated
- Has **no repeat save** — the "once/long rest" restriction limits the caster, not the target's exit options

A target who fails the initial DR 3 Will save is fully controlled for the entire minute with no recourse. Issue 9 caught Glyph of Chains and Viscera Torrent on the same basis; Hemodominate is the most severe case — full control versus merely Restrained or Poisoned — and was missed.

The "once/long rest" limit (Issue 39) limits abuse via repetition, but it does not excuse the missing escape mechanism for the controlled target.

**Recommended Fix:**
Add a repeat save clause:
> *"30 ft Bleeding; DR 3 Will or full control for up to 1 minute. The target may repeat the Will save at the end of each of its turns, ending the control on a success. While you maintain this control, you cannot cast other Concentration spells. Once per long rest."*

---

### Issue 51 — Soul Fracture: 1-Minute Spellcasting Denial Has No Repeat Save; "Increased SE Costs" Is Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 282 (Soul Fracture, Expert Forbidden)

**Problem:**
Soul Fracture reads: *"30 feet; DR 3 Soul or -2 Will/Soul checks + increased SE costs 1 minute; harder resurrection if killed."*

Two separate problems:

**1. §5.4 violation:** The spell imposes a significant action-denial effect (increased SE costs effectively denies access to higher-tier spells; a caster who cannot afford their spells cannot take meaningful actions) for 1 full minute with no Concentration requirement and no repeat save. A caster relying on 3+ SE spells could be functionally disabled for an entire minute on a single failed DR 3 Soul save.

**2. "Increased SE costs" is undefined:** By how much? +1 SE per spell? +1 SE per tier? Double costs? The GM must invent this value, and two GMs will rule it completely differently. A Hylden Warlock spending 4 SE normally on Cacophonic Flare needs to know if this effect means they spend 5, or 6, or more.

**Recommended Fix:**
Define the SE cost increase and add a repeat save:
> *"30 feet; DR 3 Soul save or for up to 1 minute: all SE costs the target pays are increased by 1, and it suffers -2 dice on Will and Soul checks. The target may repeat the Soul save at the end of each of its turns, ending the effect on a success. If the target is killed while this spell is active, resurrection requires an additional DR 1 Soul ritual beyond the normal cost."*

---

### Issue 52 — Wound Reversal: Save Target, Save Subject, and Max HP Overflow Are All Undefined

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 309 (Wound Reversal, Master Blood)

**Problem:**
Wound Reversal reads: *"30 ft; swap HP totals between 2 targets (DR 3 Blood)."*

Three unresolved questions:

**1. Who saves?** The spell does not say. Options: both targets save (either can block the swap), only the target receiving lower HP saves (protecting them from harm), or only the target receiving higher HP saves (odd). A player can legitimately argue any of these.

**2. Unilateral lethality:** A Sangromancer at 50 HP could swap totals with a near-dead ally at 3 HP. The ally goes from 3 to 50 HP; the Sangromancer drops from 50 to 3 HP. Intentional self-sacrifice? Possibly. But it could also be used offensively — swap a healthy enemy (80 HP) with a dying ally (4 HP), dropping the enemy from 80 to 4 HP without a damage roll or attack. This is effectively a save-or-die on high-HP targets unless the save is robust.

**3. Max HP overflow:** If one target has max HP 40 and the other has max HP 100, and you swap HP totals, what happens when the 40-max-HP target would receive 80 HP? Does it cap at 40? Does it receive 40 and the remainder is wasted? Does it temporarily exceed maximum HP?

**Recommended Fix:**
Rewrite with explicit targeting and HP rules:
> *"30 ft; choose two creatures you can see, at least one of which must be willing. Each unwilling creature must make a DR 3 Blood save; on a success, it is unaffected by the swap. On a failure, the HP totals of the two creatures are exchanged. HP gained this way cannot exceed a creature's maximum HP — excess is lost. This swap is not considered healing and cannot be blocked by effects that prevent HP gain."*

---

### Issue 53 — No General Dispel Mechanic: Ongoing Non-Glyph Effects Cannot Be Removed

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — §5.6 (Reactions) and §5.10 generally

**Problem:**
The system has several ways to disrupt magic:
- **Counterspell** (§5.6): Interrupts a spell as it's being cast
- **Dissonant Pulse**: Ends Concentration on a failed save
- **Glyph Disruptor / Shatter Sigil**: Dispel placed glyphs
- **Glyph of Reflection**: Reflects incoming spells

None of these can remove an ongoing, non-glyph, non-Concentration spell effect that has already been applied to a target. Examples:
- A creature under **Hemodominate** (full control 1 min, no Concentration) has no magical recourse
- A creature with permanent memory loss from **Blood Oblivion** cannot be restored by any spell in the compendium
- A creature cursed by **Fatebind Curse** (Issue 17) has no listed removal mechanic
- A creature Frightened by **Nightmare Seed** for 10 minutes cannot have that condition dispelled

In a system where permanent and long-duration effects exist, the absence of any dispel analog creates a gameplay dead-end: once a powerful curse or control effect lands, no in-system magic can address it.

**Recommended Fix:**
Add a **Dispel Magic** entry to §5.6, or add a dedicated Adept+ spell to the Warden of Balance / Glyphwright list:
> *"**Unravel** [GW, WB, HW] (Adept, 2 SE): 30 ft; choose one ongoing spell effect (not Glyph, Concentration, or Instantaneous) currently affecting a target you can see. Make an opposed check: your Soul + Glyphcasting or Soul + Forbidden Knowledge vs. the original spell's DR. On a success, the effect ends. Master-tier effects are immune to Unravel unless cast at Master tier."*

---

### Issue 54 — Dirge of Ruin: DR 2 Save on a Master Spell Is Four Tiers Below the §5.2 Formula

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 315 (Dirge of Ruin, Master Ritual)

**Problem:**
Dirge of Ruin reads: *"10 min; 60-ft radius; 3 Spectral damage + -1 die actions (DR 2 Will save + Concentration to maintain)."*

Per §5.2, the baseline DR for a Master-tier spell is **DR 4** (plus attribute modifier). Dirge of Ruin uses **DR 2** — the Adept-tier baseline. A Master spell in a 60-foot radius that imposes -1 die to all actions on every creature in that area should not be trivially resisted by a DR 2 save.

The practical impact: at DR 2 Will, most Expert and Master NPCs who invest even minimally in Will have roughly even odds of shrugging this off. The -1 die debuff is significant on paper; the DR 2 save ensures it rarely sticks against relevant targets.

This appears to be a typo or copy error. The Concentration requirement and 10-minute cast time suggest this is meant to be a powerful-but-costly ritual, not an easily-resisted one.

**Recommended Fix:**
Update the save DR to match the tier:
> *"10 min; 60-ft radius; 3 Spectral damage + -1 die to all actions (**DR 4** Will save + Concentration to maintain)."*

---

### Issue 55 — Sanguine Swarm: Summoned Swarm Has No Stat Block

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 306 (Sanguine Swarm, Master Blood)

**Problem:**
Sanguine Swarm reads: *"Cost: 4 BP (-5 HP). 30 ft; summon swarm (5 Spectral damage + Frightened) for concentration 1 min."*

The swarm has no defined:
- HP or durability (can it be attacked and destroyed?)
- Movement speed and type
- Size or area it occupies
- Whether the swarm acts on the caster's turn or separately
- Whether it makes attack rolls or auto-damages on a save
- What the Frightened effect's DR and save type is

Issue 17 catalogues unrunnable spells, but Sanguine Swarm was not on that list. It should be. The swarm is a summoned creature, not a simple area effect — it needs at minimum a movement speed, a note on whether it can be destroyed, and clarification on how it deals damage (spell attack vs. save).

**Recommended Fix:**
Add to the Issue 17 expansion pass list. Minimal working definition example:
> *"30 ft; summon a **Sanguine Swarm** in a space within 30 ft. The swarm occupies a 10-foot cube, has 10 HP, a movement speed of 20 ft, and acts on your initiative. Each creature that starts its turn in the swarm or enters it must make a DR 4 Evasion save, taking 5 Spectral damage on a failure (half on success) and becoming Frightened of you until the end of its next turn on a failure. The swarm lasts while you maintain Concentration, up to 1 minute."*

---

### Issue 56 — Memory Script: Per-Word SE Cost Creates Undefined Pricing Edge Cases

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 160 (Memory Script, Initiate Ritual)

**Problem:**
Memory Script reads: *"Cost: 1 SE/50 words. 1 minute/25 words; touch; invisible script revealed by keyword."*

This is the only spell in the compendium with a per-unit resource cost. It creates several unresolved edge cases:

1. **Partial increments:** Does 51 words cost 1 SE or 2 SE? Is each 50-word block a separate SE cost, or do partial blocks round up?
2. **Maximum length:** There is no stated maximum. Could a Glyphwright with 8 SE inscribe a 400-word document? Is that the intent?
3. **Casting time:** "1 minute/25 words" — is this 1 minute per 25 words? So a 100-word script takes 4 minutes? There is no cap.
4. **Retroactive limit:** If a player writes more words than they paid for, does the excess simply not appear, or does the spell fail entirely?

This per-word pricing model is unique in the system and doesn't connect to any other mechanic. It likely exists to prevent the spell from being used as an unlimited document-storage system, but the rules as written don't achieve that cleanly.

**Recommended Fix:**
Standardize to a flat cost with a defined word limit:
> *"Cost: 1 SE. 1 minute; touch; inscribe invisible script of up to 100 words onto a surface or object you touch. The script is revealed to a viewer who speaks the chosen keyword within 1 foot of the surface. The script lasts until your next long rest unless you spend 1 additional SE when casting to make it permanent. For a permanent script, the casting time is 10 minutes."*

---

### Issue 57 — Crimson Godseed: Attribute Boost Duration Is Unstated

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 302 (Crimson Godseed, Master Blood)

**Problem:**
Crimson Godseed reads: *"Cost: 5 BP (-3 max HP). 1 hr; vampiric transformation or boost (+1 attribute/spell)."*

The "+1 attribute" component has no stated duration. Every other attribute-modifying effect in Ch. 5 specifies its duration: Pillar Resonance (1 hr), Litany of Focus (1 hr), Communion of Shadows (dim light). Crimson Godseed does not say whether the attribute increase lasts 1 hour, 1 day, or permanently.

If it is permanent (which the -3 max HP permanent cost suggests — you sacrifice max HP forever for a permanent benefit), then this spell grants a permanent +1 to any attribute for 5 BP and -3 max HP. Compared to a Lineage Paragon (Level 10 or 20) that grants +1 attribute under strict level-gating, a freely-castable permanent attribute boost is an extraordinary outlier.

If it is not permanent, the duration needs to be stated. The "+1 spell" text is also undefined (Issue 17/Issue 23 — does this mean +1 spell known?), compounding the ambiguity.

**Recommended Fix:**
Define the duration and clarify the effect:
> *"Cost: 5 BP (-3 permanent max HP). 1 hr casting; touch; choose one effect — **Vampiric Transformation** (the subject gains the physical traits of one Vampire lineage subtype for 24 hours, decided by the caster), or **Blood Ascension** (+1 to one physical attribute — Blood, Fury, or Shadow — for **24 hours**)."*

Note: if the intent is truly permanent, this needs to be acknowledged as a deliberate design choice and capped at one use per character.

---

### Issue 58 — Shadowmancer Has Zero Glyph Spell Access

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — §5.10 (all Glyph tiers)

**Problem:**
Scanning every Glyph spell across all four tiers, the Shadowmancer [SM] tag does not appear on a single entry. Not one Initiate, Adept, Expert, or Master Glyph spell is accessible to the Shadowmancer.

By contrast:
- **Glyphwright** tags almost all Glyph spells (expected)
- **Warden of Balance** tags a significant subset of Glyphs
- **Hylden Warlock** tags several Glyph spells
- **Soul Reaver** tags two Glyph spells (Glyph of Anchoring, Glyph of Thorns)

The Shadowmancer's identity is shadow manipulation, illusion-adjacent effects, and spectral stealth — which thematically overlaps with trap-like glyphs (Glyph of Silence, Glyph of Displacement) or illusion-supporting glyphs. Whether this absence is intentional is never stated in Ch. 3 or Ch. 5. If Shadowmancers truly have no glyph access by design, that should be documented as a class pillar ("Shadowmancers do not inscribe — they work through ephemeral manipulation"). If it is an oversight, several Adept glyphs are natural candidates: Glyph of Silence, Glyph of Displacement, Glyph of Entropy.

**Recommended Fix:**
Declare the absence intentional in the Shadowmancer class entry:
> *"Shadowmancers do not inscribe. Their power is transient — cast and dissolved. They gain no access to Glyph spells."*

Or, if intended to have some access, add [SM] to: Glyph of Silence, Glyph of Displacement (with save fix per Issue 15), and Glyph of Echoes at minimum.

---

### Issue 59 — Last Rite of Balance: "DR 4–5" Provides No Rule to Determine Which Applies

**Status:** Completed

**Location:** `player's_handbook/05_Spellcasting-and-Magic.md` — Line 318 (Last Rite of Balance, Master Ritual)

**Problem:**
Last Rite of Balance reads: *"Cost: 5 SE (-2 Exhaustion stacks). 1 hr; cleanse 1-mile area of corruption (DR 4–5 Soul + Ritualism)."*

The variable DR "4–5" has no determination rule. Is it:
- DR 4 for minor corruption, DR 5 for severe corruption (by what measure)?
- DR 4 if the area is under 1 mile, DR 5 for a full 1-mile radius?
- At GM discretion?
- A typo for a specific value?

The ritual already has a meaningful cost (-2 Exhaustion stacks is significant — at 3 stacks the caster becomes Incapacitated). Adding an uncertain DR on top of that investment means a player cannot assess success probability before committing. Two GMs will consistently rule different things.

**Recommended Fix:**
Define the DR determination:
> *"Cost: 5 SE (and the caster immediately gains -2 Exhaustion stacks, which cannot be reduced). 1 hr; cleanse a 1-mile area of Corruption. Make a Soul + Ritualism check vs. DR 4 (lightly corrupted area or Corruption Level 1–5) or DR 5 (heavily corrupted area or Corruption Level 6+). On a success, remove 1d3 Corruption Levels from the area and purify mundane Corruption effects within it. On a failure, the Exhaustion cost is still paid and the area is cleansed of only superficial Corruption."*

---

## Future Passes

Additional mechanics review passes will be added here as issues are identified.

---

## Recommendations — Prioritized Action Plan

All 59 issues organized by action type and recommended execution order.

---

### Tier 1 — Quick Text Fixes
*Clear correct answer, single targeted edit, no design debate. All 22 can be completed in one focused session.*

| # | Action | File |
|---|---|---|
| **1** | Update §11.1 return threshold to `50% HP`, cross-reference §11.5.2 | Ch. 11 |
| **4** | Update 5 spell references from `§11.1` → correct `§11.5.x` subsections | Ch. 5 |
| **5** | Add BP suspension callout paragraph to §5.7 (factual cross-reference) | Ch. 5 |
| **6** | Replace `"Ethereal"` with `"Incorporeal"` in Lantern Rite | Ch. 5 |
| **8** | Add `*(crosses realms)*` tag to Soul Storm base spell | Ch. 5 |
| **10** | Add one-sentence anti-ping-pong clause to Soulweave | Ch. 5 |
| **13** | Rewrite `"(1/min limit)"` in Hemostatic Pulse to explicit target restriction | Ch. 5 |
| **14** | Remove or differentiate Blood Mark's redundant touch clause | Ch. 5 |
| **15** | Change Glyph of Displacement save from `Will` → `Evasion` | Ch. 5 |
| **23** | Standardize all `"+2 bonus"` to `"+2 dice"` across 5 spells | Ch. 5 |
| **27** | Clarify Soulforge Resurrection `"5 SE/BP"` as `OR`, class-based | Ch. 5 |
| **30** | Rewrite Cacophonic Flare condition list with explicit sequencing | Ch. 5 |
| **32** | Add `"1 Exhaustion stack"` to Sanguine Eclipse | Ch. 5 |
| **33** | Rewrite Vital Hook `"Bonus pull"` into a proper tether mechanic | Ch. 5 |
| **34** | Add DR floor note to §5.10 preamble (`"listed DR is a floor, not a cap"`) | Ch. 5 |
| **40** | Add note to Hemodominate: Blood Puppet has no effect while Hemodominate is active | Ch. 5 |
| **41** | Add clarification to Soul Lock: temp HP is not "regaining HP" and still applies | Ch. 5 |
| **42** | Rewrite Reaver Unleashed `"60-ft cone/30-ft burst"` as explicit choice | Ch. 5 |
| **47** | Increase Pulse Spike base damage from `1` to `3` Spectral | Ch. 5 |
| **49** | Standardize BP regen text — `"rituals"` vs `"relics"` between §5.3 and §5.7 | Ch. 5 |
| **50** | Add end-of-turn repeat save to Hemodominate; add Concentration requirement | Ch. 5 |
| **54** | Change Dirge of Ruin save from `DR 2` → `DR 4` | Ch. 5 |
| **56** | Replace per-word Memory Script cost with flat `1 SE / 100 words` | Ch. 5 |
| **58** | Add design note to Shadowmancer that it has no glyph access (or add 2–3 glyph tags) | Ch. 5 / Ch. 3 |

---

### Tier 2 — Design Decisions Required
*A call needs to be made before the text can be written. Options are listed for each.*

#### Spectral Realm

**Issue 2** — Native Spectral Exception scope
Confirm the exception covers MM monsters only, not PC lineages. Recommended fix text is ready — just needs sign-off.

**Issue 3** — Revenant Soul Bleed rate
Set to `1 HP per 3 rounds` (matching Wraith) or a different rate. Affects Ch. 11 §11.5.1 and Ch. 2 §2.6.

**Issue 7** — Astral Shackle forced banishment: apply or waive §11.5.5 shock damage?
- **Option A (recommended):** Controlled banishment — no shock. Master-tier precision should not also randomly hurt the target for 1d6.
- **Option B:** Shock still applies — the dimensional violence is part of the punishment.

#### Internal Consistency

**Issue 9** — Glyph of Chains, Glyph of Ruin, Viscera Torrent: add repeat saves
Recommended fix text is ready for all three. **Effectively Tier 1 once confirmed.**

**Issue 11** — Ceremony of Sorrow: add DR check or keep automatic?
- **Option A (recommended):** DR 2 Soul + Ritualism check.
- **Option B:** Keep automatic but reduce to narrative only — no mechanical Corruption removal.

**Issue 12** — Spirit Echo: add detection check or keep automatic?
- **Option A (recommended):** DR 1 Soul + Observation.
- **Option B:** Keep automatic but limit output (number only, no emotion).

**Issue 16** — Glyph of Anchoring: confirm it blocks Soul Portal crossings from Spectral side
Clarifying note is ready. Needs sign-off that the interaction is intentional.

**Issue 18** — Define "Limited Actions" condition used in Glyph of Time Sever and Chrono Collapse
Recommended definition: *one Action or one Bonus Action (not both), no Reactions.* Applies to both spells once decided.

**Issue 19** — Replace "risky roll" in Omen Tether
Recommended replacement: *"next attack roll, spell attack, or skill check."* Needs sign-off.

**Issue 21** — Soul Flicker "no offensive actions": caster restriction or attacker restriction?
- **Option A (recommended):** Caster restriction — you become evasive but cannot attack. Creates a meaningful tradeoff.
- **Option B:** Attacker restriction — unusual and probably not the intent.

#### Description Quality

**Issue 17** — 17 unrunnable spells *(see Tier 3 for full plan)*
Prioritize by table-readiness need:
- **High (combat-relevant):** Vital Dominion, Reaver Unleashed, Sanctify Ground, Fatebind Curse, Dark Reflection, Warding Circle
- **Medium (ritual/narrative):** Bloodrite Brand, Beckon of the Deep, Curse of the Nine Moons, Ritual of Eclipse, Throne of Veins
- **Lower (utility/flavor):** Echo Word, Chrono-Ward Ritual, Glyph of Echoes, Glyph of Entropy, Eternal Sigil

**Issue 20** — Eyes Beyond: what does "see invisible" cover?
- **Option A (recommended):** Invisible creatures and objects. Not Incorporeal, not fully Spectral entities. One sentence.
- **Option B:** Invisible creatures only.

**Issue 22** — Binding of the Starborn: replace "celestial entity" with Nosgoth-appropriate lore
Replace with **Bound Guardian** (pre-Vampire protective spirit). Flavor rewrite, no mechanical change. Recommended text is in the issue.

**Issue 24** — Corruption Crown: define "dread aura"
- **Option A (recommended):** 10-ft radius, creatures must save DR 2 Will or have Disadvantage on attacks against you.
- **Option B:** Frightened on a failed save — but this overlaps with the Charmed rider already on the spell.

#### Undefined Terms and Resource Costs

**Issue 25** — Counterspell: define cost, access, and availability
- **Option A (recommended):** Universal (any caster), 1 SE cost, 60-ft range.
- **Option B:** Class-restricted — only designated classes can Counterspell.
This affects every caster in the game. The recommended text is in the issue.

**Issue 26** — Rotmind Rift Corruption cap
- **Option A (recommended):** Cap at 3 Corruption Levels total per casting. Still brutal, not campaign-ending.
- **Option B:** Cap at 5. Higher risk, still finite.

**Issue 28** — The God's Rebuttal: define "divine" trigger
Recommended: Radiant damage OR Warden of Balance spells OR explicitly holy effects. One sentence addition.

**Issue 29** — Mind Spike: define "paranoia"
Recommended definition provided in issue. Needs sign-off before adding to the spell.

#### Interactions and Balance

**Issue 35** — Sangromancer non-functional in Spectral Realm
- **Option A (recommended for immediate fix):** Add a sidebar to Ch. 3 and §5.7 explicitly acknowledging SG is a Material-only caster.
- **Option B:** Add one SE-cost Adept spell as a Spectral emergency fallback.

**Issue 36** — Eyes Beyond vs. magical Darkness: does it pierce it?
- **Option A (recommended):** Yes — Eyes Beyond pierces magical darkness. States the SM/HW combo as a known valid tactic.
- **Option B:** No — add explicit language that it does not apply to magical darkness.

**Issue 37** — Realmshift overlay vs. Glyph of Anchoring
Recommended ruling: an overlay is not a creature shifting, so Anchoring does not trigger. Fix text is ready.

**Issue 38** — Nightmare Seed 10-minute Frightened
- **Option A (recommended):** Add end-of-turn repeat save. Brings it in line with Adept Dread Chain.
- **Option B:** Reduce duration to 1 minute flat.

**Issue 39** — Usage limits only on Sangromancer spells
Audit Master-tier spells across all classes. Candidates for "once per long rest": Mind Rupture (madness until cured), Blood Oblivion (permanent memory erasure), potentially Wound Reversal.

#### Glyph Triggers, AoE, Resources

**Issue 43** — 9 glyphs with no trigger conditions
Review each glyph and assign a trigger from the standard set. Recommended triggers are listed per-glyph in the issue. **Effectively Tier 1 once confirmed.**

**Issue 44** — AoE friendly fire convention
Establish universal rule: *unqualified "creatures" = everyone, including allies.* Then sweep 9 AoE spells and add `"creatures of your choice"` where unintentional. Biggest single edit pass on the list — but mechanically straightforward once decided.

**Issue 45** — Resource regeneration terms undefined
Write feeding economy into §5.7: how much BP per creature, soul shard crafting, channeling mechanics. Recommended framework is in the issue. Touches Ch. 5 and Ch. 7.

**Issue 46** — Permanent max HP reduction has no recovery mechanism
Recommended recovery: Soulforge Resurrection restores all lost max HP; long rest at a healing location restores 1. One paragraph in §5.7 or Ch. 8.

**Issue 48** — Aura scaling asymmetry: intentional or not?
- **Option A:** Acknowledge intentional asymmetry — add a design note to §5.4.
- **Option B (recommended if auras feel weak at high play):** Add partial aura scaling: `+1 damage at levels 10 and 20 only`.

#### Pass 8 Issues

**Issue 51** — Soul Fracture: SE cost increase amount
Decide the increment (+1 SE recommended), then add repeat save. **Effectively Tier 1 once the number is chosen.**

**Issue 52** — Wound Reversal: save target and max HP overflow
Recommended: both targets save; HP caps at max; excess lost. Fix text is in the issue.

**Issue 53** — No general dispel mechanic
- **Option A (recommended):** Add **Unravel** spell (Adept, GW/WB/HW) that removes one ongoing non-glyph effect.
- **Option B:** Add Dispel as a §5.6 universal mechanic like Counterspell.
- **Option C:** Intentional absence — state it explicitly as a system design pillar.

**Issue 57** — Crimson Godseed attribute boost: permanent or timed?
- **Option A (recommended):** 24-hour duration — powerful but not campaign-warping.
- **Option B:** Permanent, capped at one use per character — high cost justifies it but needs a hard cap.

**Issue 59** — Last Rite of Balance "DR 4–5": define what determines which
Recommended: Corruption Level of the area (1–5 → DR 4; 6+ → DR 5). One sentence.

---

### Tier 3 — Expansion Work
*Requires writing substantial new content. Multi-session tasks.*

**Issue 17 (main body)** — 17 unrunnable spells need full effect definitions
This is the largest single task in the document. Recommend a dedicated **Spell Expansion Session** starting with the six high-priority combat-relevant spells (Vital Dominion, Reaver Unleashed, Sanctify Ground, Fatebind Curse, Dark Reflection, Warding Circle), then proceeding through the medium and lower tiers.

**Issue 31** — Add Staggered condition entry to Ch. 12 Glossary
One new condition block in a different file from the rest of the fixes.

**Issue 45 (partial)** — Full resource regeneration rules
Write the feeding economy (BP per creature size or TV), soul shard item entries, and channeling mechanics. Touches Ch. 5, Ch. 7, and potentially Ch. 9.

**Issue 55** — Write Sanguine Swarm stat block
HP, speed, area, action timing, Frightened DR and save type. ~5–8 lines in the spell entry.

**Issue 22** — Rewrite Binding of the Starborn for Nosgoth cosmology
Replace "celestial entity" with a Bound Guardian framework. Full flavor + mechanics rewrite, ~8–10 lines.

---

### Recommended Execution Order

| Session | Focus | Issues |
|---|---|---|
| **Session A** | Spectral Realm fixes | 1, 2, 3, 5, 7, 16 |
| **Session B** | Quick text fixes across Ch. 5 | 4, 6, 8, 10, 13, 14, 15, 23, 27, 30, 32, 33, 34, 40, 41, 42, 47, 49, 50, 54, 56, 58 |
| **Session C** | Control duration and save violations | 9, 11, 12, 18, 19, 21, 38, 51, 52 |
| **Session D** | Undefined terms and resource rules | 25, 26, 28, 29, 31, 45, 46, 48, 59 |
| **Session E** | Interactions and balance decisions | 20, 24, 35, 36, 37, 39, 44, 53, 57 |
| **Session F** | Glyph trigger pass | 43 |
| **Session G+** | Spell expansion (unrunnable spells) | 17, 22, 55 |

**Session B alone closes 22 issues — the fastest single-session win available.**
