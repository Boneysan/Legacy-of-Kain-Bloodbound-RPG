# Campaign Improvement Implementation Checklist

Use this file as the master progress tracker for campaign improvement work. Check items as they are completed, and record date plus notes for any decisions or scope changes.

## How To Use

- Mark `[x]` when complete.
- Keep each item outcome-focused (what changed at table level, not just text edits).
- Add a short completion note and date in the line below each completed item.
- If an item is intentionally deferred, mark it as deferred in Notes rather than deleting it.

## Status Key

- Priority: Critical, High, Medium, Low
- Type: Schema, Encounter, Narrative, Workflow, QA

---

## Phase 1: Critical Schema And Routing

### 1. Endgame tag normalization

- [x] **C1 (Critical, Schema):** Convert `party_operative_truth` to enum-plus-note model in Arc III tracker.
  - Targets: `Arc_III_Revelation/Arc_III_VTT-State.md`
  - Done when: tracker, vignette references, and downstream conditions all use the same canonical values.
  - Notes: Completed 2026-04-28. Added canonical enum values (`balance-through-sacrifice`, `hylden-reintegration`, `undecided`, `unresolved`) and optional `party_operative_truth_note` annotation path.

- [x] **C2 (Critical, Schema):** Convert `heart_purpose` to enum-plus-note model in Arc IV tracker.
  - Targets: `Arc_IV_Convergence/Arc_IV_VTT-State.md`
  - Done when: all endgame routing logic reads from one deterministic field set.
  - Notes: Completed 2026-04-28. Added deterministic value table including V04 intermediate (`understood`) and V05 final declaration outcomes plus optional `heart_purpose_note`.

- [x] **C3 (Critical, Schema):** Resolve Hall naming drift (`Hall of Equilibrium` vs `Hall of Coalition`) across Arc IV docs.
  - Targets: `Arc_IV_Convergence/Arc_IV_VTT-State.md`, `Arc_IV_Convergence/VTT_Vignettes/02_The-Hall-Tests-the-Coalition.md`
  - Done when: one canonical name is used everywhere.
  - Notes: Completed 2026-04-28. Updated Arc IV tracker language to `Hall of Equilibrium`; vignette already used canonical naming.

### 2. VTT schema authority

- [x] **C4 (Critical, Schema):** Update VTT integration guide to full Arc I-IV canonical tag dictionary.
  - Targets: `Campaign/VTT_INTEGRATION_GUIDE.md`
  - Done when: all active tracker tags are documented with valid values and intent.
  - Notes: Completed 2026-04-28. Expanded global state section to Arc I-IV canonical variables, normalized value sets, and documented optional note fields.

- [x] **C5 (Critical, Workflow):** Add explicit source-of-truth note that tracker/matrix docs override chronicle prose for branching state.
  - Targets: `07_Campaign-Story-Chronicle.md`, `06_GM-Story-Overview.md`
  - Done when: no implied fixed-canon path conflicts with live branch play.
  - Notes: Completed 2026-04-28. Added branch-authority notes to chronicle and GM overview, explicitly prioritizing tracker/matrix procedural state.

---

## Phase 2: Encounter Reliability And GM Speed

### 3. Fail-forward and objective clarity

- [x] **H1 (High, Encounter):** Add `Success / Partial / Failure` outcome block to Arc III encounter sheets.
  - Targets: `Encounters/Arc_III_Revelation/*.md`
  - Done when: each encounter has deterministic fail-forward outcomes with branch carry-forward notes.
  - Notes: Completed 2026-04-28. Added `## Outcome` block (Success / Partial / Failure — fail-forward) to all 6 Arc III encounter sheets. Carry-forward tag updates included for `chronal_shard_fate`, `betrayal_resolved`, `wheel_exposure`, and `party_operative_truth` where applicable.

- [x] **H2 (High, Encounter):** Add `Success / Partial / Failure` outcome block to Arc IV encounter sheets.
  - Targets: `Encounters/Arc_IV_Convergence/*.md`
  - Done when: each climax encounter has explicit continuation logic.
  - Notes: Completed 2026-04-28. Added `## Outcome` block to all 5 Arc IV encounter sheets. Carry-forward tag updates included for `coalition_shape`, `black_fulcrum_status`, and `heart_purpose` where applicable.

