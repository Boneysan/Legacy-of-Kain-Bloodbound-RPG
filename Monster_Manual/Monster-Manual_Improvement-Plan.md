# Monster Manual Improvement Plan

## Purpose

This document captures the highest-value improvements needed in the Monster Manual so creature design, encounter budgeting, and chapter presentation all follow one coherent standard.

The immediate goal is not to rewrite every creature at once. The goal is to remove the contradictions that make Threat Value, encounter math, and boss balance unreliable.

---

## Implementation Status

### Completed in first pass

1. **Encounter math language aligned**
    - `GM_Guide/02_Encounter-Design.md` now defines enemy TV as a printed absolute encounter-budget number.
    - `Monster_Manual/00_Introduction.md` now matches that model.

2. **Core contradiction removed**
    - Threat tiers remain as benchmark descriptors.
    - Printed creature TV is now treated as the value added directly to encounter totals.

3. **Early outlier corrections applied**
    - `Monster_Manual/03_Mortals-and-Cultists.md`
       - Sarafan Grand Inquisitor reduced to fit TV 4 more cleanly.
       - Sarafan Footsoldier reduced to a truer TV 0.25 minion profile.
       - Witch-Hunter Raid sample encounter corrected.
    - `Monster_Manual/01_Undead-and-Vampiric.md`
       - Fracture Void-Touched encounter total corrected.
    - `Monster_Manual/02_Spectral-Entities.md`
       - Grand Arcanist TV 4 scaling option reduced to fit boss action economy better.
    - `Monster_Manual/06_Hylden-Forces.md`
       - Void-Spoken Oracle sample encounter total corrected.

4. **Second-wave tuning applied**
    - `Monster_Manual/01_Undead-and-Vampiric.md`
       - Bonelord Archon encounter math corrected from TV 8 to TV 10.
    - `Monster_Manual/04_Beasts-and-Mutants.md`
       - Blightmaw Matriarch boss scaling reduced to keep its summon package inside TV 4 expectations.
    - `Monster_Manual/05_Constructs-and-Automatons.md`
       - Pillar-Forged Warden boss scaling reduced by trimming HP, shielding, zone pressure, and Legendary Resistance.
    - `Monster_Manual/06_Hylden-Forces.md`
       - Hylden Arch-Priest boss scaling reduced by limiting summon volume and persistence.

5. **Third-wave tuning applied**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Wight Lord TV 4 scaling reduced by lowering HP and making command output more expensive.
   - `Monster_Manual/02_Spectral-Entities.md`
      - Abyssal Revenant TV 4 scaling reduced by trimming HP, Legendary Resistance, and the duration/radius of Abyssal Gate.
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Master Glyphfused Automaton TV 4 scaling reduced by trimming added HP, death burst size, and legendary-action volume.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Master Rift Engineer TV 4 scaling reduced by trimming extra summons, reducing storm footprint, and lowering legendary-action economy.

6. **Fourth-wave tuning applied**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Grave-Knight Warlord TV 4 scaling reduced by trimming HP, legendary resistance, and command radius.
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Veteran Clockwork Knight TV 4 scaling reduced by changing army-wide command output into single-target support.
      - Alpha Iron-Cage Beast TV 4 scaling reduced by shrinking bonus HP and limiting coordinated attacks to one allied beast.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Master Flesh Architect TV 4 scaling reduced by cutting summon volume, reducing mass debuff reach, and making Flesh Harvest more expensive in legendary-action economy.

7. **Fifth-wave tuning applied**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Deathguard Champion TV 4 scaling reduced by trimming charge reach and damage.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Hylden Warlord TV 4 scaling reduced by converting army-wide Advantage into narrower single-target command support.
      - Master Bio-Sigil Reaver TV 4 scaling reduced by cutting added HP, lowering legendary-action volume, and soft-capping its double-strike burst.
      - Veteran War-Stalker TV 4 scaling reduced by trimming HP, SE, damage, Corruption certainty, and Bone-Breaker duration.

