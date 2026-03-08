# Chapter 2: Encounter Design

Creating balanced, engaging encounters is an art. This chapter provides tools and guidelines for crafting memorable combat and challenges in Nosgoth.

## At a glance
- 2.1 Understanding Threat Value
- 2.2 Creature Threat Values
- 2.3 Action Economy
- 2.4 Environmental Factors
- 2.5 Enemy Abilities and Synergies
- 2.6 Encounter Pacing
- 2.7 Boss Design
- 2.8 Non-Combat Encounters
- 2.9 Adjusting on the Fly
- 2.10 Sample Encounters
- 2.11 Quick Reference: Encounter Checklist

Note on terminology: DV is for attacks, DR is for checks and saves, and Armor is flat mitigation. See Player's Handbook Chapters 5 (Spellcasting and Magic), 8 (Corruption), and 9 (Combat) for Force, Spectral, and Entropic details.

---

## 2.1 Understanding Threat Value

Use a simple Threat Value (TV) system to balance encounters:

### Character Threat Value
Each PC has a base TV equal to their level:
- Level 1-5 characters = TV 1-5
- Level 6-10 characters = TV 6-10
- Level 11-15 characters = TV 11-15
- Level 16-20 characters = TV 16-20

**Party Threat Value = Sum of all PC TVs**

### Enemy Threat Value
Enemy TV is always an **absolute encounter-budget number**. When a creature says `TV 2`, add `2` to the encounter total. When a creature says `TV 12`, add `12`.

Published Monster Manual entries use their printed TV exactly as written. Early chapters often use benchmark values like `0.25`, `1`, `2`, and `4`, while later chapters and unique threats may use any larger absolute number.

### Encounter Difficulty Guidelines

| Encounter Type | Enemy TV Relative to Party TV |
|---------------|-------------------------------|
| **Trivial** | 25% of party TV |
| **Easy** | 50% of party TV |
| **Standard** | 75-100% of party TV |
| **Challenging** | 125-150% of party TV |
| **Deadly** | 175-200% of party TV |
| **Legendary** | 250%+ of party TV |

**Example:** A party of 4 Level 5 characters has party TV = 20.
- Standard encounter = enemies totaling TV 15-20
- Challenging encounter = enemies totaling TV 25-30
- Deadly encounter = enemies totaling TV 35-40

---

## 2.2 Creature Threat Values

### Benchmark Enemy Tiers

| Enemy Type | Benchmark TV | Typical Use |
|-----------|--------------|-------------|
| **Minion** | 0.25 | Disposable bodies, swarm pressure, weak support |
| **Standard Enemy** | 1 | Rank-and-file threat, roughly one meaningful combatant |
| **Elite Enemy** | 2 | Strong specialist, two-PC level pressure |
| **Boss** | 4 | Encounter centerpiece, requires action-economy support |
| **Legendary** | 6+ | Campaign threat, layered defenses and multiple phases |

These benchmark values are the starting point for low-tier published creatures. If you are building a custom creature for a specific party level, scale the benchmark by the party's average level to get the creature's final absolute TV. Published stat blocks should always print the final TV players and GMs add directly to encounter budgets.

### Quick Enemy Stat Creation (Homebrew Baselines)

Use these formulas when building a creature specifically for a party's average level. The output is a creature whose final printed TV should match the intended benchmark for that level band.

**Minion (TV 0.25):**
- HP: 3–6
- DV: 1 + (party level ÷ 4)
- Armor: 0
- Attack: Party level d6 (1 attack)
- Damage: 2-3

**Standard Enemy (TV 1):**
- HP: 10 + (3 × party level)
- DV: 2 + (party level ÷ 3)
- Armor: 0-2
- Attack: (Party level + 2) d6
- Damage: 4-6
- Contested checks: pool = party level ÷ 2 (round up)

**Elite Enemy (TV 2):**
- HP: 15 + (4 × party level)
- DV: 3 + (party level ÷ 2), max 6 (excess becomes effective DV via Armor or reactions)
- Armor: 2-3
- Attack: (Party level + 3) d6
- Damage: 6-8
- Special: 1-2 unique abilities
- Contested checks: pool = party level

**Boss (TV 4):**
- HP: 20 + (5 × party level)
- DV: 4 + (party level ÷ 2), max 6 (excess becomes effective DV via Armor or reactions)
- Armor: 3-4
- Attack: (Party level + 4) d6, 2 attacks per turn
- Damage: 8-12
- Special: 3-4 unique abilities, Resistance to 1-2 damage types; solo bosses usually gain 2 Legendary Actions/round or a supporting retinue, not both by default
- Contested checks: pool = party level

