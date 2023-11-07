
const patient_form = document.querySelector('.patient_form')

function reload(){
    var cb = document.querySelector('#new');
    var newer = cb.checked
    
    function patient(val){
       console.log(val)
        if(val === true){ 
            console.log('true')
            console.log(val)
            patient_form.style.display = "block";
            
          }
          else if(val === false){
            console.log('false')
            patient_form.style.display = "none";
        
          }
    }
    
    patient(newer)

    
  $(document).ready(function(){
    var url1 = "/patient/form/";
    var url2 = "/appointment_details_form/";
   $("#submit").click(function( ) {
        $.post("url1", $(".form_popup").serialize());
    $.post("url2", $('.form_popup').serialize());
    })
})
    
}

  
   
