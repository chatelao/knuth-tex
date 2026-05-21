{2:}{4:}{:4}program TANGLE(input,output);label 9999;
const{8:}bufsize=100;maxbytes=45000;maxtoks=50000;maxnames=4000;
maxtexts=2000;hashsize=353;longestname=400;linelength=72;outbufsize=144;
stacksize=50;maxidlength=50;unambiglength=7;{:8}type{11:}
ASCIIcode=integer(8);{:11}{12:}textfile=packed file of char;{:12}{37:}
eightbits=0..255;sixteenbits=0..65535;{:37}{39:}namepointer=0..maxnames;
UNIXfilename=packed array[1..60] of char;
{:39}{43:}textpointer=0..maxtexts;{:43}{78:}
outputstate=record endfield:sixteenbits;bytefield:sixteenbits;
namefield:namepointer;replfield:textpointer;modfield:0..12287;end;{:78}
var{9:}history:0..3;{:9}{13:}xord:array[char]of ASCIIcode;
xchr:array[ASCIIcode]of char;{:13}{23:}webfile:textfile;
changefile:textfile;{:23}{25:}Pascalfile:textfile;pool:textfile;{:25}
{27:}buffer:array[0..bufsize]of ASCIIcode;{:27}{29:}phaseone:boolean;
{:29}{38:}bytemem:packed array[0..2,0..maxbytes]of ASCIIcode;
tokmem:packed array[0..3,0..maxtoks]of eightbits;
bytestart:array[0..maxnames]of sixteenbits;
tokstart:array[0..maxtexts]of sixteenbits;
link:array[0..maxnames]of sixteenbits;
ilk:array[0..maxnames]of sixteenbits;
equiv:array[0..maxnames]of sixteenbits;
textlink:array[0..maxtexts]of sixteenbits;{:38}{40:}nameptr:namepointer;
stringptr:namepointer;byteptr:array[0..2]of 0..maxbytes;
poolchecksum:integer;{:40}{44:}textptr:textpointer;
tokptr:array[0..3]of 0..maxtoks;z:0..3;
{maxtokptr:array[0..3]of 0..maxtoks;}{:44}{50:}idfirst:0..bufsize;
idloc:0..bufsize;doublechars:0..bufsize;
hash,chophash:array[0..hashsize]of sixteenbits;
choppedid:array[0..unambiglength]of ASCIIcode;{:50}{65:}
modtext:array[0..longestname]of ASCIIcode;{:65}{70:}
lastunnamed:textpointer;{:70}{79:}curstate:outputstate;
stack:array[1..stacksize]of outputstate;stackptr:0..stacksize;{:79}{80:}
zo:0..3;{:80}{82:}bracelevel:eightbits;{:82}{86:}curval:integer;{:86}
{94:}outbuf:array[0..outbufsize]of ASCIIcode;outptr:0..outbufsize;
breakptr:0..outbufsize;semiptr:0..outbufsize;{:94}{95:}
outstate:eightbits;outval,outapp:integer;outsign:ASCIIcode;
lastsign:-1..+1;{:95}{100:}outcontrib:array[1..linelength]of ASCIIcode;
{:100}{124:}ii:integer;line:integer;otherline:integer;templine:integer;
limit:0..bufsize;loc:0..bufsize;inputhasended:boolean;changing:boolean;
{:124}{126:}changebuffer:array[0..bufsize]of ASCIIcode;
changelimit:0..bufsize;{:126}{143:}curmodule:namepointer;
scanninghex:boolean;{:143}{156:}nextcontrol:eightbits;{:156}{164:}
currepltext:textpointer;{:164}{171:}modulecount:0..12287;{:171}{179:}
{troubleshooting:boolean;ddt:integer;dd:integer;debugcycle:integer;
debugskipped:integer;}{:179}{185:}{wo:0..2;}{:185}{189:}
webname,changename,Pascalname,poolname:UNIXfilename;{:189}
#include "tangext.h"
{30:}{procedure debughelp;forward;}{:30}{31:}procedure error;
var j:0..outbufsize;k,l:0..bufsize;begin if phaseone then{32:}
begin if changing then write(output,'. (change file ')else write(output,
begin end.