**Legendary (TV 6+):**
- HP: 30 + (6 × party level)
- DV: 6 (base cap; layer additional defense through Armor, reactions, and lair bonuses)
- Armor: 4-6
- Attack: (Party level + 6) d6, 3 attacks per turn
- Damage: 14-18
- Special: 5+ unique abilities, Immunity to 1 or more damage types where appropriate, Legendary Actions (3/round)
- Contested checks: pool = party level + 2

---

## 2.3 Action Economy

Action economy often matters more than stats:

### The Action Economy Principle
**The side with more actions per round usually wins.**

A boss with 50 HP facing 4 PCs will still get overwhelmed because:
- Boss gets: 1 Action, 1 Movement, 1 Reaction per round
- PCs get: 4 Actions, 4 Movements, 4 Reactions per round

### Balancing Boss Fights

**Option 1: Add Minions**
- Gives enemies more actions
- Provides tactical targets
- TV example: Boss (TV 12) + 4 Minions (TV 1 each) = TV 16

**Option 2: Legendary Actions**
- Boss can take actions on player turns
- Example: "The vampire lord can make one claw attack after any PC's turn ends"
- As a default benchmark, use 2 Legendary Actions for a TV 4 solo boss and 3 for a TV 6+ Legendary creature
- For custom creatures built to a level band, count each reliable legendary action as roughly `+0.5 × average party level` to the creature's final TV

**Option 3: Multi-Attack**
- Boss makes 2-3 attacks per Action
- Increases effective TV by 50% per extra attack

**Option 4: Reaction Abilities**
- By default, bosses still only get 1 Reaction per round; only grant more if a specific stat block explicitly says so
- Example: "Parry—when hit by a melee attack, reduce incoming damage by 5 (1/round)"
- If you need more boss pressure, prefer minions, multi-attack, or Legendary Actions over extra reactions

---

## 2.4 Environmental Factors

Terrain and environment dramatically affect encounter difficulty:

### Terrain Types and Their Effects

**Difficult Terrain**
- Costs 2 movement per square
- Examples: Rubble, shallow water, dense undergrowth
- **Tactical Use:** Slows melee enemies, benefits ranged

**Hazardous Terrain**
- Deals damage or requires saves
- Examples: Fire pits (2 Fire damage at the start of each turn), corrupted pools (DR 2 save or 1 Corruption)
- **Tactical Use:** Area denial, force positioning choices

**Elevated Terrain**
- Usually grants Advantage on attacks made from clearly superior footing
- In rare cases, impose Disadvantage on attacks made uphill or while climbing instead
- Use one positional modifier at a time; do not also add DV unless cover is involved
- **Tactical Use:** Powerful defensive position

**Cover**
- Half cover: +1 DV against ranged attacks/spells
- Full cover: +2 DV against ranged attacks/spells
- These are the primary recurring numeric DV modifiers in combat
- **Tactical Use:** Protects ranged enemies, encourages flanking

### Interactive Elements

Add objects players can interact with:
- **Pillars/Columns:** Can be toppled (DR 3 Blood check, 4d6 damage in line)
- **Chandeliers:** Can be dropped on enemies (DR 2, 3d6 damage in area)
- **Levers/Switches:** Change battlefield (open pits, seal doors)
- **Barrels/Crates:** Can be used as cover or thrown (improvised weapon)

### Environmental Hazards

| Hazard | Effect | DR/Damage |
|--------|--------|-----------|
| Crumbling Floor | Save or fall through | DR 2 Evasion, 2d6 Physical (Bludgeoning) |
| Collapsing Ceiling | Area damage | DR 3 Evasion or 4d6 Physical (Bludgeoning) |
| Spectral Rift | Pull toward Spectral Realm | DR 2 Will or phased for 1 round |
| Corrupted Aura | Gain Corruption | DR 2 Will or +1 Corruption |
| Poison Gas | Ongoing damage | 2 Entropic (Poison) damage at the start of each turn |

---

## 2.5 Enemy Abilities and Synergies

Create interesting encounters by giving enemies complementary abilities:

### Synergy Examples

**The Tank & Cannon:**
- **Tank:** High HP, low damage, ability to protect allies (+2 DV to adjacent allies)
- **Cannon:** Low HP, high damage, ranged attacks
- **Synergy:** Cannon hides behind tank; PCs must flank or focus fire

