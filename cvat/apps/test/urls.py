# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from rest_framework import routers

from .views import TaskLabelCountsViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("label-counts", TaskLabelCountsViewSet, basename="label_counts")

urlpatterns = router.urls
