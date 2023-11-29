  
    var openPopupBtn = document.getElementById("openPopupBtn");
     var popupContainer = document.getElementById("popupContainer");
    var closePopupBtn = document.getElementById("closePopupBtn");
    var  mainHeader = document.querySelector('.main-header');


    // let zIndexState = 1;
    function change(){
      popupContainer.style.display = "block";
      if (zIndexState === 1) {
        mainHeader.style.zIndex = -1;
        zIndexState = -1;
    }
    }
    closePopupBtn.addEventListener("click", function() {
        popupContainer.style.display = "none";
        mainHeader.style.zIndex = 1;
        zIndexState = 1;
    });
  

    console.log('sfdsjfn')
    
    function downloadPDF() {
      var element = document.querySelector('table');
      html2pdf(element);
    }