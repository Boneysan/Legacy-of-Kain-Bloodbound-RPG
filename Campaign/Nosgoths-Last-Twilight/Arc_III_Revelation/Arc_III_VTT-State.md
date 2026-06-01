# Arc III — VTT Story-State Tracker

Update this file after each vignette resolves. In Arc III, story-state tracks not just faction posture but which interpretations the party has committed to — and which futures they have made operative by acting on them.

Default contradiction for Arc III: the public northern record says Hylden pressure or party breach logic drew first blood at the Resonance Pillar. The corrected record shows a Sarafan containment volley under Scout-Confessor Maelin Rook's authority hit the Accord working ring first.

---

## Carry-In Values (from Arc II)

| Tag | Arc II Closing Value | Notes |
|-----|----------------------|-------|
| `fortress_claim` | ___ | |
| `iron_echo_status` | ___ | |
| `hylden_engagement` | ___ | |
| `sarafan_bloc` | ___ | |
| `ash_glass_reach` | ___ | |
| `last_witness` | ___ | Bearer, what they witnessed, forward fear, status |
| `balance_reckoning` | ___ | Counter carried from Arc II |

---

## Arc III Story-State Tags

<a id="chronoplast_access"></a>
### `chronoplast_access`
Tracks what the party was able to learn at the Chronoplast and how reliably they can now speak about the corrected northern breach record and the Heart's future claims.

| Value | Meaning |
|-------|---------|
| `denied` | Party could not access or interpret the site; the Wheel controlled the reading and the public first-blood account remains uncorrected |
| `partial` | Party accessed fragments; the truth is pointed toward but not resolved, including the corrected Resonance Pillar sequence |
| `full` | Party received a complete reading; they know the Heart's function and at least one decisive future, and they have enough evidence to act on the corrected northern breach record |

**Current value:** ___

**Notes:** ___

---

<a id="chronal_shard_fate"></a>
### `chronal_shard_fate`
Tracks what happened to the Chronal Shard during Arc III.

| Value | Meaning |
|-------|---------|
| `recovered` | Party holds the shard; they carry forward both its interpretive power and the obligation of having chosen a future |
| `destroyed` | Shard was eliminated; the specific futures it revealed are no longer accessible; the Wheel cannot use them either |
| `lost` | Shard taken by the Wheel or another faction; their prophetic framing now has an artifact basis |
| `divided` | The shard's visions were distributed among multiple parties; the future question and the corrected northern breach record are now political as well as personal |

**Current value:** ___

**Notes:** ___

---

<a id="wheel_exposure"></a>
### `wheel_exposure`
Tracks whether the Cult of the Wheel's true agenda has been made public or politically live.

| Value | Meaning |
|-------|---------|
| `concealed` | Wheel operations known to the party but not confirmed publicly; they can still operate behind mercy-doctrine framing |
| `named` | Party has circulated proof or accusation against the Wheel; Wheel loses soft power but hardens into more aggressive posture |
| `broken` | A specific Wheel cell or operation was dismantled; the broader cult is aware the party is an active threat |

**Current value:** ___

**Notes:** ___

---

<a id="party_operative_truth"></a>
### `party_operative_truth`
The single most important Arc III tag: which mutually exclusive future did the party treat as *real* — the one they acted on?

| Value | Meaning |
|-------|---------|
| `balance-through-sacrifice` | The party commits to continuity through costly stabilization and refuses ownership as the campaign's primary answer |
| `hylden-reintegration` | The party commits to negotiated Hylden return on explicit terms as the campaign's primary answer |
| `undecided` | The party carries competing accounts into Arc IV and accepts structural weakness in coalition formation |
| `unresolved` | No commitment was made before Arc III closed; treat as `undecided` for routing, but with delayed support timing |

**Current value:** ___

**Optional note (`party_operative_truth_note`):** Use for provenance or context such as `chosen-under-testimony`, record strategy, or intended disclosure scope.

**Notes:** ___

---

<a id="betrayal_resolved"></a>
### `betrayal_resolved`
Tracks how Arc III's internal betrayal resolved around the corrected northern breach record — when it clarified one arc while complicating the endgame.

| Value | Meaning |
|-------|---------|
| `unresolved` | The betrayal or custody fight around the corrected northern breach record has not yet surfaced or been named |
| `absorbed` | Party knows what happened, including the Maelin Rook first-volley reversal, and has chosen how to interpret it; the relationship continues in changed form |
| `severed` | The betrayed relationship is ended; one previous ally is now a free agent or opposed actor carrying, disputing, or leaking the corrected record |
| `weaponized` | The corrected northern breach record was publicly exposed or used strategically; its reverberations are live in Arc IV coalition politics |

