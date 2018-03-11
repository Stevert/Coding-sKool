function n(){
    str=document.getElementById("t2").value;
    var l=str.length;
    var i,er=0;
    end=Date.now();
    var e=(end-start)/1000;
    gw=parseInt((l/5)*60/e);
    for(i=0;i<l;i++){
        if(st[i]!=str[i]){      
            er+=1;}
    }
    nw=gw-parseInt(er*60/e);
    acc=nw/gw*100;
    if(nw<0){
        acc=0;
        nw=0;
    }
    document.getElementById("t3").value=nw.toString();
    document.getElementById("t5").value=er.toString();
    document.getElementById("t4").value=acc.toString();
    
}