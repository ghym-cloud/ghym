//window.onload = function() {
// var loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
// console.log('Page load time is ' + loadTime / 1000);
// performanceDisplay = document.getElementById("timer");
// performanceDisplay.innerText = loadTime / 1000;
//}
var modal = document.getElementById("myModal");
var modal2 = document.getElementById("myModal2");
var modal3 = document.getElementById("myModal3");
var modal4 = document.getElementById("myModal4");
var modal5 = document.getElementById("myModal5");
window.onclick = function(event) {
 if (event.target == modal) {
  modal.style.display = "none";
 }
 if (event.target == modal2) {
  modal2.style.display = "none";
 }
 if (event.target == modal3) {
  modal3.style.display = "none";
 }
 if (event.target == modal4) {
  modal4.style.display = "none";
 }
 if (event.target == modal5) {
  modal5.style.display = "none";
 }
}
let slideIndex = 1;
function plusSlides(element,n) {
  showSlides(element.title,slideIndex += n);
}
function currentSlide(element,n) {
  showSlides(element.title,slideIndex = n);
}
function showSlides(w,n) {
  let i;
  let sl;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  switch(w) {
   case "cert":
    modal.style.display = "block";
    break;
   case "restaurants":
    modal2.style.display = "block";
    break;
   case "rese":
    modal3.style.display = "block";
    break;
   case "carecarrier":
    modal4.style.display = "block";
    break;
   case "lunchbox":
    modal5.style.display = "block";
    break;
  }
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  slides[slideIndex-1].style.display = "block";
}
