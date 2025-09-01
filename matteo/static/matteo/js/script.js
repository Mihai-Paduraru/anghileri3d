// Navbar scroll effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.custom-navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });

    // Gestione video background
    const video = document.querySelector('.global-video-bg');
    if (video) {
        // Pausa il video quando non è visibile per risparmiare batteria
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    video.play().catch(e => console.log('Auto-play non permesso:', e));
                } else {
                    video.pause();
                }
            });
        }, { threshold: 0.1 });

        observer.observe(video);

        // Gestione errori
        video.addEventListener('error', function() {
            console.log('Errore video di sfondo');
            document.querySelector('.global-video-overlay').style.background = 
                'linear-gradient(135deg, #1a2a6c 0%, #b21f1f 50%, #fdbb2d 100%)';
        });

        // Disabilita su mobile per performance
        if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
            video.style.display = 'none';
            document.querySelector('.global-video-overlay').style.background = 
                'linear-gradient(135deg, #1a2a6c 0%, #b21f1f 50%, #fdbb2d 100%)';
        }
    }
});