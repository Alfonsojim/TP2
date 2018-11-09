# Sports


Sports is a simple application created as a class project. This application first shows a form with a list of values ​​and then a second form to identify the user. In future versions it will save the data in a Redis database.

  The project has two parts. The first uses the project apache and the interpreter perl for its execution. The second part requires the apache project, the interpreter perl and also the CGI module.
  
### Installation

Sports requires:
[Apache](https://httpd.apache.org) Stable Release 2.4.37.
Activate module [dynamic content cgi](https://httpd.apache.org/docs/trunk/es/howto/cgi.html) 
Install cgi library [cpan  cgi](https://metacpan.org/pod/release/MARKSTOS/CGI.pm-3.63/lib/CGI.pm)

To execute the first part of the project we need to copy deporte. pl and deportes.txt in the cgi-bin folder.
We go to the web client and write the address localhost / cgi-bin / deportes. pl

To execute the second part of the project we need to copy sport. cgi in the cgi-bin folder.
We go to the web client and write the address localhost / cgi-bin / sports. cgi


