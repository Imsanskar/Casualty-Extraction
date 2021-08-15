
// Scripts

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});



// -----------map script---------------


let mapview;

function initmap() {
    mapview = new google.maps.Map(document.getElementById("mapcontainer"), {
        center: { lat: 27.7172, lng: 85.3240 },
        zoom: 12,
    });
}

// -------------------extractionpage js-----------------
// let infoContainer = document.getElementById("infoContainer");
// infoContainer.style.display ="none";
// let submitbtn = document.getElementById("submitbtn");
// submitbtn.addEventListener('click', event=>{
//     infoContainer.style.display ="block";
// })


function test(l){
	console.log(l)
}