# Arc I — VTT Story-State Tracker

Update this file after each vignette resolves. At the start of each session, review it to confirm which version of each scene, NPC relationship, and faction posture is currently active. Carry these values forward into Arc II when Arc I closes.

---

## Story-State Tags

<a id="serit_trust"></a>
### `serit_trust`
Tracks Serit Vale's level of openness with the party. Affects her warning behavior, information access, and Arc II Accord cooperation.

| Value | Meaning |
|-------|---------|
| `low` | She is managing the party as assets; information is withheld by default; she is filing independent reports |
| `guarded` | She cooperates when directly useful; requires the right questions; no volunteered intelligence |
| `earned` | She treats the party as investigative partners; warns of threats first; Accord intelligence available in Arc II |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="guild_pressure"></a>
### `guild_pressure`
Tracks the Outlands Guilds' posture toward the party. Affects Mera Ash's behavior and whether the Guilds send a second operative in Arc II.

| Value | Meaning |
|-------|---------|
| `low` | Guilds consider the party productive; Mera Ash's support is operational rather than watchful |
| `high` | Guilds are uncertain about the party's reliability; Mera Ash is followed by a second Guild contact; operational support is transactional |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="sarafan_attention"></a>
### `sarafan_attention`
Tracks how many confirmed data points the Sarafan Order has about the party and the fragment. Feeds the Sarafan Purge Clock.

| Value | Meaning |
|-------|---------|
| `0` | No confirmed intelligence; patrols are regional, not targeted |
| `1` | One informant, witness, or incident has given the Order a useful description; targeted inquiry has started |
| `2` | The Order has the party's identities, known associates, and a formal record of the Avernus incident; pursuit begins in Arc II |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="reliquary_status"></a>
### `reliquary_status`
Tracks what the party knows and has done with the Sanguine Knot — both physically and informationally.

| Value | Meaning |
|-------|---------|
| `sealed` | Fragment in contained custody; no direct examination; its behavior is inferred rather than confirmed |
| `examined` | Fragment has been approached, studied, or responded to; its blood-active behavior is confirmed; cult now knows someone in the party is sensitive |
| `compromised` | Fragment has been touched, opened, or involved in a rite; its full influence is in active play; Corruption pressure activates |
| `stolen` | Fragment is no longer in party-aligned custody; it is being moved toward a faction objective |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="public_story"></a>
### `public_story`
Tracks what people outside the party believe happened at Avernus and on the caravan road. Affects witness behavior, cult response posture, Sarafan intelligence quality, and what the party can credibly claim in Session 6.

| Value | Meaning |
|-------|---------|
| `panic` | Witnesses are talking; stories are fragmentary and frightening; the Sarafan have heard enough to act; cult cells are going quiet |
| `secrecy` | Survivors stayed controlled; no public account has circulated; the party has cover but reduced support from visible allies |
| `controlled_lie` | The party or an ally has provided a coherent false account; it will hold until Session 6's social consolidation unless actively probed |
| `open_truth` | The party allowed or caused the accurate account to reach public or institutional ears; Sarafan attention advances; Accord position shifts |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="last_witness"></a>
### `last_witness`
Tracks the campaign's throughline civilian — the latest ordinary survivor who can still speak a fragment's cost in plain terms, with no faction varnish. This is a structured field, not a single enum: record **who** they are, **what** they witnessed, **what** they fear forward, and their current **status**. Carry it forward across every arc. The Arc IV finale (V02 Choice D → `black_fulcrum_status: witness-anchored`, and V05 Outcome D) is only reachable if a `named` or `protected` Witness has survived to the Heath. If the role is `unnamed` or `lost` at the close of Arc III, the GM must seed a replacement before the finale or those endings stay closed.

**Status values:**

| Value | Meaning |
|-------|---------|
| `unnamed` | The role is vacant; no specific person yet carries it. Campaign default, and where the role returns after a Witness is lost |
| `named` | A specific person has spoken a fragment's cost plainly and is identifiable, but their safety is not secured |
| `protected` | The party took a concrete action to keep the Witness alive, free, and able to testify; they reach the next arc |
| `exposed` | A hostile faction knows the Witness's identity and value and is recruiting, discrediting, or hunting them |
| `lost` | The Witness was killed, silenced, co-opted, or abandoned; the role returns to `unnamed` until a new survivor inherits it |

