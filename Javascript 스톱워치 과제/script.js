let timeBegan = null
    , timeStopped = null
    , stoppedDuration = 0
    , started = null;

function start() {
    if (timeBegan === null) {
        timeBegan = new Date();
    }

    if (timeStopped !== null) {
        stoppedDuration += (new Date() - timeStopped);
    }
 

    started = setInterval(clockRunning, 10);	
}

function stop() {
    timeStopped = new Date();
 
    let recordtime = document.querySelector(".watch").innerHTML;
    const boxbox = document.querySelector(".record-ul");
    boxbox.insertAdjacentHTML('beforeend', createHTMLString(recordtime));

    clearInterval(started);
}

function createHTMLString(recordtime){
    return `
<li class="record-li record-row">

    <div class="check">
        <input type="checkbox" class="check-radio radd">
    </div>

    <div>${recordtime}</div>
    <div> </div>

</li>
    `;
}



function reset() {
    clearInterval(started);
    stoppedDuration = 0;
    timeBegan = null;
    timeStopped = null;
    document.querySelector(".watch").innerHTML = "00 : 00";
}

function clockRunning(){
    var currentTime = new Date()
        , timeElapsed = new Date(currentTime - timeBegan - stoppedDuration)
        , sec = timeElapsed.getUTCSeconds()
        , ms = timeElapsed.getUTCMilliseconds()%60;

    document.querySelector(".watch").innerHTML = 
        (sec > 9 ? sec : "0" + sec) + " : " + 
        (ms > 9 ? ms : "0" + ms);
};

const a = document.querySelector(".start");
const b = document.querySelector(".stop");
const c = document.querySelector(".reset");

a.addEventListener("click", start);
b.addEventListener('click', stop);
c.addEventListener('click', reset);


function allSelect(){
    let radios = document.querySelectorAll(".check-radio");
    let hh = document.querySelector(".check-radio-first");
    let ischecked = hh.checked;
    console.log(ischecked);

    if(ischecked){
        for ( let i = 0; i < radios.length; i++){
            radios[i].checked = true;
        }
    }
    else{
        for ( let i = 0; i < radios.length; i++){
            radios[i].checked = false;
        }
    }
}



const d = document.querySelector(".check-radio-first");
d.addEventListener("click", allSelect);


function deleteRadio(){
    let radios = document.querySelectorAll(".check-radio");
    for ( let i = 0; i < radios.length; i++){
        if(radios[i].checked){
            radios[i].parentNode.parentNode.remove();
        }
    }

}

const trash = document.querySelector(".trash");
trash.addEventListener("click", deleteRadio);


//라디오 누르면 선택 취소되는 것과 delete 기능 구현