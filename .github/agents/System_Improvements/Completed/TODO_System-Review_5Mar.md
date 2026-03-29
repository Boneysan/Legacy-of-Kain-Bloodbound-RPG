# Bloodbound TTRPG — System Review Todo
*Generated from parallel review of GM_Guide, Lore, Player's Handbook, and Monster Manual.*
*Date: 2026-03-05*

---

## Glyphwright Rename Status
✅ **100% complete** across all live game files. One artifact remaining:
- [x] `lore/Class-Lore.md` — Capitalized "**Seekers**" in Glyphwright Rites section. Replace with "Glyphwrights." (lowercase "seekers" in Lattice Vault note is acceptable as a generic noun — optional change to "scholars")

---

## 🔴 Critical — Fix First

### Rules Engine (Player's Handbook)

- [x] **PHB-C1 — Disadvantage example wrong in combat chapter**
  `player's_handbook/09_Combat.md` §9.13 example re-rolls *all* successes instead of half. Correct to: re-roll half (round up), keep un-rerolled successes. (Same error also present in `GM_Guide/01_Running-the-Game.md` §1.2 example at line ~97.)
  **Files:** `player's_handbook/09_Combat.md`, `GM_Guide/01_Running-the-Game.md`

- [x] **PHB-C2 — "Bonus Action" never defined in the combat rules**
  Used 50+ times across class perks, lineage traits, and spells but absent from `09_Combat.md` §9.1 and `12_Glossary.md` §12.3 combat turn definitions. Add one paragraph: *"Bonus Action — only available when a class ability, perk, lineage trait, or spell specifically grants one. A character may take only one Bonus Action per turn."*
  **Files:** `player's_handbook/09_Combat.md`, `player's_handbook/12_Glossary.md`

- [x] **PHB-C3 — "Corruption Paths" referenced but never defined**
  `player's_handbook/01_Character-Creation.md` Step 8 §1.10 tells players to "Choose a Corruption Path" but no Paths are defined anywhere. Either add them or remove/rewrite Step 8.
  **Files:** `player's_handbook/01_Character-Creation.md`, optionally `player's_handbook/08_Corruption.md`

- [x] **PHB-C4 — Short Rest / Long Rest never formally defined**
  Referenced throughout (dozens of perk cost resets, HP/SE/BP recovery). No file defines duration, permitted activities, or exact recovery. Add a rules section to `09_Combat.md` or `12_Glossary.md`.
  **Files:** `player's_handbook/09_Combat.md` or `player's_handbook/12_Glossary.md`

- [x] **PHB-C5 — Class spell access not defined**
  `05_Spellcasting-and-Magic.md` §5.9–5.10 claims class access is in Chapter 3. It isn't. No table maps classes to accessible spell schools. Add a class-to-spell-school access table.
  **Files:** `player's_handbook/05_Spellcasting-and-Magic.md` or `player's_handbook/03_Classes.md`

- [x] **PHB-C6 — Starting skill points contradiction**
  `01_Character-Creation.md` says 6–10 skill points; `03_Classes.md` says 5–6. CONTEXT.md confirms 5–6 as canonical. Correct Ch1 to read 5–6.
  **Files:** `player's_handbook/01_Character-Creation.md`

- [x] **PHB-C7 — Weapon tier names mismatch**
  `07_Equipment.md` defines tiers as Standard → Enhanced → Masterwork. `assets/Character Sheet.md` says Standard → Advanced → Superior. Update Character Sheet to match.
  **Files:** `assets/Character Sheet.md`

- [x] **PHB-C8 — Corrupted Perk cost conflicts (Ch4 vs Ch8)**
  Three confirmed discrepancies:
  - Hylden's Rift: Ch4 = 4 SE; Ch8 = 7 SE
  - Corrupted Ferocity: Ch4 = no SE cost; Ch8 = 2 SE
  - Wraith's Lament: Ch4 = 2 SE; Ch8 = 4 SE
  Ch4 is canonical per CONTEXT. Correct Ch8 values to match, or add a note: *"If values here conflict with Chapter 4, Chapter 4 is authoritative."*
  **Files:** `player's_handbook/08_Corruption.md`

---

### GM Guide

- [x] **GMG-C1 — "Fortitude" attribute in all 6 faction NPC stat blocks**
  "Fortitude" is not a game attribute. All six faction NPC entries in `05_NPC-Compendium.md` §5.8.1–5.8.6 use it instead of "Blood." Also: Seripha and Adamas list combined "Will/Blood" rows — must be split into separate rows.
  Replace all — Commander Malthus, Elder Seripha, Chronicler Adamas, Speaker Vreth, Guildmaster Thessa, Prophet Nakthos.
  **File:** `GM_Guide/05_NPC-Compendium.md`

