import {initializeApp} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js"
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js";
import {getDatabase,set,ref} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js"
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

  const db=getDatabase();

function renderLoginPage() {
    // You can use AJAX to load the login page content dynamically, or simply redirect to the login page
    window.location.href = "/login";
}
  // SignUp


function databasefunc(email,password){
  createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    const uid = user.uid;
    set(ref(db,"TheUsers/"+uid),{
      UserId: email
    }).then(()=>{
      renderLoginPage();
    })
    alert("creating account ....")
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert(errorMessage)
    // ..
  });

}

function handleFormSubmission() {
  var formData = {
    email: $('#email').val(),
    password: $('#password').val()
  };
  databasefunc(formData.email,formData.password);
  

} 

$(document).ready(function() {
  const submit = document.getElementById('submit')
  submit.addEventListener('click',function(event){
    event.preventDefault()
    handleFormSubmission();
  });
});


    

