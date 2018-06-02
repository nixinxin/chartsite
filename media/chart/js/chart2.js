var myChart = echarts.init(document.getElementById('main'));
option = {
    legend: {
        show: true,
        zlevel: 0,
        orient: 'horizontal', // 'vertical'
        x: 'center', // 'center' | 'left' | {number},
        y: 'top', // 'center' | 'bottom' | {number}
        backgroundColor: '#eee',
        borderColor: 'rgba(178,34,34,0.8)',
        padding: 10,    // [5, 10, 15, 20]
        itemGap: 10,
        textStyle: {color: 'red'},
        data: [
            {
                name:'农业统计年鉴',
                icon : 'image://../asset/ico/favicon.png',
                textStyle:{fontWeight:'bold', color:'green'}
            },
            '农业有害生物',
            '作物遗传资源',
            '农业科技资源,',
            '作物品种品质,',
            '农产品资源,',
        ]
    },
    title : {
    text: '数据资源分类信息',
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
        name:'数据分类',
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
                name: '农业统计年鉴',
                itemStyle: {
                    normal: {
                        color: '#99cccc',
                    }
                },
                value: 25588,
                children: [
                    {
                        name: '年鉴CAJ文件',
                        value: 8858
                    },
                    {
                        name: '年鉴PDF文件',
                        value: 8858
                    },
                    {
                        name: '年鉴excel文件',
                        value: 7838
                    },
                    {
                        name: '图片文件',
                        value: 33
                    }
                ]
            },
            {
                name: '农业有害生物',
                itemStyle: {
                    normal: {
                        color: '#99ccff',
                    }
                },
                value: 5144,
                children: [
                    {
                        name: '中国粮食作物细菌病害数据库',
                        value: 33
                    },
                    {
                        name: '中国农业害鼠数据库',
                        value: 35
                    },
                    {
                        name: '中国粮食作物病毒病害数据库',
                        value: 37
                    },
                    {
                        name: '中国棉花害虫数据库',
                        value: 50
                    },
                    {
                        name: '中国叶菜类蔬菜害虫数据库',
                        value: 50
                    },
                    {
                        name: '外来有害微生物数据库',
                        value: 51
                    },
                    {
                        name: '中国水稻害虫数据库',
                        value: 56
                    },
                    {
                        name: '外来有害昆虫数据库',
                        value: 63
                    },
                    {
                        name: '中国果菜类蔬菜害虫数据库',
                        value: 66
                    },
                    {
                        name: '中国苹果桃梨害虫数据库',
                        value: 66
                    },
                    {
                        name: '中国经济作物细菌病害数据库',
                        value: 81
                    },
                    {
                        name: '中国柑桔害虫数据库',
                        value: 83
                    },
                    {
                        name: '中国经济作物病毒病害数据库',
                        value: 90
                    },
                    {
                        name: '中国旱粮作物害虫数据库',
                        value:145
                    },
                    {
                        name: '中国粮食作物真菌病害数据库',
                        value: 186
                    },
                     {
                        name: '外来有害植物数据库',
                        value: 212
                    },
                     {
                        name: '中国经济作物真菌病害数据库',
                        value: 526
                    },
                     {
                        name: '中国农业有害生物图片数据库',
                        value: 3314
                    },


                ]
            },
            {
                name: '作物遗传资源',
                itemStyle: {
                    normal: {
                        color: '#9999cc',
                    }
                },
                value: 37678,
                children: [
                    {
                        name: '作物优异资源综合评价数据库',
                        value: 1042
                    },
                    {
                        name: '作物遗传资源特性评价鉴定数据库',
                        value: 15000
                    },
                    {
                        name: '大麦作物优异资源综合评价数据库',
                        value: 188
                    },
                    {
                        name: '小麦系谱数据库',
                        value: 3554
                    },
                    {
                        name: '小麦育成品种及其系谱数据库',
                        value: 12943
                    },
                    {
                        name: '水稻育成品种及其系谱数据库',
                        value: 4097
                    },
                    {
                        name: '玉米作物优异资源综合评价数据库',
                        value: 854
                    }
                ]
            },
            {
                name: '农业科技资源',
                itemStyle: {
                    normal: {
                        color: '#68838B',
                    }
                },
                value: 132536,
                children: [
                    {
                        name: '有机农业数据库',
                        value: 7859
                    },
                    {
                        name: '农业古籍数据库',
                        value: 279
                    },
                    {
                        name: '农业科技人才数据库',
                        value: 2877
                    },
                    {
                        name: '农业科技机构数据库',
                        value: 477
                    },
                    {
                        name: '农业获奖科技成果数据库',
                        value: 50000
                    },
                    {
                        name: '国内农业科研项目数据库',
                        value: 8355
                    },
                    {
                        name: '国际农业科研项目数据库',
                        value: 4511
                    },
                    {
                        name: '中文农业科技文摘数据库',
                        value: 11253
                    },
                    {
                        name: '外文农业科技文摘数据库',
                        value: 40373
                    },
                    {
                        name: '农业科技政策法规数据库',
                        value: 3548
                    },
                    {
                        name: '农业标准和操作规范数据库',
                        value: 1931
                    },
                    {
                        name: '畜禽常见疾病及防治方法数据库',
                        value: 1073
                    }
                ]
            },
            {
                name: '作物品种品质',
                itemStyle: {
                    normal: {
                        color: '#8B864E',
                    }
                },
                value: 37554,
                children: [
                    {
                        name: '作物优异种质数据库',
                        value: 252
                    },
                    {
                        name: '作物物种分布数据库',
                        value: 499
                    },
                    {
                        name: '国外引进作物资源数据库',
                        value: 31516
                    },
                    {
                        name: '小麦作物核心种质数据库',
                        value: 2390
                    },
                    {
                        name: '水稻作物核心种质数据库',
                        value: 2598
                    },
                    {
                        name: '玉米作物核心种质数据库',
                        value: 97
                    },
                    {
                        name: '玉米新品种保护数据库',
                        value: 202
                    }
                ]
            },
            {
                name: '农产品资源',
                itemStyle: {
                    normal: {
                        color: '#D2B48C',
                    }
                },
                value: 13639,
                children: [
                    {
                        name: '中国特色农产品',

                        value: 2424
                    },
                    {
                        name: '中国重要农业文化遗产',

                        value: 71
                    },
                    {
                        name: '农产品价格行情数据库(千)',

                        value: 8500
                    },
                    {
                        name: '农作物名优特新品种数据库',

                        value: 2644
                    },
                ]
            },
        ]
    }
    ]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