- [x] **GMG-C2 — HP per level says "4–6" (should be 3–4)**
  `03_Character-Progression.md` §3.5 states "Gain HP based on class (4–6 per level)." Correct value per CONTEXT and PHB Ch3 is 3–4. No class grants +5 or +6.
  **File:** `GM_Guide/03_Character-Progression.md`

- [x] **GMG-C3 — ToC references 4 chapters that don't exist**
  `00_GM-Introduction.md` lists Chapters 6–9 (Corruption Management, Narrative Perks, Campaign Frameworks, Random Tables). None exist as files. Update ToC to list only the 6 real chapters, and mark missing chapters as "Forthcoming" or fold references into the existing chapter that covers that content.
  **File:** `GM_Guide/00_GM-Introduction.md`

---

### Lore / Cross-System

- [x] **LORE-C1 — Turelim described as "seismic voices" in PHB Ch3**
  `player's_handbook/03_Classes.md` class overview table describes Turelim as "warrior-kings with seismic voices." Every other source (Lineage-Lore, Class-Lore, game canon) says **telekinesis**. Correct to "telekinetic force."
  **File:** `player's_handbook/03_Classes.md`

- [x] **LORE-C2 — Warden of Balance called "Part Sarafan, Part Oracle-Blooded" in PHB**
  `player's_handbook/03_Classes.md` Warden lore blurb says "Part Sarafan, part Oracle-Blooded." Class-Lore.md states clearly the Sarafan consider Wardens "soft heretics" and the class is open to any lineage. Rewrite to: *"A Warden of Balance emerges when a person — of any lineage — swears themselves to the concept of the Pillars rather than to any earthly faction."*
  **File:** `player's_handbook/03_Classes.md`

- [x] **LORE-C3 — "Necrotic" damage type in Shadowmancer perks**
  Two Shadowmancer perks use "Necrotic" damage (Level 11 Living Darkness, Level 13 Void Blade). Not a canonical damage type. Replace with **Entropic**.
  **File:** `player's_handbook/03_Classes.md`

- [x] **LORE-C4 — "Physiological Damage" at Soul Reaver Level 19**
  "Physiological Damage" is not a canonical category. Replace with **Physical Damage**.
  **File:** `player's_handbook/03_Classes.md`

- [x] **LORE-C5 — Post-Defiance timeline missing from World-Primer**
  The Timeline of Major Events ends at "Defiance" — the backstory. The game is set *after* Defiance. Add a "Current Era" section (200–400 words) covering: Kain's post-Defiance position, Pillar recovery state, power vacuum in clan politics, Hylden threat level, Elder God's reduced influence.
  **File:** `lore/World-Primer.md`

- [x] **LORE-C6 — Crimson Fracture realm-merging agenda absent from World-Primer**
  Class-Lore.md attributes realm-merging as the Fracture's endgame (they covet Soul Reavers; Hylden Warlocks find common ground with them specifically for this reason). The World-Primer faction entry omits this entirely. Add realm-merging as a faction motive.
  **File:** `lore/World-Primer.md`

- [x] **LORE-C7 — Avernus Cathedral described incompatibly across two files**
  World-Primer: Hash'ak'gik cult stronghold. Class-Lore (Sangromancer Sacred Sites): active pilgrimage destination with the Blood-Well. These need a bridging paragraph: the Blood-Well predates the cult and is in the lower catacombs; the cult controls the upper cathedral. Sangromancers who pilgrimage there navigate active hostile territory.
  **Files:** `lore/World-Primer.md`, `lore/Class-Lore.md`

- [x] **LORE-C8 — Blood Knight section in Class-Lore is a structural stub**
  Every other class entry has 9 sections. Blood Knight has only Common Threads + Using This in Play. Missing: Roleplay Guidance, Factional Ties, Rites and Traditions, Sacred Sites, Famous Blood Knights, Associated Relics. Expand to match the full Class-Lore template.
  **File:** `lore/Class-Lore.md`

---

### Monster Manual

- [x] **MM-C1 — Movement still in tiles across Ch05 and Ch06 (17 entries)**
  Roadmap marked "tiles → feet" as resolved but Ch05 and Ch06 were entirely missed. Apply `1 tile = 5 feet` conversion to all entries: 4 tiles → 20 ft, 5 tiles → 25 ft, 6 tiles → 30 ft, 7 tiles → 35 ft, 9 tiles → 45 ft, 10 tiles → 50 ft.
  **Files:** `Monster_Manual/05_Constructs-and-Automatons.md`, `Monster_Manual/06_Hylden-Forces.md`

