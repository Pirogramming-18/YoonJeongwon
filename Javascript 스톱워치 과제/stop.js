let [milliseconds,second,minute,hours] = [0,0,0,0];
let timerRef = document.querySelector('.timerDisplay');
let int = null;

let recordList = document.querySelector('.recordList');

document.querySelector('#start-btn').addEventListener('click', ()=>{
  if(int!==null){
      clearInterval(int);
  }
  int = setInterval(displayTimer,10);
});

document.querySelector('#stop-btn').addEventListener('click', ()=>{
  clearInterval(int);

  let nowre = document.querySelector('.timerDisplay').innerText;
  let HTML = "<td><input type='checkbox' class='check'></td><td>" + nowre +"</td>";
  let tr = document.createElement('tr');
  tr.innerHTML = HTML;

  if(! recordList.firstChild) {
      recordList.append(tr)
  } else {
      recordList.insertBefore(tr, recordList.lastChild)
  }
  return false
});

document.querySelector('#reset-btn').addEventListener('click', ()=>{
  clearInterval(int);
  [milliseconds,seconds,minutes,hours] = [0,0,0,0];
  timerRef.innerHTML = '00 : 00 : 00 : 00';
});

function displayTimer(){
  milliseconds+=10;

  if(milliseconds == 1000){
      milliseconds = 0;
      second++;

      if(second == 60){
          second = 0;
          minute++;

          if(minute == 60){
              minute = 0;
              hours++;
          }
      }
  }
  let h = hours < 10 ? "0" + hours : hours;
  let m = minute < 10 ? "0" + minute : minute;
  let s = second < 10 ? "0" + second : second;
  let ms_1 = milliseconds / 10;
  let ms = ms_1 < 10 ? "0" + ms_1 : ms_1;

  timerRef.innerHTML = ` ${h} : ${m} : ${s} : ${ms}`;
}

let allCheck = document.querySelector(".allCheck");
let list = document.querySelectorAll(".check");
let del = document.querySelector(".del");

// 동적 자료형에 이벤트 처리 --> 이벤트 위임
// function clickHandler(event){
//   let elem = event.target;
//   while(!elem.classList.contains('.check')){
//     elem = elem.parentNode;

//     if(elem.nodeName == 'BODY'){
//       elem =null;
//       return;
//     }
//   }
//   elem.checked = true;
// }


allCheck.onclick = () => {
  if(allCheck.checked) {
    for(let i =0; i<list.length; i++){
      list[i].checked = true;
    }
  }
  else  {
    for(let i =0; i<list.length; i++){
      list[i].checked = false;
    }
  }
}

del.onclick = () => {
  for(let i =0; i<list.length; i++){
    if(list[i].checked){
      list[i].parentElement.parentElement.remove();
    }
  }
}



// sw-2
var stopFullRecord = document.getElementById("stop-full-record");
var minutes = 00;
var seconds = 00;
var mseconds = 00;
var minutesText = document.getElementById("minutes");
var secondsText = document.getElementById("seconds");
var msecondsText = document.getElementById("mseconds");
var btnStart = document.getElementById('btnStart');
var btnStop = document.getElementById('btnStop');
var btnReset = document.getElementById('btnReset');
var recordUl = document.getElementById('stop-record');
var Interval; 

btnStart.addEventListener('click', function() {
    clearInterval(Interval);
    Interval = setInterval(startTimer, 10);
});

btnStop.onclick = function() {
    clearInterval(Interval);
    createRecord();
};

btnReset.onclick = function() {
    clearInterval(Interval);
    mseconds = "00";
    seconds = "00";
    msecondsText.innerHTML = mseconds;
    secondsText.innerHTML = seconds;
    recordUl.innerHTML = "";
};

function createRecord() {
    var node = document.createElement("li");
    var record = stopFullRecord.textContent;
    var textnode = document.createTextNode(record);        
    node.appendChild(textnode);                             
    recordUl.appendChild(node); 
}

function startTimer () {
    mseconds++; 
    if(mseconds < 9){
        msecondsText.innerHTML = "0" + mseconds;
    }
    if (mseconds > 9){
        msecondsText.innerHTML = mseconds;
    } 
    if (mseconds > 99) {
        seconds++;
        secondsText.innerHTML = "0" + seconds;
        mseconds = 0;
        mseconds.innerHTML = "0" + 0;
    }
    if (seconds > 9){
        secondsText.innerHTML = seconds;
    }
    if (seconds > 59){
        minutes++;
        minutesText.innerHTML = "0" + minutesText;
        seconds = 0;
        seconds.innerHTML = "0" + 0;
    }    
}