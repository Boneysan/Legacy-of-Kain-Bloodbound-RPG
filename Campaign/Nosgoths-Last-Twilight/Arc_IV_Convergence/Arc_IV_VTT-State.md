# Arc IV — VTT Story-State Tracker

The final tracker. Arc IV has no Carry Forward — it has outcomes. Use this file to record the state of the world as the party moves through Convergence. At the close of each session, update the tags. At the end of the campaign, this document describes Nosgoth's post-campaign state.

---

## Carry-In Values (from Arc III)

| Tag | Arc III Closing Value | Notes |
|-----|----------------------|-------|
| `chronoplast_access` | ___ | |
| `chronal_shard_fate` | ___ | |
| `wheel_exposure` | ___ | |
| `party_operative_truth` | ___ | |
| `betrayal_resolved` | ___ | |
| `hylden_engagement` (from Arc II) | ___ | |

---

## Arc IV Story-State Tags

### `coalition_shape`
Tracks the party's coalition status through the Heath proceedings and into the final confrontation. Vignettes 01–03 write *process values* as the coalition forms; the *assessment value* summarises the coalition’s overall shape at the close of Vignette 04.

**Process values (written during Vignettes 01–03):**

| Value | Source | Meaning |
|-------|--------|--------|
| `unified-pending` | V01-A | Party enters as the swing coalition, Sevran-backed; positioned to anchor the proceedings |
| `contested-opening` | V01-B | No prior positioning; party builds from faction offers without a guaranteed anchor |
| `internally-fractured-but-functioning` | V01-C | Internal divergence acknowledged; external unity declared; coalition security decision required |
| `merel-advised` | V01-D | Pre-session private faction approach unlocked by Merel’s counsel; party must choose which faction to approach |
| `unanchored` | V01-default | No anchor; all factions pitch simultaneously; increased difficulty through Vignettes 02–03 |
| `recognized` | V02-A,B | Hall recognition confirmed with named accountability on record |
| `conditionally-recognized` | V02-C | Partial recognition; account must be completed at the Fulcrum examination (Vignette 04) |
| `witness-anchored-recognition` | V02-D | Last Witness bound into the formal coalition record; present at Vignette 04 |
| `unrecognized` | V02-default | Hall did not recognise the coalition; all factions negotiate knowing the party lacks Hall backing |
| `procession-neutral` | V03-B | Procession does not interfere with final proceedings |
| `procession-hostile` | V03-B/default | Procession in active disruption posture; logistics complications in Vignettes 04–05 |
| `structure-challenged` | V03-A | Accountability gap in coalition’s own structure; queried directly at the Vignette 04 Fulcrum examination |
| `grief-named` | V03-D | Party’s unresolved grief named as a strategic liability; available as a formal statement in Vignette 05 |

**Assessment values (written at close of Vignette 04, after coalition shape is finalised):**

| Value | Meaning |
|-------|---------|
| `none` | The party acts alone or with minimal support; maximum difficulty, maximum autonomy |
| `fractured` | Two or more factions nominally aligned but pursuing different outcomes; the coalition may split at the worst moment |
| `unified_goal` | Coalition factions share a tactical objective but not a post-campaign vision; they will fight together and then dispute the result |
| `unified_vision` | The party forged an alliance around a shared interpretation of the Heart’s purpose; breakage is possible but not inevitable |

**Current value:** ___

**Notes:** ___

---

### `black_fulcrum_status`
Tracks the coalition’s examination record status at the Hall of Coalition — which determines how the Fulcrum examination proceeds and what Kain-side backing is available for the final session. *Physical custody of the Black Fulcrum artifact, if relevant to your campaign, should be noted in GM Notes rather than this tag.*

**Hall record values (written during Vignette 02, carried into Vignette 04):**

| Value | Source | Meaning |
|-------|--------|--------|
| `active` | V02-A | Full named accountability on record; Fulcrum examination proceeds with the named party member answering |
| `active-collective` | V02-B | Collective accountability logged; each party member answers the examination independently |
| `partial` | V02-C | Partial recognition; account must be completed at the start of Vignette 04 before the examination proceeds |
| `witness-anchored` | V02-D | Last Witness is part of the formal record; their testimony weighs in the examination and changes its emotional register |
| `dormant` | V02-default | Coalition unrecognised; Vignette 04 runs as a crisis session rather than a formal examination |

