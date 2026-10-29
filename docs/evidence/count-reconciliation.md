# Count reconciliation: COCO file vs CVAT database

Task 1, 1000 COCO val2017 images. Generated Fri Oct 30 02:33:31 AM PKT 2026 from the live database and the COCO subset file.

## COCO subset file
- annotations: 7204
- crowd (iscrowd=1): 87
- non-crowd: 7117
- polygon parts in non-crowd annotations: 8022

## CVAT database, task 1 (shape type | rows)
- polygon | 8022
- mask | 87
- tracks: 0, tags: 0

## Reading
8022 polygon rows + 87 mask rows = 8109 rows in `engine_labeledshape`. CVAT stores one polygon row per COCO polygon part and one mask row per crowd annotation, so the endpoint counts stored shapes, not COCO objects. Example: `person` is 2251 in COCO and 2499 in the endpoint.
