# Nosgoth's Last Twilight — VTT Integration Guide

This document provides the technical structure for the campaign's dialogue and skill systems, designed for integration into the custom `Virtual_Tabletop`.

---

## 1. The Skill System
The campaign uses 15 primary skills mapped to a 3-tier Difficulty Rating (DR) system.

### The 15 Primary Skills
1. **Observation** (Physical notice)
2. **Insight** (Social/Emotional reading)
3. **Persuasion** (Diplomacy/Negotiation)
4. **Intimidation** (Coercion/Fear)
5. **Stealth** (Hidden movement)
6. **Infiltration** (Security/Trap bypassing)
7. **Lore** (History/Genealogy)
8. **Forbidden Knowledge** (Metaphysics/Elder God)
9. **Blood Sense** (Ancestry/Relic resonance)
10. **Concentration** (Mental resistance)
11. **Glyphcasting** (Hylden machinery)
12. **Ritualism** (Warden rites/Sealing)
13. **Craft** (Engineering/Repair)
14. **Wilderness** (Navigation/Environmental)
15. **Tactics** (Combat positioning)

### DR Standards
- **DR 2 (Standard):** Surface-level clues or common knowledge.
- **DR 3 (Significant):** Hidden motives, complex lore, or precise timing.
- **DR 4 (Legendary):** Breaking reality, defying the Wheel, or rewriting breaches.

### Faction Standing Modifiers
Your relationship with a faction (see GM Guide §1.6) modifies social and specific lore checks involving them:
- **Exalted (+3):** **Advantage** on all related checks.
- **Allied (+2):** **+1 Die** to the dice pool.
- **Friendly (+1):** Minor narrative concessions (no mechanical bonus).
- **Unfriendly (-1):** **-1 Die** from the dice pool.
- **Hostile (-2):** **Disadvantage** on all related checks.
- **War (-3):** Standard checks are impossible without extreme leverage.

---

## 2. Skill Usage Mapping

### A. In-Vignette (Dialogue & Exploration)
| Skill | Typical VTT Use |
| :--- | :--- |
| **Observation** | Notice physical cues (e.g., "The satchel is warm"). |
| **Insight** | Catch rehearsed stories or hidden motives. |
| **Lore** | Identify heraldry, cult-marks, or historical precedent. |
| **Blood Sense** | Sense relic proximity or "Bloodline Recognition." |
| **Forbidden Knowledge** | Decode Moebian logic or recognize Elder God influence. |

### B. In-Combat (Tactical & Reactive)
| Skill | Typical VTT Use |
| :--- | :--- |
| **Tactics** | Identify "Break-Packages" or terrain objectives. |
| **Concentration** | Maintain rites or glyph-engines while taking damage. |
| **Intimidation** | Force low-health enemies into the "Fleeing" state. |
| **Insight** | Predict a Boss's "Ultimate Move" (Advantage on Saves). |
| **Glyphcasting** | Overload pylons to create "Static Zones" or shields. |

### C. After-Combat (Discovery & Recovery)
| Skill | Typical VTT Use |
| :--- | :--- |
| **Blood Sense** | Perform "Blood-Memory" extraction on fallen elites. |
| **Infiltration** | Open locked courier cases or reliquaries. |
| **Craft** | Salvage parts (Soul-Ember/Glyph-Parts) from machines. |
| **Ritualism** | Cleanse a site to prevent "Balance Reckoning" advancement. |
| **Wilderness** | Track survivors back to their hidden base. |

---

## 3. Dialogue & Vignette Structure
Every conversation (Vignette) follows a strict A/B/C/D branching logic that updates the VTT's state.

### Data Schema
- **Trigger:** The condition or location that fires the scene.
- **Choices (A-D):** Clickable options for players.
- **NPC Response:** Reactive dialogue for each choice.
- **State Tags:** Global variables updated by the choice.
- **Handoff:** The next Encounter or Vignette to load.

### Example Mapping (V01: Caravan Argument)
| Choice | Input | VTT Tag Update | Next Scene / Handoff |
| :--- | :--- | :--- | :--- |
| **A** | Press On | `serit_trust: guarded` | Load `01_Cathedral-Road-Ambush.md` |
| **B** | Camp | `serit_trust: low`; `sarafan_attention +1` | Load Ambush (with Watcher variant) |
| **C** | Inspect | `reliquary_status: examined` | Trigger "Vessel Recognition" Logic |
| **D** | Question | `serit_trust: earned` | Add "Warning Beat" to next combat |

---

## 4. Global State Tracking
The campaign maintains continuity through named "State Tags." Your VTT should track these as global variables.

### Arc I Variables
- `serit_trust`: (`low` | `guarded` | `earned`) - controls early ally behavior.
- `sarafan_attention`: (integer) - controls pursuit intensity and enforcement pressure.
- `reliquary_status`: (`sealed` | `examined` | `compromised` | `stolen`) - controls first-fragment handling pressure.
- `public_story`: (`panic` | `secrecy` | `controlled_lie` | `open_truth`) - controls rumor and faction framing.
- `balance_reckoning`: (integer) - tracks withdrawal-of-grace pressure.

### Arc II Variables
- `fortress_claim`: (`recognized-claimant` | `neutral-brokered` | `contested`) - political legitimacy outcome from fortress struggle.
- `iron_echo_status`: (`secured` | `contested` | `lost`) - command artifact control and pressure source.
- `hylden_engagement`: (`suppressed` | `managed-contact` | `active-breach`) - Hylden conflict posture entering Arc III.
- `sarafan_bloc`: (`legalist` | `split` | `purge-forward`) - Sarafan operating line and escalation tendency.
- `ash_glass_reach`: (`contained` | `widening` | `entrenched`) - Fracture/Procession influence footprint.

