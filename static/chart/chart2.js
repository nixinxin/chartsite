var myChart = echarts.init(document.getElementById('main'));
option = {
title : {
text: '手机占有率',
subtext: '数据下钻例子，虚构数据'
},
tooltip : {
trigger: 'item',
formatter: "{b}: {c}"
},
toolbox: {
show : true,
feature : {
    mark : {show: true},
    dataView : {show: true, readOnly: false},
    restore : {show: true},
    saveAsImage : {show: true}
}
},
calculable : false,
series : [
{
    name:'手机占有率',
    type:'treemap',
    itemStyle: {
        normal: {
            label: {
                show: true,
                formatter: "{b}"
            },
            borderWidth: 1,
            borderColor: '#ccc'
        },
        emphasis: {
            label: {
                show: true
            },
            color: '#cc99cc',
            borderWidth: 3,
            borderColor: '#996699'
        }
    },
    data:[
        {
            name: '三星',
            itemStyle: {
                normal: {
                    color: '#99cccc',
                }
            },
            value: 6,
            children: [
                {
                    name: 'Galaxy S4',
                    value: 2
                },
                {
                    name: 'Galaxy S5',
                    value: 3
                },
                {
                    name: 'Galaxy S6',
                    value: 3
                },
                {
                    name: 'Galaxy Tab',
                    value: 1
                }
            ]
        },
        {
            name: '小米',
            itemStyle: {
                normal: {
                    color: '#99ccff',
                }
            },
            value: 4,
            children: [
                {
                    name: '小米3',
                    value: 6
                },
                {
                    name: '小米4',
                    value: 6
                },
                {
                    name: '红米',
                    value: 4
                }
            ]
        },
        {
            name: '苹果',
            itemStyle: {
                normal: {
                    color: '#9999cc',
                }
            },
            value: 4,
            children: [
                {
                    name: 'iPhone 5s',
                    value: 6
                },
                {
                    name: 'iPhone 6',
                    value: 3
                },
                {
                    name: 'iPhone 6+',
                    value: 3
                }
            ]
        },
        {
            name: '魅族',
            itemStyle: {
                normal: {
                    color: '#ccff99',
                }
            },
            value: 1,
            children: [
                {
                    name: 'MX4',
                    itemStyle: {
                        normal: {
                            color: '#ccccff',
                        }
                    },
                    value: 6
                },
                {
                    name: 'MX3',
                    itemStyle: {
                        normal: {
                            color: '#99ccff',
                        }
                    },
                    value: 6
                },
                {
                    name: '魅蓝note',
                    itemStyle: {
                        normal: {
                            color: '#9999cc',
                        }
                    },
                    value: 4
                },
                {
                    name: 'MX4 pro',
                    itemStyle: {
                        normal: {
                            color: '#99cccc',
                        }
                    },
                    value: 3
                }
            ]
        },
        {
            name: '华为',
            itemStyle: {
                normal: {
                    color: '#ccffcc',
                }
            },
            value: 2
        },
        {
            name: '联想',
            itemStyle: {
                normal: {
                    color: '#ccccff',
                }
            },
            value: 2
        },
        {
            name: '中兴',
            itemStyle: {
                normal: {
                    color: '#ffffcc',
                }
            },
            value: 1,
            children: [
                {
                    name: 'V5',
                    value: 16
                },
                {
                    name: '努比亚',
                    value: 6
                },
                {
                    name: '功能机',
                    value: 4
                },
                {
                    name: '青漾',
                    value: 4
                },
                {
                    name: '星星',
                    value: 4
                },
                {
                    name: '儿童机',
                    value: 1
                }
            ]
        }
    ]
}
]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
