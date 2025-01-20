document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("serviceRequestForm");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent form submission for now

            const requestType = document.getElementById("requestType").value;
            const details = document.getElementById("details").value;

            if (!requestType || !details) {
                alert("Please fill out all required fields.");
                return;
            }

            alert("Service request submitted successfully!");
            form.reset();
        });
    }
});
