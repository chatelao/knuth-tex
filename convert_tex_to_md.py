import re
import sys

def convert_tex_to_md(content):
    # 1. Strip TeX preamble and macro definitions (rough)
    # Remove lines starting with \def, \font, \newcount, \newdimen, \newskip, \chardef, \catcode, \let
    content = re.sub(r'(?m)^\\(def|font|newcount|newdimen|newskip|chardef|catcode|let|count|dimen|skip|newbox|newinsert|newif|hyphenation|message|pausing|errmessage|loop|if|fi|repeat|input|tracing|maxdepth|parindent|abovedisplayskip|belowdisplayskip|output|shipout|global|outer|pageno).*$', '', content)

    # 2. Strip comments (but not escaped %)
    content = re.sub(r'(?<!\\)%.*', '', content)

    # 3. Strip index entries
    # ^^|...|, ^^{...}, ^{...}, ^|...|
    content = re.sub(r'\^\^\|.*?\|', '', content)
    content = re.sub(r'\^\^\{.*?\}', '', content)
    content = re.sub(r'\^\{.*?\}', '', content)
    content = re.sub(r'\^\|.*?\|', '', content)

    # 4. Normalize TeX and MF logos and common macros
    content = content.replace(r'\TeX', 'TeX')
    content = content.replace(r'\MF', 'METAFONT')
    content = content.replace(r'\AmSTeX', 'AmSTeX')
    content = content.replace(r'\/', '')
    content = content.replace('~', ' ')

    # 5. Handle \beginchapter
    def repl_chapter(m):
        title = m.group(1).replace('\\\\', ' ').strip()
        # Clean up inner braces if any
        title = re.sub(r'\{|\}', '', title)
        return f"\n# {title}\n"
    content = re.sub(r'\\beginchapter\s+(.*?)(?=\n\n|\n\\pageno|\n\f|$)', repl_chapter, content, flags=re.DOTALL)

    # 6. Handle \beginsection and \subsection
    content = re.sub(r'\\beginsection\s+(.*?)\n', r'\n## \1\n\n', content)
    content = re.sub(r'\\subsection\s+(.*?)\.\s+', r'\n## \1\n\n', content)

    # 7. Handle \exercise and \answer
    content = re.sub(r'\\exercise', r'\n### Exercise\n', content)
    content = re.sub(r'\\answer', r'\n#### Answer\n', content)

    # 8. Handle \author
    content = re.sub(r'\\author\s+(.*?)\((.*?)\)', r'\n> --- \1 (\2)\n', content)

    # 9. Handle \begintt ... \endtt (verbatim blocks)
    content = re.sub(r'\\begintt(.*?)\\endtt', r'\n```\n\1\n```\n', content, flags=re.DOTALL)

    # 10. Handle |...| for inline verbatim (protecting it from later brace stripping)
    content = re.sub(r'\|(.*?)\|', r'`\1`', content)

    # 11. Handle items
    content = re.sub(r'\\itemitem\s*', r'    - ', content)
    content = re.sub(r'\\item\s*\\bull', r'- ', content)
    content = re.sub(r'\\item\s*', r'- ', content)
    content = re.sub(r'\\textindent\s*\\bull', r'- ', content)
    content = re.sub(r'\\textindent', r'- ', content)

    # 12. Handle formatting with braces (non-math)
    # We do this before general brace stripping
    content = re.sub(r'\{\\sl\s+(.*?)\}', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'\{\\it\s+(.*?)\}', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'\{\\bf\s+(.*?)\}', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'\{\\tt\s+(.*?)\}', r'`\1`', content, flags=re.DOTALL)
    content = re.sub(r'\{\\rm\s+(.*?)\}', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'\{\\sc\s+(.*?)\}', r'\1', content, flags=re.DOTALL) # Small caps to normal for MD

    # 13. Dangerous bend
    content = re.sub(r'\\danger', r'\n**[Dangerous Bend]** ', content)
    content = re.sub(r'\\ddanger', r'\n**[Double Dangerous Bend]** ', content)

    # 14. Syntactic quantity \<...>
    content = re.sub(r'\\<(.*?)>', r'*\1*', content)

    # 15. Display environments
    content = content.replace(r'\begindisplay', '\n\n> ')
    content = content.replace(r'\enddisplay', '\n\n')

    # 16. Clean up layout commands
    layout_cmds = [
        r'\\pageno=-?\d+', r'\\eject', r'\\null', r'\\vfill', r'\\bigskip',
        r'\\medskip', r'\\smallskip', r'\\noindent', r'\\par', r'\\hfill',
        r'\\break', r'\\strut', r'\\goodbreak', r'\\filbreak', r'\\vglue\s*\S+',
        r'\\hglue\s*\S+', r'\\centerline', r'\\leftline', r'\\rightline',
        r'\\line', r'\\hsize', r'\\vsize', r'\\baselineskip', r'\\parskip',
        r'\\topskip', r'\\hfil', r'\\vfil', r'\\hss', r'\\vss', r'\\unskip',
        r'\\enspace', r'\\quad', r'\\qquad', r'\\thinspace', r'\\negthinspace',
        r'\\leavevmode', r'\\hbox', r'\\vbox', r'\\vtop', r'\\halign', r'\\valign',
        r'\\crcr', r'\\cr', r'\\noalign', r'\\tabskip', r'\\setbox\d+', r'\\wd\d+',
        r'\\ht\d+', r'\\dp\d+', r'\\raise', r'\\lower', r'\\kern\s*[\d.-]+[a-z]+',
        r'\\vskip\s*[\d.-]+[a-z]+', r'\\hskip\s*[\d.-]+[a-z]+', r'\\char\'\d+',
        r'\\char\"\w+', r'\\char\d+', r'\\mathchardef', r'\\textfont\d+',
        r'\\scriptfont\d+', r'\\scriptscriptfont\d+', r'\\fam', r'\\skewchar',
        r'\\hyphenchar', r'\\magnification', r'\\magstep\d+', r'\\mag',
        r'\\titlepage', r'\\titlefont', r'\\auth', r'\\elevenbf', r'\\elevenit',
        r'\\elevenrm', r'\\eightpoint', r'\\ninepoint', r'\\tenpoint', r'\\sixrm',
        r'\\eightrm', r'\\ninerm', r'\\tenrm', r'\\rm', r'\\it', r'\\sl', r'\\bf',
        r'\\tt', r'\\sc', r'\\small', r'\\large', r'\\normalsize', r'\\relax',
        r'\\begingroup', r'\\endgroup', r'\\bgroup', r'\\egroup', r'\\today',
        r'\\folio', r'\\advance', r'\\by', r'\\multiply', r'\\divide', r'\\number'
    ]
    for cmd in layout_cmds:
        content = re.sub(cmd, '', content)

    # 17. Quotes
    content = content.replace('``', '"').replace("''", '"')
    content = content.replace('`', "'")

    # 18. SELECTIVE Brace cleanup
    # We want to remove braces that are just for grouping text,
    # but keep them if they look like they are part of a math formula or a command we didn't catch.
    # Simple strategy: only remove braces if they are NOT preceded by $ or a backslash.
    # Actually, it's safer to remove braces only if they contain NO backslashes or dollar signs inside.
    # But that's hard with regex.
    # Let's try to remove braces that enclose only plain text or Markdown markers.

    def strip_plain_braces(text):
        # Braces containing no special TeX chars like \, $, ^, _, &
        return re.sub(r'\{([^\\\$^_&\{\}]*)\}', r'\1', text)

    for _ in range(5): # Recursive but limited
        content = strip_plain_braces(content)

    # 19. Final cleanup
    # Remove multiple spaces
    content = re.sub(r' +', ' ', content)
    # Remove leading/trailing spaces on lines
    content = re.sub(r'^[ \t]+|[ \t]+$', '', content, flags=re.MULTILINE)
    # Multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_tex_to_md.py <input.tex> <output.md>")
        sys.exit(1)

    try:
        # Some files might have different encodings, latin-1 is usually safe for TeX
        with open(sys.argv[1], 'r', encoding='latin-1') as f:
            tex_content = f.read()
    except FileNotFoundError:
        print(f"Error: {sys.argv[1]} not found")
        sys.exit(1)

    md_content = convert_tex_to_md(tex_content)

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Successfully converted {sys.argv[1]} to {sys.argv[2]}")
