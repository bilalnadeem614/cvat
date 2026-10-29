# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import serializers


class LabelCountSerializer(serializers.Serializer):
    label = serializers.CharField()
    count = serializers.IntegerField()


class TaskLabelCountsSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    total = serializers.IntegerField()
    counts = LabelCountSerializer(many=True)
