#!/usr/bin/perl
#
#  PROGRAM:	scrolling_list.cgi
#
#  PURPOSE:	Demonstrate (1) how to create a scrolling_list form and
#		(2) how to determine the value(s) selected by the user.
#
#  Created by alvin alexander, devdaily.com.
#

#-----------------------------------#
#  1. Create a new Perl CGI object  #
#-----------------------------------#

use CGI;
use utf8;
$query = new CGI;


#----------------------------------#
#  2. Print the doctype statement  #
#----------------------------------#

print $query->header(-charset=>'utf8');


#----------------------------------------------------#
#  3. Start the HTML doc, and give the page a title  #
#----------------------------------------------------#

print $query->start_html('My first CGI program');


#------------------------------------------------------------#
#  4a.  If the program is called without any params, print   #
#       the scrolling_list form.                             #
#------------------------------------------------------------#

if (!$query->param) {

	print $query->start_form;
	print $query->h3('Select your favorite sport:');
	print $query->scrolling_list(-name=>'sport',
				 -values=>[
					   'Football',
					   'Tennis',
					   'Basketball',
					   'Swimming'],
				 -size=>8,
				 -multiple=>'true',
				 -default=>'Perl');

	# Notes:
	# ------
	#	"-multiple=>'true'" lets the user make multiple selections
	#		from the scrolling_list
	#	"-default" is optional
	#	"-size" lets you specify the number of visible rows in the list
	#	can also use an optional "-labels" parameter to let the user
	#		see labels you want them to see, while you use
	#		different names for each parameter in your program
	
	print $query->br;
	print $query->submit(-value=>'Submit your favorite sport');
	print $query->endform;

} 
	#----------------------------------------------------------#
	#  4b.  If the program is called with parameters, retrieve #
	#  the 'languages' parameter, assign it to an array        #
	#  named $languages, then print the array with each        #
	#  name separated by a <BR> tag.                           #
	#----------------------------------------------------------#
if ($query->param('sport')) {
	print $query->h3('Your favorite sport are:');
	$sports = $query->param('sport');
#	print "<BLOCKQUOTE>\n";
	#foreach $sport (@sports) {
		print "$sports<BR>";
#	}
#	print "</BLOCKQUOTE>\n"

        print $query->start_form;
        print $query->h1('¿What is your name?');
        print $query->textfield(-name=>'nombre');
      	print $query->submit;
        print $query->end_form;
        print $query->br;
}
if ($query->param('nombre')) {
	print $query->h3('Your name is:');
	$nombre = $query->param('nombre');
        print "$nombre<BR>";
}


#--------------------------------------------------#
#  5. After either case above, end the HTML page.  #
#--------------------------------------------------#

print $query->end_html;
