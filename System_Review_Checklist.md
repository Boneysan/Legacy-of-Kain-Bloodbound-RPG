# System Review Checklist

This checklist turns the issues from [Jack_Notes.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/Jack_Notes.md) into a structured review pass for the player-facing rules.

## Review Status

Completed major passes:

1. Classes
2. Lineages
3. Universal and Corrupted Perks
4. Corruption and Recovery
5. Core Combat / DV / Resistance Rules
6. Spellcasting baseline cleanup and corruption-cost alignment

Still open:

1. Monster abilities and resistances
2. Realm interaction rules
3. Remaining glossary cleanup and terminology polish
4. Final balance pass on high-impact capstones, control effects, and boss interactions

## Current Review Order

1. Monster abilities and resistances
2. Spell and Realm Interaction Rules
3. Glossary and terminology cleanup
4. Final balance pass

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
- Soul Reaver: `Phase Shift`, `Wraith Form`, `Banish`, `Flicker`, `Soul Rift`, `Abyssal Anchor`, `Death's Door`, `Soul Storm`.
- Shadowmancer: `Clones`, `Fear effects`, `Darkness interaction`, `Shadow Walk`, `Death from Below`.
- Sangromancer: bleeding / control wording, puppet effects, and blood-cost cadence.
- Dreadblade: auto-crit wording must explicitly require a hit.
- Any feature using `free action`, `move action`, or implied off-turn timing.

Follow-up notes:

- A second pass was completed on several high-ambiguity abilities and capstones.
- Remaining work here is mostly balance review, not baseline clarity.

### 2. Lineages

Primary file: [02_Lineages-and-Race.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/02_Lineages-and-Race.md)

Status: `Completed first clarity pass`

Focus areas:

- Review every lineage movement effect and unique trait for missing range, duration, and trigger.
- Clarify lineages that grant extra perks, free resources, or revival effects.
- Check each lineage for a clear upside, a clear limit, and a clear narrative drawback.
- Verify vulnerabilities are survivable and not disproportionately punishing.

Specific hotspots already identified:

- Base vampire trait: blood gain limit and wall-climb wording.
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

### 3. Universal and Corrupted Perks

Primary file: [04_Perks.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/04_Perks.md)

Status: `Completed first clarity pass`

Focus areas:

- Review perks that grant broad narrative or copy effects and give them hard boundaries.
- Make sure every perk has a clear trigger, cost, and refresh condition.
- Normalize corrupted perk wording with Chapter 8 corruption rules.
- Check whether perk benefits duplicate stronger class features too early.

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

Follow-up notes:

- Damage resolution order and rider handling were clarified.
- Glossary entries for corruption, short rest, long rest, and several stale terms were aligned with the updated chapters.
- The biggest remaining combat task is now checking monster-side rules against the player-side precedence.

### 6. Spell and Realm Interaction Rules

Primary files:
[05_Spellcasting-and-Magic.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/05_Spellcasting-and-Magic.md)
[11_Realms-Terrain-Arcane-Power.md](H:/GitHub/Legacy-of-Kain-Bloodbound-RPG/player's_handbook/11_Realms-Terrain-Arcane-Power.md)

Status: `Spell chapter mostly complete; realm chapter still open`

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

Status: `Not started`

Focus areas:

- Review monster passives, auras, and special attacks with the same template used for classes.
- Check monster resistances, immunity lists, and resistance-bypass effects against Chapter 9.
- Verify bosses and legendary monsters have explicit immunity language where needed.
- Make sure monsters do not rely on undefined player-facing conditions or timings.

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
| Monsters | Boss resistance and immunity riders | Core Rule Conflict | Monster-side exceptions may not match Chapter 9 precedence | Audit boss abilities against the combat hierarchy and rewrite exceptions explicitly | Open |
| Realms | Realm shift / anti-phase overlap | Terminology Conflict | Chapter 5 and Chapter 11 may still describe similar effects differently | Consolidate shared terms and add one canonical interaction rule | Open |
| Glossary | Residual stale / mojibake entries | Glossary Conflict | Some entries still have cosmetic encoding artifacts or stale shorthand | Do a final cleanup pass after the remaining rules chapters are stable | Open |
| Balance | Capstones and hard control effects | Balance Risk | Several top-tier abilities may now be clear but still overtuned or undertuned | Run a targeted balance pass after monster review | Open |

## Definition of Done

A section is ready when:

- Every player-facing ability has a clear action type, target, range, duration, and refresh.
- Every offensive effect has a clear attack or save procedure.
- Every ongoing effect states when it ends and when it ticks.
- Every special condition uses glossary wording or is defined inline.
- Every resistance / immunity interaction matches the core combat rules.
- Every corruption gain or reduction effect has a visible cost and timing.
- Similar abilities use the same language unless they are intentionally different.
