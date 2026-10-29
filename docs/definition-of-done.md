# Definition of Done

Written before the work. A box is ticked only with a number, output or link beside it.

- [ ] Endpoint returns correct counts for a known task. Evidence: counts computed independently from the COCO JSON for the same 1000 images, compared side by side. Differences explained (CVAT stores one polygon row per polygon part, so counts differ from COCO objects).
- [ ] Endpoint reads from the database, not from files or caches. Evidence: file and line of the query.
- [ ] Page calls the endpoint and renders a bar chart. Evidence: screenshot.
- [ ] Empty case handled. Evidence: screenshot of a task with no annotations.
- [ ] Failed-request case handled. Evidence: screenshot with the endpoint failing.
- [ ] Request with no login is refused. Evidence: status code from curl.
- [ ] User without access to the task is refused. Evidence: status code from curl, second user.
- [ ] MO-1 measured, 5 runs, raw output saved. Evidence: `docs/evidence/mo1-runs.txt`.
- [ ] MO-1 target met, or missed with the reason written down. Evidence: median and spread.
- [ ] One filter or grouping beyond the plain count, with the reason I chose it.
- [ ] Commits are small, with messages that say what and why. Evidence: `git log --oneline`.
- [ ] No dead code, commented-out blocks or stray files. Evidence: `git status` and a diff read.
- [ ] Loom recorded, 5 minutes or less, with K1 to K4 answered against my own code.
- [ ] Pull request opened from `dev-test01` into `develop` on my own fork, not the real CVAT repo.
- [ ] Everything I did not finish is listed below, with the reason.

## Not finished
Items 8-10 are skipped by decision (see the Plan). (Rest filled in at the end.)
