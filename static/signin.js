import {initializeApp} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js"
import { getAuth, signInWithEmailAndPassword,sendPasswordResetEmail } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js";
const firebaseConfig = {
  apiKey: "AIzaSyDuvYGS0NZQxTuLy3SNPNrTeWz2j6dvb8c",
  authDomain: "database-ce278.firebaseapp.com",
  databaseURL: "https://database-ce278-default-rtdb.firebaseio.com",
  projectId: "database-ce278",
  storageBucket: "database-ce278.appspot.com",
  messagingSenderId: "611283671593",
  appId: "1:611283671593:web:0973e6ca75f00f93485a38"
};

  const app= initializeApp(firebaseConfig)
  const auth = getAuth(app);
  const email = document.getElementById("email").value 
  const password = document.getElementById("password").value


function renderLandingPage() {
  // You can use AJAX to load the login page content dynamically, or simply redirect to the login page
  window.location.href = "/landing_page";
}

$(document).ready(function() {
  const submit = document.getElementById('submit')
  submit.addEventListener('click',function(event){
    event.preventDefault()
    handleFormSubmission();
  });
});

function handleFormSubmission() {
  var formData = {
    email: $('#email').val(),
    password: $('#password').val()
  };
  databasefunc(formData.email,formData.password);
  
  $.ajax({
    type: 'POST',
    url: '/login_data', // Endpoint on Flask server
    data: JSON.stringify(formData),
    contentType: 'application/json',
    success: function(response) {
        console.log('Form submitted successfully:', response);
        // Optionally, redirect to login page or do something else
    },
    error: function(xhr, status, error) {
        console.error('Error:', error);
        // Handle error if needed
    }
});
} 

function databasefunc(email,password){
  signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in 
    const user = userCredential.user;
    alert("logging in....")
    renderLandingPage()
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert(errorMessage)
    // ..
  });

 
}

// Forgot password
const forgotPassLabel = document.getElementById("forgetpassword")
forgotPassLabel.addEventListener('click',function(event){
  event.preventDefault()
  const email = document.getElementById("email").value 
  sendPasswordResetEmail(auth,email)
  .then(()=>{
      alert("A password Reset Link has been sent to your mail");
  })
  .catch((error)=>{
      console.log(error.code)
      console.log(error.message)

  })
})



