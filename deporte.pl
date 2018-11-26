#!/usr/bin/perl
print "Content-Type: text/html; charset=utf-8\n\n";
if($ENV{'QUERY_STRING'} eq "") {
   print "<h1>Elige un deporte</h1>
          <form name=\"search\" method=\"get\" >";
   open F, "deportes.txt";
   while(<F>) {
     chomp;
     @campos=split(":");
     $ar{$campos[1]}=$campos[1];
   }
   print "<select name = \"shell\">";
   for  (keys %ar){
     print "<option value=$_";
     print ">$_</option>";
   }
   print "</select>
         <input type=\"submit\" value=\"Search\" />";
}

if($ENV{'QUERY_STRING'} ne "") {
   @arGet=split("=",$ENV{'QUERY_STRING'});
   if (@arGet[0] eq "shell"){
   $arGet[1]=~ s/%2F/\//g;
   print "Elegiste $arGet[1]<br><br><i>Felicidades!</i> <br></br>";
   print "<i>Dime tu nombre</i><br></br>";
   print "<form name=\"nombre\" method=\"get\" >";
   print "<input type=\"text\" name=\"nombre\" >";
   print "<input type=\"submit\" value=\"enviar\" >";

}
}
   if (@arGet[0] eq "nombre"){
   $arGet[1]=~ s/%2F/\//g;
   print "Tu nombre es $arGet[1]<br><br>";
}

