
console.log('man')


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

    

    
}

  
var appointmentButtons = document.querySelectorAll('.appointment-button');
function printButtonValue(event) {
    var button = event.target;
    var value = button.value;

    

  
  
  
    var id = value;
    console.log(id)
    $.ajax({
      url: '/download',
      method: 'GET',
      data: { id: value }, // Send the value of the button as 'id'
      success: function (data) {
          // Handle the data received from the server
          console.log("Data", data.name);
          var dataContainer = document.createElement('div');

          dataContainer.innerHTML = '<style>.receipt {padding:2rem; margin:2rem;}</style><div class="receipt" ><h1>Appointment Details</h1>' +'<h2 style="text-align:center;">'+JSON.stringify(data.hospital_name, null, 3)+'</h2>'+'<p class="field">PaitentName :' + JSON.stringify(data.patient, null, 2)+'</p>'+'<p class="field">Paitent Phone: ' + JSON.stringify(data.phone, null, 2)+'</p>'+'<p class="field">Patient Gender: ' + JSON.stringify(data.gender, null, 2)+'</p>'+'<p class="field">Doctor:' + JSON.stringify(data.doctor, null, 2)+'</p>'+'</div>';
          document.body.appendChild(dataContainer);
console.log(dataContainer)
          // Use html2pdf to convert the data container to a PDF
          
          html2pdf(dataContainer)
              

          // Clean up: remove the temporary data container
          document.body.removeChild(dataContainer);
          
      },
      error: function (error) {
          console.error('Error:', error);
      }
  });
}


    

appointmentButtons.forEach(function(button) {
    button.addEventListener('click', printButtonValue);

});


const patientSearchInput = document.getElementById('patient_id_input');
const patientDropdown = document.getElementById('patient');

