//  Profile modal
document.addEventListener('DOMContentLoaded', (event) => {
    // Get the modal
    var modal = document.getElementById("profileModal");

    // Get the button that opens the modal
    var btn = document.getElementById("profileModalBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});


document.addEventListener('DOMContentLoaded', (event) => {
    // related to making orders
    var modal0 = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn1 = document.getElementById("viewDetailsBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal 
    btn1.onclick = function() {
    modal0.style.display = "block";
    }
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal0.style.display = "none";
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal0) {
        modal0.style.display = "none";
        }
  }});

// Farm modal 
// Get the modal
var farmModal = document.getElementById("addFarmModal");

// Get the button that opens the modal
var btn = document.getElementById("addFarmBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
 
// When the user clicks the button, open the modal 
btn.onclick = function() {
    farmModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    farmModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == farmModal) {
        farmModal.style.display = "none";
    }
}
