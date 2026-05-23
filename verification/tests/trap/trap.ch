% Change file for TRAP test (Metafont 2.718)
% Derived from trapman.tex Appendix A

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [1.7] debug..gubed, stat..tats
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d debug==@{ {change this to `$\\{debug}\equiv\null$' when debugging}
@d gubed==@t@>@} {change this to `$\\{gubed}\equiv\null$' when debugging}
@y
@d debug==
@d gubed==
@z
@x
@d stat==@{ {change this to `$\\{stat}\equiv\null$' when gathering
  usage statistics}
@d tats==@t@>@} {change this to `$\\{tats}\equiv\null$' when gathering
  usage statistics}
@y
@d stat==
@d tats==
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [1.8] init..tini
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d init== {change this to `$\\{init}\equiv\.{@@\{}$' in the production version}
@d tini== {change this to `$\\{tini}\equiv\.{@@\}}$' in the production version}
@y
@d init==
@d tini==
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [1.11] compile-time constants for TRAP
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@!mem_max=30000; {greatest index in \MF's internal |mem| array;
  must be strictly less than |max_halfword|;
  must be equal to |mem_top| in \.{INIMF}, otherwise |>=mem_top|}
@!max_internal=100; {maximum number of internal quantities}
@!buf_size=500; {maximum number of characters simultaneously present in
  current lines of open files; must not exceed |max_halfword|}
@!error_line=72; {width of context lines on terminal error messages}
@!half_error_line=42; {width of first lines of contexts in terminal
  error messages; should be between 30 and |error_line-15|}
@!max_print_line=79; {width of longest text lines output; should be at least 60}
@!screen_width=768; {number of pixels in each row of screen display}
@!screen_depth=1024; {number of pixels in each column of screen display}
@y
@!mem_max=3000; {greatest index in \MF's internal |mem| array;
  must be strictly less than |max_halfword|;
  must be equal to |mem_top| in \.{INIMF}, otherwise |>=mem_top|}
@!max_internal=100; {maximum number of internal quantities}
@!buf_size=500; {maximum number of characters simultaneously present in
  current lines of open files; must not exceed |max_halfword|}
@!error_line=64; {width of context lines on terminal error messages}
@!half_error_line=32; {width of first lines of contexts in terminal
  error messages; should be between 30 and |error_line-15|}
@!max_print_line=72; {width of longest text lines output; should be at least 60}
@!screen_width=100; {number of pixels in each row of screen display}
@!screen_depth=200; {number of pixels in each column of screen display}
@z
@x
@!gf_buf_size=800; {size of the output buffer, must be a multiple of 8}
@y
@!gf_buf_size=8; {size of the output buffer, must be a multiple of 8}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [1.12] sensitive compile-time constants for TRAP
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@d mem_top==30000 {largest index in the |mem| array dumped by \.{INIMF};
  must be substantially larger than |mem_min|
  and not greater than |mem_max|}
@y
@d mem_top==3000 {largest index in the |mem| array dumped by \.{INIMF};
  must be substantially larger than |mem_min|
  and not greater than |mem_max|}
@z

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [27.564] init_screen logging
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@x
@p function init_screen:boolean;
begin init_screen:=false;
end;
@y
@p function init_screen:boolean;
begin init_screen:=true;
end;
@z
