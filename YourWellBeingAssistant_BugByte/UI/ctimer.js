let startTime;
let endTime;
let intervalId;

function startTimer() {
  startTime = new Date().getTime();
  intervalId = setInterval(updateTimeDisplay, 1000);
  document.getElementById("start-btn").disabled = true;
  document.getElementById("end-btn").disabled = false;
}

function endTimer() {
  endTime = new Date().getTime();
  clearInterval(intervalId);
  document.getElementById("start-btn").disabled = false;
  document.getElementById("end-btn").disabled = true;
  alert(`You used your device for ${(endTime - startTime) / 1000} seconds`);
}

function updateTimeDisplay() {
  let currentTime = new Date().getTime();
  let elapsedTime = (currentTime - startTime) / 1000;
  let hours = Math.floor(elapsedTime / 3600);
  let minutes = Math.floor((elapsedTime % 3600) / 60);
  let seconds = Math.floor(elapsedTime % 60);
  document.getElementById("time-display").innerHTML = `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}`;
}

function padZero(num) {
  if (num < 10) {
    return "0" + num;
  }
  return num;
}
