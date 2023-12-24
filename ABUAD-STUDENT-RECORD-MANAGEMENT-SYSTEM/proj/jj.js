// Function to display the popup with a custom message
var btn = document.getElementById("btn")
btn.style.display = "none"

function showpopup(message,isSuccess){
  var popup = document.getElementById("popup")
  var popupContent = document.getElementById("popup-content")
  var btn = document.getElementById("btn")


  popupContent.textContent = message;
  popup.style.display = "block";
  popup.style.backgroundColor = isSuccess ? "green" : "red";
  
  btn.style.display = "block"
   btn.addEventListener('click',function(){
      popup.style.display = "none"
   })
   setTimeout(function(){
     popup.style.backgroundColor="yellow"
     popup.style.dispaly = "none"
     btn.style.display = "none"
   },3000) 

}
  
var login = document.getElementById("login-button")
   login.addEventListener("click",function(){
      var password = document.getElementById('password').value
      var userName = document.getElementById('username').value

      if (password === "default"  & userName === "default" ){
        showpopup("you are logged in good job ", true )
      }else if (password != "default"  & userName === "default" ){
             showpopup("password is incorrect but username is correct", false)
      }else if(password === "default"  & userName != "default" ){
        showpopup("password is correct but username is incorrect", false)
      }else
      showpopup("both  password and username are  incorrect ",false )
   })
   