**Fulcrum finding values (written at the close of Vignette 04):**

| Value | Source | Meaning |
|-------|--------|--------|
| `cleared` | V04-defensible | Account defensible; Kain-side resourcing available for the final session; Sevran confirms |
| `conditional` | V04-functional | Account functional but incomplete; Sevran present but not fully committed |
| `unfounded` | V04-inadequate | Account not defensible; party enters Vignette 05 without Fulcrum recognition; harder path, still winnable |

**Current value:** ___

**Notes:** ___

---

### `hylden_gate_resolution`
Tracks the final state of the Hylden Gate threat.

| Value | Meaning |
|-------|---------|
| `sealed` | Gate closed or reinforced; Hylden incursion ended; the breach network cannot reopen without extraordinary effort |
| `displaced` | Gate moved, redirected, or temporarily closed; Hylden threat is deferred rather than resolved; will return |
| `open` | Gate remains active; Hylden presence is a permanent feature of post-campaign Nosgoth; the party’s victory is conditional |
| `negotiated` | Party reached a binding arrangement with Hylden remnants; the breach is managed rather than opposed; contested legitimacy |
| `deferred` | Gate left unaddressed; party’s chosen outcome was Pillar restoration rather than gate resolution; Hylden question remains open for a successor coalition |
| `open-on-terms` | Gate activated with publicly recorded access conditions and stated Hylden commitment; equivalent to *negotiated* but with explicit, challengeable terms on record |
| `reth-adjacent` | *Intermediate value.* Reth’s stated access conditions partially converge with Hylden terms; Glass Voice has noted the alignment; overwritten by the Vignette 05 declaration |

**Current value:** ___

**Notes:** ___

---

### `wheel_final_state`
Tracks the Cult of the Wheel’s condition at campaign close.

| Value | Meaning |
|-------|---------|
| `active` | Wheel is diminished but intact; surrender-doctrine continues as a live force in Nosgoth’s future |
| `broken` | Key Wheel infrastructure destroyed or leadership ended; doctrine may survive without institutional power |
| `absorbed` | Wheel doctrine partially integrated into the post-campaign order; its ideas won even if the movement did not |
| `transcended` | Party demonstrated a third option beyond fate and ruin; the Wheel has no counter-argument left |
| `reduced-surviving` | Wheel survives as philosophy only, stripped of institutional influence; doctrine persists without active reach or recruitment |
| `opposing-surviving` | Wheel opposed the outcome, remained to witness it, and continues as principled opposition; diminished but not eliminated |
| `default-surviving` | Outcome did not address the Wheel; the campaign closes with the Wheel’s position unchanged from its pre-convergence state |
| `contested` | *Intermediate value.* Wheel cannot claim sole legitimate philosophy; Hall proceedings admit competing accounts; overwritten by the Vignette 05 declaration |

**Current value:** ___

**Notes:** ___

---

### `heart_purpose`
The single most important Arc IV tag: what did the party decide the complete Heart of Darkness is *for*?

> This tag does not use preset values. Write a brief sentence describing the party's final decision about the Heart's purpose and what Nosgoth's post-campaign equilibrium looks like as a result. This is the campaign's final line.

**The party's answer:**

___

---

## Vignette Log

| Vignette | Session | Choice Made | Key Tags Changed |
|----------|---------|-------------|-----------------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

---

## Final Coalition Map

Record every faction's status at the campaign's close.

| Faction | Final Posture | Key NPC Fate | Notes |
|---------|--------------|--------------|-------|
| Sarafan Order | | | |
| Pale Accord | | | |
| Outlands Guilds | | | |
| Vampire Clans | | | |
| Cult of Hash'ak'gik | | | |
| Cult of the Wheel | | | |
| Hylden Remnants | | | |
| Crimson Fracture / Ash-Glass | | | |

---

## Campaign End-State

Write one paragraph — no bullet points — describing Nosgoth after the Heart's fate is decided. Include: who survived, who rules or claims to, what the Hylden situation looks like, what the spiritual landscape of the realm is, and what unresolved tension remains for anyone telling stories in this timeline afterward.

**Nosgoth's post-campaign state:**

___

---

## Player Character Epilogues

*Optional. One sentence per PC: where they are, what they carry, and what question about themselves the campaign left unanswered.*

| Character | Played by | Epilogue |
|-----------|-----------|---------|
| | | |
| | | |
| | | |
| | | |
