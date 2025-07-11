let correct_counted = sessionStorage.getItem('correct_counted');
let incorrect_counted = sessionStorage.getItem('incorrect_counted');
let count = sessionStorage.getItem('count');

const all_count = document.querySelector('.all_count');
const correct = document.querySelector('.correct');
const correct_num = document.querySelector('.correct_num');
const incorrect = document.querySelector('.incorrect');


all_count.innerText = count + '問中...';
correct_num.innerText = correct_counted;
incorrect.innerText = incorrect_counted + '問不正解...';
if (incorrect_counted == 0) {
    incorrect.style.display = 'none';
}

if (correct_counted / count <= 0.4) {
    document.querySelector('.message').innerHTML = 'もう少し頑張りましょう！';
} else if (correct_counted / count <= 0.6) {
    document.querySelector('.message').innerHTML = 'まずまずの成績です！もう少し頑張りましょう！';
} else if (correct_counted / count <= 0.8) {
    document.querySelector('.message').innerHTML = 'よくできました！';
} else if (correct_counted <= count - 1) {
    document.querySelector('.message').innerHTML = '大変すばらしい成績です！';
} else {
    document.querySelector('.message').innerHTML = 'おめでとうございます！全問正解です！';
}


// リセットボタン
let back = document.getElementById('back');

// リセットボタンを押したときの処理
back.addEventListener('click', () => {
    count = 1;
    correct_counted = 0;
    incorrect_counted = 0;
    sessionStorage.setItem('count', count);
    sessionStorage.setItem('correct_counted', correct_counted);
    sessionStorage.setItem('incorrect_counted', incorrect_counted);
});