- [x] **H3 (High, Encounter):** Add quick `Reaction Budget` line to Arc III/IV encounter format.
  - Targets: `Arc_III_Revelation/03_Encounter-Guide.md`, `Arc_IV_Convergence/04_Encounter-Guide.md`
  - Done when: one-reaction baseline is visible in encounter prep where relevant.
  - Notes: Completed 2026-04-28. Added `Reaction Budget: 1 per PC per round.` to all 5 session entries in both encounter guides. Session 1 (Arc III) and Session 4 (Arc IV) include brief callouts for high-Reaction-demand enemies (Mirror Wraith, Dimension Lord).

- [x] **H4 (High, Encounter):** Add objective scoring micro-format for mission-style fights.
  - Targets: Arc II-IV high-complexity encounter sheets.
  - Done when: GM can track objective progress with a simple 0-3 style track.
  - Notes: Completed 2026-04-28. Added `## Objective Track` (0-3 checkbox format with score-keyed outcome references) to: Arc II `03_Breach-on-the-Northern-Ice.md` and `04_Rift-Line-Emergency.md`; Arc III `01_Chronoplast-Claim-Assault.md` and `06_Curator-Thess-Pursuit.md`; Arc IV `01_Pillar-Heath-Seal-Breaker-Push.md` and `04_Black-Fulcrum-Chamber-Crisis.md`.

### 4. Skill-check embedding

- [x] **H5 (High, QA):** Promote top-priority DR checks from recommendation backlog into scene-level docs.
  - Targets: Arc I-IV session prep and vignette files identified in `05_Skill-Check-Recommendations.md`
  - Done when: key scenes include optional checks with DR and concrete payoff/failure cost.
  - Notes: Completed 2026-04-28. Embedded optional skill check blocks (PHB skill names, explicit DRs, success/failure payoffs) into `Arc_III_Revelation/01_Session-Prep.md` (Sessions 1-4) and `Arc_IV_Convergence/01_Session-Prep.md` (Sessions 1, 2, and 3). Skills used: Observation, Lore, Insight, Concentration, Persuasion, Intimidation, Tactics, Forbidden Knowledge, Observation (DR 2-4 range).
  - Notes:

---

## Phase 3: Narrative Voice, Continuity, And Emotional Cadence

### 5. Tone and cadence pass

- [x] **H6 (High, Narrative):** Apply targeted prose pass to Arc III/IV climax vignettes to remove modern/admin diction drift.
  - Targets: `Arc_III_Revelation/VTT_Vignettes/05_Which-Future-Is-Real.md`, `Arc_IV_Convergence/VTT_Vignettes/03_What-Reth-Wants.md`
  - Done when: dramatic beats read consistently in setting tone without losing clarity.
  - Notes: Completed 2026-04-29. Replaced corporate/modern diction in Decision Pressure section of both vignettes ("foreclose ownership", "build terms", "politically costly", "distinguishable"). Rewrote 03_What-Reth-Wants.md opening narration and paragraph framing to setting register. All NPC dialogue, mechanical content, choices, and tag assignments preserved.

- [x] **H7 (High, Narrative):** Add one intentional decompression beat before final Arc IV declaration.
  - Targets: `Arc_IV_Convergence/01_Session-Prep.md`
  - Done when: players receive one consequence-focused breathing scene before final choice framing.
  - Notes: Completed 2026-04-29. Added `## Between Session 2 and Session 3 — Optional Decompression Beat` section with four suggested scene forms (Last Witness testimony, operative-truth disagreement, grief-for-past-choice, naming the dead). Includes GM guidance emphasising this is not a reopening of committed choices. Iriane Quell `chosen-under-testimony` rider honoured here.

### 6. Cross-arc payoff reinforcement

