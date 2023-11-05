/// Show loading indicator
function showLoadingIndicator() {
    document.getElementById('loading-indicator').style.display = 'block';
}

// Hide loading indicator
function hideLoadingIndicator() {
    document.getElementById('loading-indicator').style.display = 'none';
}

// Example usage when making an AJAX request
function fetchResults() {
    showLoadingIndicator();
    // Make an AJAX request or perform your data fetch operation
    // When the request is complete, call hideLoadingIndicator()
    // to hide the loading indicator.
    // For example, in the success callback of your AJAX request.
    // AJAX request code goes here...
    // hideLoadingIndicator();
}
