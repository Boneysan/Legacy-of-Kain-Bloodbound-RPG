# 04 — Fulcrum Contact

The Black Fulcrum is not a faction. It is an assessment. When the balance-relevant decision becomes immediate — when the Heart is assembled and the party has a coalition recognized or contested, and an account logged with the Hall — the Fulcrum convenes. This scene is the rendering of all prior arc choices into a single structured judgment: can the party defend their account to someone who has read everything, has no stake in the outcome, and will ask the question no one else has been willing to ask?

---

## Scene Info

- **Arc / Session:** Arc IV — Session 3 (the examination before the final session; fires after Vignettes 01–03 are resolved)
- **Trigger:** Merel has assembled all arc-relevant material. Kain, if present, has sent word that the party's account will be examined before he commits to any final position. This scene is that examination.
- **Scene Type:** `reckoning` + `examination`
- **Est. Duration:** 7–10 min
- **Tags This Scene Can Change:** `black_fulcrum_status`, `heart_purpose`, `coalition_shape`

---

## Cast

| NPC | Role in This Scene |
|-----|--------------------|
| Kain | Rare intervention; present in person only if `party_operative_truth` was committed in Arc III AND `coalition_shape` is recognized; otherwise represented by silence or Sevran |
| Warden Asha Merel | Conducts the examination; her questions derive from the arc state tags |
| Black Marshal Sevran | Present if not already arrived as party anchor; confirms or withholds Kain-side backing on the basis of Fulcrum outcome |
| The Last Witness | Present if `black_fulcrum_status: witness-anchored`; their testimony weighs on the final question |

---

## Opening Narration

> The room the examination takes place in is not the Hall chamber. It is a record room — three walls of archived material and one window with ice on the outside of the glass. Warden Asha Merel has assembled the relevant precis: the arc state records, the account the party gave in the Hall session, and the contradiction map that Iriane Quell prepared at the Chronoplast. She is not using them as evidence. She is using them as a structure around which to ask questions that cannot be answered by referring to documents. Black Marshal Sevran is in the room, in the corner, and he is not speaking unless spoken to, and his expression is the expression of a person who knows how this particular type of conversation goes and is waiting to see which way this version goes. If Kain is present, he is sitting at the table. He has already read everything. He is waiting for the party to say it out loud, in sequence, to someone who is not going to let them abbreviate.

---

## NPC Opening Line

> **Warden Asha Merel:** *"I'm going to ask you several questions derived from the arc record. The purpose is not to verify facts — the documents handle that. The purpose is to understand whether the people claiming accountability for this account understand what they are accountable for."* She looks at whoever named accountability in Vignette 02 — or at the whole party if collective accountability was chosen. *"We'll start with the simplest one. What do you believe the Heart of Nosgoth will do to the person or faction that uses it?"*

---

## The Examination (Three Questions)

Merel asks three questions, derived from the party's arc state. Each question should be GM-customized based on the actual arc-state tags. Defaults are provided below.

---

### Question 1 — What Does the Heart Do to the One Who Uses It?

> Default: *"Before we discuss what the Heart does to Nosgoth, I need to know whether you understand what it does to whoever activates it. Not the mythology. What you actually believe, based on what you've seen."*

**Party Response Types:**

| Response | Merel | Sevran | Kain (if present) |
|----------|-------|--------|-------------------|
| Confident and specific | "That is consistent with what we have." Notes it. | Nods once; does not change posture | Evaluates — no reaction |
| Uncertain but honest | "Uncertainty noted. We proceed." | Still evaluating | "Honest" — quietly, to no one |
| Confident but dismissive of personal cost | Pauses. "Are you prepared for it? Prepared is different from aware." | Slight tension | If Kain: "Prepared, they said. We'll see." |
| Refuses to answer until the purpose is ratified collectively | "The examination doesn't wait for consensus. That is its function." | Frowns | — |

---

### Question 2 — Question Derived From `party_operative_truth`

> Merel takes the `party_operative_truth` tag and asks the party to defend it against *its worst consequence*.

**If `balance-through-sacrifice`:** *"The continuity you are trying to preserve — name one thing that should not survive it. One faction, one structure, one old arrangement. If your account doesn't require anything to be foreclosed, it isn't an account. It's a preference."*

