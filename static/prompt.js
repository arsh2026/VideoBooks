  
  $(document).ready(function() {
    const submit = document.getElementById('generatebutton')
    submit.addEventListener('click',function(event){
      event.preventDefault()
      showModal();
      handleFormSubmission();
    });
  });

  function showModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = "block";
  }

function hideModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = "none";
  }


  function handleFormSubmission() {
    var formData = {
      title: $('#yourstory').val(),
      textPrompt: $('#text1').val()
    };
    $.ajax({
      type: 'POST',
      url: '/promptFunc', // Endpoint on Flask server
      data: JSON.stringify(formData),
      contentType: 'application/json',
      success: function(response) {
          console.log('Form submitted successfully:', response);
          hideModal();
          window.location.href = "/viewVideo";
      },
      error: function(xhr, status, error) {
          console.error('Error:', error);
          // Handle error if needed
      }
  });
  } 
  
  