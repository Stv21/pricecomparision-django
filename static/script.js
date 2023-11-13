const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const resultsContainer = document.getElementById("results");

function searchProducts() {
  if (searchInput.value.trim().length !== 0) {
    resultsContainer.innerHTML = "";
    const query = searchInput.value.trim();
    fetch(`/search/?query=${query}`) // Fetch the search results from the server
      .then((response) => response.json())
      .then((data) => {
        // Update the results container with the data received from the server
        displaySearchResults(data);
      })
      .catch((error) => {
        console.error("Error fetching search results:", error);
      });
  }
}

function displaySearchResults(data) {
  resultsContainer.innerHTML = ""; // Clear previous results
  data.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.classList.add("product");
    productElement.innerHTML = `
      <img src="${product.image}" alt="${product.title}">
      <h2>${product.title}</h2>
      <p>Price: ${product.price}</p>
      <button>Add to Cart</button>
    `;
    resultsContainer.appendChild(productElement);
  });
}
function searchProducts() {
  // Show the spinner
  document.getElementById('loading').style.display = 'block';

  // Your existing search code...

  // Once the search is complete, hide the spinner
  // This might be in a callback or a 'finally' block if you're using promises
  document.getElementById('loading').style.display = 'none';
}

// Event listener for Enter key press in the search input field
searchInput.addEventListener("keyup", function (event) {
  if (event.key === "Enter") {
    searchProducts();
  }
});

searchButton.addEventListener("click", searchProducts);

// Your existing image slider JavaScript code here

let slideIndex = 0;
let timeoutId = null;
const slides = document.getElementsByClassName("mySlides");
const dots = document.getElementsByClassName("dot");

showSlides();

function currentSlide(index) {
  slideIndex = index - 1;
  showSlides();
}

function plusSlides(step) {
  slideIndex += step - 1;

  if (slideIndex < 0) {
    slideIndex = slides.length - 1;
  }

  showSlides();
}

function showSlides() {
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    dots[i].classList.remove("active");
  }

  slideIndex++;

  if (slideIndex > slides.length) {
    slideIndex = 1;
  }

  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].classList.add("active");

  if (timeoutId) {
    clearTimeout(timeoutId);
  }

  timeoutId = setTimeout(showSlides, 5000); // Change image every five seconds
}
