# 01 — The Caravan Argument

The road to Avernus demands a choice before the first blood falls. Whether to press through the dark or shelter at the milestone shrines is not a tactical question — it is the first measure of what the party will trade for speed, and what it will not. Serit wants speed. Mera wants clarity. The cargo wants both, and neither.

## Control Links

- Fast flow: [../07_Vignette-Flow-Matrix.md#v01-caravan-argument](../07_Vignette-Flow-Matrix.md#v01-caravan-argument)
- Detailed fallout: [../08_Detailed-Vignette-Consequence-Matrix.md#v01-caravan-argument](../08_Detailed-Vignette-Consequence-Matrix.md#v01-caravan-argument)
- State tracker tags: [`serit_trust`](../Arc_I_VTT-State.md#serit_trust), [`sarafan_attention`](../Arc_I_VTT-State.md#sarafan_attention), [`reliquary_status`](../Arc_I_VTT-State.md#reliquary_status)


## Scene Info



## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| Serit Vale | Controlled urgency. She must reach Avernus before dawn and has said as much as she intends to about why. |
| Mera Ash | Practical arbiter. She will do whichever is decided quickly — she resents the delay more than either choice. |
| Brother Halden | Background figure only. He is helping with the wagon. He is listening to everything. |

---

## Opening Narration

> The road narrows under a green-tinged moon. Avernus is visible ahead — its white spires pale as old bone against the mist, closer than they should be and no nearer than they were an hour ago. One of the lead horses has stopped at the verge and will not be persuaded. Its refusal is the most honest thing on the road tonight. The wagon axle speaks in the register of things about to separate. Behind you, someone has lit a lantern they were told to keep dark. Serit Vale stands beside the stalled wheel with her arms folded and her satchel pressed hard against her ribs, already watching you with the expression of one who has decided the choice is yours whether you have been told so or not.

---

## NPC Opening Line

> **Serit Vale**, without moving her gaze from the road ahead: *"The milestone shrines are half a mile back. Safe, occupied by pilgrims who will remember us, visible to anyone descending from the cathedral road by first light. If we shelter there, we arrive in Avernus with witnesses and delay. I would prefer we arrived with neither."*

---

## Player Choices

### A — Press On to Avernus

> The party agrees with Serit. Get moving. Take the risk of the dark road over the certainty of being seen.

**NPC Response:**

> **Mera Ash**, already moving: *"Good. We mend it moving or we lose the night. Get underneath."* Serit exhales and loosens her grip on the satchel slightly — not relief, exactly, but the release of a held argument.

**Outcome:** The party arrives at the waystation before dawn, exhausted but ahead of any Sarafan patrol. The cult has less time to prepare, but the party has no rest before the ambush. Note this as the high-speed, low-social-cover path.

**Tags:** `serit_trust: guarded`

---

### B — Camp at the Milestone Shrines

> The party overrules Serit. The axle is a real problem. Shelter, fix it, move at dawn.

**NPC Response:**

> **Serit Vale**, after a pause that lasts exactly one breath too long: *"If you've decided, I won't argue in the road. But if anything about this caravan has been observed since we departed, the shrines are the first place they will look before dawn."* She walks back to help with the wheel without waiting for a reply.

**Outcome:** The party gains rest but the Sarafan patrol closes ground. Add +1 to `sarafan_attention`. The cult has time to position a watcher at the waystation before the party arrives.

**Tags:** `serit_trust: low`, `sarafan_attention: 1`

---

### C — Inspect the Reliquary Before Deciding

> Someone wants to understand what they're transporting before they decide how fast to move it.

**NPC Response:**

> **Serit Vale** steps between the player character and the cargo wagon with more speed than someone composed should have: *"That is sealed under Accord authority and is not to be opened on a road in the dark. Whatever you felt — if you felt something — is precisely the reason this must be behind better walls before morning."* She is not lying. She is also not saying everything.

**Outcome:** The inspection is denied, but the attempt tells the party something: she anticipated this, she moved immediately, and she did not say it was impossible — only inadvisable. Serit's hidden truth (she knows the relic resonates with blood) has been knocked closer to the surface. If a PC with blood magic or spectral sensitivity made the move, they register one pulse before Serit intervenes.

**Tags:** `serit_trust: low`, `reliquary_status: examined`

---

### D — Question Serit Directly About Why Tonight Matters

> Press her: what specifically happens if you don't arrive before dawn?

**NPC Response:**

> **Serit Vale** meets the question without flinching: *"There is a receiving contact at Avernus who will assume failure if we do not appear by the morning bell. Their records become ash. The Accord's documentation of the site's origin becomes unrecoverable."* She pauses. *"That is the true answer. There is also a less comfortable answer, which is that I am carrying something that has been answering to certain people since we crossed the second waymarker, and I would prefer it behind better walls before it answers to the wrong one."*

**Outcome:** This is the most honest Serit will be in Arc I. She has partially confirmed the relic is active. `serit_trust` rises but she is now committed — she can't walk this back. If no one follows up, the moment closes and she won't revisit it tonight.

**Tags:** `serit_trust: earned`

---

## If No Clear Choice Is Made

> If the party stalls, argues internally for more than a few minutes, or cannot agree on a direction: Brother Halden quietly finishes the axle repair and says the shrines are the sensible choice, which settles the question without anyone deciding. Default to Choice B's outcome.

**Default Tag:** `sarafan_attention: 1`

---

## Next-Scene Effects

| Tag | Value | Effect on next scene or encounter |
|-----|-------|-----------------------------------|
| `serit_trust` | `earned` | Serit will warn the party before the cult ambush if they reach the waystation; she places herself between the cargo and a shadow she notices |
| `serit_trust` | `guarded` | Serit withholds the warning; the ambush opens without her preparation action |
| `serit_trust` | `low` | Serit locks her room at the waystation; the party must work around her to get information |
| `sarafan_attention` | `1` | The Sarafan patrol is at the milestone shrine by dawn; a witness gives the Order a description of the caravan |
| `reliquary_status` | `examined` | The attempt has been noted; a cult watcher who was tracking the caravan now knows someone in the group is sensitive to the fragment |

---

## GM Notes

- This scene should run fast. It's a setup vignette, not a lore dump. The goal is one hard impression per NPC and a clear party position entering the waystation.
- Brother Halden is present but quiet. Do not spotlight him yet. Let him fix the wheel, stay warm, and seem reliably useful.
- Serit's offer of the "less comfortable answer" in Choice D should feel like a gift she regrets immediately. Keep her composed after she says it — she doesn't panic, she recalibrates.
- If someone rolls Perception or Insight during the scene: the satchel is warm. It has been warm since the second waymarker. That is all they can confirm right now.