- [x] **M1 (Medium, Narrative):** Add required arc-close Last Witness handoff beat in campaign workflow text.
  - Targets: `00_Campaign-Hub.md`
  - Done when: each arc close prompts witness identity, witnessed cost, and fear-forward statement.
  - Notes: Completed 2026-04-29. Expanded Workflow step 8 in Campaign Hub with a three-question Last Witness Arc-Close Handoff: (1) Who they are — specific named person; (2) What they witnessed — specific cost, not a faction position; (3) What they fear forward — the human thread the GM carries into the next arc. All three required before moving to new arc prep.

- [x] **M2 (Medium, Narrative):** Add one secondary contradiction fallback in Arc III in case primary reveal resolves early.
  - Targets: `Arc_III_Revelation/00_Arc-Overview.md`
  - Done when: Arc III retains pressure even if the main contradiction is diffused ahead of schedule.
  - Notes: Completed 2026-04-29. Added **Secondary Contradiction Fallback** paragraph to Arc Purpose section: Chronoplast public archive contains a fabricated account of the Willendorf Pillar suppression attributed to Pale Accord archivist Veth Saun, whose presence is irreconcilably contradicted by the Chronal Shard's fragment-trace. Same structural form as northern breach record (curated cost, installed to protect ordering authority). GM advised to activate only when primary contradiction is sufficiently contained.

---

## Phase 4: Cognitive Load Reduction And Cleanup

### 7. Tracker simplification

- [x] **M3 (Medium, Workflow):** Split Arc IV coalition process and assessment into separate fields.
  - Targets: `Arc_IV_Convergence/Arc_IV_VTT-State.md`
  - Done when: process-state and assessment-state are not multiplexed in one variable.
  - Notes: Completed 2026-04-28. Renamed the process-tracking section to `coalition_process` (own anchor, description, value table, Current value, Notes) and retained `coalition_shape` as the assessment-only field written at Vignette 04 close. Each field now has its own write-timing instruction.

- [x] **M4 (Medium, Workflow):** Create one-page session run-card template from matrix state.
  - Targets: Arc II-IV matrix and session prep workflow.
  - Done when: GM can resolve branch + encounter + immediate tag updates from one page.
  - Notes: Completed 2026-04-28. Created `09_Session-Run-Card.md` in `Nosgoths-Last-Twilight/`. Template sections: Session Header (arc, level, Last Witness, Kain contract), State Going In (live tag table), Encounter Slot (TV, Objective Track, Reaction Budget), Skill Check Slots, Vignette/Scene Notes, End-of-Session Tag Updates, Carry-Forward Notes, GM Post-Session Note.

### 8. Low-priority cleanup

- [x] **L1 (Low, QA):** Archive non-canonical campaign examples to reduce search noise.
  - Targets: `Campaign/Pathfinder_Example.md`
  - Done when: active prep paths exclude legacy reference material.
  - Notes: Completed 2026-04-28. Prepended a prominent ARCHIVED notice to `Pathfinder_Example.md` marking it as a non-canonical Pathfinder excerpt, excluded from active prep searches and indexing, with a pointer to `Nosgoths-Last-Twilight/`.

---

## Completion Log

## Phase 4 Completion

- Date: 2026-04-28
- Completed Item IDs: M3, M4, L1
- Summary of Changes: `coalition_shape` in Arc IV tracker split into `coalition_process` (V01–V03 play record) and `coalition_shape` (V04 close assessment); one-page session run-card template created at `09_Session-Run-Card.md`; `Pathfinder_Example.md` marked with ARCHIVED notice.
- Any Follow-up Needed: All planned improvement phases complete. No open items remain on this checklist.

- Date: 2026-04-29
- Completed Item IDs: H6, H7, M1, M2
- Summary of Changes: Prose tone pass on two Arc III/IV climax vignettes; decompression beat inserted between Arc IV Sessions 2 and 3; Last Witness handoff prompt formalized in Campaign Hub workflow; secondary contradiction fallback (Veth Saun, Willendorf suppression) added to Arc III Overview.
- Any Follow-up Needed: Phase 4 begins with M3 (Arc IV coalition state field split), then M4 (session run-card template), then L1 (Pathfinder_Example.md archival).