**Current value:** ___

**Notes:** ___

---

<a id="last_witness"></a>
### `last_witness`
The campaign's throughline civilian — the latest ordinary survivor who can still speak a fragment's cost in plain terms. Structured field, not a single enum: record **who** they are, **what** they witnessed, **what** they fear forward, and their **status**. *Do not confuse this with the Arc III betrayer* tracked by `betrayal_resolved`: that is the person who carried the corrected northern record; the Last Witness is the ordinary survivor who can testify to its cost without a stake. Carry it forward. The Arc IV finale (V02 Choice D and V05 Outcome D) is only reachable if a `named` or `protected` Witness survives to the Heath — so the Witness's safety should be on the table when the corrected record goes public this arc.

**Status values:**

| Value | Meaning |
|-------|---------|
| `unnamed` | Role vacant; no specific person carries it |
| `named` | A specific person has spoken a fragment's cost plainly; identifiable but unprotected |
| `protected` | The party took concrete action to keep them alive, free, and able to testify at the Heath |
| `exposed` | A hostile faction (often the Wheel, once the record turns public) knows their identity and value and is moving against them |
| `lost` | Killed, silenced, co-opted, or abandoned; role returns to `unnamed` |

**Current bearer (name + role):** ___
**What they witnessed (the cost they can testify to):** ___
**What they fear forward:** ___
**Current status:** ___
**Session this was last updated:** ___

---

<a id="balance_reckoning"></a>
### `balance_reckoning`
**Single device — this is the per-arc mirror of the canonical Balance Reckoning Clock (0–4) defined in [../Faction-Tracker/Faction-Clocks.md](../Faction-Tracker/Faction-Clocks.md#balance-reckoning-clock). Do not run a second scale or a separate increment list; advance it only per that file's Arc-End Update Cheat Sheet. Read at the finale by the [Endgame Adjudication Matrix](../Arc_IV_Convergence/03_Endgame-Adjudication-Matrix.md) Pressure Modifier (a value of 3–4 hardens the Hall's judgment).**

The counter measures how often the party used a fragment to force a crisis to resolve while leaving the deeper distortion in place — *withdrawal of grace*, not Corruption by another name. **In Arc III it advances** when the party compel a Chronoplast reading or act on the Chronal Shard to force one future operative over another (per the cheat sheet). It is also the value read by this arc's road scenes to render withdrawal of grace (see Vignette 03). **Never decrement.**

| Value | Meaning |
|-------|---------|
| `0` | No coercive fragment-answer on record; customary graces remain available |
| `1` | A fragment solution fixed an immediate problem but left a visible metaphysical distortion; a single grace thins |
| `2` | Wardens, the Hall, or spectral witnesses begin treating the party as agents of dangerous imbalance rather than reluctant stewards |
| `3` | A prior compromise returns as proof that order was preserved through coercion; aid demands explicit price before it is given |
| `4` | The endgame judgment hardens; the Hall and its living representatives no longer treat the party as untested claimants |

**Current value (carry the Arc II total forward, then advance for any Arc III use):** ___

**Session this was last updated:** ___

**Notes (which uses incremented it):** ___

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

## NPC Relationship Notes

**Serit Vale (carry-forward):**
- Arc III role (if still active): ___

**Key Arc III NPCs:**
- Wheel representative encountered: ___
- Kain contact or proxy (if any): ___
- Remaining Accord or Guild presence: ___

---

## Carry Forward to Arc IV

- `chronoplast_access` entering Arc IV: ___
- `chronal_shard_fate` entering Arc IV: ___
- `wheel_exposure` entering Arc IV: ___
- `party_operative_truth` entering Arc IV: ___
- `party_operative_truth_note` entering Arc IV (optional): ___
- `betrayal_resolved` entering Arc IV: ___
- `last_witness` entering Arc IV (bearer, what they witnessed, forward fear, status — MUST be `named` or `protected` for the V05 Witness ending): ___
- `balance_reckoning` entering Arc IV (counter + which uses): ___
- Hylden engagement level entering Arc IV (from Arc II): ___
- Surviving coalition partners: ___
- Active enemies with armies, rites, or ultimatums arriving at Pillar Heath: ___
- One truth the party knows that no other faction has, if any: ___
