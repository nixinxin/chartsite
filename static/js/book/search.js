$(document).ready(function () {
    // --自定义校验规则
    $.validator.addMethod("searchtext", function (value, element) {
        var txt = /<|>|\%|\+|"|\\|&/g;
        return this.optional(element) || (!txt.test(value));
    }, "非法字符");
    $.validator.addMethod("invalidnum", function (value, element) {
        var txt = /^(19|20)$/;
        return this.optional(element) || (!txt.test(value));
    }, "非法字符");
    $.validator.addMethod("lessTo", function (value, element) {
        var date = new Date();
        var res = false;
        var _v = parseInt(value == '不限' ? date.getFullYear() : $(element).val());
        var _to = parseInt($('#StartYear').val() == '不限' ? '1949' : $('#StartYear').val());
        if (_v >= _to) {
            res = true;
        }
        return this.optional(element) || res;
    }, "结束时间不得小于开始时间");
    //数字验证比较大小
    $.validator.addMethod("numLessTo", function (value, element) {
        var res = false;
        var _v = parseInt(value);
        var _to = parseInt($('#start').val());
        if (_v >= _to) {
            res = true;
        }
        return this.optional(element) || res;
    }, "结束位置不得小于开始位置");

    //数字验证-差值
    $.validator.addMethod("range", function (value, element, params) {
        var res = false;
        var _v = parseInt(params[0]);
        var _fro = parseInt($('#start').val() == '' ? 0 : $('#start').val());
        var _to = parseInt($('#end').val() == '' ? 0 : $('#end').val());
        if (_to - _fro < _v) {
            res = true;
        }

        return this.optional(element) || res;
    }, "下载数据超过限定条数");

    // --验证导航栏搜索框
    $('#myForm').validate({
        rules: {
            searchInput: {
                searchtext: /<|>|\%|\+|"|\\|&/g,
                invalidnum: /^(19|20)$/,
                minlength: 2,
                maxlength: 100,
                required: true
            }
        },
        messages: {
            searchInput: {
                searchtext: '*检索词中包含无效字符!',
                invalidnum: '*检索词中包含无效字符!',
                minlength: '字符不得小于2',
                maxlength: '字符长度过长!',
                required: '字符不能为空!'
                
            }
        },
        errorPlacement: function (error, element) {
            error.appendTo(element.next());
        }
    });

    $(document).keydown(function (event) {
        if ($(".querySearch").is(":focus")) {
            if (event.which == 13) {
                $(".btn-query").click();
            }
        }
    });

    $('#TemplateContainer').load(_rootUrl + '/Resources/Model.html');

    // --点击事件：条目题名
    var dialog;
    $("body").on("click", 'a.model_a', function () {
        //console.log($(this).attr("data-setting"));
        dialog = new window.ShowDialog($(this)); //创建dialog，//按钮调用
        var filename = $(this).attr('data-filename');
        var pagerange = $(this).attr('data-pagerange');
        var cdnum = $(this).attr('data-cdnum');
        dialog.show(); //显示
        $.ajax({
            type: 'get',
            async: false,
            contentType: 'application / json',
            dataType: 'json',
            url: _rootUrl + '/Search/GetSearchInfoByFileName?filename=' + filename,
            success: function (data) {
                //console.log(data);
                if (parseInt(data.IsExistXLS) >= 1) {
                    data.IsExistXLS = 1;
                } else {
                    data.IsExistXLS = "";
                }
                // --handlebars模板初始化
                var source = $("#template").html();
                var template = Handlebars.compile(source);
                var html = template(data);
                $("#Model").html(html);
                $('#ReportPreview').attr('href', _rootUrl + '/Search/ReportPreview?filename=' + filename);
                $('#Excel').attr('href', _rootUrl + '/DownLoad/Excel?filecode=' + filename);
                $('#CAJ').attr('href',  CSYD.getCajUrl(filename, pagerange, cdnum));
                $('#PDF').attr('href',  CSYD.getPdfUrl(filename, pagerange, cdnum));
            },
            error: function (xhr, errorInfo, ex) {
                //console.log(ex);
            }
        });
    });

    // --点击事件：弹窗关闭
    $(this).find('#Model').on('click', '.btn_close', function () {
        dialog.close();
    });
});