### Arc III Variables
- `chronoplast_access`: (`denied` | `partial` | `full`) - level of trustworthy chronoplastic intelligence.
- `chronal_shard_fate`: (`recovered` | `destroyed` | `lost` | `divided`) - shard custody and narrative leverage state.
- `wheel_exposure`: (`concealed` | `named` | `broken`) - Wheel public and operational status.
- `party_operative_truth`: (`balance-through-sacrifice` | `hylden-reintegration` | `undecided` | `unresolved`) - Arc IV opening posture and Kain-contract timing input.
- `party_operative_truth_note` (optional string): provenance annotation such as `chosen-under-testimony`.
- `betrayal_resolved`: (`unresolved` | `absorbed` | `severed` | `weaponized`) - betrayal continuity and coalition trust architecture.

### Arc IV Variables
- `coalition_shape`: process values during V01-V03 and assessment values after V04 (see Arc IV tracker table).
- `black_fulcrum_status`: (`active` | `active-collective` | `partial` | `witness-anchored` | `dormant` | `cleared` | `conditional` | `unfounded`) - examination/recognition status and final-session backing.
- `heart_purpose`: (`understood` interim in V04, then final `spent-for-balance` | `gate-opened-negotiated` | `foreclosed` | `withdrawn` in V05).
- `heart_purpose_note` (optional string): final declaration phrasing or moral-frame annotation.
- `hylden_gate_resolution`: (`sealed` | `displaced` | `open` | `negotiated` | `deferred` | `open-on-terms` | `reth-adjacent`).
- `wheel_final_state`: (`active` | `broken` | `absorbed` | `transcended` | `reduced-surviving` | `opposing-surviving` | `default-surviving` | `contested`).

## 5. Schema Authority Rules

- Trackers and detailed vignette consequence matrices are procedural authority.
- Story overviews and chronicles are narrative summaries and may lag behind active branch state.
- Use canonical enum values exactly as written; place context in paired note fields rather than inventing new enum variants.
- Intermediate values (for example `heart_purpose: understood`) must be overwritten by final declaration values when the vignette specifies finalization.

---

## 6. Detailed Scene Skill Outcomes (VTT Reveal Table)
Use these blocks to populate VTT "Whisper" macros or Journal reveals based on player rolls.

### Arc I: Awakening
| Scene | Skill & DR | Success Outcome (Whisper to Player) |
| :--- | :--- | :--- |
| **Caravan Argument** | **Insight DR 2** | Serit isn't just hurried; she’s terrified of being caught by a specific threat she’s already sensed. |
| **Caravan Argument** | **Blood Sense DR 2** | The satchel is pulsing. It feels like a heartbeat, heavy and rhythmic, answering your own. |
| **False Refuge** | **Observation DR 2** | You notice the "Healer" has callouses from a sword hilt, not just medicine. Something is wrong. |
| **False Refuge** | **Infiltration DR 2** | You find a hidden side entrance. It’s been recently oiled; someone expects to use it in a hurry. |
| **Blood-Well Descent** | **Lore DR 3** | These ruins aren't just old; they are built over a stolen legacy. This is a place of ancestral theft. |
| **First Blood-Memory** | **Concentration DR 2** | You hold onto your sense of self as the vision hits. You see a blue-mantled figure watching you. |

### Arc II: Ascension
| Scene | Skill & DR | Success Outcome (Whisper to Player) |
| :--- | :--- | :--- |
| **Fortress Arrival** | **Tactics DR 2** | The murder-holes are active. The guards aren't just watching; they are waiting for a signal. |
| **Claimant's Test** | **Insight DR 3** | Turel’s bravado is a mask. He’s already losing control of his captains; he needs you more than he admits. |
| **Iron Echo Chamber** | **Blood Sense DR 3** | The chamber recognizes you. The statues’ eyes follow your movement. You have local authority here. |
| **Northern Breach** | **Glyphcasting DR 3** | The pylon isn't failing; it’s being redirected. Someone is *pulling* the breach open from the other side. |

### Arc III: Revelation
| Scene | Skill & DR | Success Outcome (Whisper to Player) |
| :--- | :--- | :--- |
| **Tracks in Frost** | **Observation DR 3** | The tracks appear and disappear instantly. You are walking through a time-scar, not just a blizzard. |
| **Wheel's Offer** | **Concentration DR 4** | The "peace" in Bale’s voice is a mental weight. You realize his words are a form of spiritual sedation. |
| **Into Chronoplast** | **Forbidden Knowledge DR 3** | This machine doesn't show "the" future. It shows the future Moebius *wanted* you to believe in. |
| **Betrayal Named** | **Insight DR 3** | Your ally isn't just lying; they are under a "Suggestion" effect. They believe their own false story. |

### Arc IV: Convergence
| Scene | Skill & DR | Success Outcome (Whisper to Player) |
| :--- | :--- | :--- |
| **Heath Coalition** | **Tactics DR 3** | The Sarafan and Clans are positioned to fight each other as much as the enemy. The center is unstable. |
| **Hall of Equilibrium** | **Lore DR 4** | The Hall isn't judging your "goodness." It is judging the *consistency* of your choices across the campaign. |
| **Fulcrum Contact** | **Forbidden Knowledge DR 4** | The Heart is ready to break. Using it now will permanently wound the Wheel, but the price is your soul. |
| **Final Pursuit** | **Observation DR 3** | You see him. The white-haired man (Kain) is standing on the Pillar ruins, waiting for the coin to land. |
