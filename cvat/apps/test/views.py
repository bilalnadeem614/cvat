# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from cvat.apps.engine.models import LabeledShape, Task

from .permissions import TaskLabelCountsPermission
from .serializers import TaskLabelCountsSerializer


def count_shapes_per_label(task_id, group_by_type=False):
    fields = ["label__name", "type"] if group_by_type else ["label__name"]
    rows = (
        LabeledShape.objects.filter(job__segment__task_id=task_id)
        .values(*fields)
        .annotate(count=Count("id"))
        .order_by("-count", *fields)
    )
    return [
        {
            "label": row["label__name"],
            **({"type": row["type"]} if group_by_type else {}),
            "count": row["count"],
        }
        for row in rows
    ]


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
        parameters=[
            OpenApiParameter(
                "group_by",
                description="Also split counts by shape type",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                enum=["type"],
                required=False,
            )
        ],
        responses=TaskLabelCountsSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        group_by = request.query_params.get("group_by")
        if group_by not in (None, "type"):
            raise ValidationError("group_by must be 'type'")
        counts = count_shapes_per_label(task.pk, group_by == "type")
        return Response(
            {"task_id": task.pk, "total": sum(c["count"] for c in counts), "counts": counts}
        )
