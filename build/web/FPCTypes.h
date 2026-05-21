#ifndef FPC_TYPES_H
#define FPC_TYPES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {FALSE, TRUE} bool;

/* FPC's text file structure is different from GPC's FDR.
   We will pass the FILE pointer directly or use a simplified structure.
   For now, let's redefine FDR to be something we can use. */

typedef struct Fdr {
    FILE *FilJfn;
    int FilSta;
} *FDR;

#define FiEof (1 << 2)

/* FPC strings are different, but tangle.p-edited uses UNIXfilename which is packed array of char */

extern int _p_argc;
extern char **_p_argv;

#endif