// --初始化数值检索table
function drawValueTable(o) {
    if (o.dType == 0) { // --列表显示
        $(".table_builder").TableBuilder({
            data: o.data.data,        // --所有数据
            count: o.data.count,      // --数据总条数
            thead: o.thead,           // --thead标题数组
            toPage: o.start,          // --当前页
            length: o.length,         // --每页长度
            dType: o.dType,           // --显示方式
            column: [
                {
                    name: 'sIndex',
                    sWidth: '40',
                    sClass: 'tac'
                },
                {
                    name: 'DataTime'
                },
                {
                    name: 'Region'
                },
                {
                    name: 'FullIndicate',
                    render: function (data, full) {
                        return fnMark(data);
                    }
                },
                {
                    name: 'OriginalValue'
                },
                {
                    name: 'OriginalUnit'
                },
                {
                    name: 'ChName',
                    render: function (data, full) {
                        return fnMark(data) + '<br/>' + full['DataYear'];
                    },
                    sClass: 'tac'
                },
                {
                    name: 'PageNumber',
                    sWidth: '30'
                },
                {
                    name: 'StorageTag',
                    render: function (data, full) {
                        var str = '';
                        if (data == 0) {    // 入库标识为0，显示EXCEL图标
                            str += "<a href='" + _rootUrl + "/DownLoad/Excel?filecode=" + full["FileName"] + "' target='_blank'><img src='" + _rootUrl + "/Resources/design/images/nS_down2.png' width='16' height='16'></a>";
                        }
                        if (full['CDNum'] != null && full['CDNum'] != '') {   // 光盘号不为空，显示CAJ图标
                            str += '<a href="' + CSYD.getCajUrl(full['FileName'], full['PageRange'], full['CDNum']) + '"><img src="' + _rootUrl + '/Resources/design/images/nS_down1.png" width="15" height="15"></a>';
                        }
                        return str;
                    },
                    sWidth: '52'
                }

            ]  // --tbody数据格式
        });
    }
    else {  // --摘要显示
        $(".table_builder").TableBuilder({
            data: o.data.data,        // --所有数据
            count: o.data.count,      // --数据总条数
            thead: o.thead,           // --thead标题数组
            toPage: o.start,          // --当前页
            length: o.length,         // --每页长度
            dType: o.dType,           // --显示方式
            column: [
                {
                    name: 'sIndex',
                    sWidth: '40',
                    sClass: 'tac'
                },
                {
                    name: 'StorageTag',
                    render: function (data, full) {
                        var currStr = '';
                        currStr += fnMark(full['KnowledgeElement']);
                        currStr += '<br/>';
                        if (data == 0) {
                            currStr += '数据来自：' + full['DataYear'] + '《' + full['ChName'] + '》&nbsp;>>' + full['FatherNode'] + '&nbsp;>>&nbsp;' + '<a class="model_a" data-cdnum="' + full['CDNum'] + '" data-pagerange="' + full['PageRange'] + '" data-filename="' + full['FileName'] + "\" data-setting='{\"dialogID\":\"Model\"}' >" + full['ItemName'] + '</a>,第' + full['PageNumber'] + '页';
                        } else if (data != 0) {
                            currStr += '数据来自：' + full['DataYear'] + '《' + full['ChName'] + '》&nbsp;';
                        }
                        return currStr;
                    }
                },
                {
                    name: 'StorageTag',
                    render: function (data, full) {
                        var str = '';
                        if (full['CDNum'] != null && full['CDNum'] != '') {    // 光盘号不为空，显示CAJ图标
                            str += '<a href="' +  CSYD.getCajUrl(full['FileName'], full['PageRange'], full['CDNum']) + '"><img src="' + _rootUrl + '/Resources/design/images/nS_down1.png" width="15" height="15"></a>';
                        }
                        if (data == 0) {   // 入库标识为0，显示EXCEL图标
                            str += "<a href='" + _rootUrl + "/DownLoad/Excel?filecode=" + full["FileName"] + "' target='_blank'><img src='" + _rootUrl + "/Resources/design/images/nS_down2.png' width='16' height='16'></a>";
                        }
                        return str;
                    },
                    sWidth: '52'
                }

            ]
        });
    }
}

