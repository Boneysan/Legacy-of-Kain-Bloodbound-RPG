# Bloodbound RPG: Alternative Perk Design Review
**Scope:** All 24 "or" alternatives at Levels 5, 10, and 15 across all 8 classes  
**Date:** March 5, 2026  
**System Version:** 1.0 (In Development)

---

**Status Legend:**
- ✅ **APPROVED** — No issues found; ready for use.
- ⚠️ **MINOR REVISION** — Conceptually sound; needs wording, clarity, or minor balance fix.
- 🔴 **MAJOR REVISION** — Significant mechanical flaw, naming collision, or design failure requiring a rework before use.

---

## Table of Contents
- [Blood Knight](#blood-knight)
- [Soul Reaver](#soul-reaver)
- [Shadowmancer](#shadowmancer)
- [Sangromancer](#sangromancer)
- [Glyphwright](#glyphwright)
- [Dreadblade](#dreadblade)
- [Warden of Balance](#warden-of-balance)
- [Hylden Warlock](#hylden-warlock)
- [Summary Table](#summary-table)
- [Cross-Cutting Issues](#cross-cutting-issues)

---

## BLOOD KNIGHT
*Core Attributes: Fury, Blood | Role: Tank / Melee Bruiser*

---

### Level 5: Blood Frenzy — 🔴 MAJOR REVISION

**Lore/Theme:**
The concept is excellent: a Blood Knight entering an escalating frenzy with each kill, building momentum like a rolling avalanche of rage. This image is core to the class fantasy and echoes the relentless aggression of Blood Omen's vampire warriors. However, the name is fatally compromised by its collision with existing content.

**Mechanical Issues:**
1. **Critical — Name Collision:** The Blood Knight already has a Core Ability named **Blood Frenzy** (Passive): *"Gain +1 Fury to your dice pool for the next action when you take damage."* This perk also names itself Blood Frenzy but has a different mechanical trigger and effect entirely. A player reading their sheet, referencing either one in play, or checking the perk index will encounter immediate and persistent confusion.
2. **Undefined Stack Decay:** "Max 3 stacks" with "until end of next turn" is ambiguous: (a) Do all stacks share a single duration that resets on each kill, or does each stack have its own independent 2-turn window? (b) If you kill on Turn 3, Turn 5, and Turn 6, how many stacks are active on Turn 7? The rolling-window intent is not stated.
3. **Kill Scope:** It should be stated whether non-combat kills (e.g., execution of a downed foe) count toward stacks.

**Recommendation:**
Rename to **Killing Momentum** or **Bloodlust**. Clarify stack behavior as: *"Each kill adds one stack (max 3). All stacks expire at the end of your next turn. If you gain a stack before all stacks expire, reset all stack durations."*

---

### Level 10: Sanguine Fortress — ⚠️ MINOR REVISION

**Lore/Theme:**
Well-conceived and well-named. The image of a Blood Knight's body hardening and knitting itself back together at the edge of death is consistent with vampiric biology and the "stronger when wounded" motif that defines the class. Thematically superior to Bloodstorm for players who want a defensive identity.

**Mechanical Issues:**
1. **Missing Usage Limit:** The ≤25% HP trigger has no stated reset condition. If a Blood Knight heals above 25% HP and then drops back below it in the same combat, the effect could trigger again — potentially multiple times in an attrition fight.
2. **Double-Trigger Problem:** Deathbound (Level 7) is 1/scene. But the ≤25% HP trigger has no scene or combat limit. Both conditions can satisfy the trigger in the same fight, granting +2 Armor and 3 HP regen × 3 rounds twice. This is likely unintentional.
3. **Intentional Interaction Note:** This pairs well with Unyielding Spirit (Level 16). The stacking of both perks off a single Deathbound activation is presumably intentional for the tank class, but worth acknowledging explicitly.

**Recommendation:**
Add *"1/combat"* to the trigger. Specify: *"This effect can trigger at most twice per scene — once from the ≤25% HP condition, and once from Deathbound triggering — tracked independently."*

---

### Level 15: Endless Hunger — 🔴 MAJOR REVISION

**Lore/Theme:**
Outstanding lore fit. The name is a thesis statement on vampiric existence — the endless, unsatisfiable hunger that defines every vampire in the Legacy of Kain series. One of the best-named perks in the book.

**Mechanical Issues:**
1. **Critical — Undefined Reference:** "Life Drain has no per-turn limit" removes a limit that does **not currently exist** in the written rules. The Core Ability states: *"When you deal melee damage, heal HP equal to half the damage dealt (round up)."* No per-turn cap is written anywhere. This perk either references a prior draft or requires adding a cap to the base ability so this perk has something to remove.
2. **Double-Heal on Kill:** "Each kill heals an additional 4 HP" — does this stack with Life Drain on the same killing blow? (e.g., 10 damage kill = 5 HP Life Drain + 4 HP kill bonus = 9 HP total?) This should be confirmed explicitly.
3. **Interaction with Lord of the Feast (Level 17):** Lord of the Feast grants "100% of damage dealt when below 50% HP." With no per-turn limit, a Blood Knight could heal back to max HP in a single round against multiple weak enemies. This stacking must be flagged on one or both perks.

**Recommendation:**
Add a per-turn cap to the base **Life Drain** Core Ability: *"Life Drain applies once per turn to the first hit each turn."* Then rewrite this perk's first clause: *"Life Drain applies to every melee hit you make in a round, not just the first."* Explicitly confirm the +4 kill-heal stacks with Life Drain on the same killing blow.

---

## SOUL REAVER
*Core Attributes: Soul, Fury | Role: Phase Warrior / Hybrid Caster*

---

### Level 5: Reavers' Resonance — ⚠️ MINOR REVISION

**Lore/Theme:**
Conceptually excellent. The Soul Reaver blade is described throughout the series as resonating with the spectral plane — it devours souls, emitting a harmonic vibration of spiritual energy. Having that energy arc to a second target is entirely consistent with how the Reaver is portrayed in the source material.

**Mechanical Issues:**
1. **Apostrophe/Naming Error:** The perk is titled "Reavers' Resonance" (possessive plural) but should be "Reaver's Resonance" (possessive singular) to match the class name and every other perk that invokes the class title (*Reaver's Hunger, Reaver's Wrath*).
2. **Ambiguous Proximity:** "Within 10ft" does not specify whether the secondary target must be within 10ft of the primary target or within 10ft of the caster. The intent is almost certainly "within 10ft of the primary target."
3. **"Half damage" is undefined:** Half of the base weapon damage? Half of the actual damage dealt after armor was ignored? Should clarify it is *half of the damage dealt to the primary target.*

**Recommendation:**
Fix apostrophe to *Reaver's Resonance*. Rewrite: *"Spectral Strike chains to a second target within 10ft of the primary target, dealing half the damage dealt to the primary target (also ignores Armor)."*

---

### Level 10: Soul Rift — ⚠️ MINOR REVISION

**Lore/Theme:**
One of the most evocative perks in the game, rivaling the franchise's own imagery. A "wound in the soul" — a rent in the spectral fabric that keeps bleeding after the physical strike — is directly drawn from how the Soul Reaver blade's violence worked on Raziel's victims. Thematically and mechanically coherent.

**Mechanical Issues:**
1. **Action Economy Confusion:** The stat line reads "Action, 1/short rest." But Soul Blade is a Passive — there is no separate Soul Blade action to declare. The current wording reads as though Soul Rift is a special Action that requires landing a Soul Blade hit, but it's unclear if it's an activation-turn Action or a triggered Passive.
2. **Stack Duration Interaction:** "Stacks up to ×2" — does the second stack apply its own independent 3-turn timer, or does it refresh the existing stack's timer? Independent stacks = up to 18 Spectral dmg over 6 turns. Refreshed timer = 18 Spectral dmg over 3 turns. A significant difference requiring an explicit statement.

**Recommendation:**
Rewrite: *"When you take the Attack Action and land a hit with Soul Blade, you may activate Soul Rift (1/short rest). The target takes 3 Spectral damage (bypasses Armor) at the start of each of their turns for 3 turns. A second activation of Soul Rift on the same target before this expires adds a second stack; each stack runs its own 3-turn timer."*

---

### Level 15: Phase Anchor — 🔴 MAJOR REVISION

**Lore/Theme:**
The single most narratively powerful perk in the class tree. Dragging an unwilling creature into a different plane of existence as you pass through it is exactly how Raziel's nature worked — his existence was disruptive to the material order, and enemies who touched him risked being pulled into his spectral world. A perfect Level 15 fantasy.

**Mechanical Issues:**
1. **The "Passive" Tag Is Misleading:** A Passive triggers automatically under conditions. But "drag one unwilling creature" requires deliberate selection of a target. As written, every Phase Shift targets someone — neither practical nor always desirable. This should be an optional component of Phase Shifting.
2. **"Until They Leave" Has No Exit Condition:** For creatures without Phase Shift or any realm-traversal ability, "leaving" may be literally impossible by their own means. This creates an indefinite, no-exit debuff. A per-turn escape save is needed.
3. **Realm Isolation:** Pulling a creature into the Spectral Realm effectively removes them from the fight for everyone who cannot enter that realm. Can they be attacked by non-Soul-Reaver allies? Can they attack the Soul Reaver while in the same realm? Chapter 11 must be cross-referenced here.
4. **No Boss Exemption:** The one-time save is DR 3. There is no frequency for additional saves to escape, and no Legendary/Boss immunity clause. A single failed save could exile a boss from combat indefinitely.

**Recommendation:**
Change the tag to *"Bonus Action (when Phase Shifting)"* to make the targeting choice explicit. Add a per-turn escape save: *"The creature may repeat the DR 3 Soul save at the end of each of their turns; on a success, they are expelled back to their original realm with 0 movement remaining."* Add *"Legendary and Boss creatures are immune to this forced realm transfer."*

---

## SHADOWMANCER
*Core Attributes: Shadow, Soul | Role: Stealth / Controller / Summoner*

---

### Level 5: Shade Pact — ⚠️ MINOR REVISION

**Lore/Theme:**
Excellent. Shade Pact deepens the Shadow Familiar relationship into a deliberate, combat-binding pact — a more aggressive shadow entity called forth through intent. The Zephonim clan's relationship with shadow-beings in Soul Reaver lore (their servants were barely-corporeal shadow things) makes this very appropriate.

**Mechanical Issues:**
1. **Ambiguous Replacement:** "Replaces prior Shade" — does this replace the Shadow Familiar (Core Ability), or only a previously summoned Shade from a prior use of this same perk? If it replaces Shadow Familiar, that Core Ability effectively becomes inactive once Shade Pact is taken. If not, a player could maintain two shade-type entities simultaneously.
2. **Damage Scaling:** The Shade deals "2 Entropic dmg." The Weapon Damage Scaling rule grants +1 base damage at Levels 5, 10, 15, and 20 to "all weapons and damaging abilities." Does this apply to the Shade's attacks? If not, the Shade becomes very weak by Level 15.

**Recommendation:**
Clarify *"Replaces a previously summoned Shade from this perk (does not replace Shadow Familiar)."* Explicitly address scaling: *"The Shade's damage increases with the Weapon Damage Scaling bonus."*

---

### Level 10: Nightmare Chorus — ⚠️ MINOR REVISION

**Lore/Theme:**
Thematically sharp. One person's scream of fear becoming a chorus as it spreads to those around them is a coherent extension of the Shadowmancer's psychological-warfare identity. The Zephonim were never about direct confrontation; they preferred mechanisms that caused enemies to break themselves. This fits.

**Mechanical Issues:**
1. **Individual vs. Group Save:** "Affects all enemies within 5ft of the primary target" — does each nearby enemy make their own Will save, or is the splash automatic? Fear Toxin involves a save for the primary target; saves for nearby targets should be maintained but are not stated.
2. **Retroactive Difficulty Change:** "+1 to Will save Difficulty for all your Fear effects" applies to every Fear ability the Shadowmancer has, including Terror Aura (Level 15). This is a blanket, global buff — players and GMs should understand the stacking (Terror Aura normally Diff 3 becomes Diff 4 with this perk). Explicit cross-reference avoids confusion.

**Recommendation:**
Add *"Each nearby enemy makes a separate Will save (Difficulty 4 with this perk active)."* Add cross-reference: *"This +1 stacks with future Fear-based perks including Terror Aura."* Consider also: *"A creature can only be affected by the Fear Toxin splash once per scene."*

---

### Level 15: Shadow Court — 🔴 MAJOR REVISION

**Lore/Theme:**
The name is evocative of dark royalty — a Shadowmancer presiding over a silent court of doppelgangers. This strongly echoes the Zephonim's psychological warfare aesthetic and vampiric court dynamics. At Level 15, becoming a shadow-multiplied presence on the battlefield is a genuine power fantasy apex.

**Mechanical Issues:**
1. **Critical — Action Economy Breakdown:** The perk says each Doppelganger "acts on your Bonus Action" — but a character has exactly **one Bonus Action per turn**. If all three Doppelgangers require independent Bonus Action commands, two of them can never act in any given turn. The design intent is almost certainly "one Bonus Action commands all active Doppelgangers simultaneously" — but as written it commands only one.
2. **Undefined Doppelganger Stats:** The Level 12 base perk describes the Doppelganger only as "a combat-capable shadow clone." No HP, DV, damage output, or action suite is defined. Shadow Court buffs these nonexistent baselines. Players taking Shadow Court at Level 15 are working with pure ambiguity.
3. **Resummoning:** If a Doppelganger is destroyed mid-combat, can you spend 2 SE and a Bonus Action to resummon one? Currently unstated.

**Recommendation:**
Rewrite the action economy clause: *"One Bonus Action commands all active Doppelgangers simultaneously; each takes one specified action (attack, move, etc.)."* Define Doppelganger stats explicitly in the Level 12 Doppelganger perk entry (HP, DV, damage die) and reference that definition here. Add *"Destroyed Doppelgangers can be re-summoned during combat as a Bonus Action (2 SE each)."*

---

## SANGROMANCER
*Core Attributes: Blood, Soul | Role: Blood Mage / Battlefield Control*

---

### Level 5: Vital Surge — ⚠️ MINOR REVISION

**Lore/Theme:**
Clean and tonally accurate. The Sangromancer feeding on the vitae expressed through Hemorrhage — sustaining yourself off a target's bleeding — is the apex of Sangromantic arts. Direct and unambiguous in theme. The name could be more distinctively Nosgothic ("Sanguine Replenishment" or "Vitae Tithe") but communicates clearly.

**Mechanical Issues:**
1. **Multi-Source Stacking:** Hemorrhage can presumably be applied to multiple targets simultaneously. By higher levels, with Wound Echo (Level 7) extending duration and multiple Hemorrhage sources, a Sangromancer could passively heal 2 HP per tick per active Hemorrhage — potentially 6–10 HP per round in a group fight.
2. **Synergy Note:** The Vital Surge heal is a flat 2 HP per tick regardless of Hemorrhage's damage (which scales with Profound Hemorrhage at Level 11). This is a deliberate design choice — the heal is fixed while damage scales — but should be affirmed.

**Recommendation:**
Add *"You can only benefit from Vital Surge's healing once per round, regardless of how many Hemorrhage effects are active."* This caps passive healing without breaking the core concept.

---

### Level 10: Blood Cascade — 🔴 MAJOR REVISION

**Lore/Theme:**
Mechanically inventive and thematically on-point. Every injury on a bleeding target becoming a door for more damage — the Sangromancer treating blood itself as an attack vector that spreads through existing wounds — is core to the class identity. Cascading blood magic, where one wound begets another, is flawlessly themed.

**Mechanical Issues:**
1. **Critical — "Allies Share This Benefit" Is Ambiguous:** This clause has two interpretations: (a) each ally independently triggers their own +2 Blood damage proc on hits against bleeding targets (4 allies = up to +8 extra armor-bypassing damage per hit), or (b) allies' attacks count as sources that trigger one shared proc. Interpretation (a) in a party of 4 could add 8 armor-bypassing damage to every single attack on a bleeding enemy — making armor near-irrelevant.
2. **"Any Source" Is Too Broad:** Environmental hazards, fall damage, friendly-fire incidents, and self-damage would all technically trigger Blood Cascade. Should specify "damage from any attack or ability."

**Recommendation:**
Rewrite the ally clause: *"Allies within 30ft may also trigger Blood Cascade on their attacks against bleeding targets; however, only one instance of Blood Cascade can trigger per damage event, regardless of how many eligible attackers are present."* Change "from any source" to "from any attack or ability."

---

### Level 15: Crimson Necromancer — ⚠️ MINOR REVISION

**Lore/Theme:**
Tonally correct. "Crimson" foregrounds the blood-magic origin that distinguishes this from traditional necromancy — body-sculpting through vitae, not the raising of the dead via soul-binding. The dependency chain (Level 12 True Fleshcrafting → Level 15 Crimson Necromancer) is correctly structured.

**Mechanical Issues:**
1. **Undefined Servitor Stats:** True Fleshcrafting (Level 12) says "animate a corpse as a grotesque servitor" but provides no stat block — no HP, DV, attack damage, or action limits. Crimson Necromancer improves these values (+5 Max HP, +2 damage) but cannot be meaningfully evaluated without knowing the baseline. If defined in the GM Guide or Monster Manual, a cross-reference is needed. If not defined anywhere, it needs to be.
2. **"From One Corpse" Interpretation:** Does "creates 2 servitors from one corpse" mean one ritual, one corpse, two separate entities? This should be confirmed. What are the fiction implications (two half-size constructs splitting a corpse)?
3. **Ritual Cost:** True Fleshcrafting costs *Ritual, 1 BP*. Confirm Crimson Necromancer does not change the ritual cost (or state explicitly that it does not).

**Recommendation:**
Define True Fleshcrafting servitor stats in the Level 12 perk entry, or reference a relevant stat block. In this perk: *"One ritual on a single corpse produces two servitors instead of one. Ritual cost is unchanged."*

---

## GLYPHWRIGHT
*Core Attributes: Soul, Will | Role: Support / Utility Caster*

---

### Level 5: Shock Cascade — ⚠️ MINOR REVISION

**Lore/Theme:**
The Hylden-origin electrical arcing of Glyphwright technology is well-established by Shock Sigil (Level 4). Shock Cascade extends the arc from the glyph's primary target to the nearest bystander — consistent with how electricity behaves and how alien glyph-technology is presented in the source material: unpredictable, slightly chaotic energy that doesn't respect the neat boundaries its wielder intended.

**Mechanical Issues:**
1. **Critical — "Un-glyph'd" Wording:** "Nearest un-glyph'd enemy" has two readings: (a) the nearest enemy not the *target of the triggering glyph* (intended), or (b) the nearest enemy who does not have any *glyph placed on them*. Reading (b) creates perverse incentives where the Glyphwright avoids placing glyphs near some enemies to ensure Cascade can always find a valid secondary target.
2. **Armor Interaction:** "2 Electrical damage (no save)" does not clarify whether the standard Elemental rule applies (Armor halved for Elemental damage). Should state *"2 Electrical damage — halves Armor, no save"* to prevent table disputes.

**Recommendation:**
Rewrite: *"When a glyph triggers, the nearest enemy not already targeted by that glyph within 10ft takes 2 Electrical damage (no save; Elemental — Armor halved)."*

---

### Level 10: Glyph Surge — ⚠️ MINOR REVISION

**Lore/Theme:**
The Glyphwright's equivalent of a tactical detonation — all prepared traps firing in synchronized concert. This is the apex of the "prepared battlefield" school of Glyphwright strategy and incentivizes the behavior that defines the class: laying glyphs before the enemy arrives.

**Mechanical Issues:**
1. **Arcane Focus SE Feedback Loop:** Arcane Focus (Level 2): "Regain 1 SE when a glyph is triggered." Glyph Surge simultaneously triggers all active glyphs. With 3 glyphs active, Glyph Surge simultaneously generates 3 SE — restoring most or all of the SE spent setting those glyphs. Decide if this is intentional.
2. **Non-Damage Glyphs:** "+2 additional damage" does not address non-damage glyphs such as Seal of Binding (which immobilizes). Clarify: damage bonus applies to damage-dealing glyphs only; non-damage glyphs trigger normally.
3. **Active Glyph Count Cap:** No maximum number of active glyphs is stated. With Nexus Glyph (Level 9) and Interwoven Wards (Level 12), a large simultaneous trigger chain is possible. A cap or cross-reference to where it's defined is needed.

**Recommendation:**
Add: *"The +2 damage bonus applies only to glyphs that deal damage; non-damage glyphs trigger their effects normally."* Decide on the Arcane Focus interaction and state it explicitly: if unintentional, add *"Arcane Focus does not trigger from glyphs activated by Glyph Surge."*

---

### Level 15: Resonant Overload — ⚠️ MINOR REVISION

**Lore/Theme:**
The Glyphwright weaponizing their own creation at the cost of its destruction. Alien Hylden technology pushed past its operating parameters tearing itself apart in a final, cataclysmic release — thematically resonant with the Glyphwright's narrative of reverse-engineering incomprehensible geometries at risk to their own sanity.

**Mechanical Issues:**
1. **"Triple Damage" Multiplication Order:** Does triple apply to the glyph's base damage (before Shock Sigil +1, Resonant Frequencies +2, Weapon Damage Scaling +3, etc.), or to the total modified damage including all bonuses? Example: Seal of Fire with all bonuses = 11 dmg. Triple base (5) = 15 + bonuses = 20. Triple total = 33. Substantial difference — must be defined.
2. **Non-Damage Glyphs:** "Triple damage" is undefined for Seal of Binding, Chrono Sigil, etc. What happens to a non-damage glyph when overloaded? Needs an explicit clause.

**Recommendation:**
Specify *"triple the glyph's base damage before any bonuses (flat bonuses from Shock Sigil, Resonant Frequencies, and Weapon Damage Scaling still add after tripling)."* For non-damage glyphs: *"Non-damage glyphs instead double their area of effect and their save DR increases by 1."*

---

## DREADBLADE
*Core Attributes: Shadow, Fury | Role: Assassin / Burst Damage*

---

### Level 5: Hemorrhage Strike — ⚠️ MINOR REVISION

**Lore/Theme:**
Conceptually excellent — a Dreadblade's stealth strike leaves a wound that keeps killing, rewarding the class's core behavior with persistent damage rather than just upfront burst. However, **the name "Hemorrhage" is already claimed by the Sangromancer's Core Ability**, which also causes 2 ongoing damage per round. Two different classes with near-identical ability names performing near-identical functions in the same book is a class identity problem.

**Mechanical Issues:**
1. **Naming Overlap:** "Hemorrhage" is Sangromancer vocabulary. The Dreadblade version needs a distinct name.
2. **Stack Duration Independence:** "Stacks up to 3 times" with "2 rounds" — are stacks on independent per-stack timers (each applied separately) or on a shared timer that resets on application? These produce meaningfully different damage windows: independent stacks = 1 round of maximum overlap; shared reset = 2 rounds of maximum overlap.
3. **"Attacks from Stealth" Scope:** Should match the exact language of **Auto-Crit From Stealth** (Core Ability) to avoid disputes about what counts as "from stealth."

**Recommendation:**
Rename to **Serrated Strike** or **Vein-Tap** to disambiguate from Sangromancer. Clarify: *"Each stack has its own 2-round duration from the moment it was applied."*

---

### Level 10: Ghost Protocol — 🔴 MAJOR REVISION

**Lore/Theme:**
The concept of a Dreadblade possessing kill-resetting techniques that chain together is tactically interesting and tonally appropriate. An assassin with a toolkit of precise conditional kills is the ideal Dreadblade fantasy. The word "Protocol" is slightly anachronistic for Nosgoth's gothic aesthetic but is functional.

**Mechanical Issues:**
1. **Critical — Redundant with Core Ability:** The Dreadblade's Core Ability is **Auto-Crit From Stealth (Passive): "Attacks from stealth are critical hits."** Ghost Protocol's stated effect is: *"re-entering Stealth mid-combat makes your next Stealth attack an automatic critical hit."* These are **identical outcomes**. Every Stealth attack the Dreadblade makes is already an automatic critical hit from a Core Ability. Ghost Protocol as written grants zero additional mechanical benefit. The perk is a noop.
2. **Undefined Re-entry Mechanism:** The perk doesn't define how to re-enter Stealth mid-combat. Smoke Veil (Level 3) creates a cloud — does that grant the Stealth condition? Without a defined mechanism, the trigger may be inaccessible without GM ruling.
3. **The Kill-Reset Is the Actual Design:** The only genuinely new content is the *kill-reset* mechanic for the once-per-scene usage. This is the perk's central feature; the crit clause needs to be redesigned to provide a benefit that exceeds (not duplicates) the Core Ability.

**Recommendation — Complete Redesign Required:**
Proposed rewrite:
> **Ghost Protocol** (Passive): *Once per scene, when you re-enter Stealth mid-combat, your next attack ignores the target's Armor entirely and forces them to make a DR 3 Will save or become Frightened for 1 round. Resets after a kill.*

This preserves the kill-reset mechanic, gives the perk a unique function (Armor bypass + Fear), and maintains the assassination fantasy without duplicating Auto-Crit From Stealth.

---

### Level 15: Bleeding Storm — ⚠️ MINOR REVISION

**Lore/Theme:**
The Dreadblade as an artist of accumulated wounds, engineering a kill through compounding injuries rather than a single decisive blow. "Bleeding Storm" visualizes it precisely — blood falling like rain, each wound opening another. Tonally excellent and represents a clean build path distinct from the burst-damage paradigm.

**Mechanical Issues:**
1. **"Start and End" — Whose Turn?** "Bleeding effects deal damage twice per turn (start and end)" is ambiguous. Is this the start and end of the *target's* turn (before and after their actions), or the Dreadblade's turn? These produce meaningfully different action-order results.
2. **Cross-Class Bleed Interaction:** "Bleeding effects" without a caster qualifier means this would apply to *any* Bleeding applied by any source, including a Sangromancer ally's Hemorrhage. The intent is almost certainly "Bleeding effects *you* apply."
3. **Slowed Condition Clarification:** "Half movement, -1 die Evasion" — is this Evasion *checks* (active defense rolls) or the Evasion passive DV modifier? These are different in the system.

**Recommendation:**
Clarify: *"at the start and end of the bleeding target's turn."* Specify: *"Bleeding effects you apply."* Clarify: *"half movement speed and -1 die to Evasion checks."*

---

## WARDEN OF BALANCE
*Core Attributes: Will, Soul | Role: Judge / Fate Caster / Support*

---

### Level 5: Pillar's Verdict — ⚠️ MINOR REVISION (with Power Note)

**Lore/Theme:**
The Warden projecting the Pillar's protective mandate through their own Will is thematically precise. "Pillar's Verdict," however, implies a judicial pronouncement — a ruling that determines an outcome — rather than a physical interposition. The *concept* (intercepting harm to an ally) maps better to names like **Pillar's Ward** or **Balance's Aegis.** A verdict is an ending; this is a prevention.

**Mechanical Issues:**
1. **Power Gap vs. Primary:** Pillar's Verdict reduces one hit's damage by Will score (2–5 at Level 5) once per scene. Cycle Command returns an ally at 0 HP to 1 HP — it prevents death. The gap between "prevents 3 damage 1/scene" and "prevents death 1/scene" is enormous. Unless a player is specifically building around Will stacking, this choice requires no deliberation.
2. **Trigger Timing:** When does the reaction occur? "After the attack roll succeeds but before damage is applied to the ally's HP" should be stated explicitly.
3. **Armor Interaction:** Does the Will reduction apply before or after the target's Armor? Should specify *"reduce damage taken (after Armor), minimum 0."*

**Recommendation:**
Rename to **Pillar's Ward**. Clarify trigger timing and armor application. To make this a genuine choice: either (a) remove the 1/scene limit, (b) increase the reduction to *"Will score + 2,"* or (c) redesign as *"Negate the damage entirely from a single attack once per scene,"* making it a true death-prevention alternative.

---

### Level 10: Scales of Ruin — ⚠️ MINOR REVISION

**Lore/Theme:**
One of the strongest thematic designs in the entire class tree. What you dish out, you absorb — this is quintessentially Pillar-of-Balance philosophy, and directly evocative of Moebius's manipulation of fate in the series. However, **"Ruin"** is entropy/Hylden vocabulary — not Balance vocabulary. Ruin is collapse; Balance is equivalence. Rename to **Scales of Retribution** or **Judgment's Mirror**.

**Mechanical Issues:**
1. **Critical — "Bloodied" Is Undefined:** "Lasts until Bloodied or scene ends." The term "Bloodied" does not appear in Chapter 12 (Glossary), Chapter 8, or Chapter 9 as a defined game term. Every table will rule this differently. The most common interpretation (≤50% HP) should be explicitly stated.
2. **"Bloodied" Subject Is Ambiguous:** Even if defined, whose Bloodied threshold ends the mark — the marked target's? The Warden's? An ally's? Each interpretation changes the perk dramatically.
3. **Reflected Damage Type:** "Half the damage they deal is reflected back" — what type is the reflected damage? If the marked creature deals Fire damage, is the reflection also Fire (possibly resisted by the creature)? Recommend specifying the reflection always deals **Spectral damage** regardless of source.

**Recommendation:**
Rename to **Scales of Retribution**. Replace "Bloodied" with *"until the marked target reaches ≤50% of their Maximum HP."* Define reflected damage as Spectral: *"half the damage they deal is reflected back as Spectral damage, regardless of the original damage type."*

---

### Level 15: Cycle's Enforcer — ⚠️ MINOR REVISION

**Lore/Theme:**
The name is the best of the three new Warden perks — post-Defiance, a Warden enforcing the Cycle's rightful turning against those who resist the Wheel is deeply evocative. The Prone condition against weakened enemies thematizes the Warden as the instrument that ensures nothing broken is allowed to keep standing. Excellent.

**Mechanical Issues:**
1. **Multi-Target Dispel Concern:** Balance Strike (Level 3) includes "Dispel magic." With Cycle's Enforcer, it hits all targets in a 10ft line. Does Dispel apply to *each* target in the line (stripping buffs/effects from multiple enemies simultaneously), or only the primary target? Against multiple magic-buffed enemies, line-Dispel could be encounter-trivializing. The perk needs to explicitly state one or the other.
2. **Line Geometry Undefined:** "Hits all targets in a 10ft line" — how wide? What origin point? In what direction? The system uses zones; a line is a new geometry with no established precedent.

**Recommendation:**
Specify *"Balance Strike's Dispel Magic triggers on each individual target in the line"* (or cap it to one target if that's the intent). Define line geometry: *"A 10ft line originating from you in any direction you choose, 5ft wide."*

---

## HYLDEN WARLOCK
*Core Attributes: Soul, Will | Role: Dark Mage / Debuffer*

---

### Level 5: Entropic Overload — ⚠️ MINOR REVISION

**Lore/Theme:**
The Hylden's philosophy was the rejection of all limitation — their banishment was the consequence of wielding power the world itself pushed back against. Entropic Overload is the Warlock deliberately overloading entropy in their next strike, making it unstoppable. Philosophically correct, tonally appropriate, well-named.

**Mechanical Issues:**
1. **Immunities vs. Resistances:** "Bypasses Armor and Resistances" does not clarify whether it also bypasses Immunities. A strict reading could allow it to bypass Immunity as well since "Resistances" might be interpreted as the entire mitigation tier. Needs explicit clarification: *"does not override Immunities."*
2. **Spell Scope:** "Your next spell or Void Shard" — does the bypass apply to spells with damage types (e.g., Spectral) that already ignore armor? On non-Void spells, the Resistance bypass is the only meaningful bonus. Confirm it functions across all spell types.

**Recommendation:**
Add *"(does not override Immunities)"* to the bypass clause. Confirm explicitly that the bonus applies regardless of the spell's damage type.

---

### Level 10: Void Cascade — ⚠️ MINOR REVISION

**Lore/Theme:**
The Hylden's entropic magic seeping outward from the point of impact, corrupting what it touches rather than stopping neatly at its target — entirely consistent with how void-magic is depicted in the series. The Hylden were defined by entropy as a fundamental, uncontrolled force. Well-named and on theme.

**Mechanical Issues:**
1. **Interaction with Hex Spark (Level 2):** Hex Spark: "Dealing spell dmg deals 1 Splash dmg to nearby." Void Cascade: "25% splashes to one adjacent enemy." On a single damaging Void spell, both Passives trigger simultaneously: primary damage + Hex Spark splash + Void Cascade splash. This is likely intentional (the Warlock's escalating splash identity) but should be an explicit design acknowledgment rather than an ambiguity.
2. **"Adjacent enemy within 5ft" Clarification:** Adjacent to the *primary target*, presumably — but "adjacent" without a reference point could mean adjacent to the caster. Should be stated explicitly.

**Recommendation:**
Add explicit note: *"This splash is in addition to any splash triggered by Hex Spark."* Clarify: *"within 5ft of the primary target."*

---

### Level 15: Hylden's Mantle — ⚠️ MINOR REVISION

**Lore/Theme:**
The most powerful sorcerers in Nosgoth's history, having turned their exile into eternal mastery, becoming so saturated with their own magic that other magic cannot penetrate them — deeply thematic. "Mantle" is perfect vocabulary for Nosgoth (Raziel "wore" his vampirism; Kain's rule was a mantle). One of the strongest flavor designs in the Warlock tree.

**Mechanical Issues:**
1. **"Magical Damage Types" Is Undefined:** The system uses six explicit damage categories (Physical, Elemental, Force, Spectral, Radiant, Entropic). "Magical damage types" is not a defined grouping. Presumably it means everything except Physical, but a magically conjured Physical-damage weapon could qualify under some interpretations. An explicit list is needed.
2. **"Magical Effect" Scope for the Negate:** "Completely negate one magical effect targeting you" — does "targeting you" include AoE effects that catch you incidentally (a fireball's blast radius), or only effects specifically aimed at you? Most powerful high-level effects are AoE. If AoEs are excluded, the negate is far weaker than its wording implies.
3. **Reaction Timing:** The perk doesn't specify when the Reaction can be declared. Should be: *"After being targeted by a magical effect, before it resolves."* Without this, disputes arise about post-damage declarations.

**Recommendation:**
Define magical damage explicitly: *"Resistance to Elemental, Force, Spectral, Radiant, and Entropic damage."* Specify Reaction timing: *"After a spell or magical ability targeting you is declared, before it resolves."* Decide on AoE inclusion and state it: *"including AoE effects that include your space"* (or exclude them explicitly).

---

## Summary Table

| Class | Level | Perk Name | Status | Priority Fix |
| :--- | :---: | :--- | :---: | :--- |
| Blood Knight | 5 | Blood Frenzy | 🔴 | **Rename** — fatal name collision with existing Core Ability. |
| Blood Knight | 10 | Sanguine Fortress | ⚠️ | Add 1/combat trigger limit; prevent re-trigger on HP recovery. |
| Blood Knight | 15 | Endless Hunger | 🔴 | Add per-turn cap to base Life Drain first; "removes a limit that doesn't exist" is a broken reference. |
| Soul Reaver | 5 | Reavers' Resonance | ⚠️ | Fix apostrophe; define "within 10ft of primary target"; define "half damage" as half of damage dealt to primary. |
| Soul Reaver | 10 | Soul Rift | ⚠️ | Clarify action cost (Attack Action); define whether second stack refreshes or runs independently. |
| Soul Reaver | 15 | Phase Anchor | 🔴 | Add per-turn escape save; define max trap duration; add Boss/Legendary immunity; change Passive tag to optional Bonus Action. |
| Shadowmancer | 5 | Shade Pact | ⚠️ | Clarify whether it replaces Shadow Familiar; explicitly address Weapon Damage Scaling on Shade attacks. |
| Shadowmancer | 10 | Nightmare Chorus | ⚠️ | Specify individual saves for nearby targets; add cross-reference to Terror Aura stacking. |
| Shadowmancer | 15 | Shadow Court | 🔴 | Fix action economy — one Bonus Action commands all Doppelgangers; define Doppelganger base stats at Level 12. |
| Sangromancer | 5 | Vital Surge | ⚠️ | Add "once per round" healing cap to cap multi-Hemorrhage passive healing abuse. |
| Sangromancer | 10 | Blood Cascade | 🔴 | Rewrite ally clause to one proc per damage event total; restrict "any source" to "attack or ability." |
| Sangromancer | 15 | Crimson Necromancer | ⚠️ | Define True Fleshcrafting servitor stats or cross-reference a stat block; confirm cost unchanged. |
| Glyphwright | 5 | Shock Cascade | ⚠️ | Replace "un-glyph'd enemy" wording; clarify Elemental Armor halved rule applies. |
| Glyphwright | 10 | Glyph Surge | ⚠️ | Decide whether Arcane Focus triggers per glyph (SE feedback loop); clarify non-damage glyphs trigger normally. |
| Glyphwright | 15 | Resonant Overload | ⚠️ | Define "triple damage" as ×3 base before bonuses; add non-damage glyph clause. |
| Dreadblade | 5 | Hemorrhage Strike | ⚠️ | **Rename** (e.g., "Serrated Strike") — "Hemorrhage" name overlaps with Sangromancer Core Ability. |
| Dreadblade | 10 | Ghost Protocol | 🔴 | **Complete redesign** — current effect is identical to Auto-Crit From Stealth (Core Ability); preserve kill-reset but replace the redundant crit clause. |
| Dreadblade | 15 | Bleeding Storm | ⚠️ | Specify "start and end of the *bleeding target's* turns"; add "effects you apply" qualifier; clarify Slowed affects Evasion checks not passive DV. |
| Warden of Balance | 5 | Pillar's Verdict | ⚠️ | **Rename** (Pillar's Ward); power-buff needed to be competitive with Cycle Command; clarify armor application order. |
| Warden of Balance | 10 | Scales of Ruin | ⚠️ | **Rename** (Scales of Retribution); define "Bloodied" (≤50% Max HP); specify reflected damage type as Spectral. |
| Warden of Balance | 15 | Cycle's Enforcer | ⚠️ | Clarify whether Dispel Magic applies to each target in line; define line geometry (10ft, 5ft wide, caster origin). |
| Hylden Warlock | 5 | Entropic Overload | ⚠️ | Add "(does not override Immunities)" to bypass clause. |
| Hylden Warlock | 10 | Void Cascade | ⚠️ | Confirm splash is relative to primary target; explicitly note Hex Spark stacking is intentional. |
| Hylden Warlock | 15 | Hylden's Mantle | ⚠️ | Define "magical damage types" as an explicit list; specify Reaction timing; clarify AoE inclusion for the negate. |

**Totals: 5 × 🔴 MAJOR REVISION | 19 × ⚠️ MINOR REVISION | 0 × ✅ APPROVED**

---

## Cross-Cutting Issues

These problems appear across multiple perks and should be addressed at the **system level** rather than perk-by-perk:

### 1. Define "Bloodied" in the Glossary
The term "Bloodied" appears (or is implied) in at least three perks. Add a definition to **Chapter 12 (Glossary)**:
> *"Bloodied: A creature is Bloodied when its current HP is at or below 50% of its Maximum HP."*

### 2. Define Summoned Entity Stat Blocks
Both **Shadow Court** (Doppelganger, Level 12) and **Crimson Necromancer** (Fleshcraft Servitor, Level 12) reference class-created summons with no defined stats. A half-page appendix in the GM Guide or Player's Handbook defining the base stats of all class-summoned entities (HP, DV, damage, actions available) would resolve cascading ambiguity across perks and their upgrade chains.

### 3. Establish a "Bypasses Resistance vs. Immunity" Rule
**Entropic Overload** introduces "bypasses Resistances" language. At minimum, a note in **Chapter 9 (Combat)** or **Chapter 7 (Equipment)** should establish the mitigation hierarchy:
> *"Resistance (halved) → Default → Immunity (negated). 'Bypasses Resistance' strips the Resistance tier only and never overrides Immunity unless a perk explicitly states otherwise."*

This future-proofs the language for additional perks.

### 4. Conduct a Name-Collision Audit
The **Blood Frenzy** collision (Core Ability vs. Level 5 Perk) reveals a systemic risk. Before the next revision pass, audit all 8 class trees to ensure no Core Ability name appears in any perk name across any class. This prevents similar confusion as the game expands.
