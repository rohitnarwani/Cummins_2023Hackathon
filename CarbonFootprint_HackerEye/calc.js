let btn = document.getElementById("btn");
btn.addEventListener('click', (event) => {
  event.preventDefault();
  calcFood();
});

let btn1 = document.getElementById("btn1");
btn1.addEventListener('click', (event) => {
  event.preventDefault();
  calcElec();
});

let btn2 = document.getElementById("btn2");

btn2.addEventListener('click', (event) => {
  event.preventDefault();
  waste();

});

let btnF = document.getElementById("btnF");
btnF.addEventListener('click', (event) => {
  event.preventDefault();
  final();
});

function calcFood() {
  var value;
  let te = document.getElementById("nonveg");
  if (te.checked == true) {
    value = 2.21;

  } else {
    let te = document.getElementById("veg");

    if (te.checked == true) {
      value = 1.9;

    } else {
      value = 1.8;
    }
  }
  local(value);

}

function local(value) {
  console.log("local", value)
  let te1 = document.getElementById("YES");
  if (te1.checked == true) {
    value = value - 0.44;
  } else {
    value = value - 0;
  }
  week(value);
}
var usingInCalcElec;

function week(value) {
  let te2 = document.getElementById("time").value;
  value = value + te2 * 0.09;
  // calcElec(value);
  usingInCalcElec = value;
  //return value;
}

var v2;

function calcElec() {
  let te2 = document.getElementById("elec").value;
  usingInCalcElec = usingInCalcElec + 0.0036 * te2;
  console.log(usingInCalcElec)
  v2 = usingInCalcElec;
  console.log(usingInCalcElec, "final value in calcelec")

}
var v3;


function waste() {
  let te3 = document.getElementById("waste").value;
  v2 = v2 + te3 * 0.07;
  v3 = v2;
}
var finalVar;

function final() {
  let te4 = document.getElementById("oxy").value;
  finalVar = 0.11 * te4;
  cc(v3);
}

function cc(v3) {
  console.log("Carbon Footprint: ", v3 - finalVar);
  let v=Math.abs(v3-finalVar);
  document.write("CARBON FOOTPRINT: ",v," tonnes");
}
