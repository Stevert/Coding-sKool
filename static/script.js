
function fs(){
 //   var s=start.toString();
  //  end= Date.now();
  //  var e=(end - start)/1000;
    str=document.getElementById("t2").value.trim();
    var n=str.length;
    var i,c=1;
    for(i=0;i<n;i++)
        {
            if((str[i]==" "||str[i]=="\n"||str[i]=="\n")&&str[i-1]!=" "&&str[i-1]=="\n"&&str[i-1]!="\t")
                c+=1;
        }
    //var rpm=c*60.00/e;
    //var aa=parseInt(rpm); 
    // document.getElementById("t3").value=aa.toString();
    document.getElementById("t4").value=c.toString();
    
}
