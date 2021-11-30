var i = 0;
var txt1 = 'Hope will never be taken away.';
var speed = 70; 

function typeWriter() {
    if (i < txt1.length) {
        document.getElementById("text1").innerHTML += txt1.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
        }
}