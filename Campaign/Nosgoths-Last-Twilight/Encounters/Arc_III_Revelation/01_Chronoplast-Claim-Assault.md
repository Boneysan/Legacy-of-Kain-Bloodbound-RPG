# Chronoplast Claim Assault

- Arc: Revelation
- Recommended levels: 11-15
- Target TV: 40 listed roster, or 49-54 if the Void-Touched uses its full summon kit
- Difficulty: Standard
- Use when: The Crimson Fracture tries to turn Chronoplast instability into proof that collapse is freedom.

## Location

- Site: Mirrored galleries and contradiction archives inside the Chronoplast
- Terrain: Collapsing sequence-bridges, exposed catwalks, spectral overlap, and one contradiction archive that can be sealed with a DR 4 Focus or Glyphcasting check
- Pressure: The party is not only trying to survive; they are trying to stop the Fracture from escaping with a clean narrative victory

## Monster Roster

| Creature | Count | TV Each | Total TV | Monster Source |
|:---|:---|:---|:---|:---|
| Fracture Void-Touched | 1 | 12 | 12 | Monster_Manual/01_Undead-and-Vampiric.md |
| Fracture Dimension-Walker | 2 | 9 | 18 | Monster_Manual/01_Undead-and-Vampiric.md |
| Fracture Zealot | 2 | 5 | 10 | Monster_Manual/01_Undead-and-Vampiric.md |
| Optional extra Dimension-Walker | 1 | 9 | 9 | Monster_Manual/01_Undead-and-Vampiric.md |

## Encounter Objective

- Preserve one usable contradiction, witness, or archive key while preventing the Fracture from escaping with a clean "the future is already broken" spectacle.

## State-Conditional Variants

### Choice A — Shard Scramble

- Trigger: `chronal_shard_fate: recovered` after viewing both futures.
- Objective shift: the Shard is a live contested objective, not background treasure.
- Play guidance: use carry, drop, seize, and line-of-retreat logic. If the carrier falls, everyone in the scene should know where the fight just moved.

### Choice B — Thess Pursuit

- Trigger: the party saw manipulation first and are hunting the operative or archive thief behind it.
- Objective shift: if the party break after the fleeing operative instead of holding the chamber, hand off to Encounters/Arc_III_Revelation/06_Curator-Thess-Pursuit.md rather than running this as a static hold.
- Play guidance: keep this file only if the pursuit never fully leaves the claim chamber. Once the chase becomes a deeper-archive run, swap to the dedicated pursuit encounter.

### Choice C — Touched PC Protection

- Trigger: one PC touched the Shard before interpretation stabilized.
- Objective shift: the touched PC becomes a secondary objective for both the Fracture and any opportunist in the room.
- Play guidance: isolate, drag, or force-disclose that PC rather than just damaging them. The fight should feel personally invasive.

### Choice D — Distributed Knowledge

- Trigger: `chronal_shard_fate: divided` or the party refused the machine's authority.
- Objective shift: protect notes, contradictions, and witnesses rather than one artifact.
- Play guidance: spread the objective across multiple archives or carriers so success is measured by how much usable truth survives, not whether one object stays in party hands.

## Running Notes

- Start with the Zealots and at least one Walker already contesting space.
- Bring the Void-Touched in after the party has committed to a lane.
- Baseline mode: use only the creatures listed in the roster. Do not add further bodies through Merge Protocol or summon-style actions; let the Void-Touched escalate the scene through timing, terrain, and split-realm pressure instead.
- Escalated mode: enable Merge Protocol and other live reinforcements only for level 13-15 parties or when the party has unusually strong allied support. In that mode, treat the encounter as a materially heavier fight than the listed baseline.
- For higher-level parties, either add the extra Walker or an active dimensional seam dealing 1 Spectral damage at the start of each turn to non-phased creatures on exposed catwalks, but avoid stacking every escalation at once unless you want a near-deadly set-piece.
- If `wheel_exposure: broken`, the Fracture are fighting over public proof and narrative advantage, not only loot. Make their dialogue and retreat choices reflect that.

## Objective Track

Track progress during play. Score 1 point per objective met.

- [ ] **Obj 1:** Secure one usable witness, contradiction, or archive key and keep it in party hands at scene end.
- [ ] **Obj 2:** Prevent the Fracture from exiting with clean narrative proof ("the future is already broken" does not become public fact).
- [ ] **Obj 3:** Exit the encounter with the party in good order — no PC stranded in a contested zone when the scene ends.

**3/3 — Full success.** See **Outcome** block below.  
**2/3 — Partial.** See **Outcome** block below.  
**1/3 or 0/3 — Fail-forward.** See **Outcome** block below.

## Outcome

**Success (3/3):** The party secure a usable contradiction, archive key, or witness while the Fracture withdraw empty-handed. `chronal_shard_fate` resolves to the party's chosen state. `party_operative_truth` is ready to lock if not already fixed; the Kain contract evaluation window opens.

**Partial (2/3):** The Fracture retreat but carry minor spectacle material, or the party's objective is secured with one carrier compromised or wounded. Advance to `05_Chronoplast-Exit-Fight.md` under moderate pressure; `party_operative_truth` holds but its public credibility is in question.

**Failure — fail-forward (1/3 or 0/3):** The Fracture escape with a workable proof-spectacle. The party hold the room but lose narrative control. Hand off to `05_Chronoplast-Exit-Fight.md` immediately under pursuit pressure. `wheel_exposure` advances one step; `party_operative_truth` remains `undecided` unless previously locked, and the Kain contract window narrows.