- [x] **MM-C2 — Chapter 7 comprehensive format divergence**
  Ch07 uses D&D terminology throughout. Full pass required:
  - `DC X` → `DR X`
  - `Willpower` → `Will`
  - `Perception (Focus)` → `Observation (Focus)`
  - `Arcana (Soul)` → `Forbidden Knowledge (Soul)`
  - Add explicit `DV: X` line to every entry missing it
  - Replace text TV labels ("Major," "Deadly") with numeric values
  - Reformat dice pools from "Fury (6) + 3" to "9d6"
  **File:** `Monster_Manual/07_Elemental-and-Arcane.md`

- [x] **MM-C3 — Non-canonical damage types**
  Reclassify throughout Monster Manual:
  - **Psychic → Spectral** (Ch08, Ch09, Ch06 entries)
  - **Acid → Elemental** (Ch06 Mind-Tethered Abomination)
  - **Poison → Elemental or Entropic** (Ch04 Blightmaw Alpha, Ch03)
  **Files:** `Monster_Manual/06_Hylden-Forces.md`, `Monster_Manual/08_Ancient-Creatures.md`, `Monster_Manual/09_Legendary-Entities.md`, `Monster_Manual/04_Beasts-and-Mutants.md`

- [x] **MM-C4 — Non-canonical status conditions (9 types)**
  Standardize or collapse to canonical conditions:
  - Saddened, Shaken, Poisoned → **Weakened**
  - Confused (Ch05/06 version: "Disadvantage on all rolls") → **Weakened**
  - Confused (Ch02 version: "sees allies as enemies") → **Frightened + Weakened**
  - Branded → keep but define it formally, or rename to a canonical condition note
  - Blight Fever, Disrupted, Unraveled, Soul-Burn → either add to Core status table or replace with canonical equivalents
  **Files:** `Monster_Manual/02_Spectral-Entities.md`, `Monster_Manual/03_Mortals-and-Cultists.md`, `Monster_Manual/04_Beasts-and-Mutants.md`, `Monster_Manual/05_Constructs-and-Automatons.md`, `Monster_Manual/06_Hylden-Forces.md`, `Monster_Manual/07_Elemental-and-Arcane.md`

- [x] **MM-C5 — Bio-Sigil Reaver DV 7 exceeds cap**
  DV formula = 1 + max(Shadow, Will). Bio-Sigil Reaver: Shadow 5, Will 4 → max DV = 6. Change from DV 7 to **DV 6**.
  **File:** `Monster_Manual/06_Hylden-Forces.md`

- [x] **MM-C6 — Moebius referenced as active agent-director (post-Defiance)**
  Ch03 Wandering Mad Seer: *"A few serve as agents of Moebius."* Moebius is dead by post-Defiance. Rewrite to past-tense: *"A few were once agents of Moebius... their minds still bound by enchantments he placed before his death. They serve a dead master's designs without knowing the architect is gone."*
  **File:** `Monster_Manual/03_Mortals-and-Cultists.md`

- [x] **MM-C7 — Chainmaw Demon orphaned reference**
  Ch03 Black Rune Warlock: summons "a Chainmaw Demon (from Demonic chapter)." No Demonic chapter exists. No Chainmaw Demon stat block exists anywhere. Choose one fix:
  (a) Add inline stat block sidebar in Ch03, or
  (b) Replace with an existing TV 1 creature (e.g., Hylden-Possessed Grunt), or
  (c) Rewrite as generic "Abyssal Servant" with simple inline stats.
  **File:** `Monster_Manual/03_Mortals-and-Cultists.md`

- [x] **MM-C8 — Elder God has zero representation in Monster Manual**
  The primary antagonistic cosmic force of the entire series has no entry — no herald, no servant, no manifestation. Add at minimum an "Eye of the Wheel" or "Soul-Plucked Herald" (TV 13–15) and an apex "Elder God Manifestation" (TV 20+) to Ch09.
  **File:** `Monster_Manual/09_Legendary-Entities.md`

---

## 🟡 Medium — Fix Soon

### Player's Handbook

- [x] **PHB-M1 — "Spectral Lore" → "Spectral Navigation" in Soul Reaver key skills**
  `player's_handbook/03_Classes.md` Soul Reaver section lists "Spectral Lore" — skill does not exist. Correct to **Spectral Navigation**.

- [x] **PHB-M2 — "Psychic damage" in Shadowmancer Level 8**
  "Psychic" not in damage categories. Change to **Spectral**. Also uses d6 dice notation (see PHB-M7).

- [x] **PHB-M3 — "Dex Save" in Sangromancer Bloodburst and Glyphwright Seal of Fire**
  D&D terminology. Replace with system-native: **DR 2 Evasion save** (or appropriate DR).

