// 今何問目かを表示するためのスクリプト

let clear_button = document.getElementById('clear_button');
let next_button = document.getElementById('next_button');
let counter_area = document.getElementById('quiz_counter');
let count = sessionStorage.getItem('count');
if (count == null) {
    count = 1;
    sessionStorage.setItem('count', count);
}

// カウントを表示
counter_area.innerText = "第" + count + "問";

clear_button.addEventListener('click', () => {
    count = 1;
    sessionStorage.setItem('count', count);
});

next_button.addEventListener('click', () => {
    let count = sessionStorage.getItem('count');
    count = parseInt(count) + 1;
    sessionStorage.setItem('count', count);
});