// --初始化条目检索table
function drawItemTable(o) {
    if (dType == 0) {
        $(".table_builder").TableBuilder({
            data: o.data.data,      // --所有数据
            count: o.data.count,    // --数据总条数
            thead: o.thead,         // --thead标题数组
            toPage: o.start,        // --当前页
            length: o.length,       // --每页长度
            dType: o.dType,         // --显示方式
            column: [               // --列
                {
                    name: 'sIndex',
                    sWidth: '40',
                    sClass: 'tac'
                },
                {
                    name: 'ItemName',
                    render: function (data, full) {
                        var str = '<a class="model_a" data-cdnum="' + full['CDNum'] + '" data-pagerange="' + full['PageRange'] + '" data-filename="' + full['FileName'] + "\" data-setting='{\"dialogID\":\"Model\"}' >" + fnMark(data) + '</a>';
                        return str;
                    }
                },
                {
                    name: 'ItemKeyword',
                    sWidth: '250',
                    render: function (data, full) {
                        if (data != null) {
                            return data.substr(0, 20);
                        }
                        else {
                            return data;
                        }
                    }
                },
                {
                    name: 'ChName',
                    render: function (data, full) {
                        var str = '';
                        if (full['Volume'] == null) {
                            str = full['DataYear'] + '年《' + fnMark(data) + '》,第' + (full['PrintPageNum'] == '' || full['PrintPageNum'] == null ? '~' : full['PrintPageNum']) + '页';
                        } else {
                            str = full['DataYear'] + '年《' + fnMark(data) + '》(' + full['Volume'] + '),第' + (full['PrintPageNum'] == '' || full['PrintPageNum'] == null ? '~' : full['PrintPageNum']) + '页';
                        }
                        return str;
                    }
                },
                {
                    name: 'IsExistXLS',
                    render: function (data, full) {
                        var str = '';
                        if (full['CDNum'] != null && full['CDNum'] != '') {   // 光盘号不为空，显示CAJ图标
                            str += '<a href="' + CSYD.getCajUrl(full['FileName'], full['PageRange'], full['CDNum']) + '"><img src="' + _rootUrl + '/Resources/design/images/nS_down1.png" width="15" height="15"></a>';
                        }
                        if (data == 1) {   // 存在excel，显示Excel图标
                            str += "<a href='" + _rootUrl + "/DownLoad/Excel?filecode=" + full["FileName"] + "' target='_blank'><img src='" + _rootUrl + "/Resources/design/images/nS_down2.png' width='16' height='16'></a>";
                        }
                        return str;
                    },
                    sWidth: '52'
                }

            ]
        });
    }
    else {
        $(".table_builder").TableBuilder({
            data: o.data.data,       // --所有数据
            count: o.data.count,     // --数据总条数
            thead: o.thead,           // --thead标题数组
            toPage: o.start,          // --当前页
            length: o.length,         // --每页长度
            dType: o.dType,           // --显示方式
            column: [               // --列
                {
                    name: 'sIndex'
                },
                {
                    name: 'ItemName',
                    render: function (data, full) {
                        var currStr = '';
                        currStr += '<a class="model_a" data-cdnum="' + full['CDNum'] + '" data-pagerange="' + full['PageRange'] + '" data-filename="' + full['FileName'] + "\" data-setting='{\"dialogID\":\"Model\"}' >" + fnMark(data) + '</a><br/>';
                        currStr += '关键词:' + full['ItemKeyword'].substr(0, 20) + '<br/>';
                        if (full['Volume'] == null) {
                            currStr += '来源:' + full['DataYear'] + '年《' + fnMark(full['ChName']) + '》,第' + full['PrintPageNum'] + '页';
                        } else {
                            currStr += '来源:' + full['DataYear'] + '年《' + fnMark(full['ChName']) + '》(' + full['Volume'] + '),第' + full['PrintPageNum'] + '页';
                        }
                        return currStr;
                    }
                },
                {
                    name: 'IsExistXLS',
                    render: function (data, full) {
                        var str = '';
                        if (full['CDNum'] != null) {   // 光盘号不为空，显示CAJ图标
                            str += '<a href="' + CSYD.getCajUrl(full['FileName'], full['PageRange'], full['CDNum']) + '"><img src="' + _rootUrl + '/Resources/design/images/nS_down1.png" width="15" height="15"></a>';
                        }
                        if (data == 1) {   // 存在excel，显示图标
                            str += "<a href='" + _rootUrl + "/DownLoad/Excel?filecode=" + full["FileName"] + "' target='_blank'><img src='" + _rootUrl + "/Resources/design/images/nS_down2.png' width='16' height='16'></a>";
                        }
                        return str;
                    },
                    sWidth: '52'
                }

            ]
        });
    }
}

