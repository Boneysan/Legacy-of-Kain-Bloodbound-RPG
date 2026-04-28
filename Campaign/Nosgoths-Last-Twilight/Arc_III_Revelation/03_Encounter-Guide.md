# Arc III Encounter Guide

Use this document when Revelation needs concrete encounter planning for each session rather than only the Chronoplast compact template.

By default, Sessions 1, 2, and 5 are pressure scenes first and should not be treated as the arc's main stand-up combat unless you deliberately reinforce them.

Use the notes below as the GM-facing summary of both the current encounter files and the variant/trigger logic tracked in the encounter improvement plan.

Companion docs:

- [../Encounters/00_Encounter-Index.md](../Encounters/00_Encounter-Index.md)
- [../03_Vignette-Encounter-Improvement-Plan.md](../03_Vignette-Encounter-Improvement-Plan.md)

## Session 1: Time-Loop Skirmish

- Primary location: Time-scarred pass, dead observatory, or ruined Moebian approach site on the road to the Chronoplast.
- Primary encounter: Use Encounters/Arc_III_Revelation/02_Time-Loop-Skirmish.md.
- Recommended lineup: 1 Mirror Wraith and 2 Soul-Eater Shades.
- Scene weight: Secondary pressure scene by default, not the arc's main battle budget.
- Reaction Budget: 1 per PC per round. Mirror Wraith phase-shifts can force simultaneous Reaction decisions — note which PCs have spent before the Wraith repositions.
- Core objective: Force the party to retreat, regroup, or protect a witness while sequence itself stops behaving correctly.
- Terrain notes: Repeating corridors, duplicate tracks, and one route that only exists in the wrong order.
- Tone guidance: Choice A should foreground investigation. Choice B should foreground duplicate movement and route unreliability. Choice C should stay lighter on answers and heavier on withheld certainty.
- Reinforced option: Add 1 extra Mirror Wraith or 2 more Soul-Eater Shades if you want Session 1 to carry a fuller combat load.
- Alternate package: Replace the Mirror Wraith with 1 Silent Mourner if you want the scene to feel more tragic than predatory.

## Session 2: Burial Rite Interruption

- Primary location: Wheel-influenced refuge, mortuary chapel, or controlled mourning hall.
- Primary encounter: Use Encounters/Arc_III_Revelation/03_Burial-Rite-Interruption.md.
- Recommended lineup: 1 Silent Mourner bound into the rite and 2 Soul-Eater Shades feeding on the settlement's surrender logic from the edges of the scene.
- Scene weight: Social confrontation and pressure scene first, combat second.
- Reaction Budget: 1 per PC per round.
- Core objective: Expose whether the calm is chosen, coerced, or metaphysically enforced without reducing the Wheel's appeal to cartoon evil.
- Terrain notes: Ritual circles, confession alcoves, controlled candlelight, and civilians whose panic will change the politics of the room.
- Wheel-awareness note: If `wheel_exposure` is `named` or `broken`, frame the rite as a deliberate ideological staging ground rather than a surprise pastoral trap. If the cult already has personal relief data on the party, let Bale and the rite target specific emotional vulnerabilities rather than generic grief.
- Reinforced option: Add 1 Mirror Wraith if the Wheel package needs to function as a full combat rather than a ritual interruption.
- Alternate package: If you want less direct supernatural violence, treat the encounter as a rescue from ritual quieting with the Shades arriving only if the rite is disrupted.

## Session 3: Chronoplast Claim Assault

- Primary location: Mirrored galleries and contradiction archives inside the Chronoplast.
- Primary encounter: Use Encounters/Arc_III_Revelation/01_Chronoplast-Claim-Assault.md.
- Recommended lineup: 1 Fracture Void-Touched, 2 Fracture Dimension-Walkers, and 2 Fracture Zealots.
- Reaction Budget: 1 per PC per round. Dimension-Walkers can force multi-front pressure that creates Reaction competition between offensive and defensive options.
- Core objective: Protect meaning, witness, and the corrected northern breach record from becoming Fracture propaganda.
- Approach framing: Viewing both futures should make the Shard a live scramble objective. Seeing manipulation first should usually hand off to Encounters/Arc_III_Revelation/06_Curator-Thess-Pursuit.md; keep 01_Chronoplast-Claim-Assault.md only if the fight stays chamber-centered. Touching the Shard first should make the touched PC a protection objective. Refusing the machine's authority should reframe the scene around scattered notes and records rather than one artifact.
- Continuity note: Under the sequel pass, one of the machine's displayed futures should be the wrong-handed Reaver-shaped outcome the party may later commit to or reject.

## Session 4: Corridor of Contradictions

- Primary location: Split-history corridor, archive bridge, or accusation chamber where two versions of an event remain active at once.
- Primary encounter: Use Encounters/Arc_III_Revelation/04_Corridor-of-Contradictions.md.
- Recommended lineup: 1 Mirror Wraith, 1 Fracture Dimension-Walker, and one manipulated witness or betrayer whose position matters more than their damage output.
- Scene weight: Story confrontation first; use terrain instability and witness pressure to do as much work as the stat blocks.
- Reaction Budget: 1 per PC per round.
- Core objective: Protect the witness carrying the corrected northern breach record or expose the lie around it while terrain states, memory states, and faction agendas conflict openly.
- Terrain notes: Duplicate doors, phased cover, and history scars that change which path, ally, or enemy is currently real.
- Pursuit handoff: If Thess, the Witness, or the last missing record is still moving when Vignette 04 begins, start with Encounters/Arc_III_Revelation/06_Curator-Thess-Pursuit.md and let 04_Corridor-of-Contradictions.md resolve the testimony, custody, or accusation afterward.
- Betrayal-state guidance: If `betrayal_resolved` is unresolved, the tempted ally or missing record-carrier is the center of the scene. If absorbed, protect the ally and the corrected record against outside force. If severed, document custody replaces a person and the real objective is keeping the Resonance Pillar record legible. If weaponized, sharpen the scene into open retaliation rather than pastoral uncertainty.
- Alternate package: If the party avoid combat, run the same scene as a collapsing rite of false remembrance that still costs them a relationship or alliance.

## Session 5: Chronoplast Exit Fight

- Primary location: Extraction route out of the Chronoplast, archive lift, or collapsing sequence bridge leading back toward the Material.
- Primary encounter: Use Encounters/Arc_III_Revelation/05_Chronoplast-Exit-Fight.md.
- Recommended lineup: Choose the bloc that best represents who is trying to define the arc's ending.
- Scene weight: Secondary pressure scene by default unless you deliberately make the escape itself the session's main fight.
- Reaction Budget: 1 per PC per round.
- Fracture package: 2 Fracture Zealots and 1 Fracture Dimension-Walker trying to seize the spectacle of collapse.
- Wheel package: 2 Soul-Eater Shades and 1 Silent Mourner or Wheel-bound spectral echo enforcing surrender through fear and exhaustion.
- Core objective: End Arc III on commitment and leverage, not simple victory over a final health pool.
- Package selection: If `wheel_exposure` is `broken`, prefer the Fracture package as retaliation or suppression. If `party_operative_truth` is balance-through-sacrifice or hylden-reintegration, the Wheel is morally weakened and Fracture pressure usually fits better. If the party stayed undecided, choose whichever bloc better exploits structural weakness. Treat this as pressure on the Kain contract window, not as a direct on/off Kain trigger.
- Reinforced option: Add 1 Mirror Wraith to either package, or pair the route with repeating environmental Spectral damage, if you want the exit to be a true primary combat.
- Terrain notes: Unstable bridges, collapsing futures, and one last omen that points toward Convergence.