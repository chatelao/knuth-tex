%  Change file for the GFtoDVI processor, for use with GNU Pascal
%  (by Don Knuth; see ../mfware-sparc for the prehistory)

% History:
% 2000.04.30 Original version

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [0] WEAVE: print changes only
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
\pageno=\contentspagenumber \advance\pageno by 1
@y
\pageno=\contentspagenumber \advance\pageno by 1
\let\maybe=\iffalse
\def\title{GF\lowercase{to}DVI changes for {\mc GNU} Pascal}
@z
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [1] Change banner string
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d banner=='This is GFtoDVI, Version 3.0' {printed when the program starts}
@y
@d banner=='This is GFtoDVI, Version 3.0 for Linux'
                                          {printed when the program starts}
@z
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [2] Use default case statement feature of ISO Extended Pascal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d othercases == others: {default for cases not listed explicitly}
@y
@d othercases == otherwise {default for cases not listed explicitly}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [3] Add inclusion of ext.h and standard input to program header
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@p program GF_to_DVI(@!output);
label @<Labels in the outer block@>@/
const @<Constants in the outer block@>@/
type @<Types in the outer block@>@/
var @<Globals in the outer block@>@/
procedure initialize; {this procedure gets things started properly}
  var @!i,@!j,@!m,@!n:integer; {loop indices for initializations}
  begin print_ln(banner);@/
  @<Set initial values@>@/
  end;
@y
@p program GF_to_DVI(@!input,@!output);
label @<Labels in the outer block@>@/
const @<Constants in the outer block@>@/
type UNIX_filename = packed array [1..1024] of char;
@<Types in the outer block@>@/
var @<Globals in the outer block@>@/
@\@=#include "../tex/ext.h"@>@\ {declarations for external C procedures}
procedure initialize; {this procedure gets things started properly}
  var @!i,@!j,@!m,@!n:integer; {loop indices for initializations}
  begin print_ln(banner);@/
  @<Set initial values@>@/
  first_input:=true;
  end;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [5] Enlarge file_name_size to 1024
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@<Constants...@>=
@!max_labels=2000; {maximum number of labels and dots and rules per character}
@!pool_size=10000; {maximum total length of labels and other strings}
@!max_strings=1100; {maximum number of labels and other strings}
@!terminal_line_length=150; {maximum number of characters input in a single
  line of input from the terminal}
