/**
 * Created by mona on 2017/11/11.
 */
//头像预览

$('.avatar_input').change(function () {
    var reader = new FileReader();
    var file = $('.avatar_input')[0].files[0];
    reader.readAsDataURL(file);
    reader.onload=function () {
        $('.avatar_img')[0].src = this.result;
    }

});


//初始化页面数据
(function () {
    function GetInitData() {
        //初始化页面数据函数
        $.ajax({
            url:'/ajax_get_user_info/',
            type:'GET',
            success:function (data) {
                data = JSON.parse(data)[0];
                nickname = data['nickname'];
                email = data['user__email'];
                bio = data['bio'];
                gender = data['gender'];
                $('[name="user"]').val(nickname);
                console.log(gender);
                if(gender){
                    $('#gender #1')[0].setAttribute('selected','selected');
                }
                else{
                    $('#gender #0')[0].setAttribute('selected','selected');

                }
                $('[name="email"]').val(email);
                $('[name="person_bio"]').val(bio);
            }
        })
    }

    $.extend({
        "initdata": function () {
            GetInitData();
        }
    });

})();
