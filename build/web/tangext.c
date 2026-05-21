#include "FPCTypes.h"

#define BUF_SIZE 500
#define max_file_name_length 60

unsigned char Buffer[BUF_SIZE+1];
unsigned char Xord[256];
unsigned char Xchr[256];
int Limit;

int _p_argc;
char **_p_argv;

void Argv(int n, char* str)
{
    if (n < 0 || n >= _p_argc) {
        str[0] = '\0';
        return;
    }
    strncpy(str, _p_argv[n], max_file_name_length);
    str[max_file_name_length-1] = '\0';
}

void Flushstdout()
{
    fflush(stdout);
}

void Lineread(FILE **f)
{
    FILE *iop = *f;
    int c;
    unsigned char *cs = &Buffer[0];
    unsigned char *cnb = &Buffer[0];
    int l = BUF_SIZE;

    while ((--l >= 0) && ((c = getc(iop)) != EOF) && (c != '\n')) {
        if ((*cs++ = Xord[c]) != ' ')
            cnb = cs;
    }
    Limit = (cnb - &Buffer[0]);
}

bool Testeof(FILE **f)
{
    FILE *iop = *f;
    int c = getc(iop);
    if (c == EOF) return TRUE;
    ungetc(c, iop);
    return FALSE;
}

void Exit(int c)
{
    exit(c);
}