@!file_name_size=50; {a file name shouldn't be longer than this}
@!font_mem_size=2000; {space for font metric data}
@!dvi_buf_size=800; {size of the output buffer; must be a multiple of 8}
@!widest_row=8192; {maximum number of pixels per row}
@!lig_lookahead=20; {size of stack used when inserting ligature characters}
@y
@<Constants...@>=
@!max_labels=2000; {maximum number of labels and dots per character}
@!pool_size=10000; {maximum total length of labels and other strings}
@!max_strings=1100; {maximum number of labels and other strings}
@!terminal_line_length=150; {maximum number of characters input in a single
  line of input from the terminal}
@!file_name_size=1024; {a file name shouldn't be longer than this}
@!font_mem_size=2000; {space for font metric data}
@!dvi_buf_size=800; {size of the output buffer; must be a multiple of 8}
@!widest_row=8192; {maximum number of pixels per row}
@!lig_lookahead=20; {size of stack used when inserting ligature characters}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [8] Add <nl> to end of abort() message
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d abort(#)==@+begin print(' ',#); jump_out;@+end
@y
@d abort(#)==@+begin print_ln(' ',#); jump_out;@+end
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [was15,now16] change update_terminal to flush(), change def'n of term_in
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
Since the terminal is being used for both input and output, some systems
need a special routine to make sure that the user can see a prompt message
before waiting for input based on that message. (Otherwise the message
may just be sitting in a hidden buffer somewhere, and the user will have
no idea what the program is waiting for.) We shall call a system-dependent
subroutine |update_terminal| in order to avoid this problem.

@d update_terminal == break(output) {empty the terminal output buffer}

@<Glob...@>=
@!buffer:array[0..terminal_line_length] of 0..255;
@!term_in:text_file; {the terminal, considered as an input file}
@y
Since the terminal is being used for both input and output, some systems
need a special routine to make sure that the user can see a prompt message
before waiting for input based on that message. (Otherwise the message
may just be sitting in a hidden buffer somewhere, and the user will have
no idea what the program is waiting for.) We shall call a system-dependent
subroutine |update_terminal| in order to avoid this problem.
@^system dependencies@>

@d update_terminal == flush_stdout {empty the terminal output buffer}
@d term_in == input {standard input}

@<Glob...@>=
@!buffer:array[0..terminal_line_length] of ByteCard;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [was16,now17] Remove reset(term_in) from input_ln
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@ A global variable |line_length| records the first buffer position after
the line just read.
@^system dependencies@>

@p procedure input_ln; {inputs a line from the terminal}
begin update_terminal; reset(term_in);
if eoln(term_in) then read_ln(term_in);
line_length:=0;
while (line_length<terminal_line_length)and not eoln(term_in) do
  begin buffer[line_length]:=xord[term_in^]; incr(line_length); get(term_in);
  end;
end;

@y
@ A global variable |line_length| records the first buffer position after
the line just read. Another one, |first_input|, tells if such a line exists.
@^system dependencies@>

@p procedure input_ln; {inputs a line from the terminal}
begin update_terminal;
if first_input then first_input:=false
else if eoln(term_in) then read_ln(term_in);
line_length:=0;
while (line_length<terminal_line_length)and not eoln(term_in) do
  begin buffer[line_length]:=xord[term_in^]; incr(line_length); get(term_in);
  end;
end;

@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [45] Change type of binary file for binary (byte) files
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@!eight_bits=0..255; {unsigned one-byte quantity}
@y
@!eight_bits=ByteCard; {unsigned one-byte quantity}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [47] Modify file open routines to match binary I/O library
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
variable that specifies the file name.
@^system dependencies@>

@p procedure open_gf_file; {prepares to read packed bytes in |gf_file|}
begin reset(gf_file,name_of_file);
cur_loc:=0;
end;
@#
procedure open_tfm_file; {prepares to read packed bytes in |tfm_file|}
begin reset(tfm_file,name_of_file);
end;
@#
procedure open_dvi_file; {prepares to write packed bytes in |dvi_file|}
begin rewrite(dvi_file,name_of_file);
end;
@y
variable that specifies the file name.

An external C procedure, |test_access| is used to check whether or not the
open will work.  It is declared in the \.{ext.h} include file, and it returns
|true| or |false|. The |name_of_file| global holds the file name whose access
is to be tested.
The first parameter for |test_access| is the access mode,
one of |read_access_mode| or |write_access_mode|.

We also implement path searching in |test_access|:  its second parameter is
one of the ``file path'' constants defined below.  If |name_of_file|
doesn't start with |'/'| then |test_access| tries prepending pathnames
from the appropriate path list until success or the end of path list
is reached.
On return, |real_name_of_file| contains the original name with the path
that succeeded (if any) prepended.  It is the name used in the various
open procedures.

@d read_access_mode=4  {``read'' mode for |test_access|}
@d write_access_mode=2 {``write'' mode for |test_access|}

@d no_file_path=0 {do no path searching}
@d font_file_path=3 {path specifier for \.{TFM} files}

@p procedure open_gf_file; {prepares to read packed bytes in |gf_file|}
var@!i: 1..file_name_size;
begin if test_access(read_access_mode,no_file_path) then
  begin reset(gf_file,real_name_of_file); cur_loc:=0;
  end
else begin i:=1;
  while (real_name_of_file[i] <> chr(0)) do@+incr(i);
  abort('Can''t open GF file ',real_name_of_file:i);
  end;
end;
@#
procedure open_tfm_file; {prepares to read packed bytes in |tfm_file|}
var@!i: 1..file_name_size;
begin if test_access(read_access_mode,font_file_path) then
  begin reset(tfm_file,real_name_of_file); cur_loc:=0;
  end
else begin i:=1;
  while (real_name_of_file[i] <> chr(0)) do@+incr(i);
  abort('Can''t open TFM file ',real_name_of_file:i);
  end;
end;
@#
procedure open_dvi_file; {prepares to write packed bytes in |dvi_file|}
var@!i: 1..file_name_size;
begin if test_access(write_access_mode,no_file_path) then
  rewrite(dvi_file,real_name_of_file)
else begin i:=1;
  while (real_name_of_file[i] <> chr(0)) do@+incr(i);
  abort('Can''t write on DVI file ',real_name_of_file:i);
  end;
end;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [48] Declare real_name_of_file
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
be read next, and the string |name_of_file| will be set to the current
file name before the file-opening procedures are called.

@<Glob...@>=
@!cur_loc:integer; {current byte number in |gf_file|}
@!name_of_file:packed array[1..file_name_size] of char; {external file name}
@y
be read next, and the string |name_of_file| will be set to the current
file name before the file-opening procedures are called.
Under UNIX, we also have a |real_name_of_file| string, that gets
set by the external |test_access| procedure after path searching.

@<Glob...@>=
@!cur_loc:integer; {current byte number in |gf_file|}
@!name_of_file,@!real_name_of_file:external UNIX_filename;
	 {external names}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [78] change default extension to ".2602gf"
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
l:=3; init_str3(".")("g")("f")(gf_ext);@/
@y
l:=7; init_str7(".")("2")("6")("0")("2")("g")("f")(gf_ext);@/
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [87] change ">" and ":" to "/" in file name scanning
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@ The file names we shall deal with for illustrative purposes have the
following structure:  If the name contains `\.>' or `\.:', the file area
consists of all characters up to and including the final such character;
otherwise the file area is null.  If the remaining file name contains
`\..', the file extension consists of all such characters from the first
remaining `\..' to the end, otherwise the file extension is null.
@^system dependencies@>

We can scan such file names easily by using two global variables that keep track
of the occurrences of area and extension delimiters:

@<Glob...@>=
@!area_delimiter:pool_pointer; {the most recent `\.>' or `\.:', if any}
@!ext_delimiter:pool_pointer; {the relevant `\..', if any}
@y
@ The file names we shall deal with for Linux have the
following structure:  If the name contains `\./', the file area
consists of all characters up to and including the final such character;
otherwise the file area is null.  If the remaining file name contains
`\..', the file extension consists of all such characters from the first
remaining `\..' to the end, otherwise the file extension is null.
@^system dependencies@>

We can scan such file names easily by using two global variables that keep track
of the occurrences of area and extension delimiters:

@<Glob...@>=
@!area_delimiter:pool_pointer; {the most recent `\./', if any}
@!ext_delimiter:pool_pointer; {the relevant `\..', if any}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [88] change home_font_area to null_string (open_tfm provides path)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@ Font metric files whose areas are not given
explicitly are assumed to appear in a standard system area called
|home_font_area|.  This system area name will, of course, vary from place
to place. The program here sets it to `\.{TeXfonts:}'.
@^system dependencies@>
@.TeXfonts@>

@<Initialize the strings@>=
l:=9; init_str9("T")("e")("X")("f")("o")("n")("t")("s")(":")(home_font_area);@/
@y
@ Font metric files whose areas are not given
explicitly are assumed to appear in a standard system area called
|home_font_area|.  This system area name will, of course, vary from place
to place. In the Linux version, we set |home_font_area|
to |null_string| because the default areas to search for \.{TFM} files
are built into the routine |test_access|.
@^system dependencies@>

@<Initialize the strings@>=
l:=0; init_str0(home_font_area);@/
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [90] change more_name to understand UNIX file name paths
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@p function more_name(@!c:ASCII_code):boolean;
begin if c=" " then more_name:=false
else  begin if (c=">")or(c=":") then
    begin area_delimiter:=pool_ptr; ext_delimiter:=0;
    end
  else if (c=".")and(ext_delimiter=0) then ext_delimiter:=pool_ptr;
  str_room(1); append_char(c); {contribute |c| to the current string}
  more_name:=true;
  end;
end;
@y
@p function more_name(@!c:ASCII_code):boolean;
begin if c=" " then more_name:=false
else  begin if (c="/") then
    begin area_delimiter:=pool_ptr; ext_delimiter:=0;
    end
  else if (c=".")and(ext_delimiter=0) then ext_delimiter:=pool_ptr;
  str_room(1); append_char(c); {contribute |c| to the current string}
  more_name:=true;
  end;
end;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [92] change pack_file_name for UNIX conventions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
if k<=file_name_size then name_length:=k@+else name_length:=file_name_size;
for k:=name_length+1 to file_name_size do name_of_file[k]:=' ';
end;
@y
if k<file_name_size then name_length:=k@+else name_length:=file_name_size-1;
for k:=name_length+1 to file_name_size do name_of_file[k]:=chr(0);
end;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [94] change start_gf to get file name from command line arguments
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@ The |start_gf| procedure prompts the user for the name of the generic
font file to be input. It opens the file, making sure that some input is
present; then it opens the output file.

Although this routine is system-independent, it should probably be
modified to take the file name from the command line (without an initial
prompt), on systems that permit such things.

@p procedure start_gf;
label found,done;
begin loop@+begin print_nl('GF file name: '); input_ln;
@.GF file name@>
  buf_ptr:=0; buffer[line_length]:="?";
  while buffer[buf_ptr]=" " do incr(buf_ptr);
  if buf_ptr<line_length then
    begin @<Scan the file name in the buffer@>;
    if cur_ext=null_string then cur_ext:=gf_ext;
    pack_file_name(cur_name,cur_area,cur_ext); open_gf_file;
    if not eof(gf_file) then goto found;
    print_nl('Oops... I can''t find file '); print(name_of_file);
@.Oops...@>
@.I can't find...@>
    end;
  end;
found:job_name:=cur_name; pack_file_name(job_name,null_string,dvi_ext);
open_dvi_file;
end;
@y
@ The |start_gf| procedure obtains the name of the generic font file to
be input from the command line.
It opens the file, making sure that some input is
present; then it opens the output file.

@p procedure start_gf;
label done;
var
    arg_buffer: UNIX_filename;
    arg_buf_ptr: 1..file_name_size;
begin if (argc > 2) then abort('Usage: gftodvi [GF-file]');
if argc = 1 then begin
    print_nl('GF file name: '); input_ln;
@.GF file name@>
    end
else begin
    argv(1, arg_buffer);
    arg_buf_ptr := 1;
    line_length := 0;
    while (arg_buf_ptr < file_name_size)
    and (line_length < terminal_line_length)
    and (arg_buffer[arg_buf_ptr] <> chr(0)) do
    begin
        buffer[line_length] := xord[arg_buffer[arg_buf_ptr]];
        incr(line_length);
        incr(arg_buf_ptr);
    end;
end;
  buf_ptr:=0; buffer[line_length]:="?";
  while buffer[buf_ptr]=" " do incr(buf_ptr);
  if buf_ptr<line_length then
    begin @<Scan the file name in the buffer@>;
    if cur_ext=null_string then cur_ext:=gf_ext;
    pack_file_name(cur_name,cur_area,cur_ext); open_gf_file;
    end;
job_name:=cur_name; pack_file_name(job_name,null_string,dvi_ext);
open_dvi_file;
end;
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [was216,now219] call set_paths before gf_start to initialize paths
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@p begin initialize; {get all variables initialized}
@<Initialize the strings@>;
start_gf; {open the input and output files}
@y
@p begin initialize; {get all variables initialized}
@<Initialize the strings@>;
set_paths;  {initialize paths for \.{TFM} files from environment if needed}
start_gf; {open the input and output files}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [was216,now219] finish normal end with newline on terminal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
  cur_gf:=get_byte; str_ptr:=init_str_ptr; pool_ptr:=str_start[str_ptr];
  end;
final_end:end.
@y
  cur_gf:=get_byte; str_ptr:=init_str_ptr; pool_ptr:=str_start[str_ptr];
  end;
final_end:print_ln(' ');
end.
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [was219,now222] declare special global
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@* System-dependent changes.
This section should be replaced, if necessary, by changes to the program
that are necessary to make \.{GFtoDVI} work at a particular installation.
It is usually best to design your change file so that all changes to
previous sections preserve the section numbering; then everybody's version
will be consistent with the printed program. More extensive changes,
which introduce new sections, can be inserted here; then only the index
itself will get a new section number.
@^system dependencies@>
@y
@* System-dependent changes.
This section should be replaced, if necessary, by changes to the program
that are necessary to make \.{GFtoDVI} work at a particular installation.
It is usually best to design your change file so that all changes to
previous sections preserve the section numbering; then everybody's version
will be consistent with the printed program. More extensive changes,
which introduce new sections, can be inserted here; then only the index
itself will get a new section number.
@^system dependencies@>

@<Glob...@>=
@!first_input:boolean; {true before the first call to |input_ln|}

@ @<Types in...@>=
@!word_file=file of memory_word; {needed in \.{ext.h}}
@z
