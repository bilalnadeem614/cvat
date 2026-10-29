# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import serializers

from cvat.apps.engine.models import ShapeType


class LabelCountSerializer(serializers.Serializer):
    label = serializers.CharField()
    type = serializers.ChoiceField(choices=ShapeType.choices(), required=False)
    count = serializers.IntegerField()


class TaskLabelCountsSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    total = serializers.IntegerField()
    counts = LabelCountSerializer(many=True)
