// var modal = document.getElementById("signIn");
// var btn = document.getElementById("loginButton");
// var span = document.getElementsByClassName("close")[0];

// btn.onclick = function() {
//     modal.style.display = "block";
// }

// span.onclick = function() {
//     modal.style.display = "none";
// }

// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const email = loginForm.email.value;
    const password = loginForm.password.value;

    if (email === "zhw87@pitt.edu" && password === "123456") {
        alert(".");
        location.reload();
    }
})

const signUpForm = document.getElementById("signup-form");
const signUpButton = document.getElementById("signup-form-submit");

signUpButton.addEventListener("click", (e) => {
    e.preventDefault();
    const email = signUpForm.email.value;
    const password = signUpForm.password.value;

    if (email === "zhw87@pitt.edu" && password === "123456") {
        alert(".");
        location.reload();
    }
})