// --初始化条目检索右侧分组列表
function initItemGroupList(data) {
    var tStr = '';
    var pStr = '';
    var cStr = '';
    var yStr = '';
    for (var i = 0; i < 5;) {
        if (data.ItemType[i]) {
            if (data.ItemType[i].data != '') {
                tStr += '<li><a>>&nbsp;<span>' + data.ItemType[i].data + '</span>(' + data.ItemType[i].count + ')' + '</a><li>';
                i++;
            }
            else {
                data.ItemType.splice(i, 1);
            }
        }
        else {
            break;
        }
    }
    $('#ItemType').html(tStr).removeClass('all');
    for (var i = 0; i < 5;) {
        if (data.Province[i]) {
            if (data.Province[i].data != '') {
                pStr += '<li><a>>&nbsp;<span>' + data.Province[i].data + '</span>(' + data.Province[i].count + ')' + '</a><li>';
                i++;
            }
            else {
                data.Province.splice(i, 1);
            }
        }
        else {
            break;
        }
    }
    $('#Province').html(pStr).removeClass('all');
    for (var i = 0; i < 5;) {
        if (data.ChName[i]) {
            if (data.ChName[i].data != '') {
                cStr += '<li><a>>&nbsp;<span>' + data.ChName[i].data + '</span>(' + data.ChName[i].count + ')' + '</a><li>';
                i++;
            }
            else {
                data.ChName.splice(i, 1);
            }
        }
        else {
            break;
        }
    }
    $('#ChName').html(cStr).removeClass('all');
    for (var i = 0; i < 5;) {
        if (data.DataYear[i]) {
            if (data.DataYear[i].data != '') {
                yStr += '<li><a>>&nbsp;<span>' + data.DataYear[i].data + '</span>(' + data.DataYear[i].count + ')' + '</a><li>';
                i++;
            }
            else {
                data.DataYear.splice(i, 1);
            }
        }
        else {
            break;
        }
    }
    $('#DataYear').html(yStr).removeClass('all');
}

// --初始化数值检索右侧分组列表
function initValueGroupList(data) {
    var tStr = '';
    var pStr = '';
    var cStr = '';
    var iStr = '';
    for (i = 0; i < 5; ) {
        if (!data.Year[i]) {
            break;
        }
        else if (data.Year[i].data != '') {
            tStr += '<li><a>>&nbsp;<span>' + data.Year[i].data + '</span>(' + data.Year[i].count + ')' + '</a><li>';
            i++;
        }
        else {
            data.Year.splice(i, 1);
        }
    }
    $('#Year').html(tStr).removeClass('all');
    for (i = 0; i < 5;) {
        if (!data.Province[i]) {
            break;
        }
        else if (data.Province[i].data != '') {
            pStr += '<li><a>>&nbsp;<span>' + data.Province[i].data + '</span>(' + data.Province[i].count + ')' + '</a><li>';
            i++;
        }
        else {
            data.Province.splice(i, 1);
        }
    }
    $('#Province').html(pStr).removeClass('all');
    for (i = 0; i < 5;) {
        if (!data.ChName[i]) {
            break;
        }
        else if (data.ChName[i].data != '') {
            cStr += '<li><a>>&nbsp;<span>' + data.ChName[i].data + '</span>(' + data.ChName[i].count + ')' + '</a><li>';
            i++;
        }
        else {
            data.ChName.splice(i, 1);
        }
    }
    $('#ChName').html(cStr).removeClass('all');
    for (i = 0; i < 5; ) {
        if (!data.FullIndicate[i]) {
            break;
        }
        else if (data.FullIndicate[i].data != '') {
            iStr += '<li><a>>&nbsp;<span>' + data.FullIndicate[i].data + '</span>' + '</a><li>';
            i++;
        }
        else {
            data.FullIndicate.splice(i, 1);
        }
    }
    $('#FullIndicate').html(iStr).removeClass('all');
}

// --初始化年鉴名称列表
function initKeywordList(keyword) {
    var data = [];
    for (var i = 0; i < oChNames.length; i++) {
        if (oChNames[i].ChNames.indexOf(keyword) == 0) {
            data.push(oChNames[i].ChNames);
        }
    }
    var str = '';
    var length = 0;
    length = data.length > 10 ? 10 : data.length;
    for (var i = 0; i < length; i++) {
        str += '<li>' + data[i] + '</li>';
    }
    $('ul#ChNameList').html(str);

    if (str == '') {
        $('ul#ChNameList').css({
            'border': 0,
            'padding' : 0
        });
    }
    else {
        $('ul#ChNameList').css({
            'border': '1px #e4e4e4 solid',
            'padding': '4px 6px'
        });
    }
}

// --获取url中的参数
function getUrlParam(name) {
    var res = "";
    if (window.location.search.indexOf("?") != -1) {
        var url = window.location.search.substr(1);
        var params = url.split("&");

        for (var i = 0; i < params.length; i++) {
            if (params[i].split("=")[0] == name) {
                res = params[i].split("=")[1];
            }
        }
    }
    return res;
}