**The Controller & Striker:**
- **Controller:** Abilities that inflict conditions (Rooted, Stunned, Blinded)
- **Striker:** High damage, bonus damage against conditioned targets
- **Synergy:** Controller locks down PC, striker finishes them

**The Healer & Horde:**
- **Healer:** Can restore HP to allies (1 action heals 1d6 HP)
- **Horde:** Many weak minions
- **Synergy:** Healer negates AoE damage, must be priority target

**The Phaser & Ambusher:**
- **Phaser:** Can shift between realms, grant allies concealment
- **Ambusher:** Bonus damage from stealth/surprise
- **Synergy:** Phaser creates opportunities for ambusher

### Enemy Ability Templates

**Defensive Abilities:**
- Regeneration (restore X HP at the start of each turn)
- Resistance to a damage type (half damage after Armor interaction)
- Reactive Armor (damage attackers who hit in melee)
- Phase Shift (become incorporeal, once per scene)

**Offensive Abilities:**
- Multi-Attack (2-3 attacks per action)
- Area of Effect (cone/sphere damage)
- Status Infliction (guaranteed condition on hit)
- Grab/Grapple (restrain target, DR to escape)

**Support Abilities:**
- Heal Allies (restore HP)
- Buff Allies (+damage or +DV)
- Debuff Enemies (-damage or -DV)
- Summon Minions (add reinforcements)

---

## 2.6 Encounter Pacing

### Encounter Length Guidelines

**Short (2-3 rounds):**
- Good for: Random encounters, ambushes, minor obstacles
- Enemy count: 3-5 enemies
- Intensity: High, brutal

**Medium (4-6 rounds):**
- Good for: Standard combat, tactical challenges
- Enemy count: 5-8 enemies or 1 elite + minions
- Intensity: Moderate, with tactical choices

**Long (7-10 rounds):**
- Good for: Boss fights, climactic battles, set pieces
- Enemy count: Boss + minions + reinforcements
- Intensity: Varied, with phases or waves

**Very Long (10+ rounds):**
- Warning: Risk of player fatigue
- Only use for: Campaign climaxes, legendary encounters
- Must include: Multiple phases, environmental changes, high stakes

### Preventing Slog

If combat drags:
1. **Increase Damage:** Both sides deal more damage
2. **Reduce HP:** Cut enemy HP by 25-50%
3. **Add Reinforcements:** Fresh enemies to change dynamics
4. **Environmental Shift:** Collapsing floor, spreading fire
5. **Offer Escape:** Make retreat a viable option
6. **Narrate Conclusion:** "You defeat the remaining enemies"

---

## 2.7 Boss Design

Memorable bosses need more than high HP:

### The Three-Phase Boss

**Phase 1 (100-66% HP):**
- Standard attacks and abilities
- Establishes baseline threat
- Players learn patterns

**Phase 2 (66-33% HP):**
- Unlock new ability or tactic
- Environmental change
- Add minions or hazard

**Phase 3 (33-0% HP):**
- Desperate, more dangerous
- Strongest attacks
- Possible vulnerability
- Dramatic conclusion

### Boss Principles

**1. Telegraph Attacks**
- Describe boss winding up big attack
- Gives players round to respond
- Makes surviving feel earned

**2. Weak Points**
- Boss has vulnerability (takes 2× damage from specific source)
- Players must discover and exploit
- Rewards investigation and creativity

**3. Environmental Interaction**
- Boss uses terrain to advantage
- Players can turn environment against boss
- Makes encounter dynamic

**4. Thematic Abilities**
- Boss abilities reflect their nature
- Vampire lord: Blood drain, summon bats, dominate mind
- Hylden warlock: Entropy bolts, summon void creature, reality warp

**5. Solo Boss Survival**
- Legendary Actions: Act on player turns
- Damage Resistance: Half damage from certain types
- Regeneration: Heal each round
- Minions: Add reinforcements mid-fight

---

## 2.8 Non-Combat Encounters

Not every encounter needs swords:

### Social Encounters

**Structure:**
1. **Establish NPC Goal:** What do they want?
2. **Set Stakes:** What happens if negotiation fails?
3. **Player Approach:** How do PCs attempt to influence?
4. **Resolution:** Skill checks + roleplay

**Example Stakes:**
- Low: NPC tells truth or lies
- Medium: NPC offers aid or refuses
- High: NPC becomes ally or enemy

