document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('.username').focus();
   var div =document.querySelectorAll('div');
   if(div[0].innerHTML=='Invalid Credentials.' ||   div[0].innerHTML=="Logged Out."){
       div[0].className='message';
   }
})