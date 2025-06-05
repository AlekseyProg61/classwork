let list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
shakeList(list);
let flag = true;
let prev = 0;

setTimeout(clear, 5000);

let boxes = document.querySelectorAll(".box");
console.log(boxes);

for (let i = 0; i < boxes.length; i++) {
  boxes[i].textContent = list[i];
}

boxes.forEach((element) => {
  element.addEventListener("click", function () {});
  showAllNumbers();
  shakeList(element);
});

function showNumber(element) {
  let index = 0;
  for (let i = 0; i < boxes.length; i++) {
    if (boxes[i] == element) {
      index = i;
      break;
    }
  }
  element.textContent = list[index];
  if (prev + 1 != list[index]) {
    flag = false;
    setTimeout(clear, 2000);
  } else prev++;
}

function showAllNumbers() {
  for (let i = 0; i < boxes.length; i++) {
    boxes[i].textContent = list[i];
  }
}

function showNumbers() {
  for (let i = 0; i < boxes.length; i++) {
    boxes[i].textContent = list[i];
  }
}

function clear() {
  for (let i = 0; i < boxes.length; i++) {
    boxes[i].textContent = "";
  }
}
// function changeCounter(element) {
//   let val = element.textContent;
//   element.textContent = Number(val) + 1;
// }

// function changeColor(element) {
//   let red = Math.floor(Math.random() * 255);
//   let green = Math.floor(Math.random() * 255);
//   let blue = Math.floor(Math.random() * 255);
//   element.style.backgroundColor = `rgb(${red},${green},${blue})`;
// }

// function click() {
//   let count = 0;
//   for (i = count; i++; );
//   {
//     if (count == 0) {
//       count++;
//       console.log("Счетчик", count);
//     }
//   }
// }

function shakeList(list) {
  for (let i = 0; i < list.length; i++) {
    n = list[i];
    rand = getRandomInt(list.length - 1);
    list[i] = list[rand];
    list[rand] = n;
  }
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

console.log(list);
