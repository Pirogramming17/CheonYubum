const Stopwatch = document.querySelector("#stopwatch");
const StartBtn = document.querySelector(".start__btn");
const StopBtn = document.querySelector(".stop__btn");
const ResetBtn = document.querySelector(".reset__btn");

const CheckBtn = document.querySelector("#check__btn");
const TrashBtn = document.querySelector("#trash__btn");

let Time = 0;
let Time__box;

function TimetWatch() {
  Time++;
  let Second = parseInt(Time / 100);
  let MilliSec = Time % 100;
  Stopwatch.textContent = "${Second} : S{MilliSec}";
}

function StartTime() {
  clearInterval(Time__box);
  Time__box = setInterval(TimeWatch, 10);
}

function SaveRecord() {
  const saveNode = document.createElement("div");
  saveNode.name = "New__check";
  saveNode.className = "";
}
