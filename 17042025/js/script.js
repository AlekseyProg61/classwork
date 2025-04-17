num = 0;

elNum = document.getElementsByClassName("num")[0];
console.log(elNum.textContent);

function up() {
  elNum.textContent++;
}

function down() {
  elNum.textContent--;
}
console.log(num);


age = confirm("Тебе есть 18 лет?", "ДА", "НЕТ");
if (age) {
  man = confirm("Ты человек или робот?");
  if (man) {
    jv = confirm("Ты учишь Java?");
    if (jv) {
      alert("Добро пожаловать");
    }
  }
} else {
  alert("Вход запрещён!!!");
}

let a = (Math.floor(Math.random() * 2));