**If `hylden-reintegration`:** *"Name the terms the Hylden have agreed to that you believe they will honor for longer than one generation. Not what you hope. What they have agreed to, explicitly, in the Hall's public record."*

**If `undecided`:** *"You have not committed to an account. I am going to ask you one more time, in this room, with these people. If you cannot give me an answer now, the Fulcrum finds no basis for recognition of your coalition's stated purpose."*

**If `unresolved`:** *"Do you know what your coalition is for?"* — and then silence.

---

### Question 3 — The Question No One Has Asked

> Derived from the campaign's deepest unresolved tag. GM selects from:

**If `betrayal_resolved: unresolved`:** *"There is a person in your coalition's history who carried a false account and did not correct it. You have not resolved what that means for the coalition's reliability. I am asking you: can a coalition with an unaddressed breach in its record be trusted to maintain an account it claims is true?"*

**If `betrayal_resolved: absorbed`:** *"The person who carried the false account is now absorbing the correction. They are still in your coalition. What guarantees that the same pressure that shaped the false account doesn't shape the correction?"*

**If `wheel_exposure: hidden`:** *"The Wheel's interference was not publicly named in Arc III. That account is still in circulation. Who, in your coalition, is responsible for correcting it — and when?"*

**If `chronal_shard_fate: broken`:** *"The Shard was broken rather than secured. The intelligence from the Chronoplast is therefore incomplete. Are you proceeding on an incomplete account or a complete one?"*

---

## After the Three Questions — The Fulcrum Finding

Merel makes a determination. It does not have to be the party's preference. It reflects whether the answers held:

> **If answers were consistent and accountable:** *"The Fulcrum finds the coalition's account defensible. It has gaps. All accounts have gaps. The specific gaps are now on record. Kain-side resourcing is available for the final session."* Sevran confirms.

> **If answers were partial or deflected:** *"The Fulcrum finds the coalition's account functional but not complete. For the purposes of the final session, the incomplete portions are the points your opposition will use. You've had this conversation. You know where they are."*

> **If answers were inadequate or evasive:** *"The Fulcrum cannot find the coalition's account defensible in its current form. That does not foreclose the final session. It means you go into it without the Fulcrum's recognition, which is a structural disadvantage, not a verdict."*

---

## Tags

| Fulcrum Finding | Tag Value | Effect on Vignette 05 |
|-----------------|-----------|----------------------|
| Defensible | `black_fulcrum_status: cleared` | Heart activation authorized in final session; Kain-side backing confirmed |
| Functional-incomplete | `black_fulcrum_status: conditional` | Heart activation conditionally available; Sevran present but not fully committed |
| Not defensible | `black_fulcrum_status: unfounded` | Party goes into Vignette 05 without Fulcrum recognition; harder path; still winnable |

Additionally:
- Strong honest answers on Question 1 → `heart_purpose: understood`
- Party names `party_operative_truth` term correctly under pressure → no additional tag, but Merel notes it in the formal record
- Last Witness present and testimony matches the party's account → `coalition_shape` upgraded (remove fracture notation if present)

---

## GM Notes

- This scene should feel like a deposition in the best possible sense: rigorous, uncomfortable, and focused. Merel is not hostile. She is thorough. The questions are derived from the party's actual record. There are no trick questions — only honest ones that are hard to answer.
- Kain's presence, if earned, should be quiet and weighty. He may speak exactly once, in response to something the party says that earns a response. The GM should decide in advance what line crosses that threshold. A suggested trigger: if the party names something they are willing to sacrifice, without being asked to, that names the same thing Kain once named in his own account — he will acknowledge it. Not warmly. Just: *"Yes."*
- If `betrayal_resolved` is still `unresolved` at this stage, Merel's third question will be about reliability. The party should feel — not punished, but seen. The breach is not fatal. It is a documented liability. That is different.
- The Fulcrum finding is a structural outcome, not a verdict on whether the party is good people. Make sure Merel's language reflects that. The Hall has seen many coalitions. It has seen many good people with bad accounts and many flawed people with defensible ones. What the Fulcrum tests is the account.
