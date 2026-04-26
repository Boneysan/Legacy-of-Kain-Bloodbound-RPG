# Monster Manual - Introduction

**Welcome, Game Master**

This Monster Manual provides stat blocks, tactics, and lore for the creatures that prowl the shattered realm of Nosgoth. From feral ghouls to ancient vampires, from spectral wraiths to Hylden abominations, these entities represent the dangers your players will face.

---

## How to Use This Manual

### Organization

The manual is divided into thematic chapters, each containing creatures appropriate for different encounter types and threat levels:

1. **Undead & Vampiric** - Bloodthirsty creatures of the night
2. **Spectral Entities** - Denizens of the Spectral Realm
3. **Mortals & Cultists** - Human enemies and fanatics
4. **Beasts & Mutants** - Corrupted wildlife and monsters
5. **Constructs & Automatons** - Mechanical and magical servants
6. **Hylden Forces** - The banished race and their creations
7. **Elemental & Arcane** - Magical creatures and bound spirits
8. **Ancient Creatures** - Primordial beings and ruin guardians
9. **Legendary Entities** - Story-bound threats and unique foes

### Threat Tiers

TV (TV) is relative to the **Average Party Level (APL)**. A "standard" challenge for a level 5 party uses TV 5 enemies.

- **Minion (Relative TV = APL - 2):** Weak enemies; used in groups to pressure action economy
- **Standard (Relative TV = APL + 0):** Baseline threat; reliable rank-and-file opponent
- **Elite (Relative TV = APL + 2):** Strong specialist; high pressure, 1-2 unique abilities
- **Boss (Relative TV = APL + 4):** Encounter centerpiece; 2 Legendary Actions/round
- **Legendary (Relative TV = APL + 6+):** Campaign-defining threat; 3+ Legendary Actions/round

Threat tiers are descriptive benchmark bands. **The printed TV on a creature is always its final absolute encounter-budget contribution.** If a stat block says `TV 9` and its header says `Elite (Level 7)`, it means this creature is an Elite challenge for a Level 7 party.

**Calculating Encounter TV:**
- **Party TV** = Sum of all PC levels (e.g., 4 players at Level 5 = Party TV 20).
- **Enemy TV** = The absolute printed TV on each creature.
- **Trivial:** Total Enemy TV is 25% of Party TV.
- **Easy:** Total Enemy TV is 50% of Party TV.
- **Standard:** Total Enemy TV is 75-100% of Party TV.
- **Challenging:** Total Enemy TV is 125-150% of Party TV.
- **Deadly:** Total Enemy TV is 175-200% of Party TV.
- **Legendary:** Total Enemy TV is 250%+ of Party TV.

*Example: A Level 5 party of 4 has Party TV 20. A "Challenging" encounter (TV 25-30) could be one TV 11 Boss (Level 7) supported by two TV 9 Elites (Level 7).*

---

## How to Read Dice Pools — A Primer

This manual uses a **d6 dice pool system**. When a creature makes an attack or ability check, its dice pool is calculated as:

**Attribute + Skill = Xd6**

For example, a creature with Fury 4 and Weapon Mastery 3 rolls **7d6** to attack. Each die showing **5 or 6** counts as a **success**. Compare the total number of successes to the target's **Defense Value (DV)** or the listed **DR** for a save/check.

### Key Terms
- **Dice Pool**: The total number of d6 rolled (Attribute + Skill)
- **Defense Value (DV)**: The number of successes an attacker must meet or exceed to land a hit. Base DV should stay at **6** or lower; temporary cover, reactions, and special effects may raise effective DV higher.
- **Difficulty Rating (DR)**: The number of successes needed for saves, checks, and non-attack effects.
- **Armor**: Flat mitigation applied after a hit lands. Use one Armor score unless a stat block explicitly says otherwise.
- **Threat Value (TV)**: A creature's overall power rating used for encounter balancing.
- **Soul Energy (SE)**: Resource pool for magical abilities. Spent to fuel spells and special abilities.
- **Blood Points (BP)**: Resource pool for vampiric/blood-based abilities.

> **Damage Label Note:** Some older stat blocks use legacy labels such as Necrotic, Blood, Void, or Corruption as shorthand. Read them through the Player's Handbook damage framework: usually **Entropic** for necrotic/corruptive effects, **Spectral** for soul-rending effects, and **Physical** for mundane weapon damage.

