# 02 — The Loyalty Test

Both claimants need something from the party, and the fortress is watching. Before access to the Iron Echo becomes possible, the party must demonstrate at minimum that they are useful and at most that their presence here is worth the political cost it imposes on whoever shelters them. The task assigned is the test. What the party does with the assignment is the answer.

---

## Scene Info

- **Arc / Session:** Arc II — Session 2
- **Trigger:** The party's chosen claimant (or their second, if the party entered neutrally) makes a specific request: expose a spy, represent them in a formal challenge, retrieve a document from a sealed barracks, or witness an oath ceremony they want witnessed by someone not already owned by either house.
- **Scene Type:** `confrontation`
- **Est. Duration:** 4–6 min
- **Tags This Scene Can Change:** `fortress_claim`, `iron_echo_status`, `sarafan_bloc`

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| The claimant who shelters the party (Turel or Drath) | Making the request. They frame it as reasonable. The strings are visible only after the task is accepted. |
| Archivist Sen Vael | Present as a witness or incidental complication. They want access to the sealed records attached to the task site. |
| Scout-Confessor Maelin Rook | Watching from the margins. She wants the party to make a mistake that looks like it belongs to their claimant. |

---

## Opening Narration

> The request is delivered privately, which is the first warning. Whatever it is — expose an informant, witness an oath, retrieve a command record from the sealed barracks — it is being asked quietly because asking it publicly would cost the claimant something they cannot afford to spend. They are treating your discretion as the price of your shelter. They have not asked whether you agree.

---

## NPC Opening Line

> **The sheltering claimant**, sitting across a bare table with no other witnesses: *"I need something done that I cannot assign to my own people. Not because the task is wrong. Because whoever does it must have no prior stake here — the thing may need to be witnessed afterward, and the witness must be clean. I want to be clear that I am asking, not ordering. I want to be equally clear that the distinction may matter less than it sounds."*

---

## Player Choices

### A — Accept and Complete the Task As Requested

> Do what is asked. You owe them that much for shelter and access.

**NPC Response (claimant):**

> *"Then we understand each other."* They do not thank the party. Thanks would imply the party had a choice.

**Outcome:** The task is completed. The party now has demonstrated loyalty on record, which is simultaneously their best protection and their most visible liability. Senator Rook has watched what they did and is composing her summary for the Sarafan. The sealed records include the first legible reference to the Iron Echo's chamber location.

**Tags:** `fortress_claim: party_backed`, `iron_echo_status: contested` *(the location is now known to three parties)*

---

### B — Accept, but Report Back to Both Claimants

> Do the task, keep the findings, and share relevant results with both sides. You are not an instrument. You are a resource.

**NPC Response (claimant, after the fact):**

> *"You told Drath."* Or: *"You told the Marshal."* A long pause. *"Did you think I wouldn't know?"* They are not immediately hostile. They are recalibrating how much autonomy they will extend to someone who just demonstrated they have some.

**Outcome:** Both claimants are now cautious about the party but neither has discarded them. The party sits at a genuine independent position — valued by both, fully trusted by neither. Access to the Iron Echo chamber becomes a mutual offer rather than a single-patron prize: both want the party to go first.

**Tags:** `fortress_claim: neutral_brokered`

---

### C — Refuse the Task

> You are here on your own terms. No one's errand-runner. Find another way to offer value.

**NPC Response (claimant):**

> *"Then I'll need to think carefully about the cost of your presence here."* They do not throw the party out. They withdraw access, slowly, starting with information rather than shelter — the kind of squeeze that is hard to name and impossible to litigate.

**Outcome:** The party has standing but not allies. The claimant no longer actively helps them but has also not publicly broken. Archivist Sen Vael approaches the party independently within the day: he has leverage of his own and doesn't need either claimant's permission to share it. The Iron Echo's location arrives through a different channel, but later and with more conditions.

**Tags:** `fortress_claim: unsettled`, `iron_echo_status: contested`

---

### D — Do the Task, Then Use What You Found to Expose the Request Itself

> The task reveals that the claimant is holding something more damaging than they disclosed. Bring it to light rather than deliver it quietly.

**NPC Response (claimant, publicly):**

> They respond the way people who have been in power long enough to know when they've lost a round respond: controlled acknowledgment, minimal confirmation, immediate subject change. In private, afterward: *"You will understand that I cannot extend shelter here if you act so again."*

**Outcome:** The party blows the cover on something the claimant needed quiet. Public standing goes up with the neutral faction; the insider-faction relationship cracks but doesn't break. Maelin Rook files a much more favorable Sarafan report: the outsiders are independent and potentially exploitable. One of the two claimants begins treating the party as a threat to be redirected rather than an asset to be managed.

**Tags:** `fortress_claim: contested`, `sarafan_bloc: one_contact` *(Rook opens an unofficial line)*

---

## If No Clear Choice Is Made

> If the party cannot agree on what to do: the task deadline passes, the claimant interprets the silence as refusal, and the default shifts to Choice C's outcome. The window for easy Iron Echo access narrows by one session.

**Default Tag:** `fortress_claim: unsettled`

---

## Next-Scene Effects

| Tag | Value | Effect on Session 3 (Iron Echo access) |
|-----|--------|----------------------------------------|
| `fortress_claim` | `party_backed` | The claimant provides direct escort and access to the Echo chamber; the rival claimant contests entry |
| `fortress_claim` | `neutral_brokered` | Both claimants send the party together, which means neither side has full control of what the fragment reveals |
| `fortress_claim` | `contested` | Neither claimant provides clean access; the party must force entry or negotiate around both |
| `iron_echo_status` | `contested` | Sarafan scouts and Guild informants have the chamber's location; the Session 3 approach is under surveillance |
| `sarafan_bloc` | `one_contact` | Rook's private channel opens; she will warn the party once before Session 4 if the hardliners plan a move |

---

## GM Notes

- The claimant's task should be morally neutral but politically loaded. Good options: retrieve a sealed command record only the party can be trusted to handle neutrally; witness an oath binding that removes a rival's grounds for a later legal challenge; expose a Guild informant the claimant knows is there but can't act against without implicating themselves.
- Archivist Sen Vael's interest in the same task site as the party is not a coincidence. He followed the party because anyone assigned to that site probably has access the Accord wants. He is not directly hostile — he just wants to be there.
- Maelin Rook is always watching. The party doesn't need to fail for her to write a useful report. She writes what is useful to the Sarafan whether or not the party cooperates.
- This scene's energy should feel like the morning after the first real political meal: everyone is polite, everyone has already made three decisions the party doesn't know about.