### Exploration Encounters

**Structure:**
1. **Present Mystery:** Locked door, ancient rune, hidden passage
2. **Offer Clues:** Observation checks reveal information
3. **Player Solution:** How do they solve it?
4. **Reward:** Access to new area, information, loot

**Puzzle Guidelines:**
- Multiple solutions possible
- Skills should be useful
- Failure has consequence, not just nothing
- Don't require real-world knowledge players lack

### Infiltration Encounters

**Structure:**
1. **Goal:** Get to specific location undetected
2. **Obstacles:** Guards, traps, locked doors
3. **Detection Mechanic:** Track alerts (3 alerts = discovered)
4. **Payoff:** Advantage if successful, combat if not

---

## 2.9 Adjusting on the Fly

Reading your table and adjusting mid-encounter:

### Encounter Too Easy?

**Quick Fixes:**
- Reinforcements arrive
- Enemy triggers alarm
- Boss uses hidden ability
- Environment becomes hazardous
- Time pressure added

### Encounter Too Hard?

**Quick Fixes:**
- Enemy HP lower than expected
- Ally arrives to help
- Environment helps PCs (pillar falls on enemies)
- Enemy morale breaks, some flee
- Offer parley or escape route

### How to Tell

**Too Easy Signs:**
- Players casually joking, not tactically thinking
- Enemies die in 1-2 hits
- PCs taking no significant damage
- Players seem bored

**Too Hard Signs:**
- Players frustrated, not engaged
- Multiple PCs downed
- Combat lasting 10+ rounds
- Players discussing giving up

---

## 2.10 Sample Encounters

The examples below illustrate how to build encounters for each difficulty band. Each creature entry lists its closest **Monster Manual equivalent** so GMs can use, scale, or replace these stat blocks directly with published entries.

**Using Monster Manual entries directly:** The MM chapters print benchmark TVs (0.25/1/2/4 for Chs 1–6; absolute values for Chs 7–9). To build an encounter using MM entries, total the printed TVs of all selected creatures and compare to the party TV thresholds in §2.1.

### Level 3 Party (4 PCs, Party TV = 12)

**Encounter: Vampire's Thralls (Challenging, TV 15)**

> **MM Cross-reference:** Use the Blooded Fledgling scaling option (MM Ch1, Vampire Fledgling entry, Elite TV 2) for the Spawn, or scale a Wight Lord (MM Ch1, Elite TV 2) to its Boss form (TV 4). Human Thralls map to Sarafan Footsoldiers (MM Ch3, Minion TV 0.25) or Commoners (MM Ch3, Minion TV 0.25). Adjust creature count to match the desired total TV.

- 1 Vampire Spawn (Elite, TV 6)
  - HP: 18, DV: 3, Armor: 1
  - Attack: 5d6, Damage: 6 Slashing
  - Ability: Blood Drain (heal 4 HP on hit)
- 3 Human Thralls (Standard, TV 3 each = 9 total)
  - HP: 10, DV: 2, Armor: 0
  - Attack: 4d6, Damage: 4 Bludgeoning
- **Terrain:** Crumbling mansion, pillars can be toppled
- **Tactics:** Spawn commands thralls to engage PCs while it targets isolated members

**All-MM equivalent (TV 13):** 1× Wight Lord (Boss variant, MM Ch1, TV 4) + 3× Vampire Fledglings (Standard, MM Ch1, TV 1 each) + 4× Deathguard Champions (Standard, MM Ch1, TV 1 each) + 8× Sarafan Footsoldiers (Minion, MM Ch3, TV 0.25 each). Total TV: 4 + 3 + 4 + 2 = 13.

---

### Level 8 Party (4 PCs, Party TV = 32)

**Encounter: Hylden War Machine (Challenging, TV 40)**

> **MM Cross-reference:** The Hylden Construct maps to the Pillar-Forged Warden (MM Ch5, Boss TV 4) scaled up for absolute level — use its TV 4 Boss scaling as printed and treat the extra HP and DV as justified by the party's level band. The Corrupted Cultist maps to a Rune-Forger (MM Ch5, Standard TV 1) or Corruption Host (MM Ch6, Standard TV 1). For a fully MM-sourced version, pair a Void-Spoken Oracle (MM Ch6, Boss TV 4) with a Master Rift Engineer (MM Ch6, Boss TV 4) and supporting Shock Troopers and Grunts.

