
//自定义验证函数库
//验证textbox
var IsTextBoxValid = function (obj) {
    var reg = /^[\da-zA-Z\u4e00-\u9fa5]*$/g;
    if (obj.val() == "") {
        alert("请输入查询关键词!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入数字、字母或中文!");
        return false;
    }
    if (obj.val().length > 50) {
        alert("字符超长，请保证在50个字符以下!");//删去“检索词”
        return false;
    }
    return true;
}

var IsTextValid = function (obj) {
    var reg = /^[\da-zA-Z\u4e00-\u9fa5]*$/g;
    if (!reg.test(obj.val())) {
        alert("请输入数字、字母或中文!");
        return false;
    }
    if (obj.val().length > 50) {
        alert("字符超长，请保证在50个字符以下!");//删去“检索词”
        return false;
    }
    return true;
}

var IsNameValid = function (obj) {
    var reg = /^[\da-zA-Z\u4e00-\u9fa5]*$/g;
    if (obj.val() == "") {
        alert("名称不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入数字、字母或中文!");
        return false;
    }
    if (obj.val().length > 50) {
        alert("字符超长，请保证在50个字符以下!");//删去“检索词”
        return false;
    }
    return true;
}

var IsEqualValid = function (obj) {
    var reg = /([（）\da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("公式不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("构造公式不符合四则运算基本法则,请验证公式!");
        return false;
    }
    if (obj.val().length > 500) {
        alert("字符超长，请保证在500个字符以下!");//删去“检索词”
        return false;
    }
    return true;
}
var IsFormularValid = function (obj) {
    var reg = /([ＧＤＰ（）【】、 \da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("公式不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("构造公式不符合四则运算基本法则,请验证公式!");
        return false;
    }
    if (obj.val().length > 500) {
        alert("字符超长，请保证在500个字符以下!");//删去“检索词”
        return false;
    }
    if (obj.val().indexOf("<")>=0 || obj.val().indexOf(">")>=0) {
        alert("构造公式不符合四则运算基本法则,请验证公式!");
        return false;
    }
    return true;
}

//搜索框验证
var Valid_SearchBox =function (obj) {
    var reg = /([（）\da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("搜索框不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入字母、数字和汉字!");
        return false;
    }
    if (obj.val().length > 100) {
        alert("字符超长，请保证在100个字符以下!");
        return false;
    }
    return true;
}

//权重输入框验证
var Valid_Weight = function (string,obj) {
    var reg = /^\d+(\.\d+)?$/;
    if (obj.val() == "") {
        alert(string+"权重不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert(string+"权重必须为数字!");
        return false;
    }
    if (obj.val().length > 5) {
        alert(string+"权重不超过3位小数!");
        return false;
    }
    if (parseFloat(obj.val()) > 1 || parseFloat(obj.val())<=0) {
        alert(string+"权重值应大于0且小于1！");
        return false;
    }
    return true;
}

//名称输入框验证
var Valid_NameInput =function (obj) {
    var reg = /([（）【】、 \da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("名称不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入字母、数字和汉字!");
        return false;
    }
    if (obj.val().length > 100) {
        alert("字符超长，请保证在100个字符以下!");
        return false;
    }
    return true;
}

//公式输入框验证
var Valid_FormularInput = function (obj) {
    var reg = /([（）【】、\da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("构造公式不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入字母、数字和汉字，请勿输入除【】、之外的特殊字符!");
        return false;
    }
    if (obj.val().length > 500) {
        alert("字符超长，请保证在500个字符以下!");
        return false;
    }
    return true;
}

//正文输入框验证
var Valid_TextInput = function (obj) {
    var reg = /([（）【】、，。\da-zA-Z \u4e00-\u9fa5])+/;
    if (obj.val() == "") {
        alert("名称不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("请输入字母、数字、汉字或中文标点!");
        return false;
    }
    if (obj.val().length > 100) {
        alert("字符超长，请保证在100个字符以下!");
        return false;
    }
    return true;
}

//
var insertAtCaret = function (obj, myValue) {
    var $t = obj[0];
    if (document.selection) {
        $t.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
        $t.focus();
    }
    else {
        if ($t.selectionStart || $t.selectionStart == '0') {
            var startPos = $t.selectionStart;
            var endPos = $t.selectionEnd;
            var scrollTop = $t.scrollTop;
            $t.value = $t.value.substring(0, startPos) + myValue + $t.value.substring(endPos, $t.value.length);
            this.focus();
            $t.selectionStart = startPos + myValue.length;
            $t.selectionEnd = startPos + myValue.length;
            $t.scrollTop = scrollTop;
            point = $t.selectionEnd;
        }
        else {
            this.value += myValue;
            this.focus();
        }
    }
}

//年份输入框验证
var Valid_db_year = function (obj) {
    var reg = /\d{4}\年/;
    if (obj.val() == "") {
        alert("年份不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("年份格式“2000年”!");
        return false;
    }
    if (obj.val().length > 5) {
        alert("年份格式“2000年”!");
        return false;
    }
    return true;
}

//年份输入框验证
var Valid_db_month = function (obj) {
    var reg = /\d{4}年\d月|\d{4}年[1-4]季度|\d{4}年[1]{1}-\d月|\d{4}年[1]{1}-[2-4]季度/;
    if (obj.val() == "") {
        alert("年份不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("年份格式“2000年1月（季度）、2000年1-2月（季度）”!");
        return false;
    }
    if (obj.val().length > 11) {
        alert("年份格式“2000年1月（季度）、2000年1-2月（季度）”!");
        return false;
    }
    return true;
}


//国标地域代码输入框验证
var Valid_db_zonecode = function (obj) {
    var reg = /\d{6}/;
    if (obj.val() == "") {
        alert("国标地域代码不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("国标地域代码为6位数字!");
        return false;
    }
    if (obj.val().length > 6) {
        alert("国标地域代码为6位数字!");
        return false;
    }
    return true;
}

//生成随机数
var RandomCount = function (count) {
    var str = "";
    for (var i = 0; i < count; i++) {
        str += Math.floor(Math.random() * 10).toString();
    }
    return str;
}

//数值输入框验证
var Valid_db_value = function (obj) {
    var reg = /([-.\d])+/;
    if (obj.val() == "") {
        alert("数值不能为空!");
        return false;
    }
    if (!reg.test(obj.val())) {
        alert("数值请输入数字!");
        return false;
    }
    if (obj.val().length > 100) {
        alert("字符超长，请保证在100个字符以下!");
        return false;
    }
    return true;
}
/*var Validation = function Validation(IsNull,IsValid,IsLength,IsType,obj) {
    this.IsNull = IsNull;
    this.IsValid = IsValid;
    this.IsLength = IsLength;
    this.IsType = IsType;
    IsType(IsNull,IsValid,IsLength);
}

Validation(true, true, true, Valid_FormularInput,$("#"));*/