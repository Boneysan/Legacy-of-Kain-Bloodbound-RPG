# Chapter 2: Encounter Design

Creating balanced, engaging encounters is an art. This chapter provides tools and guidelines for crafting memorable combat and challenges in Nosgoth.

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

### Basic Enemy TV

| Enemy Type | TV Multiplier |
|-----------|--------------|
| **Minion** (1-2 HP, weak attacks) | 0.25× character level |
| **Standard Enemy** (average stats) | 1× character level |
| **Elite Enemy** (stronger stats, special abilities) | 1.5× character level |
| **Boss** (major threat, multiple abilities) | 3-4× character level |
| **Legendary** (campaign antagonist) | 5-10× character level |

### Quick Enemy Stat Creation

**Minion (TV 0.25):**
- HP: 1-2
- DV: 1 + (party level ÷ 4)
- Armor: 0
- Attack: Party level d6 (1 attack)
- Damage: 2-3

**Standard Enemy (TV 1):**
- HP: 4 + (2 × party level)
- DV: 2 + (party level ÷ 3)
- Armor: 0-2
- Attack: (Party level + 2) d6
- Damage: 4-6

**Elite Enemy (TV 1.5):**
- HP: 8 + (3 × party level)
- DV: 3 + (party level ÷ 2)
- Armor: 2-3
- Attack: (Party level + 3) d6
- Damage: 6-8
- Special: 1-2 unique abilities

**Boss (TV 3-4):**
- HP: 20 + (5 × party level)
- DV: 4 + (party level ÷ 2)
- Armor: 3-4
- Attack: (Party level + 4) d6, 2 attacks per turn
- Damage: 8-12
- Special: 3-4 unique abilities, resistance to 1-2 damage types

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
- Count each legendary action as +0.5 TV

**Option 3: Multi-Attack**
- Boss makes 2-3 attacks per Action
- Increases effective TV by 50% per extra attack

**Option 4: Reaction Abilities**
- Boss can use Reaction multiple times per round
- Example: "Parry—reduce incoming damage by 5 (3 times per round)"

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
- Examples: Fire pits (2 Fire damage/round), corrupted pools (DR 2 save or 1 Corruption)
- **Tactical Use:** Area denial, force positioning choices

**Elevated Terrain**
- +1 success on attacks from high ground
- +1 DR to hit target on high ground
- **Tactical Use:** Powerful defensive position

**Cover**
- Half cover: +1 DR to be hit by ranged/spells
- Full cover: +2 DR to be hit by ranged/spells
- **Tactical Use:** Protects ranged enemies, encourages flanking

### Interactive Elements

Add objects players can interact with:
- **Pillars/Columns:** Can be toppled (DR 3 Might check, 4d6 damage in line)
- **Chandeliers:** Can be dropped on enemies (DR 2, 3d6 damage in area)
- **Levers/Switches:** Change battlefield (open pits, seal doors)
- **Barrels/Crates:** Can be used as cover or thrown (improvised weapon)

### Environmental Hazards

| Hazard | Effect | DR/Damage |
|--------|--------|-----------|
| Crumbling Floor | Save or fall through | DR 2 Evasion, 2d6 falling damage |
| Collapsing Ceiling | Area damage | DR 3 Evasion or 4d6 bludgeoning |
| Spectral Rift | Pull toward Spectral Realm | DR 2 Will or phased for 1 round |
| Corrupted Aura | Gain Corruption | DR 2 Will or +1 Corruption |
| Poison Gas | Ongoing damage | 2 damage/round, DR 2 Might to resist |

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
- Regeneration (restore X HP per round)
- Damage Resistance (half damage from specific type)
- Reactive Armor (damage attackers who hit in melee)
- Phase Shift (become incorporeal, 1/scene)

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

### Level 3 Party (4 PCs, Party TV = 12)

**Encounter: Vampire's Thralls (Standard, TV 12)**
- 1 Vampire Spawn (Elite, TV 4.5)
  - HP: 18, DV: 3, Armor: 1
  - Attack: 5d6, Damage: 6 Slashing
  - Ability: Blood Drain (heal 4 HP on hit)
- 3 Human Thralls (Standard, TV 2.5 each = 7.5 total)
  - HP: 10, DV: 2, Armor: 0
  - Attack: 4d6, Damage: 4 Bludgeoning
- **Terrain:** Crumbling mansion, pillars can be toppled
- **Tactics:** Spawn commands thralls to engage PCs while it targets isolated members

### Level 8 Party (4 PCs, Party TV = 32)

**Encounter: Hylden War Machine (Challenging, TV 40)**
- 1 Hylden Construct (Boss, TV 28)
  - HP: 60, DV: 6, Armor: 4
  - Attack: 10d6 (2 attacks/turn), Damage: 10 Force
  - Abilities: Energy Blast (AoE, 3d6 Lightning), Phase Shift (1/scene, become incorporeal)
- 3 Corrupted Cultists (Standard, TV 4 each = 12 total)
  - HP: 20, DV: 4, Armor: 2
  - Attack: 7d6, Damage: 6 Soul
  - Ability: Entropic Curse (target -1 to rolls)
- **Terrain:** Ancient Hylden temple, glyph pillars that can be activated
- **Tactics:** Construct uses AoE to damage group, cultists debuff strongest PCs

### Level 15 Party (4 PCs, Party TV = 60)

**Encounter: Elder Vampire Lord (Deadly, TV 90)**
- 1 Ancient Vampire Lord (Legendary, TV 75)
  - HP: 120, DV: 9, Armor: 3
  - Attack: 16d6 (3 attacks/turn), Damage: 14 Slashing + Bleeding
  - Abilities: 
    - Dominate (1/scene, control 1 PC for 1 round)
    - Mist Form (become incorporeal, heal 5 HP/round)
    - Summon Bats (create difficult terrain, obscure vision)
    - Blood Frenzy (deal 2× damage when below 50% HP)
  - Legendary Actions: Make 1 claw attack after each PC turn
- 5 Vampire Warriors (Standard, TV 3 each = 15 total)
  - HP: 30, DV: 6, Armor: 2
  - Attack: 12d6, Damage: 8 Slashing
- **Terrain:** Vampire Citadel throne room, elevated platforms, blood pools (heal vampires)
- **Phases:** 
  - Phase 1: Lord fights normally with warriors
  - Phase 2 (66% HP): Lord uses Dominate, summons bat swarm
  - Phase 3 (33% HP): Lord goes into Mist Form and Blood Frenzy
- **Win Condition:** Reduce lord to 0 HP (warriors flee if lord dies)

---

## Quick Reference: Encounter Checklist

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
