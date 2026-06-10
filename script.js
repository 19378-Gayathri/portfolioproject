

const themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    themeToggle.textContent = "☀️";
  } else {
    themeToggle.textContent = "🌙";
  }
});



const reveals = document.querySelectorAll(".reveal");

function revealElements() {
  reveals.forEach((element) => {
    const windowHeight = window.innerHeight;
    const revealTop = element.getBoundingClientRect().top;
    const revealPoint = 120;

    if (revealTop < windowHeight - revealPoint) {
      element.classList.add("active");
    }
  });
}

window.addEventListener("scroll", revealElements);
window.addEventListener("load", revealElements);



window.addEventListener("scroll", () => {
  const nav = document.querySelector(".nav");

  if (window.scrollY > 50) {
    nav.style.boxShadow = "0 4px 20px rgba(0,0,0,0.1)";
  } else {
    nav.style.boxShadow = "none";
  }
});