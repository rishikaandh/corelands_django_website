// JavaScript for the product detail page

// Variables for the slideshow
let slideIndex = 1;

// Show the initial slides
showSlides(slideIndex);

// Function to show slides based on index
function showSlides(n) {
    const slides = document.getElementsByClassName("media-slide");
    if (n > slides.length) { slideIndex = 1; } // Loop back to the first slide
    if (n < 1) { slideIndex = slides.length; } // Loop to the last slide
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // Hide all slides
    }
    slides[slideIndex - 1].style.display = "block"; // Show the current slide
}

// Function to navigate through slides
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Function to handle thumbnail clicks and display corresponding slides
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Video control
const videoElements = document.querySelectorAll('.video-section video');

videoElements.forEach(video => {
    video.addEventListener('click', function () {
        // Pause all other videos when one is clicked
        videoElements.forEach(v => {
            if (v !== video) {
                v.pause();
            }
        });
        // Toggle play/pause on the clicked video
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    });
});
