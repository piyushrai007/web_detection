function detectObjects() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    
    var formData = new FormData();
    formData.append('file', file);

    $.ajax({
        url: 'https://web-detection.onrender.com/detect',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            var imageData = response.image;
            if (imageData) {
                var imgElement = document.getElementById('detectedImage');
                imgElement.src = "data:image/jpeg;base64," + imageData;
            } else {
                console.error("Empty image data received.");
            }
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
}
document.addEventListener('DOMContentLoaded', function() {
    var modelTesting = document.getElementById('modelTesting');
    
    modelTesting.addEventListener('click', function() {
        if (!this.classList.contains('enlarged')) {
            this.classList.add('enlarged');
        }
    });

    var refreshButton = document.getElementById('refreshButton');

    refreshButton.addEventListener('click', function() {
        modelTesting.classList.remove('enlarged');
    });
});
