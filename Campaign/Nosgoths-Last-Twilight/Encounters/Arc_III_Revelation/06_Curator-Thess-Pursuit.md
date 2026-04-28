# Curator Thess Pursuit

- Arc: Revelation
- Recommended levels: 12-14
- Target TV: 19 plus archive-collapse pressure
- Difficulty: Pressure
- Use when: The party exposes Moebian-adjacent manipulation and breaks after Curator Thess or the fleeing record bundle before the deeper archive can erase the proof.

## Location

- Site: Deeper Chronoplast archive, mirror-stack catwalks, or contradiction catalog lanes behind the main chamber
- Terrain: Sliding ladders, narrow bridges over collapsing stacks, seal-glyph doors, and one live purge lane that can erase records or strand pursuers
- Pressure: Thess is trying to decide which version of history survives. The party must catch the operative or seize the record case before the archive closes around it.

## Monster Roster

| Creature | Count | TV Each | Total TV | Monster Source |
|:---|:---|:---|:---|:---|
| Fracture Dimension-Walker | 1 | 9 | 9 | Monster_Manual/01_Undead-and-Vampiric.md |
| Fracture Zealot | 2 | 5 | 10 | Monster_Manual/01_Undead-and-Vampiric.md |
| Optional Mirror Wraith | 1 | 10 | 10 | Monster_Manual/02_Spectral-Entities.md |

## Encounter Objective

- Catch Curator Thess alive or secure the manipulated record case before it is burned, misfiled, or carried beyond any legible route back.

## State-Conditional Variants

### Thess Present

- Trigger: Curator Thess exists in the campaign and ran from the manipulated mirror-stack.
- Objective shift: The party is hunting a living archivist who wants survival and authorship more than open battle.
- Play guidance: Thess should spend turns opening false lanes, dropping catalog stacks, or threatening the proof rather than trading damage. If cornered with a plausible bargain, she talks.

### Document Trail Only

- Trigger: Thess was removed from the arc or never surfaced as a tracked NPC.
- Objective shift: Replace the operative with a fleeing case, glyph relay, or self-writing query bundle carrying the fabricated sequence.
- Play guidance: The same terrain applies, but the chase is about intercepting evidence before purge logic or an offscreen handler destroys it.

### Broken Wheel Cover

- Trigger: `wheel_exposure: broken`.
- Objective shift: Preserving legible proof matters more than killing escorts.
- Play guidance: Enemy actions should prioritize burning, scattering, or reordering records. A tactical win with the evidence lost should still feel like failure.

## Running Notes

- One route should always remain open. If every lane seals, the encounter stops reading like a pursuit and collapses into a static brawl.
- The Walker is the route-breaker. Use it to phase through cover, pull open contradiction seams, and force the party to split.
- The Zealots are there to delay, shove, and cut off the clean lane to Thess, not to stand in formation.
- If `chronal_shard_fate: recovered`, let one escort peel toward the Shard carrier while Thess keeps moving. The party should feel the cost of chasing proof while holding another dangerous proof-object.
- Resolve the chase into one of three outputs: Thess caught with proof, proof caught without Thess, or proof partially lost. That output determines who speaks first in Vignette 04.
- Do not end on a corpse unless you want Arc III to become strictly documentary. The richer result is live capture, partial escape, or evidence seized at a cost.
- If the party catch Thess quickly, the real reward is live explanation and clean custody of the records. Move straight into Vignette 04 or Encounters/Arc_III_Revelation/04_Corridor-of-Contradictions.md once the chase resolves.
- If you need a heavier combat, add the Mirror Wraith as the archive's unstable memory made hostile, but only if the scene still preserves movement.

## Objective Track

Track progress during play. Score 1 point per objective met.

- [ ] **Obj 1:** Catch Curator Thess alive.
- [ ] **Obj 2:** Secure the record case intact — not burned, misfiled, or split beyond recovery.
- [ ] **Obj 3:** Preserve at least one confirming detail beyond the record case (archive route, secondary copy, or testimony fragment).

**3/3 — Full success.** See **Outcome** block below.  
**2/3 — Partial.** See **Outcome** block below.  
**1/3 or 0/3 — Fail-forward.** See **Outcome** block below.

## Outcome

**Success (3/3):** Thess is caught alive with the record case; the party control both witness and proof. Session 4 opens with full custodial advantage. `betrayal_resolved` can reach any value, including `weaponized` if the party use live testimony aggressively.

**Partial (2/3):** Proof secured without Thess, or Thess caught but records only partially intact. One confirming detail is degraded, reframed, or separated from its most authoritative interpreter. `betrayal_resolved` can reach `absorbed` or `severed` but not easily `weaponized`.

**Failure — fail-forward (1/3 or 0/3):** Thess escapes; the record case is partially burned or scattered. At least one fragment survives in party hands — carry it physically into Session 4 as the proof object. `betrayal_resolved` can only reach `severed` (documentary) or `absorbed` (incomplete); live testimony is off the table.