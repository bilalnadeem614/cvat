# Plan: Annotation Analytics for CVAT

Branch: `dev-test01`. CVAT base commit: `5d9c21558fff8d8eb47c6f9577357b0e1ecf97c5` (shallow clone of my fork, `develop`).
Clock started 9:20 PM PKT, deadline 5:20 AM PKT. About 1h40m went on environment setup before the first commit.

## Revision note (written at 12:55 AM PKT)
My first versions of the three docs were committed at about 11:03 PM. At about 12:35 AM the external drive holding my repo (a disk image on an NTFS USB drive) started returning read errors, and the repo with its commits became unreadable. I lost the commits, not the work: the docs below are recreated from the same text, with this note and the time budget updated. They contain no code. I also lost the CVAT task, which I recreate from the same COCO data, and one hour of the clock. The repo now lives on the internal SSD.

## What I will build
An authenticated per-task endpoint that returns annotation counts per label, read from the database, and a page in the CVAT UI that draws those counts as a bar chart.

## Order and time budget (remaining about 4h25m at 12:55 AM)
| Step | Work | Budget |
|---|---|---|
| 0 | Recreate docs, restart the stack, recreate the task and import the 1000-image subset | 25 min |
| 1 | Item 1: Django app `test`, task-scoped endpoint, after reading how CVAT reaches labels from a task | 45 min |
| 2 | Items 2-4: page in `cvat-ui`, bar chart, empty and error states | 70 min |
| 3 | Item 5: reuse CVAT's permission system, show a 401 and a 403 | 25 min |
| 4 | Item 6: one speed target, 5 runs, raw output saved | 25 min |
| 5 | Item 7: one extra grouping (shape type), only if items 1-6 are done | 15 min |
| 6 | Definition of Done evidence, Loom, pull request, email | 40 min |
| - | Buffer | 10 min |

## Decided to skip
Items 8-10 (WebSocket updates, reconnect, decision record). I will say so in the Definition of Done.

## Questions I answer by reading code
- Which models hold a shape and its label, and how a task reaches them (read already: `Annotation` has `job` and `label` foreign keys, `Label.name` is the class name, and a shape reaches its task through `job.segment.task`).
- How tracks are counted. Tracks and tags are separate tables and are empty in my data, so item 1 counts shapes only.
- Which permission class CVAT's own task endpoints use. Access goes through Open Policy Agent, and a view must define `iam_permission_class`.
- Whether `cvat-ui` can be built and run on this machine in the time I have.

## Risks
- Tight RAM (16 GB) and 12 GB of free SSD space for the stack and frontend dependencies.
- Building `cvat-ui` from source on this CPU, and the repo wants yarn 4 while the machine has yarn 1. If the frontend cannot be built in the budget, I will say so rather than fake it.