- [x] **PHB-M4 — "Shadow Realm" undefined; used at Shadowmancer Levels 14 and 17**
  Nosgoth has Material and Spectral realms. "Shadow Realm" is a third undefined location. Update to **Spectral Realm** or formally define the Shadow Realm in `player's_handbook/11_Realms-Terrain-Arcane-Power.md`.

- [x] **PHB-M5 — "Investigation" used in Opposed Rolls example in Ch0**
  Not a defined skill. Replace with **Observation** or **Insight**.

- [x] **PHB-M6 — "Perception" used in Blinded status in Ch0 and Ch12**
  Not a defined skill. Replace with **Observation** in both locations.
  **Files:** `player's_handbook/00_Core-Mechanics.md`, `player's_handbook/12_Glossary.md`

- [x] **PHB-M7 — "Fortitude check" for Melchiahim in Ch2**
  Not a defined save type. Based on physical/biological context (bodily decay), replace with **Blood save**.
  **File:** `player's_handbook/02_Lineages-and-Race.md`

- [x] **PHB-M8 — Wraith racial bonus (+1 Will) missing from Ch1 character creation step**
  Ch2 correctly lists +1 Possession, +1 Observation, +1 Will. Ch1 Step 2 only mentions +1 Possession and +1 Observation. Add +1 Will to Ch1.
  **File:** `player's_handbook/01_Character-Creation.md`

- [x] **PHB-M9 — d6 variable damage dice in class perks (inconsistent with fixed-damage system)**
  Several perks use d6 notation (Soul Reaver Spectral Nova: 3d6; Soul Storm: 5d6; Shadowmancer Living Darkness: 1d4 Necrotic; Nightmare Fuel: 1d6 Psychic). System uses fixed damage throughout. Convert to fixed values or note explicitly that these are exceptions.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-M10 — "Presence" skill used but not in skill list (Ch1 and Ch2)**
  `01_Character-Creation.md` §1.5 links Fury to "Presence." Dumahim: "+1 Presence." Melchiahim: "−1 to Presence checks." "Presence" was replaced with "Intimidation" per CONTEXT. Update all three instances.
  **Files:** `player's_handbook/01_Character-Creation.md`, `player's_handbook/02_Lineages-and-Race.md`

- [x] **PHB-M11 — "H:" label instead of "Human:" in Ch1 §1.3**
  Copy-paste artifact. Replace "H:" with "Human:".
  **File:** `player's_handbook/01_Character-Creation.md`

- [x] **PHB-M12 — "Void Walker" name collision (class perk vs. universal perk)**
  Soul Reaver Level 10 perk and Tier 2 Universal Perk share the name "Void Walker" with completely different effects. Rename one.
  **Files:** `player's_handbook/03_Classes.md`, `player's_handbook/04_Perks.md`

- [x] **PHB-M13 — "Assassinate" used at Dreadblade Levels 6 and 10 with different effects**
  Two different abilities with the same name in the same class's perk tree. Rename the Level 10 version to something distinct (e.g., "Master Assassinate" or "Perfect Kill").
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-M14 — Ch10 Initiative omits the Concentration alternative**
  Ch0, Ch9, Ch12 all allow Shadow + Tactics OR Shadow + Concentration for initiative. Ch10 §10.4.1 lists only Shadow + Tactics. Add the Concentration option.
  **File:** `player's_handbook/10_Dice-System.md`

- [x] **PHB-M15 — Shadowmancer Level 20 capstone doesn't fit class identity**
  "Avatar of Zephon: Transform into giant spider-monster" doesn't match the Shadowmancer's established identity as a shadow-weaver and psychological manipulator. Redesign capstone as a shadow apotheosis (becoming an entity *of* darkness) rather than a physical bestial transformation.
  **File:** `player's_handbook/03_Classes.md`

### GM Guide

- [x] **GMG-M1 — Boss/Elite TV formula conflicts with sample encounter numbers**
  Section 2.2 defines per-level scaling TV formula. Sample encounters in §2.10 use flat TV values. These don't match. Pick one system and apply consistently to both the formula and all worked examples.
  **File:** `GM_Guide/02_Encounter-Design.md`

- [x] **GMG-M2 — Cover/terrain modifiers use "DR" instead of "DV"**
  §2.4 says elevated terrain and cover grant "+1 DR." DR is difficulty for skill checks — attacks target DV. Replace all three instances with "+1 DV."
  **File:** `GM_Guide/02_Encounter-Design.md`

- [x] **GMG-M3 — Corruption thresholds missing named labels and Level 0 distinction**
  §1.5 collapses 0–2 into one tier labeled "Untouched." CONTEXT defines 0 as "Uncorrupted" and 1–2 as "Touched by Corruption" (with distinct roleplaying effects). Also missing named tier labels: Touched by Corruption, Marked by Corruption, Deeply Corrupted, Abyss-Bound.
  **File:** `GM_Guide/01_Running-the-Game.md`

