$(function(){
    $('#submit').click(function(){
        var a = {}
        a['datetime'] = $('#datetimepicker1').find("input").val()
        a['book_num'] = $('#book_num').val()
        a['phone_num'] = $('#phone_num').val()
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/submit_order",
            data: JSON.stringify(a),
            dataType: 'json',
            cache: false,
            timeout: 600000,
            success: function (data) {
                if(data['ret'] == 'book success'){
                    alert('订餐成功')
                }
                else{
                    alert(data['ret'])
                }
                
            },
            error: function (e) {
                alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
            }
        });
    })
});


$(function(){
    $('#submit2').click(function(){
        var a = {}
        a['phone_num'] = $('#phone_num2').val()
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/delete_by_phone",
            data: JSON.stringify(a),
            dataType: 'json',
            cache: false,
            timeout: 600000,
            success: function (data) {
                if(data['ret'] == 'phone num invalid'){
                    alert('无效号码')
                }
                else if (data['ret'] == 'success'){
                    alert('退订成功')
                }
                else{
                    alert('退订失败')
                }
                
            },
            error: function (e) {
                alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
            }
        });
    })
});


$(function(){
    $('#phone_num').blur(function(){
        var a = {}
        a['phone_num'] = $('#phone_num').val()
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/query_order",
            data: JSON.stringify(a),
            dataType: 'json',
            cache: false,
            timeout: 600000,
            success: function (data) {
                if(data['ret'] == 'phone num invalid'){
                    $('#ee').html('无效号码')
                }
                else{
                    $('#ee').html('手机尚未订餐')
                }
                
            },
            error: function (e) {
                alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
            }
        });
    })
});


$(function(){
    $('#phone_num2').blur(function(){
        var a = {}
        a['phone_num'] = $('#phone_num2').val()
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/query_order",
            data: JSON.stringify(a),
            dataType: 'json',
            cache: false,
            timeout: 600000,
            success: function (data) {
                if(data['ret'] == 'phone num invalid'){
                    $('#board').html('无效号码')
                }
                else if(data['ret'] == 'None'){
                    $('#board').html('手机尚未订餐')
                }
                else{

                    var j = JSON.parse(data['ret'].replace(/'/g,"\""))
                    var date = j['date']
                    var phone = j['phone']
                    var num = j['num']
                    var s = '查询到订单：' + '\n\t电话号码：' + phone + '\n\t日期：' + date + '\n\t人数：' + num
                    $('#board').html(s)
                }
                
            },
            error: function (e) {
                alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
            }
        });
    })
});





$(function(){
    $('#book_num').blur(function(){
        var a = {}
        a['datetime'] = $('#datetimepicker1').find("input").val()
        a['book_num'] = $('#book_num').val()
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/query_num",
            data: JSON.stringify(a),
            dataType: 'json',
            cache: false,
            timeout: 600000,
            success: function (data) {
                if(data['ret'].indexOf('ok') == -1){
                    $('#dd').html('暂无空余座位')
                }
                else{
                    $('#dd').html('输入手机号码')
                }
                
            },
            error: function (e) {
                alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
            }
        });
    })
});


function query_date(time){
    alert(time)
    var a = {}
    a['datetime'] = time
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/query_date",
        data: JSON.stringify(a),
        dataType: 'json',
        cache: false,
        timeout: 600000,
        success: function (data) {
            // alert("success")
            if(data['ret'] == 'not the time'){
                // window.alert("not")
                $('#cc').html('不在预订日期内,请重新输入日期\n注意：用户能够预订两天之内的晚餐餐位，晚上七点之后\n不能预订当天的餐位，但可以预订后天的餐位。')
            }
            else{
                // alert("good")
                var t = data['ret']
                t = JSON.parse(t)
                res = ""
                for (var i = 0;i < 6;i++){
                    res += "第" + i + "桌空闲座位："
                    var ans = 0 
                    for(var j = 0;j < 8;j++){
                        if(t[i][j] ==0){
                            ans += 1
                        }
                    }
                    res += ans
                    res += "\n"
                }
                res += '输入就餐人数'
                $('#cc').html(res)
            }
            
        },
        error: function (e) {
            alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);  
        }
    });
    

    return "moren"
}