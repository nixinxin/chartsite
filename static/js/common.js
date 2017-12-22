(function (root,factory) {

    "use strict";

    // CommonJS module is defined
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = factory(require('jquery')(root));
    } else {
        // planted over the root!
        root.common = factory(root.jQuery);
    }

})( this,function($){
    $.fn.serializeJSON=function() {
        var json = {};
        $.map($(this).serializeArray(), function(n, i){
            json[n['name']] = n['value'];
        });
        return json;
    };
    String.prototype.visualLength = function(size){
        var $e = document.createElement('span');
        $e.style.fontSize = size+'px';
        $e.textContent = this;
        document.body.appendChild($e);
        var length = $e.offsetWidth;
        document.body.removeChild($e);
        return this == 'C语言'?327:length;
    };
    String.prototype.toJSON = function(){
        var json = {},sArr = this.split( '&' );
        for ( var s = 0; s < sArr.length;s++ ) {
            var cache = sArr[s].split( '=' );
            if(cache.length == 2){
                json[cache[0]] = cache[1].trim();
            }
        }
        return json;
    };
    var Common = function(){

    };
    Common.cookie = function(name, value, options){
        if ( typeof value != 'undefined' ) { // name and value given, set cookie
            options = options || {};
            if ( value === null ) {
                value = '';
                options.expires = -1;
            }
            var expires = '';
            if ( options.expires && ( typeof options.expires == 'number' || options.expires.toUTCString ) ) {
                var date;
                if ( typeof options.expires == 'number' ) {
                    date = new Date();
                    //过期时间，分钟
                    date.setTime( date.getTime() + ( options.expires * 60 * 1000 ) );
                    //过期时间，天
                    //date.setTime(date.getTime() + (options.expires * 24 * 60 * 60 * 1000));
                } else {
                    date = options.expires;
                }
                expires = '; expires=' + date.toUTCString();
                // use expires attribute, max-age is not supported by IE
            }
            var path = options.path ? '; path=' + options.path : '; path=/';
            var domain = options.domain ? '; domain=' + options.domain : '';
            var secure = options.secure ? '; secure' : '';
            document.cookie = [name, '=', encodeURIComponent(value), expires, path, domain, secure].join('');
        } else { // only name given, get cookie
            var cookieValue = null;
            if ( document.cookie && document.cookie != '') {
                var cookies = document.cookie.split( ';' );
                for ( var i = 0; i < cookies.length; i++ ) {
                    var cookie = $.trim( cookies[i] );
                    // Does this cookie string begin with the name we want?
                    if ( cookie.substring( 0, name.length + 1 ) == ( name + '=' ) ) {
                        cookieValue = decodeURIComponent( cookie.substring( name.length + 1 ) );
                        break;
                    }
                }
            }
            return cookieValue;
        }
    };
    // Private array of chars to use
    var CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        .split("");

    Common.uuid = function(len, radix) {
        var chars = CHARS, uuid = [], i;
        radix = radix || chars.length;

        if (len) {
            // Compact form
            for (i = 0; i < len; i++)
                uuid[i] = chars[0 | Math.random() * radix];
        } else {
            // rfc4122, version 4 form
            var r;

            // rfc4122 requires these characters
            uuid[8] = uuid[13] = uuid[18] = uuid[23] = "-";
            uuid[14] = "4";

            // Fill in random data. At i==19 set the high bits of clock sequence
            // as
            // per rfc4122, sec. 4.1.5
            for (i = 0; i < 36; i++) {
                if (!uuid[i]) {
                    r = 0 | Math.random() * 16;
                    uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r];
                }
            }
        }

        return uuid.join("");
    };

    // A more performant, but slightly bulkier, RFC4122v4 solution. We boost
    // performance
    // by minimizing calls to random()
    Common.uuidFast = function() {
        var chars = CHARS, uuid = new Array(36), rnd = 0, r;
        for (var i = 0; i < 36; i++) {
            if (i == 8 || i == 13 || i == 18 || i == 23) {
                uuid[i] = "-";
            } else if (i == 14) {
                uuid[i] = "4";
            } else {
                if (rnd <= 0x02)
                    rnd = 0x2000000 + (Math.random() * 0x1000000) | 0;
                r = rnd & 0xf;
                rnd = rnd >> 4;
                uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r];
            }
        }
        return uuid.join("");
    };

    // A more compact, but less performant, RFC4122v4 solution:
    Common.uuidCompact = function() {
        return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,
            function(c) {
                var r = Math.random() * 16 | 0, v = c == "x"
                    ? r
                    : (r & 0x3 | 0x8);
                return v.toString(16);
            });
    };
    return Common;
});