- [x] **GMG-M4 — "Martyr's Fury" ability gives "+1 DV to attacks" — mechanically incoherent**
  DV is a defensive stat. "+1 DV to all attacks" means nothing. The intent is clearly "+1 die to attack rolls." Fix the ability text.
  **File:** `GM_Guide/05_NPC-Compendium.md`

- [x] **GMG-M5 — "Presence Check" references a non-existent stat**
  `04_Economy-and-Resources.md` §4.9 Scenario 2 references a "Presence check." No such attribute or skill exists. Replace with Will + Intimidation (or equivalent per context).
  **File:** `GM_Guide/04_Economy-and-Resources.md`

- [x] **GMG-M6 — NPC "DR" stat row is undefined in stat block format**
  All faction NPCs in §5.8 include a "DR" row alongside DV. DR is not a creature property in this system. Clarify what this row means (save DC for this creature's abilities?) or remove it and move the information into individual ability descriptions.
  **File:** `GM_Guide/05_NPC-Compendium.md`

- [x] **GMG-M7 — Minion HP range contradiction (1–2 vs. MM standard 3–6)**
  §2.2 Quick Enemy Stats sets Minion HP = 1–2. Monster Manual Introduction uses 3–6 as the canonical range. Align to match.
  **File:** `GM_Guide/02_Encounter-Design.md`

### Lore

- [x] **LORE-M1 — "Razielite Exception" vs. "Razielite Martyrdom" — no cross-reference**
  Lineage-Lore.md frames "Razielite" as a vampire theological debate; World-Primer frames "Razielite Martyrdom" as a human mortal faith. Both can coexist but neither acknowledges the other. Add a cross-reference sentence to each.
  **Files:** `lore/Lineage-Lore.md`, `lore/World-Primer.md`

- [x] **LORE-M2 — Hash'ak'gik absent from Class-Lore and Lineage-Lore**
  A significant faction in World-Primer with no mention in either class or lineage docs. Add:
  - Sangromancer (Class-Lore): note that the Blood-Well pilgrimage site is Hash'ak'gik's territory
  - Hylden Warlock (Class-Lore): note that even Hylden Remnants recognize it as a rival
  - Lineage-Lore Revenants: note that Vessels are a specific threat to Revenants
  **File:** `lore/Class-Lore.md`

- [x] **LORE-M3 — Blood Knight telekinesis in Class-Lore has zero mechanical representation**
  Class-Lore lists "Mastery of Telekinesis (Turelim heritage)" as a Blood Knight common thread. No telekinetic ability exists in the Level 1–20 perk tree. Either add a telekinetic ability or update the Class-Lore to note it is a heritage trait rather than a playable mechanic.
  **Files:** `lore/Class-Lore.md`, `player's_handbook/03_Classes.md`

- [x] **LORE-M4 — Revenants and Unbound absent from World-Primer faction entries**
  No faction entry addresses its relationship to Revenants or Unbound as a lineage group (e.g., does Elder God Cult pursue Revenant souls? Do Guilds employ Unbound?). Add brief faction notes for each.
  **File:** `lore/World-Primer.md`

- [x] **LORE-M5 — Defiant Creed (Kainite Heresy) isolated in World-Primer Religions**
  Described as a living underground movement but has no leadership structure, headquarters, or faction alignment in the Key Factions section. Absent from Class-Lore faction tables. Add minimal cross-referencing or expand into a formal faction entry.
  **File:** `lore/World-Primer.md`

- [x] **LORE-M6 — Lattice Vault "secretive academy" mentioned but never developed**
  Class-Lore Glyphwright Sacred Sites describes a cooperative human-vampire academy "maintained for centuries" — politically sensitive and narratively significant, but has no name, leadership, or faction entry anywhere.
  **Files:** `lore/Class-Lore.md`, optionally `lore/World-Primer.md`

### Monster Manual

- [x] **MM-M1 — "Perception" and "Arcana" skills still present in Ch08**
  Stone-Chime Oracle, Titan-Kin Stalker, and Relic-Watcher Colossus use non-canonical skill names. Replace: Perception → **Observation**, Arcana → **Forbidden Knowledge**.
  **File:** `Monster_Manual/08_Ancient-Creatures.md`

- [x] **MM-M2 — "Agility" used as a save attribute in Ch08**
  Relic-Watcher Colossus and Stone-Chime Oracle use "Agility DR 15" saves. "Agility" is not an attribute. Replace with Shadow or Blood save as appropriate.
  **File:** `Monster_Manual/08_Ancient-Creatures.md`

- [x] **MM-M3 — DV missing from most Ch07–09 entries**
  DV is a required field per Ch00 format. Add explicit DV lines to all entries in Ch07 and the Legendary Entities missing them in Ch09.
  **Files:** `Monster_Manual/07_Elemental-and-Arcane.md`, `Monster_Manual/09_Legendary-Entities.md`

- [x] **MM-M4 — Loot currency inconsistency across chapters**
  Ch01/02 use "barter value"; Ch03–07 use "Trade Value: X supplies"; Ch08–09 omit currency entirely. Standardize to one format across all chapters.
  **Files:** All Monster Manual chapters

- [x] **MM-M5 — "DR" as creature stat in Ch05/06**
  Several entries list `Difficulty Rating (DR): X` as a creature property (e.g., "DR: 5 Physical saves, 4 Magical saves"). DR is a task-difficulty number, not a creature attribute. Clarify meaning or replace with a defined field: e.g., "Save DR: X (for saves made against this creature's abilities)."
  **Files:** `Monster_Manual/05_Constructs-and-Automatons.md`, `Monster_Manual/06_Hylden-Forces.md`

- [x] **MM-M6 — Revenant PC lineage disambiguation missing from Ch01**
  Ch01 Nosgothian Revenant describes mindless goal-driven undead. "Revenant" is also a playable PC lineage. Add a callout: *"Note: Playable Revenant characters (PHB Ch02) are sapient beings who retain full faculties. This entry represents a mindless variant."*
  **File:** `Monster_Manual/01_Undead-and-Vampiric.md`

- [x] **MM-M7 — TV 5–8 gap (zero creatures for this tier)**
  Monster Manual jumps from TV 4 (Ch01–06 bosses) directly to TV 9 (Ch07). Six threat levels representing mid-level play (~Levels 8–13) have no purpose-built creatures. Create or designate bridge entries.
  **Files:** New content addition to appropriate chapters

- [x] **MM-M8 — Vorador absent from Ch09**
  The "First of the Turned" and most powerful canonical vampire in the setting is explicitly requested in the Roadmap (TV 18–19) but absent. Add an entry for Vorador the Patriarch.
  **File:** `Monster_Manual/09_Legendary-Entities.md`

---

## 🟢 Low / Polish / Balance Flags

### Player's Handbook

- [x] **PHB-L1 — Blood Knight "Life Drain" has no usage cap**
  Passive unlimited melee healing, stacking with Level 14 and Level 17 upgrades, creates near-invulnerability in sustained melee. No other class has an equivalent. Consider adding a per-round or per-scene cap, or note it as an intentional design choice.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L2 — Wraith lineage uniquely grants an attribute bonus (+1 Will) at creation**
  All other lineages grant only skill bonuses. +1 Will cascades into DV and SE max. Combined with Wraith Phasing, this lineage appears strongest at creation. Review for rebalance.
  **File:** `player's_handbook/02_Lineages-and-Race.md`

- [x] **PHB-L3 — Unbound has three distinct mechanics; others have one or two**
  Immunity to fate effects + Probability Shift + Bonus Action teleport 20ft/session. Teleport especially powerful given it matches or exceeds SE-costed class abilities. Review for rebalance.
  **File:** `player's_handbook/02_Lineages-and-Race.md`

- [x] **PHB-L4 — Shadowmancer Level 17 "Death from Below" — instant kill, no save listed**
  Kills any non-boss regardless of HP for 5 SE with no save. Add a save (e.g., DR 3 Soul save) or an HP threshold condition.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L5 — Critical Hit frequency becomes routine at Level 20**
  Level 20 high-investment attacker: 14 dice. DV cap 6 = 8+ successes = crit. Probability well above 50%. May or may not be intentional — note this as a design decision to review.

- [x] **PHB-L6 — "Contemplation" purification method absent from Ch8**
  Ch12 §12.6 lists 4 purification methods including "Contemplation." Ch8 §8.6 lists only 3 (Contemplation missing). Add Contemplation to Ch8.
  **File:** `player's_handbook/08_Corruption.md`

- [x] **PHB-L7 — Hylden Warlock lore error: "escaped from the Spectral Realm"**
  Hylden were banished to the Demon Dimension, not the Spectral Realm. The Spectral Realm is the vampire afterlife/wraith space.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L8 — "Sanguine Transfiguration" description is vague**
  Sangromancer Level 9: "Increase speed, heal Soul attr HP." No values given. Add specific speed increase amount/duration and clarify if "Soul attr HP" = heal HP equal to Soul attribute value.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L9 — Hylden Warlock Level 8 "Ritual of Pain" has no mechanics**
  "Sacrifice HP to deal extra Damage — Free Action." No HP amount, no damage amount, no target, no duration. Add values.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L10 — Blood Knight Level 5 "Crushing Blow" uses non-standard save phrasing**
  "Target: Blood vs Difficulty 3" should be formatted as "DR 3 Blood save."
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L11 — Blood Knight missing "Blood Sense" from key skills**
  Blood Sense is Ch6-described as "peerless for hunting in total darkness" and core to vampiric hunter identity. Not listed in Blood Knight key skills despite being thematically central.
  **File:** `player's_handbook/03_Classes.md`

- [x] **PHB-L12 — Rahabim "alchemical moisturizers" not listed in equipment**
  The Rahabim vulnerability mitigation item is mentioned in Ch2 but not in Ch7 (no cost, availability, or crafting requirements).
  **Files:** `player's_handbook/02_Lineages-and-Race.md`, `player's_handbook/07_Equipment.md`

- [x] **PHB-L13 — Character Sheet "Armor (Flat DR)" uses incorrect terminology**
  "DR" in this system means Difficulty Rating for skill checks. Armor is flat damage reduction, not a DR. Rename to "Armor (Flat Damage Reduction)."
  **File:** `assets/Character Sheet.md`

### GM Guide

- [x] **GMG-L1 — Milestone pacing checklist oversimplifies tier-specific guidance**
  §3.12 Quick Reference Checklist says "3–5 sessions since last milestone." §3.3 gives tier-specific guidance (every 2–4 sessions L1–5; 3–5 sessions L6–15; 4–6 sessions L16–20). Update checklist to reflect all three bands.
  **File:** `GM_Guide/03_Character-Progression.md`

- [x] **GMG-L2 — Quick enemy templates have no attribute values for contested skill checks**
  Minion/Standard/Elite/Boss templates in §2.2 provide HP/DV/Armor/Attacks but no attributes. GMs have no pool for resolving PC vs. NPC social or skill contests. Add: "Save/contested checks: pool equal to half party level."
  **File:** `GM_Guide/02_Encounter-Design.md`

- [x] **GMG-L3 — Suffocation uses seconds rather than rounds**
  §1.9: "Will × 10 seconds." In a round-based system, tracking seconds is awkward. Suggest: "Will × 2 rounds before DR checks begin."
  **File:** `GM_Guide/01_Running-the-Game.md`

- [x] **GMG-L4 — "Blood Frenzy" immunity on Adamas uses class-specific term ambiguously**
  "Immune to Blood Frenzy" could refer to the Blood Knight class ability or the vampiric death-frenzy state. Clarify: "immune to vampiric frenzy (the involuntary combat state triggered at 0 HP)."
  **File:** `GM_Guide/05_NPC-Compendium.md`

- [x] **GMG-L5 — Kain's current status description reads as pre-Defiance**
  §5.2 describes Kain as "Wandering specter, more legend than ruler." Post-Defiance Kain wields the purified Soul Reaver and is actively working to restore Nosgoth — not passive or spectral. Update description to reflect his post-Defiance active role.
  **File:** `GM_Guide/05_NPC-Compendium.md`

- [x] **GMG-L6 — NPC abilities use undefined "saves" phrasing**
  Multiple NPCs say "advantage on saves vs. fear, charm, and Corruption effects" without naming the attribute + skill pool. Specify (e.g., "Will + Concentration checks vs. fear and charm").
  **File:** `GM_Guide/05_NPC-Compendium.md`

### Lore

- [x] **LORE-L1 — "Sarafan historically wiped out by Kain" — imprecise canon**
  More accurately: the Sarafan as a formal military theocracy predates Kain; Kain destroyed the Sarafan Lord in Blood Omen 2; the original Sarafan knights were killed during Raziel's time period. Revise to a more accurate summary.
  **File:** `lore/World-Primer.md`

- [x] **LORE-L2 — Wraith Anchor has no mechanical representation**
  Central to Lineage-Lore (Fading = Wraith equivalent of death) but no mechanics in PHB Ch2. Add a light rule: designate one anchor object/location/NPC; if destroyed without replacement, DR 2 Will check per session; failure = +1 Corruption.
  **Files:** `lore/Lineage-Lore.md`, `player's_handbook/02_Lineages-and-Race.md`

- [x] **LORE-L3 — Hall of Equilibrium has no location or World-Primer entry**
  A Warden sacred site described in Class-Lore with no geographic anchor and no presence in Key Locations. Add a brief note or location reference.
  **File:** `lore/Class-Lore.md`

- [x] **LORE-L4 — Class-Lore TOC formatting: Hylden Warlock line runs on**
  `- Hylden Warlock- Inter-Class Tensions` — missing space before hyphen.
  **File:** `lore/Class-Lore.md`

### Monster Manual

- [x] **MM-L1 — Void-Spoken Oracle Prophecy Sight is uncapped**
  Permanent Advantage on *all* defense rolls at TV 4. Functionally invulnerable without specific counters. Cap to once per round (reaction-triggered).
  **File:** `Monster_Manual/06_Hylden-Forces.md`

- [x] **MM-L2 — Kain's Echo-Knight Rewrite economy (13 forced rerolls/encounter)**
  Rewrite ability costs 6 SE from an 80 SE pool. Change to: 3/encounter at 0 SE; or reduce SE pool to 30; or increase cost to 15 SE per use.
  **File:** `Monster_Manual/09_Legendary-Entities.md`

- [x] **MM-L3 — Hylden Rift Engineer and Flesh Architect overtuned for TV 2**
  Rift Engineer: 11d6 attack pool at TV 2 (matching TV 15+ entities). Flesh Architect: 10d6.
  Reduce Dimensional Manipulation from 5 to 3; reduce Flesh Architect Biomancy from 5 to 3.
  **File:** `Monster_Manual/06_Hylden-Forces.md`

- [x] **MM-L4 — "Cannot be turned" on Sluagh Tide uses D&D terminology**
  "Turn" is not defined in this system. Replace with: "immune to Radiant-based banishment attempts."
  **File:** `Monster_Manual/02_Spectral-Entities.md`

- [x] **MM-L5 — Titan-Kin Stalker attacks with Stealth as its attack skill**
  Attack pool: Shadow + Stealth = 10d6. Stealth is concealment/evasion, not offense. Replace with Fury + Weapon Mastery or Shadow + Weapon Mastery.
  **File:** `Monster_Manual/08_Ancient-Creatures.md`

- [x] **MM-L6 — Crimson Fracture has no creature representation**
  A major World-Primer faction with zero stat blocks. Add at minimum: Fracture Zealot (TV 1), Fracture Dimension-Walker (TV 3), Fracture Void-Touched (TV 4 Boss).
  **File:** `Monster_Manual/01_Undead-and-Vampiric.md` or new entries

- [x] **MM-L7 — No aquatic creatures in the entire Monster Manual**
  Nosgoth has rivers, subterranean lakes, flooded ruins, and the entire Rahabim clan. Zero aquatic entries.
  **File:** `Monster_Manual/04_Beasts-and-Mutants.md` (new content)

- [x] **MM-L8 — No clan-identified vampire variants in Ch01**
  Every vampire in Ch01 is generic. Basic clan template sidebars (one per clan) would greatly improve lore density and combat variety.
  **File:** `Monster_Manual/01_Undead-and-Vampiric.md`

- [x] **MM-L9 — Blood Moon Prophet lore is vague**
  Roadmap flags this as unresolved. "A seer bound to cycles of red light" has no franchise connection. Add a specific lore anchor tying the Blood Moon to Nosgoth's history.
  **File:** `Monster_Manual/09_Legendary-Entities.md`

- [x] **MM-L10 — "Arcane Lore" skill referenced in Ch05 repair checks**
  Glyphfused Automaton: "Focus + Arcane Lore, DR 4." Canonical skill is **Forbidden Knowledge**.
  **File:** `Monster_Manual/05_Constructs-and-Automatons.md`

- [x] **MM-L11 — Hylden physical presence in Ch06 is ambiguous**
  Some Ch06 entries describe Hylden with native corporeal physiology; lore establishes they interact via possession and constructs post-banishment. Add a clarifying intro paragraph to Ch06 explaining what these creatures are (possessed hosts, fabricated constructs, or dimensional projections).
  **File:** `Monster_Manual/06_Hylden-Forces.md`

---

## Execution Notes

- **Highest priority starting points:** PHB-C1 (Disadvantage fix — affects every table session), PHB-C2 (Bonus Action definition), GMG-C1 (Fortitude → Blood fix), LORE-C8 (Blood Knight stub), MM-C1 (tiles fix), MM-C2 (Ch07 format pass).
- **Single-line fixes that can be batched:** PHB-M5, PHB-M6, PHB-M11, LORE-L4, MM-C5.
- **New content needed:** LORE-C5 (post-Defiance timeline), LORE-C8 (Blood Knight full entry), MM-C8 (Elder God entry), MM-M7 (TV 5–8 creatures), MM-M8 (Vorador).
- **Design decisions required before fixing:** PHB-M15 (Shadowmancer capstone redesign), PHB-L1 (Life Drain cap), PHB-L3 (Unbound rebalance), PHB-C5 (spell access table design).
- **Source-Docs/Main-Rules:** Do not edit. Archive only.

---

*Total items: ~80 across all severity levels.*
*Generated from 4-agent parallel review — March 5, 2026.*
