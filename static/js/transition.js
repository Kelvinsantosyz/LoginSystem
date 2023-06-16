var formSignin = document.querySelector('#signin')
var formSignup = document.querySelector('#signup')
var btnColor = document.querySelector('.btnColor')

document.querySelector('#btnSignin').addEventListener('click', () => 
{
  formSignin.style.left = "25px"
  formSignup.style.left = "400px"
  btnColor.style.left = "10px"
})

document.querySelector('#btnSignup').addEventListener('click', () => 
{
  formSignup.style.left = "25px"
  formSignin.style.left = "-400px"
  btnColor.style.left = "110px"
})