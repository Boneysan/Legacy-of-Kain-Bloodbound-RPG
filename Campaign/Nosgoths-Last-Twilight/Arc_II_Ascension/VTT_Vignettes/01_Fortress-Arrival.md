# 01 — Whose Leave

The fortress does not grant entry. It interrogates arrivals. Before the party can plan, find shelter, or locate the Iron Echo, they must answer the first political question Dumah's Fortress has been asking since its last lord fell: under whose authority do you stand here?

---

## Scene Info

- **Arc / Session:** Arc II — Session 1
- **Trigger:** The party approaches the fortress gate and encounters a gate challenge, envoy delegation, or rival claimant parley. Arc I consequences — relic rumors, faction tags, known associations — are visible to everyone present.
- **Scene Type:** `setup`
- **Est. Duration:** 4–6 min
- **Tags This Scene Can Change:** `fortress_claim`, `ash_glass_reach`

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| Marshal Kaev Turel | Present or represented. He wants the party's public alignment. He mistakes leverage for respect. |
| Steward Vaul Drath | Present or represented. He wants acknowledgment that history matters here. He mistakes dignity for strength. |
| Ledger-Master Corin Vey | Watching from slightly off the main floor. He has already run numbers on both arrivals. |

---

## Opening Narration

> Dumah's Fortress rises from the eastern wastes as a gray mountain of dead authority. Its gate banners have been torn away, leaving pale stone where colors used to justify the walls, but the walls still work. You have been visible from the ramparts for the last half-mile, and the gate is not open. Two delegations wait in the forecourt — one wearing Turelim colors, one bearing a faded steward's seal — and they have arranged themselves so that greeting one means ignoring the other. They are both looking at you.

---

## NPC Opening Line

> **Marshal Kaev Turel's envoy**, stepping forward first: *"The Marshal extends the hospitality of the fortress's eastern quarters — provisions, shelter, and a single authority to address rather than two to navigate. His condition is the eastern gate."*

> The western gate is still closed. Steward Drath's people have not moved.

---

## Player Choices

### A — Enter Through the Eastern Gate (Align With Turel)

> Accept the offer. Walk through the eastern gate. You are not endorsing anything — you are choosing where to sleep.

**NPC Response:**

> **Steward Vaul Drath**, quietly enough to be heard: *"They always think the gate doesn't count."* He withdraws. He does not forget.

**Outcome:** The party has provisional shelter and practical access under Turel's hospitality. Kaev Turel now interprets their presence as partial endorsement. The Dumahim faction reads this as a choice and begins calculating what it would cost to reverse it. Ledger-Master Vey immediately opens a separate channel with the party — he wants to be on whichever side the outsiders end up feeding.

**Tags:** `fortress_claim: party_backed` *(Turel faction)*

---

### B — Request Use of the Western Gate (Align With Drath)

> Acknowledge the Steward's people. Walk through the western gate. Continuity has its logic.

**NPC Response:**

> **Marshal Kaev Turel's envoy**, with military precision: *"Noted."* He withdraws without visible emotion, which is more alarming than anger would be.

**Outcome:** The party has shelter in Drath's portion of the fortress. Vaul Drath treats this as profound validation, which means he will also hold the party responsible when his position weakens. Turel begins watching for the moment to publicly demonstrate that Drath's alliance does not produce outcomes.

**Tags:** `fortress_claim: party_backed` *(Drath faction)*

---

### C — Refuse Both Gates; Demand a Joint Parley First

> Neither. You are here on independent standing. You want both claimants at the same table before any of you walk inside.

**NPC Response:**

> Both delegation members go still at precisely the same moment. Then the Turel envoy: *"That has not been attempted since the third day of the dispute. The last party who tried it negotiated from the courtyard for two weeks and left without entering."* He says this as a warning, not a precedent.

**Outcome:** The party is taken seriously as independent actors. No faction debt accrues. But they sleep in the forecourt until the joint parley can be arranged, which delays access to the Iron Echo and gives every faction another day to build pressure. Ledger-Master Vey is the one who quietly arranges the table — and he now knows the party values process over comfort, which is useful information he will sell.

**Tags:** `fortress_claim: neutral_brokered`

---

### D — Enter Through the Gate Marked by Arc I Standing

> If the party arrived with Accord credentials, Guild contracts, or Sarafan neutrality papers, use whichever entrance is most defensible under that framing. Let prior standing carry them through without fresh alignment.

**NPC Response:**

> **Steward Vaul Drath**, after a pause: *"Institutional neutrality. Reasonable. You'll have the archive rooms near the east vault. They haven't been contested yet because no one understands why they matter."* He steps aside. The Turel envoy does not visibly acknowledge the outcome, which is itself an answer.

**Outcome:** The party enters under institutional rather than factional cover. Both claimants leave them alone for the first session while they send envoys with invitations rather than demands. This costs more time but gives the party the best intelligence position: they see both factions' opening offers before committing.

**Tags:** `fortress_claim: unsettled`

---

## If No Clear Choice Is Made

> If the party halts too long, Ledger-Master Vey appears from behind the western colonnade and says, practically: *"The longer you stand here, the more it looks like Drath is blocking you. I would not choose that read intentionally."* He is correct. Default to the eastern gate and Turel's hospitality.

**Default Tag:** `fortress_claim: party_backed` *(Turel faction)*

---

## Next-Scene Effects

| Tag | Value | Effect on next scene or encounter |
|-----|-------|-----------------------------------|
| `fortress_claim` | `party_backed` (Turel) | Session 2 starts with Turel's leverage request: a military task the party cannot cleanly refuse without breaking hospitality |
| `fortress_claim` | `party_backed` (Drath) | Session 2 starts with Drath invoking the party as witnesses to an inheritance ceremony — before they know what they're witnessing |
| `fortress_claim` | `neutral_brokered` | Session 2 parley is arranged; the party run it; both claimants use it to try to expose the other rather than negotiate |
| `fortress_claim` | `unsettled` | Both factions' Session 2 approach is cautious; the party gets information first, choices second |
| `ash_glass_reach` | `fringe` | A Procession-marked defector watching the gate scene is noting who the outsiders chose; this will feed Reth's approach in Session 4 |

---

## GM Notes

- This scene should run fast and feel inevitable — not as a trap, but as the honest shape of Dumah's Fortress's politics. Both delegations are competent people doing a competent job for their side.
- Kaev Turel and Vaul Drath are not villains. They are two defensible answers to the same terrible question, which is worse.
- Ledger-Master Vey is the scene's loose variable. He will assist whoever is winning in a way that makes them feel he was always on their side.
- Sister Nerys Vale, if the party is watching for her: she enters through neither gate. She is already inside.
