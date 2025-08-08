function renderCounter(count) {
    const counter = document.getElementById('counter-display');
    const numberString = count.toString().padStart(4, '0'); // always 4 digits
    counter.innerHTML = '';

    for (let digit of numberString) {
    const div = document.createElement('div');
    div.classList.add('digit');
    div.textContent = digit;
    counter.appendChild(div);
    }

    document.getElementById('counter-number').textContent = count;
}

window.onload = function() {
  renderCounter(line_count);
};