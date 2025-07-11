// 選択肢をランダムにする

window.addEventListener('load', shuffle_select);

function shuffle_select() {
    let select_list = document.querySelector('.select_list');
    let list_items = Array.from(select_list.children);
    let shuffled_items = list_items.sort(() => Math.random() - 0.5);
    select_list.innerHTML = '';
    shuffled_items.forEach(item => select_list.appendChild(item));
}

// 選択肢より、正解不正解を判別するスクリプト
const selects = document.querySelectorAll('.btn');
const correct = document.querySelector('.correct_content');
const incorrect = document.querySelector('.incorrect_content');
const next_content = document.querySelector('.next.is_hidden');


function destinction_answer() {
    if(this.id == 'select_1') {
        this.style.background = "#ff5733";
        correct.classList.add('is_active');
        correct_counted++;
        sessionStorage.setItem('correct_counted', correct_counted);
    } else {
        this.style.background = "#4747ff";
        incorrect.classList.add('is_active');
        incorrect_counted++;
        sessionStorage.setItem('incorrect_counted', incorrect_counted);
    }
    this.classList.add('is_selected');
    next_content.classList.remove('is_hidden');
    console.log('正解数：' + correct_counted)
    console.log('不正解数：' + incorrect_counted)
    selects.forEach(select => {
        select.removeEventListener('click', destinction_answer);
    });
}

selects.forEach(select => {
    select.addEventListener('click', destinction_answer);
});

// 正解・不正解をカウントするスクリプト

let correct_counted = sessionStorage.getItem('correct_counted');
let incorrect_counted = sessionStorage.getItem('incorrect_counted');
let back = document.getElementById('back');

if(correct_counted == null && incorrect_counted == null) {
    correct_counted = 0;
    incorrect_counted = 0;
    sessionStorage.setItem('correct_counted', correct_counted);
    sessionStorage.setItem('incorrect_counted', incorrect_counted);
};

back.addEventListener('click', () => {
    correct_counted = 0;
    incorrect_counted = 0;
    sessionStorage.setItem('correct_counted', correct_counted);
    sessionStorage.setItem('incorrect_counted', incorrect_counted);
});