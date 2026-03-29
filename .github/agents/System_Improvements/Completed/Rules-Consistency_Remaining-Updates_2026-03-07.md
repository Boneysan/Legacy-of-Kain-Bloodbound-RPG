# Rules Consistency Remaining Updates

Date: 2026-03-07

Scope reviewed:
- `GM_Guide/`
- `Monster_Manual/`
- `player's_handbook/`

This pass focused on cross-document rules consistency, terminology consistency, and whether the current text matches the repository canon notes.

## Already Aligned

These areas now read consistently enough that they do **not** need priority fixes in this pass:

- Corrupted Perks are generally described as replacing Universal Perk choices rather than granting free bonus progression.
- `Trade Value` / market-style loot language is now mostly framed as barter weight, faction leverage, or scarcity shorthand rather than a literal coin economy.
- GM-facing guidance generally prefers Advantage / Disadvantage for situational adjudication, with numeric DV modifiers mainly reserved for cover and explicit abilities.
- GM encounter guidance still respects the `1 Reaction per round` baseline unless a stat block explicitly overrides it.

## Status After Fix Passes

The major contradictions identified in this review have now been resolved in the source documents.

### Completed

1. **Printed monster DV above 6**
  - Fixed in the flagged Ancient and Legendary entries.
  - Follow-up pass also removed the remaining over-cap DV lines from Chapter 7.

2. **Parallel defense wording in monster/NPC entries**
  - Flagged `Defense roll`, `vs Dodge`, and similar attack-resolution drift was rewritten to use DV, DR, or explicit reaction wording.
  - Counter-magic wording in affected entries was anchored to DR/reaction language rather than freeform active-pool contests.
  - Follow-up monster pass also cleaned the remaining old `Dodge` / `Parry` reaction labels and `vs Parry` attack headers in active stat blocks.

3. **Non-PHB monster skill lists in flagged chapters**
  - Normalized the targeted Chapters 8 and 9 entries.
  - Follow-up pass normalized the remaining high-signal stat blocks in Chapters 2, 4, 5, 6, and 7 where legacy skill lines were still appearing in active mechanics.

4. **Player-facing PHB `Defense` wording**
  - Updated the flagged class and perk entries to explicit DV wording.

5. **Reaction-cap implication drift in PHB combat**
  - Rewrote the combat chapter to preserve the canonical baseline: 1 Reaction per round unless a feature explicitly grants another.

6. **Situational modifiers alternating between Advantage/Disadvantage and flat dice bonuses**
  - Cleaned the representative PHB and mortal-enemy files so binary situational edge now prefers Advantage / Disadvantage wording.
  - Left explicit scaling, stacking, and progression bonuses as flat dice where the number still carries mechanical meaning.
  - Follow-up targeted sweep extended the same wording cleanup into additional authored handbook, monster, and GM-facing NPC files.

7. **Attribute annotations and mixed schema in normalized monster chapters**
  - Cleaned the targeted normalized entries so the most visible stat blocks no longer keep parenthetical attribute reminders as a parallel schema.

8. **Older PHB action/reaction summary vocabulary**
  - Updated the summary chapters so they now point back to the combat chapter as shorthand summaries instead of re-teaching outdated action names as canonical rules text.

9. **Perks mojibake and legacy labels**
  - Fixed the flagged encoding noise and the related damage / DV terminology drift in the perks chapter.

10. **`Terraign` filename typo**
  - Renamed the chapter file to `11_Realms-Terrain-Arcane-Power.md` and updated the tracked references.

## Notes

- Follow-up monster-manual sweep confirmed that remaining references to concepts such as blood magic, tracking, or melee range are now predominantly lore or tactical prose rather than active parallel rules vocabulary.
- Follow-up monster-manual sweep also caught the remaining off-list check phrasing in active mechanics, replacing terms such as `Investigation` and `Pillar Lore` with PHB skill language where they still appeared.
