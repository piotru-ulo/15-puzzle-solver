
var Interval;
let time = 0;

function shuffle(){

    clearInterval(Interval);
    Interval = setInterval(function () {
        time++;
        document.getElementById("timer").innerHTML = `Time: ${time}s`;
    }, 1000);

    let where = 16;
    for(let i=0; i<1000; i++)
    {
        let r;
        while(true)
        {
            r = Math.floor(Math.random() * 4);
            if(r == 0 && where>4)
            {
                document.querySelector(`#t${where}`).textContent = document.querySelector(`#t${where-4}`).textContent;
                document.querySelector(`#t${where-4}`).textContent = "_";
                where = where - 4;
                break;
            }
            else if(r==1 && where%4!=0)
            {
                document.querySelector(`#t${where}`).textContent = document.querySelector(`#t${where+1}`).textContent;
                document.querySelector(`#t${where+1}`).textContent = "_";
                where = where + 1;
                break;
            }
            else if(r==2 && where<13)
            {
                document.querySelector(`#t${where}`).textContent = document.querySelector(`#t${where+4}`).textContent;
                document.querySelector(`#t${where+4}`).textContent = "_";
                where = where + 4;
                break;
            }
            else if(r==3 && (where-1)%4!=0)
            {
                document.querySelector(`#t${where}`).textContent = document.querySelector(`#t${where-1}`).textContent;
                document.querySelector(`#t${where-1}`).textContent = "_";
                where = where - 1;
                break;
            }
        }
    }
    document.querySelector(`#t${where}`).style.visibility = "hidden";

}

let counter = 0;

document.addEventListener('DOMContentLoaded', () => {
    
    btns = document.getElementsByClassName("tile");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        
        let secondTile = null;
        let tileNum = parseInt(this.id.slice(1), 10);
        
        if(tileNum%4 != 0 && document.querySelector(`#t${tileNum + 1}`).textContent == "_")
            secondTile = tileNum + 1;
        if((tileNum - 1)%4 != 0 && document.querySelector(`#t${tileNum - 1}`).textContent == "_")
            secondTile = tileNum -1 ;
        if((tileNum +4) <=16 && document.querySelector(`#t${tileNum + 4}`).textContent == "_")
            secondTile = tileNum + 4 ;
        if((tileNum -4) >=1 && document.querySelector(`#t${tileNum - 4}`).textContent == "_")
                secondTile = tileNum - 4 ;
        if(secondTile == null)
            return false;
        document.querySelector(`#t${secondTile}`).textContent = `${this.textContent}`;
        document.querySelector(`#t${secondTile}`).style.visibility = "visible";
        this.textContent = "_";
        this.style.visibility = "hidden";
        
        counter++;
        document.getElementById("moves").innerHTML = `Moves: ${counter}`;

        for(let i=1; i<=15; i++)
        {
            if(parseInt(document.querySelector(`#t${i}`).textContent, 10) != i)
                return false;

        }

        clearInterval(Interval);
        swal(`Good Job!
        moves: ${counter}
        time: ${time}s`);
        btns = document.getElementsByClassName("tile");
        for (var i = 0; i < btns.length; i++) {
            btns[i].disabled = true;
        }

        return true;

    });
}

});
