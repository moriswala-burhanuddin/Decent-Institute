$(document).ready(function () {
    $('#contact-form').submit(function (event) {
      event.preventDefault() // Prevent page reload

      $.ajax({
        type: 'POST',
        url: '', // Submits to the same URL
        data: $(this).serialize() + '&contact_form=true',
        dataType: 'json',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        success: function (response) {
          if (response.success) {
            // Show success message
            $('#contact-message').text(response.message).fadeIn()

            // Clear the form fields
            $('#contact-form')[0].reset()
          } else {
            $('#contact-message').text('Error submitting message.').css('color', 'red').fadeIn()
          }

          // Hide message after 3 seconds
          setTimeout(() => {
            $('#contact-message').fadeOut()
          }, 3000)
        }
      })
    })
  })



  function toggleMenu() {
    const navLink = document.querySelector('.nav-link');
    navLink.classList.toggle('show');
}
let lastScrollTop = 0 // Variable to store the last scroll position
  const navbar = document.querySelector('.nav')
  const hamburger = document.querySelector('.hamburger')
  const links = document.querySelector('.links')
  
  // Function to handle scrolling behavior
  window.addEventListener('scroll', function () {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop
  
    if (currentScroll > lastScrollTop) {
      // Scroll down
      navbar.style.transform = 'translateY(-100%)' // Hide navbar when scrolling down
    } else {
      // Scroll up
      navbar.style.transform = 'translateY(0)' // Show navbar when scrolling up
    }
  
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll // Prevent negative values
  })
  
  document.addEventListener("DOMContentLoaded", function () {
    // Get the current page URL
    const currentPage = window.location.pathname;

    // Select all navigation links
    const navLinks = document.querySelectorAll(".nav-link ul li a");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active"); // Add 'active' class to the matching link
        }
    });
});
  


const sr = ScrollReveal ({
    distance:'60px',
    duration:2500,
    delay:400,
    reset:false
     


})
sr.reveal('.contact-form ',{delay:150, origin:'left'})
sr.reveal('.contact-form h2 ',{delay:150, origin:'top'})
sr.reveal('.contact-info',{delay:160, origin:'right'})

// ***********************************************
// Disable Right Click
document.addEventListener('contextmenu', event => event.preventDefault());

// Disable Keyboard Shortcuts for Inspect Element
document.addEventListener('keydown', function (event) {
    if (event.ctrlKey && (event.key === 'u' || event.key === 'U' || event.key === 's' || event.key === 'S' || event.key === 'p' || event.key === 'P')) {
        event.preventDefault();
    }
    if (event.ctrlKey && event.shiftKey && (event.key === 'I' || event.key === 'J' || event.key === 'C')) {
        event.preventDefault();
    }
    if (event.key === 'F12') {
        event.preventDefault();
    }
});

// Detect DevTools Opening (No alert, just logs)
console.log('%c ', 'font-size: 1px; background: url() no-repeat;');


// ***********************************************
function closeAd() {
  document.getElementById("adContainer").style.display = "none";
    }

// ***********************************************


document.addEventListener('DOMContentLoaded', function() {
  const glide = new Glide('.glide', {
    type: 'carousel',
    perView: 3,  // Default to 3 slides for larger screens
    gap: 10,     // Space between slides
    focusAt: 'center',
    autoplay: 2000,  // Auto-scroll every 2 seconds
    animationDuration: 600,
    animationTimingFunc: 'ease-in-out',
  });

  glide.mount();

  // Update the perView property based on screen size (responsive behavior)
  function updateSlides() {
    if (window.innerWidth <= 768) {
      glide.update({ perView: 1 });  // Show only 1 slide on mobile screens
    } else {
      glide.update({ perView: 3 });  // Show 3 slides for larger screens
    }
  }

  // Apply responsive behavior on page load and window resize
  updateSlides();
  window.addEventListener('resize', updateSlides);
});