8. **Sixth-wave tuning applied**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Bonelord Acolyte TV 4 scaling reduced by trimming HP and SE while keeping its reduced summon profile.
      - Vampire Beast Lord TV 4 scaling reduced by cutting base HP, reducing commanded ghoul volume, and explicitly limiting its legendary-action budget.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Master Horror Warden TV 4 scaling reduced by shrinking fear radius, lowering save pressure, and making Mind Spike a more expensive legendary-action option.
      - Rift Archon TV 4 scaling reduced by trimming HP and reducing the number of summoned grunts.

9. **Seventh-wave tuning applied**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Fracture Void-Touched boss package reduced by trimming Legendary Resistance and limiting extra zealot summoning.
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Master Restoration Engine TV 4 scaling reduced by trimming healing throughput, SE, and shield support efficiency.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Hylden Rift Commander TV 4 scaling reduced by trimming HP, SE, and the number of grunts produced by downgraded Rift Command.

10. **Eighth-wave tuning applied**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
      - Witch-Hunter General TV 4 scaling reduced by shrinking anti-magic reach and trimming legendary-action volume.
      - Master Rune-Forger TV 4 scaling reduced by lowering HP, SE, glyph saturation, and one-shot battlefield detonation volume.
   - `Monster_Manual/04_Beasts-and-Mutants.md`
      - Elder Drake TV 4 scaling reduced by trimming bonus HP, narrowing upgraded breath coverage, and making fear output more expensive in legendary-action economy.
      - Berserker Troll TV 4 scaling reduced by lowering bonus HP, softening bloodied-mode burst, and making Ground Slam costlier as off-turn pressure.

11. **Ninth-wave tuning applied**
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Pillar-Forged Warden TV 4 scaling reduced by lowering shield sustain and preventing off-turn Glyph Pulse spam when the ability is not recharged.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Master Rift Engineer TV 4 scaling reduced by capping the quality of repeated summons, trimming storm coverage, and removing extra off-turn rift generation.
      - Hylden Arch-Priest TV 4 scaling reduced by lowering total grunt output from both Dimensional Tether and Permanent Rift.

12. **Tenth-wave tuning applied**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
      - Archwarlock of the Black Rune TV 4 scaling reduced by trimming bonus HP, softening Mass Curse from full disadvantage to a narrower penalty, and limiting extra demon reinforcement.
      - Complete Turning TV 4 scaling reduced by trimming HP and regeneration.
   - `Monster_Manual/04_Beasts-and-Mutants.md`
      - Apex Warptooth TV 4 scaling reduced by lowering bonus HP, cutting peak attack count, and making its strongest off-turn leap more expensive.
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Master Restoration Engine TV 4 scaling reduced again by trimming durability, SE, burst healing, and the ceiling on emergency restoration.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Rift Archon TV 4 scaling reduced by trimming HP, reducing rift radius, and lowering grunt output.

13. **Eleventh-wave tuning applied**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
      - Greater Vessel TV 4 scaling reduced by trimming bonus HP and narrowing Possession Cascade from a broad crowd effect into a smaller-target package.
   - `Monster_Manual/04_Beasts-and-Mutants.md`
      - Ancient Bramblehide TV 4 scaling reduced by trimming bonus HP, lowering burst damage, and making its fear output more expensive and shorter-ranged.
      - Blightmaw Matriarch TV 4 scaling reduced by trimming HP, requiring Toxic Spray to respect recharge timing, and lowering summoned brood count.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Hylden Warlord TV 4 scaling reduced again by softening its command bonus and shortening the support radius.

14. **Twelfth-wave tuning applied**
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Veteran Clockwork Knight TV 4 scaling reduced again by trimming bonus HP and making Shield Wall compete more directly with its attack economy.
      - Master Glyphfused Automaton TV 4 scaling reduced again by lowering bonus HP and softening its death-burst radius and damage.

15. **Schema normalization started**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
      - Standardized the late Chapter 3 entry block (`Sarafan Footsoldier`, `Sarafan Outrider`, `Commoner`, and `Rune-Forger`) to match the chapter's primary metadata and heading schema.
      - Collapsed separate `Threat Tier` and `Threat Value` lines into the chapter's more common combined format and aligned section headings back to the `####` pattern used through most of the file.

16. **Second schema-normalization pass applied**
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Standardized the late Chapter 5 construct block (`Rune-Forged Warden`, `Restoration Engine`, `Glyph Spider`, and `Animated Ward`) toward the chapter's more common combined threat-line format.
      - Kept the existing section hierarchy intact while removing the most visible metadata-format drift.

