# Vignette–Encounter Improvement Plan

Captures every gap between what the Detailed Consequence Matrices promise and what the encounter files actually support. Each item is a concrete edit to an existing encounter file (or, in one case, a possible new file). Items are grouped by priority.

## How to Use This Document

1. Pick an item. Read the encounter file and the matching matrix entry side-by-side.
2. Add the described section or note directly into the encounter file.
3. Mark the item **Implemented** and note the commit.
4. After each arc's items are done, re-read that arc's Encounter Guide to make sure any new trigger conditions or variant names are reflected there too.

---

## Priority Legend

| Priority | Meaning |
|----------|---------|
| MAJOR | Encounter needs fundamentally different objective framings the matrix promises — full variant-section work |
| SIGNIFICANT | Encounter needs new conditional sections for distinct choice paths |
| MODERATE | Encounter needs brief conditional notes tied to state tags |
| MINOR | Encounter mostly works; needs small trigger-condition or framing additions |

---

## MAJOR

### M-1 — Breach on the Northern Ice needs 4 objective variants

Status: Implemented

File: `Encounters/Arc_II_Ascension/03_Breach-on-the-Northern-Ice.md`
Matrix source: Arc II V05 — The Breach Answer (Choices A–D)

Problem:
The matrix promises 4 fundamentally different encounter shapes based on the party's Breach Answer:

- **Choice A (Seal):** seal-hold finish — party fights to stabilize and close the breach
- **Choice B (Redirect):** door-building crisis — party fights to keep a controlled passage open under hostile conditions
- **Choice C (Destroy Ember):** denial-and-survival scene — party destroys their own instrument and retreats
- **Choice D (Let it Fail):** catastrophe management — party tries to limit damage from an uncontrolled collapse

The encounter currently has one fixed 2-Shock-Trooper roster and one generic objective ("Shut the breach, save the possessed, or retreat with proof"). No variant sections exist.

Required changes:
- Add a `## State-Conditional Objectives` section with 4 blocks keyed to the party's breach answer
- Each block needs: restated objective, terrain behavior changes, success/failure conditions
- Seal and Door variants may share the base roster; Denial should de-escalate to retreat-under-fire; Catastrophe should add reinforcement pressure or environmental hazard escalation
- Running Notes should reference `hylden_engagement` tag values to select the correct block

---

### M-2 — Chronoplast Claim Assault needs choice-driven variants

Status: Implemented

File: `Encounters/Arc_III_Revelation/01_Chronoplast-Claim-Assault.md`
Matrix source: Arc III V03 — What the Machine Shows (Choices A–D)

Problem:
The matrix promises 4 distinct encounter framings:

