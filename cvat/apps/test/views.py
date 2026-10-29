# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from cvat.apps.engine.models import LabeledShape, Task

from .permissions import TaskLabelCountsPermission
from .serializers import TaskLabelCountsSerializer


def count_shapes_per_label(task_id):
    rows = (
        LabeledShape.objects.filter(job__segment__task_id=task_id)
        .values("label__name")
        .annotate(count=Count("id"))
        .order_by("-count", "label__name")
    )
    return [{"label": row["label__name"], "count": row["count"]} for row in rows]


@extend_schema(tags=["test"])
class TaskLabelCountsViewSet(viewsets.GenericViewSet):
    serializer_class = TaskLabelCountsSerializer
    iam_permission_class = TaskLabelCountsPermission
    iam_supports_organization_params = False
    filter_backends = []

    def get_queryset(self):
        return Task.objects.all()

    @extend_schema(
        summary="Get annotation shape counts per label for a task",
        responses=TaskLabelCountsSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        counts = count_shapes_per_label(task.pk)
        return Response(
            {"task_id": task.pk, "total": sum(c["count"] for c in counts), "counts": counts}
        )
