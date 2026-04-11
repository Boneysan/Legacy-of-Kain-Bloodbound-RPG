# Arc I Detailed Vignette Consequence Matrix

Use this when you want exact downstream NPC, faction-pressure, and encounter routing without flipping between the vignette files, the Arc I choice guides, and Arc_I_VTT-State.md.

<a id="v01-caravan-argument"></a>
## 01 — The Caravan Argument

| Choice | NPC shift | State and clock guidance | Encounter handoff |
|--------|-----------|--------------------------|-------------------|
| A — Press On to Avernus | Mera approves the call; Serit stays useful but guarded and does not volunteer more than necessary | Set `serit_trust: guarded`; no immediate `sarafan_attention` increase; the cult has less time to stage and the party has less rest | Run Encounters/Arc_I_Awakening/01_Cathedral-Road-Ambush.md without Serit's warning beat; move into the refuge exhausted and socially uncovered |
| B — Camp at the Milestone Shrines | Serit drops to low cooperation and treats the party as people who chose visibility over urgency | Set `serit_trust: low` and `sarafan_attention: 1`; shrine witnesses seed later Sarafan pressure and give the cult time to place a watcher ahead | Keep Encounters/Arc_I_Awakening/01_Cathedral-Road-Ambush.md, but add the watcher and plan for Encounters/Arc_I_Awakening/03_Purge-at-First-Light.md if the surface story turns public |
| C — Inspect the Reliquary | Serit physically blocks access; she now knows someone in the party felt the Knot answer | Set `serit_trust: low` and `reliquary_status: examined`; cult interest shifts from cargo-only recovery to identifying the sensitive PC | In the next cult scene, make the chosen target the sensitive PC or weakest observer instead of the strongest carrier |
| D — Question Serit Directly | Serit gives the most honest answer she will give this early and is committed to the party knowing the relic is active | Set `serit_trust: earned`; no direct Sarafan bump, but the party now has a true reason to treat the cargo as urgent | Give Serit her warning beat before Encounters/Arc_I_Awakening/01_Cathedral-Road-Ambush.md and let her body-block one early shadow move |

<a id="v02-false-refuge"></a>
## 02 — The False Refuge

| Choice | NPC shift | State and clock guidance | Encounter handoff |
|--------|-----------|--------------------------|-------------------|
| A — Accept Sanctuary Fully | Halden gains control of space, beds, and possibly cargo position; Mera stays awake and suspicious but does not stop the choice | Set `reliquary_status: sealed` and `public_story: secrecy`; the cult cell gets position while Sarafan pressure stays indirect | Run the Session 2 refuge investigation through Encounters/Arc_I_Awakening/02_The-Healers-Smile.md with low collateral and cult initiative inside the shelter |
| B — Accept but Post Guards | Halden adapts politely; one party member becomes the isolated first-watch problem | Set `public_story: secrecy` and `sarafan_attention: 0`; the cult loses easy cargo access and must work socially or pick off the watcher | Keep Encounters/Arc_I_Awakening/02_The-Healers-Smile.md, but frame it as layered social pressure and outside isolation rather than quiet theft |
| C — Challenge Halden Publicly | Serit becomes guarded because the party made noise before they had proof; the civilians are now frightened witnesses | Set `public_story: panic` and `serit_trust: guarded`; Sarafan Purge Clock is the most likely to advance once anyone survives to talk | Run Encounters/Arc_I_Awakening/02_The-Healers-Smile.md or an immediate refuge clash with fleeing civilians; keep Encounters/Arc_I_Awakening/03_Purge-at-First-Light.md ready as the next public surface scene |
| D — Split the Party | Serit reads the split as risky and avoidable; the outside team gets the best physical clue load | Set `reliquary_status: examined` and `sarafan_attention: 1`; the cult now knows who is observant and the Sarafan have another trail point | Start the next scene with separated information, the hidden side entrance, and the group reuniting under pressure before Encounters/Arc_I_Awakening/02_The-Healers-Smile.md |

<a id="v03-what-serit-knows"></a>
## 03 — What Serit Knows

| Choice | NPC shift | State and clock guidance | Encounter handoff |
|--------|-----------|--------------------------|-------------------|
| A — Demand Full Disclosure | Serit becomes a limited but genuine ally because she names both the truth and the boundary around it | Set `serit_trust: earned` and `reliquary_status: examined`; Accord cooperation is strongest from here | The Session 2 investigation starts with the relic named and the cult objective legible; Session 3 descent gets warning and better site context |
| B — Accept Partial Truth | Serit gives useful field intelligence instead of institutional confession | Set `serit_trust: guarded` and `reliquary_status: examined`; the party gets the practical answer but not volunteered follow-up | Keep the Session 2-3 flow intact, but require the party to ask the right questions to unlock more help |
| C — Threaten or Pressure Her | Serit counter-leverages the party and starts managing them from a greater distance | Set `serit_trust: low` and `reliquary_status: sealed`; Accord reports begin bypassing the party | The Session 2 investigation and Session 3 descent proceed with weaker lore framing and a stronger chance that Serit acts offscreen rather than alongside the party |
| D — Reveal the Party Already Knows More | Serit opens her notes and starts treating the party as investigative partners, while also flagging a bloodline carrier to the Accord | Set `serit_trust: earned` and `reliquary_status: examined`; this is the strongest Arc I-to-II Accord relationship result | Start the next investigation scene with Serit approaching the party first and offering controlled site research rather than waiting to be pressed |

