var options = {
            annotations: {
                yaxis: [{
                    y: 8200,
                    borderColor: '#00E396',
                    label: {
                        borderColor: '#00E396',
                        style: {
                            color: '#fff',
                            background: '#00E396',
                        },
                        text: 'Support',
                    }
                }],
                xaxis: [{
                    x: new Date('23 Nov 2017').getTime(),
                    strokeDashArray: 0,
                    borderColor: '#775DD0',
                    label: {
                        borderColor: '#775DD0',
                        style: {
                            color: '#fff',
                            background: '#775DD0',
                        },
                        text: 'Anno Test',
                    }
                }, {
                    x: new Date('03 Dec 2017').getTime(),
                    borderColor: '#FEB019',
                    label: {
                        borderColor: '#FEB019',
                        style: {
                            color: '#fff',
                            background: '#FEB019',
                        },
                        orientation: 'horizontal',
                        text: 'New Beginning',
                    }
                }],
                points: [{
                    x: new Date('27 Nov 2017').getTime(),
                    y: 8506.9,
                    marker: {
                        size: 8,
                        fillColor: '#fff',
                        strokeColor: 'red',
                        radius: 2
                    },
                    label: {
                        borderColor: '#FF4560',
                        offsetY: 0,
                        style: {
                            color: '#fff',
                            background: '#FF4560',
                        },
                        
                        text: 'Point Annotation',
                    } 
                }]
            },
            chart: {
                height: 350,
                type: 'line',
                id: 'areachart-2'
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'straight'
            },
            grid: {
                padding: {
                    right: 30,
                    left: 20
                }
            },
            series: [{
                data: series.monthDataSeries1.prices
            }],
            title: {
                text: 'Line with Annotations',
                align: 'left'
            },
            labels: series.monthDataSeries1.dates,
            xaxis: {
                type: 'datetime',
            },
        }

        var chart = new ApexCharts(
            document.querySelector("#chart"),
            options
        );

        chart.render();
