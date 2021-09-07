window.addEventListener('DOMContentLoaded', event => {
    // Toggle the side navigation
    const teToggle = document.getElementById("te-button")
    if (teToggle) {
        teToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});