**Current bearer (name + role):** ___
**What they witnessed (the cost they can testify to):** ___
**What they fear forward:** ___
**Current status:** ___
**Session this was last updated:** ___

---

<a id="balance_reckoning"></a>
### `balance_reckoning`
**Single device — this is the per-arc mirror of the canonical Balance Reckoning Clock (0–4) defined in [../Faction-Tracker/Faction-Clocks.md](../Faction-Tracker/Faction-Clocks.md#balance-reckoning-clock). Do not run a second scale or a separate increment list; advance it only per that file's Arc-End Update Cheat Sheet. Read at the finale by the [Endgame Adjudication Matrix](../Arc_IV_Convergence/03_Endgame-Adjudication-Matrix.md) Pressure Modifier (a value of 3–4 hardens the Hall's judgment).**

The counter measures how often the party used a fragment to force a crisis to resolve while leaving the deeper distortion in place — *withdrawal of grace*, not Corruption by another name. **In Arc I it advances** when the Sanguine Knot is touched publicly or used to expose or coerce when mercy was still possible (per the cheat sheet). **Never decrement** — grace withdrawn does not return cheaply.

| Value | Meaning |
|-------|---------|
| `0` | No coercive fragment-answer on record; the world's customary graces remain available |
| `1` | A fragment solution fixed an immediate problem but left a visible metaphysical distortion; a single grace thins — a minor rite is refused, a shrine is shut |
| `2` | Wardens, the Hall, or spectral witnesses begin treating the party as agents of dangerous imbalance rather than reluctant stewards |
| `3` | A prior compromise returns as proof that order was preserved through coercion; safe houses, healers, and sanctioned rites demand explicit price before aid |
| `4` | The endgame judgment hardens; the Hall of Equilibrium and its living representatives no longer treat the party as untested claimants |

**Current value:** ___

**Session this was last updated:** ___

**Notes (which uses incremented it):** ___

---

## Vignette Log

Use this section to record which choices were made in each vignette. Brief notes only — the full consequence is already tagged above.

| Vignette | Session | Choice Made | Key Tags Changed |
|----------|---------|-------------|-----------------|
| 01 — Caravan Argument | | | |
| 02 — The False Refuge | | | |
| 03 — What Serit Knows | | | |
| 04 — First Blood-Memory | | | |
| 05 — Who Carries the Knot | | | |

---

## NPC Relationship Notes

Brief running record of how each key Arc I NPC stands with the party at the close of each session. Carry forward into 02_NPC-Appendix.md if circumstances change significantly.

**Serit Vale:**
- Session 1 end: ___
- Session 2 end: ___
- Session 3 end: ___
- Session 5 end: ___
- Arc close status: ___

**Mera Ash:**
- Arc close status: ___
- Guild standing: ___

**Brother Halden:**
- Exposed / Not exposed: ___
- Survived: ___

**Sister Caris:**
- Introduced: ___
- Party relationship: ___

**Confessor Ilyr Voss:**
- Appeared: ___
- Party standing: ___

---

## Running Notes

*Copy forward from 01_Session-Prep.md Running Notes section as the arc progresses.*

- Which lies the party currently believes:
- Which NPC is compromised but not yet exposed:
- Current owner or bearer of the Sanguine Knot:
- Sarafan posture toward the party:
- Guild posture toward the party:
- Current Corruption consequences in the region:

---

## Carry Forward to Arc II

Complete before the Arc II opening session. Cross-reference with 05_Choice-Consequence-Guide.md.

- `serit_trust` entering Arc II: ___
- `guild_pressure` entering Arc II: ___
- `sarafan_attention` entering Arc II: ___
- `reliquary_status` entering Arc II: ___
- `public_story` entering Arc II: ___
- `last_witness` entering Arc II (bearer, what they witnessed, forward fear, status): ___
- `balance_reckoning` entering Arc II (counter + which uses): ___
- Fragment physical location at arc close: ___
- Surviving allies traveling into Arc II: ___
- Active enemies with motivation to pursue into Arc II: ___
- One wound left open at the end of Arc I: ___
