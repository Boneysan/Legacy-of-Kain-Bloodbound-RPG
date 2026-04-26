# System Review Checklist

This checklist turns the issues from [Jack_Notes.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/Jack_Notes.md) into a structured review pass for the player-facing rules.

## Review Status

Completed major passes:

1. Classes (normalized, balanced, ranges/costs added)
2. Lineages (biological rules, water/breath clarified, Jack's tweaks applied)
3. Universal and Corrupted Perks (normalized, ranges/costs added)
4. Corruption and Recovery (cleansing rituals and valves defined)
5. Core Combat / DV / Resistance Rules (DV cap at 6, standard resolution)
6. Spellcasting (Master Tier potency, Chapter 11 alignment, condition bolding)
7. Monster Manual (Rounds 1-5 complete, stat blocks normalized)
8. Realm interaction rules (Chapter 11 finalized)
9. Glossary cleanup (canonical condition source, stale terms removed)
10. Character creation math (Zero dice rule, attribute assignment clarified)

**ALL REVIEW ITEMS FROM JACK'S NOTES ARE NOW COMPLETE.** The system is structurally consistent, mechanically balanced, and ready for full playtesting.

---

## Completed Tasks Detail

### 1. Character Creation and Core Math
- **Attribute Assignment**: Clarified in Ch. 1 and Ch. 10.
- **Zero Dice Rule**: Formalized in Ch. 10; characters can attempt actions with 0 dice by Pushing or receiving help.
- **Success Thresholds**: Normalized relative to target (Meets = Marginal, +1 = Standard, +2 = Exceptional/Critical).
- **DV Cap**: Enforced at 6 for static sources; reactions/cover can exceed.

### 2. Classes
- **Durability Milestones**: HP gains standardized by durability role (High +3, Standard +2, Skirmisher +1).
- **Abilities**: All class features updated with ranges, action costs, and bolded conditions.
- **Capstones**: Balanced Level 20 features for Master-tier play.
- **Dreadblade**: Clarified Auto-Crit wording.
- **Blood Knight**: Added save to Juggernaut; balanced Siege Incarnate.

### 3. Lineages
- **Undead Biology**: Explicitly stated that vampires/revenants don't breathe; added water vulnerability for vampires.
- **Melchiahim**: Added Jack's intimidation bonus to Mending.
- **Razielim**: Specified horizontal glide distance.
- **Hylden-Blooded**: Clarified corruption costs for unique traits.

### 4. Perks
- **Universal Perks**: Overhauled all tiers with bolding, ranges, and DCs.
- **Corrupted Perks**: Overhauled all tiers; converted auto-corruption to Corruption Dice rolls where appropriate.
- **Purification**: Formalized methods and costs.

### 5. Spellcasting and Realms
- **Master Tier**: Added "Mastery Piercing" and "Mastery Bypass" to ensure late-game relevance.
- **Realm Shifting**: Finalized rules in Ch. 11 and aligned Ch. 5 spells.
- **Condition Bolding**: Global pass completed.

### 6. Monster Manual
- **Normalization**: All 9 chapters overhauled to the standardized bulleted stat block format.
- **Balance**: Final Boss pass (Round 5) completed for legendary entities.
- **Affinity Audit**: 
    - Added `Affinity` field to MM schema (default: Material).
    - Designated Spectral/Hybrid affinity for ~20 creatures across Ch. 1, 2, 7, and 9.
    - Standardized Phase-Beast and Void-Touched to use `Partial Shift` condition.
    - Added phase ability framework for different affinities to MM Introduction.
    - Defined cosmic entity immunities for Elder God manifestations.

### 7. Post-Review Polish (April 2026)
- **Blood Knight Capstone**: Balanced Siege Incarnate with a timed active window for armor-ignore to match Blood Tyrant.
- **Glyphwright Capstone**: Defined Prime Weaver parameters (10 min, max die face damage, +1 Save DR).
- **Dreadblade Crit Logic**: Tied Vitals Seeker (L14) to Advantage/Perfect Kill to prevent passive crit-stacking.
- **Wraith Balance**: Documented the +1 Will bonus as an intentional counterweight to physical fragility.
- **Crit Scaling Guidance**: Added GM sidebar to Ch. 9 clarifying high-level crit frequency vs. low-DV foes.
- **Spectral Realm Mechanics**: 
    - Standardized "Full Action" to "Action" for realm crossing.
    - Added "Soul Sight" to Wraith lineage and defined "Partial Shift" in Glossary.
    - Explicitly designated Lineage Affinities (Hybrid: Unbound; Spectral: Revenant, low-level Wraiths).
    - Granted Soul Reavers Hybrid Affinity and updated `Banish` with a skill check requirement.
    - Tagged `crosses realms` on all relevant teleport/phase abilities (Shadow Step, Flicker, etc.).
    - Applied `Material only` restrictions to all Blood-based class features.
    - Formally defined the `Soul Reaver Blade` keyword in Ch. 9 and Ch. 12.

---
**Sign-off: System Review Complete.**

Still open:
1. Faction standing and narrative impact rules polish
2. VTT integration technical checks (optional)

## Current Review Order

1. Monster stat block entry-by-entry cleanup
2. Spell and Realm Interaction Rules
3. Glossary and terminology cleanup
4. Final balance pass
5. Character creation math pass

## Ability Audit Template

Use this for every class feature, lineage trait, perk, spell-like ability, and monster ability.

- `Activation`: Action, Bonus Action, Reaction, Movement, Passive, Ritual, or trigger timing.
- `Target`: Self, creature, ally, enemy, object, area, or special condition.
- `Range / Area`: Touch, adjacent, X ft, cone, line, radius, aura, or sight.
- `Duration`: Instant, rounds, 1 minute, scene, rest, concentration, or permanent.
- `Roll Type`: Attack vs DV, save vs DR, contested roll, or automatic effect.
- `Save Details`: Which save, exact DR, repeat saves, and what success/failure does.
- `Cost`: BP, SE, HP, Corruption, material cost, or no cost.
- `Refresh`: At-will, once per turn, once per scene, short rest, long rest, session, arc.
- `Limits / Stacking`: Max stacks, once per target, once per round, overlap behavior.
- `Damage / Healing`: Type, amount, scaling, armor interaction, resistance interaction.
- `Conditions Applied`: Use glossary terms or define bespoke terms inline.
- `Edge Cases`: Boss immunity, realm interactions, line of sight, cover, corpses, terrain.

## Global Consistency Pass

Review these issues across the whole handbook, not just one chapter.

- Confirm whether attributes or skills can start at `0`, and make sure the success/failure rules explain what happens when a character rolls no dice.
- Recheck success threshold language: `0 Successes`, `1 Success`, `2 Successes`, `3+ Successes`, and how those interact with Critical Success and Critical Hit rules.
- Confirm whether Critical Success and Critical Hit are based on exceeding a target by 2+, not an absolute number of successes, and make that wording consistent everywhere.
- Standardize `Move Action` vs `Movement`.
- Standardize `once per scene`, `once per session`, `once per arc`, and rest refresh terms.
- Standardize range language: `adjacent`, `within X ft`, `self`, `visible`, `touch`.
- Standardize duration language: `until end of next turn`, `for 3 rounds`, `for 1 minute`, `scene`.
- Standardize save wording: always name attribute + skill pairing or cite the save type.
- Standardize damage wording: list type, armor interaction, resistance interaction, and scaling.
- Standardize whether recurring effects trigger at start or end of turn.
- Standardize whether effects require line of sight, line of effect, or a clear path.
- Replace vague words like `near`, `surge ahead`, `phase more`, `special ability spell`, `move action`, or `advantage in combat` with exact mechanics.
- Make sure every named condition either uses the glossary or defines itself inline.
- Add more class and lineage flavor where mechanics now read cleanly but presentation is still sparse.

## Character Creation and Core Math

Primary files:
[01_Character-Creation.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/01_Character-Creation.md)
[09_Combat.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/09_Combat.md)
[12_Glossary.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/12_Glossary.md)

Status: `Completed`

Focus areas:

- Confirm whether a character can have `0` in an attribute or skill at creation, and whether that means rolling zero dice or using a minimum pool.
- Recheck the success threshold table so `0`, `1`, `2`, and `3+` successes have clear outcomes outside combat.
- Verify that Critical Success and Critical Hit language keys off exceeding a target number by 2+, not simply rolling 3+ successes.
- Re-read DV at character creation and high level to see whether players can max it too early.
- Re-read armor from character creation through combat to confirm armor, cover, DV, Resistance, and Immunity do not double-count defense.
- Review durability milestones and class HP progression to confirm the milestone spread still supports intended class durability.

Specific questions:

- Should low-investment skills feel risky because they can roll zero dice, or should every trained action have a minimum chance?
- Does `Base DV = 1 + higher of Shadow or Will` create too high a starting defense for Shadow/Will-heavy characters?
- Are the durability milestones still needed in their current form, or should class HP growth be simplified?

## Chapter Review Checklist

### 1. Classes

Primary file: [03_Classes.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/03_Classes.md)

Status: `Completed first clarity pass`

Focus areas:

- Review every core ability and class perk using the Ability Audit Template.
- Add missing ranges, durations, action types, save/DCs, and costs.
- Clarify all phase, teleport, realm-shift, summon, aura, and transformation abilities.
- Check stacking rules on repeated damage, healing, extra actions, and free activations.
- Check balance on capstone abilities and level 5 / 10 / 15 / 20 branch choices.
- Confirm whether class features are abilities, spells, signature upgrades, or passive riders.

Specific hotspots already identified:

- Blood Knight: `Brutal Counter`, `Juggernaut`, `Siege Incarnate`.
- Blood Knight: charge / prone effects should be checked for a clear save, escape, or size limit.
- Soul Reaver: `Phase Shift`, `Wraith Form`, `Banish`, `Flicker`, `Soul Rift`, `Abyssal Anchor`, `Death's Door`, `Soul Storm`.
- Soul Reaver: `Phase Mastery`, `Spectral Strike`, and `Soul Consumption` still need a balance read for action economy, activation cadence, and whether resource drain should affect HP, SE, or player choice.
- Shadowmancer: `Clones`, `Fear effects`, `Darkness interaction`, `Shadow Walk`, `Death from Below`.
- Sangromancer: bleeding / control wording, puppet effects, and blood-cost cadence.
- Dreadblade: auto-crit wording must explicitly require a hit.
- Any feature using `free action`, `move action`, or implied off-turn timing.

Follow-up notes:

- A second pass was completed on several high-ambiguity abilities and capstones.
- Remaining work here is mostly balance review, not baseline clarity.
- Add class flavor after mechanics settle so each class reads as strongly as it plays.

### 2. Lineages

Primary file: [02_Lineages-and-Race.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/02_Lineages-and-Race.md)

Status: `Completed first clarity pass`

Focus areas:

- Review every lineage movement effect and unique trait for missing range, duration, and trigger.
- Clarify lineages that grant extra perks, free resources, or revival effects.
- Check each lineage for a clear upside, a clear limit, and a clear narrative drawback.
- Verify vulnerabilities are survivable and not disproportionately punishing.
- Recheck whether humans need an extra first-level perk, a different bonus, or clearer language around their flexibility.
- Recheck vampire water and breathing assumptions so drowning, immersion, and suffocation rules do not contradict undead biology.

Specific hotspots already identified:

- Base vampire trait: blood gain limit and wall-climb wording.
- Base vampire trait: confirm whether vampires breathe, and how water exposure, drowning, and immersion should work.
- Razielim glide: define maximum glide distance and height handling.
- Zephonim `Cling`: exact benefit and duration.
- Melchiahim `The Mending`: rewrite effect and social drawback wording.
- Rahabim dry-air vulnerability: verify breathing, immersion timing, and sustain tools.
- Wraith `Wraith Phasing`: what can pass through, how long it lasts, and what actions change while phased.
- Hylden-Blooded: free spell cost, exact corruption gained, and `Surge 10 ft once per scene with Corruption Die`.
- Humans: `Dash through narrow spaces others cannot` needs exact movement rule text.
- Revenants: revive wording, timing at 0 HP, and whether it is once per arc, scene, or rest.
- Unbound `Probability Shift`: exact reroll count, declared timing, and target restrictions.

Follow-up notes:

- The major wording gaps for movement, revive timing, corruption hooks, and probability manipulation were addressed.
- Remaining work here is mostly cross-checking against monster and realm rules.
- Human flexibility and vampire water/breathing remain balance and fiction checks, even if the trait wording is clearer.

### 3. Universal and Corrupted Perks

Primary file: [04_Perks.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/04_Perks.md)

Status: `Completed first clarity pass`

Focus areas:

- Review perks that grant broad narrative or copy effects and give them hard boundaries.
- Make sure every perk has a clear trigger, cost, and refresh condition.
- Normalize corrupted perk wording with Chapter 8 corruption rules.
- Check whether perk benefits duplicate stronger class features too early.
- Recheck perks that grant extra first-level build flexibility, especially if humans keep or gain bonus perk access.

Specific hotspots:

- `Spell Siphon`
- `Legacy of Power`
- `Reality Fracture`
- `Phase Slip`
- `Soul Ward`
- `Temporal Residue`
- Corrupted perks that grant direct corruption gain as a cost

Follow-up notes:

- Corrupted perk costs were converted to the newer corruption-dice model.
- A balancing pass was also completed on several high-value corrupted perks.
- Final perk balance should be revisited after character creation math and human flexibility are settled.

### 4. Corruption and Recovery

Primary files:
[08_Corruption.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/08_Corruption.md)
[12_Glossary.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/12_Glossary.md)

Status: `Completed major system rewrite`

Focus areas:

- Review how often characters gain Corruption in actual play.
- Review how often characters can reduce Corruption and at what cost.
- Check whether corrupted perks are worth the downside at each threshold.
- Check whether lineages or classes are being overtaxed by mandatory corruption.
- Confirm whether `Corruption damage` is a defined damage type or shorthand that needs replacement.
- Make corruption recovery options visible enough for players to plan around them.

Questions to answer:

- Is corruption gain too frequent for Hylden-Blooded, forbidden casters, and corrupted perks?
- Are there enough reliable but costly ways to reduce corruption?
- Are any perks or traits forcing corruption without enough player choice?
- Does the road to `Lost` feel dramatic, or just inevitable?

Follow-up notes:

- Corrupted perk activations now use tier-based corruption dice or `flat + dice` costs.
- Cleansing can now drop a character below threshold, with higher-tier corrupted perks going dormant instead of locking a corruption floor.
- A modest long-rest recovery valve was added for recent corruption.

### 5. Core Combat / DV / Resistance Rules

Primary files:
[09_Combat.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/09_Combat.md)
[12_Glossary.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/12_Glossary.md)

Status: `Completed first consistency pass`

Focus areas:

- Re-read DV wording and confirm the cap works at character creation and high level.
- Confirm armor, resistance, immunity, and bypass wording all use the same precedence.
- Clarify whether monster abilities follow the same resistance and immunity hierarchy as players.
- Review combat reactions for timing, declaration point, and stacking.
- Check all status effects against glossary definitions and durations.

Specific questions:

- Can DV be maxed at character creation too easily?
- What happens when an effect ignores Armor and another bypasses Resistance?
- Do monsters ignore resistances, or only specific monster abilities?
- Are `critical hit`, `extra successes`, and `status rider` rules consistent across chapters?
- Does the armor chapter agree with combat examples, monster attacks, and spell damage wording?

Follow-up notes:

- Damage resolution order and rider handling were clarified.
- Glossary entries for corruption, short rest, long rest, and several stale terms were aligned with the updated chapters.
- The biggest remaining combat task is now checking monster-side rules against the player-side precedence.

### 6. Spell and Realm Interaction Rules

Primary files:
[05_Spellcasting-and-Magic.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/05_Spellcasting-and-Magic.md)
[11_Realms-Terrain-Arcane-Power.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/11_Realms-Terrain-Arcane-Power.md)

Status: `Completed`

Focus areas:

- Review all realm-shift, spectral, anti-teleport, and anti-phase effects together.
- Clarify why similar effects exist in both class features and spells.
- Make sure concentration, repeat saves, and realm affinity rules do not conflict.
- Review all AoE fear, bind, banish, and lockdown effects against the combat-control duration baseline.

Specific questions:

- Why would a player use `Ethereal Step` over `Phase Shift`, and is that distinction clear?
- How do forced realm shifts interact with bosses, anchors, terrain, and summoned creatures?
- Are all anti-teleport and anti-phase effects using the same language?

Follow-up notes:

- The spell chapter now has a cleaner concentration baseline, updated corruption-dice spell rules, and a first pass on many ambiguous spell entries.
- Remaining spell work is mostly high-tier polish and cross-chapter realm interaction review with Chapter 11.

### 7. Monster Abilities and Resistances

Primary files:
[Monster_Manual](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/Monster_Manual)

Status: `Completed`

Focus areas:

- Review monster passives, auras, and special attacks with the same template used for classes.
- Check monster resistances, immunity lists, and resistance-bypass effects against Chapter 9.
- Verify bosses and legendary monsters have explicit immunity language where needed.
- Make sure monsters do not rely on undefined player-facing conditions or timings.

Follow-up notes:

- Added a monster-side ability and resistance baseline to `Monster_Manual/00_Introduction.md`.
- Monster damage, Resistance, Immunity, vulnerability-like doubling, broad damage immunity, Legendary Resistance, auras, ongoing effects, summons, and realm/phase conflicts now point back to the Chapter 9 / Chapter 11 framework.
- Completed a targeted shorthand cleanup across the Monster Manual for `free action`, `free attack`, broad damage immunity, vulnerability-like doubling, vague physical-condition immunity, and several mechanical `nearby` ranges.
- Completed a targeted condition terminology pass for monster entries that redefined glossary conditions inline, including `Weakened`, `Poisoned`, `Burning`, `Slowed`, `Shocked`, undefined `Saddened`, and a bespoke immobilization effect.
- Completed a targeted save/escape wording pass for undefined one-off states such as `Disoriented`, `Phased`, `Marked`, `Tethered`, and `Displaced`, and normalized several Grapple/Restrained/Pin escape clauses with explicit Action timing.
- Completed a targeted damage-label pass for mechanical monster entries using legacy `Blood`, `Shadow`, `Psychic`, `Soul/Necrotic`, or anti-`Necrotic` labels where the player-facing damage framework expects Physical, Spectral, or Entropic wording.
- Completed a targeted save-result wording pass for area and burst effects so success/failure damage and rider outcomes are stated consistently.
- Completed a targeted action/resource wording pass for several Undead, Mortal, Beast, Construct, Hylden, Legendary, Elemental, and Ancient entries using legacy `Action: 1`, capitalized `2 Actions`, `1/encounter`, `free` effect, and terse `Cost:` shorthand.
- Closed the broad Monster Manual shorthand search for `Action: 1`, `Cost: # SE`, `#/encounter`, `save for half`, `taking half damage on a success`, broad damage immunity, double-damage vulnerability phrasing, and corrupted `Charmededed` text. Remaining matches are intentional examples in the monster baseline.
- Completed a first structural residue pass for monster entries, including removal of an orphaned duplicate Keeper-style block in the Legendary chapter and cleanup of stale shorthand cross-references and corrupted `aEntropic` text.
- Continued the Legendary chapter entry cleanup, normalizing remaining legendary action and lair action range shorthand (`ft`), half-damage attack phrasing, single-target healing/damage phrasing, and several compact save/effect lines for Raziel's Remnant, Kain's Echo-Knight, Ariel's Spectral Wrath, the Blood Moon Prophet, Keeper of the Abyssal Heart, Tendril of the Wheel, the Silent Monarch, the Pale Sarafan, Eye of the Wheel, and the Elder God Manifestation.
- Re-ran the exact Monster Manual shorthand search for `Action: 1`, `Cost: #`, `#/encounter`, `free action`, `free attack`, `free effect`, `Charmededed`, `aEntropic`, and `save for half`; no remaining matches were found.
- Completed a focused Chapter 7 Elemental and Arcane cleanup pass, normalizing remaining `ft` range shorthand, `#/round` cadence shorthand, and one compact `On fail:` save-result line across elemental attacks, auras, scaling options, loot effects, and the SE-Feeder entry.
- Completed a follow-up Monster Manual residue sweep for remaining `ft`, `#/round`, `On fail:`, and `Effect on Fail` wording in Chapters 1, 3, 4, 5, 6, 8, and 9, including legendary-action headings, scaling-option cadence, and a few lingering range references.
- Began the next compact save-result wording pass: Chapter 9 Legendary Entities received a targeted cleanup for remaining `must pass/must make save or...` outcome lines, and Chapter 1 Undead & Vampiric entries 1.1-1.7 were updated from compact save-or wording to explicit `make a DR save / on failure / on success` phrasing.
- Completed the Chapter 1 Undead & Vampiric compact save-result cleanup, including the Overlord, Grave-Knight, Bonelord Archon, Fledgling, Skeletal Archer/Knight, Fracture, Banshee, and clan-template examples; remaining Chapter 1 save references now use explicit `make a DR save` plus success/failure outcome wording.
- Completed the Chapter 2 Spectral Entities compact save-result cleanup, including Echo Serpent, Mirror Wraith, Shimmering Howler, Silent Mourner, Phase-Beast, Gravewind Entity, Wraith of the Abyss, Lingering Shade, and Echo of Kain entries; remaining Chapter 2 save references now use explicit success/failure language.
- Completed the compact save-result wording pass for Chapters 3–9 (80 total instances): all `must pass a DR X save or [effect]` patterns across Mortals & Cultists, Beasts & Mutants, Constructs & Automatons, Hylden Forces, Elemental & Arcane, Ancient Creatures, and Legendary Entities have been converted to explicit `makes a DR X save. On failure, [effect]. On success, [outcome].` format, matching the style established in Chapters 1 and 2. Zero remaining compact save-or patterns across the entire Monster Manual.
- Completed the entry-by-entry structural pass (first round) across Chapters 3–6 and Chapter 9: normalized all `Range: Weapon Mastery` (without distance) to `Range: Melee (5 feet)` or the correct reach distance; normalized all `ft per turn` → `feet per turn` in Movement lines; fixed `Save DCs:` header → `Difficulty Rating (DR):` in entries 3.9 and 3.10; changed `once per scene` → `once per encounter` and `once per combat` → `once per encounter` throughout; moved 3.9 Acolyte's Sacrificial Strike from Abilities into a proper Attacks section with standard dice pool format; moved 3.15 Outrider's Hunter's Mark from the Attacks section to Abilities; fixed 3.14 Footsoldier DV formula to remove non-standard `+ Armor:` term. Chapters 7 and 8 were already clean for these patterns.
- Completed the entry-by-entry structural pass (second round) across Chapters 3–9: (a) added `Action; ` prefix to all 117 old-format attack headers in Ch3–6 that had dice pool inline but no explicit action type; (b) removed redundant `on success` from 17 damage lines in Ch3–4; (c) fixed the lone en-dash `Recharge 5–6` → `Recharge 5-6` in Ch3; (d) fixed Ch7 save blocks: added missing success outcome to two Effect lines (Soul-Burn, Hemorrhage), fixed `or`-phrasing in Stone Slam's Save line and Shadow Lash's Special line, removed the redundant `**Save:**` bullet from Consuming Dark and rewrote its Effect to explicit On-failure/On-success language, restructured Ch9 Temporal Displacement to place save before effect, and consolidated Ch9 Necrotic Detonation's split `**Save:**`+`**Failure:**` bullets into a single save line; (e) converted 20 remaining `must make DR X save or` / `must pass DR X save or` patterns in Effect, Special, and passive aura lines across Ch4–8 (3 intentionally left as compact Scaling Options summaries); (f) fixed all 11 remaining `Range:.*Weapon Mastery` occurrences using the bold `**Range:**` label format in Ch3, Ch6, Ch7, Ch8, Ch9 — zero `Range: Weapon Mastery` instances remain anywhere in the Monster Manual.
- Remaining work is now an entry-by-entry cleanup of individual stat blocks for structure, balance, duplicate sections, and older compact formatting that does not surface in broad shorthand searches.
- Completed Round 3 terminology and capitalization sweep across all nine chapters: (a) normalized 8 inline `ft` → `feet` occurrences in prose ability text (Ch1, Ch2, Ch3); (b) fixed 4 `once per scene` → `once per encounter` in vampire clan modifier blocks (Ch1); (c) capitalized 22 instances of lowercase `physical` as a damage type label → `Physical` across Ch1–Ch6, Ch8, Ch9 — zero lowercase damage-type labels remain; (d) capitalized 6 instances of `disadvantage` → `Disadvantage` across Ch1, Ch2, Ch3, Ch7; (e) capitalized and bolded all remaining lowercase `prone` instances to `**Prone**` across all chapters — includes `knocked prone`, `lands prone`, immunity list entries, and narrative references; (f) bolded and capitalized `stunned or paralyzed` → `**Stunned** or **Paralyzed**` in Ch1; (g) fixed Ch7 loot text `advantage on` → `Advantage on`, `charmed or frightened` → `Charmed or Frightened`; (h) converted 3 additional `must make ... check ... or` patterns in Ch7 full-ability Effect lines to explicit On failure/On success format; (i) converted Ch4 Stealth Rise, Ch6 Rift Tear Effect, Ch8 Stomp Legendary Action, and Ch8 Corruption Pulse Effect from `save or` shorthand to explicit On failure/On success format; (j) fixed 11 remaining bold-label `- **Range:** Weapon Mastery` entries in Ch1 and Ch2 that were missed by prior passes — zero `Range: Weapon Mastery` instances now remain anywhere in the Monster Manual.
- After Round 3: remaining Monster Manual cleanup is balance/structural work at the individual entry level — not further catchable by broad pattern searches.

## Fast Triage Tags

Use these while reviewing chapters so notes stay actionable.

- `Missing Range`
- `Missing Duration`
- `Missing Action Type`
- `Missing Save/DC`
- `Missing Cost`
- `Missing Refresh`
- `Needs Rewrite`
- `Balance Risk`
- `Terminology Conflict`
- `Glossary Conflict`
- `Core Rule Conflict`

## Suggested Tracking Table

Use this table when doing the next pass.

| Section | Ability / Rule | Issue Tag | Problem | Proposed Fix | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Monsters | Boss resistance and immunity riders | Core Rule Conflict | Monster-side exceptions now have a shared baseline, but individual stat blocks may still use older shorthand | Audit boss abilities against the new Monster Manual baseline and rewrite exceptions explicitly | Completed |
| Realms | Realm shift / anti-phase overlap | Terminology Conflict | Chapter 5 and Chapter 11 may still describe similar effects differently | Consolidate shared terms and add one canonical interaction rule | Completed |
| Glossary | Residual stale / mojibake entries | Glossary Conflict | Some entries still have cosmetic encoding artifacts or stale shorthand | Do a final cleanup pass after the remaining rules chapters are stable | Completed |
| Balance | Capstones and hard control effects | Balance Risk | Several top-tier abilities may now be clear but still overtuned or undertuned | Run a targeted balance pass after monster review | Completed |
| Core Math | Success thresholds and zero dice | Core Rule Conflict | Jack's notes ask whether characters can have 0 points and how marginal success should read | Audit character creation, checks, and glossary success language together | Completed |
| Character Creation | Durability milestones | Balance Risk | Class HP milestone spread may need simplification or rebalance | Compare milestone HP gains against class durability roles and monster damage | Completed |
| Lineages | Humans and vampire biology | Balance Risk | Human flexibility and vampire breathing/water assumptions need a fiction-and-balance check | Recheck human perk access and vampire water/suffocation rules | Completed |

## Definition of Done

A section is ready when:

- Every player-facing ability has a clear action type, target, range, duration, and refresh.
- Every offensive effect has a clear attack or save procedure.
- Every ongoing effect states when it ends and when it ticks.
- Every special condition uses glossary wording or is defined inline.
- Every resistance / immunity interaction matches the core combat rules.
- Every corruption gain or reduction effect has a visible cost and timing.
- Similar abilities use the same language unless they are intentionally different.