17. **Schema pass status**
   - The first two consistency passes were intentionally localized to late-added entry blocks, where chapter-internal formatting drift was most visible.
   - `Monster_Manual/03_Mortals-and-Cultists.md` now has a cleaner final block that matches the chapter's dominant `####` heading style and combined threat-line format.
   - `Monster_Manual/05_Constructs-and-Automatons.md` now has its late construct block using the same combined threat metadata approach as the surrounding entries.

18. **Schema normalization — Chapters 4 and 6 completed**
   - `Monster_Manual/04_Beasts-and-Mutants.md`
      - Blightmaw Alpha: collapsed split `Threat Tier` / `Threat Value (TV)` lines into `**Threat Tier**: Elite (TV 3)`.
      - Nosgothian Alpha Wyrm: collapsed split lines into `**Threat Tier**: Legendary (TV 7)`.
   - `Monster_Manual/06_Hylden-Forces.md`
      - Hylden Rift-Priest: collapsed into `**Threat Tier**: Elite (TV 3)`.
      - Hylden-Possessed Grunt (duplicate late entry): collapsed into `**Threat Tier**: Minion (TV 0.25)`.
      - Hylden Dimension Lord: collapsed into `**Threat Tier**: Legendary (TV 8)`.
   - All split `Threat Tier` / `Threat Value (TV)` metadata in Chapters 3–6 is now normalized.

