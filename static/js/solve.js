document.addEventListener('DOMContentLoaded', () => {

document.getElementById('solve').addEventListener("click", function(e){
    document.getElementById('solve').disabled = true;
    btns = document.getElementsByClassName("tile");
    for (var i = 0; i < btns.length; i++) {
        btns[i].disabled = true;
    }
    e.preventDefault()
    let array = [0];
    for(let i = 1; i<=16; i++)
    {
        array.push(parseInt(document.querySelector(`#t${i}`).textContent))
    }
    let myJSON = JSON.stringify(array)
    $.getJSON(`/solve/${myJSON}`,
        function(data) {
            
    console.log(data)
    swap(data, 1)

    });
    
    clearInterval(Interval);
    document.getElementById('reload').style.visibility = "visible"
    return false;

});

});

function swap(sequence, i) {

       

    setTimeout(function() {
        document.querySelector(`#t${sequence[i-1]}`).textContent = document.querySelector(`#t${sequence[i]}`).textContent
        document.querySelector(`#t${sequence[i]}`).textContent = "_"
        document.querySelector(`#t${sequence[i-1]}`).style.visibility = "visible"
        document.querySelector(`#t${sequence[i]}`).style.visibility = "hidden"
        counter++
        document.getElementById("moves").innerHTML = `Moves: ${counter}`;
        i++;              
        if (i < sequence.length) {          
          swap(sequence, i);            
        }                       
      }, 250)

}