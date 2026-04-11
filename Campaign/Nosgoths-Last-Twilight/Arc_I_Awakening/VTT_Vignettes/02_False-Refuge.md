# 02 — The False Refuge

Hospitality in Nosgoth is never free. When Brother Halden opens the waystation door and the warmth inside is exactly what an exhausted party wants, the cost is already set. The question is not whether to accept — the road behind is closed by now — but what the party decides to do with suspicion when sleep is the other option.

## Control Links

- Fast flow: [../07_Vignette-Flow-Matrix.md#v02-false-refuge](../07_Vignette-Flow-Matrix.md#v02-false-refuge)
- Detailed fallout: [../08_Detailed-Vignette-Consequence-Matrix.md#v02-false-refuge](../08_Detailed-Vignette-Consequence-Matrix.md#v02-false-refuge)
- State tracker tags: [`reliquary_status`](../Arc_I_VTT-State.md#reliquary_status), [`public_story`](../Arc_I_VTT-State.md#public_story), [`sarafan_attention`](../Arc_I_VTT-State.md#sarafan_attention), [`serit_trust`](../Arc_I_VTT-State.md#serit_trust)

---

## Scene Info

- **Arc / Session:** Arc I — Session 1
- **Trigger:** The party reaches the waystation, hospice outbuilding, or chapel ruin near Avernus. Brother Halden appears promptly and offers shelter, food, and somewhere to lock the cargo.
- **Scene Type:** `confrontation`
- **Est. Duration:** 4–6 min
- **Tags This Scene Can Change:** `serit_trust`, `sarafan_attention`, `public_story`

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| Brother Halden | Warm, practiced, and one beat too fast. He has already made room for the party. He already knows roughly how many they are. |
| Serit Vale | Exhausted and trying to evaluate the space without looking like she's evaluating the space. |
| Mera Ash | On edge. She doesn't like enclosed spaces with strangers and she is not pretending otherwise. |
| A guild broker (background) | An Outlands Guild factor sheltering here on commercial business, heading toward Avernus. Does not advertise their affiliation. Mentions it if the party makes useful conversation. Their presence plants the `guild_pressure` thread that pays off in V05. |

---

## Opening Narration

> The waystation is lit. That is the first strange thing. It is well past midnight and every window holds a candle, and the door opens before anyone knocks. Brother Halden stands in the threshold in a practical robe still dusted with road grit, as if he had only just arrived himself, and his face is the face of someone who has been doing this work long enough to look like the answer to every prayer. Behind him, the smell of warm bread and something medicinal, and beyond that, the sound of other people already sheltered inside.

---

## NPC Opening Line

> **Brother Halden**, stepping back from the door and extending his arm: *"Word came that a caravan was overdue on the south road. Come in — there are people here from the eastern road in need of attention, if any among you has the skill. There is room for you."*

> *Who told him?*

---

## Player Choices

### A — Accept Sanctuary Fully

> The party enters, takes the offered beds, and begins to settle. No open suspicion — or not yet.

**NPC Response:**

> **Mera Ash**, quietly to whoever is closest: *"He knew our number before we were through the door. Did someone speak of our approach?"* She doesn't wait for an answer. She takes the corner with the window. She does not sleep.

**Outcome:** The party is inside and relatively safe for the night. Brother Halden assigns them rooms and offers to store the reliquary "somewhere dry." If a PC allows it, the cargo moves out of direct sight. The cult cell inside the refuge now has position.

**Tags:** `reliquary_status: sealed`, `public_story: secrecy`

---

### B — Accept but Insist on Posting Guards Outside

> The party enters but establishes a watch rotation. Someone is always outside. The cargo stays with them.

**NPC Response:**

> **Brother Halden** nods without any visible surprise: *"A reasonable precaution. There is a dry post beside the east stable wall. I'll bring whoever takes first watch something warm."* He smiles. He is noting which of you thought of it.

**Outcome:** The cargo stays visible and the ambush trigger is harder to execute quietly. The cult cell must adjust its approach — expect more social pressure inside rather than a direct move on the cargo. Trade-off: one party member will be isolated outside when the first real incident begins.

**Tags:** `public_story: secrecy`, `sarafan_attention: 0` *(watch presence deters a Sarafan informant also sheltering here)*

---

### C — Openly Question How He Knew the Caravan Was Coming

> Challenge him in front of everyone. Who sent word? What word? When?

**NPC Response:**

> **Brother Halden** meets the question with practiced calm: *"A rider passed through at dusk. He said a caravan from the south road had a wheel problem and would likely want shelter. I assumed that was you."* He pauses. *"I apologize if the welcome felt presumptuous. I can go."* He does not move toward the door.

**Outcome:** There was no rider. Everyone in the room who thinks about it knows there was no rider. Brother Halden has offered an explanation and staked his warmth on whether the party will push harder or take the exit it was offered. If the party presses further, he produces an implausibly precise physical description of the rider and ends the line of questioning. The public challenge means every other sheltered traveler in the room heard it.

**Tags:** `public_story: panic`, `serit_trust: guarded` *(Serit is alarmed that the party made noise)*

---

### D — Split the Party

> Some enter. Some stay with the cargo. Someone scouts around the outside of the building first.

**NPC Response:**

> **Serit Vale**, low: *"Splitting in an unknown structure is how the Accord lost three couriers last winter. I would prefer we make one decision together."* She does not tell anyone what to do. She is noting whether anyone listens.

**Outcome:** The group that stays outside with the cargo discovers a side entrance that was not offered to them, fresh footprints in mud that match neither pilgrim nor stable traffic, and a narrowly shuttered window that shows candlelight lower and steadier than the others. The group inside meanwhile is isolated from this information until they reunite.

**Tags:** `reliquary_status: examined` *(the outside team gets close enough to notice the crate's warmth)*, `sarafan_attention: 1`

---

## If No Clear Choice Is Made

> If the party is frozen with suspicion and will not commit: Mera Ash makes the decision. She goes in, finds the corner, and says that standing in the road arguing is the only plan that benefits the people watching from the tree line. Default to Choice A's outcome, with Mera visibly judging anyone who hesitates. 

**Default Tags:** `reliquary_status: sealed`, `public_story: secrecy`

---

## Next-Scene Effects

| Tag | Value | Effect on next scene or encounter |
|-----|-------|-----------------------------------|
| `public_story` | `panic` | The other sheltered travellers are awake and frightened before the cult ambush; some will flee, creating chaos that the cult exploits |
| `public_story` | `secrecy` | The ambush happens without civilian escalation; collateral damage is lower and the party can control what they leave behind |
| `reliquary_status` | `examined` | The cult knows someone in the party is tracking the cargo by feel; they redirect their approach away from the carrier and toward the weakest observer |
| `sarafan_attention` | `1` | An informant sheltered at the waystation is now carrying the party's description toward Avernus; Sarafan Clock advances before Session 2 |
| `serit_trust` | `guarded` | Serit meets the Session 2 investigation with less cooperation; she is recalibrating how much the party can handle without creating worse problems |

---

## GM Notes

- The vignette should close the moment someone decides. Do not let it become an interrogation of Brother Halden — he is designed to deflect soft pressure. Save the real confrontation with him for Session 2 if he survives.
- The warmth of the building and the quality of the welcome are both genuine *and* calculated. He is not a monster. That is the point.
- Mera Ash is the scene's implicit timer. If she starts moving toward the door unilaterally, the party has taken too long.
- If someone rolls Awareness during Halden's explanation: the "rider" detail is sourced too cleanly for an ad hoc cover. Someone rehearsed it. It is not a lie that emerged under pressure — it was retrieved.
- The guild broker is a background presence; do not spotlight them unless the party makes friendly conversation with the other sheltered travelers. If they do, the broker mentions being "Accord-adjacent, commerce side" and having business at Avernus. Their name is Turas Vel. They survive the night regardless of party choice — and they reach the party again in V05 with the `guild_pressure` thread activated. If the party was hostile or the waystation scenario ended badly, Vel's approach in V05 is cooler but still present.
- **The ambush follows this vignette, not a prior scene.** The cult cell Halden is managing activates during or immediately after the party leaves the waystation. Run the ambush as a combat encounter between V02 and V03. The GM should not wait for the party to seek out a fight; the cult moves when the party is on the road and exposed. V03 (What Serit Knows) requires the party to have survived this encounter before it can fire.
