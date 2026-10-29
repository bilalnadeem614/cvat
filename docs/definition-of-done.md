# Definition of Done

Written before the work, ticked at the end. A box is ticked only with a number, output or link beside it.

- [x] Endpoint returns correct counts for a known task. Evidence: `docs/evidence/per-class-check.txt`: 79 of 79 classes match the COCO subset file, 0 differences, both totals 8109. Why the total is not the COCO annotation count (7204): `docs/evidence/count-reconciliation.md` (CVAT stores one polygon row per polygon part).
- [x] Endpoint reads from the database. Evidence: `cvat/apps/test/views.py` lines 20-25, one grouped query on `LabeledShape`.
- [x] Page renders a bar chart from the endpoint. Evidence: `docs/evidence/chart.png`, component `cvat-ui/src/components/label-counts-page/label-counts-page.tsx`.
- [x] Empty case handled. Evidence: `docs/evidence/empty-state.png` (task 2, no annotations).
- [x] Failed-request case handled. Evidence: `docs/evidence/error-state.png`, with a Retry button. Triggered with a task id that does not exist (404). I did not simulate a network outage or a 500.
- [x] A request with no login is refused. Evidence: 401 in `docs/evidence/auth-checks.txt`.
- [x] A user without access to the task is refused. Evidence: 403 for a second user in `docs/evidence/auth-checks.txt`, and again with `group_by=type` in `docs/evidence/group-by-checks.txt`.
- [x] MO-1 measured, 5 runs, raw output saved: `docs/evidence/mo1-runs.txt`.
- [x] MO-1 target met: median 45 ms (min 44, max 48) against a target of 300 ms. The target was too loose, see `docs/objectives.md`.
- [x] One grouping beyond the plain count: `?group_by=type` splits counts by shape type. Why: it makes the polygon/mask mix visible (8022 polygon rows, 87 mask rows), which is where the gap to COCO counts comes from. Evidence: `docs/evidence/group-by-checks.txt`. The page does not use it.
- [x] Commits are small, with messages that say what and why. Evidence: `git log --oneline 5d9c21558fff8d8eb47c6f9577357b0e1ecf97c5..HEAD`, plan first, then objectives, definition of done, app skeleton, permission class, endpoint, page, evidence.
- [ ] No dead code, commented-out blocks or stray files. Pending: `git status` and a diff read.
- [ ] Loom recorded, 5 minutes or less, with K1 to K4 answered against my own code.
- [ ] Pull request opened from `dev-test01` into `develop` on my own fork, not the real CVAT repo.
- [x] Everything I did not finish is listed below.

## Not finished
- Items 8 and 9 (live updates over WebSocket, reconnect) and item 10 (decision record): skipped by decision, as the Plan says. I did not check whether CVAT's server supports WebSocket, so I cannot say what they would have cost.
- The page has no control for `group_by`. Item 7 exists in the API only.
- The page was run on the webpack dev server (`localhost:3000`, proxying `/api` to the CVAT stack on 8080). I did not rebuild the production UI image, so the page is not served at `localhost:8080`.
- Only shapes are counted. Tracks and tags are separate tables and are empty in my data.
- MO-1 was measured on one task (8109 shapes), with token authentication and the dev server stopped.
- My first commits were lost when the external drive failed and were recreated. See the note in `docs/plan.md`.
