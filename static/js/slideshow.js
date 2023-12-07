var slideIndexFemales = 1;
showFemaleDivs(slideIndexFemales);

function femaleNextDivs(n) {
    showFemaleDivs(slideIndexFemales += n);
}

function femalePrevDivs(n) {
    showFemaleDivs(slideIndexFemales += n);
}

function showFemaleDivs(n) {
    var x = document.getElementsByClassName("female-candidate");
    if (n > x.length) {slideIndexFemales = 1}
    if (n < 1) {slideIndexFemales = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndexFemales-1].style.display = "block";
}