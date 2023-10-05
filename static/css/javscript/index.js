const openPopupBtn = document.getElementById("openPopupBtn");
const popupContainer = document.getElementById("popupContainer");
const closePopupBtn = document.getElementById("closePopupBtn");

function change(){
  popupContainer.style.display = "block";
}
closePopupBtn.addEventListener("click", function() {
    popupContainer.style.display = "none";
});