19. **P3 terminology: DC → DR fixed**
   - `Monster_Manual/07_Elemental-and-Arcane.md`: all `DC N` save-difficulty references replaced with `DR N` (the game's canonical term). 12 instances corrected.
   - `Monster_Manual/09_Legendary-Entities.md`: all `DC N` references replaced with `DR N`. 7 instances corrected.
   - `Monster_Manual/08_Ancient-Creatures.md` was already using `DR` consistently and required no changes.
   - Chapters 1–6 were already using `DR` consistently.

20. **GM Guide sample encounters aligned to Monster Manual**
   - `GM_Guide/02_Encounter-Design.md` section 2.10 updated.
   - Section header rewritten to explain the relationship between bespoke examples and MM entries.
   - Each encounter now includes a `MM Cross-reference` block pointing to the closest named MM entries and chapters.
   - Each encounter now also includes an **All-MM equivalent** composition showing how to rebuild the encounter using only published creature entries at their printed TVs.

21. **P3 schema normalization — complete across all nine chapters**
   - **Ch7–9 old-format conversion:** All creature stat blocks in Chapters 7, 8, and 9 converted from the old `Health`/`Resources`/`Size/Type` format to the canonical `HP`/`DV`/`Type` format matching Chapters 1–6.
      - `**Size/Type:**` → `**Type:**` across all three chapters.
      - `**Threat Value:** N (Label)` → `**Threat Tier:** Label (TV N)` (flat merged line).
      - Bulleted/inline Attributes → `- **Attributes:** Fury N, Soul N, Shadow N, Will N, Focus N, Blood N`.
      - Resources block (`Health`/`SE`/`BP`/`Armor`) → flat Statistics list with `HP`, `DV`, `Armor`, `SE`, `BP`, `Initiative`, `Movement`.
      - Immunities, Resistances, and Vulnerabilities separated into standalone lines.
      - Skills converted from total dice pool to rank only.
      - Movement converted from `N (type)` to `N×5 feet (N squares)`.
      - `### Statistics` section header added to each converted block.
      - Orphaned duplicate stat block (Arcane Flare Wyrm duplicate in Ch7) deleted.
   - **Already-normalised entries in Ch7–9 fixed:** Four entries per chapter that were partially normalised gained merged Threat lines and `- **Initiative:** N` fields.
   - **Ch1–6 Threat Tier merge:** Python regex pass merged all remaining split `**Threat Tier:**` / `**Threat Value (TV):**` line pairs into the single `**Threat Tier:** Label (TV N)` format across all six chapters.
   - **Initiative added — all 127 creatures across Chapters 1–9** now have a `- **Initiative:** N` stat-block field, inserted after the Armor line.
      - Ch1: 18 creatures. Ch2: 11. Ch3: 17. Ch4: 10. Ch5: 12. Ch6: 12. Ch7: 13. Ch8: 12. Ch9: 15.
      - Initiative is derived as Shadow + estimated Tactics rank; high-speed or temporal creatures bias higher.
   - **Scaling Options health terminology:** 11 occurrences of `Increase/Reduce Health to` in Ch7 Scaling Options replaced with `Increase/Reduce HP to`. Ch8–9 were already using `HP`.
   - **Verification pass:** Automated check confirmed zero remaining `**Size/Type:**`, `**Resources:**`, split `**Threat Value (TV):**`, or `Increase Health` fields across all nine chapters.

22. **Heading-depth normalization — complete across all nine chapters**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
   - `Monster_Manual/04_Beasts-and-Mutants.md`
   - `Monster_Manual/05_Constructs-and-Automatons.md`
   - `Monster_Manual/06_Hylden-Forces.md`
      - All creature-entry subsection headings normalized from `####` to `###` to match the dominant chapter pattern used elsewhere in the manual.
   - `Monster_Manual/02_Spectral-Entities.md`
      - One stray late-entry `#### Loot` heading corrected to `### Loot`.
   - Result: creature-entry subsection heading depth is now consistent across Chapters 1–9.

23. **Auxiliary Health → HP cleanup — Chapters 7–9 completed**
   - `Monster_Manual/07_Elemental-and-Arcane.md`
      - Anchor/object references, temporary-HP wording, and late scaling text normalized from `Health` to `HP`.
   - `Monster_Manual/08_Ancient-Creatures.md`
      - Auxiliary regeneration, shard/anchor object references, and scaling shorthand normalized from `Health` to `HP`.
   - `Monster_Manual/09_Legendary-Entities.md`
      - All weakened-form variants, the Elder God true-manifestation setpiece, and the remaining `full health` prose reference normalized to `HP`.
   - Result: Chapters 7–9 now contain no remaining `Health` wording; auxiliary prose and scaling text match the canonical `HP` terminology.

24. **Chapter 5 TV conversion — complete**
   - `Monster_Manual/05_Constructs-and-Automatons.md`
      - Converted the remaining benchmark-era Chapter 5 entries to final absolute TVs aligned to their printed level bands: `Spellbound Golem`, `Bound-Logic Scribe`, `Obsidian Drone`, `Glyph Spider`, and `Animated Ward`.
      - Earlier in the pass, the chapter's high-tier setpiece entries were already converted: `Sarafan Clockwork Knight`, `Pillar-Guardian Sentinel`, `Iron-Cage Beast`, `Glyphfused Automaton`, `Hylden Soul-Tower`, `Rune-Forged Warden`, and `Restoration Engine`.
      - Updated all directly related scaling options, encounter-design examples, sample encounter totals, and the ally-role reference table so the chapter now uses one TV dialect throughout.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated the encounter-design note so it now reflects Chapter 5 as fully converted while other early chapters remain in transition.
   - Result: Chapter 5 now uses final absolute TV values consistently across all of its creature entries and internal examples.

25. **Chapter 1 TV conversion — complete**
   - `Monster_Manual/01_Undead-and-Vampiric.md`
      - Added concrete recommended level bands to the chapter's base creatures and converted all benchmark-era printed TVs to final absolute TVs aligned to those bands.
      - Updated Chapter 1 scaling options, summon references, and encounter-design examples so the chapter now uses one absolute-TV dialect throughout.
      - Removed the chapter's remaining benchmark-era boss-action wording where the text was describing generic role expectations rather than printed creature TV.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated encounter-design notes and Ch1 sample cross-references to reflect Chapter 1 as fully converted.
   - `Monster_Manual/00_Introduction.md`
      - Updated the manual-wide conversion-state note so it now includes Chapter 1 among the fully converted chapters.
   - Result: Chapter 1 now uses final absolute TV values consistently across all of its creature entries and internal examples.

26. **Chapter 2 TV conversion — complete**
   - `Monster_Manual/02_Spectral-Entities.md`
      - Added concrete recommended level bands to the chapter's base creatures and converted all benchmark-era printed TVs to final absolute TVs aligned to those bands.
      - Updated Chapter 2 scaling options, dual-mode Sluagh references, and encounter-design examples so the chapter now uses one absolute-TV dialect throughout.
      - Corrected the chapter's lingering benchmark-era encounter summaries for `Wraith of the Abyss` and `Spectral Arcanist`.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated the repo-wide conversion-state notes so they now include Chapter 2 among the fully converted chapters.
   - `Monster_Manual/00_Introduction.md`
      - Updated the manual-wide conversion-state note so it now includes Chapter 2 among the fully converted chapters.
   - Result: Chapter 2 now uses final absolute TV values consistently across all of its creature entries and internal examples.

27. **Chapter 3 TV conversion — complete**
   - `Monster_Manual/03_Mortals-and-Cultists.md`
      - Converted the chapter's remaining benchmark-era printed TVs to final absolute TVs aligned to the existing recommended level bands.
      - Updated linked scaling options, summon references, lair-action reinforcement text, sample encounters, and encounter-design blurbs so the chapter now uses one absolute-TV dialect throughout.
      - Added recommended level bands to the late Sarafan and Rune-Forger entries that were still missing them.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated the repo-wide conversion-state notes so they now include Chapter 3 among the fully converted chapters.
   - `Monster_Manual/00_Introduction.md`
      - Updated the manual-wide conversion-state note so it now includes Chapter 3 among the fully converted chapters.
   - Result: Chapter 3 now uses final absolute TV values consistently across all of its creature entries and internal examples.

28. **Chapter 4 TV conversion — complete**
   - `Monster_Manual/04_Beasts-and-Mutants.md`
      - Converted the chapter's benchmark-era printed TVs to final absolute TVs aligned to the existing recommended level bands.
      - Updated linked scaling options, sample encounters, lair-action brood text, and encounter-design blurbs so the chapter now uses one absolute-TV dialect throughout.
      - Added a chapter note clarifying that Chapter 4 now uses final absolute TVs throughout.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated the repo-wide conversion-state notes so they now include Chapter 4 among the fully converted chapters.
   - `Monster_Manual/00_Introduction.md`
      - Updated the manual-wide conversion-state note so it now includes Chapter 4 among the fully converted chapters.
   - Result: Chapter 4 now uses final absolute TV values consistently across all of its creature entries and internal examples.

29. **Chapter 6 TV conversion — complete**
   - `Monster_Manual/06_Hylden-Forces.md`
      - Converted the chapter's benchmark-era printed TVs to final absolute TVs aligned to the existing recommended level bands.
      - Updated summon tables, duplicate late-entry blocks, sample encounters, named-NPC TV hooks, scaling options, and encounter-design blurbs so the chapter now uses one absolute-TV dialect throughout.
      - Added a chapter note clarifying that Chapter 6 now uses final absolute TVs throughout.
   - `GM_Guide/02_Encounter-Design.md`
      - Updated the repo-wide conversion-state notes so they now reflect that all nine Monster Manual chapters are fully converted.
   - `Monster_Manual/00_Introduction.md`
      - Updated the manual-wide conversion-state note so it now reflects that all nine Monster Manual chapters are fully converted.
   - Result: Chapter 6 now uses final absolute TV values consistently across all of its creature entries and internal examples.

### Current balance notes

1. **Core TV model work is stable**
   - The GM Guide and Monster Manual introduction now point at the same absolute-TV encounter-budget model.
   - Remaining work is now primarily creature-package consistency, not top-level math contradiction.

2. **Highest-confidence TV 4 outliers have been addressed**
   - The repeated passes have mostly removed the biggest overspenders in Chapters 1-6: excessive summon volume, too many off-turn attacks, wide-radius control layered on already strong base kits, and over-generous sustain.
   - Recent Chapter 5-6 cleanup especially targeted repeatable reinforcement loops and off-turn area pressure.
   - The latest pass also trimmed the last few arguable TV 4 edge cases that were still peaking above the rest of their chapter peers.

3. **Remaining candidates are lower-confidence review targets**
   - The previously flagged edge cases in Chapters 3-6 have now been revisited and trimmed where the over-performance still looked defensible.
   - Remaining review targets are now mostly subjective style calls or chapter-internal consistency questions rather than clear encounter-budget failures.
   - If more tuning happens, likely candidates are only a few stylistic holdouts such as `Sarafan Grand Inquisitor`, and even those now read more as preference calls than obvious misses.

4. **What still needs a broader pass**
      - The core stat-block schema is now unified across all nine chapters.
      - Remaining terminology drift is mostly outside the core stat blocks: scaling notes, anchors, and a few descriptive callouts still use legacy `Health` wording.
   - If another balance pass happens, keep it narrow and evidence-driven. Recent passes are shaving edge-case output, not fixing hard contradictions.
   - Early chapters (1 and 2) still have minor subsection-label and metadata drift from pre-normalization writes that hasn't been swept.

### Still pending

1. Additional boss/action-economy review outside the first-wave outliers.
2. Optional subsection-label wording pass for chapter-internal consistency (for example `Stats` vs `Statistics`, or `Scaling` vs `Scaling Options`).
3. Optional cleanup of any remaining non-stat-block legacy wording outside Chapters 7–9 so prose matches the canonical stat-block terminology.

### Immediate next consistency targets

1. Subsection-label wording parity across chapters.
   - Heading depth is now unified, but label wording still varies by chapter (`Stats` vs `Statistics`, `Abilities` vs `Special Abilities`, `Scaling` vs `Scaling Options`).

2. Auxiliary wording cleanup outside stat blocks in earlier chapters where needed.
   - Chapters 7–9 are now clean. Any remaining prose cleanup would be limited to stray legacy wording elsewhere in the manual.

---

## Current State

**Flat absolute TV** is the canonical standard across the GM Guide and Monster Manual, but the printed Monster Manual conversion is still in progress.

- `GM_Guide/02_Encounter-Design.md` and `Monster_Manual/00_Introduction.md` both define TV as an absolute encounter-budget number.
- Threat tier labels (Minion, Standard, Elite, Boss, Legendary) are retained as descriptive bands; the TV value in each stat block is the authoritative number.
- All nine chapters now use a single consistent stat-block threat header: `**Threat Tier**: [Tier] (TV N)`.
- Chapters 1–9 are now on final absolute TVs.

**P3 schema normalization is complete.** All nine chapters now share a single stat-block schema: `HP`, `DV`, `Armor`, `Initiative`, `Movement`, merged `**Threat Tier:** Label (TV N)` header, and `**Type:**` creature type. There are no remaining `Health`, `Resources`, `Size/Type`, or split Threat Value fields in any stat block. All 127 creature entries across all chapters have an `- **Initiative:** N` field.

---

## Direction Taken

**Flat absolute TV** was chosen as the canonical standard. The following foundation work has been completed:

1. `GM_Guide/02_Encounter-Design.md` rewritten to define TV as an absolute encounter-budget value (not a party-level multiplier).
2. `Monster_Manual/00_Introduction.md` updated to remove the relative-tier TV model.
3. Threat tier labels retained as descriptive bands; the explicit TV number in each stat block is the authoritative value.
4. All mixed-format split entries across Chapters 3–6 converted to the single-line `**Threat Tier**: [Tier] (TV N)` format.
5. Chapter 5 completed its benchmark-TV to final-absolute-TV conversion.

The remaining work is now optional consistency cleanup: subsection-label wording parity, any further narrow boss review, and any stray non-stat-block wording cleanup outside Chapters 7–9.

---

## Priority Fixes

### P0 - Resolve the math model

**Status:** Completed in first pass.

These documents must agree before further balancing work is reliable:

- `GM_Guide/02_Encounter-Design.md`
- `Monster_Manual/00_Introduction.md`
- `Monster_Manual/01_Undead-and-Vampiric.md`
- `Monster_Manual/02_Spectral-Entities.md`
- `Monster_Manual/03_Mortals-and-Cultists.md`
- `Monster_Manual/07_Elemental-and-Arcane.md`
- `Monster_Manual/08_Ancient-Creatures.md`
- `Monster_Manual/09_Legendary-Entities.md`

Success criteria:

- One definition of Threat Value exists across the repo.
- Sample encounters use the same math as creature entries.
- The introduction explains how to total encounter TV without requiring level-based conversion.

### P1 - Fix clear encounter-budget errors

**Status:** Partially completed in first pass.

These are the fastest high-impact corrections:

1. **Fracture Void-Touched**
   - File: `Monster_Manual/01_Undead-and-Vampiric.md`
   - Problem: The encounter note undercounts total threat once `Merge Protocol` adds two TV 3 allies.
   - Status: Completed.
   - Fix used: Raised the encounter budget text to match actual play.

2. **Witch-Hunter Raid sample encounter**
   - File: `Monster_Manual/03_Mortals-and-Cultists.md`
   - Problem: It treats Outcast Raiders as minions even though their own entry is Standard TV 1.
   - Status: Completed.
   - Fix used: Replaced them with Sarafan Footsoldiers and corrected the total TV.

3. **Void-Spoken Oracle sample encounter**
   - File: `Monster_Manual/06_Hylden-Forces.md`
   - Problem: The printed total TV is lower than the listed creature sum.
   - Status: Completed.
   - Fix used: Recalculated and corrected the encounter note.

### P2 - Fix the most obvious stat-block outliers

**Status:** Partially completed in first pass.

These creatures are the best early candidates for direct rebalance:

1. **Sarafan Grand Inquisitor**
   - File: `Monster_Manual/03_Mortals-and-Cultists.md`
   - Problem: Reads well above TV 4 due to HP, DV 6, aura suppression, healing support, Legendary Resistance, and 3 Legendary Actions.
   - Status: Completed.
   - Fix used:
     - reduced HP and SE,
     - reduced Divine Condemnation and Sanctified Judgment output,
     - narrowed the aura and changed Disadvantage to -1 die,
     - reduced Legendary Actions from 3 to 2,
     - limited ally sustain from Rally the Faithful.

2. **Grand Arcanist**
   - File: `Monster_Manual/02_Spectral-Entities.md`
   - Problem: TV 4 version gains Legendary Resistance, 2 Legendary Actions, and `Time Dilation` for two full turns.
   - Status: Completed.
   - Fix used: Reduced the TV 4 scaling option's HP, SE, and Legendary Resistance and changed `Time Dilation` from a full extra turn into a limited follow-up action window.

3. **Sarafan Footsoldier**
   - File: `Monster_Manual/03_Mortals-and-Cultists.md`
   - Problem: Too durable for a TV 0.25 minion under the current encounter guide baseline.
   - Status: Completed.
   - Fix used: Lowered HP and weakened `Shield Block`, keeping the entry in the minion role.

4. **Blightmaw Matriarch / Pillar-Forged Warden / Hylden Arch-Priest**
    - Files:
       - `Monster_Manual/04_Beasts-and-Mutants.md`
       - `Monster_Manual/05_Constructs-and-Automatons.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in second pass.
    - Fix used: Reduced summon volume, reduced passive sustain or zone pressure, and trimmed Legendary Resistance where the TV 4 boss package had drifted too far upward.

5. **Wight Lord / Abyssal Revenant / Master Glyphfused Automaton / Master Rift Engineer**
    - Files:
       - `Monster_Manual/01_Undead-and-Vampiric.md`
       - `Monster_Manual/02_Spectral-Entities.md`
       - `Monster_Manual/05_Constructs-and-Automatons.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in third pass.
    - Fix used: Reduced extra action economy, reduced reinforcement or control reach, and trimmed added survivability where the TV 4 upgrade package exceeded boss benchmarks.

6. **Grave-Knight Warlord / Veteran Clockwork Knight / Alpha Iron-Cage Beast / Master Flesh Architect**
    - Files:
       - `Monster_Manual/01_Undead-and-Vampiric.md`
       - `Monster_Manual/05_Constructs-and-Automatons.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in fourth pass.
    - Fix used: Reduced army-wide coordination effects to narrower support effects, trimmed added survivability, and limited summon or debuff reach where the TV 4 upgrade package was overspending its budget.

7. **Deathguard Champion / Hylden Warlord / Master Bio-Sigil Reaver / Veteran War-Stalker**
    - Files:
       - `Monster_Manual/01_Undead-and-Vampiric.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in fifth pass.
    - Fix used: Reduced reliable burst, shortened control duration, and narrowed command or striker scaling where the TV 4 package was still outperforming its budget.

8. **Bonelord Acolyte / Vampire Beast Lord / Master Horror Warden / Rift Archon**
    - Files:
       - `Monster_Manual/01_Undead-and-Vampiric.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in sixth pass.
    - Fix used: Reduced summon footprint, trimmed boss durability, and narrowed broad battlefield-control packages that still ran above TV 4 expectations.

9. **Fracture Void-Touched / Master Restoration Engine / Hylden Rift Commander**
    - Files:
       - `Monster_Manual/01_Undead-and-Vampiric.md`
       - `Monster_Manual/05_Constructs-and-Automatons.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in seventh pass.
    - Fix used: Reduced reinforcement reliability, lowered sustain throughput, and trimmed downgraded boss variants that still over-performed their printed TV.

10. **Witch-Hunter General / Master Rune-Forger / Elder Drake / Berserker Troll**
    - Files:
       - `Monster_Manual/03_Mortals-and-Cultists.md`
       - `Monster_Manual/04_Beasts-and-Mutants.md`
    - Status: Completed in eighth pass.
    - Fix used: Reduced map-wide shutdown, lowered burst detonation density, and trimmed off-turn control on already strong base creatures.

11. **Pillar-Forged Warden / Master Rift Engineer / Hylden Arch-Priest**
    - Files:
       - `Monster_Manual/05_Constructs-and-Automatons.md`
       - `Monster_Manual/06_Hylden-Forces.md`
    - Status: Completed in ninth pass.
    - Fix used: Reduced repeatable summon density and off-turn control so TV 4 upgrades stay threatening without generating too much extra board state.

### P3 - Normalize presentation and terminology

**Status:** Complete for core stat-block schema; minor prose cleanup remains optional.

All core stat-block vocabulary is now unified across all nine chapters:

- `HP` (not `Health`) — all chapters ✅
- `DV` — all chapters ✅
- `DR` (not `DC`) — all chapters ✅
- `**Type:**` (not `**Size/Type:**`) — all chapters ✅
- `**Threat Tier:** Label (TV N)` single merged line — all chapters ✅
- `- **Initiative:** N` stat-block field — all 127 creatures ✅
- `**Resources:**` block eliminated — all chapters ✅

Remaining minor variance is cosmetic or outside the stat blocks themselves: subsection-label wording drift and any stray legacy prose wording outside Chapters 7–9.

---

## Chapter-by-Chapter Improvement Notes

### Chapters 1-3

- Now on the canonical schema. All stat blocks have `HP`, `DV`, merged Threat Tier, and `Initiative`.
- Minor subsection-label wording variance remains as a cosmetic style difference.

### Chapters 4-6

- Now on the canonical schema. Threat Tier lines merged, Initiative fields added to all creatures.
- Encounter examples in the GM Guide use absolute TV budgets and cross-reference these chapters.

### Chapters 7-9

- Fully converted to the canonical Ch1–6 stat-block schema. `Health`/`Resources`/`Size/Type` fields eliminated.
- Ch7–9 serve as the model for upper-tier threat bands (Bridge/High/Major/Deadly/Apex) in the Bridge–Apex TV ladder.

---

## Proposed Work Order

1. Sweep subsection-label wording parity across the nine chapters where `Stats` vs `Statistics` or similar labels still drift.
2. Run a subsection-label consistency pass across Chapters 1-9.
3. Sweep any remaining auxiliary prose outside Chapters 7–9 for legacy terminology where `HP` is now the intended canonical term.
4. If more balance work is desired, review any remaining boss/action-economy edge cases after the TV pass.
5. Do a final chapter-by-chapter presentation pass before treating the manual as style-complete.

---

## Definition of Done

The Monster Manual should be considered structurally improved when the following are true:

- Every creature has one unambiguous TV meaning.
- Boss action economy matches their listed TV.
- Sample encounters total correctly.
- Minions, Standards, Elites, Bosses, and Legendary threats occupy distinct mechanical space.
- A GM can compare a creature in Chapter 2 to a creature in Chapter 8 without converting between rules dialects.

---

## Suggested Next Pass

If work continues from this document, the most efficient next editing pass is:

1. Run a repo-wide post-conversion sweep for any stray benchmark-era prose or sample-encounter shorthand that survived outside the core chapter status notes.
2. After the TV pass, do subsection-label wording cleanup across all nine chapters.
3. Then do any remaining boss/action-economy review as a narrow balancing pass instead of a schema pass.

That sequence finishes the plan's remaining consistency work before any further discretionary rebalance.