> **Condition Note:** The glossary in [player's_handbook/12_Glossary.md](../player's_handbook/12_Glossary.md) is the canonical source for named conditions such as **Grappled**, **Frightened**, **Pinned**, **Charmed**, and **Suppressed**. If a stat block applies one of those conditions and also adds extra text such as ongoing damage, forced movement, or a special escape clause, apply both the glossary condition and the extra rider.

> **Loot Note:** When a loot entry gives a **Trade Value** in supplies, treat it as barter weight or faction interest, not as a literal coin price.

### Reading a Stat Block Attack
When you see: `Fury 4 + Weapon Mastery 3 = 7d6`
- The creature rolls 7d6
- Count each 5 or 6 as one success
- Compare total successes to the target's DV
- If successes meet or exceed DV, the attack hits and deals its listed damage

### Saves and Contested Reactions
Some creatures call for a save or a defensive reaction instead of a normal attack resolution.

- **Saves** use a listed DR, such as `DR 3 Will save` or `DR 2 Blood save`.
- **Reactions** use the relevant PHB reaction framework, usually Evasion or Weapon Mastery.
- If an older entry references **Dodge**, read that as the target's DV or an Evasion-based reaction when the entry clearly says it uses a Reaction.
- If an older entry references **Parry**, read it as a Weapon Mastery-based reaction.
- If an older entry references **Agility**, convert it to an **Evasion** save/check.

### Monster Ability and Resistance Baseline

Use this baseline when running or revising any monster entry in this book.

- **Ability structure:** If a monster ability omits a detail, default to the most restrictive reading: one Action, one visible target, within the listed attack range or 30 feet if no range is listed, instant duration for damage, and no repeat use limit unless the text says otherwise. When revising the entry, add the missing action type, target, range, duration, save, cost, and refresh directly to the ability.
- **Passive traits and auras:** Passive traits are always on unless disabled by their own weakness. Auras affect creatures that start their turn in the aura or enter it for the first time on a turn, whichever happens first. A creature saves against the same aura at most once per round unless the aura says otherwise.
- **Ongoing damage and control ticks:** Ongoing damage from monster abilities triggers at the start of the affected creature's turn unless the entry says otherwise. Control effects that deny actions, movement, reactions, or realm shifting must state whether the target repeats the save at the start or end of its turn.
- **Resistance and vulnerability:** Resistance halves damage after Armor, matching Chapter 9's damage resolution order. Legacy phrases such as "takes double damage" mean vulnerability-like doubling at the Resistance step. Resistance never reduces damage below 1 unless the damage would already be 0 after Armor or Immunity.
- **Immunity:** Immunity reduces the damage to 0 and blocks any rider tied to that damage unless the rider explicitly works on a successful save or on 0 damage. Effects that bypass Resistance do not bypass Immunity unless the stat block says they bypass Immunity.
- **Broad damage immunity:** If a monster becomes "immune to all damage," treat that as a special encounter state, not a normal defense. The entry must define the state, duration, movement limits, and at least one counterplay hook such as Radiant damage, sunlight, a ward, a terrain objective, or a named vulnerability.
- **Boss and legendary control:** Bosses and legendary creatures are not automatically immune to conditions. They use their printed immunities, Legendary Resistance, phase rules, lair rules, or explicit boss traits. If a control effect would remove the only meaningful enemy action for a full round, the GM may spend one available Legendary Resistance or scripted phase resource to downgrade it to a lesser effect such as Slowed, Suppressed, or loss of one action.
- **Legendary Resistance:** When a creature uses Legendary Resistance, it changes a failed save into a success only for that triggering effect. It does not heal damage, undo riders from earlier turns, refresh reactions, or bypass Immunity rules.
- **Summons and created creatures:** Summoned minions use their own stat blocks and defenses. If a boss aura or phase says it protects allies, it must state the range, duration, and whether it applies to summoned creatures.
- **Realm and phase effects:** Material, Spectral, incorporeal, anti-phase, and forced realm-shift effects use the realm interaction rules in Chapter 11 and the spell rules in Chapter 5. If a monster entry conflicts with those chapters, use the more specific monster rule for that creature and flag the entry for revision.
- **Phase abilities by affinity:** Phase Movement, Phase Step, Phase Strike, Phase Runner, Realm Shift, and all similar abilities that allow movement through solid objects are innate traits tied to a creature's Affinity. Creatures with **Spectral Affinity** use these abilities in both realms by nature — moving through matter is what they are, regardless of which side of the veil they inhabit. Creatures with **Material Affinity** that possess phase abilities through mutation, technology, or glyph-craft (constructs, mutants, Hylden-engineered forces) can only use those abilities in the Material Realm; they are lost if the creature is fully shifted to the Spectral Realm. **Hybrid Affinity** creatures use phase abilities in both realms. Brief in-and-out transits (such as the Dimension-Walker's Realm Shift) do not trigger Soul Bleed — the ability's listed SE cost covers the entire crossing and return; Soul Bleed only applies to extended stays.

