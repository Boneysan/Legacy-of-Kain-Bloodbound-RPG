# Pillar Heath Seal-Breaker Push

- Arc: Convergence
- Recommended levels: 16-20
- Target TV: 59 listed roster, or 70+ if live reinforcement abilities are fully enabled
- Difficulty: Standard
- Use when: One battlefield front must decide whether the party's chosen ending can actually be executed.

## Location

- Site: Pillar Heath front line near the final rite position
- Terrain: Cracked Pillar trench, two rift pylons feeding the assault, unstable high ground holding the witness, Hall guide, or rite operator, and overlapping Material-Spectral pressure
- Pressure: This is a battlefield objective encounter; killing enemies matters only if the party can keep the rite or operator intact

## Monster Roster

| Creature | Count | TV Each | Total TV | Monster Source |
|:---|:---|:---|:---|:---|
| Hylden Dimension Lord | 1 | 18 | 18 | Monster_Manual/06_Hylden-Forces.md |
| Hylden Rift-Priest | 1 | 11 | 11 | Monster_Manual/06_Hylden-Forces.md |
| Hylden Shock Trooper | 2 | 9 | 18 | Monster_Manual/06_Hylden-Forces.md |
| Hylden-Possessed Grunt | 4 | 3 | 12 | Monster_Manual/06_Hylden-Forces.md |
| Optional Hylden War-Stalker | 1 | 7 | 7 | Monster_Manual/06_Hylden-Forces.md |
| Optional Wraith of the Abyss | 1 | 9 | 9 | Monster_Manual/02_Spectral-Entities.md |

## Encounter Objective

- Hold the operator zone for 4 rounds, destroy both pylons, or kill the Rift-Priest before the Dimension Lord can convert battlefield pressure into a permanent breach gain.

## Heart Purpose Guidance

- If the endgame answer is `spent-for-balance`, make the exposed operator a Pillar-aligned custodian, Hall guide, or rite anchor whose completion matters more than body count. The battlefield goal is to hold the operator zone long enough to finish the rite.
- If the endgame answer is `gate-opened-negotiated`, shift the objective toward controlled passage rather than closure. The party are protecting a managed opening, stated terms, or access geometry from panic, sabotage, or opportunistic seizure.
- If the endgame answer is `foreclosed`, make denial primary. The party should win by destroying pylons, breaking the priest's control geometry, or rendering the breach unusable before any faction can claim it.
- Hylden opposition intensity should scale inversely with how cooperative the gate resolution is. A negotiated opening wants sharper political pressure and fewer berserk surges; a foreclosed or forced ending wants the hardest direct assault.

## Running Notes

- The Dimension Lord is the anchor and should force the party off the objective rather than simply chase kills.
- The Rift-Priest contaminates the zone and opens movement breaks that make the pylons and operator vulnerable.
- Baseline mode: keep the listed roster fixed. Treat summon-style abilities and Dimensional Tether as battlefield pressure, threatened reinforcements, or narrative stakes rather than additional bodies on the map.
- Escalated mode: if you enable live reinforcements from the Dimension Lord or Rift-Priest, treat the front as a finale spike for level 18-20 parties or a heavily reinforced coalition and reduce pressure somewhere else in the overall endgame sequence.
- The Troopers and Grunts create time pressure; the optional War-Stalker makes the front more military, while the optional Wraith makes it feel more metaphysically ruptured.
- Tune visible instability or reinforcement pressure to match the endgame answer already chosen in the adjudication matrix.

## Objective Track

Track progress during play. Score 1 point per objective met.

- [ ] **Obj 1:** Hold the operator zone for 4 rounds without losing the rite anchor, operator, or zone control.
- [ ] **Obj 2:** Destroy both rift pylons.
- [ ] **Obj 3:** Kill or route the Rift-Priest before breach geometry locks.

**3/3 — Full success.** See **Outcome** block below.  
**2/3 — Partial.** See **Outcome** block below.  
**1/3 or 0/3 — Fail-forward.** See **Outcome** block below.

## Outcome

**Success (3/3):** The chosen ending executes fully. `heart_purpose` locks to the declared value; Hylden breach gains are contained or sealed. The Dimension Lord withdraws or is eliminated; the Pillar Heath front is no longer actively contested.

**Partial (2/3):** The ending executes but at coalition cost. One pylon remains cycling or the operator zone was briefly lost. `heart_purpose` locks with a rider condition — note in `heart_purpose_note` what was compromised (e.g., "rite executed with one pylon still cycling," "operator wounded before completion").

**Failure — fail-forward (1/3 or 0/3):** The Dimension Lord converts battlefield pressure into a breach gain; the party fall back. The chosen ending is still possible through `05_Last-Pursuit-or-Mercy-Scene.md` or a second push, but `heart_purpose` execution is delayed and under active opposition. Start Session 5 with the declared answer contested.