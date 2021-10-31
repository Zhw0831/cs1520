import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

const signInWithGoogle = document.getElementById('login');
const auth = firebase.auth();

const signInWithGoogle = () => {
    const googleProvider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(googleProvider)
    .then(() => {
        window.location.assign('./login')
    })
    .catch(error => {
        console.error(error);
    })
}
signInWithGoogle.addEventListener('click', signInWithGoogle);