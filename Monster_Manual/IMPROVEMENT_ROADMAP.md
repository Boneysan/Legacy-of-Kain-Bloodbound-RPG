# Monster Manual — Improvement Roadmap

> **Audit Date:** March 3, 2026  
> **Last Updated:** March 2026 — Tier 1–4 fixes applied across all chapters; Tier 2 critical content gaps resolved  
> **Scope:** All 10 chapters (00–09) reviewed against Core Mechanics, Combat, Dice System, Encounter Design, and Character Progression rules.

---

## Table of Contents

1. [System-Wide Critical Issues](#1-system-wide-critical-issues)
2. [TV / Threat Value Distribution](#2-tv--threat-value-distribution)
3. [Balance Red Flags](#3-balance-red-flags)
4. [Formatting & Mechanical Issues by Chapter](#4-formatting--mechanical-issues-by-chapter)
5. [Missing Monsters — Priority Additions](#5-missing-monsters--priority-additions)
6. [Top 10 Priority Recommendations](#6-top-10-priority-recommendations)
7. [Lore Quality Ranking](#7-lore-quality-ranking)

---

## 1. System-Wide Critical Issues

These are cross-chapter inconsistencies that break mechanical compatibility and should be resolved before any content additions.

| Issue | Chapters Affected | Severity |
|---|---|---|
| **Movement units**: feet vs. tiles vs. squares | Ch1/2 use feet; Ch3 uses tiles | ✅ **RESOLVED** |
| **Damage type naming**: "Spectral" vs "Soul" | Ch2 (Sluagh) vs all other chapters | ✅ **RESOLVED** |
| **Attack notation**: "+X to hit" vs dice pool | Ch3 (Hash'ak'gik entries) | ✅ **RESOLVED** |
| **Attribute naming**: "Fortitude" vs "Blood" | Ch3 (Hash'ak'gik entries) | ✅ **RESOLVED** |
| **DV cap of 6** violated by GM Guide scaling formulas | GM Guide Elite/Boss tables; some stat blocks | ✅ **RESOLVED** — DV cap clarified in Ch0 Introduction; overtuned stat blocks corrected |
| **Stat block verbosity divergence** | Ch7 verbose vs Ch8/9 compact vs Ch1–3 medium | ✅ **RESOLVED** — Ch8 attacks standardized with attribute-skill links and defense targets |
| **Loot currency**: "barter value" vs "supplies" vs "Trade Value" | Ch1/2 vs Ch3 | **MEDIUM** |
| **Skill naming drift**: Perception vs Observation, Melee vs Swordplay, etc. | All chapters | ✅ **RESOLVED** — "Observation" standardized in Ch2; informal skills renamed in Ch4; missing skills added |
| **SE/BP pools never listed** on most monsters | Ch4–6 especially | ✅ **RESOLVED** — SE/BP lines added to all stat blocks in Ch4, Ch5 |
| **No Size/Type tags** on any creature | Ch7, Ch8, Ch9 | **LOW** |

### Resolution Guidance

- ✅ **Pick one movement unit** — All chapters now use feet. Ch0 Introduction includes "÷5 for squares" conversion note. Ch3 and Ch4 tile references converted.
- ✅ **Canonize "Soul damage"** — All instances of "Spectral damage" in Ch2 Sluagh entry changed to "Soul damage."
- ✅ **Rewrite Hash'ak'gik entries** — Acolyte and Vessel of Hash'ak'gik now use d6 dice pool notation and the "Blood" attribute.
- ✅ **Clarify the DV cap** — Ch0 Introduction now states DV 6 hard cap; overtuned DV values corrected (Bleeding Eye Assassin DV 7→6, Glyphfused Automaton DV 7→5).
- ✅ **Stat block format standardized** — Attribute-skill links added to Ch8; SE/BP pools added to Ch4/Ch5; attack formatting standardized across all chapters.

---

## 2. TV / Threat Value Distribution

### Full Roster by TV Tier

| TV Tier | Ch1 Undead | Ch2 Spectral | Ch3 Mortals | Ch4 Beasts | Ch5 Constructs | Ch6 Hylden | Ch7 Elemental | Ch8 Ancient | Ch9 Legendary | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|
| **0.25 (Minion)** | 2 | 1 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | **8** |
| **1 (Standard)** | 3 | 4 | 3 | 3 | 2 | 2 | 0 | 0 | 0 | **17** |
| **2 (Elite)** | 3 | 2 | 5 | 4 | 3 | 5 | 0 | 0 | 0 | **22** |
| **3** | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | **6** |
| **4 (Boss)** | 1 | 1 | 1 | 0 | 2 | 1 | 0 | 0 | 0 | **6** |
| **9–14** | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 5 | 0 | **13** |
| **15–19** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 8 | **11** |
| **20+** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | **0** |

### Key Gaps

| Gap | Impact | Priority |
|---|---|---|
| **TV 3 is completely empty** | No bridge between Elite (TV 2) and Boss (TV 4) — entire mid-tier missing | ✅ **RESOLVED** — 6 TV 3 creatures added (1 per Ch1–6) |
| **TV 5–8 is empty** | Massive jump from Ch1–6 (TV 0.25–4) to Ch7 (TV 9+); mid-level play has no dedicated creatures in upper chapters | **HIGH** |
| **TV 20+ is absent** | No true apex entity for endgame campaigns | **HIGH** |
| **Ch1 and Ch3 have no Boss stat blocks** | Only scaling sidebars — most-used chapters lack standalone Boss entries | ✅ **RESOLVED** — Nosgothian Vampire Overlord (Ch1, TV 4) and Sarafan Grand Inquisitor (Ch3, TV 4) added |
| **Ch6 has no Minion tier** | Can't run Hylden fodder encounters | ✅ **RESOLVED** — Hylden-Possessed Grunt (TV 0.25) added to Ch6 |
| **TV 14 has only 1 creature** (Bloodhail Cyclone) | Thin mid-high tier | **MEDIUM** |
| **Only 7 Minions total** across the entire book | Low-level encounter variety is constrained — now 8 Minions | **MEDIUM** |

---

## 3. Balance Red Flags

### Overtuned Creatures

| Creature | Chapter | Stated TV | Issue | Recommendation |
|---|---|---|---|---|
| **Bleeding Eye Assassin** | Ch3 | TV 2 | DV 7, 10d6 attacks, Evasion (10d6 defense roll), Coup de Grace instakill, AoE immunity while Hidden | ✅ **RESOLVED** — DV→6, pools reduced to 8d6, Coup de Grace→triple damage, AoE immunity→Advantage |
| **Wandering Mad Seer** | Ch3 | TV 1 | Advantage on all defenses, 33% total damage immunity (Fractured Timeline), turn-undo (Temporal Echo), crit negation | ✅ **RESOLVED** — Fractured Timeline→1/encounter half-damage, Temporal Echo→forced reroll |
| **Red Vein Acolyte** | Ch1 | TV 1 | Blood Bolt at 8d6 / 60ft range matches TV 2 melee creatures | ✅ **RESOLVED** — Blood Bolt reduced to 6d6 |
| **Soul-Eater Shade** | Ch2 | TV 1 | Growing Hunger grants +5 HP / +1 die per kill with **no cap** | ✅ **RESOLVED** — Capped at 3 stacks |
| **Silent Mourner** | Ch2 | TV 1 | Three separate Will-save attacks + passive Will aura — locks down low-Will parties | ✅ **RESOLVED** — Aura radius reduced to 10ft, triggers only on turn start |
| **Glyphfused Automaton** | Ch5 | TV 2 | DV 7, Armor 3 Phys / 4 Magic, Glyph Adaptation, Phase Step, Self-Repair (20 HP) — more defensive layers than the TV 4 Sentinel | ✅ **RESOLVED** — DV→5, Self-Repair→10 HP, Glyph Adaptation 1/encounter, Phase Step Recharge 5-6 |
| **Bound-Logic Scribe** | Ch5 | TV 1 | Knowledge Blast at 10d6, DV 5 — hits harder than several TV 2 creatures | ✅ **RESOLVED** — DV→4, Knowledge Blast reduced to 8d6 |
| **Void-Spoken Oracle** | Ch6 | TV 4 | Telepathic Coordination gives +2 dice to ALL Hylden allies within 100ft — game-warping force multiplier | ✅ **RESOLVED** — Reduced to +1 die within 30ft |
| **Warptooth Cougar** | Ch4 | TV 2 | At-will Incorporeal as a bonus action with no resource cost | ✅ **RESOLVED** — Limited to 3/encounter |
| **Frostbound Guardian** | Ch7 | TV 10 | **Exact copy-paste duplicate** of Frost-Wrought Avenger (identical stats, abilities, scaling) | ✅ **RESOLVED** — Replaced with **Glacial Warden** (TV 11, defensive area-denial ice construct) |

### Under-Protected Creatures

| Creature | Chapter | TV | Issue | Recommendation |
|---|---|---|---|---|
| **Vessel of Hash'ak'gik** | Ch3 | TV 2 | DV 3 — lowest for any TV 2 creature; dies before using abilities | ✅ **RESOLVED** — DV increased to 4 |
| **Razielic Remnant** | Ch9 | TV 18 | Armor 4 / 210 HP — weakest survivability of any Ch9 Boss | ✅ **RESOLVED** — Armor increased to 6, Legendary Resistance (3/day) added |
| **Blood Moon Prophet** | Ch9 | TV 15 | Armor 2 / 130 HP — extremely fragile for a Major threat | ✅ **RESOLVED** — Armor increased to 4, Crimson Veil reaction added, Legendary Resistance (2/day) added |
| **Forgotten Dreambeast** | Ch8 | TV 13 | Armor 2 / 110 HP — very fragile for its TV (controller tax?) | ✅ **RESOLVED** — GM Design Note added explaining glass-cannon design |
| **All Ch9 Entities** | Ch9 | TV 15–19 | **None have Legendary Resistance** — a single Restrain/Stun/Banish trivializes these fights | ✅ **RESOLVED** — Legendary Resistance (2–3/day) added to all 8 entities |

### Other Balance Notes

- ✅ **Bloodgullet Hound** (Ch4, TV 1): 3 HP/turn regen with no stop condition pushes effective HP to ~41 over 5 rounds — **RESOLVED**: Fire/Radiant damage now stops regen for 1 round.
- ✅ **Dire Cave Wolf packs** (Ch4): Pack Tactics (+3 dice) on 5–6 wolves with Pounce can deal 31+ damage round 1 — **RESOLVED**: GM note added warning about alpha-strike potential.
- ✅ **Hylden Soul-Tower** (Ch5, TV 4): 200 HP + 15/turn regen + 3 Soul Cores = astronomical effective HP — **RESOLVED**: GM siege encounter design note added.
- **Kain's Echo-Knight** (Ch9, TV 17): Rewrite ability (force reroll at Disadvantage, 6 SE) from 80 SE pool = **13 uses**. Risk of extremely prolonged, grindy encounters.

---

## 4. Formatting & Mechanical Issues by Chapter

### Chapter 0 — Introduction ✅

- ✅ Quick Reference lists creatures (e.g., "Dire Cave Wolves," "Echo Serpents," "Kain's Echo-Knight") that may or may not have stat blocks. Track as a checklist.
- ✅ Scaling rules are linear (+5 HP / +1 attribute / +1 DV / +2 damage per tier) but actual stat blocks show much larger jumps. **Non-linear scaling note added.**
- ✅ The "20 Standard enemies" example (line ~41) needs a note that this is mathematical equivalence, not practical encounter design. **Clarification added.**
- ✅ Missing: "How to read dice pools" primer for GMs unfamiliar with the system. **Primer added.**

### Chapter 1 — Undead & Vampiric ✅

- ✅ **Multiattack undefined**: "Can attack twice if using both claws" — **Proper Multiattack definition added.**
- ✅ **Vampire Thrall Swarm**: Thousand Bites dice pool/auto-hit conflict — **Dice pool removed, purely automatic hit.**
- ✅ **Revenant**: "Will" as both attribute and skill — **Skill renamed to "Resolve (Will): 2".**
- ✅ **Feralslave Ghoul**: Has Blood 1 as a non-vampiric mindless undead — **Changed to Blood 0 (Immune to Blood-based effects).**
- ✅ **Predator's Dodge** on Hunger-Warped Vampire references "Evasion 0" — **Evasion (Shadow): 0 added to skill block.**

### Chapter 2 — Spectral Entities ✅

- ✅ **"Spectral damage" vs "Soul damage"**: Sluagh — **All instances changed to "Soul damage."**
- ✅ **Sluagh's Carrion Grasp**: Unexplained +1 — **"Death Touch (Soul): 1" skill added to explain the pool.**
- ✅ **Shimmering Howler**: "Perception" — **Changed to "Observation." Loot section added.**
- ✅ **Phase-Beast Dimensional Instability**: Random direction undefined — **1d8 direction table added.**
- ✅ **Mirror Wraith Spectral Claws**: Multiattack ambiguity — **Proper Multiattack definition added.**
- ✅ **Gravewind Entity**: "Costs 2 actions" unclear — **Changed to "costs 2 Legendary Actions."**

### Chapter 3 — Mortals & Cultists ✅

- ✅ **Hash'ak'gik entries use "+X to hit" notation** — **Converted to d6 dice pool format.**
- ✅ **"Fortitude" attribute** on Acolyte and Vessel — **Corrected to "Blood."**
- ✅ **Movement in tiles, not feet** — **All tiles converted to feet (1 tile = 5 feet).**
- **Temporal Echo** ("undo a player's entire turn"): No rules for edge cases — **Rebalanced** to forced reroll, but edge case guidance could still be expanded.
- ✅ **Unique skills**: "Fanaticism: 3," "Pain Tolerance: 2" — **Renamed to "Devotion (Will): 3" and "Endurance (Blood): 2."**
- ✅ **Forsaken Priest**: Missing "Melee" in Skills section — **"Melee (Fury): 1" added.**
- **Section numbering**: Uses "### 1. Cult Fanatic" style vs "## 3.1 ..." in Ch1/2. — Cosmetic; low priority.
- ✅ **"Difficulty Rating (DR)"** on Hash'ak'gik entries — **Changed to "Save DCs" format.**

### Chapter 4 — Beasts & Mutants ✅

- ✅ **Informal skill names**: "Smashing Things: 4," "Mauling: 4" — **Renamed to "Brute Force (Fury)" and "Savage Attack (Fury)."**
- ✅ **No SE/BP pools listed** — **Explicit SE/BP lines added to all stat blocks.**
- ✅ **Flame Breath uses Recharge 5–6** but no SE cost — **Recharge system note added explaining it as separate from SE.**
- ✅ **Grapple escape DCs vary** — **All grapple escapes standardized to contested Fury + Athletics checks.**
- ✅ **No cross-chapter references** — **Cross-references added: Drake→Ch5, Blight-Boar→Ch6, Warptooth Cougar→Ch2.**

### Chapter 5 — Constructs & Automatons ✅

- ✅ **"Called shot" undefined** — **Definition added to Pillar-Guardian Sentinel's Core Weakness.**
- ✅ **SE pools never listed** — **SE lines added to all 8 stat blocks.**
- ✅ **Summoned Flesh Abomination at "TV 0.5"** — **Changed to "TV 1 (weakened)."**
- ✅ **Encounter 4 references scaled-down Automatons with no stat block** — **Stand-in stat block note added.**
- ✅ **Iron-Cage Beast Erratic Behavior** (skip turn on 1-in-6) — **Changed to deterministic one-time stun when bloodied.**

### Chapter 6 — Hylden Forces ✅

- ✅ **Soul Override** (Shock Trooper) — **Full PC possession resolution rules added** (contested Will save, 1d4 rounds, exorcism options).
- ✅ **Corruption Host Final Transformation → Abomination** — **Controller clarified** (GM controls, collapses if creator dies).
- ✅ **"Corruption damage" ambiguity** — **Separated into HP damage + Will save for Corruption points.**
- ✅ **Hylden Nature trait repeated verbatim 6 times** — **Refactored into Shared Traits section; subsequent instances reference it.**
- ✅ **Reality Distortion Aura** — **Standardized as optional trait in Shared Traits section.**
- ✅ **Open Rift summoning randomness** — **d6 table added with exactly 1 creature per roll result.**

### Chapter 7 — Elemental & Arcane ✅

- ✅ **Frost-Wrought Avenger / Frostbound Guardian**: Copy-pasted stat block — **Frostbound Guardian replaced with Glacial Warden (TV 11, defensive area-denial ice construct).**
- ✅ **Arcane Flare Wyrm Spell Echo**: No per-round limit — **"(1/round)" limit added.**
- ✅ **Thundercrack Behemoth vulnerability to "Earth-based effects"** — **Changed to "Grounding effects, anti-magic fields, and abilities that dispel or suppress magical energy."**
- ✅ **Mist Binder Soul Bind**: Full incapacitation — **Limited to one target at a time.**
- ✅ **Spiritbound Flame Wolf Pack Hunter's Sorrow**: Ambiguous trigger — **Clarified to "only hostile creature on the battlefield (no other enemies present)."**
- ✅ **Fire-Spite Djinn Immolate**: Stack removal unclear — **"(removes all stacks)" added.**

### Chapter 8 — Ancient Creatures ✅

- ✅ **Compact format drops details** — **Attribute-skill links added to all 8 creatures. Attack formatting standardized with defense targets.**
- ✅ **Missing save DCs** — **DCs added to Leviathan grapple escape, Undertow, and other missing saves.**
- ✅ **Only 3 of 8 creatures have scaling options** — **Scaling options added to all 5 missing creatures** (Bound Pillar Shade, Vaultspawn Ravager, Titan-Kin Stalker, Forgotten Dreambeast, Root-Entombed Horror).
- ✅ **No Immunities/Vulnerabilities** — **Added to Dreambeast, Titan-Kin Stalker, and Vaultspawn Ravager.**
- ✅ **Root-Entombed Horror**: Feels generic — **Lore expanded to tie to corrupted Pillar ley lines and ecology.**

### Chapter 9 — Legendary Entities ✅

- ✅ **No loot/rewards for ANY creature** — **Loot & Rewards sections added to all 8 entities** (3 thematic items each).
- ✅ **No Legendary Resistance on any entity** — **Legendary Resistance (2–3/day) added to all 8 entities.**
- ✅ **No scaling options** — **Weakened Form variants (TV −3 to −4) added to all 8 entities.**
- ✅ **The Pale Sarafan is missing its Lair Action** — **Sanctified Ground lair action added (3 options: Radiant damage, ally healing, consecrated ground).**
- ✅ **Vague mechanics**:
  - Kain's Echo-Knight **Hourglass Shatter** — **Full clarification added (buffs expire faster, DoT triggers twice).**
  - Warden of Lost Names **Unword** — **GM targeting guidance + Will save DC 17 added.**
  - Unseen Monarch **Command the Scene** — **Range 60ft, Will DC 16, action loss, costs 2 Legendary Actions.**
  - Blood Moon Prophet **Red Cycle** — **Clarified: cycle starts round 1, triggers rounds 3, 6, 9.**
- ✅ **Ariel's Spectral Wrath — Mercy Weighed** — **Bonus action cost, once per round.**
- ✅ **No Tactics sections** — **"For Players" / "For the GM" subsections added to all 8 entities.**
- ✅ **Under-protected entities** — Razielic Remnant Armor 4→6, Blood Moon Prophet Armor 2→4 + Crimson Veil reaction.

---

## 5. Missing Monsters — Priority Additions

### By Category

| Chapter | Missing Type | Suggested Monster | Recommended TV |
|---|---|---|---|
| **Ch1 Undead** | Boss Vampire Lord | **Nosgothian Vampire Overlord** — full Boss stat block | TV 4 |
| **Ch1** | Basic zombie/shambler | **Risen Thrall** — mindless melee fodder | TV 0.25 |
| **Ch1** | Necromancer/Lich | **Bonelord Archon** — undead spellcaster boss | TV 4 |
| **Ch1** | Vampire Spawn/Fledgling | **Vampiric Fledgling** — weak vampire (not just a scaling option) | TV 0.5–1 |
| **Ch1** | Skeletal variants | **Skeletal Archer / Knight** — ranged and melee skeletal types | TV 0.25–1 |
| **Ch2 Spectral** | Solo low-tier spectral | **Lingering Shade** — simple ghostly presence | TV 0.25 |
| **Ch2** | Spectral caster | **Spectral Arcanist** — ranged spell-focused ghost | TV 2 |
| **Ch2** | Spectral vampire (Raziel-type) | **Wraith of the Abyss** | TV 2–3 |
| **Ch3 Mortals** | Boss mortal | **Grand Inquisitor / Cult Hierophant** | TV 4 |
| **Ch3** | Basic soldiers/guards | **Sarafan Footsoldier / Town Guard** | TV 0.25 |
| **Ch3** | Corrupted mid-transform | **The Turning** — human mid-vampiric transformation | TV 1–2 |
| **Ch3** | Mortal ranger/tracker | **Sarafan Outrider** — wilderness enemy | TV 1 |
| **Ch3** | Civilian/non-combatant | **Commoner** — rules for bystanders in encounters | TV 0 |
| **Ch3** | Alchemist/artificer | **Rune-Forger** — tech/alchemy mortal | TV 1–2 |
| **Ch4 Beasts** | Aquatic creature | **Blightwater Eel / Corruption Leech** | TV 1 |
| **Ch4** | Swarm creature | **Plague Rat Swarm / Spectral Bat Cloud** | TV 0.25 |
| **Ch4** | Boss apex predator | **Nosgothian Alpha Wyrm** — fully statted, not just scaling | TV 4 |
| **Ch4** | Burrowing creature | **Tunnelworm** | TV 1 |
| **Ch4** | Aerial (non-drake) | **Corrupted Raptor / Spectral Crow** | TV 0.25–1 |
| **Ch4** | Symbiotic/parasitic | **Corruption Leech** — attaches to PCs | TV 0.25 |
| **Ch5 Constructs** | Healer/repair construct | **Restoration Engine** | TV 1–2 |
| **Ch5** | Stealth construct | **Glyph Spider** — infiltrator/scout | TV 0.25 |
| **Ch5** | Trap-construct hybrid | **Animated Ward / Glyph Turret** | TV 1 |
| **Ch5** | Friendly/reprogrammable | Template for ally constructs | — |
| **Ch6 Hylden** | Minion foot soldier | **Hylden-Possessed Grunt** | TV 0.25 |
| **Ch6** | Legendary commander | **Hylden Dimension Lord** | TV 6+ |
| **Ch6** | Corrupted beast mount | **Hylden War-Stalker** (beast + Hylden hybrid) | TV 2 |
| **Ch6** | Priest/ritualist | **Hylden Rift-Priest** — corruption spreader | TV 2–3 |
| **Ch7 Elemental** | Introductory elemental | **Lesser Spark Sprite / Flame Wisp** | TV 7–8 |
| **Ch7** | Earth/stone elemental | **Pillar-Stone Golem** | TV 10–11 |
| **Ch7** | Shadow elemental | **Umbral Vortex** | TV 9–10 |
| **Ch7** | Void/anti-magic entity | **Null Elemental** | TV 12 |
| **Ch7** | Arcane parasite | **SE-Feeder** — drains spent Soul Energy | TV 9 |
| **Ch8 Ancient** | TV 14 filler | **Ancient Pillar Wyrm** | TV 14 |
| **Ch8** | Ancient vampiric beast | **Primordial Blood Stalker** | TV 13 |
| **Ch8** | Corrupted Pillar variant | **Pillar-Decay Sentinel** | TV 12 |
| **Ch8** | Ruin trap-construct | **Living Ward** — trap + creature hybrid | TV 11 |
| **Ch9 Legendary** | TV 20+ apex | **Elder God Tendril / The Wheel Fragment** | TV 22–25 |
| **Ch9** | Ancient vampire lord | **Vorador the Patriarch** (or equivalent) | TV 18–19 |
| **Ch9** | Hylden Lord | **Hylden Overlord** — endgame faction boss | TV 18–20 |
| **Ch9** | Corrupted Pillar Guardian | **The Death Guardian** — Pillar-fused lich | TV 17–18 |
| **Ch9** | Time entity (Moebius link) | **Echo of Moebius** | TV 16–17 |

### By TV Gap

| TV | Current Count | Target Count | Action Required |
|---|---|---|---|
| **TV 3** | 6 | ~5–6 | ✅ **RESOLVED** — 1 added per chapter across Ch1–6 |
| **TV 5–8** | 0 | ~4–6 | Add bridge creatures connecting low and high chapters |
| **TV 14** | 1 | 2–3 | Add 1–2 creatures in Ch7/Ch8 |
| **TV 20+** | 0 | 1–2 | Elder God + one other apex entity in Ch9 |

---

## 6. Top 10 Priority Recommendations

### Tier 1 — Fix Immediately ✅ ALL RESOLVED

1. ✅ **Fix the Frost-Wrought Avenger / Frostbound Guardian duplication** (Ch7)  
   Frostbound Guardian replaced with **Glacial Warden** — a distinct TV 11 defensive area-denial ice construct with unique abilities (Icebound Slam, Permafrost Zone, Ice Wall, Crystalline Reformation).

2. ✅ **Standardize terminology system-wide**  
   All chapters now use: feet (not tiles) · Soul damage (not Spectral) · Blood (not Fortitude) · d6 dice pool (not +X to hit) · Observation (not Perception where applicable). Movement ÷5 note added to Ch0.

3. ✅ **Add Legendary Resistance to all Ch9 entities**  
   All 8 Legendary Entities now have Legendary Resistance (2–3/day based on TV).

### Tier 2 — Critical Content Gaps ✅ ALL RESOLVED

4. ✅ **Write full Boss stat blocks for Ch1 (Vampire Lord) and Ch3 (Grand Inquisitor)**  
   **Nosgothian Vampire Overlord** (Ch1, §1.11, TV 4): HP 90, DV 6, Legendary Resistance 3/day, 3 Legendary Actions/round. Full Boss with Blood Dominion (Charm), Crimson Torrent (cone AoE), Mist Form (death-save mechanic), and Command Undead. Includes scaling from TV 2 Diminished to TV 6+ Ancient Overlord.  
   **Sarafan Grand Inquisitor** (Ch3, §11, TV 4): HP 85, DV 6, Legendary Resistance 2/day, 3 Legendary Actions/round. Full Boss with Sanctified Aura (anti-vampire debuff zone), Divine Condemnation (double Radiant vs undead), Sanctified Judgment (40ft Radiant AoE). Includes scaling from TV 2 Captain to TV 6+ High Inquisitor with Lair Actions.

5. ✅ **Create TV 3 creatures**  
   Six TV 3 creatures added, one per chapter across Ch1–6, filling the void between Elite (TV 2) and Boss (TV 4):  
   - **Grave-Knight Commander** (Ch1, §1.12): Intelligent undead martial leader with Commander's Presence (+1 die to undead allies) and Deathless Fortitude.  
   - **Wraith of the Abyss** (Ch2, §2.12): Abyssal spectral entity with SE drain, Void Scream AoE, Phase Shift invisibility, and Dimensional Anchor (immune to banishment).  
   - **The Turning** (Ch3, §12): Mortal mid-vampiric transformation with Unstable Form (random d6 effects), Feral Desperation (attacks anyone when bloodied), and Tragic Nature (can be saved with Rituals checks).  
   - **Blightmaw Alpha** (Ch4, §9): Corrupted apex predator with Crushing Jaws grapple, Toxic Spray cone, Trampling Charge, and Alpha's Roar rallying ability.  
   - **Rune-Forged Warden** (Ch5, §9): Ancient Pillar-era construct with Zone of Denial (passive damage aura), Runic Shielding (regenerating temp HP), Sentinel Protocol (immune to forced movement), and Defensive Stance.  
   - **Hylden Rift-Priest** (Ch6, §9): Hylden caster with Corruption Lance, Rift Tear (AoE teleport scatter), Corruption Pulse, and Dimensional Tether (summons Grunts).

6. ✅ **Add a Hylden Minion (Ch6) and expand Minions overall**  
   **Hylden-Possessed Grunt** (Ch6, §10, TV 0.25): HP 8, DV 3. Expendable possessed mortal with Crude Weapon Strike, Corrupted Grasp, Hivemind Fodder (+1 die near other Hylden), and Expendable Host (25% death-lash). Designed as cannon fodder for combined-arms Hylden encounters. Total Minion count: 7→8.

### Tier 3 — Balance Corrections ✅ ALL RESOLVED

7. ✅ **Rebalance the Bleeding Eye Assassin, Wandering Mad Seer, and Glyphfused Automaton**  
   All three rebalanced: Assassin (DV→6, pools reduced, Coup de Grace→triple damage), Mad Seer (Fractured Timeline→1/encounter, Temporal Echo→forced reroll), Automaton (DV→5, Self-Repair halved, abilities limited).

8. ✅ **Add loot tables to Ch9**  
   All 8 Legendary Entities now have Loot & Rewards sections with 3 thematic endgame items each (24 total items).

### Tier 4 — Polish & Completeness (PARTIALLY RESOLVED)

9. ✅ **Standardize stat block format across all chapters**  
   Attribute-skill links, SE/BP pools, save DCs, loot sections, scaling options, and tactics breakdowns now appear across all chapters. Remaining: Size/Type tags for Ch7–9.

10. **Add an Elder God or TV 20+ apex entity to Ch9**  
    The franchise's iconic antagonist is conspicuously absent from a Legacy of Kain monster manual. Even a "Tendril of the Wheel" fragment encounter would anchor the endgame.

---

## 7. Lore Quality Ranking

| Chapter | Grade | Notes |
|---|---|---|
| Ch9 — Legendary Entities | **A+** | Every entity tied to deep franchise lore; campaign-defining encounters |
| Ch3 — Mortals & Cultists | **A** | Best GM guidance; moral complexity; faction integration outstanding |
| Ch6 — Hylden Forces | **A** | Strongest villain faction writing; Corruption Host concept is brilliant |
| Ch2 — Spectral Entities | **A−** | Great atmospheric writing; Sluagh ecology is a standout |
| Ch8 — Ancient Creatures | **A−** | Strong thematic cohesion; creatures feel like living history |
| Ch7 — Elemental & Arcane | **A−** | Copy-paste issue resolved; Glacial Warden adds distinct defensive design; all balance fixes applied |
| Ch5 — Constructs & Automatons | **B+** | Iron-Cage Beast and Scribe are creative; good faction diversity; SE pools and called shot defined |
| Ch4 — Beasts & Mutants | **B+** | Solid ecology; corruption theme well-woven; needs cross-references |
| Ch1 — Undead & Vampiric | **B** | Good but conventional; campaign usage section (1.9) elevates it |
| Ch0 — Introduction | **B** | Functional reference; good design philosophy; lacks narrative voice |

### Lore Improvement Notes

- ✅ **Add cross-chapter references**: Blight-Boars → Ch6, Warptooth Cougars → Ch2, Nosgothian Drake → Ch5. **Done in Ch4.**
- **Add named NPCs to Ch6**: The Hylden are "campaign villains" but have zero named individuals. A legendary General, a specific Oracle, etc., would seed campaign narratives.
- **Sharpen Blood Moon Prophet lore** (Ch9): "A seer bound to cycles of red light" is vague compared to the other entries' deep franchise connections.
- ✅ **Tie Root-Entombed Horror** (Ch8) more specifically to Nosgoth's corrupted Pillar ecology. **Pillar ley line lore added.**
- **Add Corruption interaction notes to Ch5**: Can constructs be corrupted? Can a corrupted Golem exist? Given the central Corruption mechanic, this gap is notable.

---

## Appendix: Stat Expectation Reference

For validating monster stat blocks, the following PC and enemy benchmarks apply.

### PC HP by Level (approximate ranges)

| Level | Tank (Blood Knight) | Melee DPS | Caster |
|---|---|---|---|
| 1 | 14–15 | 11–12 | 10–11 |
| 5 | 30–31 | 23–24 | 22–23 |
| 10 | 50–51 | 38–39 | 37–38 |
| 15 | 70–71 | 53–54 | 52–53 |
| 20 | 90–93 | 68–71 | 67–70 |

### PC Attack Pools by Level

| Level | Typical Pool | Expected Successes (avg) | Effective Damage/Hit |
|---|---|---|---|
| 1 | 5–6d6 | 1.7–2.0 | 3–6 |
| 5 | 7–8d6 | 2.3–2.7 | 4–7 |
| 10 | 9–11d6 | 3.0–3.7 | 5–8 |
| 15 | 10–13d6 | 3.3–4.3 | 7–13 |
| 20 | 11–14d6 | 3.7–4.7 | 9–15 |

### GM Guide Enemy Benchmarks (Level 5 Party)

| Type | HP | DV | Armor | Attack Pool | Damage |
|---|---|---|---|---|---|
| Minion | 1–2 | 2 | 0 | 5d6 | 2–3 |
| Standard | 14 | 4 | 0–2 | 7d6 | 4–6 |
| Elite | 23 | 6 | 2–3 | 8d6 | 6–8 |
| Boss | 45 | 6+ | 3–4 | 9d6 ×2 atk | 8–12 |

### GM Guide Enemy Benchmarks (Level 10 Party)

| Type | HP | DV | Armor | Attack Pool | Damage |
|---|---|---|---|---|---|
| Minion | 1–2 | 4 | 0 | 10d6 | 2–3 |
| Standard | 24 | 5 | 0–2 | 12d6 | 4–6 |
| Elite | 38 | 8* | 2–3 | 13d6 | 6–8 |
| Boss | 70 | 9* | 3–4 | 14d6 ×2 atk | 8–12 |

> \* DV values above 6 exceed the stated hard cap. The GM Guide formulas produce Elite DV > 6 at level 7+ and Boss DV > 6 at level 5+. This is an **internal inconsistency** that needs resolution — likely by capping base DV at 6 and using armor/reactions/lair effects to increase effective defense.
