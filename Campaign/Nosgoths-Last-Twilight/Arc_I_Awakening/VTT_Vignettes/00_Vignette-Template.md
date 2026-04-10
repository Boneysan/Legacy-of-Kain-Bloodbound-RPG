# [Vignette Title]

Use this template for all VTT branching vignettes. Short scenes (2–5 min) that fire at defined triggers, resolve through player choice, and write their outcome into the arc's story-state tracker. Do not extend a vignette beyond its natural length — let it close, tag the result, and move into the encounter or dialogue it feeds.

## Control Links

- Fast flow: [../07_Vignette-Flow-Matrix.md#v0x-scene-key](../07_Vignette-Flow-Matrix.md#v0x-scene-key)
- Detailed fallout: [../08_Detailed-Vignette-Consequence-Matrix.md#v0x-scene-key](../08_Detailed-Vignette-Consequence-Matrix.md#v0x-scene-key)
- State tracker tags: [`tag_name`](../Arc_I_VTT-State.md#tag_name), [`second_tag_name`](../Arc_I_VTT-State.md#second_tag_name)

---

## Scene Info

- **Arc / Session:** Arc # — Session #
- **Trigger:** [What causes this scene to fire: an NPC action, a location reached, a relic event, a faction move]
- **Scene Type:** `setup` | `revelation` | `confrontation` | `consequence`
- **Est. Duration:** 3–5 min
- **Tags This Scene Can Change:** [list applicable story-state tags]

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| [Name] | [One-line context: what they want and what they won't say] |

---

## Opening Narration

> [GM read-aloud, 2–4 sentences. Atmospheric, present-tense. Establish image, tension, and who is speaking first. No mechanical information here.]

---

## NPC Opening Line

> **[NPC Name]**, [body language, posture, or action context]: *"[Dialogue line — character-voiced, not neutral. Should contain a partial truth, a pressure, or a question that demands a response.]*"

---

## Player Choices

### A — [Choice Label]

> [One sentence describing what this looks like: what the player character does or says.]

**NPC Response:**

> *"[Voiced response — reactive, in-character. Should feel like a consequence of the choice, not just an acknowledgment.]*"

**Mechanical or Narrative Outcome:** [What physically or socially changes. Use plain sentences, not bullet lists.]

**Tags:** `[tag_name]: [new value]`

---

### B — [Choice Label]

> [Description]

**NPC Response:**

> *"[Response]*"

**Outcome:** [What changes]

**Tags:** `[tag_name]: [new value]`

---

### C — [Choice Label]

> [Description]

**NPC Response:**

> *"[Response]*"

**Outcome:** [What changes]

**Tags:** `[tag_name]: [new value]`

---

### D — [Choice Label] *(optional fourth branch)*

> [Description]

**NPC Response:**

> *"[Response]*"

**Outcome:** [What changes]

**Tags:** `[tag_name]: [new value]`

---

## If No Clear Choice Is Made

> [GM instruction for handling player inaction, derailment, or consensus failure. Usually: assign the worst-case default outcome and name it, so the GM can narrate the cost rather than stall.]

**Default Tag:** `[tag_name]: [default value]`

---

## Next-Scene Effects

Document how each possible tag outcome changes the encounter, NPC behavior, or scene setup that follows this vignette.

| Tag | Value | Effect on next scene or encounter |
|-----|-------|-----------------------------------|
| `[tag]` | `[value]` | [Concrete change to what follows] |
| `[tag]` | `[alt value]` | [Concrete change to what follows] |

---

## GM Notes

- [Any advisory for running the scene smoothly: pacing cues, who to keep off-camera, what not to force]
- [If an NPC here has a hidden truth from the NPC Appendix, note which truth is at risk of exposure in this scene]
- [Any connection to existing Choice Guide entries this vignette feeds or preempts]
