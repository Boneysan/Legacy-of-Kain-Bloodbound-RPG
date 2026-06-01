# Arc II — VTT Story-State Tracker

Update this file after each vignette resolves. Cross-reference Arc I carry-forward values before the opening session. The tags below cover the political, military, and breach-related pressures specific to Arc II: Ascension.

---

## Carry-In Values (from Arc I)

Record the closing Arc I tag values here before play begins.

| Tag | Arc I Closing Value | Notes |
|-----|---------------------|-------|
| `serit_trust` | ___ | |
| `guild_pressure` | ___ | |
| `sarafan_attention` | ___ | |
| `reliquary_status` | ___ | |
| `public_story` | ___ | |
| `last_witness` | ___ | Bearer, what they witnessed, forward fear, status |
| `balance_reckoning` | ___ | Counter carried from Arc I |

---

## Arc II Story-State Tags

<a id="fortress_claim"></a>
### `fortress_claim`
Tracks how the Dumah's Fortress dispute resolved. Feeds clan posture, Iron Echo access, and who controls military passage northward.

| Value | Meaning |
|-------|---------|
| `unsettled` | No binding resolution; multiple claimants still active; alliances are provisional |
| `party_backed` | The party supported a specific claimant; that clan owes a debt and the rival owes a grudge |
| `contested` | The fortress is in operational dispute; no safe passage; the Iron Echo cannot be accessed cleanly |
| `neutral_brokered` | The party refused to back one side and negotiated a temporary compact; no debts, no grudges, no trust |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="iron_echo_status"></a>
### `iron_echo_status`
Tracks what happened to the Iron Echo fragment during the fortress arc.

| Value | Meaning |
|-------|---------|
| `sealed` | Fragment secured and in defined custody; politically explosive but contained |
| `contested` | Fragment known location but disputed access; two or more factions have a live claim |
| `lost` | Fragment moved or taken during the fortress conflict; the party must locate it before it matters strategically |
| `used` | Fragment was drawn upon during the arc; its seal-reinforcing or exposure properties are now public knowledge |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="hylden_engagement"></a>
### `hylden_engagement`
Tracks how the party handled first Hylden contact at the Rift Ember breach.

| Value | Meaning |
|-------|---------|
| `none` | No meaningful engagement; Hylden treated as environmental threat only |
| `negotiated` | Some form of contact beyond combat; Hylden have identified a PC as a possible vessel or negotiator |
| `contained` | Breach was sealed or partially stabilized; Hylden pressure withdrawn but not resolved |
| `escalated` | Breach worsened; Hylden have a foothold; Hylden Gate mechanics are live in Arc III |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="sarafan_bloc"></a>
### `sarafan_bloc`
Tracks which Sarafan faction now sees the party as useful vs. an active target.

| Value | Meaning |
|-------|---------|
| `divided` | Proceduralist bloc considers the party tolerable; hardliner bloc is openly hostile; the party can exploit the split |
| `unified_against` | Both Sarafan factions have agreed the party is a priority target; no useful Sarafan contacts remain |
| `one_contact` | One Sarafan figure (confessor, proceduralist, field agent) has opened a private line; they will not last if discovered |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="ash_glass_reach"></a>
### `ash_glass_reach`
Tracks whether the Crimson Fracture's Ash-Glass Procession gained meaningful access to Arc II events.

| Value | Meaning |
|-------|---------|
| `fringe` | Ash-Glass scouts observed but did not act; they have data but no leverage |
| `proof_text` | Procession gained a surviving fragment account, witness, or relic impression; Ash-Glass Reth is now a stronger rhetorical threat |
| `convert` | One Arc II NPC or minor faction figure has adopted Ash-Glass doctrine; the Fracture has a voice in the Arc III political landscape |

**Current value:** ___

**Session this was last updated:** ___

**Notes:** ___

---

<a id="last_witness"></a>
### `last_witness`
The campaign's throughline civilian — the latest ordinary survivor who can still speak a fragment's cost in plain terms. Structured field, not a single enum: record **who** they are, **what** they witnessed, **what** they fear forward, and their **status**. Carry it forward every arc. The Arc IV finale (V02 Choice D and V05 Outcome D) is only reachable if a `named` or `protected` Witness survives to the Heath. In Arc II the role can change hands: a fortress or breach survivor may inherit it, or the existing bearer may be exposed or lost in the politics.

**Status values:**

| Value | Meaning |
|-------|---------|
| `unnamed` | Role vacant; no specific person carries it |
| `named` | A specific person has spoken a fragment's cost plainly; identifiable but unprotected |
| `protected` | The party took concrete action to keep them alive, free, and able to testify; they reach the next arc |
| `exposed` | A hostile faction knows their identity and value and is recruiting, discrediting, or hunting them |
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

The counter measures how often the party used a fragment to force a crisis to resolve while leaving the deeper distortion in place — *withdrawal of grace*, not Corruption by another name. **In Arc II it advances** when the party seal or redirect the Rift Ember breach (the V05 Balance Reckoning Hook flags this; destroying the Ember or allowing failure does not advance it). **Never decrement.**

| Value | Meaning |
|-------|---------|
| `0` | No coercive fragment-answer on record; customary graces remain available |
| `1` | A fragment solution fixed an immediate problem but left a visible metaphysical distortion; a single grace thins |
| `2` | Wardens, the Hall, or spectral witnesses begin treating the party as agents of dangerous imbalance rather than reluctant stewards |
| `3` | A prior compromise returns as proof that order was preserved through coercion; aid demands explicit price |
| `4` | The endgame judgment hardens; the Hall and its living representatives no longer treat the party as untested claimants |

**Current value (carry the Arc I total forward, then advance for any Arc II use):** ___

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
- Arc II opening status:
- Arc II closing status:

**Mera Ash (carry-forward):**
- Arc II role change (if any):

**Key Arc II NPCs:**
- Clan claimant backed (name): ___
- Sarafan contact (if any): ___
- Hylden-adjacent NPC (if contact occurred): ___
- Ash-Glass observer (if present): ___

---

## Carry Forward to Arc III

- `fortress_claim` entering Arc III: ___
- `iron_echo_status` entering Arc III: ___
- `hylden_engagement` entering Arc III: ___
- `sarafan_bloc` entering Arc III: ___
- `ash_glass_reach` entering Arc III: ___
- `last_witness` entering Arc III (bearer, what they witnessed, forward fear, status): ___
- `balance_reckoning` entering Arc III (counter + which uses): ___
- Surviving allies traveling into Arc III: ___
- Active enemies pursuing into Arc III: ___
- Contradiction from the north that only the Chronoplast can explain: ___