- **Choice A (View both futures):** Shard is a live scramble objective; party certainty already destabilized
- **Choice B (See manipulation first):** pursuit branch toward Curator Thess; this is a hunt, not a hold
- **Choice C (Touch Shard first):** personal-protection angle around the touched PC; stronger theft motive from Silk-Without-Moon
- **Choice D (Refuse machine's authority):** distributed knowledge, not artifact-centered; less decisive but more defensible

The encounter has one fixed Fracture roster and one generic objective. No mention of the Shard as an objective, no Thess pursuit branch, no PC-protection variant, no artifact-vs-knowledge framing toggle.

Required changes:
- Add a `## State-Conditional Variants` section with at least 3 blocks keyed to `chronal_shard_fate` and `wheel_exposure`
- Choice A: add the Shard as a contested terrain objective with carry/drop/seize mechanics
- Choice B: add a Thess pursuit branch — either as a full variant within this file or as a separate encounter file (see item N-1). The objective shifts from "hold the Fracture" to "catch the fleeing operative before she reaches cover"
- Choice C: name the touched PC as a secondary objective the Fracture and Silk-Without-Moon both want to isolate
- Choice D: reframe the objective around scattered notes and records rather than a single artifact

---

## SIGNIFICANT

### S-1 — Sanguine Extraction Standoff needs custody-framing variants

Status: Implemented

File: `Encounters/Arc_I_Awakening/06_Sanguine-Extraction-Standoff.md`
Matrix source: Arc I V05 — Who Carries the Knot (Choices A–D)

Problem:
The matrix promises 4 different operational objectives:

- **Choice A (Party keeps Knot):** custody defense — party holds against cult and Sarafan simultaneously
- **Choice B (Entrust to Serit):** Accord extraction — protect Serit's exit route with the Knot
- **Choice C (Conceal/neutral holder):** concealment retreat — hide the Knot and escape without revealing the holder
- **Choice D (Faction vote):** public claim scene — open standoff where every faction knows the stakes

The encounter treats the standoff as a single three-sided fight. Running Notes don't differentiate these 4 framings.

Required changes:
- Add a `## Framing by Custody State` section with 4 blocks
- Each block should restate the objective, note which NPCs are hostile/neutral/allied, and specify whether the Inquisitor acts as opponent or co-claimant
- Choice C should note conditions under which the encounter is partially or fully skipped (successful concealment)

---

### S-2 — The Healer's Smile needs vignette entry conditions

Status: Implemented

File: `Encounters/Arc_I_Awakening/02_The-Healers-Smile.md`
Matrix source: Arc I V02 — The False Refuge (Choices A–D)

Problem:
The matrix promises 4 refuge scenarios:

- **Choice A (Accept fully):** low collateral, cult has initiative inside the shelter
- **Choice B (Accept with guards):** layered social pressure, isolated first-watch PC is the target
- **Choice C (Challenge publicly):** immediate refuge clash with fleeing civilians, panic framing
- **Choice D (Split party):** separated information, hidden side entrance, reunion under pressure before the encounter fires

The encounter has one framing. Notes mention a chase variant but not these 4 entry conditions.

Required changes:
- Add a `## Vignette Entry Conditions` section with 4 blocks
- Each block should state the opening position, cult tactics adjustment, and civilian disposition
- Choice C should note that `public_story: panic` may also trigger 03_Purge-at-First-Light as a follow-on

---

### S-3 — Cathedral Road Ambush needs Serit participation notes

Status: Implemented

File: `Encounters/Arc_I_Awakening/01_Cathedral-Road-Ambush.md`
Matrix source: Arc I V01 — The Caravan Argument (Choices A–D)

Problem:
The matrix promises different Serit behavior:

- **Choice A (Press on):** run without Serit's warning beat; party arrives exhausted
- **Choice B (Camp at shrines):** add a cult watcher to the ambush; plan for Purge later
- **Choice D (Question Serit directly):** Serit gets a warning beat and body-blocks one early shadow move

The encounter never mentions Serit. No watcher variant exists.

Required changes:
- Add a `## Serit Participation` note (3-4 bullets) explaining when she warns, body-blocks, or is absent
- Add a `## Watcher Add` note for Choice B explaining the cult watcher's behavior and how it seeds later Sarafan pressure
- Note that Choice A should impose exhaustion or reduced rest benefits on the party

---

### S-4 — Iron Echo Chamber Crisis needs approach-framing variants

Status: Implemented

File: `Encounters/Arc_II_Ascension/06_Iron-Echo-Chamber-Crisis.md`
Matrix source: Arc II V03 — What Command Sounds Like (Choices A–D)

Problem:
The matrix promises 4 approach framings:

- **Choice A (Claimant's rep):** judgment and immediate backlash — the Echo answers and rivals react
- **Choice B (Party's own name):** politically unstable contested escort — everyone wants to court or fear the party
- **Choice C (Refuse contact):** refusal scene, not coronation — fragment stays inert, travel pressure replaces fortress scenes
- **Choice D (Expose oathbreaker):** one person's standing collapses — chamber answers with cracked ruling

The encounter has a generic undead roster. Notes vaguely mention "Add claimant champions, rival retainers, or a saboteur" without connecting to these 4 framings.

Required changes:
- Add a `## Chamber Approach Framing` section with 4 blocks keyed to `iron_echo_status` and `fortress_claim`
- Each block should specify the objective shift, whether to add a political NPC to the roster, and who the politically dangerous faction is
- Choice C should note that combat may be replaced entirely by a departure/travel-pressure scene

---

### S-5 — Rift-Line Emergency needs Hylden engagement toggle

Status: Implemented

File: `Encounters/Arc_II_Ascension/04_Rift-Line-Emergency.md`
Matrix source: Arc II V04 — What the Glass Voice Offers (Choices A–D)

Problem:
The matrix promises a critical mechanical toggle:

- **Choice A (Refuse negotiation):** no redirection option; less reliable seal data; Corruption cost higher
- **Choice B (Engage logic):** redirect option becomes technically available; political cost noted
- **Choice C (Ask what it needs):** door-not-wall logic permanently unlocked; breach descriptions change
- **Choice D (Accuse):** stronger adversarial respect; more precise Hylden counterplay

The encounter has terrain mechanics (stabilize/sabotage/shatter pylons) but no explicit "redirect option" that appears or disappears based on `hylden_engagement`.

Required changes:
- Add a `## Hylden Engagement Toggle` section
- Define what the redirect option mechanically is (e.g., a DR 4 Glyphcasting check to convert a pylon into a controlled passage node)
- State when it's available (`hylden_engagement: negotiated`) and what's lost when absent (`hylden_engagement: none` — no redirect check, seal data is less reliable so stabilization DRs increase by 1)
- Note Choice D's effect: Hylden use more precise counterplay (focused targeting of whoever negotiated)

---

## MODERATE

### MOD-1 — Burial Rite Interruption needs Wheel-awareness toggle

Status: Not started

File: `Encounters/Arc_III_Revelation/03_Burial-Rite-Interruption.md`
Matrix source: Arc III V01-D, V02-B, V02-D

Problem:
If `wheel_exposure ≥ named`, the encounter should be framed as a known ideological staging ground rather than a surprise pastoral trap. If V02-D was chosen, the Wheel already knows each character's preferred relief.

Required changes:
- Add 2-3 lines in Running Notes: "If `wheel_exposure` is `named` or `broken`, frame the rite as a deliberate staging ground, not a surprise. If the Wheel already has personal data on the party (V02-D), Bale targets specific emotional vulnerabilities rather than generic grief."

---

### MOD-2 — Time-Loop Skirmish needs tone-by-approach guidance

Status: Not started

File: `Encounters/Arc_III_Revelation/02_Time-Loop-Skirmish.md`
Matrix source: Arc III V01 (Choices A–C)

Problem:
The matrix promises 3 tone variants:

- Choice A: investigative framing
- Choice B: duplicate movement and route unreliability foregrounded
- Choice C: lighter on answers, stronger on withheld certainty

Required changes:
- Add a `## Tone Guidance by Approach` block with 3 bullets matching the above

---

### MOD-3 — Corridor of Contradictions needs betrayal-state guidance

Status: Not started

File: `Encounters/Arc_III_Revelation/04_Corridor-of-Contradictions.md`
Matrix source: Arc III V04 — The Name in the Archive

Problem:
The encounter says "Keep the key witness, betrayer, or contradiction alive" but doesn't specify who fills those roles based on `betrayal_resolved`.

Required changes:
- Add guidance: if `betrayal_resolved: unresolved`, the tempted ally is the central figure; if `absorbed`, the ally is present but the wound is named — protect them against external threats; if `severed`, document custody replaces a person entirely — the objective becomes keeping records legible; if `weaponized`, the encounter is sharper and less pastoral — open retaliation framing

---

### MOD-4 — Endgame Parley Break needs package-selection guidance

Status: Not started

File: `Encounters/Arc_IV_Convergence/02_Endgame-Parley-Break.md`
Matrix source: Arc IV V01 (Choices A–D)

Problem:
Has Sarafan vs. Fracture break packages but no guidance on which to use based on `coalition_shape`.

Required changes:
- Add a `## Package Selection by Coalition State` block:
  - `unified-pending` → Fracture break (test the center)
  - `contested-opening` → Sarafan break (exploit missing anchor)
  - `internally-fractured-but-functioning` → whichever faction can peel the diverging member
  - `merel-advised` → whichever faction the private approach threatened

---

### MOD-5 — Pillar Heath Seal-Breaker Push needs heart_purpose guidance

Status: Not started

File: `Encounters/Arc_IV_Convergence/01_Pillar-Heath-Seal-Breaker-Push.md`
Matrix source: Arc IV V05 — The Heart Is For

Problem:
Notes say "Tune visible instability or reinforcement pressure to match the endgame answer" without specifying how.

Required changes:
- Add a `## Heart Purpose Guidance` block:
  - `spent-for-balance` → rite operator is a Pillar-aligned custodian; objective is to hold for completion
  - `gate-opened-negotiated` → operator is managing a passage opening; objective shifts to controlled breach, not closure
  - `foreclosed` → objective is denial; destroy pylons rather than hold them
  - Note that the Hylden opposition intensity should scale inversely with how cooperative the gate resolution is

---

### MOD-6 — Road to the Hall needs state-to-package mapping

Status: Not started

File: `Encounters/Arc_IV_Convergence/03_Road-to-the-Hall.md`
Matrix source: Arc IV V02, V03

Problem:
Has metaphysical vs physical packages but no table mapping state to package selection.

Required changes:
- Add a `## Package Selection` block:
  - `coalition_shape: recognized` + `black_fulcrum_status: active` → physical package (test the line, not the legitimacy)
  - `coalition_shape: conditionally-recognized` → metaphysical package (the path judges prior choices)
  - Procession-neutral result from V03 → remove one logistics complication from the physical package

---

## MINOR

### m-1 — Purge at First Light needs trigger conditions

Status: Not started

File: `Encounters/Arc_I_Awakening/03_Purge-at-First-Light.md`

Required change:
- Add a `## Trigger Conditions` note: "Fire this encounter when `public_story = panic` or `open_truth`, or when `sarafan_attention ≥ 2`. If none of these are true, the Purge stays in reserve."

---

### m-2 — Blood-Well Chamber Defense needs personal-contact hook

Status: Not started

File: `Encounters/Arc_I_Awakening/05_Blood-Well-Chamber-Defense.md`
Matrix source: Arc I V04-C

Required change:
- Add a Running Note: "If V04-C was chosen (Follow the Vision's Pull), use the chain, mark, or ancestral symbol from that vision as the clearest direct-contact hook in the chamber terrain. The relic station that matches the vision should be the most dangerous and most rewarding point in the room."

---

### m-3 — Avernus Exit Pursuit needs skip-condition note

Status: Not started

File: `Encounters/Arc_I_Awakening/07_Avernus-Exit-Pursuit.md`
Matrix source: Arc I V05-C

Required change:
- Add a Running Note: "If V05-C concealment holds and no witnesses survived, skip this encounter entirely. Only trigger if the hiding place is seen, guessed, or betrayed."

---

### m-4 — Empty Throne Gate needs flex-slot guidance

Status: Not started

File: `Encounters/Arc_II_Ascension/01_Empty-Throne-Gate.md`
Matrix source: Arc II V01

Required change:
- Expand the flex elite entry: "If `fortress_claim` favors Turel, fill the flex slot with Drath's champion or retainer. If it favors Drath, use Turel's side. If `fortress_claim: neutral_brokered` or `unsettled`, use Corin Vey's proxy or a local opportunist."

---

### m-5 — Fortress Gate Purge needs trigger conditions

Status: Not started

File: `Encounters/Arc_II_Ascension/02_Fortress-Gate-Purge.md`

Required change:
- Add a `## Trigger Conditions` note: "Fire when Sarafan hardliners use a public endorsement, exposure, or institutional collapse as justification for intervention at the threshold. Most commonly triggered by V01-A (public Turel endorsement), V02-D (public exposure of the loyalty task), or V01-D (institutional cover collapse)."

---

### m-6 — Chronoplast Exit Fight needs state-to-package mapping

Status: Not started

File: `Encounters/Arc_III_Revelation/05_Chronoplast-Exit-Fight.md`

Required change:
- Add 2-3 lines in Running Notes: "If `wheel_exposure = broken`, use the Fracture package framed as retaliation or suppression. Map `party_operative_truth` to package: balance-through-sacrifice or hylden-reintegration → Fracture package (Wheel is morally weakened); undecided → either package based on which bloc feels more immediately dangerous."

---

### m-7 — Black Fulcrum Chamber Crisis needs status-to-framing table

Status: Not started

File: `Encounters/Arc_IV_Convergence/04_Black-Fulcrum-Chamber-Crisis.md`

Required change:
- Add a brief framing note: "`black_fulcrum_status: cleared` → encounter is defense of a recognized account; `conditional` → opposition targets the known incomplete portions; `unfounded` → scramble for legitimacy without institutional protection."

---

### m-8 — Last Pursuit or Mercy Scene needs antagonist guidance

Status: Not started

File: `Encounters/Arc_IV_Convergence/05_Last-Pursuit-or-Mercy-Scene.md`

Required change:
- Add guidance: "Fill the hunt package with whichever major antagonist survived the endgame: Elain if the Wheel was broken but she escaped; a Fracture remnant if `wheel_final_state` left the Fracture operational; a Hylden commander if `hylden_gate_resolution` was sealed by force. Use 1-2 escorts from that faction's roster."

---

## POSSIBLE NEW FILE

### N-1 — Curator Thess Pursuit (Arc III)

Status: Not started — decide whether to create or fold into M-2

Matrix source: Arc III V03-B

Problem:
The matrix says "Route directly into 01_Chronoplast-Claim-Assault.md or a pursuit branch toward Curator Thess." No such pursuit encounter exists. The Thess chase is mechanically distinct from a Fracture hold-and-defend — it's a hunt through collapsing archive corridors against a fleeing operative, not a fixed-position defense.

Options:
- **Option A:** Create `Encounters/Arc_III_Revelation/06_Curator-Thess-Pursuit.md` as a dedicated chase encounter with its own terrain, objective, and roster
- **Option B:** Fold the pursuit into 01_Chronoplast-Claim-Assault.md as a dedicated variant branch within the State-Conditional Variants section (item M-2)

Recommendation: Option B if the pursuit can share the same roster with modified positioning and objective. Option A if the chase needs its own terrain, pacing, and smaller roster.

---

## Cross-Reference Checklist

After implementing encounter-file changes, also update:

- [ ] Arc I `03_Encounter-Guide.md` — reflect any new trigger conditions or variant names
- [ ] Arc II `03_Encounter-Guide.md` — reflect Breach variants and Hylden toggle
- [ ] Arc III `03_Encounter-Guide.md` — reflect Chronoplast variants and possible new file
- [ ] Arc IV `04_Encounter-Guide.md` — reflect package-selection tables
- [ ] `Encounters/00_Encounter-Index.md` — add any new encounter files

---

## Consequence Carry-Through Audit

*Added April 2026 — findings from a full 20-vignette logical flow review.*

### Within-Arc Chains: Working

Tag chains are tight within each arc. Set-and-consume sequences are explicit in every Next-Scene Effects table and downstream vignettes reference them by name. Examples:

- `serit_trust` threads through all five Arc I vignettes
- `fortress_claim` is set in Arc II V01 and consumed in V02–V03 and V05
- `betrayal_resolved` accumulates from Arc III V01 through V04
- `coalition_shape` is set in Arc IV V01 and touched by every subsequent Arc IV vignette

The Arc IV Fulcrum examination (V04) is the strongest cross-arc mechanism in the campaign — it explicitly reads four arc-state tags and generates custom questions from their values.

### Cross-Arc Chains: Partially Working

Tags that cleanly cross arc boundaries:

| Tag | Set | Consumed |
|-----|-----|---------|
| `party_operative_truth` | Arc III V05 | Arc IV V04 Q2; gates Kain in V04/V05 |
| `betrayal_resolved` | Arc III V01–V04 | Arc IV V02 (Merel asks directly), Arc IV V04 Q3 |
| `chronal_shard_fate` | Arc III V03 | Arc IV V04 Q3 (incomplete intelligence question) |
| `wheel_exposure` | Arc III V02–V04 | Arc IV V04 Q3 |
| Reth/Procession thread | Arc II V01 (`ash_glass_reach`) → V05 | Arc III rhetoric → Arc IV V03 direct confrontation |
| `sarafan_attention` → `sarafan_bloc` | Arc I | Garric Sol's framing at the Heath, Arc IV V01 (narrative only) |

### Orphaned Tags

Tags set in vignettes but never explicitly named as an input in any later vignette or Fulcrum question:

| Tag | Last Set | Problem |
|-----|---------|---------|
| `iron_echo_status` | Arc II V05 | Never consumed in any Arc III or IV vignette |
| `fortress_claim` | Arc II V03 | Never consumed in any Arc III or IV vignette |
| `guild_pressure` | Arc I V05 | Grounded by Turas Vel (now in V02 cast) but not consumed downstream |
| `public_story` | Arc I V02–V03 | Never consumed in any Arc II vignette |
| `ash_glass_reach` | Arc II V04–V05 | Only implicit in Reth thread — no named tag check |
| `sarafan_bloc` | Arc II V02 | Only narrative (Sol at Heath) — no explicit tag check in Arc IV vignettes |

### The Structural Gap

Arc II V01's trigger states *"Arc I consequences — relic rumors, faction tags, known associations — are visible to everyone present"* but does not map specific tag values to specific scene modifications. Arc III V01's trigger references *"the Arc II contradiction"* but doesn't specify which Arc II outcome produced it or whether the contradiction's form differs by `hylden_engagement`, `iron_echo_status`, or `fortress_claim`.

Two tables can finish Arc II with radically different tag states and Arc III V01 treats both identically at the vignette layer.

### Recommended Fixes

#### FIX A — Carry-Forward Reading blocks at arc transitions

**Priority: SIGNIFICANT**
Status: Not started

Add a `## Prior-Arc Tag Reading` GM Note section to Arc II V01, Arc III V01, and Arc IV V01. Each block lists which prior-arc tags to check before running the scene and what scene modifications apply based on their values.

**Arc II V01 additions needed:**
- `reliquary_status: examined` → Turel and Drath envoys both show recognition; they know someone in the group has touched it
- `sarafan_attention: 2+` → A Sarafan-adjacent observer is already in the forecourt; Choice D (institutional cover) becomes significantly harder
- `public_story: panic` → The party's road reputation precedes them; Ledger-Master Vey approaches first, not last
- `serit_trust: earned` → Serit is with the party and visible; Drath recognizes her Accord status and adjusts his pitch accordingly

**Arc III V01 additions needed:**
- `hylden_engagement: negotiated` → The contradiction is specifically about the Glass Voice's stated terms vs. observed Hylden behavior; Iriane recognizes it immediately
- `hylden_engagement: none` → The contradiction is purely environmental/temporal; Iriane has no prior context for it
- `iron_echo_status: contested` or `sealed` → The Echo's resolution feeds into which memory-seam feels load-bearing; clarify which version of events the party acted on
- `fortress_claim` value → affects which party member's account is treated as authoritative by Iriane

**Arc IV V01 additions needed:**
- `iron_echo_status` → affects which faction Garric Sol invokes as precedent in his position statement
- `fortress_claim` final value → affects whether clan presence at the Heath is unified or factionally split

#### FIX B — Surface orphaned tags in Arc IV V04 Fulcrum Q3

**Priority: MODERATE**
Status: Not started

File: Arc IV `VTT_Vignettes/04_Fulcrum-Contact.md`, Question 3 pool

Add `iron_echo_status` and `fortress_claim` to the Q3 selection pool alongside the existing options. Suggested entries:

**If `iron_echo_status: contested` (never resolved in Arc II):** *"The Iron Echo was not settled. Its unresolved claim is producing faction pressure at this Heath that would not exist if you had decided it. What account do you give for the decision not to decide?"*

**If `fortress_claim: neutral_brokered` (party never committed):** *"You brokered the fortress without anchoring the outcome. Both claimants survived and both are represented in this room's wider coalition politics. Name one structural consequence — not a mistake, a consequence — of that choice."*

These questions make prior-arc stakes visible in the finale examination and ensure tables that resolved things differently feel reflected in the Fulcrum's judgment.
