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

Each creature is categorized by threat level, which corresponds to the Threat Value (TV) system from **GM_Guide Chapter 2: Encounter Design**:

- **Minion (benchmark TV 0.25):** Weak enemies; used in groups to pressure action economy
- **Standard (benchmark TV 1):** Baseline threat; reliable rank-and-file opponent
- **Elite (benchmark TV 2):** Strong specialist; roughly two standards' worth of pressure
- **Boss (benchmark TV 4):** Encounter centerpiece; needs layered defenses or support
- **Legendary (benchmark TV 6+):** Campaign-defining threat with multiple layers of action economy

Threat tiers are descriptive benchmark bands. **The printed TV on a creature is always its final encounter-budget contribution.** If a stat block says `TV 3`, add `3` to the encounter total. If it says `TV 16`, add `16`.

Early chapters often use benchmark values such as `0.25`, `1`, `2`, and `4` directly. Later chapters and unique creatures often print larger absolute TVs because they are already scaled, bespoke threats.

**Calculating Encounter TV:**
- Party TV = Sum of all PC levels
- Enemy TV = the printed TV on each creature
- Trivial: 25% of Party TV
- Easy: 50% of Party TV
- Standard: 75-100% of Party TV
- Challenging: 125-150% of Party TV
- Deadly: 175-200% of Party TV
- Legendary: 250%+ of Party TV

*Example: A Level 5 party of 4 has Party TV 20. A balanced encounter (TV 20) could be: 2 TV 4 bosses + 4 TV 2 elites + 4 TV 1 standards, 1 TV 12 major threat + 2 TV 4 lieutenants, or any other mix totaling about 20.*

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

---

## Reading Stat Blocks

### Standard Format

Each creature entry includes:

**Name & Classification**
- **Type:** Undead, Aberration, Beast, etc.
- **Threat Tier:** Minion, Standard, Elite, Boss, or Legendary
- **Threat Value (TV):** Numeric value for encounter balancing

**Lore & Behavior**
Brief description of the creature's nature, origins, and role in Nosgoth.

**Statistics**
- **HP / Health:** Hit Points (some chapters label this as Health)
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

> **Scaling Note:** The scaling guidelines above are approximations for Tier 1–2 (TV 0.25–4) creatures. At higher Threat Values (TV 9+), scaling is **non-linear** — creatures gain disproportionately more HP, damage, and special abilities per tier. When scaling high-tier creatures, use the stat blocks in Chapters 7–9 as reference points rather than applying simple arithmetic.

### Adding Variants

**Environmental Adaptation:**
- **Fire-Touched:** +2 Fire damage on attacks, Resistance to Fire
- **Frost-Wreathed:** Attacks inflict Slowed, Resistance to Cold
- **Spectral-Touched:** Can phase partially, +1 DV
- **Corrupted:** +1 Corruption damage, more aggressive tactics

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
- Glyphfused Automatons (Standard)

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
- **Soul Drained:** Reduced max SE from Soul damage
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
- Threat Value calculations
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
