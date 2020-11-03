document.addEventListener('DOMContentLoaded',function(){

    var textar=document.querySelector('textarea');
    textar.rows=1;
    textar.cols=20;
    var label=document.querySelectorAll('label');
    label[2].style.display='none';
    var label=document.querySelector('#profile_pic-clear_id').style.display='none';
    var p=document.querySelectorAll('p');
    p[1].innerHTML='<br><label for="id_profile_pic">Profile pic:</label><input type="file" name="profile_pic" accept="image/*" id="id_profile_pic">';
    var button=document.querySelectorAll('button');
    button[0].className='submit';
    button[0].innerHTML='<i class="fab fa-telegram-plane fa-2x"></i>';
})
