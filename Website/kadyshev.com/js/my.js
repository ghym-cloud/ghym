window.onload = function() {
 var loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
 console.log('Page load time is ' + loadTime / 1000);
 performanceDisplay = document.getElementById("timer");
 performanceDisplay.innerText = loadTime / 1000;
}
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
function myBtn(img) {
 document.getElementById("myImg").src = img;
 modal.style.display = "block";
}
function mySlide(img) {
 document.getElementById("myModal").style.display = "block";
}
span.onclick = function() {
 modal.style.display = "none";
}
window.onclick = function(event) {
 if (event.target == modal) {
  modal.style.display = "none";
 }
}
