const crypto = require('crypto');
const w2 = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
    , Nue = w2 + "-@#$%^&*+!";


function jue(e) {
    return [...Array(e)].map(() => w2[Lue(0, 61)]).join("")
}


function Lue(e, t) {
    switch (arguments.length) {
        case 1:
            return parseInt(Math.random() * e + 1, 10);
        case 2:
            return parseInt(Math.random() * (t - e + 1) + e, 10);
        default:
            return 0
    }
}

function Pv(e = {}) {
    const {p: t, t: n, n: r, k: o} = e
        , u = Hue(t);
    return sha256(r + o + decodeURIComponent(u) + n)
}


function sha256(input) {
    console.log(input)
    const hash = crypto.createHash('sha256').update(input);
    return hash.digest('hex');
}


function Hue(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n => `${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
        t
}


function Au(e = []) {
    return e.map(t => Nue[t]).join("")
}


Xq = function (e, t) {
    var n = e, r = Jq(t), o, u;
    typeof r.filter == "function" ? (u = r.filter,
        n = u("", n)) : mr(r.filter) && (u = r.filter,
        o = u);
    var i = [];
    if (typeof n != "object" || n === null)
        return "";
    var s;
    t && t.arrayFormat in q1 ? s = t.arrayFormat : t && "indices" in t ? s = t.indices ? "indices" : "repeat" : s = "indices";
    var a = q1[s];
    if (t && "commaRoundTrip" in t && typeof t.commaRoundTrip != "boolean")
        throw new TypeError("`commaRoundTrip` must be a boolean, or absent");
    var l = a === "comma" && t && t.commaRoundTrip;
    o || (o = Object.keys(n)),
    r.sort && o.sort(r.sort);
    for (var c = oA(), d = 0; d < o.length; ++d) {
        var f = o[d];
        r.skipNulls && n[f] === null || iA(i, Qq(n[f], f, a, l, r.strictNullHandling, r.skipNulls, r.encode ? r.encoder : null, r.filter, r.sort, r.allowDots, r.serializeDate, r.format, r.formatter, r.encodeValuesOnly, r.charset, c))
    }
    var p = i.join(r.delimiter)
        , h = r.addQueryPrefix === !0 ? "?" : "";
    return r.charsetSentinel && (r.charset === "iso-8859-1" ? h += "utf8=%26%2310003%3B&" : h += "utf8=%E2%9C%93&"),
        p.length > 0 ? h + p : ""
}

function main123(PageNo) {
    // 网页上的格式
    c = "k8tUyS$m"
    a = 1681221242101
// jue 方法
    l = "1NISm2O3EKskaEYm"
    // console.log(Xq(data, {
    //     allowDots: !0
    // }))
    data = 'type=trading-type&publishStartTime=&publishEndTime=&siteCode=44&secondType=A&projectType=&thirdType=&dateType=&total=233956&pageNo=6&pageSize=10&openConvert=false'
    const f = Pv({
        p: JSON.stringify(data, {
            allowDots: !0
        }),
        t: a,
        n: l,
        k: c
    })
    d = {
        ['X-Dgi-Req-App']: 'ggzy-portal',
        ['X-Dgi-Req-Nonce']: l,
        ['X-Dgi-Req-Timestamp']: a,
        ['X-Dgi-Req-Signature']: f,
    }
    return d
}




console.log(main123(4))