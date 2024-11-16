// Optional: Enhance feedback
document.addEventListener("DOMContentLoaded", () => {
    const output = document.querySelector(".output");
    if (output) {
        setTimeout(() => {
            output.style.display = "none";
        }, 5000); // Hide after 5 seconds
    }
});
