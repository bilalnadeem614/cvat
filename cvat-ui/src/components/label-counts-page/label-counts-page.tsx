// Copyright (C) CVAT.ai Corporation
//
// SPDX-License-Identifier: MIT

import React, { useCallback, useEffect, useState } from 'react';
import { Row, Col } from 'antd/lib/grid';
import Button from 'antd/lib/button';
import Empty from 'antd/lib/empty';
import Result from 'antd/lib/result';
import Title from 'antd/lib/typography/Title';
import {
    Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

import { getCore } from 'cvat-core-wrapper';
import CVATLoadingSpinner from 'components/common/loading-spinner';
import GoBackButton from 'components/common/go-back-button';
import { useInstanceId } from 'utils/hooks';
import { InstanceType } from 'reducers';

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip);

const core = getCore();

interface LabelCounts {
    task_id: number;
    total: number;
    counts: { label: string; count: number }[];
}

function LabelCountsPage(): JSX.Element {
    const taskId = useInstanceId(InstanceType.TASK);
    const [data, setData] = useState<LabelCounts | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [fetching, setFetching] = useState(true);

    const fetchCounts = useCallback(async () => {
        setFetching(true);
        setError(null);
        try {
            const response = await core.server.request(
                `${core.config.backendAPI}/label-counts/${taskId}`, { method: 'GET' },
            ) as { data: LabelCounts };
            setData(response.data);
        } catch (err: unknown) {
            setError((err as Error).message);
        } finally {
            setFetching(false);
        }
    }, [taskId]);

    useEffect(() => {
        fetchCounts();
    }, [fetchCounts]);

    let content: JSX.Element;
    if (fetching) {
        content = <CVATLoadingSpinner />;
    } else if (error) {
        content = (
            <Result
                status='error'
                title='Could not load label counts'
                subTitle={error}
                extra={<Button type='primary' onClick={fetchCounts}>Retry</Button>}
            />
        );
    } else if (!data?.total || !data.counts.length) {
        content = <Empty description='This task has no annotations' />;
    } else {
        content = (
            <div style={{ height: 400 }}>
                <Bar
                    options={{ responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }}
                    data={{
                        labels: data.counts.map((item) => item.label),
                        datasets: [{ label: 'Shapes', data: data.counts.map((item) => item.count) }],
                    }}
                />
            </div>
        );
    }

    return (
        <div className='cvat-label-counts-page'>
            <Row justify='center'>
                <Col span={22}>
                    <GoBackButton />
                    <Title level={4}>{`Label counts for task #${taskId}`}</Title>
                    {content}
                </Col>
            </Row>
        </div>
    );
}

export default React.memo(LabelCountsPage);
