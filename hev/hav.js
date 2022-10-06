function szamol()
{

    var indulo = document.getElementById("select1").value;
    var erkezo = document.getElementById("select2").value;

    var eredmeny= indulo-erkezo;
    

    if(erkezo = indulo){
        alert("hiba");
        
    }
    else{
        alert(Math.abs(eredmeny));
    }
}