---

## Reading Stat Blocks

### Standard Format

Each creature entry includes:

**Name & Classification**
- **Type:** Undead, Aberration, Beast, etc.
- **Affinity:** Spectral, Hybrid, or Material (omit if Material — Material is the default)
- **Threat Tier:** Minion, Standard, Elite, Boss, or Legendary, with the printed encounter-budget TV shown in parentheses

**Lore & Behavior**
Brief description of the creature's nature, origins, and role in Nosgoth.

**Statistics**
- **HP:** Hit Points
- **DV:** Defense Value (calculated as 1 + higher of Shadow or Will). The DV hard cap from base stats is **6**. No creature's innate DV exceeds 6. Effective DV may be raised above 6 through armor bonuses, magical effects, lair actions, or reactions, but the base stat block DV line should never read higher than 6.

> **DV Cap & Scaling Note:** The GM Guide's homebrew formulas may produce projected DV values above 6 for Elite and Boss creatures aimed at higher-level parties. This is intentional — those formulas describe *effective* DV (base + armor + reactions + lair bonuses), not base stat block DV. When creating or scaling a creature, keep the printed DV line at 6 or below and layer additional defenses through Armor, shield reactions, lair actions, or conditional bonuses (e.g., "+2 DV when in darkness") to reach the target effective DV.
- **Armor:** Flat damage mitigation.
- **DR in abilities:** The target number for saves, checks, or escape attempts.
- **Movement:** Speed in feet (divide by 5 for squares)

> **Movement Note:** All movement in this manual is measured in **feet**. To convert to a grid/square-based map, divide by 5 (e.g., 30 feet = 6 squares). Unless otherwise stated, one round of movement equals the creature's listed Movement value.
- **Attributes:** Fury, Soul, Shadow, Will, Focus, Blood
- **Resources:** Soul Energy (SE), Blood Points (BP) when applicable
- **Skills:** Relevant trained skills

Note on defenses: Treat the Player's Handbook and GM Guide terminology as canonical. Attacks normally target DV; saves and checks use DR; Armor is flat mitigation. If a stat block uses older labels like Dodge, Parry, or Agility, convert them using the guidance above instead of introducing a parallel defense subsystem.

**Attacks & Abilities**
- **Primary Attack:** Name, dice pool, damage, special effects
- **Special Abilities:** Unique powers or traits
- **Reactions:** Available response actions

**Tactics**
How the creature fights and behaves in combat.

**Loot (Optional)**
Treasure, components, or unique items the creature may drop.

---

## Customizing Creatures

### Adjusting Threat Level

To scale a creature up or down:

**Increase Threat by 1 Tier:**
- +5 HP per tier
- +1 to all attributes
- +1 DV
- +2 damage on attacks
- Add one special ability

**Decrease Threat by 1 Tier:**
- -5 HP per tier
- -1 to all attributes (minimum 1)
- -1 DV (minimum 1)
- -2 damage on attacks
- Remove one special ability

> **Scaling Note:** The scaling guidelines above are approximations for Tier 1–2 (TV 0.25–4) creatures. At higher TVs (TV 9+), scaling is **non-linear** — creatures gain disproportionately more HP, damage, and special abilities per tier. When scaling high-tier creatures, use the stat blocks in Chapter 5 and Chapters 7–9 as reference points rather than applying simple arithmetic.

### Adding Variants

**Environmental Adaptation:**
- **Fire-Touched:** +2 Fire damage on attacks, Resistance to Fire
- **Frost-Wreathed:** Attacks inflict Slowed, Resistance to Cold
- **Spectral-Touched:** Can phase partially, +1 DV
- **Corrupted:** +1 Entropic damage, more aggressive tactics

**Tactics Variants:**
- **Alpha/Champion:** Elite tier version with +1 to all skills
- **Veteran:** Standard tier with unique ability or tactic
- **Hive Mind:** Minions that gain bonuses when near others

---

## Using Creatures Narratively

### More Than Combat

