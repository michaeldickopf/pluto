// Render the wait-list counter as "0010"
document.addEventListener('DOMContentLoaded', () => {
  const count = 10;
  const digits = String(count).padStart(4, '0').split('');
  document.querySelectorAll('.digit').forEach((el, i) => {
    el.textContent = digits[i];
  });
});

document.getElementsByClassName("email-form").addEventListener("click", onclickevent())

function onclickevent() {
    alert("clicked email form")
}