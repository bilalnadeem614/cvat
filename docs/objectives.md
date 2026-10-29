# Objectives

## Machine and build
- CPU: Intel Core i5-8350U @ 1.70GHz, 8 threads
- RAM: 16 GB (15 GiB usable), 8 GB swap
- OS: Fedora Linux 43 Workstation, kernel 7.2.7-100.fc43.x86_64
- Docker 29.8.1, Compose v5.5.1, storage on the internal SSD
- CVAT base commit: `5d9c21558fff8d8eb47c6f9577357b0e1ecf97c5`
- Sample data: COCO 2017 val, first 1000 images by filename, annotations from `instances_val2017.json` cut down to those images. Annotation count in the task: (fill in after import)

## MO-1: endpoint response time
| Field | Entry |
|---|---|
| What is measured | Total response time of the per-class count endpoint for the 1000-image task, from request sent to last byte received. |
| How | `curl -w "%{time_total}"` from the host against the local Docker stack, with a valid login. One warm-up request, then 5 measured requests. Raw output saved in `docs/evidence/mo1-runs.txt`. |
| Target | Median of the 5 measured runs at or below 300 ms. Min and max reported with it. |
| Conditions | Local Docker stack, the sample data above, nothing else heavy running, same machine and session for all 5 runs. |
| Not included | The warm-up request, the first request after stack start, browser render time, and tasks other than the sample task. |

### Why 300 ms
I set this before measuring anything. The database work should be one grouped query over a few thousand rows. The rest is CVAT's auth and permission checks and the proxy in front, on a laptop running the full stack. Permission checks go through a separate policy service (Open Policy Agent), which adds a network hop per request. 300 ms is not free, and I want a target I could miss. If I miss it, I will write down where the time went.