Creatures in Nosgoth are not just obstacles—they're story elements:

**Environmental Storytelling:**
- What does this creature's presence reveal about the location?
- What happened to create or attract this creature here?
- What does it guard, hunt, or fear?

**Faction Connections:**
- Which faction controls, hunts, or studies this creature?
- Can it be negotiated with, befriended, or turned?
- What political implications come from encountering it?

**Corruption Themes:**
- How does corruption manifest in this creature?
- What was it before corruption took hold?
- Can it be saved, or is it too far gone?

### Memorable Encounters

**Give Creatures Personality:**
- Not all undead are mindless—some remember their past lives
- Beasts have survival instincts and pack dynamics
- Even constructs can have quirks from their programming

**Use the Environment:**
- Spectral creatures phase through walls
- Vampires use darkness and elevation
- Beasts lay traps and ambushes

**Create Consequences:**
- Fleeing enemies return with reinforcements
- Defeated leaders leave power vacuums
- Spared creatures remember mercy (or betrayal)

---

## Quick Reference: Creature by Level

### Levels 1-3 (Starting Adventures)
- Feralslave Ghouls (Minion)
- Dire Cave Wolves (Standard)
- Cult Fanatics (Standard)
- Bone-Pyre Skeletons (Minion)

### Levels 4-6 (Established Heroes)
- Vampire Thrall Swarms (Elite)
- Echo Serpents (Standard)
- Sarafan Inquisitors (Elite)
- Bound-Logic Scribes (Standard)

### Levels 7-10 (Veteran Adventurers)
- Hunger-Warped Vampires (Elite)
- Hylden Shock Troopers (Elite/Boss)
- Arcane Flare Wyrms (Boss)
- Titan-Kin Stalkers (Boss)

### Levels 11-15 (Masters of Nosgoth)
- Noble Revenant Scribes (Elite)
- Hylden Flesh Architects (Boss)
- The Echoed One (Boss)
- Corrupted Heroes (Elite/Boss)

### Levels 16-20 (Legendary Campaigns)
- Razielic Remnants (Legendary)
- Kain's Echo-Knight (Legendary)
- The Corruption Itself (Legendary)
- Nosgoth's Last Flame (Legendary)

---

## Design Philosophy

### Tactical Depth

Creatures are designed to create interesting combat choices:
- **Minions** force area control decisions
- **Standards** test core competencies
- **Elites** require focus fire or crowd control
- **Bosses** demand strategy and resource management
- **Legendaries** are puzzle fights with multiple solutions

### Status Effects

Many creatures inflict status effects tied to damage types (see **Core Mechanics, Chapter 9: Combat**):
- **Bleeding:** Ongoing damage from Piercing/Slashing
- **Burning:** Fire damage over time
- **Stunned:** Lost actions from Bludgeoning/Force
- **Soul Drain:** Target loses 1 SE (Spectral damage); powerful Spectral creatures may add riders that also reduce max SE
- **Corrupted:** Vulnerability and corruption gain

### Action Economy

Encounter design should consider total actions per side:
- 4 Minions = 4 actions (same as 4-player party)
- 1 Boss = 1 action (needs minions or legendary actions)
- Use Legendary Actions for solo bosses (see individual entries)

---

## GM Guidance Integration

This Monster Manual is designed to work seamlessly with:

**Chapter 2: Encounter Design**
- TV calculations
- Enemy templates (Minion, Standard, Elite, Boss, Legendary)
- Action economy principles
- Sample encounters

**Chapter 3: Character Progression**
- Creatures scaled for milestone advancement
- Encounters appropriate for narrative beats
- Boss fights as campaign milestones

**Chapter 4: Economy & Resources**
- Loot tables reflect barter economy
- Creature components as trade goods
- Faction-specific rewards

**Chapter 5: NPC Compendium**
- Legendary creatures tie to major NPCs
- Kain's vampire spawn
- Raziel's spectral echoes
- Elder God's servants

---

## A Note on Lethality

Nosgoth is a dangerous world. Not every encounter should be perfectly balanced. Sometimes players should:
- **Flee from overwhelming threats**
- **Negotiate rather than fight**
- **Use environment and tactics over brute force**
- **Accept that death is a real consequence**

However, ensure players have:
- **Clear warning signs** of deadly encounters
- **Options for escape or alternative solutions**
- **Moments to shine** against appropriate challenges
- **Meaningful victories** that feel earned

---

*"In Nosgoth, death is not the end—but becoming a monster might be worse."*
