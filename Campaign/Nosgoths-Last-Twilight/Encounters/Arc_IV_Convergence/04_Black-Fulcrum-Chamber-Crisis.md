# Black Fulcrum Chamber Crisis

- Arc: Convergence
- Recommended levels: 17-19
- Target TV: 13 Wheel package, 29 Hylden package, 22 Fracture package, 38 with the reinforced Hylden package
- Difficulty: Pressure
- Use when: The party's endgame direction needs to lock in under chamber pressure rather than only through debate.

## Location

- Site: Hall of Equilibrium approach and Black Fulcrum chamber
- Terrain: Answer-responsive stone, collapsing route control, spectral overlays, and faction pressure converging on the chamber from multiple angles
- Pressure: Chamber control and answer-shaping matter more than kill count; the roster should exist to force clarity, not replace it

## Monster Roster

| Creature | Count | TV Each | Total TV | Monster Source |
|:---|:---|:---|:---|:---|
| Silent Mourner | 1 | 7 | 7 | Monster_Manual/02_Spectral-Entities.md |
| Soul-Eater Shade | 2 | 3 | 6 | Monster_Manual/02_Spectral-Entities.md |
| Hylden Rift-Priest | 1 | 11 | 11 | Monster_Manual/06_Hylden-Forces.md |
| Hylden Shock Trooper | 2 | 9 | 18 | Monster_Manual/06_Hylden-Forces.md |
| Fracture Void-Touched | 1 | 12 | 12 | Monster_Manual/01_Undead-and-Vampiric.md |
| Fracture Zealot | 2 | 5 | 10 | Monster_Manual/01_Undead-and-Vampiric.md |
| Optional Hylden Shock Trooper | 1 | 9 | 9 | Monster_Manual/06_Hylden-Forces.md |

## Encounter Objective

- Hold chamber control long enough for the party to commit to what the Heart is for before the threatened bloc turns indecision into collapse, surrender, or rupture.

## Status-to-Framing Guidance

- If `black_fulcrum_status` is `cleared`, run the encounter as defense of a recognized account. Enemies are trying to break a standing judgment before it becomes executable.
- If `black_fulcrum_status` is `conditional`, have the opposition target the known incomplete portions of the party's account. The fight should pressure whatever the coalition could not fully answer.
- If `black_fulcrum_status` is `unfounded`, frame the room as a scramble for legitimacy without institutional protection. Every hostile move should imply that nobody will validate the party unless they do it themselves.

## Running Notes

- Use the Wheel, Hylden, or Fracture package based on which answer the party most threatens.
- If the coalition record entered the Hall as `witness-anchored`, the current Last Witness should be part of what the opposition can threaten, discredit, or force the party to protect.
- Baseline mode: keep the chosen package fixed and use the chamber itself as the real escalation engine.
- Reinforced mode: add the extra Shock Trooper or fold this directly into the Pillar Heath set-piece only if Session 3 is carrying the arc's main battle.
- Make every voiced answer change the room slightly so the choice feels mechanically present before it is final.

## Objective Track

Track progress during play. Score 1 point per objective met.

- [ ] **Obj 1:** Hold chamber control through hostile pressure — the enemy does not hold the room when the party's answer is declared.
- [ ] **Obj 2:** Declare the `heart_purpose` answer under hostile pressure before the threatened bloc forces collapse, surrender, or rupture.
- [ ] **Obj 3:** Keep the current Last Witness legible, unharmed, and in the party's custody at scene end.

**3/3 — Full success.** See **Outcome** block below.  
**2/3 — Partial.** See **Outcome** block below.  
**1/3 or 0/3 — Fail-forward.** See **Outcome** block below.

## Outcome

**Success (3/3):** The answer is committed cleanly with witnesses intact. `heart_purpose` locks to the declared value. Session 4 begins with the declared answer already confirmed and the coalition at highest available coherence.

**Partial (2/3):** The answer is committed but the opposition forced a concession. `heart_purpose` locks with a rider condition — note in `heart_purpose_note` what was compromised (e.g., "declared under Rift-Priest channeling," "Last Witness threatened before answer"). Session 4 begins with the answer in place but its legitimacy under active challenge.

**Failure — fail-forward (1/3 or 0/3):** Chamber control temporarily lost; the party declare under pressure with witnesses compromised. `heart_purpose` still locks but `black_fulcrum_status` becomes `unfounded`. Session 4 begins with the declared answer openly contested and coalition cohesion under visible strain.