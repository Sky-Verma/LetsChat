document.addEventListener("DOMContentLoaded", function () {
  var input = document.querySelectorAll("input");
  var placeholders = [
    "Username",
    "First Name",
    "Last Name",
    "Email",
    "Password",
    "Confirm Password",
  ];
  for (i = 0; i < placeholders.length; i++) {
    input[i + 1].placeholder = placeholders[i];
  }

  function chckpswd() {
    var pswd1 = document.querySelector("#id_password1");
    var pswd2 = document.querySelector("#id_password2");
    if (pswd2.value != pswd1.value) {
      pswd2 = document.querySelector("#id_password2").className = "not-same";
      console.log('not same')
    } else {
      pswd2 = document.querySelector("#id_password2").className = "same";
      console.log('same')
    }
  }

  document.querySelector("#id_password2").addEventListener("keyup", chckpswd);
});