- 1 Hylden Construct (Boss, TV 32)
  - HP: 60, DV: 6, Armor: 4
  - Attack: 10d6 (2 attacks/turn), Damage: 10 Force
  - Abilities: Energy Blast (AoE, 3d6 Lightning), Phase Shift (once per scene, become incorporeal)
- 1 Corrupted Cultist (Standard, TV 8)
  - HP: 20, DV: 4, Armor: 2
  - Attack: 7d6, Damage: 6 Soul
  - Ability: Entropic Curse (target -1 to rolls)
- **Terrain:** Ancient Hylden temple, glyph pillars that can be activated
- **Tactics:** Construct uses AoE to damage group, cultist debuffs the strongest PC

**All-MM equivalent (TV 40):** 1× Void-Spoken Oracle (Boss, MM Ch6, TV 4) + 1× Master Rift Engineer (Boss, MM Ch6, TV 4) + 2× Hylden Flesh Architects (Elite, MM Ch6, TV 2 each) + 4× Bio-Sigil Reavers (Elite, MM Ch6, TV 2 each) + 8× Hylden Shock Troopers (Elite, MM Ch6, TV 2 each) + 16× Hylden-Possessed Grunts (Minion, MM Ch6, TV 0.25 each). Total TV: 4 + 4 + 4 + 8 + 16 + 4 = 40. *Note: This composition is a full Hylden assault force; GMs should reduce scale for most sessions.*

---

### Level 15 Party (4 PCs, Party TV = 60)

**Encounter: Elder Vampire Lord (Legendary, TV 165)**

> **MM Cross-reference:** The Ancient Vampire Lord maps to a Legendary-tier result for the Vampire Beast Lord (MM Ch1) or Grave-Knight Warlord (MM Ch1) scaled far above their Boss (TV 4) baseline. For a fully MM-sourced encounter at this level, use entries from MM Ch9 (Legendary Entities) directly — these are written as absolute TV creatures in the TV 10–25 range. The Vampire Warriors map to high-scaling Grave-Knights or Deathguard Champions (both MM Ch1, Elite TV 2 base), used in large numbers.

- 1 Ancient Vampire Lord (Legendary, TV 90)
  - HP: 120, DV: 6, Armor: 3 (effective DV higher via lair blood pools and reactions)
  - Attack: 16d6 (3 attacks/turn), Damage: 14 Slashing + standard Bleeding
  - Abilities: 
    - Dominate (once per scene, control 1 PC for 1 round)
    - Mist Form (become incorporeal, heal 5 HP at the start of each turn)
    - Summon Bats (create difficult terrain, obscure vision)
    - Blood Frenzy (deal 2x damage while Bloodied)
  - Legendary Actions: Make 1 claw attack after each PC turn
- 5 Vampire Warriors (Standard, TV 15 each = 75 total)
  - HP: 30, DV: 6, Armor: 2
  - Attack: 12d6, Damage: 8 Slashing
- **Terrain:** Vampire Citadel throne room, elevated platforms, blood pools (heal vampires)
- **Phases:** 
  - Phase 1: Lord fights normally with warriors
  - Phase 2 (66% HP): Lord uses Dominate, summons bat swarm
  - Phase 3 (33% HP): Lord goes into Mist Form and Blood Frenzy
- **Win Condition:** Reduce lord to 0 HP (warriors flee if lord dies)

**All-MM equivalent (TV ~60):** Use Vorador (MM Ch9, TV as printed) or the Dimension Lord's peak scaling (MM Ch9) as the central threat. Pair with 6–8 Grave-Knights (MM Ch1, Elite TV 2 each = TV 12–16) and 20 Sarafan Footsoldiers (MM Ch3, Minion TV 0.25 each = TV 5). Adjust until the total reaches roughly 150% of party TV.

---

## 2.11 Quick Reference: Encounter Checklist

- [ ] Encounter has clear victory/defeat conditions
- [ ] Enemy count appropriate for party size
- [ ] Total threat value matches desired difficulty
- [ ] Enemies have distinct roles/abilities
- [ ] Environment provides tactical options
- [ ] Boss has at least 2 phases or legendary actions
- [ ] Non-combat resolution possible (if appropriate)
- [ ] Consequence for failure clear and interesting
- [ ] Reward for success proportional to risk
- [ ] Encounter advances story or reveals information

---

*"The best encounters aren't about defeating players—they're about giving players interesting choices under pressure."*
