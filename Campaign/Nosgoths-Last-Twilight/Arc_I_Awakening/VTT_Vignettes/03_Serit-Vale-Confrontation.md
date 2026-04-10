# 03 — What Serit Knows

After the ambush, the party has standing to ask for the truth. Serit Vale has been managing them, and they have had a chance to notice. This scene forces the first real negotiation over information: what she gives the party, and on what terms, shapes every conversation with the Accord from here forward.

---

## Scene Info

- **Arc / Session:** Arc I — Session 1 (post-ambush) or Session 2 (investigation phase)
- **Trigger:** The party has survived the cult ambush or a significant cult incident. Serit Vale is present. A PC directly asks her what the cargo actually is, what the cult wanted, or what she hasn't told them.
- **Scene Type:** `confrontation`
- **Est. Duration:** 4–6 min
- **Tags This Scene Can Change:** `serit_trust`, `reliquary_status`

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| Serit Vale | She has prepared for this conversation. She has a version of the truth precise enough to satisfy and constructed so that only she knows how much it omits. |
| Mera Ash | Present if the party is together. She is not interested in lore. She wants to know whether the cargo is still survivable to transport. |

---

## Opening Narration

> Serit Vale is cleaning something from her hands — not blood, something darker — and she has had precisely the time required to arrange what she will say. She has known the question was coming since the waymarker. Her satchel is on the table between you and her, and she has not reached for it since she sat down.

---

## NPC Opening Line

> **Serit Vale**, meeting the question before it is fully asked: *"I will answer what I can answer clearly. The rest I will describe in terms of what I believe rather than what I can demonstrate, because demonstrating it in the field is what this whole exercise was meant to avoid."*

---

## Player Choices

### A — Demand Full Disclosure Now

> No more framing. What is it, where did it come from, and who else knows.

**NPC Response:**

> *"It is called the Sanguine Knot. It is a blood-active fragment whose original site predates the current cathedral and possibly the Order that built it. It responds to inherited blood and broken vows — which is not a metaphor."* She folds her hands. *"The Accord's position is that it must be documented below Avernus before anyone else can claim it. The cult's position apparently includes armed recovery. That is what I can confirm. What I am choosing not to tell you relates to the Accord's prior knowledge of the site, which is an internal matter and will remain one until I have better leverage than gratitude for surviving tonight."*

**Outcome:** She has told the party the functional truth and labeled the gap explicitly. They know the relic is named, blood-active, and site-bound to a pre-Avernus location. They also know she is managing them and she knows they know. `serit_trust` rises because honesty about the limits of honesty is still honesty.

**Tags:** `serit_trust: earned`, `reliquary_status: examined`

---

### B — Accept Partial Truth and Offer Trust in Return

> Tell her you don't need everything. You need enough to do your job. What does she *need* you to know?

**NPC Response:**

> Serit pauses. This answer was not in her prepared version. *"What I need you to know is that the object has probably been active since before we left the departure point. That one or more people in the caravan noticed it first, said nothing, and that the cult attack was not random targeting of a supply route."* She looks at whoever is nearest to the satchel. *"It knew specific people. I don't know how. That is what the Accord is trying to understand."*

**Outcome:** She gives the party actionable intelligence rather than background lore. They now know the relic already identified specific individuals — which implies someone in their group, possibly including a PC. This is the more useful disclosure. `serit_trust` is stable but she is calculating whether this trade will pay.

**Tags:** `serit_trust: guarded`, `reliquary_status: examined`

---

### C — Threaten or Pressure Her for the Information

> She works for the Accord. The Accord is not here. She needs the party more than the party needs her right now.

**NPC Response:**

> Serit goes very still. *"That is true. I do. But you are operating under the assumption that I need to describe the object's full significance to move it safely, and that assumption is wrong."* She does not raise her voice. *"If you want what I know, I'll trade it for what you know. Tell me which member of your group the fragment answered to on the road, and I'll tell you what the Accord believes that means."*

**Outcome:** She has countered the leverage. Now the party must decide whether to volunteer sensitive personal information in exchange for Accord lore. If anyone reveals a PC's blood-connection to the relic, Serit gains advantage in all future Accord negotiations. If they refuse, she closes the conversation and they get nothing new.

**Tags:** `serit_trust: low`, `reliquary_status: sealed`

---

### D — Tell Her You Already Know More Than She Thinks

> Bluff — or reveal — that someone in the party has already experienced the relic's influence directly.

**NPC Response:**

> Serit Vale sets down what she was holding. This is the first genuinely unguarded expression the party has seen from her. *"Show me."* She does not say *prove it.* She says *show me,* and she means physically — a sign, a pulse, a recognition event. If the party has one, she will do a controlled test right now, in this room, in a way that exposes considerably more of her real knowledge than she planned to share tonight. *"If it answered you and you knew what you were receiving — we are in different circumstances than I thought."*

**Outcome:** If the party has a genuine relic-sensitive PC and can demonstrate it, Serit immediately opens her notes, names the Accord's prior site research, and begins treating the party as investigative partners rather than assets. `serit_trust` maxes out, but she also now reports to the Accord that a bloodline carrier is in the field, which has its own consequences in Arc II.

**Tags:** `serit_trust: earned`, `reliquary_status: examined`

---

## If No Clear Choice Is Made

> If the party asks the question and then backs down under her framing, lets her redirect, or accepts her opening statements without any pushback: she thanks them for their work tonight, closes her notes, and goes to sleep. She tells them exactly nothing new. The Accord's prior knowledge remains hidden.

**Default Tag:** `serit_trust: guarded`, `reliquary_status: sealed`

---

## Next-Scene Effects

| Tag | Value | Effect on next scene or encounter |
|-----|-------|-----------------------------------|
| `serit_trust` | `earned` | Serit warns the party before any move against them in Sessions 2–3; she becomes a genuine ally with limits rather than a managed asset |
| `serit_trust` | `guarded` | Serit cooperates when directly useful and withholds when it costs her; the party must ask the right questions to get anything |
| `serit_trust` | `low` | Serit begins coordinating with Accord resources independently; the party may discover she has been sending reports that do not include them |
| `reliquary_status` | `examined` | The party knows the relic's name, behavior, and site-link; they can use this to identify cult objectives in Session 2's investigation |
| `reliquary_status` | `sealed` | The party has no confirmed details; they work the Session 2 investigation by instinct rather than knowledge |

---

## GM Notes

- Serit is not villainous in this scene. She is managing competing obligations and doing it professionally. Play her as someone who knows the right answer and is choosing a slower route to it for defensible reasons.
- Choice D's trigger requires a PC to have already experienced a relic event — specifically the `reliquary_status: examined` result from Vignette 01 or the first blood-memory pulse in Vignette 04. Don't offer this option if it hasn't happened.
- The Accord's prior knowledge of the site (the thing she explicitly withholds in Choice A) is a major Arc II revelation. Don't let her give it here even under Choice D — she reveals she knows more, not what she knows.
- Mera Ash, if present, will not add much. She may audit the exchange for useful logistics information and otherwise stay silent. She does not trust Serit, but she considers this conversation appropriate and will not interrupt it.
