function sendMSG() {
    const msg = document.getElementById('input').value;
    if (msg === '') {
        alert('Please fill in all fields');
    } else {
        alert('Message sent successfully');
    }
    document.getElementById('input').value = '';
}

const textarea = document.getElementById('myTextarea');

textarea.addEventListener('keyup', () => {
  const height = textarea.scrollHeight;
  textarea.style.height = height + 'px';
});