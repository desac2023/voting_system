var slideIndexMales = 1;
showDivs(slideIndexMales);

function nextDivs(n) {
    showDivs(slideIndexMales += n);
}

function prevDivs(n) {
    showDivs(slideIndexMales += n);
}

function showDivs(n) {
    var x = document.getElementsByClassName("candidate");
    if (n > x.length) {slideIndexMales = 1}
    if (n < 1) {slideIndexMales = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndexMales-1].style.display = "flex";
}
