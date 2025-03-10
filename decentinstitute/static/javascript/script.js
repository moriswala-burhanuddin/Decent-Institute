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
sr.reveal('.one',{delay:300, origin:'left'})
sr.reveal('.two',{delay:330, origin:'top'})
sr.reveal('.three',{delay:300, origin:'right'})
sr.reveal('.hero .bg-img h1',{delay:150, origin:'top'})
sr.reveal('.hero .bg-img a',{delay:120, origin:'bottom'})
sr.reveal('.title h3',{delay:150, origin:'left'})
sr.reveal('.title h2',{delay:150, origin:'right'})
sr.reveal('.title-2 h3',{delay:150, origin:'left'})
sr.reveal('.title-2 h2',{delay:160, origin:'right'})
sr.reveal('.title-3 h3',{delay:150, origin:'left'})
sr.reveal('.title-3 h2',{delay:150, origin:'right'})
sr.reveal('.cc1', {
  delay: 160, 
  origin: 'left',
 
  duration: 1000,
  interval: 200, // Staggered effect
  easing: 'ease-in-out'
});
sr.reveal('.cc2', {
  delay: 160, 
  origin: 'right',
 
  duration: 1000,
  interval: 200, // Staggered effect
  easing: 'ease-in-out'
});

sr.reveal('.review-list ',{delay:150, origin:'left'})
sr.reveal('.review-form-container ',{delay:150, origin:'right'})
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
const coursesPerPage = 4;
let currentPage = 1;

function displayCourses() {
    const allCourses = document.querySelectorAll('.course-card-container');
    const totalCourses = allCourses.length;
    const totalPages = Math.ceil(totalCourses / coursesPerPage);

    // Hide all courses
    allCourses.forEach(course => (course.style.display = 'none'));

    // Show courses for the current page
    const start = (currentPage - 1) * coursesPerPage;
    const end = start + coursesPerPage;
    for (let i = start; i < end && i < totalCourses; i++) {
        allCourses[i].style.display = 'block';
    }

    // Enable/disable pagination buttons
    document.querySelector('.prev').disabled = currentPage === 1;
    document.querySelector('.next').disabled = currentPage === totalPages;

    // Update page numbers
    renderPageNumbers(totalPages);
}

function renderPageNumbers(totalPages) {
    const pageNumbersContainer = document.getElementById('page-numbers');
    pageNumbersContainer.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.innerText = i;
        pageButton.className = i === currentPage ? 'active' : '';
        pageButton.onclick = () => goToPage(i);
        pageNumbersContainer.appendChild(pageButton);
    }
}

function changePage(direction) {
    const allCourses = document.querySelectorAll('.course-card-container');
    const totalCourses = allCourses.length;
    const totalPages = Math.ceil(totalCourses / coursesPerPage);

    if (direction === 'next' && currentPage < totalPages) {
        currentPage++;
    } else if (direction === 'prev' && currentPage > 1) {
        currentPage--;
    } else if (typeof direction === 'number') {
        currentPage = direction; // Go to specific page (Last page button)
    }

    displayCourses();

    // Scroll to the top of the course container
    scrollToCourseContainer();
}

function goToPage(page) {
    currentPage = page;
    displayCourses();

    // Scroll to the top of the course container
    scrollToCourseContainer();
}

function scrollToCourseContainer() {
    const courseContainer = document.getElementById('course-container');
    courseContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Initial display (without scrolling)
displayCourses();


// ***********************************************


    document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("contact-link").addEventListener("click", function (event) {
            event.preventDefault(); // Prevent page reload
    
            // Hide specific sections
            let sectionsToHide = [
                "title",
                "course-container-ii",
                "title-3",
                "course-container",
                "pagination",
                "about-us-container",
                "title-2",
                "reviews-section"
            ];
    
            sectionsToHide.forEach(function (id) {
                let element = document.getElementById(id);
                if (element) {
                    element.style.display = "none";
                }
            });
    
            // Show the contact section
            document.querySelector(".contact").style.display = "block";
        });
    });



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
      