<a id="v04-first-blood-memory"></a>
## 04 — The First Blood-Memory

| Choice | NPC shift | State and clock guidance | Encounter handoff |
|--------|-----------|--------------------------|-------------------|
| A — Resist It and Say Nothing | No one else knows yet; the PC alone carries the recognition burden | Set `reliquary_status: sealed`; the next voluntary Blood-Well contact is harder and the pulse will recur under worse stress | Bring the next pulse back during violence or the first chamber contact rather than in safety |
| B — Report It to Serit Vale | Serit starts treating the PC as a likely bloodline carrier and documents them accordingly | Set `serit_trust: earned` and `reliquary_status: examined`; Accord attention to the PC begins now | Serit's Session 2 information offer becomes proactive, and Vignette 03 Choice D no longer needs to be forced manually |
| C — Follow the Vision's Pull | The PC gets the strongest personal relic seed; Serit may notice and quietly record the reaction if she is present | Set `reliquary_status: examined`; no immediate public fallout, but the marked image becomes binding prep for later | Reuse the chain, mark, or ancestral symbol in Encounters/Arc_I_Awakening/05_Blood-Well-Chamber-Defense.md as the clearest direct-contact hook |
| D — Share the Experience With Another PC | Internal trust changes immediately; the fragment now treats the two PCs as linked witnesses | Set `reliquary_status: examined`; the next pulse hits both and makes secrecy harder | Fire the next pulse during an NPC-heavy investigation scene so discretion, trust, and cult targeting all tighten at once |

<a id="v05-who-carries-the-knot"></a>
## 05 — Who Carries the Knot

| Choice | NPC shift | State and clock guidance | Encounter handoff |
|--------|-----------|--------------------------|-------------------|
| A — The Party Keeps the Sanguine Knot | Serit becomes ally-plus-watcher; Mera and the Guilds shift from support to monitoring | Set `reliquary_status: sealed`, `guild_pressure: high`, and usually `public_story: secrecy`; bearer Corruption pressure starts immediately after the exit | Run Encounters/Arc_I_Awakening/06_Sanguine-Extraction-Standoff.md as custody defense, then Encounters/Arc_I_Awakening/07_Avernus-Exit-Pursuit.md with the party as obvious carriers |
| B — Entrust It to Serit and the Accord | Serit becomes the accountable custodian and strongest Accord contact; Mera cools toward a purely operational relationship | Set `reliquary_status: sealed`, `serit_trust: earned`, and `guild_pressure: low`; the party lose bearer strain but gain Accord vulnerability | Run Encounters/Arc_I_Awakening/06_Sanguine-Extraction-Standoff.md around Accord custody and extraction, then let Arc II open with researchers or transport routes under threat |
| C — Conceal It or Use a Neutral Holder | Serit goes guarded and independent; Mera supports routing and concealment rather than ownership | Set `reliquary_status: sealed`, `serit_trust: guarded`, `public_story: controlled_lie`, and `sarafan_attention: 0`; secrecy starts cracking immediately even if it holds for the night | Play Encounters/Arc_I_Awakening/06_Sanguine-Extraction-Standoff.md as a concealment retreat; only trigger Encounters/Arc_I_Awakening/07_Avernus-Exit-Pursuit.md if the hiding place is seen, guessed, or betrayed |
| D — Force a Faction Vote | Every surviving faction now knows the room's real incompatibilities; Serit usually wins the sharpest argument, but the party lose deniability | Set `reliquary_status: examined`, keep `serit_trust` at `guarded` or `earned`, and move `public_story` toward `open_truth`; Sarafan investigators should start Arc II informed if witnesses live | Frame Encounters/Arc_I_Awakening/06_Sanguine-Extraction-Standoff.md as a public claim scene and be ready to use Encounters/Arc_I_Awakening/03_Purge-at-First-Light.md or Encounters/Arc_I_Awakening/07_Avernus-Exit-Pursuit.md depending on how openly the chamber story spreads |

## Arc I Closing Check

- If `public_story` is `panic` or `open_truth`, check Purge-at-First-Light before you assume the party gets a quiet road-out scene.
- If `serit_trust` is `earned`, spend it on an actual warning, access route, or volunteered Accord intelligence in the next scene. Do not leave it as a passive note.
- If `reliquary_status` is `examined`, the cult should stop acting as if the fragment is inert and start acting as if specific blood is being recognized.
- Finalize Arc_I_VTT-State.md before Arc II starts. The control problem in Arc I is not missing consequences. It is forgetting to write them down. 