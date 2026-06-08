

\errmessageThis manual is copyrighted and should not be TeXed\repeat



{ The {\manual ()*+,-.*}book}

The fine print in the upper right-hand
corner of each page is a draft of intended
index entries; it won't appear in the real book.
Some index entries will be in 'typewriter type'
{and/or enclosed in *$\ldots$*, etc;}
such typographic distinctions aren't shown here.
An index entry often extends for several pages;
the actual scope will be determined later.
Please note things that should be indexed but aren't.

Apology: The xeroxed illustrations are often hard to see;
they will be done professionally in the real book.



{ The {\manual ()*+,-.*}book}

13pt
to{# 0pt plus 1fil&#0pt
DONALD \kern+0pt E. \kern+0pt KNUTH&
Stanford University

& I by
&DUANE BIBBY

&={\manual77}
= to{\manual6}
2.3mm\box2\kern-\box0
&ADDISON--WESLEY

{ \global}
&Upper Saddle River, NJ
&Boston$\cdot$ Indianapolis
&San Francisco$\cdot$ New York
&Toronto$\cdot$ Montr\'eal
&London$\cdot$ Munich
&Paris$\cdot$ Madrid
&Capetown$\cdot$ Sydney$\cdot$ Tokyo
&Singapore$\cdot$ Mexico City}



to 8pc

This manual describes METAFONT\ Version 2.0. Some
of the advanced features mentioned here are absent from earlier versions.

The joke on page 8 is due to Richard S. .

The quotation on page 283 was suggested by Georgia K. M. .

{\manual opqrstuq} is a trademark of Addison--Wesley
Publishing Company.

TeX\ is a trademark of the American Mathematical Society.

**Library of Congress cataloging in publication data**

{{#
Knuth, Donald Ervin, 1938-
\ \ \ The METAFONTbook.

\ \ \ (Computers \& Typesetting ; C)
\ \ \ Includes index.
\ \ \ 1. METAFONT (Computer system).\ \ 2. Type and type-
founding--Data processing.\ \ I. Title.\ \ II. Series:
Knuth, Donald Ervin, 1938-\ \ \ \ .\ \ Computers \&
typesetting ; C.
Z250.8.M46K58\ \ 1986\ \ \ \ \ \ \ \ \ 686.2 24\ \ \ \ \ \ 85-28675
ISBN 0-201-13445-4
ISBN 0-201-13444-6 (soft)}}

* Incorporates all corrections known in 2020.*

Internet page 'http://www-cs-faculty.stanford.edu/\char'\
knuth/abcde.html'
contains current information about this book and related books.

Copyright $\copyright$ 1986 by the American Mathematical Society

This book is published jointly by the American Mathematical Society
and Addison--Wesley Publishing Company.
All rights reserved.

This publication is protected by copyright, and permission must be
obtained from the publisher prior to any prohibited reproduction, storage in
a retrieval system, or transmission in any form or by any means, electronic,
mechanical, photocopying, recording, or likewise. For information regarding
permissions, request forms, and the appropriate contacts with the
Pearson Education Global Rights \& Permissions Department, please visit
'www.pearson.com/permissions/'.
Printed in the United States of America.

ISBN-13 978-0-201-13445-2
ISBN-10 \phantom978-0-201-13445-4
ISBN-13 978-0-201-13444-5 (soft)
ISBN-10 \phantom978-0-201-13444-6 (soft)

Tenth Printing, February 2021

{\pearsonkluj ScoutAutomatedPrintCode}



to 8pc
{\eightssi To Hermann Zapf:}

{\eightssi Whose strokes are the best}





to 8pc
Preface
{ 9pc

\hang\hangafter-2
\smash{12pt to 0pt{\hskip-\hangindent\cmman G}}
ENERATION OF LETTERFORMS by mathematical means
was first tried in the fifteenth century; it became popular in the
sixteenth and seventeenth centuries; and it was abandoned (for good
reasons) during the eighteenth century. Perhaps the twentieth century
will turn out to be the right time for this idea to make a comeback,
now that mathematics has advanced and computers are able to
do the calculations.

Modern printing equipment based on raster lines---in which metal "type"
has been replaced by purely combinatorial patterns of zeroes and ones
that specify the desired position of ink in a discrete way---makes
mathematics and computer science increasingly relevant to printing.
We now have the ability to give a completely precise definition of letter
shapes that will produce essentially equivalent results on all raster-based
machines. Moreover, the shapes can be defined in terms of variable
parameters; computers can "draw" new fonts of characters
in seconds, making it possible for designers to perform valuable experiments
that were previously unthinkable.

METAFONT\ is a system for the design of alphabets suited to raster-based
devices that print or display text. The characters that you are reading
were all designed with METAFONT\!, in a completely precise way; and they
were developed rather hastily by the author of the system, who is a rank
amateur at such things. It seems clear that further work with METAFONT\ has
the potential of producing typefaces of real . This manual has
been written for people who would like to help advance the art of
mathematical type design.

A top-notch designer of typefaces needs to have an unusually good eye
and a highly developed sensitivity to the nuances of shapes.
A top-notch user of computer languages needs to have an unusual
talent for abstract reasoning and a highly developed ability to
express intuitive ideas in formal terms. Very few people have both
of these unusual combinations of skills; hence the best products of
METAFONT\ will probably be collaborative efforts between two
people who complement each other's abilities. Indeed, this situation
isn't very different from the way types have been created for many
generations, except that the r\^ole of "punch-cutter" is now being
played by skilled computer specialists instead of by skilled
metalworkers.

A METAFONT\ user writes a "program" for each letter or symbol of a typeface.
These programs are different from ordinary computer programs,
because they are essentially *declarative* rather than imperative.
In the METAFONT\ language you explain where the major components of a
desired shape are to be located, and how they relate to each other,
but you don't have to work out the details of exactly where the lines
cross, etc.; the computer takes over the work of solving equations as it
deduces the consequences of your specifications. One of the advantages of
METAFONT\ is that it provides a discipline according to which the principles
of a particular alphabet design can be stated precisely. The underlying
intelligence does not remain hidden in the mind of the designer; it is
spelled out in the programs. Thus consistency can readily be obtained
where consistency is desirable, and a font can readily be extended to
new symbols that are compatible with the existing ones.

It would be nice if a system like METAFONT\ were to simplify the task of type
design to the point where beautiful new alphabets could be created in a
few hours. This, alas, is impossible; an enormous amount of subtlety lies
behind the seemingly simple letter shapes that we see every day, and the
designers of high-quality typefaces have done their work so well that we
don't notice the underlying complexity. One of the disadvantages of METAFONT\
is that a person can easily use it to produce poor alphabets, cheaply and
in great quantity. Let us hope that such experiments will have educational
value as they reveal why the subtle tricks of the trade are important, but
let us also hope that they will not cause bad workmanship to proliferate.
Anybody can now produce a book in which all of the type is home-made, but
a person or team of persons should expect to spend a year or more on the
project if the type is actually supposed to look right. METAFONT\ won't put
today's type designers out of work; on the contrary, it will tend to make
them heroes and heroines, as more and more people come to appreciate their
skills.

Although there is no royal road to type design, there are some things that
can, in fact, be done well with METAFONT\ in an afternoon. Geometric designs
are rather easy; and it doesn't take long to make modifications to letters
or symbols that have previously been expressed in METAFONT\ form. Thus,
although comparatively few users of METAFONT\ will have the courage to do an
entire alphabet from scratch, there will be many who will enjoy
customizing someone else's design.

This book is not a text about mathematics or about computers. But if
you know the rudiments of those subjects (namely, contemporary high school
mathematics, together with the knowledge of how to use the text
editing or word processing facilities on your computing machine),
you should be able to use METAFONT\ with little difficulty after reading
what follows. Some parts of the exposition in the text are more obscure
than others, however, since the author has tried to satisfy experienced
METAFONT ers as well as beginners and casual users with a single manual.
Therefore a special symbol has been used to warn about esoterica: When you
see the sign
$${{\dbend}}$$
at the beginning of a paragraph, watch out for a ""
in the train of thought---don't read such a paragraph unless you need to.
You will be able to use METAFONT\ reasonably well, even to design characters like
the dangerous-bend symbol itself, without reading the fine print in such
advanced sections.

Some of the paragraphs in this manual are so far out that they are rated
$$\vcenter{{\dbend\dbend}}\;;$$
everything that was said about single dangerous-bend signs goes double
for these. You should probably have at least a month's experience with
METAFONT\ before you attempt to fathom such doubly dangerous depths
of the system; in fact, most people will never need to know METAFONT\
in this much detail, even if they use it every day. After all, it's
possible to fry an egg without knowing anything about biochemistry.
Yet the whole story is here in case you're curious. \ (About METAFONT\!, not eggs.)

The reason for such different levels of complexity is that people change
as they grow accustomed to any powerful tool. When you first try to use
METAFONT\!, you'll find that some parts of it are very easy, while other things
will take some getting used to. At first you'll probably try to control
the shapes too rigidly, by overspecifying data that has been copied from
some other medium. But later, after you have begun to get a feeling for
what the machine can do well, you'll be a different person, and you'll be
willing to let METAFONT\ help contribute to your designs as they are being
developed. As you gain more and more experience working with this unusual
apprentice, your perspective will continue to change and you will
run into different sorts of challenges. That's the way it is with any
powerful tool: There's always more to learn, and there are always better
ways to do what you've done before. At every stage in the development
you'll want a slightly different sort of manual. You may even want to
write one yourself. By paying attention to the dangerous bend signs in
this book you'll be better able to focus on the level that interests you
at a particular time.

Computer system manuals usually make dull reading, but take heart:
This one contains every once in a while. You might actually
enjoy reading it. \ (However, most of the jokes can only be appreciated
properly if you understand a technical point that is being made---so
read *carefully*.)

Another noteworthy characteristic of this book is that it doesn't
always tell the . When certain concepts of METAFONT\ are introduced
informally, general rules will be stated; afterwards you will find that the
rules aren't strictly true. In general, the later chapters contain more
reliable information than the earlier ones do. The author feels that this
technique of deliberate lying will actually make it easier for you to
learn the ideas. Once you understand a simple but false rule, it will not
be hard to supplement that rule with its exceptions.

In order to help you internalize what you're reading,
are sprinkled through this manual. It is generally intended
that every reader should try every exercise, except for questions that appear
in the "dangerous bend" areas. If you can't solve a problem, you
can always look up the answer.
But please, try first to solve it by yourself; then you'll learn more
and you'll learn faster. Furthermore, if you think you do know the solution,
you should turn to Appendix A and check it out, just to make sure.

\hrule
{\vrule{
\leftskip=indent \rightskip=indent
WARNING: Type design can be hazardous to your other
interests. Once you get hooked, you will develop intense feelings about
letterforms; the medium will intrude on the messages that you read. And you
will perpetually be thinking of improvements to the fonts that you see
everywhere, especially those of your own design.
}\vrule}
\hrule

The METAFONT\ language described here has very little in common with the
author's previous attempt at a language for alphabet design, because
five years of experience with the old system has made it clear that a
completely different approach is preferable. Both languages have
been called METAFONT; but henceforth the old language should be called
METAFONT79, and its use should rapidly fade away. Let's keep the name
METAFONT\ for the language described here, since it is so much better, and
since it will never change again.

I wish to thank the hundreds of people who have helped me to formulate
this "definitive edition" of METAFONT\!, based on their experiences with
preliminary versions of the system. In particular, John
discovered many of the algorithms that have made the new language
possible. My work at Stanford has been generously supported by the
, the , the ^IBM
Corporation, and the . I also wish to
thank the for its encouragement and for
publishing the ** newsletter (see Appendix J).
Above all, I deeply thank my wife, Jill, for the inspiration,
understanding, comfort, and support she has given me for more than
25 years, especially during the eight years that I have been
working intensively on mathematical typography.

*Stanford, California*--- D. E. K.
*September 1985*

}
\endchapter

It is hoped that Divine Justice may find
some suitable affliction for the malefactors
who invent variations upon the alphabet of our fathers. ...
The type-founder, worthy mechanic, has asserted himself
with an overshadowing individuality,
defacing with his monstrous creations and revivals
every publication in the land.
or AMBROSE , *The Opinionator. Alphab\^etes*
(1911)

Can the new process yield a result that, say,
a Club of Bibliophiles would recognise as a work of art
comparable to the choice books they have in their cabinets?
or STANLEY , *Typographic Design in Relation to
Photographic Composition* (1958)



to 8pc
Contents

\ifodd\counter \fi
\leaders to 20pt{\ifodd\counter \else \fi
.}}
15pt plus 5pt

toindent to 1em#1
#2\diamondleaders to 2em#3}}
\\1. The Name of the Game. 1.
\\2. Coordinates. 5.
\\3. Curves. 13.
\\4. Pens. 21.
\\5. Running METAFONT\!. 31.
\\6. How METAFONT\ Reads What You Type. 49.
\\7. Variables. 53.
\\8. Algebraic Expressions. 59.
\\9. Equations. 75.
\\10. Assignments. 87.
\\11. Magnification and Resolution. 91.
\\12. Boxes. 101.
\\13. Drawing, Filling, and Erasing. 109.
\\14. Paths. 123.
\\15. Transformations. 141.
\\16. Calligraphic Effects. 147.
\\17. Grouping. 155.
\\18. Definitions (also called Macros). 159.
\\19. Conditions and Loops. 169.
\\20. More About Macros. 175.
\\21. Random Numbers. 183.
\\22. Strings. 187.
\\23. Online Displays. 191.

to 8pc
\\24. Discreteness and Discretion. 195.
\\25. Summary of Expressions. 209.
\\26. Summary of the Language. 217.
\\27. Recovery from Errors. 223.

{\indent Appendices}
\\A. Answers to All the Exercises. 233.
\\B. Basic Operations. 257.
\\C. Character Codes. 281.
\\D. Dirty Tricks. 285.
\\E. Examples. 301.
\\F. Font Metric Information. 315.
\\G. Generic Font Files. 323.
\\H. Hardcopy Proofs. 327.
\\I. Index. 345.
\\J. Joining the TeX\ Community. 361.


# Chapter 1. The Name of the Game

This is a book about a computer system called METAFONT\!, just as
*The TeX
book* is about TeX. METAFONT\ and TeX\ are good friends who intend to live
together for a long time. Between them they take care of the two most
fundamental tasks of typesetting: TeX\ puts characters into the proper
positions on a page, while METAFONT\ determines the shapes of the characters
themselves.

Why is the system called METAFONT? The '-{\manual FONT}'
part is easy to understand, because sets of related characters that are
used in typesetting are traditionally known as fonts of type. The
'{\manual META}-' part is more interesting: It indicates that we are
interested in making high-level descriptions that transcend any of the
individual fonts being described.

Newly coined words beginning with 'meta-' generally reflect our contemporary
inclination to view things from outside or above, at a more abstract level than
before, with what we feel is a more mature understanding. We now have
metapsychology (the study of how the mind relates to its containing body),
metahistory (the study of principles that control the course of events),
metamathematics (the study of mathematical reasoning), metafiction
(literary works that explicitly acknowledge their own forms), and so on.
A metamathematician proves metatheorems (theorems about theorems);
a computer scientist often works with metalanguages (languages for
describing languages). Similarly, a is a schematic description
of the shapes in a family of related fonts; the letterforms change
appropriately as their underlying parameters change.

Meta-design is much more difficult than design. It's easier to draw something
than to explain how to draw it. One of the problems is that different sets
of potential specifications can't easily be envisioned all at once.
Another is that a computer has to be told absolutely everything.
However, once we have successfully explained how to draw something
in a sufficiently general manner, the same explanation will work for
related shapes, in different circumstances; so the time spent in formulating
a precise explanation turns out to be worth it.

Typefaces intended for text are normally seen small, and our eyes can read
them best when the letters have been designed specifically for the size at
which they are actually used. Although it is tempting to get 7-point fonts
by simply making a 70\% reduction from the 10-point size, this shortcut
leads to a serious degradation of quality. Much better results can be
obtained by incorporating parametric variations into a meta-design. In
fact, there are advantages to built-in variability even when you want to
produce only one font of type in a single size, because it allows you to
postpone making decisions about many aspects of your design. If you leave
certain things undefined, treating them as parameters instead of
"freezing" the specifications at an early stage, the computer will be
able to draw lots of examples with different settings of the parameters,
and you will be able to see the results of all those experiments at the final
size. This will greatly increase your ability to edit and fine-tune the font.

If meta-fonts are so much better than plain old ordinary fonts, why weren't
they developed long ago? The main reason is that computers did not exist until
recently. People find it difficult and dull to carry out calculations with
a multiplicity of parameters, while today's machines do such tasks with ease.
The introduction of parameters is a natural outgrowth of automation.

OK, let's grant that meta-fonts sound good, at least in theory. There's still
the practical problem about how to achieve them. How can we actually
specify shapes that depend on unspecified parameters?

If only one parameter is varying, it's fairly easy to solve the problem in
a visual way, by overlaying a series of drawings that show graphically how
the shape changes. For example, if the parameter varies from 0 to 1, we
might prepare five sketches, corresponding to the parameter values 0,
$1\over4$, $1\over2$, $3\over4$, and 1. If these sketches follow a
consistent pattern, we can readily to find the shape for a
value like $2\over3$ that lies between two of the given ones. We might
even try extrapolating to parameter values like 1$1\over4$.

But if there are two or more independent parameters, a purely visual solution
becomes too cumbersome. We must go to a verbal approach, using some sort
of language to describe the desired drawings. Let's imagine, for example,
that we want to explain the shape of a certain letter 'a' to a friend in
a distant country, using only a telephone for communication; our friend
is supposed to be able to reconstruct exactly the shape we have in mind.
Once we figure out a sufficiently natural way to do that, for a particular
fixed shape, it isn't much of a trick to go further and make our verbal
description more general, by including variable parameters instead of
restricting ourselves to constants.

An analogy to cooking might make this point clearer. Suppose you have just
baked a delicious berry pie, and your friends ask you to tell them the
so that they can bake one too. If you have developed your cooking
skills entirely by intuition, you might find it difficult to record exactly
what you did. But there is a traditional language of recipes in which you
could communicate the steps you followed; and if you take careful measurements,
you might find that you used, say, 1$1\over4$ cups of sugar. The next step,
if you were instructing a computer-controlled cooking machine, would be to
go to a meta-recipe in which you use, say, $.25x$ cups of sugar for $x$
cups of berries; or $.3x+.2y$ cups for $x$ cups of boysenberries and
$y$ cups of blackberries.

In other words, going from design to meta-design is essentially like
going from arithmetic to elementary algebra. Numbers are replaced
by simple formulas that involve unknown quantities. We will see
many examples of this.

A METAFONT\ definition of a complete typeface generally consists of three
main parts. First there is a rather mundane set of subroutines that take care
of necessary administrative details, such as assigning code numbers
to individual characters; each character must also
be positioned properly inside an invisible "box," so that typesetting
systems will produce the correct spacing. Next comes a more interesting
collection of subroutines, designed to draw the basic strokes characteristic
of the typeface (e.g., the serifs, bowls, arms, arches, and so on).
These subroutines will typically be described in terms of their own special
parameters, so that they can produce a variety of related strokes;
a serif subroutine will, for example, be able to draw serifs of
different lengths, although all of the serifs it draws should have the
same "feeling." Finally, there are routines for each of the characters.
If the subroutines in the first and second parts have been chosen well,
the routines of the third part will be fairly high-level descriptions
that don't concern themselves unnecessarily with details; for example, it
may be possible to substitute a different serif-drawing subroutine without
changing any of the programs that use that subroutine, thereby obtaining
a typeface of quite a different flavor. [A particularly striking example
of this approach has been worked out by John D. and Guoan
in "A Chinese Meta-Font," *TUGboat 5* (1984), 119--136. By
changing a set of 13 basic stroke subroutines, they were able to draw 128
sample in three different styles (Song, Long Song,
and Bold), using the same programs for the characters.]

A well-written METAFONT\ program will express the designer's intentions more
clearly than mere drawings ever can, because the language of algebra has
simple "idioms" that make it possible to elucidate many visual relationships.
Thus, METAFONT\ programs can be used to communicate knowledge
about type design, just as recipes convey the expertise of a chef. But
algebraic formulas are not easy to understand in isolation; METAFONT\ descriptions
are meant to be read with an accompanying illustration, just as the
constructions in geometry textbooks are accompanied by diagrams.
Nobody is ever expected to read the text of a METAFONT\ program and say,
"Ah, what a beautiful letter!" But with one or more enlarged pictures
of the letter, based on one or more settings of the parameters, a reader
of the METAFONT\ program should be able to say, "Ah, I understand how this
beautiful letter was drawn!" We shall see that the METAFONT\ system makes it
fairly easy to obtain annotated proof drawings that you can hold in your
hand as you are working with a program.

Although METAFONT\ is intended to provide a relatively painless way to describe
meta-fonts, you can, of course, use it also to describe unvarying shapes that
have no "meta-ness" at all. Indeed, you need not even use it to produce
fonts; the system will happily draw geometric designs that have no relation
to the characters or glyphs of any alphabet or script. The author
occasionally uses METAFONT\ simply as a pocket calculator, to do elementary
arithmetic in an interactive way. A computer doesn't mind if its
programs are put to purposes that don't match their names.

\endchapter

[Tinguely] made some large, brightly coloured open reliefs,
juxtaposing stationary and mobile shapes.
He later gave them names like
Meta-\ and Meta-,
to clarify the ideas and attitudes
that lay at the root of their conception.

> --- K. G. PONTUS , *Jean : M\'eta* (1972)

The idea of a meta-font should now be clear. But what good is it?
The ability to manipulate lots of parameters may be interesting and fun,
but does anybody really need a 6{\manual\seventh}-point font
that is one fourth of the way between Baskerville and Helvetica?

> --- DONALD E. , *The Concept of a Meta-Font* (1982)


# Chapter 2. Coordinates

If we want to tell a computer how to draw a particular shape, we need a way to
explain where the key points of that shape are supposed to be.
METAFONT\ uses standard ** for this purpose:
The location of a point is defined by specifying its $x$ coordinate, which
is the number of units to the right of some reference point, and its
$y$ coordinate, which is the number of units upward from the reference
point. First we determine the horizontal (left/right) component of a
point's position, then we determine the vertical (up/down) component.
METAFONT's world is two-dimensional, so two coordinates are enough.

For example, let's consider the following six points:
\displayfig 2a (4.75pc)
METAFONT's names for the positions of these points are

>
$(x_1,y_1)=(0,100)$;&$(x_2,y_2)=(100,100)$;&$(x_3,y_3)=(200,100)$;
$(x_4,y_4)=(0,0)$;&$(x_5,y_5)=(100,0)$;&
$(x_6,y_6)=(200,0)$.

Point 4 is the same as the reference point, since both of its coordinates
are zero; to get to point $3=(200,100)$, you start at the reference point
and go 200 steps right and 100 up; and so on.

### Exercise
Which of the six example points is closest to the point $(60,30)$?

#### Answer
Point $5=(100,0)$ is closer than any of the others. \ (See
the diagram below.)

### Exercise
True or false: All points that lie on a given horizontal straight
line have the same $x$ coordinate.

#### Answer
\decreasehsize 15pc
\rightfig A2a (13pc x 5pc) ^9pt
False. But they all do have the same $y$ coordinate.

### Exercise
Explain where the point $(-5,15)$ is located.

#### Answer
5 units to the *left* of the reference point, and 15 units up.

### Exercise
What are the coordinates of a point that lies exactly
60 units below point 6 in the diagram above?
("Below" means "down the page," not "under the page.")

#### Answer
\restorehsize $(200,-60)$.

In a typical application of METAFONT\!, you prepare a rough sketch of the shape
you plan to define, on a piece of , and you label important
points on that sketch with any convenient numbers. Then you write a METAFONT\
program that explains (i) the coordinates of those key points, and
(ii) the lines or curves that are supposed to go between them.

METAFONT\ has its own internal graph paper, which forms a so-called
or consisting of square "."
The output of METAFONT\ will specify that certain of the pixels are "black"
and that the others are "white"; thus, the computer essentially converts
shapes into binary patterns like the designs a person can make when doing
needlepoint with two colors of yarn.

Coordinates are lengths, but we haven't discussed yet what the units of
length actually are. It's important to choose convenient units,
and METAFONT's coordinates are given in units of pixels. The little squares
illustrated on the previous page, which correspond to differences
of 10 units in an $x$ coordinate or a $y$ coordinate, therefore represent
$10\times10$ arrays of pixels, and the rectangle enclosed by our six
example points contains 20,000 pixels altogether.\footnote*We
sometimes use the term "pixel" to mean a square picture element,
but sometimes we use it to signify a one-dimensional unit of length.
A square pixel is one pixel-unit wide and one pixel-unit tall.

Coordinates don't have to be whole numbers. You can refer, for example,
to point $(31.5,42.5)$, which lies smack in the middle of the pixel
whose corners are at $(31,42)$, $(31,43)$, $(32,42)$, and $(32,43)$.
The computer works internally with coordinates that are integer multiples
of ${1\over65536}\approx0.00002$ of the width of a pixel, so it is
capable of making very fine distinctions. But METAFONT\ will never make
a pixel half black; it's all or nothing, as far as the output is concerned.

The fineness of a grid is usually called its **, and
resolution is usually expressed in pixel units per inch (in America)
or pixel units per millimeter (elsewhere). For example, the type you
are now reading was prepared by METAFONT\ with a resolution of slightly
more than 700 pixels to the inch, but with slightly fewer than 30 pixels
per mm. For the time being we shall assume that the pixels are so tiny
that the operation of rounding to whole pixels is unimportant;
later we will consider the important questions that arise when METAFONT\ is
producing low-resolution output.

It's usually desirable to write METAFONT\ programs that can manufacture fonts
at many different resolutions, so that a variety of low-resolution printing
devices will be able to make proofs that are compatible with a variety of
high-resolution devices. Therefore the key points in METAFONT\ programs are rarely
specified in terms of pure numbers like '100'; we generally make
the coordinates relative to some other resolution-dependent quantity, so
that changes will be easy to make. For example, it would have been better
to use a definition something like the following, for the six points
considered earlier:

>
$(x_1,y_1)=(0,b)$;&$(x_2,y_2)=(a,b)$;&$(x_3,y_3)=(2a,b)$;
$(x_4,y_4)=(0,0)$;&$(x_5,y_5)=(a,0)$;&$(x_6,y_6)=(2a,0)$;

then the quantities $a$ and $b$ can be defined in some way appropriate to
the desired resolution. We had $a=b=100$ in our previous example, but
such constant values leave us with little or no flexibility.

Notice the quantity '$2a$' in the definitions of $x_3$ and $x_6$; METAFONT\
understands enough algebra to know that this means twice the value of $a$,
whatever $a$ is. We observed in Chapter 1 that simple uses of algebra give
METAFONT\ its meta-ness. Indeed, it is interesting to note from a historical
standpoint that coordinates are named after Ren\'e
, not because he invented the idea of coordinates, but because
he showed how to get much more out of that idea by applying algebraic
methods. People had long since been using coordinates for such things as
latitudes and longitudes, but Descartes observed that by putting unknown
quantities into the coordinates it became possible to describe infinite
sets of related points, and to deduce properties of curves that were
extremely difficult to work out using geometrical methods alone.

So far we have specified some points, but we haven't actually done
anything with them. Let's suppose that we want to draw a straight line
from point 1 to point 6, obtaining
\displayfig 2b (5pc)
One way to do this with METAFONT\ is to say

>
@draw@ $(x_1,y_1)\to(x_6,y_6)$.

The '$\to$' here tells the computer to connect two points.

It turns out that we often want to write formulas like '$(x_1,y_1)$', so
it will be possible to save lots of time if we have a special abbreviation
for such things. Henceforth we shall use the notation $z_1$ to stand for
$(x_1,y_1)$; and in general,
$z_k$ with an arbitrary subscript will stand for the point $(x_k,y_k)$.
The '@draw@' command above can therefore be written more simply as

>
^@draw@ $z_1\to z_6$.

Adding two more straight lines by saying, '@draw@ $z_2\to z_5$' and
'@draw@ $z_3\to z_4$', we obtain a design that is slightly reminiscent of
the :
\displayfig 2c (5.5pc)
We shall call this a , because it has six endpoints. Notice
that the straight lines here have some thickness, and they are rounded at
the ends as if they had been drawn with a felt-tip pen having a circular
nib. METAFONT\ provides many ways to control the thicknesses of lines and to
vary the terminal shapes, but we shall discuss such things in later
chapters because our main concern right now is to learn about coordinates.

If the hex symbol is scaled down so that its height parameter $b$
is exactly equal to the height of the letters in this paragraph,
it looks like this: '{\manual\hexa}'. Just for fun,
let's try to typeset ten of them in a row:

>
{\manual\hexa\hexa\hexa\hexa\hexa\hexa\hexa\hexa\hexa\hexa}

How easy it is to do this!\footnote*Now that authors have
for the first time the power to invent new symbols with great ease, and to
have those characters printed in their manuscripts on a wide variety of
typesetting devices, we must face the question of how much experimentation
is desirable. Will font freaks abuse this toy by overdoing it? Is it wise
to introduce new symbols by the thousands? Such questions are beyond
the scope of this book; but it is easy to imagine an epidemic of
fontomania occurring, once people realize how much fun it is to design
their own characters, hence it may be necessary to perform fontal
lobotomies.

Let's look a bit more closely at this new character.
The {\manual\hexa} is a bit too tall, because it extends above points
1, 2, and 3 when the thickness of the lines is taken into account;
similarly, it sinks a bit too much below the baseline (i.e., below
the line $y=0$ that contains points 4, 5, and 6). In order to correct
this, we want to move the key points slightly. For example, point $z_1$
should not be exactly at $(0,b)$; we ought to arrange things so that
the top of the pen is at $(0,b)$ when the center of the pen is at $z_1$.
We can express this condition for the top three points as follows:

>
$"top"\,z_1=(0,b)$;&$"top"\,z_2=(a,b)$;&$"top"\,z_3=(2a,b)$;
{\vskip\belowdisplayskip
similarly, the remedy for points 4, 5, and 6 is to specify
the equations
\vskip\abovedisplayskip}
$"bot"\,z_4=(0,0)$;&$"bot"\,z_5=(a,0)$;&$"bot"\,z_6=(2a,0)$.

The resulting squashed-in character is
\displayfig 2d (4.5pc)
(shown here with the original weight '{\manual\hexb}'
and also in a bolder version '{\manual\hexc}').

### Exercise
Ten of these bold hexes produce '{\manual
\hexc\hexc\hexc\hexc\hexc\hexc\hexc\hexc\hexc\hexc}'; notice that
adjacent symbols overlap each other. The reason is that each character
has width $2a$, hence point 3 of one character coincides with point 1
of the next. Suppose that we actually want the characters to be
completely confined to a rectangular box of width $2a$, so that
adjacent characters come just shy of touching ({\manual
\hexd\hexd\hexd\hexd\hexd\hexd\hexd\hexd\hexd\hexd}).
Try to guess how the point-defining equations above could be modified
to make this happen, assuming that
METAFONT\ has operations '"lft"' and '"rt"' analogous to '"top"' and '"bot"'.

#### Answer
$"top"\,"lft"\,z_1=(0,b)$; \ $"top"\,z_2=(a,b)$; \
$"top"\,"rt"\,z_3=(2a-1,b)$; \ $"bot"\,"lft"\,z_4=(0,0)$; \
$"bot"\,z_5=(a,0)$; \ $"bot"\,"rt"\,z_6=(2a-1,0)$.
Adjacent characters will be separated by exactly one column of white
pixels, if the character is $2a$ pixels wide, because the right edge of
black pixels is specified here to have the $x$ coordinate $2a-1$.

Pairs of coordinates can be thought of as "" or "displacements"
as well as points. For example, $(15,8)$ can be regarded as a command to
go right 15 and up 8; then point $(15,8)$ is the position we get to after
starting at the reference point and obeying the command $(15,8)$. This
interpretation works out nicely when we consider addition of vectors:
If we move according to the vector $(15,8)$ and then move according to
$(7,-3)$, the result is the same as if we move $(15,8)+(7,-3)=
(15+7,8-3)=(22,5)$. The sum of two vectors $z_1=(x_1,y_1)$ and $z_2=
(x_2,y_2)$ is the vector $z_1+z_2=(x_1+x_2,y_1+y_2)$ obtained by adding
$x$ and $y$ components separately. This vector represents the result of
moving by vector $z_1$ and then moving by vector $z_2$; alternatively,
$z_1+z_2$ represents the point you get to by starting at point $z_1$

and moving by vector $z_2$.

### Exercise
Consider the four fundamental vectors $(0,1)$, $(1,0)$,
$(0,-1)$, and $(-1,0)$. Which of them corresponds to moving one pixel unit
(a) to the right? (b) to the left? (c) down? (d) up?

#### Answer
$"right"=(1,0)$; $"left"=(-1,0)$; $"down"=(0,-1)$; $"up"=(0,1)$.

Vectors can be subtracted as well as added; the value of $z_1-z_2$ is simply
$(x_1-x_2,y_1-y_2)$. Furthermore it is natural to multiply a vector
by a single number $c$: The quantity $c$ times $(x,y)$, which is written
$c(x,y)$, equals $(cx,cy)$. Thus, for example, $2z=2(x,y)=(2x,2y)$ turns
out to be equal to $z+z$.
In the special case $c=-1$, we write $-(x,y)=(-x,-y)$.

Now we come to an important notion, based on the fact that subtraction
is the opposite of addition. *If $z_1$ and $z_2$ are any two points,
then $z_2-z_1$ is the vector that corresponds to moving from $z_1$ to $z_2$.*
The reason is simply that $z_2-z_1$ is what we must add to $z_1$ in order
to get $z_2$: i.e., $z_1+(z_2-z_1)=z_2$. We shall call this the
**.
It is used frequently in METAFONT\ programs when the designer wants to specify the
direction and/or distance of one point from another.

METAFONT\ programs often use another idea to express relations between points.
Suppose we start at point $z_1$ and travel in a straight line from there
in the direction of point $z_2$, but we don't go all the way. There's a
special notation for this, using square brackets:

> by 3pt
${1\over3}[z_1,z_2]$ is the point one-third of the way from $z_1$ to $z_2$,
${1\over2}[z_1,z_2]$ is the point midway between $z_1$ and $z_2$,
$.8[z_1,z_2]$ is the point eight-tenths of the way from $z_1$ to $z_2$,

and, in general, $t[z_1,z_2]$ stands for the point that lies a fraction
$t$ of the way from $z_1$ to $z_2$. We call this the operation of ** between points, or (informally) the "^of-the-way
function." If the fraction $t$ increases from 0 to 1, the expression
$t[z_1,z_2]$ traces out a straight line from $z_1$ to $z_2$. According to
the vector subtraction principle, we must move $z_2-z_1$ in order to go all
the way from $z_1$ to $z_2$, hence the point $t$ of the way between them is

>
$t[z_1,z_2]\;=\;z_1+t(z_2-z_1)$.

This is a general formula by which we can calculate $t[z_1,z_2]$ for any
given values of $t$, $z_1$, and $z_2$. But METAFONT\ has this formula built in,
so we can use the bracket notation explicitly.

For example, let's go back to our first six example points, and suppose
that we want to refer to the point that's 2/5 of the way from
$z_2=(100,100)$ to $z_6=(200,0)$. In METAFONT\ we can write this simply as
$.4[z_2,z_6]$. And if we need to compute the exact coordinates for some
reason, we can always work them out from the general formula, getting
$z_2+.4(z_6-z_2)=(100,100)+.4\bigl((200,0)-(100,100)\bigr)=(100,100)
+.4(100,-100)=(100,100)+(40,-40)=(140,60)$.

### Exercise
True or false: The direction vector from $(5,-2)$ to $(2,3)$
is $(-3,5)$.

#### Answer
True; this is $(2,3)-(5,-2)$.

### Exercise
Explain what the notation '$0[z_1,z_2]$' means, if anything.
What about '$1[z_1,z_2]$'? And '$2[z_1,z_2]$'? And '$(-.5)[z_1,z_2]$'?

#### Answer
$0[z_1,z_2]=z_1$, because we move none of the way towards $z_2$;
similarly $1[z_1,z_2]$ simplifies to $z_2$, because we move all of the
way. If we keep going in the same direction until we've gone twice as far
as the distance from $z_1$ to $z_2$, we get to $2[z_1,z_2]$. But if we
start at point $z_1$ and face $z_2$, then back up exactly half the distance
between them, we wind up at $(-.5)[z_1,z_2]$.

### Exercise
True or false, for mathematicians: (a) ${1\over2}[z_1,z_2]=
{1\over2}(z_1+z_2)$; \ (b) ${1\over3}[z_1,z_2]={1\over3}z_1+{2\over3}z_2$;
\ (c) $t[z_1,z_2]=(1-t)[z_2,z_1]$.

#### Answer
(a) True; both are equal to $z_1+{1\over2}(z_2-z_1)$.
(b) False, but close; the right-hand side should be
${2\over3}z_1+{1\over3}z_2$. (c) True; both are equal to $(1-t)z_1+tz_2$.

={
{\rlap{ to 250\apspix{
={
{\tenex}
}
\offinterlineskip
{{\tenex}}
\cleaders\copy2

to{$b$}

\cleaders\copy2
{{\tenex}}
}}\kern 30\apspix
{
{
\kern30\apspix\figbox2e{150\apspix}{250\apspix}

\kern30\apspix}
}}

{ to 30\apspix{\vrule height 7pt depth 2pt
$s$\vrule}
to 150\apspix{\leftarrowfill$\,a\,$\rightarrowfill}
to 30\apspix{\vrule height 7pt depth 2pt
$s$\vrule}}}
=0pt

\hangindent-300\apspix \hangafter-13
Let's conclude \vadjust{\box0}
this chapter by using mediation
to help specify the five points in the stick-figure '{\manual\Aa}'
shown enlarged at the right. The distance between points 1 and 5
should be $a$, and point 3 should be $b$ pixels above the baseline;
these values $a$ and $b$ have been predetermined by some method
that doesn't concern us here, and so has a "" parameter $s$
that specifies the horizontal distance of points 1 and 5 from the
edges of the type. We shall assume that we don't know for sure what
the height of the bar line should be; point 2 should be somewhere on the
straight line from point 1 to point 3, and point 4 should be in the
corresponding place between 5 and 3, but we want to try several
possibilities before we make a decision.

The width of the character will be $s+a+s$, and we can specify points
$z_1$ and $z_5$ by the equations

>
$"bot"\,z_1=(s,0)$; $z_5=z_1+(a,0)$.

There are other ways to do the job, but these formulas clearly express
our intention to have the bottom of the pen at the baseline, $s$ pixels
to the right of the reference point, when the pen is at $z_1$,
and to have $z_5$ exactly $a$ pixels to the right of $z_1$.
Next, we can say

>
$z_3=\bigl({1\over2}[x_1,x_5],b\bigr)$;

this means that the $x$ coordinate of point 3 should be halfway between
the $x$ coordinates of points 1 and 5, and that $y_3=b$. Finally, let's say

>
$z_2="alpha"[z_1,z_3]$; $z_4="alpha"[z_5,z_3]$;

the parameter "alpha" is a number between 0 and 1 that governs the
position of the bar line, and it will be supplied later. When "alpha"
has indeed received a value, we can say

>
@draw@ $z_1\to z_3$; @draw@ $z_3\to z_5$; @draw@ $z_2\to z_4$.

METAFONT\ will draw the characters '{\manual\sevenAs}' when "alpha" varies
from 0.2 to 0.5 in steps of 0.05 and when $a=150$, $b=250$, $s=30$.
The illustration on the previous page has $"alpha"=(3-\sqrt5\,)/2\approx
0.38197$; this value makes the ratio of the area below the bar to the area
above it equal to $(\sqrt5+1)/2\approx1.61803$, the so-called "^golden
ratio" of classical Greek mathematics.

**[Dangerous Bend]** (Are you sure you should be reading this paragraph? The
"" sign here is meant to warn you about material that
ought to be skipped on first reading. And maybe also on second reading.
The reader-beware paragraphs sometimes refer to concepts that aren't
explained until later chapters.)

**[Dangerous Bend]** exercise Why is it better to define $z_3$ as $\bigl({1\over2}[x_1,
x_5],b\bigr)$, rather than to work out the explicit coordinates
$z_3=(s+{1\over2}a,\,b)$ that are implied by the other equations?

#### Answer
There are several reasons. (1) The equations in a METAFONT\ program
should represent the programmer's intentions as directly as possible;
it's hard to understand those intentions if you are shown only
their ultimate consequences, since it's not easy to reconstruct algebraic
manipulations that have gone on behind the scenes. (2) It's easier and
safer to let the computer do algebraic calculations, rather than
to do them by hand. (3) If the specifications for $z_1$ and $z_5$ change,
the formula $\bigl({1\over2}[x_1,x_5],b\bigr)$
still gives a reasonable value for $z_3$. It's
almost always good to anticipate the need for subsequent modifications.
However, the stated formula for $z_3$ isn't the only reasonable way to
proceed. We could, for example, give two equations

>
$x_3-x_1=x_5-x_3$; $y_3=b$;

the first of these states that the horizontal distance from 1 to 3 is
the same as the horizontal distance from 3 to 5. We'll see later that
METAFONT\ is able to solve a wide variety of equations.

**[Double Dangerous Bend]** exercise Given $z_1$, $z_3$, and $z_5$ as above, explain how
to define $z_2$ and $z_4$ so that all of the following conditions hold
simultaneously:
\enddanger

- the line from $z_2$ to $z_4$ slopes upward at a $20^\circ$ angle;

- the $y$ coordinate of that line's midpoint is 2/3 of the
way from $y_3$ to $y_1$;

- $z_2$ and $z_4$ are on the respective lines $z_1\to z_3$ and
$z_3\to z_5$.

(If you solve this exercise, you deserve an '{\manual\Az}'.)

#### Answer
The following four equations suffice to define the four
unknown quantities $x_2$, $y_2$, $x_4$, and $y_4$:
$z_4-z_2="whatever"\astdir\,20$;
${1\over2}[y_2,y_4]={2\over3}[y_3,y_1]$;
$z_2="whatever"[z_1,z_3]$;
$z_4="whatever"[z_3,z_5]$. ^^"whatever"

\endchapter

Here, where we reach the sphere of mathematics,
we are among processes which seem to some
the most inhuman of all human activities
and the most remote from poetry.
Yet it is here that the artist has the fullest scope for his imagination.

> --- HAVELOCK , *The Dance of Life* (1923)

To anyone who has lived in a modern American city (except Boston)
at least one of the underlying ideas of ' analytic geometry
will seem ridiculously evident. Yet, as remarked,
it took mathematicians all of two thousand years
to arrive at this simple thing.
or ERIC TEMPLE , *Mathematics: Queen and Servant of
Science* (1951)


# Chapter 3. Curves

Albrecht and other Renaissance men attempted to establish
mathematical principles of type design, but the letters they came up with
were not especially beautiful. Their methods failed because they
restricted themselves to "ruler and compass" constructions, which cannot
adequately express the nuances of good calligraphy. METAFONT\ gets around this
problem by using more powerful mathematical techniques, which provide the
necessary flexibility without really being too complicated. The purpose of
the present chapter is to explain the simple principles by which a
computer is able to draw "pleasing" .

The basic idea is to start with four points $(z_1,z_2,z_3,z_4)$ and to

construct the three $z_12={1\over2}[z_1,z_2]$,
$z_23={1\over2}[z_2,z_3]$, $z_34={1\over2}[z_3,z_4]$:
\displayfig 3a (5pc)
Then take those three midpoints $(z_12,z_23,z_34)$ and construct
two second-order midpoints $z_123={1\over2}[z_12,z_23]$ and
$z_234={1\over2}[z_23,z_34]$; finally, construct the third-order
midpoint $z_1234={1\over2}[z_123,z_234]$:
\displayfig 3b (5pc)
This point $z_1234$ is one of the points of the curve determined by
$(z_1,z_2,z_3,z_4)$. To get the remaining points of that curve,
repeat the same construction on $(z_1,z_12,z_123,z_1234)$ and
on $(z_1234,z_234,z_34,z_4)$, ad infinitum:
\displayfig 3c (4.5pc)
The process converges quickly, and the preliminary scaffolding
(which appears above the limiting curve in our example) is ultimately discarded.
The limiting curve has the following important properties:

- It begins at $z_1$, heading in the direction from $z_1$ to $z_2$.

- It ends at $z_4$, heading in the direction from $z_3$ to $z_4$.

- It stays entirely within the so-called convex hull of $z_1$,
$z_2$, $z_3$, and $z_4$; i.e., all points of the curve lie "between" the
defining points.

**[Dangerous Bend]** The recursive midpoint rule for curve-drawing was discovered in 1959
by Paul , who showed that the curve could be described
algebraically by the remarkably simple formula

>
$z(t)\;=\;(1-t)^3z_1+3(1-t)^2t\,z_2+3(1-t)t^2z_3+t^3z_4$,

as the parameter $t$ varies from 0 to 1. This polynomial of degree 3 in $t$
is called a *n polynomial*}, because Serge\u\i N.
n} introduced such functions in 1912 as part of his
pioneering work on approximation theory. Curves traced out by Bernshte{\u\i}n
polynomials of degree 3 are often called *B\'ezier cubics*, after
Pierre who realized their importance for computer-aided design
during the 1960s.

**[Dangerous Bend]** It is interesting to observe that the Bernshte\u\i n polynomial
of degree 1, i.e., the function $z(t)=(1-t)\,z_1+t\,z_2$, is precisely the
operator $t[z_1,z_2]$ that we discussed in the previous chapter.
Indeed, if the geometric construction we have just seen is changed to
use $t$-of-the-way points instead of midpoints (i.e., if $z_12=
t[z_1,z_2]$ and $z_23=t[z_2,z_3]$, etc.), then $z_1234$ turns out
to be precisely $z(t)$ in the formula above.

No matter what four points $(z_1,z_2,z_3,z_4)$ are given, the construction
on the previous page defines a curved line that runs from $z_1$ to $z_4$.
This curve is not always interesting or beautiful; for example, if all
four of the given points lie on a straight line, the entire "curve"
that they define will also be contained in that same line. We obtain
rather different curves from the same four starting points if we
number the points differently:
\displayfig 3d (7.05pc)
Some discretion is evidently advisable when the $z$'s are chosen. But the
four-point method is good enough to obtain satisfactory approximations to
any curve we want, provided that we break the desired curve into short
enough segments and give four suitable control points for each segment.
It turns out, in fact, that we can usually get by with only a few segments.
For example, the four-point method can produce an approximate
quarter-circle with less than 0.06\% error; it never yields an exact
circle, but the differences between four such quarter-circles and a true
circle are imperceptible.

All of the curves that METAFONT\ draws are based on four points, as just
described. But it isn't necessary for a user to specify all of those
points, because the computer is usually able to figure out good values of
$z_2$ and $z_3$ by itself. Only the endpoints $z_1$ and $z_4$, through
which the curve is actually supposed to pass, are usually mentioned
explicitly in a METAFONT\ program.

For example, let's return to the six points that were used to introduce the
ideas of coordinates in Chapter 2. We said '@draw@ $z_1\to z_6$' in that
chapter, in order to draw a straight line from point $z_1$ to point $z_6$.
In general, if three or more points are listed instead of two, METAFONT\ will draw a
smooth curve through all the points. For example, the commands
'@draw@ $z_4\to z_1\to z_2\to z_6$' and '@draw@ $z_5\to z_4\to z_1
\to z_3\to z_6\to z_5$' will produce the respective results
\displayfig 3e (7.75pc)
(Unlabeled points in these diagrams are that METAFONT\ has
supplied automatically so that it can use the four-point scheme to draw
curves between each pair of adjacent points on the specified paths.)

Notice that the curve is not smooth at $z_5$ in the right-hand example,
because $z_5$ appears at both ends of that particular path. In order to
get a completely smooth curve that returns to its starting point, you can
say '@draw@ $z_5\to z_4\to z_1\to z_3\to z_6\to \cycle$' instead:
\displayfig 3f (7.25pc)
The word '' at the end of a path refers to the starting point
of that path.
METAFONT\ believes that this
is the nicest way to connect the given points in the given cyclic order;
but of course there are many decent curves that satisfy the specifications,
and you may have another one in mind. You can obtain finer control
by giving hints to the machine in various ways. For example, the
bean curve can be "pulled tighter" between $z_1$ and $z_3$ if you say

>
@draw@ $z_5\to z_4\to z_1\to\tension1.2\to z_3\to z_6\to \cycle$;

the so-called between points is normally 1, and an increase
to 1.2 yields
\displayfig 3g (5.75pc)

**[Dangerous Bend]** An asymmetric effect can be obtained by increasing the tension
only at point 1 but not at points 3 or 4; the shape
\displayfig 3h (6.5pc)
comes from

'@draw@ $z_5\to z_4\to\tension1\and1.5\to z_1\to
\tension1.5\and1\to z_3\to z_6\to \cycle$'.
The effect of tension has been achieved in this example by moving two of
the anonymous control points closer to point 1.

It's possible to control a curve in another way, by telling METAFONT\ what
direction to travel at some or all of the points. Such directions are
given inside curly braces; for example,

>
@draw@ $z_5\to z_4\{"left"\}\to z_1\to z_3\to z_6\{"left"\}\to\cycle$

says that the curve should be traveling leftward at points 4 and 6. The
resulting curve is perfectly straight from $z_6$ to $z_5$ to $z_4$:
\displayfig 3i (5.8pc)
We will see later that '"left"' is an abbreviation for the vector $(-1,0)$,
which stands for one unit of travel in a leftward direction. Any desired
direction can be specified by enclosing a vector in $\{\ldots\}$'s; for
example, the command '@draw@ $z_4\to z_2\{z_3-z_4\}\to z_3$' will draw a
curve from $z_4$ to $z_2$ to $z_3$ such that the tangent direction at
$z_2$ is parallel to the line $z_4\to z_3$, because $z_3-z_4$ is the
vector that represents travel from $z_4$ to $z_3$:
\displayfig 3j (4.7pc)
The same result would have been obtained from a command such as '@draw@
$z_4\to z_2 \{10(z_3-z_4)\}\to z_3$', because the vector $10(z_3-z_4)$ has
the same direction as $z_3-z_4$. METAFONT\ ignores the magnitudes of vectors
when they are simply being used to specify directions.

### Exercise
What do you think will be the result of
'@draw@ $z_4\to z_2\{z_4-z_3\}\to z_3$', when points $z_2$, $z_3$, $z_4$
are the same as they have been in the last several examples?

#### Answer
The direction at $z_2$ is parallel to the line $z_4\to z_3$, but
the vector $z_4-z_3$ specifies a direction towards $z_4$, which is
$180^\circ$ different from the direction $z_3-z_4$ that was discussed in
the text. Thus, we have a difficult specification to meet, and METAFONT\ draws
a pretzel-shaped curve that loops around in a way that's too ugly to show
here. The first part of the path, from $z_4$ to $z_2$, is mirror symmetric
about the line $z_1\to z_5$ that bisects $z_4\to z_2$, so it starts out in a
south-by-southwesterly direction; the second part is mirror symmetric about
the vertical line that bisects $z_2\to z_3$, so when the curve ends at $z_3$
it's traveling roughly northwest. The moral is: Don't specify a direction
that runs opposite to (i.e., is the negative of) the one you really want.

### Exercise
Explain how to get METAFONT\ to draw the wiggly shape
\displayfig 3k (5pc)
in which the curve aims directly at point 2 when it's at point 6, but
directly away from point 2 when it's at point 4. [*Hint:* No
tension changes are needed; it's merely necessary to specify directions
at $z_4$ and $z_6$.]

#### Answer
@draw@ $z_5\to z_4\{z_4-z_2\}\to z_1\to z_3\to z_6\{z_2-z_6\}
\to\cycle$.

METAFONT\ allows you to change the shape of a curve at its endpoints by
specifying different amounts of "." For example, the two commands

>
@draw@ $z_4\{\curl0\}\to z_2\{z_3-z_4\}\to\{\curl0\}\,z_3$;
@draw@ $z_4\{\curl2\}\to z_2\{z_3-z_4\}\to\{\curl2\}\,z_3$

give the respective curves
\displayfig 3l (5pc)
which can be compared with the one shown earlier when no special curl was
requested. \ (The specification '$\curl1$' is assumed at an endpoint
if no explicit curl or direction has been mentioned, just as
'$\tension1$' is implied between points when no tension has
been explicitly given.) \ Chapter 14 explains more about this.

It's possible to get curved lines instead of straight lines even when
only two points are named, if a direction has been prescribed at one or
both of the points. For example,

>
@draw@ $z_4\{z_2-z_4\}\to\{"down"\}\,z_6$

asks METAFONT\ for a curve that starts traveling towards $z_2$ but finishes
in a downward direction:
\displayfig 3m (4pc)

**[Dangerous Bend]** Here are some of the curves that METAFONT\ draws between two points, when
it is asked to move outward from the left-hand point at an angle of
$60^\circ$, and to approach the right-hand point at various angles:
\displayfig 3aa (2.6cm)
This diagram was produced by the METAFONT\ program ^^@for@ ^^@step@ ^^@until@ ^^"cm"

>
@for@ $d=0$ @step@ 10 @until@ 120:
\indent @draw@ $(0,0)\{dir\,60\}\to\{dir\,-d\}(6"cm",0)$;
@endfor@;

the '' function specifies a direction measured in degrees
counterclockwise from a horizontal rightward line, hence '$dir\,-d$'
gives a direction that is $d^\circ$ below the horizon. The lowest curves
in the illustration correspond to small values of $d$, and the highest
curves correspond to values near $120^\circ$.

**[Dangerous Bend]** A car that drives along the upper paths in the diagram above
is always turning to the right, but in the lower paths it comes to a
point where it needs to turn to the left in order to reach its destination
from the specified direction.
The place where a path changes its curvature from right to left or
vice versa is called an "." METAFONT\ introduces
inflection points when it seems better to change the curvature than
to make a sharp turn; indeed, when $d$ is negative there is no way to
avoid points of inflection, and the curves for small positive $d$ ought to
be similar to those obtained when $d$ has small negative values. The program

>
@for@ $d=0$ @step@ $-10$ @until@ $-90$:
\indent @draw@ $(0,0)\{dir\,60\}\to\{dir\,-d\}(6"cm",0)$;
@endfor@

shows what METAFONT\ does when $d$ is negative:
\displayfig 3bb (2.8cm)

**[Dangerous Bend]** It is sometimes desirable to avoid points of inflection, when $d$ is
positive, and to require the curve to remain inside the triangle
determined by its initial and final directions. This can be achieved

by using three dots instead of two when you specify a curve: The program

>
@for@ $d=0$ @step@ 10 @until@ 120:
\indent @draw@ $(0,0)\{dir\,60\}\ldots\{dir\,-d\}(6"cm",0)$;
@endfor@

generates the curves
\displayfig 3cc (2.6cm)
which are the same as before except that inflection points do not occur
for the small values of $d$. The '$\ldots$' specification keeps the
curve "" inside the triangle that is defined by the endpoints
and directions; but it has no effect when there is
no such triangle. More precisely, suppose that the curve goes from $z_0$
to $z_1$; if there's a point $z$ such that the initial direction is from
$z_0$ to $z$ and the final direction is from $z$ to $z_1$, then the curve
specified by '$\ldots$' will stay entirely within the triangle whose
corners are $z_0$, $z_1$, and $z$. But if there's no such triangle
(e.g., if $d<0$ or $d>120$ in our example program), both '$\ldots$'
and '$\to$' will produce the same curves.

In this chapter we have seen lots of different ways to get METAFONT\ to draw
curves. And there's one more way, which subsumes all of the others.
If changes to tensions, curls, directions, and/or boundedness
aren't enough to produce the sort of curve that a person wants, it's
always possible as a last resort to specify all four of the points in the
four-point method. For example, the command

>
@draw@ $z_4\to\controls z_1\and z_2\to z_6$

will draw the following curve from $z_4$ to $z_6$:
\displayfig 3n (5pc)

\endchapter

And so I think I have omitted nothing

that is necessary to an understanding of curved lines.

> --- REN\'E , *La G\'eom\'etrie* (1637)

Rules or substitutes for the artist's hand must necessarily be inadequate,
although, when set down by such men as
, , , , and others,
they probably do establish canons of proportion and construction
which afford a sound basis upon which to present new expressions.

> --- FREDERIC W. , *Typologia* (1940)


# Chapter 4. Pens

Our examples so far have involved straight lines or curved lines that look
as if they were drawn by a felt-tip , where the of that pen
was perfectly round. A mathematical "line" has no thickness, so it's
invisible; but when we plot circular dots at each point of an infinitely
thin line, we get a visible line that has constant thickness.

Lines of constant thickness have their uses, but METAFONT\ also provides
several other kinds of scrivener's tools, and we shall take a look at some
of them in this chapter. We'll see not only that the sizes and shapes of
pen nibs can be varied, but also that characters can be built up in such a
way that the outlines of each stroke are precisely controlled.

First let's consider the simplest extensions of what we have seen before.
The letter '{\manual\Aa}' of Chapter 2 and the kidney-
'\kk{\manual\beana}\kk' of Chapter 3 were drawn with circular pen nibs of
diameter $0.4\pt$, where 'pt' stands for a printer's point;\footnote*{$
1\,in=2.54\,cm=72.27\pt$ exactly, as explained in
*The TeX book*.} $0.4\pt$ is the standard thickness of a ruled line
'$\,\vcenter{\hrule width 2em}\,$' drawn by TeX. Such a penpoint can be
specified by telling METAFONT\ to

>
\pickup @pencircle@ $0.4"pt"$;

METAFONT\ will use the pen it has most recently picked up ^^@pickup@
whenever it is asked to '^@draw@' anything. A ^@pencircle@ is a
circular pen whose diameter is the width of one pixel. Scaling it
by $0.4"pt"$ will change it to the size that corresponds
to $0.4\pt$ in the output, because ^"pt" is the number of pixels
in $1\pt$. If the key points $(z_1,z_2,z_3,z_4,z_5,z_6)$ of Chapters 2 and 3
have already been defined, the METAFONT\ commands

>
\pickup @pencircle@ scaled $0.8"pt"$;
@draw@ $z_5\to z_4\to z_1\to z_3\to z_6\to \cycle$

will produce a bean shape twice as thick as before: '\kk{\manual\beanb}\kk'
instead of '\kk{\manual\beana}\kk'.

More interesting effects arise when we use non-circular pen nibs. For example,
the command

>
\pickup @pencircle@ $0.8"pt"$ $0.2"pt"$

picks up a pen whose tip has the shape of an ellipse, $0.8\pt$ wide and
$0.2\pt$ tall; magnified 10 times, it looks like this:
'$\,\vcenter{{\manual\niba}}\,$'.
\ (The operation of "xscaling" multiplies $x$ coordinates by a specified
amount but leaves $y$ coordinates unchanged, and the operation of
"yscaling" is similar.) \ Using such a pen, the '\kk{\manual\beana}\kk'
becomes '\kk{\manual\beanc}\kk', and '{\manual\Aa}' becomes '{\manual\Ab}'.
Furthermore,

>
\pickup @pencircle@ xscaled $0.8"pt"$ yscaled $0.2"pt"$ 30

takes that ellipse and rotates it $30^\circ$ counterclockwise, obtaining the nib
'$\vcenter{{\manual\nibb}}$'; this changes '\kk{\manual\beanc}\kk' into
'\kk{\manual\beand}\kk' and '{\manual\Ab}' into '{\manual\Ac}'. An
enlarged view of the bean shape shows more clearly what is going on:
\displayfig 4a (7pc)
The right-hand example was obtained by eliminating the clause
'yscaled $0.2"pt"$'; this makes the pen almost razor thin, only
one pixel tall before rotation.

### Exercise
Describe the pen shapes defined by
(a) @pencircle@ xscaled $0.2"pt"$ yscaled $0.8"pt"$;
\ (b) @pencircle@ scaled $0.8"pt"$ rotated 30;
\ (c) @pencircle@ xscaled .25 scaled $0.8"pt"$.

#### Answer
(a) An ellipse $0.8\pt$ tall and $0.2\pt$ wide
('$\,\vcenter{{\manual\nibc}}\,$');
\ (b) a circle of diameter $0.8\pt$ (rotation doesn't change a circle!);
\ (c) same as (a).

### Exercise
We've seen many examples of '^@draw@'
used with two or more points. What do you think METAFONT\ will do
if you ask it to perform the following commands?

>
@draw@ $z_1$; \ @draw@ $z_2$; \ @draw@ $z_3$; \ @draw@ $z_4$;
\ @draw@ $z_5$; \ @draw@ $z_6$.

#### Answer
Six individual points will be drawn, instead of lines or curves.
These points will be drawn with the current pen. However, for technical
reasons explained in Chapter 24, the @draw@ command does its best work when it
is moving the pen; the pixels you get at the endpoints of curves are
not always what you would expect, especially at low resolutions. It is
usually best to say '^@drawdot@' instead of '@draw@' when you are drawing
only .

={
{{ to 208\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4b{208\apspix}{216\apspix}

to 208\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt

\hangindent-125pt \hangafter4
\indent\vadjust{\box0}
Let's turn now to the design of a real letter that has already appeared
many times in this manual, namely the '{\manual }' of
'METAFONT'. All seven of the distinct letters in 'METAFONT' will
be used to illustrate various ideas as we get into the details of the
language; we might as well start with '{\manual T}',
because it occurs twice, and (especially) because it's the simplest. An
enlarged version of this letter is shown at the right of this paragraph,
including the locations of its four key points $(z_1,z_2,z_3,z_4)$ and its
. Typesetting systems like TeX\ are based on the
assumption that each character fits in a rectangular ; we shall
discuss boxes in detail later, but for now we will be content simply to
know that such boundaries do exist.\footnote*{Strictly speaking, the
bounding box doesn't actually have to "bound" the black pixels of a
character; for example, the '{\manual q}' protrudes
slightly below the baseline at point 4, and italic letters frequently
extend rather far to the right of their boxes. However, TeX\ positions
all characters by lumping boxes together as if they were pieces of metal
type that contain all of the ink.} Numbers $h$ and $w$ ^^"h" ^^"w" will
have been computed so that the corners of the box are at positions
$(0,0)$, $(0,h)$, $(w,0)$, and $(w,h)$ as shown.

\hangindent-125pt
\hangafter\prevgraf \hangafter by -16
Each of the letters in 'METAFONT' is drawn with a pen whose nib is an unrotated
ellipse, 90\% as tall as it is wide. In the 10-point size, which is used
for the main text of this book, the pen is $2/3\pt$ wide, so it has
been specified by the command

>
\pickup @pencircle@ scaled $2\over3$"pt" yscaled $9\over10$

or something equivalent to this.

We shall assume that a special value '$o$' has been computed so that the
bottom of the vertical stroke in '{\manual T}' should
descend exactly $o$ pixels below the baseline; ^^"o" this is called the
amount of "." Given $h$, $w$, and $o$, it is a simple matter
to define the four key points and to draw the
'{\manual T}': ^^"top" ^^"lft" ^^"rt" ^^"bot"

>
$"top"\,"lft"\,z_1=(0,h)$; $"top"\,"rt"\,z_2=(w,h)$;
$"top"\,z_3=(.5w,h)$; $"bot"\,z_4=(.5w,-o)$;
@draw@ $z_1\to z_2$; @draw@ $z_3\to z_4$.

**[Dangerous Bend]** Sometimes it is easier and/or clearer to define the $x$ and $y$
separately. For example, the key points of
the '{\manual j}'
could also be specified thus:

>
$"lft"\,x_1=0$;&$w-x_2=x_1$;&$x_3=x_4=.5w$;
$"top"\,y_1=h$;&$"bot"\,y_4=-o$;&$y_1=y_2=y_3$.

The equation $w-x_2=x_1$ expresses the fact that $x_2$ is just as far from
the right edge of the bounding box as $x_1$ is from the left edge.

**[Dangerous Bend]** What exactly does '"top"\!' mean in a METAFONT\ equation? If the
currently-picked-up pen extends $l$ pixels to the left of its center,
$r$ pixels to the right, $t$ pixels upward and $b$ downward, then

>
$"top"\,z=z+(0,t)$,&$"bot"\,z=z-(0,b)$,&
$"lft"\,z=z-(l,0)$,&$"rt"\,z=z+(r,0)$,
{\vskip\belowdisplayskip
{
when $z$ is a pair of coordinates. But---as the previous paragraph
shows, if you study it carefully---we also have
}\vskip\abovedisplayskip}
$"top"\,y=y+t$,&$"bot"\,y=y-b$,&
$"lft"\,x=x-l$,&$"rt"\,x=x+r$,

when $x$ and $y$ are single values instead of coordinate pairs.
You shouldn't apply '"top"\!' or '"bot"\!' to $x$ coordinates,
nor '"lft"\!' or '"rt"\!' to $y$ coordinates.

**[Dangerous Bend]** exercise True or false: $"top"\,"bot"\,z=z$, whenever $z$
is a pair of coordinates.

#### Answer
True, for all of the pens discussed so far. But false in general,
since we will see later that pens might extend further upward than
downward; i.e., $t$ might be unequal to $b$ in the equations for
"top" and "bot".

={
{{ to 288\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4c{288\apspix}{216\apspix}

to 288\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt
\decreasehsize 165pt

**[Dangerous Bend]** exercise An enlarged \vadjust{\box0}
picture of METAFONT's '{\manual h}' shows that it has five key points. Assuming
that special values "ss" and "ygap" have been precomputed and that the equations

>
$x_1="ss"=w-x_5$;$y_3-y_1="ygap"$

have already been given, what further equations and '@draw@' ^^METAFONT
logo commands will complete the specification of this letter? \ (The
value of $w$ will be greater for '{\manual h}' than it was
for '{\manual j}'; it
stands for the pixel width of whatever character is currently being drawn.)

#### Answer
$x_2=x_1$; $x_3={1\over2}[x_2,x_4]$; $x_4=x_5$; $"bot"\,y_1=-o$;
$"top"\,y_2=h+o$; $y_4=y_2$; $y_5=y_1$; @draw@ $z_1\to z_2$;
@draw@ $z_2\to z_3$; @draw@ $z_3\to z_4$; @draw@ $z_4\to z_5$.
We will learn later that the four @draw@ commands can be replaced by

>
@draw@ $z_1\dashto z_2\dashto z_3\dashto z_4\dashto z_5$;

in fact, this will make METAFONT\ run slightly faster.

METAFONT's ability to '@draw@' allows it to produce character shapes that are
satisfactory for many applications, but the shapes are inherently limited
by the fact that the simulated pen nib must stay the same through an
entire stroke. Human penpushers are able to get richer effects by
using different amounts of pressure and/or by rotating the pen as they draw.

We can obtain finer control over the characters we produce if we specify
their outlines, instead of working only with key points that lie somewhere
in the middle. In fact, METAFONT\ works internally with outlines, and the
computer finds it much easier to fill a region with solid black than to
figure out what pixels are blackened by a moving pen. There's a '^@fill@'
command that does region filling; for example, the solid shape
\displayfig 4d (6.5pc)
can be obtained from our six famous example points by giving the command

>
@fill@ $z_5\to z_4\to z_1\to z_3\to z_6\to \cycle$.

The filled region is essentially what would be cut out by an
infinitely sharp blade if it traced over the given curve while
cutting a piece of thin film. A @draw@ command needs to add thickness to
its curve, because the result would otherwise be invisible; but a @fill@
command adds no thickness.

The curve in a @fill@ command must end with '', because an
entire region must be filled. It wouldn't make sense to say, e.g.,
'@fill@ $z_1\to z_2$'. The cycle being filled shouldn't cross itself,
either; METAFONT\ would have lots of trouble trying to figure out how to
obey a command like '@fill@ $z_1\to z_6\to z_3\to z_4\to\cycle$'.

**[Dangerous Bend]** exercise Chapter 3 discusses the curve $z_5\to z_4\to z_1\to
z_3\to z_6\to z_5$, which isn't smooth at $z_5$. Since this curve
doesn't end with 'cycle', you can't use it in a @fill@ command.
But it does define a closed region. How can METAFONT\ be instructed
to fill that region?

#### Answer
Either say '@fill@ $z_5\to z_4\to z_1\to z_3\to z_6\to z_5\to
\cycle$', which doubles point $z_5$ and abandons smoothness there,
or '@fill@ $z_5\{\curl1\}\to z_4\to z_1\to z_3\to z_6\to
\{\curl1\}\cycle$'. In the latter case you can omit either one of
the specifications, but not both.

The black '{\manual}' that appears in the statement of
exercises in this book was drawn with the command

>
@fill@ $z_1\dashto z_2\dashto z_3\dashto\cycle$

after appropriate corner points $z_1$, $z_2$, and $z_3$ had been specified.
In this case the outline of the region to be filled was specified in terms
of the symbol '$\dashto$' instead of '$\to$';
this is a convention we haven't discussed before. Each '$\dashto$'
introduces a straight line segment, which is independent of the rest of

the path that it belongs to; thus it is quite different from '$\to$', which
specifies a possibly curved line segment that connects smoothly with neighboring
points and lines of a path. In this case '$\dashto$' was used so that the
triangular region would have straight edges and sharp corners. We might say
informally that '$\to$' means "Connect the points with a nice curve,"
while '$\dashto$' means "Connect the points with a straight line."

={
{{ to 180\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4e{180\apspix}{225\apspix}

to 180\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt
\decreasehsize 111pt

**[Dangerous Bend]** \vadjust{\box0}
The corner points $z_1$, $z_2$, and $z_3$ were defined carefully
so that the triangle would be , i.e., so that all three
of its sides would have the same length. Since an equilateral triangle
has $60^\circ$ angles, the following equations did the job:

>
$x_1=x_2=w-x_3=s$;
$y_3=.5h$;
$z_1-z_2=(z_3-z_2)$ 60.

Here $w$ and $h$ represent the character's width and height, and $s$ is
the distance of the triangle from the left and right edges of the type.

**[Dangerous Bend]** The @fill@ command has a companion called ^@unfill@, which changes
pixels from black to white inside a given region. For example, the solid
bean shape on the previous page can be changed to
\displayfig 4f (6.5pc)
if we say also '@unfill@ ${1\over4}[z_4,z_2]\to{3\over4}[z_4,z_2]\to\cycle$;
\ @unfill@ ${1\over4}[z_6,z_2]\to{3\over4}[z_6,z_2]\to\cycle$'.
This example shows, incidentally, that METAFONT\ converts a two-point specification
like '$z_1\to z_2\to\cycle$' into a more-or-less circular path, even though
two points by themselves define only a straight line.

**[Dangerous Bend]** exercise Let $z_0$ be the point $(.8[x_1,x_2],.5[y_1,y_4])$,
and introduce six new points by letting $z'_k=.2[z_k,z_0]$ for $k=1,$ 2,
\dots, 6. Explain how to obtain the shape
\displayfig 4g (7.0pc)
in which the interior region is defined by $z'_1\ldots z'_6$ instead of
by $z_1\ldots z_6$.

#### Answer
After the six original points have been defined, say

>
@fill@ $z_5\to z_4\to z_1\to z_3\to z_6\to\cycle$;
$z_0=(.8[x_1,x_2],.5[y_1,y_4])$;
@for@ $k=1$ @upto@ 6: $z[k]'=.2[z[k],z_0]$; @endfor@
@unfill@ $z_5'\to z_4'\to z_1'\to z_3'\to z_6'\to\cycle$.

The ability to fill between outlines makes it possible to pretend that we
have that change in direction and pressure as they
glide over the paper, if we consider the separate paths traced out by the
pen's left edge and right edge. For example, the stroke
\displayfig 4h (3.5pc)
can be regarded as drawn by a pen that starts at the left, inclined
at a $30^\circ$ angle; as the pen moves, it turns gradually until its
edge is strictly vertical by the time it reaches the
right end. The pen motion was horizontal at positions 2 and 3. This stroke
was actually obtained by the command

>
@fill@ $z_1l\to z_2l\{"right"\}\to\{"right"\}\,z_3l$
$\dashto z_3r\{"left"\}\to\{"left"\}\,z_2r\to z_1r$
$\dashto\cycle$;

i.e., METAFONT\ was asked to fill a region bounded by a "left path" from
$z_1l$ to $z_2l$ to $z_3l$, followed by a straight line
to $z_3r$, then a reversed "right path" from $z_3r$ to $z_2r$ to
$z_1r$, and finally a straight line back to the starting point $z_1l$.

Key positions of the "pen" are represented in this example by sets of
three points, like $(z_1l,z_1,z_1r)$, which stand for the pen's left edge,
its midpoint, and its right edge. The midpoint doesn't actually occur in the
specification of the outline, but we'll see examples of its usefulness.
The relationships between such triples of points are established by a
'^"penpos"' command, which states the breadth of the pen and its angle of
inclination at a particular position. For example, positions 1, 2, and 3
in the stroke above were established by saying

>
$\penpos1(1.2"pt",30)$;&
$\penpos2(1.0"pt",45)$;&
$\penpos3(0.8"pt",90)$;

this made the pen $1.2\pt$ broad and tipped $30^\circ$ with respect to
the horizontal at position 1, etc. In general the idea is to specify
'$\penpos k(b,d)$',
where $k$ is the position number or position name, $b$ is the breadth (in
pixels), and $d$ is the angle (in degrees). Pen angles are measured
counterclockwise from the horizontal. Thus, an angle of 0 makes the right
edge of the pen exactly $b$ pixels to the right of the left edge; an angle
of 90 makes the right pen edge exactly $b$ pixels above the left; an angle
of $-90$ makes it exactly $b$ pixels below. An angle of 45 makes the right
edge $b/{\sqrt2}$ pixels above and $b/{\sqrt2}$ pixels to the right of the
left edge; an angle of $-45$ makes it $b/{\sqrt2}$ pixels below and
$b/{\sqrt2}$ to the right. When the pen angle is between $90^\circ$ and
$180^\circ$, the "right" edge actually lies to the left of the "left"
edge. In terms of on a conventional map, an angle
of $0^\circ$ points due East, while $90^\circ$ points North and $-90^\circ$
points South. The angle corresponding to Southwest is $-135^\circ$,
also known as $+225^\circ$.

### Exercise
What angle corresponds to the direction North-Northwest?

#### Answer
${1\over2}\bigl["North",{1\over2}["North","West"]\bigr]=
{1\over2}\bigl[90,{1\over2}[90,180]\bigr]={1\over2}[90,135]=112.5$.

\decreasehsize 9pc

### Exercise
\xdef\circlex{4.\exno}
\rightfig 4i (7pc x 7pc) ^20pt
What are the pen angles at positions 1, 2, 3, and 4 in
the circular shape shown here? [*Hint:* Each angle is a multiple
of $30^\circ$. Note that $z_3r$ lies to the left of $z_3l$.]

#### Answer
$30^\circ$, $60^\circ$, $210^\circ$, and $240^\circ$. Since it's
possible to add or subtract $360^\circ$ without changing the meaning,
the answers $-330^\circ$, $-300^\circ$, $-150^\circ$, and $-120^\circ$
are also correct.

### Exercise
What are the coordinates of $z_1l$ and $z_1r$ after the
command '$\penpos1(10,-90)$', if $z_1=(25,25)$?

#### Answer
$z_1l=(25,30)$, $z_1r=(25,20)$.

**[Dangerous Bend]** The statement '$\penpos k(b,d)$' is simply an abbreviation for
two equations, '$z_k={1\over2}[z_kl,z_kr]$' and
'$z_kr=z_kl+(b,0)$ $d\,$'. You might want to use other
equations to define the relationship between $z_kl$, $z_k$, and
$z_kr$, instead of giving a "penpos" command, if an alternative
formulation turns out to be more convenient.

After '"penpos"' has specified the relations between three points, we still
don't know exactly where they are; we only know their positions relative
to each other. Another equation or two is needed in order to fix the
horizontal and vertical locations of each triple. For example, the three
"penpos" commands that led to the pen stroke on the previous page were
accompanied by the equations

>
$z_1=(0,2"pt")$;&$z_2=(4"pt",0)$;&$x_3=9"pt"$;&$y_3l=y_2r$;

these made the information complete. There should be one $x$ equation and
one $y$ equation for each position; or you can use a $z$ equation, which
defines both $x$ and $y$ simultaneously.

It's a nuisance to write long-winded @fill@ commands when broad-edge
pens are being simulated in this way, so METAFONT\ provides a convenient
abbreviation: You can write simply

>
^@penstroke@ $z_1e\to z_2e\{"right"\}\to\{"right"\}\,z_3e$

instead of the command '@fill@ $z_1l\to
z_2l\{"right"\}\to\{"right"\}\,z_3l \dashto
z_3r\{"left"\}\to\{"left"\}\,z_2r\to z_1r\dashto\cycle$' that was
stated earlier. The letter '$e$' ^^"e" stands for the pen's edge. A @penstroke@
command fills the region '$p.l\dashto \reverse p.r\dashto\cycle$', where
$p.l$ and $p.r$ are the left and right paths formed by changing each '$e$'
into '$l$' or '$r$', respectively.

**[Dangerous Bend]** The @penstroke@ abbreviation can be used to draw cyclic paths
as well as ordinary ones. For example, the circle in exercise \circlex\
was created by saying simply '@penstroke@ $z_1e\to z_2e\to z_3e\to
z_4e\to\cycle$'. This type of penstroke essentially expands into

>
@fill@ $z_1r\to z_2r\to z_3r\to z_4r\to\cycle$;
@unfill@ $z_1l\to z_2l\to z_3l\to z_4l\to\cycle$;

or the operations '@fill@' and '@unfill@' are reversed, if points
$(z_1r,z_2r, z_3r,z_4r)$ are on the inside and
$(z_1l,z_2l,z_3l,z_4l)$ are on the outside.

**[Dangerous Bend]** exercise The circle of exercise \circlex\ was actually drawn with
a slightly more complicated @penstroke@ command than just claimed: The
edges of the curve were forced to be vertical at
positions 1 and 3, horizontal at 2 and 4. How did the author do this?

#### Answer
He said '@penstroke@
$z_1e\{"up"\}\to z_2e\{"left"\}\to z_3e\{"down"\}
\to z_4e\{"right"\}\to\cycle$'.

={
{{ to 126\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4j{126\apspix}{252\apspix}

to 126\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt

\hangindent-100pt \hangafter2
\indent\vadjust{\box0}
Here's an example of how this new sort of pen can be used to draw a
sans-serif letter '{\manual\IOI}'. As usual, we assume
that two variables, $h$ and $w$, have been set up to give the height and
width of the character in pixels. We shall also assume that there's a
"stem" parameter, which specifies the nominal pen breadth. The breadth
decreases to .9"stem" in the middle of the stroke, and the
pen angle changes from $15^\circ$ to $10^\circ$:

>
$\penpos1("stem",15)$; \ $\penpos2(.9"stem",12)$;
$\penpos3("stem",10)$; \ $x_1=x_2=x_3=.5w$;
$y_1=h$; \ $y_2=.55h$; \ $y_3=0$;
$x_2l:={1\over6}[x_2l,x_2]$;
@penstroke@ $z_1e\to z_2e\{"down"\}\to z_3e$.

Setting $x_1=x_2=x_3=.5w$ centers the stroke; setting $y_1=h$ and $y_3=0$
makes it sit in the type box, protruding just slightly at the top and bottom.

The second-last line of this program is something that we haven't seen
before: It resets $x_2l$ to a value 1/6 of the way towards the center
of the pen, thereby making the stroke a bit at the left.
The '$:=$' operation is called an ; we shall
study the differences between '$:=$' and '$=$' in Chapter 10.

**[Dangerous Bend]** It is important to note that these simulated pens
have a serious limitation compared to the way a real calligrapher's pen
works: The left and right edges of a "penpos"-made pen must never cross,
hence it is necessary to turn the pen when going around a curve.
Consider, for example, the following two curves:
\displayfig 4k (6pc)
The left-hand circle was drawn with a broad-edge pen of fixed breadth,
held at a fixed angle; consequently the left edge of the pen was responsible
for the outer boundary on the left, but the inner boundary on the right.
\ (This curve was produced by saying '\pickup @pencircle@ xscaled 0.8"pt"
rotated 25; @draw@ $z_1\to z_2\to\cycle$'.) \ The right-hand shape
was produced by '$\penpos1(0.8"pt",25)$; $\penpos2(0.8"pt",25)$;
@penstroke@ $z_1e\to z_2e\to\cycle$'; important chunks of the shape
are missing at the crossover points, because they don't lie on either of
the circles $z_1l\to z_2l\to\cycle$ or $z_1r\to z_2r\to\cycle$.

**[Dangerous Bend]** To conclude this chapter we shall improve the character
{\manual\hexb} of Chapter 2, which is too dark in the middle because it has
been drawn with a pen of uniform thickness. The main trouble with unvarying
pens is that they tend to produce black blotches where two strokes meet,
unless the pens are comparatively thin or unless the strokes are nearly
perpendicular. We want to thin out the lines at the center just enough
to cure the darkness problem, without destroying the illusion that the lines
still seem (at first glance) to have uniform thickness.

={
{{ to 200\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4l{200\apspix}{100\apspix}

to 200\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt

**[Dangerous Bend]** \vadjust{\box0}
It isn't difficult to produce '
{\manual\hexe\hexe\hexe\hexe\hexe\hexe\hexe\hexe\hexe\hexe}'
instead of '
{\manual\hexb\hexb\hexb\hexb\hexb\hexb\hexb\hexb\hexb\hexb}'
when we work with dynamic pens:

>
\pickup @pencircle@ scaled $b$;
$"top"\,z_1=(0,h)$; \ $"top"\,z_2=(.5w,h)$; \ $"top"\,z_3=(w,h)$;
$"bot"\,z_4=(0,0)$; \ $"bot"\,z_5=(.5w,0)$; \ $"bot"\,z_6=(w,0)$; \
@draw@ $z_2\to z_5$;
$z_1'=.25[z_1,z_6]$; \ $z_6'=.75[z_1,z_6]$; \
$z_3'=.25[z_3,z_4]$; \ $z_4'=.75[z_3,z_4]$;
$"theta"_1:=\angle(z_6-z_1)+90$;
$"theta"_3:=\angle(z_4-z_3)+90$;
$\penpos1'(b,"theta"_1)$; \ $\penpos6'(b,"theta"_1)$;
$\penpos3'(b,"theta"_3)$; \ $\penpos4'(b,"theta"_3)$;
$\penpos7(.6b,"theta"_1)$; \ $\penpos8(.6b,"theta"_3)$;
$z_7=z_8=.5[z_1,z_6]$;
@draw@ $z_1\to z_1'$; \ @draw@ $z_6'\to z_6$;
@draw@ $z_3\to z_3'$; \ @draw@ $z_4'\to z_4$;
@penstroke@ $z_1'e\{z_6'-z_1'\}\to z_7e\to\{z_6'-z_1'\}z_6'e$;
@penstroke@ $z_3'e\{z_4'-z_3'\}\to z_8e\to\{z_4'-z_3'\}z_4'e$.

Here $b$ is the diameter of the pen at the terminal points;
'' computes the direction angle of a given vector.
Adding $90^\circ$ to a direction angle gives a
direction (see the definitions of $"theta"_1$ and $"theta"_3$).
It isn't necessary to take anything off of the vertical stroke $z_2\to z_5$,
because the two diagonal strokes fill more than the width of the vertical
stroke at the point where they intersect.

={
{{ to 200\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox4m{200\apspix}{105\apspix}

to 200\apspix{\hidecoords(0,0)
\hidecoords(w\mkern-2mu,0)}}}}
=0pt

\decreasehsize 125pt

**[Dangerous Bend]** exercise \vadjust{\box0}
Modify the hex character so that its ends are cut
sharply and confined to the bounding box, as shown.

#### Answer
We use angles to $(w,h)$ and $(w,-h)$ at the
diagonal endpoints:

>
$x_1l=x_4l=0$;
$x_2=x_5=.5w$;
$x_3r=x_6r=w$;
$y_1r=y_2=y_3l=h$;
$y_4r=y_5=y_6l=0$;
$z_1'=.25[z_1,z_6]$; \ $z_6'=.75[z_1,z_6]$;
$"theta"_1:=\angle(w,-h)+90$;
$\penpos1(b,"theta"_1)$; \ $\penpos6(b,"theta"_1)$;
$z_7=.5[z_1,z_6]$; \ $\penpos7(.6b,"theta"_1)$;
$\penpos1'(b,"theta"_1)$; \ $\penpos6'(b,"theta"_1)$;
@penstroke@ $z_1e\to z_1'e\{z_6'-z_1'\}\to z_7e\to
\{z_6'-z_1'\}z_6'e\to z_6e$;
$z_3'=.25[z_3,z_4]$; \ $z_4'=.75[z_3,z_4]$;
$"theta"_3:=\angle(-w,-h)+90$;
$\penpos3(b,"theta"_3)$; \ $\penpos4(b,"theta"_3)$;
$z_8=.5[z_1,z_6]$; \ $\penpos8(.6b,"theta"_3)$;
$\penpos3'(b,"theta"_3)$; \ $\penpos4'(b,"theta"_3)$;
@penstroke@ $z_3e\to z_3'e\{z_4'-z_3'\}\to z_8e\to
\{z_4'-z_3'\}z_4'e\to z_4e$;
$\penpos2(b,0)$; \ $\penpos5(b,0)$; \ @penstroke@ $z_2e\to z_5e$.

\endchapter

It is very important that the nib be cut "sharp,"
and as often as its edge wears blunt it must be resharpened.
It is impossible to make "clean cut" strokes with a blunt pen.
or EDWARD , *Writing \& Illuminating,
\& Lettering* (1906)

I might compare the high-speed computing machine
to a remarkably large and awkward pencil
which takes a long time to sharpen and
cannot be held in the fingers in the usual manner so that it
gives the illusion of responding to my thoughts,
but is fitted with a rather delicate engine
and will write like a mad thing
provided I am willing to let it dictate pretty much
the subjects on which it writes.
or R. H. , *Computational Aspects of Certain
Combinatorial Problems* (1956)


# Chapter 5. Running METAFONT

It's high time now for you to stop reading and to start playing with the
computer, since METAFONT\ is an interactive system that is best learned by
trial and error. \ (In fact, one of the nicest things about computer graphics
is that errors are often more interesting and more fun than "successes.")

You probably will have to ask somebody how to deal with the idiosyncrasies
of your particular version of the system, even though METAFONT\ itself works in
essentially the same way on all machines; different computer terminals and
different hardcopy devices make it necessary to have somewhat different
interfaces. In this chapter we shall assume that you have a computer
terminal with a reasonably high-resolution graphics display; that you have
access to a (possibly low-resolution) output device; and that you can
rather easily get that device to work with newly created fonts.

OK, are you ready to run the program? First you need to log in, of course;
then start METAFONT\!, which is usually called for short. Once you've figured
out how to do it, you'll be welcomed by a message something like
$$\def\\{{\ }}
{{\indent
This\\is\\METAFONT,\\Version\\2.0\\(preloaded\\base=plain 89.11.8)}
{\indent **}}$$
The '' is METAFONT's way of asking you for an input file name.

Now type "''---that's , 'r', 'e', 'l', 'a', 'x'---and
hit ^*return* (or whatever stands for "end-of-line" on your keyboard).
METAFONT\ is all geared up for action, ready to make a big font; but you're
saying that it's all right to take things easy, since this is going to
be a real simple run. The backslash means that METAFONT\ should not read a file,
it should get instructions from the keyboard; the '' means
"do nothing."

The machine will respond by typing a single asterisk: ''. This means
it's ready to accept instructions (not the name of a file). Type the
following, just for fun:

"'

drawdot (35,70); showit;

"'

and *return*---don't forget to type the semicolons along with the other
stuff. A more-or-less circular dot should now appear on your screen! And
you should also be prompted with another asterisk.
Type

"'

drawdot (65,70); showit;

"'

and *return*, to get another dot. \ (Henceforth we won't keep mentioning
the necessity of *return*ing after each line of keyboard input.) \ Finally,
type

"'

draw (20,40)..(50,25)..(80,40); showit; shipit; end.

"'

This draws a curve through three given points, displays the result,

ships it to an output file, and stops. METAFONT\ should respond with "[0]'',
meaning that it has shipped out a character whose number is zero, in the
"font" just made; and it should also tell you that it has created
an output file called "mfput.2602gf''. \ (The name is used when
you haven't specified any better name in response to the at the
beginning. The suffix '2602' stands for " at
2602 pixels per inch." The data in 'mfput.2602gf' can be converted into
fonts suitable for a wide assortment of typographical output devices;
since it doesn't match the font file conventions of any name-brand
manufacturer, we call it generic.)

This particular file won't make a very interesting font,
because it contains only one character, and because it probably doesn't
have the correct resolution for your output device. However, it does
have the right resolution for hardcopy proofs of characters; your next
step should therefore be to convert the data of 'mfput.2602gf' into a
picture, suitable for framing. There should be a program called
on your computer. Apply it to 'mfput.2602gf', thereby
obtaining a file called 'mfput.dvi' that can be printed.
Your friendly local computer hackers will tell you how to run
'GFtoDVI' and how to print 'mfput.dvi'; then you'll have a marvelous
souvenir of your very first encounter with METAFONT\!. \looseness=-1

Once you have made a complete test run as just described, you will
know how to get through the whole cycle, so you'll be ready to tackle
a more complex project. Our next experiment will therefore be
to work from a file, instead of typing the input online.

Use your favorite text editor to create a file called 'io.mf' that
contains the following 23 lines of text (no more, no less):
$${ toindent{\sevenrm#\ \ }&#
1&'mode_setup;'{^^@mode\_setup@}
2&' em#:=10pt#; cap#:=7pt#;'
3&' thin#:=1/3pt#; thick#:=5/6pt#;'
4&' o#:=1/5pt#;'
5&'define_pixels(em,cap);'
6&'define_blacker_pixels(thin,thick);'
7&'define_corrected_pixels(o);'
8&' curve_sidebar=round 1/18em;'
9&'beginchar("O",0.8em#,cap#,0); "The letter O";'
10&' penpos1(thick,10); penpos2(.1[thin,thick],90-10);'
11&' penpos3(thick,180+10); penpos4(thin,270-10);'
12&' x1l=w-x3l=curve_sidebar; x2=x4=.5w;'
13&' y1=.49h; y2l=-o; y3=.51h; y4l=h+o;'
14&' penstroke z1edown..z2eright'
15&' ..z3eup..z4eleft..cycle;'
16&' penlabels(1,2,3,4); endchar;'
17&'def test_I(expr code,trial_stem,trial_width) ='
18&' stem#:=trial_stem*pt#; define_blacker_pixels(stem);'
19&' beginchar(code,trial_width*em#,cap#,0); "The letter I";'
20&' penpos1(stem,15); penpos2(.9stem,12); penpos3(stem,10);'
21&' x1=x2=x3=.5w; y1=h; y2=.55h; y3=0; x2l:=1/6[x2l,x2];'
22&' penstroke z1e..z2edown..z3e;'
23&' penlabels(1,2,3); endchar; enddef;'}$$
(But don't type the numbers at the left of these lines; they're
only for reference.)

This example file is dedicated to , the Greek goddess of input
and output. It's a trifle long, but you'll be able to get worthwhile
experience by typing it; so go ahead and type it now. For your own
good. And think about what you're typing, as you go; the example
introduces several important features of METAFONT\ that you can learn
as you're creating the file.

Here's a brief explanation of what you've just typed: Line 1 contains a
command that usually appears near the beginning of every METAFONT\ file;
it tells the computer to get ready to work in whatever "mode" is
currently desired. \ (A file like 'io.mf' can be used to generate
proofsheets as well as to make fonts for a variety of devices at a
variety of magnifications, and '@mode\_setup@' is what adapts METAFONT\
to the task at hand.) \ Lines 2--8 define parameters that will be used
to draw the letters in the font. Lines 9--16 give a complete program
for the letter 'O'; and lines 17--23 give a program that will draw
the letter 'I' in a number of related ways.

It all looks pretty frightening at first glance, but a closer look
shows that Io is not so mysterious once we penetrate her disguise.
Let's spend a few minutes studying the file in more detail.

Lines 2--4 define dimensions that are independent of the mode; the "#''
signs are meant to imply "sharp" or "true" ^units of
measure, which remain the same whether we are making a font at high or
low resolution. For example, one "pt#'' is a true printer's point, one
72.27th of an inch. This is quite different from the '^"pt"' we have
discussed in previous chapters, because '"pt"' is the number of pixels
that happen to correspond to a printer's point when the current resolution
is taken into account. The value of "pt#'' never changes, but
@mode\_setup@ establishes the appropriate value of '"pt"'.

The "em#:=10pt#'' and "cap#:=7pt#'' in line 2 mean that
the Io font has two parameters, called "em" and "cap", whose mode-independent
values are 10 and 7 points, respectively. The statement ^^@define\_pixels@
"define_pixels(em,cap)'' on line 5 converts these values into pixel
units. For example, if we are working at the comparatively low resolution
of 3 pixels per pt, the values of "em" and "cap" after the computer has
performed the instructions on line 5 will be $"em"=30$ and $"cap"=21$.
\ (We will see later that the widths of characters in this font are
expressed in terms of ems, and that "cap" is the height of the capital
letters. A change to line 2 will therefore affect the widths and/or heights
of all the letters.)

Similarly, the Io font has parameters called "thin" and "thick", defined
on line 3 and converted to pixel units in line 6. These are used to control
the breadth of a simulated pen when it draws the letter O. Experience has
shown that METAFONT\ produces better results on certain output devices if
pixel-oriented pens are made slightly broader than the true dimensions would
imply, because black pixels sometimes tend to "burn off" in the process
of printing. The command on line 6, "define_blacker_pixels'',
^^@define\_blacker\_pixels@ adds a correction based on the device for which
the font is being prepared. For example, if the resolution is 3 pixels
per point, the value of "thin" when converted from true units to pixels
by @define\_pixels@ would be 1, but @define\_blacker\_pixels@ might set
"thin" to a value closer to 2.

The "o'' parameter ^^"o" on line 4 represents the amount by which curves will
their boundaries. This is converted to pixels in yet another
way on line 7, so as to avoid yet another problem that arises in low-resolution
printing. The author apologizes for letting such real-world considerations
intrude into a textbook example; let's not get bogged down in fussy details
now, since these refinements will be explained in Chapter 11 after we have
mastered the basics.

For now, the important point is simply that a typeface
design usually involves parameters that represent physical lengths. The
true, "sharped" forms of these parameters need to be converted to
"unsharped" pixel-oriented quantities, and best results are obtained when
such conversions are done carefully. After METAFONT\ has obeyed line 7 of the
example, the pixel-oriented parameters "em", "cap", "thin", "thick",
and $o$ are ready to be used as we draw letters of the font.

Line 8 defines a quantity called "curve\_sidebar" that will
measure the distance of the left and right edges of the 'O' from the
bounding box. It is computed by ${1\over18}"em"$ to the nearest
integer number of pixels. For example, if $"em"=30$ then ${30\over18}=
{5\over3}$ yields the rounded value $"curve\_sidebar"=2$; there will be
two all-white columns of pixels at the left and right of the 'O',
when we work at this particular resolution.

Before we go any further, we ought to discuss the strange collection
of words and pseudo-words in the file 'io.mf'. Which of the terms
"mode_setup'', "em'', "curve_sidebar'', and so forth are part of
the METAFONT\ language, and which of them are made up specifically for
the Io example? Well, it turns out that almost *nothing* in this
example is written in the pure METAFONT\ language that the computer understands!
METAFONT\ is really a low-level language that has been designed to allow easy
adaptation to many different styles of programming, and 'io.mf'
illustrates just one of countless ways to use it. Most of the terms
in 'io.mf' are conventions of " METAFONT\!," which is a collection
of subroutines found in Appendix B. METAFONT's primitive capabilities are
not meant to be used directly, because that would force a particular style
on all users. A "base file" is generally loaded into the computer
at the beginning of a run, so that a standard set of conventions is
readily available. METAFONT's welcoming message, quoted at the
beginning of this chapter, says "preloaded' 'base=plain''; it
means that the primitive METAFONT\ language has been extended to include the
features of the plain base file. This book is not only about METAFONT; it also
explains how to use the conventions of METAFONT's plain base. Similarly, *The TeX book* describes a standard extension of TeX\ called "plain
TeX\ format"; the "plain" extensions of TeX\ and METAFONT\ are
completely analogous to each other.

The notions of @mode\_setup@, @define\_pixels@, @beginchar@, "penpos",
and many other things found in 'io.mf' are aspects
of plain METAFONT\ but they are not hardwired into METAFONT\ itself. Appendix B
defines all of these things, as well as the relations between "sharped"
and "unsharped" variables. Even the fact that $z_1$ stands for
$(x_1,y_1)$ is defined in Appendix B; METAFONT\ does not have this built in.
You are free to define even fancier bases as you gain more experience,
but the plain base is a suitable starting point for a novice.

**[Dangerous Bend]** If you have important applications that make use of a different
base file, it's possible to create a version of METAFONT\ that has any desired
base preloaded. Such a program is generally called by a special name,
since the nickname '' is reserved for the version that includes the
standard plain base assumed in this book. For example, the author has made
a special version called '' just for the typefaces
he has been developing, so that the Computer Modern base file does not
have to be loaded each time he makes a new experiment.

**[Dangerous Bend]** There's a simple way to change the base file from the one that has
been preloaded: If the first character you type in response to '' is
an ("&''), METAFONT\ will replace its memory
with a specified base file before proceeding. If, for example, there is a
base file called "cm.base'' but not a special program called "cmmf'',
you can substitute the Computer Modern base for the plain base in 'mf' by
typing "&cm'' at the very beginning of a run. If you are working with a
program that doesn't have the plain base preloaded, the first experiment
in this chapter won't work as described, but you can do it by starting
with "&plain '' instead of just "''. These conventions are
exactly the same as those of TeX.

Our Ionian example uses the following words that are not part of plain
METAFONT: "em", "cap", "thin", "thick", $o$, "curve\_sidebar", "test\_I", "code",
"trial\_stem", "trial\_width", and "stem". If you change these to some other
words or symbols---for example, if you replace "thin'' and "thick'' by
"t'' and "T'' respectively, in lines 3, 6, 10, and 11---the results will
be unchanged, unless your substitutions just happen to clash with something
that plain METAFONT\ has already pre\"empted. In general, the best policy is to
choose descriptive terms for the quantities in your programs, since they
are not likely to conflict with reserved pseudo-words like "penpos" and
@endchar@.

We have already noted that lines 9--16 of the file represent a program
for the letter 'O'. The main part of this program, in lines 10--15,
uses the ideas of Chapter 4, but we haven't seen the stuff in lines 9
and 16 before. Plain METAFONT\ makes it convenient to define letters by starting
each one with

>
$@beginchar@($*code*, *width*, *height*, *depth*);^^@beginchar@

here *code* is either a quoted single character like '"O"' or a number that
represents the character's position in the final font. The other three
quantities *width*, *height*, and *depth* say how big the
is, so that typesetting systems like TeX\ will be able to use the character.
These three dimensions must be given in device-independent units, i.e.,
in "" form.

### Exercise
What are the height and width of the bounding box described
in the @beginchar@ command on line 9 of 'io.mf', given the parameter
values defined on line 2? Give your answer in terms of printer's points.

#### Answer
The width is '0.8em#', and an 'em#' is 10 true points, so the
box will be exactly $8\pt$ wide in device-independent units. The
height will be $7\pt$. \ (And the depth below the baseline will be $0\pt$.)

Each @beginchar@ operation assigns values to special variables called
$w$, $h$, and $d$, ^^"w" ^^"h" ^^"d" which represent the respective
width, height, and depth of the current character's bounding box,
to the nearest integer number of pixels. Our example file
uses $w$ and $h$ to help establish the locations of several pen positions
(see lines 12, 13, and 21 of 'io.mf').

### Exercise
Continuing the previous exercise, what will be the values of
$w$ and $h$ if there are exactly 3.6 pixels per point?

#### Answer
$8\times3.6=28.8$ rounds to the value $w=29$; similarly, $h=25$.
\ (And $d=0$.)

There's a quoted phrase '"The' 'letter' 'O"' at the end of line 9; this is
simply a title that will be used in printouts.

The "endchar'' ^^@endchar@ on line 16 finishes the character that was
begun on line 9, by writing it to an output file and possibly displaying
it on your screen. We will want
to see the positions of the control points $z_1$, $z_2$,
$z_3$, and $z_4$ that are used in its design, together with the auxiliary
points $(z_1l,z_2l,z_3l,z_4l)$ and $(z_1r,z_2r,z_3r,z_4r)$
that come with the "penpos" conventions; the statement "penlabels(1,2,3,4)''
^^"penlabels" takes care of labeling these points on the proofsheets.

So much for the letter O. Lines 17--23 are analogous to what we've seen
before, except that there's a new wrinkle: They contain a little program
^^@def@ enclosed by "def...enddef'', which means that a
is being defined. In other words, those lines set up
a whole bunch of METAFONT\ commands that we will want to execute several times
with minor variations. The subroutine is called "test\_I" and it has three
parameters called "code", "trial\_stem", and "trial\_width" (see line 17).
The idea is that we'll want to draw several different versions of an 'I',
having different stem widths and character widths; but we want to type the
program only once. Line 18 defines "stem"\0 and "stem", given a value of
"trial\_stem"; and lines 19--23 complete the program for the letter I
(copying it from Chapter 4).

Oops---we've been talking much too long about 'io.mf'. It's time to stop
rambling and to begin Experiment 2 in earnest, because it will be much
more fun to see what the computer actually does with that file.

Are you brave enough to try Experiment 2? Sure.
Get METAFONT\ going again, but this time when the machine says '' you should
say "io'', since that's the name of the file you have prepared so
laboriously. \ (The file could also be specified by giving its full name
"io.mf'', but METAFONT\ automatically adds ".mf'' when
no suffix has been given explicitly.)

If all goes well, the computer should now flash its lights a bit
and---presto---a big '{\manual\IOO}' should be drawn on your screen.
But if your luck is as good as the author's, something will probably go wrong
the first time, most likely because of a typographic error in the file.
A METAFONT\ program contains lots of data with comparatively little redundancy,
so a single error can make a drastic change in the meaning. Check that
you've typed everything perfectly: Be sure to notice the difference between
the letter "l'' and the numeral "1'' (especially in line 12, where it
says "x1l'', not "x11'' or "xll''); be sure to distinguish between
the letter "O'' and the numeral "0'' (especially in line 9); be sure to
type the "underline" characters in words like "mode_setup''. We'll see
later that METAFONT\ can recover gracefully from most errors, but your job for
now is to make sure that you've got 'io.mf' correct.

Once you have a working file, the computer will draw you an '{\manual\IOO}'
and it will also say something like this:

"'

(io.mf
The letter O [79])
*

"'

What does this mean? Well, "(io.mf'' means that it has started to read your
file, and "The' 'letter' 'O'' was printed when the title was found in
line 9. Then when METAFONT\ got to the 'endchar' on line 16, it said
"[79]'' to tell you that it had just output character number 79.
\ (This is the code for the letter 'O'; Appendix C lists all
of these codes, if you need to know them.) The ")'' after "[79]''
means that METAFONT\ subsequently finished reading the file, and the ''
means that it wants another instruction.

Hmmm. The file contains programs for both I and O; why did we get only
an O? Answer: Because lines 17--23 simply define the subroutine "test\_I";
they don't actually *do* anything with that subroutine. We need to
activate "test\_I" if we're going to see what it does. So let's type

"'

test_I("I",5/6,1/3);

"'

this invokes the subroutine, with $"code"=$'"I"',
$"trial\_stem"={5\over6}$, and $"trial\_width"={1\over3}$. The computer will
now draw an I corresponding to these values,\footnote*{Unless, of course,
there was a typing error in lines 17--23, where "test\_I" is defined.} and
it will prompt us for another command.

It's time to type '' now, after which METAFONT\ should tell us that it has
completed this run and made an output file called "io.2602gf''. Running this
file through as in Experiment 1 will produce two proofsheets,
showing the '{\manual\IOO}' and the '{\manual\IOI}' we have created.
The output won't be shown here, but you can see the results by doing
the experiment personally.

Look at those proofsheets now, because they provide instructive examples
of the simulated broad-edge pen constructions introduced in Chapter 4.
Compare the '{\manual\IOO}' with the program that drew it: Notice that
the $\penpos2$ in line 10 makes the curve slightly thicker at the ^^"penpos"
bottom than at the top; that the equation '$x_1l=w-x_3l="curve\_sidebar"$'
in line 12 makes the right edge of the curve as far from the right of the
bounding box as the left edge is from the left; that line 13 places point 1
slightly lower than point 3. The proofsheet for '{\manual\IOI}' should look
very much like the corresponding illustration near the end of Chapter 4,
but it will be somewhat larger.

**[Dangerous Bend]** Your proof copy of the '{\manual\IOO}' should show twelve dots
for key points; but only ten of them will be labeled, because there isn't
room enough to put labels on points 2 and 4. The missing usually
appear in the upper right corner, where it might say, e.g.,
"4' '=' '4l' '+' '(-1,-5.9)''; this
means that point $z_4$ is one pixel to the left and 5.9 pixels down
from point $z_4l$, which is labeled. \ (Some implementations omit this
information, because there isn't always room for it.)

The proofsheets obtained in Experiment 2 show the key points and the
bounding boxes, but this extra information can interfere with our
perception of the character shape itself. There's a simple way to
get proofs that allow a viewer to criticize the results from an aesthetic
rather than a logical standpoint; the creation of such proofs will be the
goal of our next experiment.

Here's how to do Experiment 3: Start METAFONT\ as usual, then type

"'

\mode=smoke; input io

"'

in response to the ''. This will input file 'io.mf' again,
after establishing "smoke" mode. \ (As in Experiment 1, the command line
begins with "\'' so that the computer knows you aren't starting with
the name of a file.) \ Then complete the run exactly
as in Experiment 2, by typing "test_I("I",5/6,1/3);' 'end'';
and apply 'GFtoDVI' to the resulting file 'io.2602gf'.

This time the proofsheets will contain the same characters as before, but
they will be darker and without labeled points. The bounding boxes will
be indicated only by small markings at the corners; you can put these
boxes next to each other and tack the results up on the wall, then stand
back to see how the characters will look when set by a high-resolution
typesetter. \ (This way of working is called ^"smoke" mode because it's
analogous to the "smoke proofs" that punch-cutters traditionally used to
test their handiwork. They held the newly cut type over a candle flame so
that it would be covered with carbon; then they pressed it on paper to
make a clean impression of the character, in order to see whether changes
were needed.)

**[Dangerous Bend]** Incidentally, many systems allow you to invoke METAFONT\ by typing
a one-line command like "mf' 'io'' in the case of Experiment 2; you
don't have to wait for the "**'' before giving a file name. Similarly,
the one-liners "mf' "' and "mf' '\mode=smoke;' 'input' 'io'' can be
used on many systems at the beginning of Experiments 1 and 3. You might want
to try this, to see if it works on your computer; or you might ask
somebody if there's a similar shortcut.

Experiments 1, 2, and 3 have demonstrated how to make proof drawings of
test characters, but they don't actually produce new fonts that can be
used in typesetting. For this, we move onward to Experiment 4, in which
we put ourselves in the position of a person who is just starting to
design a new typeface. Let's imagine that we're happy with the O of
'io.mf', and that we want a "sans serif" I in the general style produced
by "test\_I", but we aren't sure about how thick the stem of the I
should be in order to make it blend properly with the O. Moreover, we aren't
sure how much white space to leave at the sides of the I. So we want to do
some typesetting experiments, using a sequence of different I's.

The ideal way to do this would be to produce a high-resolution test font and to
view the output at its true size. But this may be too expensive, because fine
printing equipment is usually available only for large production runs.
The next-best alternative is to use a low-resolution printer but to magnify
the output, so that the resolution is effectively increased. We shall adopt
the latter strategy, because it gives us a chance to learn about
as well as fontmaking.

After starting METAFONT\ again, you can begin Experiment 4 by typing

"'

\mode=localfont; mag=4; input io

"'

in response to the "**''. The at your installation is supposed
to recognize as the name of the mode that makes fonts for your
"standard" output device. The equation "mag=4'' means that this run will
produce a font that is magnified fourfold; i.e., the results will be
4 times bigger than usual.

The computer will read 'io.mf' as before, but this time it won't display an 'O';
characters are normally not displayed in fontmaking modes, because we usually
want the computer to run as fast as possible when it's generating a font
that has already been designed. All you'll see is
"(io.mf' 'The' 'letter' 'O' '[79])'' or possibly only "(io.mf' '[79])'',
followed by ''. Now the fun starts: You should type

"'

code=100;
for s=7 upto 10:
for w=5 upto 8:
test_I(incr code,s/10,w/20);
endfor endfor end.

"'

(Here '' must be typed as a single word.) \ We'll learn about
repeating things with "...'' in Chapter 19. This little
program produces 16 versions of the letter I, with stem widths of
$7\over10$, $8\over10$, $9\over10$, and ${10\over10}\pt$, and with
character widths of $5\over20$, $6\over20$, $7\over20$, and ${8\over20}\,
em$. The sixteen trial characters will appear in positions 101 through 116
of the font; it turns out that these are the codes for lowercase
letters 'e' through 't' inclusive. \ (Other codes would have been used if
"code'' had been started at a value different from 100. The construction
"incr' 'code'' increases the value of 'code' by 1 and produces the new value;
thus, each use of 'test_I' has a different code number.) ^^"incr"

This run of METAFONT\ will not only produce a generic font 'io.nnngf', it will also
create a file called 'io.tfm', the "" that tells

typesetting systems like TeX\ how to make use of the new font. The remaining
part of Experiment 4 will be to put TeX\ to work: We shall make some test
patterns from the new font, in order to determine which 'I' is best.

You may need to ask a local system wizard for help at this point, because
it may be necessary to move the file 'io.tfm' to some special place where
TeX\ and the other typesetting software can find it. Furthermore, you'll
need to run a program that converts 'io.nnngf' to the font format used by your
local output device. But with luck, these will both be fairly simple
operations, and a new font called "io'' will effectively be installed
on your system. This font will contain seventeen letters, namely an 'O' and
sixteen 'I''s, where the 'I''s happen to be in the positions normally occupied
by 'e', 'f', \dots, 't'. Furthermore, the font will be magnified fourfold.

**[Dangerous Bend]** The magnification of the font will be reflected in its file name.
For example, if "localfont" mode is for a device with 200 pixels per inch,
the 'io' font at 4$\times$ magnification will be called "io.800gf''.

You can use TeX\ to typeset from this font like any other, but for the
purposes of Experiment 4 it's best to use a special TeX\ package that has
been specifically designed for font testing. All you need to do is to
run TeX---which is just like running METAFONT\!, except that you call it "tex''
instead of "mf''; and you simply type '' in reply to TeX's
"**''. \ (The 'testfont' routine should be available on your system; if
not, you or somebody else can type it in, by copying the relevant material
from Appendix H.) \ You will then be asked for the name of the font
you wish to test. Type

"'

io scaled 4000

"'

(which means the 'io' font magnified by 4, in TeX's jargon),
since this is what METAFONT\ just created. The machine will now ask you for
a test command, and you should reply

"'

\mixture

"'

to get the "" test. \ (Don't forget the .) \
You'll be asked for a , a starting letter, and an
ending letter; type "O'', "e'', and "t'', respectively. This will
produce sixteen lines of typeset output, in which the first line contains
a mixture of 'O' with 'e', the second contains a mixture of 'O' with 'f',
and so on. To complete Experiment 4, type "\end'' to TeX, and print the
file 'testfont.dvi' that TeX\ gives you.

= I \def\\{\copy0}
If all goes well, you'll have sixteen lines that say 'O\\OO\\\\OOO\\\\\\O\\',
but with a different I on each line. In order to choose the line that looks
best, without being influenced by neighboring lines, it's convenient to take
two sheets of blank paper and use them to mask out all of the lines
except the one you're studying. Caution: These letters are four times
larger than the size at which the final font is meant to be viewed,
so you should look at the samples from afar. Xerographic reductions may
introduce distortions that will give misleading results. Sometimes when
you stare at things like this too closely, they all look wrong, or
they all look right; first impressions are usually more significant
than the results of logical reflection. At any rate, you should be able
to come up with an informed judgment about what values to use for the
stem width and the character width of a decent 'I'; these can then be
incorporated into the program, the "def'' and "enddef'' parts of
'io.mf' can be removed, and you can go on to design other characters
that go with your I and O. Furthermore you can always go back and make
editorial changes after you see your letters in more contexts.

**[Double Dangerous Bend]** exercise The goddess Io was known in Egypt as .
Design an '{\manual\IOS}' for her.

#### Answer
Here's one way, using a variable "slab" to control the
\rightfig A5a ({200\apspix} x 252\apspix) ^-71pt
pen breadth at the ends of the stroke:

"'

slab#:=.8pt#; define_blacker_pixels(slab);
beginchar("S",5/9em#,cap#,0); "The letter S";
penpos1(slab,70); penpos2(.5slab,80);
penpos3(.5[slab,thick],200); penpos5(.5[slab,thick],210);
penpos6(.7slab,80);
penpos7(.25[slab,thick],72);
x1=x5; y1r=.94h+o;
x2=x4=x6=.5w; y2r=h+o; y4=.54h; y6l=-o;
x3r=.04em; y3=.5[y4,y2];
x5l=w-.03em; y5=.5[y4,y6];
.5[x7l,x7]=.04em; y7l=.12h-o;
path trial; trial=z3down..z4..downz5;
pair dz; dz=direction 1 of trial;
penpos4(thick,angle dz-90);
penstroke z1e..z2eleft..z3edown
..z4edz..z5edown..z6eleft..z7e;
penlabels(1,2,3,4,5,6,7); endchar;

"'

Notice that the pen angle at point 4 has been found by letting METAFONT\
construct a through the center points,
then using the direction. The letters work reasonably
well at their true size: '{\manual\IOS\IOO} {\manual\IOI\IOO}
{\manual\IOI\IOS} {\manual\IOI\IOS\IOI\IOS}.'

Well, this isn't a book about type design; the example of 'io.mf' is
simply intended to illustrate how a type designer might want to operate,
and to provide a run-through of the complete process from design of
type to its use in a document. We must go back now to the world of
computerese, and study a few more practical details about the use of METAFONT\!.

This has been a long chapter, but take heart: There's only one more
experiment to do, and then you will know enough about METAFONT\ to run it
fearlessly by yourself forever after. The only thing you are still missing
is some information about how to cope with error messages. Sometimes
METAFONT\ stops and asks you what to do next. Indeed, this may have already
happened, and you may have panicked.

Error messages can be terrifying when you aren't prepared for them;
but they can be fun when you have the right attitude. Just remember that
you really haven't hurt the computer's feelings, and that nobody will
hold the errors against you. Then you'll find that running METAFONT\ might
actually be a creative experience instead of something to dread.

The first step in Experiment 5 is to plant some intentional mistakes
in the input file. Make a copy of 'io.mf' and call it 'badio.mf'; then
change line 1 of 'badio.mf' to

"'

mode setup;

"'

(thereby omitting the underline character in 'mode_setup').
Also change the first semicolon (";'') on line 2
to a colon (":'');
change "thick,10'' to "thick,l0'' on line 10 (i.e., replace the numeral "1''
by the letter "l''); and change "thin'' to "thinn'' on line 11.
These four changes introduce typical typographic errors, and it will be
instructive to see if they lead to any disastrous consequences.

Now start METAFONT\ up again; but instead of cooperating with the computer, type
"mumble'' in reply to the "**''. \ (As long as you're going to make
intentional mistakes, you might as well make some dillies.) \
METAFONT\ will say that it can't find any file called 'mumble.mf',
and it will ask you for another name. Just hit *return* this time;
you'll see that you had better give the name of a real file.
So type "badio'' and wait for METAFONT\ to find one of the *faux pas*
in that messed-up travesty.

Ah yes, the machine will soon stop, after typing something like this:

"'

>> mode.setup
! Isolated expression.
<to be read again>
;
l.1 mode setup;

?

"'

METAFONT\ begins its error messages with "!'', and it sometimes precedes them
with one or two related mathematical expressions that are displayed on
lines starting with ''. Each error message is also followed by lines
of context that show what the computer was reading at the time of the
error. Such context lines occur in pairs; the top line of the pair (e.g.,
"mode' 'setup;'') shows what METAFONT\ has looked at so far, and
where it came from ("l.1'', i.e., line number 1); the bottom line (here
'|
read. In this case there are two pairs of context lines; the top pair
refers to a semicolon that METAFONT\ has read once but will be reading again,
because it didn't belong with the preceding material.

You don't have to take out pencil and paper in order to write down the
error messages that you get before they disappear from view, since METAFONT\
always writes a "" or "" that records what
happened during each session. For example, you should now have a file
called 'io.log' containing the transcript of Experiment 4, as well as a file
'mfput.log' that contains the transcript of Experiment 1. \ (The old
transcript of Experiment 2 was probably overwritten when you did
Experiment 3, and again when you did Experiment 4, because all three
transcripts were called 'io.log'.) \ At the end of Experiment 5 you'll
have a file 'badio.log' that will serve as a helpful reminder of
what errors need to be fixed up.

The ''\ that appears after the context display means that METAFONT\ wants
advice about what to do next. If you've never seen an error message before,
or if you've forgotten what sort of response is expected, you can type
"?'' now (go ahead and try it!); METAFONT\ will respond as follows:

"'

Type <return> to proceed, S to scroll future error messages,
R to run without stopping, Q to run quietly,
I to insert something, E to edit your file,
1 or ... or 9 to ignore the next 1 to 9 tokens of input,
H for help, X to quit.

"'

This is your menu of options. You may choose to continue in various ways:

- 1.
Simply type *return*. METAFONT\ will resume its processing, after
attempting to recover from the error as best it can.

break- 2. Type "S''. METAFONT\ will proceed without
pausing for instructions if further errors arise. Subsequent error messages
will flash by on your terminal, possibly faster than you can read them, and
they will appear in your log file where you can scrutinize them at your
leisure. Thus, "S'' is sort of like typing *return* to every message.

break- 3. Type "R''. This is like "S'' but even stronger,
since it tells METAFONT\ not to stop for any reason, not even if a file name
can't be found.

break- 4. Type "Q''. This is like "R'' but even more so,
since it tells METAFONT\ not only to proceed without stopping but also to
suppress all further output to your terminal. It is a fast, but somewhat
reckless, way to proceed (intended for running METAFONT\ with no operator in
attendance).

break- 5. Type "I'', followed by some text that you want to
insert. METAFONT\ will read this text before encountering what it
would ordinarily see

next.

break- 6. Type a small number (less than 100). METAFONT\ will
delete this many from whatever it is
about to read next, and it will pause again to give you another chance to
look things over.
\ (A "token" is a name, number, or symbol that METAFONT\ reads as a unit;
e.g., "mode'' and "setup'' and ";'' are the first three tokens
of 'badio.mf', but "mode_setup'' is the first token of 'io.mf'.
Chapter 6 explains this concept precisely.)

break- 7. Type "H''. This is what you should do now and whenever
you are faced with an error message that you haven't seen for a while. METAFONT\
has two messages built in for each perceived error: a formal one and an
informal one. The formal message is printed first (e.g., "!' 'Isolated'
'expression.''); the informal one is printed if you request
more help by typing "H'', and it also appears in your log file if you
are scrolling error messages. The informal message tries to complement the
formal one by explaining what METAFONT\ thinks the trouble is, and often
by suggesting a strategy for recouping your losses.

break- 8. Type "X''. This stands for "exit." It causes METAFONT\
to stop working on your job, after putting the finishing touches on your
'log' file and on any characters that have already been output to your 'gf'
and/or 'tfm' files. The current (incomplete) character will not be output.

break- 9. Type "E''. This is like "X'', but it also prepares
the computer to edit the file that METAFONT\ is currently reading, at the
current position, so that you can conveniently make a change before
trying again.

break
After you type "H'' (or "h'', which also works), you'll get a message
that tries to explain the current problem: The mathematical quantity just
read by METAFONT\ (i.e., 'mode.setup') was not followed by "='' or ":='', so
there was nothing for the computer to do with it. Chapter 6 explains that
a between tokens (e.g., "mode' 'setup'') is equivalent to
a between tokens (e.g., "mode.setup''). The correct
spelling "mode_setup'' would be recognized as a preloaded subroutine of
plain METAFONT\!, but plain METAFONT\ doesn't have any built-in meaning for
'mode.setup'. Hence 'mode.setup' appears as a sort of orphan, and METAFONT\
realizes that something is amiss.

In this case, it's OK to go ahead and type *return*, because we really
don't need to do the operations of @mode\_setup@ when no special mode
has been selected. METAFONT\ will continue by forgetting the isolated expression,
and it will ignore the rest of line 1 because everything after a
'|
will be explained in Chapter 6; it's a handy way to put
into your METAFONT\ programs.) \ The changes that were made to line 1 of 'badio.mf'
therefore have turned out to be relatively harmless. But METAFONT\ will
almost immediately encounter the mutilated semicolon in line 2:

"'

! Extra tokens will be flushed.
<to be read again>
:
l.2 em#:=10pt#:
cap#:=7pt#;
?

"'

What does this mean? Type "H'' to find out. METAFONT\ has no idea what to
do with a ":'' at this place in the file, so it plans to recover by
"" or getting rid of everything it sees, until coming to a
semicolon. It would be a bad idea to type *return* now, since you'd lose
the important assignment "cap#:=7pt#'', and that would lead to worse errors.

You might type "X'' or "E'' at this point, to exit from METAFONT\ and to fix
the errors in lines 1 and 2 before trying again. But it's usually best
to keep going, trying to detect and correct as many mistakes as possible
in each run, since that increases your productivity while
decreasing your computer bills. An experienced METAFONT\ user will quit
after an error only if the error is unfixable, or if there's almost no
chance that additional errors are present.

The solution in this case is to proceed in two steps: First type "1'',
which tells METAFONT\ to delete the next token (the unwanted ":''); then type
"I;'', which inserts a semicolon. This semicolon protects the rest of line 2
from being flushed away,
so all will go well until METAFONT\ reaches another garbled line.

The next error message is more elaborate, because it is detected while
METAFONT\ is trying to carry out a "penpos" command; "penpos" is not a
primitive operation (it is defined in plain METAFONT), hence a lot more
context is given:

"'

>> l0
! Improper transformation argument.
<to be read again>
;
penpos->...(EXPR3),0)rotated(EXPR4);
x(SUFFIX2)=0.5(x(SUFF...
l.10 penpos1(thick,l0)
; penpos2(.1[thin,thick],90-10);
?

"'

At first, such error messages will appear to be complete nonsense to you,
because much of what you see is low-level METAFONT\ code that you never wrote. But
you can overcome this hangup by getting a feeling for the way METAFONT\ operates.

The bottom line shows how much progress METAFONT\ has made so far in the 'badio'
file: It has read "penpos1(thick,l0)'' but not yet the semicolon, on line 10.
The "penpos" routine expands into a long list of tokens; indeed, this list
is so long that it can't all be shown on two lines, and the appearances of
'' indicate that the definition of "penpos" has been truncated here.
Parameter values are often inserted into the expansion of a high-level
routine; in this case, for example, "(EXPR3)'' and "(EXPR4)'' correspond
to the respective parameters "thick'' and "l0'', and "(SUFFIX2)''
corresponds to "1''.
METAFONT\ detected an error just after encountering the phrase "rotated(EXPR4)'';
the value of '(EXPR4)' was an undefined quantity (namely "l0'',
which METAFONT\ treats as the subscripted variable '$l_0$'), and
is permitted only when a known numeric value has been supplied.
Rotations are particular instances of what METAFONT\ calls ;
hence METAFONT\ describes this particular error by saying that an "improper
transformation argument" was present.

When you get a multiline error message like this, the best clues about the
source of the trouble are usually on the bottom line (since that is what
you typed) and on the top line (since that is what triggered the error
message). Somewhere in there you can usually spot the problem.

If you type "H'' now, you'll find that
METAFONT\ has simply decided to continue without doing the requested rotation.
Thus, if you respond by typing *return*, METAFONT\ will go on as if the program
had said "penpos1(thick,0)''. Comparatively little harm has been done;
but there's actually a way to fix the error perfectly before proceeding:
Insert the correct rotation by typing

"'

I rotated 10

"'

and METAFONT\ will rotate by 10 degrees as if "l0'' had been "10''.

What happens next in Experiment 5? METAFONT\ will hiccup on the remaining
bug that we planted in the file. This time, however, the typo will
not be discovered until much later, because there's nothing wrong
with line 11 as it stands. \ (The variable 'thinn' is not defined,
but undefined quantities are no problem unless you're doing something
complicated like rotation. Indeed, METAFONT\ programs typically
consist of equations in which there are lots of unknowns;
variables get more and more defined as time goes on. Hence spelling
errors cannot possibly be detected until the last minute.) \
Finally comes the moment of truth, when 'badio' tries to draw a
path through an unknown point; and you will get an error message
that's even scarier than the previous one:

"'

>> 0.08682thinn+144
! Undefined x coordinate has been replaced by 0.
<to be read again>
{
<for(l)> ...FFIX0)up..z4(SUFFIX0)
left..cycle; ENDFOR
penstroke->...ath_.e:=(TEXT0);endfor
.if.cycle.path_.l:cyc...
<to be read again>
;
l.15 ... ..z3eup..z4eleft..cycle;
|quad
?

"'

Wow; what's this? The expansion of @penstroke@ involves a "@for@ loop,"
and the error was detected in the midst of it. The
expression "0.08682thinn+144'' just above the error message implies that
the culprit in this case was a misspelled "thin''. If that hadn't been
enough information, you could have gleaned another clue from the fact that
"z4(SUFFIX0)'' has just been read; '(SUFFIX0)' is the current loop value
and "<for(l)>'' indicates that the value in question is "l'', hence
$z_4l$ is under suspicion. \ (Sure enough, the undefined $x$ coordinate
that provoked this error can be shown to be $x_4l=0.08682"thinn"+144$.)

In any event the mistake on line 11 has propagated too far to be fixable,
so you're justified in typing "X'' or "E'' at this point. But type "S''
instead, just for fun: This tells METAFONT\ to plunge ahead, correcting all
remaining errors as best it can. \ (There will be a few more problems,
since several variables still depend on "thinn''.) \ METAFONT\ will draw a
very strange letter O before it gets to the end of the file. Then you
should type "end'' to terminate the run.

If you try to edit 'badio.mf' again, you'll notice that line 2 still
contains a colon instead of a semicolon. The fact that you
told METAFONT\ to delete the colon and to insert additional material doesn't
mean that your file has changed in any way. However, the transcript file
'badio.log' has a record of all the errors, so it's a handy reference when
you want to correct mistakes. \ (Why not look at
'badio.log' now, and 'io.log' too, in order to get familiar with log files?)

**[Dangerous Bend]** exercise Suppose you were doing Experiment 3 with 'badio' instead
of 'io', so you began by saying "\mode=smoke;' 'input' 'badio''. Then you
would want to recover from the error on line 1 by inserting a correct
@mode\_setup@ command, instead of by simply *return*ing, because
@mode\_setup@ is what really establishes "smoke" mode. Unfortunately if you
try typing "I' 'mode_setup'' in response to the "isolated expression"
error, it doesn't work. What should you type instead?

#### Answer
After an "isolated expression," METAFONT\ thinks it is at the end of
a statement or command, so it expects to see a semicolon next. You should
type, e.g., "I;' 'mode_setup'' to keep METAFONT\ happy.

By doing the five experiments in this chapter you have learned at first hand
(1) how to produce proofsheets of various kinds, including "smoke proofs";
(2) how to make a new font and test it; (3) how to keep calm when METAFONT\
issues stern warnings. Congratulations! You're on the threshold of being able to
do lots more. As you read the following chapters, the best strategy
will be for you to continue making trial runs, using experiments
of your own design.

### Exercise
However, this has been an extremely long chapter,
so you should go outside now and get some *real* exercise.

#### Answer
Yes.

\endchapter

Let us learn how Io's frenzy came---
She telling her disasters manifold.
or \AE SCHYLUS,
*Prometheus Bound* (c.470 B.C.)

To the student who wishes to use graphical methods as a tool,
it can not be emphasized too strongly that practice in the use of that tool
is as essential as a knowledge of how to use it.
The oft-repeated pedagogical phrase, "we learn by doing," is applicable here.

> --- THEODORE , *Graphical Mathematics* (1927)


# Chapter 6. How METAFONT Reads What You Type

So far in this book we've seen lots of things that METAFONT\ can do, but we haven't
discussed what METAFONT\ can't do. We have looked at many examples of commands that
METAFONT\ can understand, but we haven't dwelt on the fact that the computer will
find many phrases unintelligible. It's time now to adopt a more systematic
approach and to study the exact rules of METAFONT's language. Then we'll know what
makes sense to the machine, and we'll also know how to avoid ungrammatical
utterances.

A METAFONT\ program consists of one or more lines of text, where each line is made
up of letters, numbers, punctuation marks, and other symbols that appear on
a standard computer keyboard. A total of 95 different characters can be
employed, namely a blank space plus the 94 visible symbols of standard .
\ (Appendix C describes the American Standard Code for Information
Interchange, popularly known as "ASCII," under which code numbers 33
through 126 have been assigned to 94 specific symbols. This particular
coding scheme is not important to a METAFONT\ programmer; the only relevant thing
is that 94 different nonblank symbols can be used.)

METAFONT\ converts each line of text into a series of **, and a
programmer should understand exactly how this conversion takes place.
Tokens are the individual lexical units that govern the computer's
activities. They are the basic building blocks from which meaningful
sequences of instructions can be constructed. We discussed tokens briefly
at the end of the previous chapter; now we shall consider them in detail.
Line 9 of the file 'io.mf' in that chapter is a typical example of what
the machine might encounter:

"'

beginchar("O",0.8em#,cap#,0); "The letter O";

"'

When METAFONT\ reads these ASCII characters it finds sixteen tokens:

> \chardef\"='\" \openup 2pt
okbegincharok(ok{\"O\"}
ok,ok0.8okemok{\#}ok,
okcapok{\#}ok,ok0
ok)ok;ok{\"The letter O\"}ok;

Two of these, '"O"' and '"The' 'letter' 'O"', are called
because they represent strings of characters. Two of them, "0.8'' and "0'',
are called because they represent numbers. The
other twelve---"beginchar'', "('', etc.---are called {^symbolic
tokens}; such tokens can change their meaning while a METAFONT\ program runs,
but string tokens and numeric tokens always have a predetermined significance.
Notice that clusters of letters like "beginchar'' are treated as a unit;
the same holds with respect to letters mixed with characters,
as in "mode_setup''. Indeed,
the rules we are about to study will explain that clusters of other
characters like "0.8'' and ":='' are also considered to be
indecomposable tokens. METAFONT\ has a definite way of deciding where one
token stops and another one begins.

It's often convenient to discuss by formulating them in
a special notation that was introduced about 1960 by John and
Peter . Parts of speech are represented by named quantities in
, and are used to express the ways
in which those quantities can be built up from simpler units. For example,
here are three syntax rules that completely describe the possible forms of
numeric tokens:

\beginsyntax
<decimal digit>\is\\0\alt\\1\alt\\2\alt\\3\alt\\4\alt\\5\alt\\6
\alt\\7\alt\\8\alt\\9
<digit string>\is<decimal digit>\alt<digit string><decimal digit>
<numeric token>\is<digit string>\alt[.]<digit string>
\alt<digit string>\\.<digit string>
\endsyntax
The first rule says that a *decimal digit* is either "0'' or "1'' or
$\cdots$ or "9''; thus it must be one of the ten numerals. The next
rule says that a *digit string* is either a *decimal digit* or a
*digit string* followed by a *decimal digit*; thus it must be a sequence
of one or more digits. Finally, a *numeric token* has one of three forms,
exemplified respectively by "15'', ".05'', and "3.14159''.

Syntax rules explain only the surface structure of a language, not the
underlying meanings of things. For example, the rules above tell us that
"15'' is a *numeric token*, but they don't imply that "15'' has
any connection with the number fifteen. Therefore syntax rules are
generally accompanied by rules of , which ascribe
meanings to the strings of symbols that meet the conditions of the syntax.
In the case of numeric tokens, the principles of ordinary decimal notation
define the semantics, except that METAFONT\ deals only with numbers in a
limited range: A numeric token must be less than 4096, and its value is
always rounded to the nearest multiple of $1\over65536$. Thus, for example,
".1'' does not mean $1\over10$, it means $6554\over65536$ (which is
slightly greater than $1\over10$). It turns out that the tokens
".099999'' and "0.10001'' both have exactly the same meaning as

".1'', because all three tokens represent the value $6554\over65536$.

**[Dangerous Bend]** exercise Are the following pairs of numeric tokens equivalent
to each other, when they appear in METAFONT\ programs?
\ (a) '0' and '0.00001'; \ (b) '0.00001' and '0.00002';
\ (c) '0.00002' and '0.00003'; \ (d) '04095.999999' and '10000'.

#### Answer
(a) No, the second token represents $1\over65536$. \ (A token has
the same meaning as "0'' if and only if its decimal value
is strictly less than $2=.00000\,76293\,94531\,25$.) \ (b) Yes; both
tokens represent $1\over65536$, because 1 is the nearest integer to both
$.00001\times65536=.65536$ and $0.00002\times65536=1.31072$. \ (c) No,
'0.00003' represents $2\over65536$. \ (d) Yes, they both mean "^enormous
number that needs to be reduced"; METAFONT\ complains in both
cases and substitutes the largest legal numeric token. \ (Rounding
4095.999999 to the nearest multiple of $1\over65536$ yields 4096,
which is too big.)

METAFONT\ converts each line of text into a sequence of tokens by repeating
the following rules until no more characters remain on the line:

\hang- 1)If the next character is a , or if it's a
(".'')\ that isn't followed by a
decimal digit or a period, ignore it and move on.

\hang- 2)If the next character is a
('|
that remains on the current line. \ (Percent signs therefore allow you to
write that are unseen by METAFONT\!.)

\hang- 3)If the next character is a or a period
that's followed by a decimal digit, the next token is a numeric token,
consisting of the longest sequence of contiguous characters starting at
the current place that satisfies the syntax for *numeric token* above.

\hang- 4)If the next character is a (
""''), the next token is a string token, consisting of all
characters from the current place to the next double-quote, inclusive.
\ (There must be at least one more double-quote remaining on the line,
otherwise METAFONT\ will complain about an ".") \ A string
token represents the sequence of characters between the double-quotes.

\hang- 5)If the next character is a (
"('' or ")''), a comma (",''), or a
semicolon (";''), the next token is a symbolic token
consisting of that single character.

\hang- 6)Otherwise the next token is a symbolic token consisting
of the next character together with all immediately following characters
that appear in the same row of the following
table:

> \displayindent=0pt
'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'\hidewidth
'<=>:'\|
"''
'+-'
'/*\'
'!?'
'#&@$'
'^ '
'['
']'
''
'.'&(see rules 1, 3, 6)
', ; ( )'&(see rule 5; these characters are "loners")
'"'&(see rule 4 for details about string tokens)
'0123456789'&(see rule 3 for details about numeric tokens)
|

The best way to learn the six rules about tokens is to work the following
exercise, after which you'll be able to read any input file just as the
computer does.

### Exercise
What tokens does METAFONT\ find in the (ridiculous) line

>
|xx3.1.6..[[a+-bc_d.e] ]"a

#### Answer
\cstokxx, \cstok3.1 (a numeric token), \cstok.6 (another
numeric token), \cstok.., \cstok[[, \cstoka, \cstok+-,
\cstok{bc\char'\_d}, \cstoke, \cstok], \cstok], {\chardef\"='\"\cstok{\"a
\%\"} (a string token), \cstok{<\|>}, \cstok( (see rule 5), \cstok(,
\cstok{\$}, \cstok1 (a numeric token), \cstok5 (likewise numeric),
\cstok{\"+-\"} (a string token), and \cstok{\"\"}} (a string token that
denotes an empty sequence of characters).
All of these tokens are symbolic unless otherwise mentioned. \ (Notice that
four of the spaces and two of the periods were deleted by rule 1.
One way to verify that METAFONT\ finds precisely these tokens is to prepare a
test file that says "isolated' 'expression;'' on its first line and that
contains the stated text on its second line. Then respond to METAFONT's
error message by repeatedly typing "1'', so that one token is deleted
at a time.)

### Exercise
Criticize the following statement: METAFONT\ ignores all spaces in the
input.

#### Answer
The statement is basically true but potentially misleading. You can
insert any number of spaces *between* tokens without changing the
meaning of a program, but you cannot insert a space in the *middle*
of any token without changing something. You can delete spaces between
tokens *unless* that would "glue" two adjacent tokens together.

**[Dangerous Bend]** exercise True or false: If the syntax for *numeric token* were
changed to include a fourth alternative, '*digit string*'.'', the meaning
of METAFONT\ programs would not change in any way.

#### Answer
False. It may seem that this new sort of numeric token would be
recognized only in cases where the period is not followed by a digit,
hence the period would be dropped anyway by rule 1. However, the new rule
would have disastrous consequences in a line like "draw' 'z1..z2''!

\endchapter

Yet wee with all our seeking could see no tokens.

> --- PHILEMON , *'s Brittania* (1610)

Unpropitious tokens interfered.

> --- WILLIAM , *'s Iliad* (1791)


# Chapter 7. Variables

One of METAFONT's most important concepts is the notion of a
---something that can take on a variety of different
values. Indeed, this is one of the most important concepts in all of
mathematics, and variables play a prominent r\^ole in almost all
computer languages. The basic idea is that a program manipulates data,
and the data values are stored in little compartments of a computer's
memory. Each little compartment is a variable, and we refer to an item
of data by giving its compartment a name.

For example, the 'io.mf' program for the letter {\manual\IOO} in Chapter 5
contains lots of variables. Some of these, like "x1l'' and "y1'', represent
coordinates. Others, like "up'', represent
directions. The variables "em#'' and "thin#'' stand for physical,
machine-independent distances; the analogous variables "em'' and "thin''
stand for the corresponding machine-dependent distances in units of pixels.

These examples indicate that different variables are often related to each
other. There's an implicit connection between "em#'' and "em'',
between "x1'' and "y1''; the '"penpos"' convention
sets up relationships between "x1l'', "x1'', and "x1r''. By choosing
the names of variables carefully, programmers can make their programs
much easier to understand, because the relationships between variables
can be made to correspond to the structure
of their names.

In the previous chapter we discussed tokens, the atomic elements from which
all METAFONT\ programs are made. We learned that there are three kinds of
tokens: numeric (representing numbers), string (representing text), and
symbolic (representing everything else). Symbolic tokens have no
intrinsic meaning; any symbolic token can stand for whatever a programmer
wants it to represent.

Some symbolic tokens do, however, have predefined
meanings, when METAFONT\ begins its operations. For example, "+'' stands
initially for "plus," and ";'' stands for "finish the current
statement and move on to the next part of the program." It is customary
to let such tokens retain their primitive meanings, but any symbolic token
can actually be assigned a new meaning as a program is performed. For
example, the definition of "test_I'' in 'io.mf' makes that token stand
for a , i.e., a subroutine. We'll see later that you can
instruct METAFONT\ to "let' 'plus=+'', after which "plus'' will act just
like "+'' did.

METAFONT\ divides symbolic tokens into two categories, depending on their
current meaning. If the symbolic token currently stands for one of METAFONT's
primitive operations, or if it has been defined to be a macro, it is
called a ; otherwise it is called a . Almost
all symbolic tokens are tags, because only a few are defined to be sparks;
however, METAFONT\ programs typically involve lots of sparks, because sparks
are what make things happen. The symbolic tokens on the first five lines
of 'io.mf' include the following sparks:

"'

mode_setup ; := / define_pixels ( , )

"'

and the following tags:

"'

em # pt cap thin thick o

"'

(some of which appear several times). Tags are used to designate variables,
but sparks cannot be used within a variable's name.

Some variables, like "em#'', have names that are made from more than one token;
in fact, the variable "x1l'' is named by three tokens, one of which is
numeric. METAFONT\ has been designed so that it is easy to make compound names
that correspond to the relations between variables. Conventional programming
languages like would refer to "x1l'' by the more
cumbersome notation "x[1].l''; it turns out that "x[1].l'' is an
acceptable way to designate the variable 'x1l' in a METAFONT\ program, but the
shorthand form "x1l'' is a great convenience because such variables
are used frequently.

Here are the formal rules of syntax by which METAFONT\ understands the names of
variables:

\beginsyntax
<variable>\is<tag><suffix>
<suffix>\is<empty>\alt<suffix><subscript>\alt<suffix><tag>
<subscript>\is<numeric token>\alt\\{\char'\[}<numeric expression>\\]
\endsyntax
First comes a tag, like "x''; then comes a to the tag,
like "1l''.
The suffix might be empty, or it might consist of one or more subscripts
or tags that are tacked on to the original tag. A is
a numeric index that permits you to construct of related
variables. The subscript is either a single numeric token, or it is a formula
enclosed in square ; in the latter case the formula should produce a
numeric value. For example, "x[1]'' and "x[k]'' and "x[3-2k]'' all mean
the same thing as "x1'', if 'k' is a variable whose value is 1. But
"x.k'' is not the same; it is the tag "x'' suffixed by the tag "k'',
not the tag "x'' subscripted by the value of variable 'k'.

**[Dangerous Bend]** The variables "x1'' and "x01'' and "x1.00'' are identical.
Since any numeric token can be used as a subscript, fractional indices
are possible; for example, "x1.5'' is the same as "x[3/2]''. Notice,
however, that "B007'' and "B.007'' are *not* the same variable,
because the latter has a fractional subscript.

**[Dangerous Bend]** METAFONT\ makes each *suffix* as long as possible. In other words,
a *suffix* is always extended if it is followed by a *subscript*
or a *tag*.

**[Dangerous Bend]** exercise Explain how to type a reference to the doubly subscripted
variable "a[1][5]'' without using square brackets.

#### Answer
You can put a space between the subscripts, as in "a1' '5''. \
(We'll see later that a acts as a null symbol,
hence "a1\5'' is another solution.)

**[Dangerous Bend]** exercise Is it possible to refer to *any* variable without
using square brackets?

#### Answer
No; 'a[-1]' can't be accessed without using '[' and ']'. The
only other form of *subscript* is *numeric token*, which can't be
negative. \ (Well, strictly speaking, you could say "let' '?=[;'
'let' '??=]'' and then refer to "a?-1??''; but that's cheating.)

**[Double Dangerous Bend]** exercise Jonathan H. (a student) used "a.plus1'' as the name
of a variable at the beginning of his program; later he said "let'
'plus=+''. How could he refer to the variable "a.plus1'' after that?

#### Answer
Assuming that "+'' was still a spark when he said "let' 'plus=+'',
he can't refer to the variable "a.plus1'' unless he changes the meaning of
'plus' again to make it a tag. \ (We will eventually learn a way to do this
without permanently clobbering 'plus', as follows: '
'plus;' 'a.plus1' '.)

**[Dangerous Bend]** METAFONT\ has several special variables called {^internal
quantities} that are intimately wired-in to the computer's behavior.
For example, there's an internal quantity called '' that controls
whether or not a 'tfm' file is produced; another one called ''
governs whether or not titles like '"The' 'letter' 'O"' appear on your
terminal; still another one called '' affects the digitization of
curves. \ (A complete list of METAFONT's internal quantities appears in
Chapter 25.) \ The name of an internal quantity acts like a tag, but
internal quantities cannot be suffixed or subscripted.
Thus, the syntax rule for *variable*
should actually be replaced by a slightly more complicated pair of rules:
\beginsyntax
<variable>\is<external tag><suffix>\alt<internal quantity>
<tag>\is<external tag>\alt<internal quantity>
\endsyntax

**[Dangerous Bend]** exercise True or false: Every *variable* is a legal *suffix*.

#### Answer
False. After "newinternal x;'' you can't say
"x'*tag*' in a *suffix list*.

**[Double Dangerous Bend]** The "['' and "]'' that appear in the syntax for *subscript*
stand for any symbolic tokens whose current meanings are the same as
METAFONT's primitive meanings of left and right bracket, respectively;
those tokens don't necessarily have to be brackets. Conversely, if the
meanings of the tokens "['' and "]'' have been changed, brackets cannot
be used to delimit subscripts. Similar remarks apply to all of the
symbolic tokens in all of the syntax rules from now on. METAFONT\ doesn't look
at the form of a token; it considers only a token's current meaning.

The examples of METAFONT\ programs in this book have used two different
typographic conventions. Sometimes we refer to variables by using
and/or genuine subscripts, e.g., '"em"' and '$x_2r$';
but sometimes we refer to those same variables by using a -like
style of type, e.g., "em'' and "x2r''. In general, the typewriter style
is used when we are mainly concerned with the way a programmer is supposed
to type something that will appear on the terminal or in a file; but fancier
typography is used when we are focusing on the meaning of a program rather
than its ASCII representation. It should be clear how to convert the fancier
form into tokens that METAFONT\ can actually understand.

**[Dangerous Bend]** In general, we shall use italic type only for tags (e.g., "em",
"x", "r"), while boldface and roman type will be used for sparks
(e.g., @draw@, @fill@, cycle, rotated, sqrt). Tags that consist of special
characters instead of letters will sometimes get special treatment;
for example, 'em#' and 'z2'' might be rendered $"em"\0$ and $z'_2$,
respectively.

The variables we've discussed so far have almost always had numbers as their
values, but in fact METAFONT's variables are allowed to assume values of eight
different . A variable can be of type
\nobreak
- , representing the values '' or '';
- , representing sequences of ASCII characters;
- , representing a (possibly curved) line;
- , representing the shape of a pen nib;
- , representing an entire pattern of pixels;
- , representing the operations of scaling, rotating,
shifting, reflecting, and/or slanting;
- , representing two numbers (e.g., a point or a vector);
- , representing a single number.

If you want a variable to represent something besides a number, you must
first give a that states
what the type will be. But if you refer to a variable whose type has not
been declared, METAFONT\ won't complain, unless you try to use it in a way that
demands a value that isn't numeric.

Type declarations are easy. You simply name one of the eight types,
then you list the variables that you wish to declare for that type.
For example, the declaration

>
@pair@ "right", "left", $a.p$

says that "right" and "left" and $a.p$ will be variables of type @pair@,
so that equations like

>
$"right"=-"left"=2a.p=(1,0)$

can be given later. These equations, incidentally, define the values
$"right"=(1,0)$, $"left"=(-1,0)$, and $a.p=(.5,0)$. \ (Plain METAFONT\
has the stated values of "right" and "left" already built in.)

The rules for declarations are slightly trickier when subscripts are
involved, because METAFONT\ insists that all variables whose names are identical
except for subscript values must have the same type. It's possible to
set things up so that, for example, $a$ is numeric, $a.p$ is a pair,
$a.q$ is a pen, $a.r$ is a path, and $a_1$ is a string; but if $a_1$
is a string, then all other variables $a_2$, $a_3$, etc., must also be
strings. In order to enforce this restriction, METAFONT\ allows only
"collective" subscripts, represented by empty brackets '',
to appear in type declarations. For example,

"'

path r, r[], x[]arc, f[][]

"'

declares $r$ and all variables of the forms $r[i]$, $x[i]"arc"$,
and $f[i][j]$ to be path variables. This declaration doesn't affect
the types or values of other variables like $r[\,]"arc"$; it affects
only the variables that are specifically mentioned.

Declarations destroy all previous values of the variables being defined.
For example, the path declaration above makes $r$ and $r[i]$ and $x[i]"arc"$
and $f[i][j]$ undefined, even if those variables previously had paths
as their values. The idea is that all such variables will start out with a
clean slate so that they can receive appropriate new values based on
subsequent equations.

### Exercise
Numeric variables don't need to be declared. Therefore is there
ever any reason for saying "numeric' 'x''?

#### Answer
Yes, because it removes any existing value that $x$ may have
had, of whatever type; otherwise you couldn't safely use $x$ in a
numeric equation. It's wise to declare numeric variables when you're
not sure about their former status, and when you're sure that you don't
care what their previous value was. A numeric declaration together with a
comment also provides useful documentation. \ (Incidentally, "numeric' 'x''
doesn't affect other variables like "x2'' or "x.x'' that might be present.)

**[Dangerous Bend]** The formal syntax rules for type declarations explain these
grammatical conventions precisely. If the symbolic token that begins a
declared variable was previously a spark, it loses its former meaning and
immediately becomes a tag.
\beginsyntax
<declaration>\is<type><declaration list>
<type>\is[boolean]\alt[string]\alt[path]\alt[pen]
\alt[picture]\alt[transform]\alt[pair]\alt[numeric]
<declaration list>\is<declared variable>
\alt<declaration list>[,]<declared variable>
<declared variable>\is<symbolic token><declared suffix>
<declared suffix>\is<empty>\alt<declared suffix><tag>
\alt<declared suffix>\\{\char'\[}\\]
\endsyntax

**[Dangerous Bend]** exercise Find three errors in the supposed declaration
"transform' 't42,24t,,t,path''.

#### Answer
(a) The "42'' is illegal because subscripts must be collective.
\ (b) The "24'' is illegal because a *declared variable* must start with
a *symbolic token*, not a numeric token. \ (c) There's nothing wrong with
the consecutive commas; the second comma begins a *declared variable*, so
it loses its former meaning and becomes a tag. Thus METAFONT\ tries to declare
the variable ",t,path''. However, "path'' cannot appear in a suffix,
since it's a spark. \ (Yes, this is admittedly tricky. Computers follow rules.)

\endchapter

Beings low in the scale of nature are
more variable than those which are higher.

> --- CHARLES , *On the Origin of Species* (1859)

Among the variables, Beta ({\cmman) Persei}, or ,
is perhaps the most interesting, as its period is short.

> --- J. NORMAN , *Elements of Astronomy* (1870)


# Chapter 8. Algebraic Expressions

METAFONT\ programmers express themselves algebraically by writing algebraic
formulas called . The formulas are algebraic in the
sense that they involve variables as well as constants. By combining
variables and constants with appropriate mathematical operations, a
programmer can specify an amazing variety of things with comparative ease.

We have already seen many examples of expressions; our goal now is to make
a more systematic study of what is possible. The general idea is that an
expression is either a (e.g., '$x_1$') or a
(e.g., '20'), or it consists of an
(e.g., '$+$') together with its (e.g.,
'$x_1+20$'). The operands are, in turn, expressions built up in
the same way, perhaps enclosed in . For example,
'$(x_1+20)/(x_2-20)$' is an expression that stands for the quotient of two
subexpressions. It is possible to concoct extremely complicated algebraic
expressions, but even the most intricate constructions are built from
simple parts in simple ways.

Mathematicians spent hundreds of years developing good ways to write formulas;
then computer scientists came along and upset all the time-honored traditions.
The main reason for making a change was the fact that computers find it
difficult to deal with two-dimensional constructions like

>
$\displaystyle{x_1+20\over x_2-20}+\sqrt{a^2-{2\over3}\sqrt b}.$

One-dimensional sequences of tokens are much easier to input and to decode;
hence programming languages generally put such formulas all on one line,
by inserting parentheses, brackets, and asterisks as follows:

"'

(x[1]+20)/(x[2]-20)+sqrt(a**2-(2/3)*sqrt(b)).

"'

METAFONT\ will understand this formula, but it also accepts a notation that
is shorter and closer to the standard conventions of mathematics:

"'

(x1+20)/(x2-20)+sqrt(a**2-2/3sqrt b).

"'

We observed in the previous chapter that METAFONT\ allows you to write "x2''
instead of "x[2]''; similarly, you can write "2x'' instead of "2*x''
and "2/3x'' instead of "(2/3)*x''. Such operations are extremely common
in METAFONT\ programs, hence the language has been set up to facilitate them.
On the other hand, METAFONT\ doesn't free you from all the inconveniences of
computer languages; you must still write "x*k'' for the of
$x$ times $k$, and "x[k]'' for the variable $x$ subscripted by $k$,
in order to avoid confusion with the suffixed variable "x.k''.

We learned in the previous chapter that there are eight types of
variables: numeric, boolean, string, and so on. The same types apply
to expressions; METAFONT\ deals not only with numeric expressions but also
with boolean expressions, string expressions, and the others. For example,
'$(0,0)\to(x_1,y_1)$'
is a path-valued expression, formed by applying the operator '$\to$' to the
subexpressions '$(0,0)$' and '$(x_1,y_1)$'; these subexpressions, in turn,
have values of type "pair," and they have been built up from values of
type "numeric." Each operation produces a result whose type can be
determined from the types of the operands; furthermore, the simplest
expressions (variables and constants) always have a definite type.
Therefore the machine always knows what type of quantity it is dealing
with, after it has evaluated an expression.

If an expression contains several operators, METAFONT\ has to decide which

operation should be done first. For example, in the expression '$a-b+c$'
it is important to compute '$a-b$' first, then to add $c$; if '$b+c$' were
computed first, the result '$a-(b+c)$' would be quite different from the
usual conventions of mathematics. On the other hand, mathematicians
usually expect '$b/c$' to be computed first in an expression like
'$a-b/c$'; multiplications and divisions are usually performed before
additions and subtractions, unless the contrary is specifically indicated
by parentheses as in '$(a-b)/c$'. The general rule is to evaluate
subexpressions in parentheses first, then to do operations in order of
their ""; if two operations have the same precedence, the
left one is done first. For example, '$a-b/c$' is equivalent to
'$a-(b/c)$' because division takes precedence over subtraction; but
'$a-b+c$' is equivalent to '$(a-b)+c$' because left-to-right order is
used on operators of equal precedence.

It's convenient to think of operators as if they are tiny that
attract their operands; the magnets for '$\ast$' and '/' are stronger
than the magnets for '$+$' and '$-$', so they stick to their operands more
tightly and we want to perform them first.

METAFONT\ distinguishes four (and only four) levels of precedence. The
strongest magnets are those that join '2' to '$x$' and 'sqrt' to '$b$'
in expressions like '$2x$' and 'sqrt$\,b$'. The next strongest are
multiplicative operators like '$\ast$' and '/'; then come the additive
operators like '$+$' and '$-$'. The weakest magnets are operators like
'$\to$' or '$<$'. For example, the expression

>
$a+sqrt\,b/2x<c$

is equivalent to the fully parenthesized formula

>
$\bigl(a+\bigl((sqrt\,b)/(2x)\bigr)\bigr)<c$.

### Exercise
Insert parentheses into the formula "z1+z2..z3/4*5..z6-7*8z9'',
to show explicitly in what order METAFONT\ will do the operations.

#### Answer
'((z1+z2)..((z3/4)*5))..(z6-(7*(8z9)))'.

**[Dangerous Bend]** High-school algebra texts often avoid parentheses inside of
parentheses by using and . Therefore many people
have been trained to write

>
$\{a+[(sqrt\,b)/(2x)]\}<c$

instead of the fully parenthesized formula above. However, professional
mathematicians usually stick to only one kind of parentheses, because
braces and brackets have other meanings that are more important. In this
respect METAFONT\ is like the professionals: It reserves curly braces "''
and square brackets "[]'' for special purposes, so you should not
try to substitute them for parentheses.

**[Double Dangerous Bend]** If you really want alternatives to parentheses, there is actually
a way to get them. You can say, for example,

"'

delimiters [[ ]]; delimiters

"'

after which double brackets and braces can be used in formulas like

"'

a+[[(sqrt b)/(2x)]]<c.

"'

The symbolic token "{{'' has no relation to "{'', and it
has no primitive meaning, hence you are free to define it in any way you
like; the ^@delimiters@ command defines a new pair of delimiters. In formulas
with mixed delimiters as defined here, METAFONT\ will check that "[['' matches only
with "]]'', "'' only with "'', and "('' only with ")''; thus you
can more easily detect errors in large expressions. However, it's usually
unnecessary to have any delimiters other than parentheses, because large
expressions are rare, and because the rules of operator precedence make
most parentheses superfluous.

If you're reading this chapter carefully, you may be thinking, "Hey wait!
Isn't there a contradiction? A minute ago I was told that "2/3x'' stands
for "(2/3)*x'', but now the rules of precedence appear to state that
"2/3x'' really stands for "2/(3x)''. What gives?" Indeed, you have an
excellent point; but there is no contradiction, because of another rule that
hasn't been mentioned yet. When two *numeric tokens* are divided, the
magnetism of "/'' is stronger than usual;
in this case "/'' has the same precedence as the implied multiplication
operator in "3x''. Hence the operations in "2/3x'' are carried out from
left to right, as stated previously. \ (This is a good rule because it
is almost always what a METAFONT\ programmer wants. However, one should bear
in mind that "a/3x'' means "a/(3x)'' when 'a' is *not* a numeric token.)

Because of the rule in the previous paragraph, the METAFONT\ programs in this
book often say '${2\over3}x$' for what would be typed "2/3x'' in a file.
Such built-up are never used except when the numerator and
denominator are both numbers; a construction like "a/3x'' will always be
rendered as '$a/3x$', not '$\,{a\over3x}\,$'.

METAFONT\ knows how to do dozens of operations that haven't been mentioned yet
in this book. Let's take a look at some of them, so that we will know
they are available in case of need. It will be most instructive and
most fun to learn about expressions by interacting with the computer;
^^"tracingonline" ^^@scrollmode@ ^^@forever@ ^^@scantokens@
^^@message@
therefore you should prepare the following short file, called :

"'

string s[]; s1="abra";
path p[]; p1=(0,0)..(3,3); p2=(0,0)..(3,3)..cycle;
tracingonline:=1; scrollmode;
forever: message "gimme an expr: "; s0:=readstring;
show scantokens s0; endfor

"'

**[Dangerous Bend]** You don't need to understand what's in 'expr.mf' when you read this
chapter for the first time, because the file uses METAFONT\ in ways that will be
explained carefully later. But here is a translation, in case you're
curious: Line 1 declares all variables of the form $s_k$ to be strings, and
sets $s_1$ to the value '"abra"'. Line 2 declares all variables of the
form $p_k$ to be paths, and sets $p_1$ and $p_2$ to simple example paths.
Line 3 tells METAFONT\ to print diagnostic information , i.e., on the
terminal as well as in the ; it also establishes
'@scrollmode@', which means that the computer won't stop after error
messages. Lines 4 and 5 set up an infinite loop in which METAFONT\ reads an
expression from the terminal and shows the corresponding value.

\catcode'\"=\other
\indent to 160pt##&##
}

{\nobreak}}

If you start METAFONT\ and type "expr'' when it asks for an input file name,
it will read the file 'expr.mf' and then it will say '
'an' 'expr''. Here's where the fun starts: You can type any expression,
and METAFONT\ will compute
and display its value. Try it; type "2+2'' and *return*, obtaining the
value ">>' '4''. Isn't that amazing? Here are some more things to try:
\begindemo
\demohead
1.2-2.3&-1.1
1.3-2.4&-1.09999
1.3*1000&1300.00305
2.4*1000&2399.9939
3/8&0.375
.375*1000&375
1/3&0.33333
1/3*3&0.99998
0.99999&0.99998
1-epsilon&0.99998
1/(1/3)&3.00005
1/3.00005&0.33333
.1*10&1.00006
1+4epsilon&1.00006
\enddemo
These examples illustrate the small errors that occur because METAFONT\ does
"fixed binary" using integer multiples of $1\over65536$.
The result of $1.3-2.4$ is not quite the same as $-1.1$, because '1.3' is
a little bit larger than $13\over10$ and '2.4' is a little smaller
than $24\over10$. Small errors get magnified when they are multiplied by
1000, but even after magnification the discrepancies are negligible because
they are just tiny fractions of a pixel. You may be surprised that
1/3 times 3 comes out to be .99998 instead of .99999; the truth is that both
'0.99999' and '0.99998' represent the same value, namely $65535\over65536$; METAFONT\
displays this value as '0.99998' because it is closer to .99998 than to
.99999. Plain METAFONT\ defines ^"epsilon" to be $1\over65536$, the smallest
representable number that is greater than zero; therefore '1-epsilon'
is $65535\over65536$, and '1+4epsilon' is $65540\over65536$.
\begindemo
\demohead
4096&4095.99998\werror
infinity&4095.99998
1000*1000&32767.99998\werror
infinity+epsilon&4096
100*100&10000
.1(100*100)&1000.06104
(100*100)/3&3333.33333
\enddemo
METAFONT\ will complain that an "Enormous' 'number' 'has'
'been' 'reduced'' when you try to introduce constants that are 4096 or more.
Plain METAFONT\ defines ^"infinity" to be $4096-"epsilon"$, which is the largest
legal numeric token. On the other hand, it turns out that larger numbers
can actually arise when an expression is being evaluated; METAFONT\ doesn't
worry about this unless the resulting magnitude is at least 32768.

**[Dangerous Bend]** exercise If you try "100*100/3'' instead of "(100*100)/3'', you
get "3333.33282''. Why?

#### Answer
The fraction '100/3' is evaluated first (because such divisions
take precedence); the rounding error in this fraction is then magnified by 100.

**[Double Dangerous Bend]** Sometimes METAFONT\ will compute things more accurately than you would
expect from the examples above, because many of its internal calculations
are done with multiples of $2$ instead of $2$. For example,
if $t=3$ the result of "1/3t'' will be exactly 1
(not 0.99998); the same thing happens if you write "1/3(3)''.

Now let's try some more complicated expressions, using undefined
variables as well as constants. \ (Are you actually trying these
examples, or are you just reading the book? It's far better to type
them yourself and to watch what happens; in fact, you're also allowed
to type things that *aren't* in the book!)
\begindemo
\demohead
b+a&a+b
a+b&a+b
b+a-2b&a-b
2(a-b+.5)&2a-2b+1
.5(b-a)&-0.5a+0.5b
.5[a,b]&0.5a+0.5b
1/3[a,b]&0.66667a+0.33333b
0[a,b]&a
a[2,3]&a+2
t[a,a+1]&t+a
a*b&b\werror
1/b&b\werror
\enddemo
METAFONT\ has a preferred way to arrange variables in order when they are added
together; therefore '$a+b$' and '$b+a$' give the same result. Notice that
the construction '$.5[a,b]$' specifies a number that's halfway
between $a$ and $b$, as explained in Chapter 2. METAFONT\ does not allow you to
two unknown numeric quantities together, nor can you by an
unknown numeric; all of the unknown expressions that METAFONT\ works with must be
"," i.e., they must be sums of variables with constant
coefficients, plus an optional constant. \ (You might want to try typing
"t[a,b]'' now, in order to see what error message is given.)
\begindemo
\demohead
sqrt 2&1.41422
sqrt 100&10
sqrt 100*100&1000
sqrt(100*100)&100
sqrt 100(100)&100
sqrt sqrt 100(100)&10
sqrt .01&0.09998
0.09998**2&0.01
2**1/2&1.41422
sqrt 2**2&2
sqrt -1&0\werror
sqrt a&a\werror
\enddemo
Since has more "magnetism" than '*', the formula 'sqrt' '100*100'

is evaluated as '(sqrt' '100)*100'; but in "sqrt' '100(100)'' the
'100(100)' is computed first. The reason is that "(sqrt' '100)(100)'' isn't
a legal expression, so the operations in "sqrt' '100(100)'' must be carried
out from right to left. If you are unsure about the order of evaluation,
you can always insert parentheses; but you'll find that METAFONT's rules of
precedence are fairly natural as you gain experience.

### Exercise
Is "sqrt' '2**2'' computed as "(sqrt' '2)**2'' or as
"sqrt(2**2)''?

#### Answer
A 'sqrt' takes precedence over any operation with two operands, hence
the machine computes "(sqrt' '2)**2''; METAFONT\ was somewhat lucky that the
answer turned out to be exactly 2. \ (The 'sqrt' operation computes the
nearest multiple of $1\over65536$, and the rounding error in this quantity
is magnified when it is squared. If you try 'sqrt' '3**2', you'll get
'3.00002'; also 'sqrt' '2**4' turns out to be '4.00002'.) \ Incidentally,
the operation of plain METAFONT\ has the same precedence as '*' and '/';
hence "x*y**2'' means the same as "(x*y)**2'', and "-x**2'' means
"(-x)**2'', contrary to the conventions of .

Some METAFONT\ expressions have '' or '' values, instead of numbers;
we will see later that they can be used to adapt METAFONT\ programs to special
conditions.
\begindemo
\demohead
0<1&true
0=1&false
a+1>a&true
a>=b&false\werror
"abc"<="b"&true
"B">"a!"&false
"b">"a?"&true
(1,2)<>(0,4)&true
(1,2)<(0,4)&false
(1,a)>(0,b)&true
numeric a&true
known a&false
not pen a&true
known "a" and numeric 1&true
(0>1) or (a<a)&false
0>1 or a<a&a\werrors
\enddemo
^^@and@ ^^@or@
The tokens '', '', and '' stand respectively for the
, , and
. When strings are compared, METAFONT\ uses the order of words in
a dictionary, except that it uses ASCII code to define ordering of individual
characters; thus, all uppercase letters are considered to be less than all
lowercase letters. \ (See Appendix C.) \ When pairs of numbers are
compared, METAFONT\ considers only the $x$ coordinates, unless the $x$ coordinates
are equal; in the latter case it compares the $y$ coordinates. The type
of an expression can be ascertained by an expression like "pair' 'a'',
which is true if and only if 'a' is a pair.
The expression "known' 'a'' is true if and only if the value
of 'a' is fully known.

**[Dangerous Bend]** exercise What causes the error messages in "0>1' 'or' 'a<a''?

#### Answer
Since '' has stronger precedence than '$<$' or '$>$',
METAFONT\ tries to evaluate this expression by putting things in
parentheses as follows: '$(0>(1\mathbinora))<a$'. Now
'$1\mathbinora$' makes no sense, because 'or' operates only on
booleans; in such cases METAFONT\ uses the right operand '$a$' as the result. Then
'$\mkern1mu0>a$' is indeterminate because $a$ is unknown; METAFONT\ treats this as
@false@. Finally '$@false@<a$' is another illegal combination of types.

**[Dangerous Bend]** The rest of this chapter is entirely preceded by "dangerous bend"
signs, so you can safely omit it on first reading (unless you're hooked
and can't stop).

**[Dangerous Bend]** METAFONT\ expressions can include many operations that are
less familiar but still useful. For example, the and
operations compute the and of numbers, strings,
or pairs:
\begindemo
\demohead
max(1,-2,4)&4
min(1,-2,4)&-2
max("a","b","ab")&"b"
min("a","b","ab")&"a"
max((1,5),(0,6),(1,4))&(1,5)
min((1,5),(0,6),(1,4))&(0,6)
max(.5a+1,.5a-1)&0.5a+1
\enddemo
Numbers can be converted to in a variety of ways:
\begindemo
\demohead
floor 3.14159&3
floor -3.14159&-4
floor -epsilon&-1
floor infinity&4095
ceiling 3.14159&4
ceiling -3.14159&-3
round 3.14159&3
round -3.14159&-3
round(1.1,2.8)&(1,3)
round(3.5,-3.5)&(4,-3)
round a&a+0.5\werror
8 mod 3&2
-8 mod 3&1
.8 mod .3&0.2
\enddemo
The '' operation computes the that is less than
or equal to its operand; this quantity is often denoted by $\lfloor x\rfloor$
in mathematics texts. Plain METAFONT\ also includes the analogous ''
operation $\lceil x\rceil$, which is the greater than or
equal to $x$. Furthermore, '$\,x$' is the integer nearest to $x$;
plain METAFONT\ computes this by using the formula $\lfloor x+.5\rfloor$, and
applies it to both components of a pair if a pair is being rounded. The
of $x$ with respect to $y$, written '$x\bmod y$', is
calculated by using the formula $x-y\lfloor x/y\rfloor$.
\begindemo
\demohead
abs -7&7
abs(3,4)&5
length(3,4)&5
3++4&5
300++400&500
sqrt(300**2 + 400**2)&181.01933\werrors
1++1&1.4142
0 ++ -7&7
5+-+4&3
\enddemo

The '' operation is called ; $a\pyth+b$
is the same thing as $\sqrt{\stt a^2+b^2}$. Most of the
operations in computer programs could probably be avoided if $++$ were
more widely available, because people seem to want square roots primarily
when they are computing distances. Notice that $a\pyth+b\pyth+c=
\sqrt{\stt a^2+b^2+c^2}$; we have the identity $(a\pyth+b)\pyth+c=a\pyth+(
b\pyth+c)$ as well as $a\pyth+b=b\pyth+a$. It is better to use Pythagorean
addition than to calculate $\sqrt{\stt a^2+b^2}$, because the computation
of $a^2$ and $b^2$ might produce numbers that are too large even when
$a\pyth+b$ is rather small. There's also an inverse operation,
, which is denoted by ''; the quantity
$a\mathbin+-+b$ is equal to $\sqrt{\stt a^2-b^2}$.

**[Dangerous Bend]** exercise When the author was preparing these examples he typed
"0++-7'' and was surprised to get the answer "0''. Why should this not
have been a surprise?

#### Answer
The token "++-'' is undefined, so it is a tag; therefore
'++-7' is a subscripted variable, which was multiplied by zero.

**[Double Dangerous Bend]** exercise (For mathematicians.) \ Although the Pythagorean addition
operation is associative and commutative, METAFONT\ says that
$5\pyth+4\pyth+2\pyth+2=7=2\pyth+2\pyth+4\pyth+5$ yet
$2\pyth+4\pyth+5\pyth+2=6.99998$. Why?

#### Answer
The associative law is valid for exact computations, but not
for rounded computations. For example, it fails even in the case of
multiplication, since $(.1\ast.1)\ast10=0.09995$ while $.1\ast(.1\ast10)=.1$
when products are rounded to the nearest multiples of $1\over65536$.
However, this observation doesn't quite explain the stated example, which
would have yielded 7 in all cases if METAFONT\ had computed $2\pyth+4$ with
full accuracy! The closest approximation to $\sqrt20$ is
$4{30942\over65536}$, but $2\pyth+4$ turns out to be $4{30941\over65536}$
instead. METAFONT\ computes the absolutely best possible approximations to the
true answers when it does multiplications, divisions, and square roots,
but not when it does Pythagorean operations.

**[Dangerous Bend]** METAFONT\ uses the names '' and '' for the
functions and , because METAFONT's operations are designed to
deal with angles expressed in degrees. But it turns out that programmers
rarely need to refer to sines and cosines explicitly, because the ''
and '' functions provide most of what a font designer needs.
\begindemo
\demohead
sind 30&0.5
cosd 30&0.86603
sind -30&-0.5
cosd 360&1
sind 10 ++ cosd 10&1
dir 30&(0.86603,0.5)
dir -90&(0,-1)
angle(1,1)&45
angle(1,2)&63.43495
angle(1,-2)&-63.43495
sind 63.43495 / cosd 63.43495&1.99997
angle up&90
angle left&180
angle(-1000,-epsilon)&-180
angle dir 60&60.00008
angle(0,0)&0\werror
\enddemo
Plain METAFONT\ defines 'dir$\,x$' to be the pair of values $(\mathopcosdx,
\mathopsindx)$; this is a vector, which points $x$ degrees above the
rightward horizon. Conversely, the 'angle' operator determines the angle
that corresponds to a given vector.

**[Double Dangerous Bend]** Logarithms and exponentials are computed with respect to an
unusual base, designed to enhance the accuracy of calculations
involving fixed-radix numbers in METAFONT's range. The values $\,x=256\ln x$
and $\,x=e$ produce reasonably good results when
$x\mathbin{\ast\ast}y$ is computed by the formula mexp$(y\ast\mathopmlog x)$.
\begindemo
\demohead
mlog 2&177.44568
mexp mlog 2&2
mexp 8 mlog 2&256
mexp 256&2.71828
mlog 2.71828&255.99954
mlog 2.71829&256.00098

15 mlog 2&2661.68518
mexp 2661.68518&32767.99998
mexp 2661.68519&32767.99998\werror
mexp-2661.68519&0.00003
\enddemo

**[Dangerous Bend]** METAFONT\ also generates two flavors of random numbers. It is very
unlikely that you will get the particular values shown in the following
examples, when you do the experiment yourself, because the results come
out different each time the computer is asked for a new random number
(unless you have specified a "seed value" as explained in Chapter 21).
\begindemo
You type& And the result might be

uniformdeviate 100&47.4241
uniformdeviate 100&97.28148
uniformdeviate -100&-36.1628
(normaldeviate,normaldeviate)&(0.46236,-1.87648)
\enddemo
The value of 'uniformdeviate100' is a random number between 0 and 100;

the value of 'normaldeviate' is a normally distributed random number whose
mean value is zero and whose standard deviation is unity. Chapter 21 explains
what this means and gives several applications.

**[Dangerous Bend]** Besides all of these operations on numbers, METAFONT\ has a rich collection

of operations on pairs, some of which are indicated in the following examples:
\begindemo
\demohead
right&(1,0)
(1,2)+(3,4)&(4,6)
1/3(3,10)&(1,3.33333)
z2-z1&(-x1+x2,-y1+y2)
.2[z1,z2]&(0.8x1+0.2x2,0.8y1+0.2y2)
3z&(3x,3y)
z scaled 3&(3x,3y)
z xscaled 2 yscaled 1/2&(2x,0.5y)
z shifted (2,3)&(x+2,y+3)
z shifted 3right&(x+3,y)
z slanted 1/6&(0.16667y+x,y)
z rotated 90&(-y,x)
z rotated 30&(-0.5y+0.86603x,0.86603y+0.5x)
xpart(z rotated 30)&-0.5y+0.86603x
ypart(z rotated 30)&0.86603y+0.5x
(1,2)*(3,4)&(3,4)\werror
(1,2)zscaled(3,4)&(-5,10)
(a,b)zscaled(3,4)&(-4b+3a,3b+4a)
(a,b)zscaled dir 30&(-0.5b+0.86603a,0.86603b+0.5a)
(1,2)dotprod(3,4)&11
(a,b)dotprod(3,4)&4b+3a
dir 21 dotprod dir 51&0.86603
(3,4)dotprod((30,40)rotated 90)&0
\enddemo
(Recall that plain METAFONT\ converts "z$'' into "(x$,y$)'' when '$' is any
*suffix*.) \ ^^"right"
^^"z" The operations exhibited here are almost
all self-evident. When a point or vector is , it is moved
counterclockwise about $(0,0)$ through a given number
of degrees. METAFONT\ computes the rotated coordinates by using
and in an appropriate way; you don't have to
remember the formulas! Although you cannot use "*'' to multiply
a pair by a pair, you can use '' to get the effect of
multiplication: Since $(1+2i)$ times $(3+4i)$ is
$-5+10i$, we have $(1,2)\mathbinzscaled(3,4)=(-5,10)$.
There's also a that converts pairs into numbers:
$(a,b)\mathbindotprod(c,d\mkern1mu)=ac+bd$. This is the
"," often written '$(a,b)\cdot(c,d\mkern1mu)$' in
mathematics texts; it turns out to be equal to $a\pyth+b$ times
$c\pyth+d$ times the cosine of the angle between the vectors $(a,b)$ and
$(c,d)$. Since cosd$\,90^\circ=0$, two vectors are
to each other if and only if their dot is zero.

**[Dangerous Bend]** There are operations on strings, paths, and the other types too;
we shall study such things carefully in later chapters. For now, it will
suffice to give a few examples, keeping in mind that the file 'expr.mf'
defines 's' with any subscript to be a , while 'p' with any subscript
is a path. Furthermore $s_1$ has been given the value '"abra"', while
$p_1$ is '$(0,0)\to(3,3)$' and $p_2$ is '$(0,0)\to(3,3)\to\cycle$'.
\begindemo
\demohead
s2&unknown string s2
s1\&"cad"\&s1&"abracadabra"
length s1&4
length p1&1
length p2&2
cycle p1&false
cycle p2&true
substring (0,2) of s1&"ab"
substring (2,infinity) of s1&"ra"
point 0 of p1&(0,0)
point 1 of p1&(3,3)
point .5 of p1&(1.5,1.5)
point infinity of p1&(3,3)
point .5 of p2&(3,0)
point 1.5 of p2&(0,3)
point 2 of p2&(0,0)
point 2+epsilon of p2&(0.00009,-0.00009)
point -epsilon of p2&(-0.00009,0.00009)
point -1 of p1&(0,0)
direction 0 of p1&(1,1)
direction 0 of p2&(4,-4)
direction 1 of p2&(-4,4)
\enddemo

The of a path is the number of '$\to$' steps that it contains;
the construction ' *path*' can be used to tell whether or not a
particular path is cyclic. If you say just "p1'' you get to see
path $p_1$ with its :

"'

(0,0)..controls (1,1) and (2,2)
..(3,3)

"'

Similarly, "p2'' is

"'

(0,0)..controls (2,-2) and (5,1)
..(3,3)..controls (1,5) and (-2,2)
..cycle

"'

and "subpath' '(0,1)' 'of' 'p2'' is analogous to a :

"'

(0,0)..controls (2,-2) and (5,1)
..(3,3)

"'

The expression 'point $t$ of $p_2$' gives the position of a point that
moves along path $p_2$, starting with the initial point $(0,0)$ at $t=0$,
then reaching point $(3,3)$ at $t=1$, etc.;
the value at $t=1/2$ is the
third-order midpoint obtained by the construction of Chapter 3, using
intermediate control points $(2,-2)$ and $(5,1)$.
Since $p_2$ is a cyclic path of length 2,
point $(t+2)$ of $p_2$ is the same as point $t$. Path $p_1$ is not
cyclic, so its points turn out to be identical to point 0 when $t<0$,
and identical to point 1 when $t>1$. The expression 'direction $t$
of *path*' is similar to 'point $t$ of *path*'; it yields a vector for the
direction of travel at time $t$.

{
\medbreak
shape 14 3pc 12pc 3pc 12pc
0pc 15pc 0pc 15pc 0pc 15pc 0pc 15pc 0pc 15pc 0pc 15pc
0pc 15pc 0pc 15pc 0pc 15pc 0pc 15pc 0pc 15pc 0pc 29pc

to0pt{\dbend}
\rightfig 8a (12pc x 12pc) ^16pt
Paths are not necessarily traversed at constant speed. For example,
the diagram at the right shows point $t$ of $p_2$ at twenty equally
spaced values of $t$.
METAFONT\ moves faster in this case at time 1.0 than at time 1.2; but the
points are spread out fairly well, so the concept of fractional
time can be useful. The diagram shows, incidentally, that
path $p_2$ is not an especially good approximation to
a circle; there is no left-right symmetry, although the curve from point 1
to point 2 is a mirror image of the curve from point 0 to point 1.
This lack of circularity is not surprising, since
$p_2$ was defined by simply specifying two points, $(0,0)$ and $(3,3)$;
at least four points are needed to get a path that is convincingly round.
fillskip=0pt}

**[Double Dangerous Bend]** The operation "&'' can be used to splice paths
together in much the same way as it concatenates strings. For example, if
you type "p2' '&' 'p1'', you get the path of length 3 that is obtained by
breaking the cyclic connection at the end of path $p_2$ and attaching $p_1$:

"'

(0,0)..controls (2,-2) and (5,1)
..(3,3)..controls (1,5) and (-2,2)
..(0,0)..controls (1,1) and (2,2)
..(3,3)

"'

Concatenated paths must have identical endpoints at the junction.

**[Double Dangerous Bend]** You can even "slow down the clock" by concatenating subpaths
that have non-integer time specifications. For example, here's what you
get if you ask for "subpath' '(0,.5)' 'of' 'p2' '&' 'subpath' '(.5,2)'
'of' 'p2' '&' 'cycle'':

"'

(0,0)..controls (1,-1) and (2.25,-0.75)
..(3,0)..controls (3.75,0.75) and (4,2)
..(3,3)..controls (1,5) and (-2,2)
..cycle

"'

When $t$ goes from 0 to 1 in subpath $(0,.5)$ of $p_2$, you get the same
points as when $t$ goes from 0 to .5 in $p_2$; when $t$ goes from 0 to 1
in subpath $(.5,2)$ of $p_2$, you get the same points as when $t$ goes
from .5 to 1 in $p_2$; but when $t$ goes from 1 to 2 in subpath
$(.5,2)$ of $p_2$, it's the same as the segment from 1 to 2 in $p_2$.

**[Dangerous Bend]** Let's conclude this chapter by discussing the exact rules of
by which METAFONT\ decides what operations to do first. The
informal notion of "magnetism" gives a good intuitive picture of what
happens, but syntax rules express things unambiguously in borderline cases.

**[Dangerous Bend]** The four levels of precedence correspond to four kinds of formulas,
which are called primaries, secondaries, tertiaries, and
expressions. A is a variable or a constant or a
tightly bound unit like "2x'' or "sqrt 2''; a
is a primary or a sequence of primaries connected by multiplicative
operators like "*'' or "scaled''; a is a secondary
or a sequence of secondaries connected by additive operators like "+''
or "++''; an is a tertiary or a sequence of
tertiaries connected by external operators like "<'' or "..''. For example,
the expression

"'

a+b/2>3c*sqrt4d

"'

is composed of the primaries "a'', "b'', "2'', "3c'', and "sqrt4d'';
the last of these is a primary containing "4d'' as a primary within itself.
The subformulas "a'', "b/2'', and "3c*sqrt4d'' are secondaries; the
subformulas "a+b/2'' and "3c*sqrt4d'' are tertiaries.

**[Dangerous Bend]** If an expression is enclosed in parentheses, it becomes a primary
that can be used to build up larger secondaries, tertiaries, etc.

**[Dangerous Bend]** The full syntax for expressions is quite long, but most of it
falls into a simple pattern. If $\alpha$, $\beta$, and $\gamma$ are
any "types"---numeric, boolean, string, etc.---then *$\alpha$ variable*
refers to a variable of type $\alpha$, *$\beta$ primary* refers to a
primary of type $\beta$, and so on. Almost all of the syntax rules fit into
the following general framework:
\beginsyntax
<$\alpha$ primary>\is<$\alpha$ variable>\alt<$\alpha$ constant>
\alt[(]<$\alpha$ expression>[)]
\alt<operator that takes type $\beta$ to type $\alpha$><$\beta$ primary>
<$\alpha$ secondary>\is*$\alpha$ primary*
\alt<$\beta$ secondary><multiplicative op taking types $\beta$ and
$\gamma$ to $\alpha$><$\gamma$ primary>
<$\alpha$ tertiary>\is*$\alpha$ secondary*
\alt<$\beta$ tertiary><additive op taking types $\beta$ and
$\gamma$ to $\alpha$><$\gamma$ secondary>
<$\alpha$ expression>\is<$\alpha$ tertiary>
\alt<$\beta$ expression><external op taking types $\beta$ and
$\gamma$ to $\alpha$><$\gamma$ tertiary>
\endsyntax
These schematic rules don't give the whole story, but they do give the
general structure of the plot.

**[Dangerous Bend]** Chapter 25 spells out all of the syntax rules for all types of
expressions. We shall consider only a portion of the numeric and pair
cases here, in order to have a foretaste of the complete menu:

\beginsyntax
<numeric atom>\is<numeric variable>
\alt<numeric token primary>
\alt[(]<numeric expression>[)]
\alt[normaldeviate]
\alt[length]<string primary>
\alt[length]<path primary>
\alt[length]<pair primary>
\alt[angle]<pair primary>
\alt[xpart]<pair primary>
\alt[ypart]<pair primary>
\alt<numeric operator><numeric primary>
<numeric token primary>\is<numeric token>[/]<numeric token>
\alt<numeric token not followed by
'/$\langle$numeric token$\rangle$'>
<numeric primary>\is<numeric atom not followed by []<expression>[,]>
\alt<numeric atom>[]<numeric expression>
[,]<numeric expression>[]
<numeric operator>\is[sqrt]\alt[sind]\alt[cosd]\alt[mlog]\alt[mexp]
\alt[floor]\alt[uniformdeviate]\alt<scalar multiplication operator>
<scalar multiplication operator>\is<plus or minus>
\alt<numeric token primary not followed by
+ or - or a numeric token>
<numeric secondary>\is<numeric primary>
\alt<numeric secondary><times or over><numeric primary>
<times or over>\is[*]\alt[/]
<numeric tertiary>\is<numeric secondary>
\alt<numeric tertiary><plus or minus><numeric secondary>
\alt<numeric tertiary><Pythagorean plus or minus><numeric secondary>
<plus or minus>\is[+]\alt[-]
<Pythagorean plus or minus>\is[++]\alt[+-+]
<numeric expression>\is<numeric tertiary>
\endsyntax
All of the finicky details about and such things are made
explicit by this syntax. For example, we can use the rules to deduce that
"sind-1/3x-2'' is interpreted as "(sind(-(1/3x)))-2''; notice that the
first minus sign in this formula is considered to be a "scalar multiplication
operator," which comes in at the primary level, while the second one denotes
subtraction and enters in the construction of *numeric tertiary*. The
or "" operation '$t[a,b]$' is handled at the
primary level.

**[Dangerous Bend]** Several operations that haven't been discussed yet do not appear
in the syntax above, but they fit into the same general pattern; for example,
we will see later that '*string primary*' and '\<transform
primary>' are additional cases of the syntax for *numeric primary*.
On the other hand, several operations that we have discussed in this chapter
do not appear in the syntax, because they are not primitives of METAFONT\ itself;
they are defined in the plain METAFONT\ base (Appendix B). For example,
'' is analogous to "floor'', and '' is analogous to "*''.
Chapter 20 explains how METAFONT\ allows extensions to its built-in syntax,
so that additional operations can be added at will.

**[Dangerous Bend]** exercise How does METAFONT\ interpret "2' '2''?
\ (There's a space between the 2's.)

#### Answer
It's impossible to make an expression from '*numeric token*
*numeric token*', because the rule for *scalar multiplication operator*
specifically prohibits this. METAFONT\ will recognize the first "2'' as
a *numeric primary*, which is ultimately regarded as a \<numeric
expression>; the other "2'' will probably be an extra token that is
flushed away after an error message has been given.

**[Double Dangerous Bend]** exercise According to 'expr.mf', the value of "1/2/3/4'' is
'0.66667'; the value of "a/2/3/4'' is '0.375a'. Explain why.

#### Answer
If a numeric token is followed by "/'*numeric token*' but
not preceded by '*numeric token*'/'', the syntax allows it to become part of
an expression only by using the first case of \<numeric token
primary>. Therefore "1/2/3/4'' must be treated as "(1/2)/(3/4)'',
and "a/2/3/4'' must be treated as "a/(2/3)/4''.

**[Dangerous Bend]** The rules of *pair expression* are similar to those for
*numeric expression*, so it's convenient to learn them both at the same time.
\beginsyntax
<pair primary>\is<pair variable>
\alt[(]<numeric expression>[,]<numeric expression>[)]
\alt[(]<pair expression>[)]
\alt<numeric atom>[]<pair expression>
[,]<pair expression>[]
\alt[point]<numeric expression>[of]<path primary>
\alt<scalar multiplication operator><pair primary>
<pair secondary>\is<pair primary>
\alt<pair secondary><times or over><numeric primary>
\alt<numeric secondary>[*]<pair primary>
\alt<pair secondary><transformer>
<transformer>\is[rotated]<numeric primary>
\alt[scaled]<numeric primary>
\alt[shifted]<pair primary>
\alt[slanted]<numeric primary>
\alt[transformed]<transform primary>
\alt[xscaled]<numeric primary>
\alt[yscaled]<numeric primary>
\alt[zscaled]<pair primary>
<pair tertiary>\is<pair secondary>
\alt<pair tertiary><plus or minus><pair secondary>
<pair expression>\is<pair tertiary>
\endsyntax

**[Dangerous Bend]** exercise Try to guess the syntax rules for *string primary*,
*string secondary*, $\langle$string tertiary$\rangle$, and \<string
expression>, based solely on the examples that have appeared in this
chapter. \ [*Hint:* The "&'' operation has the same precedence
as "..''.]

#### Answer
*string primary*\is*string variable*break
\alt*string token*break

\alt\\(*string expression*\\)break
\alt\\substring*pair expression*\\of*string primary*break
*string secondary*\is*string primary*break
*string tertiary*\is*string secondary*break
*string expression*\is*string tertiary*break
\alt*string expression*\\{\char'\&}*string tertiary*

(The full syntax in Chapter 25 includes several more varieties of
*string primary* that haven't been hinted at yet.)

\endchapter

A maiden was sitting there who was lovely as any picture,

nay, so beautiful that no words can express it.

> --- JAKOB and WILHELM , *Fairy Tales* (1815)

He looked astonished at the expression.

> --- EMILY , *Wuthering Heights* (1847)


# Chapter 9. Equations

The variables in a METAFONT\ program receive their values by appearing in
, which express relationships that the programmer
wants to achieve. We've seen in the previous chapter that algebraic
expressions provide a rich language for dealing with both numerical
and graphical relationships. Thus it is possible to express a great
variety of design objectives in precise form by stating that certain
algebraic expressions should be equal to each other.

The most important things a METAFONT\ programmer needs to know about
equations are (1) how to translate intuitive design concepts into
formal equations, and (2) how to translate formal equations into
intuitive design concepts. In other words, it's important to be able
to *write* equations, and it's also important to be able to
*read* equations that you or somebody else has written. This
is not nearly as difficult as it might seem at first. The best way
to learn (1) is to get a lot of practice with (2) and to generalize
from specific examples. Therefore we shall begin this chapter by
translating a lot of equations into "simple English."

={\indent$z_12-z_11=z_14-z_13$}
\longesteq=

to\longesteq{\indent#1}
\hangindent\longesteq\ignorespaces}

to\longesteq{\indent Equation}
*Translation*

\\$a=3.14$\\
The value of $a$ should be 3.14.

\\$3.14=a$\\
The number 3.14 should be the value of $a$. \ (This means the same
thing as '$a=3.14$'; the left and right sides of an equation can be
interchanged without affecting the meaning of that equation in any way.)

\\$"mode"="smoke"$\\
The value of ^"mode" should be equal to the value of ^"smoke". \
(Plain METAFONT\ assigns a special meaning to '"smoke"', so that if
^@mode\_setup@ is invoked when $"mode"="smoke"$ the computer will
prepare "smoke proofs" as explained in Chapter 5 and Appendix H.)

\\$y_3=0$\\
The $y$ coordinate of point 3 should be zero; i.e., point 3 should
be at the . \ (Point 3 is also known as $z_3$, which is an
abbreviation for the pair of coordinates $(x_3,y_3)$, if you are
using the conventions of plain METAFONT\!.)

\\$x_9=0$\\
The $x$ coordinate of point 9 should be zero; i.e., point 9 should
be at the left edge of the type box that encloses the current character.

\\$x_1l="curve\_sidebar"$\\
The $x$ coordinate of point $1l$ should be equal to the value of the
variable called "curve\_sidebar". This puts $z_1l$ a certain
distance from the left edge of the type.

\\$x_1=x_2$\\
Points 1 and 2 should have the same $x$ coordinate; i.e., they should
have the same horizontal position, so that one will lie directly
above or below the other.

\\$y_4=y_5+1$\\
Point 4 should be one pixel higher than point 5.
\ (However, points 4 and 5 might be far apart; this equation
says nothing about the relation between $x_4$ and $x_5$.)

\\$y_6=y_7+2"mm"$\\
Point 6 should be two millimeters higher than point 7. \ (Plain METAFONT's
^@mode\_setup@ routine sets variable ^"mm" to the number of pixels in a
millimeter, based on the resolution determined by "mode" and "mag".)

\\$x_4=w-.01"in"$\\
Point 4 should be one-hundredth of an inch inside the right edge of
the type. \ (Plain METAFONT's ^@beginchar@ routine sets variable equal
to the width of whatever character is currently being drawn, expressed in
pixels.)

\\$y_4=.5h$\\
Point 4 should be halfway between the baseline and the top of the type.
\ (Plain METAFONT's @beginchar@ sets to the height of the
current character, in pixels.)

\\$y_6=-d$\\
Point 6 should be below the baseline, at the bottom edge of the type.
\ (With plain METAFONT's @beginchar@ each
character has a "" that runs from $(0,h)$
at the upper left and $(w,h)$ at the upper right to $(0,-d)$ and $(w,-d)$
at the lower left and lower right; variable represents the depth of
the type. The values of $w$, $h$, and $d$ might change from character to
character, since the individual pieces of type need not have the same size
in a computer-produced font.)

\\$y_8=.5[h,-d]$\\
Point 8 should be halfway between the top and bottom edges of the type.

\\$w-x_5={2\over3}x_6$\\
The distance from point 5 to the right edge of the type should be
two-thirds of the distance from point 6 to the left edge of the type.
\ (Since $w$ is at the right edge, $w-x_5$ is the from
point 5 to the right edge.)

\\$z_0=(0,0)$\\
Point 0 should be at the of the current character,
i.e., it should be on the baseline at the left edge of the type.
This equation is an abbreviation for two equations, '$x_0=0$' and '$y_0=0$',
because an equation between pairs of coordinates implies that the $x$
and $y$ coordinates must both agree. \ (Incidentally, plain METAFONT\
defines a variable called ^"origin" whose value is $(0,0)$; hence
this equation could also have been written '$z_0="origin"$'.)

\\$z_9=(w,h)$\\
Point 9 should be at the upper right corner of the current character's
bounding box.

\\$"top"\,z_8=(.5w,h)$\\
If the pen that has currently been "picked up" is placed at point 8,
its top edge should be at the top edge of the type. Furthermore,
$x_8$ should be $.5w$; i.e., point 8 should be centered between the
left and right edges of the type. \ (Chapter 4 contains further
examples of '^"top"', as well as the corresponding operations
'"bot"', '"lft"', and '"rt"'.)

\\$z_4={3\over7}[z_5,z_6]$\\
Point 4 should be three-sevenths of the way from point 5 to point 6.

\\$z_12-z_11=z_14-z_13$\\
The that moves from point 11 to point 12 should be the same
as the vector that moves from point 13 to point 14. In other words,
point 12 should have the same direction and distance from point 11
as point 14 has from point 13.

\\\smash{{{$z_3-z_2=$}
{$(z_4\!-\!z_2)$ rotated 15}}}\\
Points 3 and 4 should be at the same distance from point 2, but
the direction to point 3 should be 15 degrees counterclockwise from
the direction to point 4.

### Exercise
Translate the following equations into "simple English":
\ (a) $x_7-9=x_1$; \ (b) $z_7=(x_4,.5[y_4,y_5])$; \
(c) $"lft"\,z_21="rt"\,z_20+1$.

#### Answer
(a) Point 1 should lie nine pixels to the left of point 7,
considering horizontal positions only; no information is given about the
vertical positions $y_1$ or $y_7$. \ (b) Point 7 should sit directly
above or below point 4, and its distance up from the baseline should be
halfway between that of points 4 and 5. \ (c) The left edge of the
currently-picked-up pen, when that pen is centered at point 21, should be
one pixel to the right of its right edge when at point 20. \ (Thus there
should be one clear pixel of white space between the images of the
pen at points 20 and 21.)

### Exercise
Now see if your knowledge of equation reading gives you the
ability to write equations that correspond to the following objectives:
\ (a) Point 13 should be just as far below the baseline as point 11 is
above the baseline. \ (b) Point 10 should be one millimeter to the right
of, and one pixel below, point 12. \ (c) Point 43 should be one-third of
the way from the top left corner of the type to the bottom right corner
of the type.

#### Answer
(a) $y_13=-y_11$ (or $-y_13=y_11$, or $y_13+y_11=0$).
\ (b) $z_10=z_12+("mm",-1)$. \ (c) $z_43={1\over3}[(0,h),(w,-d)]$.

Let's return now to the six example points $(z_1,z_2,z_3,z_4,z_5,z_6)$
that were used so often in Chapters 2 and 3. Changing the notation
slightly, we might say that the points are

>
$(x_1,y_1)=(0,h)$;&$(x_2,y_2)=(.5w,h)$;&$(x_3,y_3)=(w,h)$;
$(x_4,y_4)=(0,0)$;&$(x_5,y_5)=(.5w,0)$;&$(x_6,y_6)=(w,0)$.

There are many ways to specify these points by writing a series of
equations. For example, the six equations just given would do fine;
or the short names $z_1$ through $z_6$ could be used instead of the
long names $(x_1,y_1)$ through $(x_6,y_6)$. But there are several
other ways to specify those points and at the same time to "explain"
the relations they have to each other. One way is to define the
$x$ and $y$ coordinates separately:

>
$x_1=x_4=0; x_2=x_5=.5w; x_3=x_6=w;$
$y_1=y_2=y_3=h; y_4=y_5=y_6=0$.

METAFONT\ allows you to state several equations at once, by using more than
one equality sign; for example, '$y_1=y_2=y_3=h$' stands for three
equations, '$y_1=y_2$', '$y_2=y_3$', and '$y_3=h$'.

In order to define the coordinates of six points, it's necessary to
write twelve equations, because each equation contributes to the
definition of one value, and because six points have twelve coordinates
in all. However, an equation between pairs of coordinates counts as
two equations between single numbers; that's why we were able to get by
with only six '$=$' signs in the first set of equations, while twelve
were used in the second.

Let's look at yet another way to specify those six points, by giving
equations for their positions relative to each other:

>
$z_1-z_4=z_2-z_5=z_3-z_6$
$z_2-z_1=z_3-z_2=z_5-z_4=z_6-z_5$
$z_4="origin"$; \ $z_3=(w,h)$.

^^"origin" First we say that the vectors from $z_4$ to $z_1$,
from $z_5$ to $z_2$, and from $z_6$ to $z_3$, are equal to each other;
then we say the same thing for the vectors from $z_1$ to $z_2$,
$z_2$ to $z_3$, $z_4$ to $z_5$, and $z_5$ to $z_6$. Finally the
corner points $z_4$ and $z_3$ are given explicitly. That's a total
of seven equations between pairs of coordinates, so it should be
more than enough to define the six points of interest.

However, it turns out that those seven equations are not enough!
For example, the six points

>
$z_1=z_4=(0,0)$; \ $z_2=z_5=(.5w,.5h)$; \ $z_3=z_6=(w,h)$

also satisfy the same equations. A closer look explains why:
The two formulas

>
$z_1-z_4=z_2-z_5$ and $z_2-z_1=z_5-z_4$

actually say exactly the same thing. \ (Add $z_5-z_1$ to both sides
of the first equation and you get '$z_5-z_4=z_2-z_1$'.) \ Similarly,
$z_2-z_5=z_3-z_6$ is the same as $z_3-z_2=z_6-z_5$. Two of the
seven equations give no new information, so we really have specified
only five equations; that isn't enough. An additional relation
such as '$z_1=(0,h)$' is needed to make the solution unique.

**[Dangerous Bend]** exercise (For mathematicians.) \ Find a solution to the seven
equations such that $z_1=z_2$. Also find another solution in which
$z_1=z_6$.

#### Answer
(a) $z_1=z_2=z_3=(w,h)$; $z_4=z_5=z_6=(0,0)$.
\ (b) $z_1=z_6=(.5w,.5h)$; $z_2=(.75w,.75h)$; $z_3=(w,h)$;
$z_4=(0,0)$; $z_5=(.25w,.25h)$.

At the beginning of a METAFONT\ program, variables have no values,
except that plain METAFONT\ has assigned special values to variables
like "smoke" and "origin". Furthermore, when you begin a new
character with @beginchar@, any previous values that may have been
assigned to $x$ or $y$ variables are obliterated and forgotten.
Values are gradually established as the computer reads equations and
tries to solve them, together with any other equations that have already
appeared in the program.

It takes ten equations to define the values of ten variables.
If you have given only nine equations it may turn out that none of
the ten variables has yet been determined; for example, the
nine equations

>
$g_0=g_1=g_2=g_3=g_4=g_5=g_6=g_7=g_8=g_9$

don't tell us any of the $g$ values. However, the further equation

>
$g_0+g_1=1$

will cause METAFONT\ to deduce that all ten of the $g$'s are equal to $1\over2$.

METAFONT\ always computes the values of as many variables as possible, based
on the equations it has seen so far. For example, after the two equations

>
$a+b+2c=3$;
$a-b-2c=1$

the machine will know that $a=2$ (because the sum of these two equations is
'$2a=4$'); but all it will know about $b$ and $c$ is that $b+2c=1$.

At any point in a program a variable is said to be either ""
or "," depending on whether or not its value can be
deduced uniquely from the equations that have been stated so far.
The sample expressions in Chapter 8 indicate that METAFONT\ can compute a
variety of things with unknown variables; but sometimes a quantity
must be known before it can be used. For example, METAFONT\ can multiply
an unknown numeric or pair variable by a known numeric value, but it
cannot multiply two unknowns.

Equations can be given in any order, except that you might sometimes
need to put certain equations first in order to make critical
values known in the others. For example, METAFONT\ will find the
solution $(a,b,c)=(2,7,-3)$ to the equations '$a+b+2c=3$;
$a-b-2c=1$; $b+c=4$' if you give those equations in any other order,
like '$b+c=4$; $a-b-2c=1$; $a+b+2c=3$'. But if the equations had
been '$a+b+2c=3$; $a-b-2c=1$; $a\ast(b+c)=8$', you would not have
been able to give the last one first, because METAFONT\ would have refused
to multiply the unknown quantity $a$ by another unknown quantity $b+c$.
Here are the main things that METAFONT\ can do with unknown quantities:

>
$-*unknown*$
$*unknown*+*unknown*$
$*unknown*-*unknown*$
$*unknown*\ast*known*$
$*known*\ast*unknown*$
$*unknown*/*known*$
$*known*[*unknown*,*unknown*]$
$*unknown*[*known*,*known*]$

Some of the operations of plain METAFONT\!, defined in Appendix B, also work
with unknown quantities. For example, it's possible to say
^"top"*unknown*, ^"bot"*unknown*,
^"lft"*unknown*, ^"rt"*unknown*, and even

>
"penpos"*suffix*(*unknown*,*known*).

**[Dangerous Bend]** A METAFONT\ program can say '*unknown*$[a,b\mkern1mu]$' when $a-b$ is
known, and variable $a$ can be compared to variable $b$ in boolean
expressions like '$a<b$' when $a-b$ is known. The quantity
$a-b$ might be known even when $a$ and $b$ aren't known by themselves.

**[Dangerous Bend]** You might wonder how METAFONT\ is able to keep its knowledge up-to-date,
based on scraps of partial information that it receives from miscellaneous
equations. The best way to understand this is to watch how it happens,
by asking the computer to show certain calculations that it usually keeps
to itself. Here's one way to do it: Run METAFONT\ and say

"'

"'

^^"tracingequations" ^^"tracingonline"
in response to the opening "**''. \ (Be sure to type the backslash "\'',
and to use ":='' instead of "=''. We will see in Chapter 27 that METAFONT\
can be asked to "trace" many aspects of what it's doing.) \ Now type

"'

a+b+2c=3;

"'

the machine will reply by saying

"'

## c=-0.5b-0.5a+1.5

"'

since that is how it has digested your equation. \ (The "##'' in this
line identifies diagnostic information that comes from
"tracingequations".) \ Now type

"'

a-b-2c=1;

"'

METAFONT\ will read this as if you had said "a-b-2(-0.5b-0.5a+1.5)=1'',
since it has previously learned how to replace 'c' by an expression
that involves only 'a' and 'b'. This new equation can be simplified by
multiplying out the left-hand side and collecting terms. The result is
"2a-3=1'', hence METAFONT\ will respond with

"'

## a=2

"'

and it will be your turn to type something again. Say

"'

showdependencies;

"'

^^@showdependencies@ METAFONT's response will be

"'

c=-0.5b+0.5

"'

indicating that there is only one variable whose value depends on others,
and that its equation of dependency is now '$c=-0.5b+0.5$'. \ (The previous
dependency equation '$c=-0.5b-0.5a+1.5$' has
been simplified to take account of the newly discovered value, $a=2$.) \
Finally type

"'

b+c=4;

"'

this spurs the computer on to say

"'

## b=7
#### c=-3

"'

A line that begins with "##'' states what METAFONT\ has deduced from
the equation it has just read; a line that begins with "####'' states
an indirect consequence of that direct result,
if some previously dependent variable has now become known.

**[Dangerous Bend]** It's interesting to continue the computer experiment just begun
by typing the following lines, one at a time, and watching what happens:

"'

a'+b'+.5c'=3;
a'-b'-.5c'=1;
g0=g1=g2=g3=g4;
showdependencies;
g0+g1=1;
z1-z4=z2-z5=z3-z6;
z2-z1=z3-z2=z5-z4=z6-z5;
z4=origin;
z3=(w,h);
x1=0;
y6=0;
w=2h=100;
end.

"'

Notice that on the sixth line ('$z_1-z_4=\cdots\,$')
METAFONT\ reports four equations, but on the next line
('$z_2-z_1=\cdots\,$') it reports only two. This
happens because most of that line is redundant, as we have already
observed.

**[Dangerous Bend]** This computer session indicates that METAFONT\ deals with two kinds
of unknown numeric variables: variables and
ones.
Every variable is independent at the beginning of its life, but every
equation causes one of the independent variables to become dependent
or . Each "##'' line emitted by "tracingequations" shows a
newly dependent-or-known variable, together with an equivalent expression
that involves only independent variables. For example, the line
"##' 'c=-0.5b-0.5a+1.5''
means that variable $c$ has just become dependent and that it equals
$-{1\over2}b-{1\over2}a+1.5$, where variables $b$ and $a$ are independent.
Similarly, "##' 'a=2'' means that $a$ has just changed from
independent to known. When an independent variable $v$ changes to dependent
or known, the equivalents of all dependent variables are updated so that
they no longer depend on $v$; in this updating process some or all of them
may change from dependent to known, whereupon a "####'' line will be printed.

**[Double Dangerous Bend]** When METAFONT\ reads a numeric equation it replaces all known variables
by their numeric values and all dependent variables by their equivalents.
The resulting equation can be converted into the form

>
$c_1v_1+\cdots+c_mv_m=\alpha$

where the $c$'s are nonzero constants and the $v$'s are independent variables;
$\alpha$ is a numeric constant that might be zero. If some $c_k$ is so
small that it probably would have been zero in a calculation free of
rounding errors, it is replaced by zero and the corresponding $v_k$ is
removed from the equation. Now if $m=0$, the equation is considered to be
either (if $\alpha$ is zero or extremely small)
or (otherwise). But if $m>0$, METAFONT\ chooses an
independent variable $v_k$ for which $c_k$ is maximum, and rewrites
the equation in the form

>
{\#\#} $v_k=(\alpha-c_1v_1-\cdots-c_k-1v_k-1-c_k+1v_k+1-
\cdots-c_mv_m)/c_k$.

Variable $v_k$ becomes dependent (if $m>1$) or known (if $m=1$).

**[Dangerous Bend]** Inconsistent equations are equations that have no solutions.
For example, if you say '$0=1$', METAFONT\ will issue an error message

saying that the equation is "off by 1." A less blatant inconsistency
arises if you say, e.g., '$a=b+1$; $b=c+1$; $c=a+1$'; this last equation
is off by three, for the former equations imply that $c=b-1=a-2$.
The computer will simply ignore an inconsistent equation when you
resume processing after such an error.

**[Dangerous Bend]** Redundant equations are equations that say nothing new.
For example, '$0=0$' is redundant, and so is '$a=b+c$' if you have
previously said that $c=a-b$. METAFONT\ stops with an error message if
you give it a redundant equation between two numeric expressions,
because this usually indicates an oversight in the program. However,
no error is reported when an equation between pairs leads to one or
two redundant equations between numerics. For example, the equation
'$z_3=(0,h)$' will not trigger an error message when the program
has previously established that $x_3=0$ or that $y_3=h$ or both.

**[Dangerous Bend]** Sometimes you might have to work a little bit to put an equation
into a form that METAFONT\ can handle. For example, you can't say

>
$x/y=2$

when $y$ is independent or dependent, because METAFONT\ allows
only by known quantities. The alternative

>
$x=2y$

says the same thing and causes the computer no difficulties;
furthermore it is a correct equation even when $y=0$.

**[Double Dangerous Bend]** METAFONT's ability to remember previous equations is limited to
"linear" dependencies as explained above.
A mathematician might want to introduce the condition $x\ge0$ by giving an
equation such as '$x=\mathopabsx$'; but METAFONT\ is incapable
of dealing with such a constraint. Similarly, METAFONT\ can't cope with
an equation like '$x=\mathopfloorx$', which states that
$x$ is an integer. Systems of equations that involve the ^absolute
value and/or operation can be extremely difficult to solve,
and METAFONT\ doesn't pretend to be a mathematical genius.

**[Double Dangerous Bend]** The rules given earlier explain how an independent variable
can become dependent or known; conversely, it's possible for a
dependent variable to become independent again, in unusual circumstances.
For example, suppose that the equation $a+b+2c=3$ in our example above
had been followed by the equation $d=b+c+a/4$. Then there would be
two dependent variables,

"'

## c=-0.5b-0.5a+1.5
## d=0.5b-0.25a+1.5

"'

Now suppose that the next statement is "numeric' 'a'', meaning that the
old value of variable $a$ should be discarded. METAFONT\ can't simply delete
an independent variable that has things depending on it, so it
chooses a dependent variable to take $a$'s place; the computer prints out

"'

### 0.5a=-c-0.5b+1.5

"'

meaning that $0.5a$ will be replaced by $-c-{1\over2}b
+{3\over2}$ in all dependencies, before $a$ is discarded. Variable $c$ is
now independent again; '^@showdependencies@' will reveal that the only
dependent variable is now $d$, which equals $0.5c+0.75b+0.75$. \ (This
is correct, for if the variable $a$ is eliminated from the two given
equations we obtain $4d=3b+2c+3$.) \ The variable chosen for independence
is one that has the greatest coefficient of dependency with respect
to the variable that will disappear.

**[Dangerous Bend]** A designer often wants to stipulate that a certain point lies on
a certain line. This can be done easily by
using a special feature of plain METAFONT\ called '^"whatever"', which
stands for an anonymous numeric variable that has a different unknown
value each time you use it. For example,

>
$z_1="whatever"[z_2,z_3]$

states that point 1 appears somewhere on the straight line that passes
through points 2 and 3. \ (The expression $t[z_2,z_3]$ represents that
entire straight line, as $t$ runs through all values from $-\infty$ to
$+\infty$. We want $z_1$ to be equal to $t[z_2,z_3]$ for some value of $t$,
but we don't care what value it is.) \ The expression '"whatever"$[z_2,z_3]$'
is legal whenever the difference $z_2-z_3$ is known; it's usually used
only when $z_2$ and $z_3$ are both known, i.e., when both points have been
determined by prior equations.

**[Dangerous Bend]** Here are a few more examples of equations that involve
'"whatever"', together with their translations into English. These
equations are more fun than the "tame" ones we considered at the
beginning of this chapter, because they show off more of the
computer's amazing ability to deduce explicit values from implicit
statements.

={\indent$z_7-z_6="whatever"\ast(z_3-z_2)$}
\longesteq=
to\longesteq{\indent Equation}
*Translation*

\\$z_5-z_4="whatever"\ast\mathopdir30$\\
The angle between points 4 and 5 will be $30^\circ$ above the horizon.
\ (This equation can also be written '$z_4=z_5+"whatever"\ast\mathopdir30$', which states that point 4 is obtained by starting at point 5
and moving by some unspecified multiple of $\,30$.)

\\$z_7-z_6="whatever"\ast(z_3-z_2)$\\
The line from point 6 to point 7 should be to the
line from point 2 to point 3.

\\$\penpos8("whatever",60)$\\
The simulated pen angle at point 8 should be 60 degrees; the breadth
of the pen is unspecified, so it will be determined by other equations.

**[Dangerous Bend]** exercise If $z_1$, $z_2$, $z_3$, and $z_4$ are known points,
how can you tell METAFONT\ to compute the point $z$ that lies on the
of the lines $z_1\to z_2$ and $z_3\to z_4$?

#### Answer
$z="whatever"[z_1,z_2]$; $z="whatever"[z_3,z_4]$. \ (Incidentally,
it's interesting to watch this computation in action. Run METAFONT\ with
'\tracingequations:='\allowbreak'tracingonline:=1' and say, for example,

"'

z=whatever[(1,5),(8,19)]; z=whatever[(0,17),(6,1)];

"'

the solution appears as if by magic.
If you use 'alpha' and 'beta' in place of the whatevers, the machine will
also calculate values for "alpha" and "beta".)

**[Dangerous Bend]** exercise Given five points $z_1$, $z_2$, $z_3$, $z_4$, and $z_5$,
explain how to compute $z$ on the line $z_1\to z_2$ such that the line
$z\to z_3$ is parallel to the line $z_4\to z_5$.

#### Answer
$z="whatever"[z_1,z_2]$; $z-z_3="whatever"\ast(z_5-z_4)$.

**[Dangerous Bend]** exercise What METAFONT\ equation says that the line between points
11 and 12 is to the line between points 13 and 14?

#### Answer
$z_11-z_12="whatever"\ast(z_13-z_14)$ 90,
assuming that $z_13-z_14$ is known. \ (It's also possible to say
'$(z_11-z_12)\mathbindotprod (z_13-z_14)=0$',
although this risks overflow if the coordinates are large.)

**[Dangerous Bend]** exercise (For mathematicians.) \ Given three points $z_1$, $z_2$,
and $z_3$, explain how to compute the distance from $z_1$ to the straight
line through $z_2$ and $z_3$.

#### Answer
One solution constructs the point $z_4$ on $z_2\to z_3$ such
that $z_4\to z_1$ is perpendicular to $z_2\to z_3$, using ideas like
those in the previous two exercises: '$z_4="whatever"[z_2,z_3]$;
$z_4-z_1="whatever"\ast(z_3-z_2)$ rotated 90'. Then the requested distance

is $length(z_4-z_1)$. But there's a slicker solution: Just calculate
$${abs ypart$((z_1-z_2)\mathbinrotated-angle(z_3-z_2))$.}$$

**[Double Dangerous Bend]** exercise (For mathematicians.) \ Given three points $z_1$,
$z_2$, $z_3$, and a length $l$, explain how to compute the two points
on the line $z_2\to z_3$ that are at distance $l$ from $z_1$. \ (Assume
that $l$ is greater than the distance from $z_1$ to the line.)

#### Answer
It would be nice to say simply '$z="whatever"[z_2,z_3]$' and
then to be able to say either 'length$(z-z_1)=l$' or '$z-z_1=(l,0)$
rotated "whatever"'; but neither of the second equations is legal. \
(Indeed, there couldn't possibly be a legal solution that has this general
flavor, because any such solution would determine a unique $z$, while
there are two points to be determined.) \ The best way seems to be to
compute $z_4$ as in the previous exercise, and
then to let
$v=(l\mathbin+-+\mathoplength (z_4-z_1))\ast\mathopunitvector(z_3-z_2)$;
the desired points are then $z_4+v$ and $z_4-v$.

**[Double Dangerous Bend]** exercise The applications of "whatever" that we have seen so far
have been in equations between *pairs* of numeric values, not
in equations between simple numerics. Explain why an equation like
'$a+2b="whatever"$' would be useless.

#### Answer
Such an equation tells us nothing new about $a$ or $b$. Indeed,
each use of "whatever" introduces a new independent variable, and
each new independent variable "uses up" one equation, since we need
$n$ equations to determine the values of $n$ unknowns. On the other hand
an equation between pairs counts as two equations; so there's a net
gain of one, when "whatever" appears in an equation between pairs.

**[Dangerous Bend]** All of the equations so far in this chapter have been between numeric
expressions or pair expressions. But METAFONT\ actually allows equations
between any of the eight types of quantities. For example, you can write

"'

s1="go"; s1&s1=s2

"'

if $s_1$ and $s_2$ are string variables; this makes $s_1=$'"go"'
and $s_2=$'"gogo"'. Moreover, the subsequent equations

"'

s3=s4; s5=s6; s3=s5; s4=s1&"sh"

"'

will make it possible for the machine to deduce that $s_6=$'"gosh"'.

**[Dangerous Bend]** But nonnumeric equations are not as versatile as numeric
ones, because METAFONT\ does not perform operations on unknown quantities

of other types. For example, the equation

"'

"h"&s7="heck"

"'

cannot be used to define $s_7=$'"eck"', because the
operator '&' works only with strings that are already known.

**[Double Dangerous Bend]** After the declaration "string' 's[]'' and the equations
"s1=s2=s3'', the statement "show' 's0'' will produce the result
"unknown' 'string' 's0''; but "show' 's1'' will produce "unknown'
'string' 's2''. Similarly, "show' 's2'' and "show' 's3'' will produce
"unknown' 'string' 's3'' and "unknown' 'string' 's1'', respectively. In
general, when several nonnumeric variables have been equated, they will
point to each other in some cyclic order.

\endchapter

Let "X" equal my father's signature.

> --- FRED , *Vogues* (1924)

ALL ANIMALS ARE EQUAL
BUT SOME ANIMALS ARE MORE EQUAL THAN OTHERS

> --- GEORGE , *Animal Farm* (1945)


# Chapter 10. Assignments

Variables usually get values by appearing in equations, as described in
the preceding chapter. But there's also another way, in which ''
is used instead of "=''. For example, the 'io.mf' program in Chapter 5
said

"'

stem# := trial_stem * pt#

"'

when it wanted to define the value of 'stem#'.

The operator ":='' means "discard the previous value of
the variable and assign a new one"; we call this an
operation. It was convenient for 'io.mf' to define 'stem#' with an
assignment instead of an equation, because 'stem#' was getting several
different values within a single font. The alternative would have been to say

"'

numeric stem#; stem# = trial_stem * pt#

"'

(thereby specifically undefining the previous value of 'stem#' before using
it in an equation); this is more cumbersome.

The variable at the left of ":='' might appear also in the expression on
the right. For example,

"'

code := code + 1

"'

means "increase the value of "code" by 1." This assignment would make no
sense as an equation, since '$"code"="code"+1$' is inconsistent. The former
value of "code" is still relevant on the right-hand side when '$"code"+1$'
is evaluated in this example, because old values are not discarded until
the last minute; they are retained until just before a new assignment is made.

**[Dangerous Bend]** exercise Is it possible to achieve the effect of '$"code":="code"+1$'
by using equations and @numeric@ declarations but not assignments?

#### Answer
Yes, but it must be done in two steps: '@numeric@ "newcode";
$"newcode"="code"+1$; @numeric@ "code"; $"code"="newcode"$'.

Assignments are permitted only when the quantity at the left of the ":=''
is a variable. For example, you can't say "code+1:=code''. More
significantly, things like "(x,y):=(0,0)'' are not permitted, although
you can say "w:=(0,0)'' if $w$ has been declared to be a variable of
type @pair@. This means that a statement like "z1:=z2'' is illegal, because
it's an abbreviation for the inadmissible construction "(x1,y1):=(x2,y2)'';
we must remember that 'z1' is not really a variable, it's a pair of variables.

The restriction in the previous paragraph is not terribly significant, because
assignments play a relatively minor r\^ole in METAFONT\ programs. The best
programming strategy is usually to specify equations instead of
assignments, because equations indicate the relationships between
variables in a declarative ^^imperative
versus declarative manner. A person who makes too many assignments is
still locked into the habits of old-style "imperative" programming
languages in which it is necessary to tell the computer exactly how to do
everything; METAFONT's equation
mechanism liberates us from that more complicated style of programming,
because it lets the computer take over the job of solving equations.

The use of assignments often imposes a definite order on the statements of
a program, because the value of a variable is different before and after
an assignment takes place. Equations are simpler than assignments because
they can usually be written down in any order that comes naturally to you.

Assignments do have their uses; otherwise METAFONT\ wouldn't bother with
":='' at all. But experienced METAFONT\ programmers introduce assignments
sparingly---only when there's a good reason for doing so---because
equations are generally easier to write and more enlightening to read.

**[Dangerous Bend]** METAFONT's like "tracingequations" always have
known numeric values, so there's no way to change them except by giving
assignments. The computer experiment in Chapter 9 began with

"'

"'

this illustrates the fact that multiple assignments are possible, just
like multiple equations. Here is the complete syntax for equations
and assignments:
\beginsyntax
<equation>\is<expression>[=]<right-hand side>
<assignment>\is<variable>[:=]<right-hand side>
<right-hand side>\is<expression>\alt<equation>\alt<assignment>
\endsyntax
Notice that the syntax permits mixtures like '$a+b=c:=d+e$'; this is
the same as the assignment '$c:=d+e$' and the equation '$a+b=c$'.

**[Double Dangerous Bend]** In a mixed equation/assignment like '$a+b=b:=b+1$', the old
value of $b$ is used to evaluate the expressions. For example, if $b$ equals 3
before that statement, the result will be the same as '$a+3=b:=3+1$';
therefore $b$ will be set to 4 and $a$ will be set to 1.

**[Dangerous Bend]** exercise Suppose that you want variable $x_3$ to become "like new,"

completely independent of any value that it formerly had; but you don't
want to destroy the values of $x_1$ and $x_2$. You can't say '^@numeric@
$x[\,]$', because that would obliterate all the $x_k$'s. What can you do
instead? \checkequals\xwhat\exno

#### Answer
The assignment '$x_3:=$^"whatever"' does exactly what you want.

**[Double Dangerous Bend]** exercise Apply METAFONT\ to the short program

>
@string@ $s[\,]$; \ $s_1=s_2=s_3=s_4$; \ $s_5=s_6$; \ $s_2:=s_5$; \
@showvariable@ $s$;

and explain the results you get.

#### Answer
The result shows that $s_1=s_3=s_4$ and $s_2=s_5=s_6$ now:

"'

s[]=unknown string
s1=unknown string s3
s2=unknown string s6
s3=unknown string s4
s4=unknown string s1
s5=unknown string s2
s6=unknown string s5

"'

(The assignment $s_2:=s_5$ broke $s_2$'s former relationship with $s_1$,
$s_3$, and $s_4$.)

**[Double Dangerous Bend]** If other variables depend on $v$ when $v$ is assigned a new value,
the other variables do not change to reflect the new assignment; they still
act as if they depended on the previous (unknown) value of $v$. For example,
if the equations '$2u=3v=w$' are followed by the assignment '$w:=6$', the
values of $u$ and $v$ won't become known, but METAFONT\ will still remember the
fact that $v=.66667u$. \ (This is not a new rule; it's a consequence of
the rules already stated. When an independent variable is discarded, a
dependent variable may become independent in its place, as described in
Chapter 9.)

**[Double Dangerous Bend]** exercise Apply METAFONT\ to the program

>
$"tracingequations":="tracingonline":=1$;
$a=1$; \ $a:=a+b$; \ $a:=a+b$; \ $a:=a+b$;
@show@ $a,b$;

and explain the results you get.

#### Answer
The results are

>
'## a=1'
'## a=b+1'&(after the first assignment)
'## b=0.5a-0.5'&(after the second assignment)
|### -1.5a=-
|## a=
'>> a'&(after '@show@'; variable $a$ is independent)
'>> 0.33333a-0.33333'&(this is the final value of $b$)

Let $a_k$ denote the value of $a$ after $k$ assignments were made.
Thus, $a_0=1$, and $a_1$ was dependent on the independent variable $b$.
Then $a_1$ was discarded and $b$ became dependent on the independent
variable $a_2$. The right-hand side of the third assignment was
therefore $a_2+b$. At the time $a_2$ was about to be discarded, METAFONT\
had two dependencies $b=0.5a_2-0.5$ and $\kappa=1.5a_2-0.5$, where
$\kappa$ was a nameless "" inside of the computer, representing
the new value to be assigned. Since $\kappa$ had a higher coefficient
of dependency than $b$, METAFONT\ chose to make $\kappa$ an independent variable,
after which $-1.5a_2$ was replaced by $-\kappa-0.5$ in all dependencies; hence
$b$ was equal to $0.33333\kappa-0.33333$. After the third
assignment was finished, $\kappa$ disappeared and $a_3$ became independent
in its place. \ (The line "##' |a=
temporarily dependent on $\kappa$, before $\kappa$ was discarded. If
the equation $a=\kappa$ had happened to make $\kappa$ dependent on $a$, rather
than vice versa, no "##'' line would have been printed;
such lines are omitted when a capsule or part of a capsule has been made
dependent, unless you have made ^"tracingcapsules"$>0$.)

\endchapter

At first his assignment had pleased,
but as hour after hour passed
with growing weariness,
he chafed more and more.

> --- C. E. , *Hopalong Cassidy* (1910)

*left part* ::= *variable* :=
*left part list* ::= *left part* $\vert$ *left part list**left part*
*assignment statement* ::= *left part list**arithmetic expression* $\vert$
*left part list**Boolean expression*
or PETER et al., *Report
on the Algorithmic language ALGOL 60* (1960)


# Chapter 11. Magnification and Resolution

A single METAFONT\ program can produce fonts of type for many different kinds
of printing equipment, if the programmer has set things up so that the
can be varied. The "plain METAFONT" base file described
in Appendix B establishes a set of conventions that make such variability
quite simple; the purpose of the present chapter is to explain those
conventions.

For concreteness let's assume that our computer has two output devices.
One of them, called ^"cheapo", has a resolution of 200 pixels per
inch (approximately 8 per millimeter); the other, called ^"luxo",
has a resolution of 2000 pixels per inch. We would like to write METAFONT\
programs that are able to produce fonts for both devices. For example,
if the file 'newface.mf' contains a program for a new typeface, we'd
like to generate a low-resolution font by invoking METAFONT\ with

"'

\mode=cheapo; input newface

"'

and the same file should also produce a high-resolution font if we start with

"'

\mode=luxo; input newface

"'

instead. Other people with different printing equipment should also be
able to use 'newface.mf' with their own favorite ^"mode" values.

The way to do this with plain METAFONT\ is to call ^@mode\_setup@ near the
beginning of 'newface.mf'; this routine establishes the values of
variables like ^"pt" and ^"mm", which represent the respective numbers of
pixels in a point and a millimeter. For example, when $"mode"= "cheapo"$,
the values will be $"pt"=2.7674$ and $"mm"=7.87402$; when $"mode"="luxo"$,
they will be $"pt"=27.674$ and $"mm"=78.74017$. The 'newface.mf' program
should be written in terms of such variables, so that the pixel patterns
for characters will be about 10 times narrower and 10 times shorter in
"cheapo" mode than they are in "luxo" mode. For example, a line that's
drawn from $(0,0)$ to $(3"mm",0)$ will produce a line that's about 23.6
pixels long in "cheapo" mode, and about 236.2 pixels long in "luxo" mode;
the former line will appear to be 3 mm long when printed by
"cheapo", while the latter will look 3 mm long when printed by
"luxo".

A further complication occurs when a typeface is being ; in such
cases the font does not correspond to its normal size. For example, we might
want to have a set of fonts for "cheapo" that are twice as big as usual,
so that users can make transparencies for overhead projectors. \ (Such
output could also be reduced to 50\% of its size as printed,
on suitable reproduction equipment, thereby increasing the effective
resolution from 200 to 400.) \ TeX\ allows entire jobs to be magnified
by a factor of 2 if the user says "=2000''; individual
fonts can also be magnified in a TeX\ job by saying, e.g.,
"\font\f=newface' 'scaled' '2000''. The standard way to produce a font
with two-fold magnification using the conventions of plain METAFONT\ is to say, e.g.,

"'

\mode=cheapo; mag=2; input newface;

"'

this will make $"pt"=5.5348$ and $"mm"=15.74803$.

The @mode\_setup@ routine looks to see if ^"mag" has a known value;
if not, it sets $"mag"=1$. Similarly, if "mode" is unknown,
^^"proof" @mode\_setup@ sets $"mode"="proof"$.

Plain METAFONT\ also computes the values of several other dimension-oriented
values in addition to "pt" and "mm", corresponding to the dimensions
that are understood by TeX. Here is the complete list:

> \openup 1pt
"pt"&printer's point&($72.27\,pt=1\,in$)
^"pc"&pica&($1\,pc=12\,pt$)
^"in"&inch&($1\,in=2.54\,cm$)
^"bp"&big point&($72\,bp=1\,in$)
^"cm"&centimeter&($100\,cm=1\,meter$)
"mm"&millimeter&($10\,mm=1\,cm$)
^"dd"&didot point&($1157\,dd=1238\,pt$)
^"cc"&cicero&($1\,cc=12\,dd$)

In each case the values are rounded to the nearest $1\over65536$th of a pixel.

Although such standard physical are available, they haven't
been used very much in traditional typefaces; designers usually specify
other units like '"em"' or '"x\_height"' in order to define the sizes
of letters, and such quantities generally have ad hoc values that vary
from font to font. Plain METAFONT\ makes it easy to introduce ^ad hoc
dimensions that will vary with the resolution and the magnification just
as "pt" and "mm" do; all you have to do is define ""
dimensions that have the same name as your pixel-oriented dimensions, but
with "#'' tacked on as a suffix. For example, $"em"\0$ and
$"x\_height"\0$ (typed "em#'' and "x_height#'') would be the
corresponding to "em" and "x\_height". Plain METAFONT\ has
already defined the quantities $"pt"\0$, $"pc"\0$, $"in"\0$, $"bp"\0$,
$"cm"\0$, $"mm"\0$, $"dd"\0$, and $"cc"\0$ for the standard units named above.

Sharped dimensions like $"em"\0$ and $"x\_height"\0$ should always be
defined in terms of resolution-independent dimension variables like $"pt"\0$,
$"in"\0$, etc., so that their values do not change in any way when "mode"
and "mag" are varied. The "#'' sign implies unchangeability.
After @mode\_setup@ has been called,
the pixel-oriented dimensions can be calculated by simply saying

>
^@define\_pixels@("em", "x\_height").

This statement is an abbreviation for

>
$"em":="em"\0\ast"hppp"$;&$"x\_height":="x\_height"\0\ast"hppp"$

where ^"hppp" is an internal variable of METAFONT\ that represents the number
of pixels per point in the horizontal dimension. Any number of ad hoc
dimensions can be listed in a single @define\_pixels@ statement.
Notice that '\#' is not an operator that could convert "em" to $"em"\0$;
rounding errors would be mode-dependent.

Chapter 5's demonstration program 'io.mf' contains several examples of ad hoc
dimensions defined in this way, and it also contains the statement

>
^@define\_blacker\_pixels@("thin", "thick");

what's this? Well, Appendix B makes that statement an abbreviation for

>
$"thin":="thin"\0\ast"hppp"+"blacker"$;&
$"thick":="thick"\0\ast"hppp"+"blacker"$;

in other words, the sharped dimensions are being unsharped in this case
by converting them to pixels and then adding '"blacker"'. The variable
^"blacker" is a special correction intended to help adapt a font to the
idiosyncrasies of the current output device; @mode\_setup@ uses the value
of "mode" to establish the value of "blacker". For example, "cheapo" mode
might want $"blacker"=0.65$, while "luxo" mode might give best results
when $"blacker"=0.1$. The general convention is to add "blacker" to
pixel-oriented variables that determine the breadth of pens and the
thickness of stems, so that the letters will be slightly darker on machines
that otherwise would make them appear too light. Different machines treat
pixels quite differently, because they are often based on quite different
physical principles. For example, the author once worked with an extremely
high-resolution device that tended to shrink stem lines rather drastically
when it used a certain type of photographic paper, and it was necessary
to set $"blacker"=4$ to get proper results on that machine; another
high-resolution device seems to want "blacker" to be only $0.2$. Experimentation
is necessary to tune METAFONT's output to particular devices, but the author's
experience suggests strongly that such a correction is worthwhile. When
^^"proof" $"mode"="proof"$ or ^"smoke", the value of "blacker" is taken to
be zero, since the output in these modes is presumably undistorted.

### Exercise
Does '$"mode"="cheapo"$; $"mag"=10$' produce exactly the same
font as '$"mode"="luxo"$', under the assumptions of this chapter?

#### Answer
Almost, but not quite. The values of standard dimension variables
like "pt" and "mm" will be identical in both setups, as will the values of
ad hoc dimension variables like "em" and "x\_height". But pen-oriented
dimensions that are defined via @define\_blacker\_pixels@ will be slightly
different, because "cheapo" mode has $"blacker"=0.65$ while "luxo" mode
has $"blacker"=0.1$ (since the "luxo" printer has different physical
characteristics). Similarly, @define\_corrected\_pixels@ (which we are
just about to discuss) will produce slightly different results in the two
given modes.

**[Dangerous Bend]** Line 7 of 'io.mf' says '^@define\_corrected\_pixels@($o$)', and
this is yet a third way of converting from true physical dimensions to
pixel-oriented values. According to Appendix B, variable $o$ is
defined by the assignment

>
$o:=\round(o\0\ast"hppp"\ast"o\_correction")+"eps"$

^^"eps" ^^"o"
where ^"o\_correction", like "blacker", is a magic number that depends on
the output device for which fonts are being made. On a high-resolution
device like "luxo", the appropriate value for the "o\_correction" factor
is 1; but on a low-resolution device like "cheapo", the author has obtained
more satisfactory results with $"o\_correction"=0.4$. The reason is that
'$o$' is used to specify the number of pixels by which certain features
of characters "" the baseline or some other line to which
they are visually related. High-resolution curves look better when they
overshoot in this way, but low-resolution curves do not; therefore it is
usually wise to curtail the amount of overshoot by applying the
"o\_correction" factor. In "proof" and "smoke" modes the factor is
equal to 1.0, since these modes correspond to high resolution.

**[Double Dangerous Bend]** The properties of output devices are modeled also by a
parameter that's called ^"fillin", which represents the amount by which
diagonal strokes tend to be darker than horizontal or vertical strokes.
More precisely, let us say that a "" pixel is one whose color
matches the color of five of its neighbors but not the other three, where the
three exceptions include one horizontal neighbor, one vertical neighbor,
and the diagonal neighbor between them. If a white corner pixel has
apparent darkness $f_1$ and if a black corner pixel has apparent darkness
$1-f_2$, then the "fillin" is $f_1-f_2$. \ (A "true" raster image would
have $f_1=f_2=0$, but physical properties often cause pixels to influence
their neighbors.)

**[Double Dangerous Bend]** Each output device for which you will be generating fonts should
be represented by a symbolic ^"mode" name in the implementation of METAFONT\
that you are using. Since these mode names vary from place to place, they
are not standard aspects of the METAFONT\ language; for example, it is doubtful
whether the hypothetical "cheapo" and "luxo" modes discussed in this
chapter actually exist anywhere. The plain METAFONT\ base is intended to be
extended to additional modes in a disciplined way, as described at the
end of Appendix B.

**[Double Dangerous Bend]** It's easy to create a new symbolic mode, using plain METAFONT's
'^@mode\_def@' convention. For example, the "luxo" mode we have been
talking about could be defined by saying

>
@mode\_def@ "luxo" $=$
$"pixels\_per\_inch":=2000$;&\% high res, almost 30 per point
$"blacker":=.1$;&\% make pens a teeny bit blacker
$"o\_correction":=1$;&\% keep the full overshoot
$"fillin":=0.1$;&\% compensate for darkened corners
$"proofing":=0$;&\% no, we're not making proofs
$"fontmaking":=1$;&\% yes, we are making a font
$"tracingtitles":=1$; \ @enddef@;&\% yes, show titles online

The name of the mode should be a single symbolic token. The resolution
should be specified by assigning a value to "pixels\_per\_inch"; all other
dimension values ("pt", "mm", etc.)\ will be computed from this one by
@mode\_setup@. A mode definition should also assign values to the
internal variables "blacker", "o\_correction", and "fillin" (which describe
the device characteristics), as well as ^"proofing", ^"fontmaking", and
^"tracingtitles" (which affect the amount of output that will be produced).
In general, "proofing" and "fontmaking" are usually
set to 0 and 1, respectively, in modes that are intended for font
production rather than initial font design; "tracingtitles" is usually
0 for low-resolution fonts (which are generated quickly), but 1 for
high-resolution fonts (which go more slowly), because detailed online
progress reports are desirable when comparatively long jobs are running.

**[Double Dangerous Bend]** Besides the seven mandatory quantities '"pixels\_per\_inch"',
\dots, '"tracingtitles"' just discussed, a mode definition might assign
a value to '^"aspect\_ratio"'. In the normal case when no
"aspect\_ratio" is specified, it means that the fonts to be output
are assumed to have square pixels. But if, for
example, the @mode\_def@ sets $"aspect\_ratio":=5/4$,
it means that the output pixels
are assumed to be in the ratio of 5 to 4; i.e.,
5 vertical pixel units are equal to 4 horizontal pixel units. The
pixel-oriented dimensions of plain METAFONT\ are given in terms of horizontal
pixel units, so an aspect ratio of 5/4 together with 2000 pixels per inch
would mean that there are 2500 vertical pixel units per inch; a square
inch would consist of 2500 rows of pixels, with 2000 pixels in each row. \
(Stating this another way, each pixel would be $1\over2000$ inches wide and
$1\over2500$ inches high.) \ In such a case, plain METAFONT\ will set the
^"currenttransform" variable so that all @draw@ and @fill@ commands
stretch the curves by a factor of 5/4 in the vertical dimension; this
compensates for the nonsquare pixels, so the typeface designer doesn't have to
be aware of the fact that pixels aren't square.

Let's look now at a concrete example, so that it will be clear how the
ideas of device-independent font design can be implemented in practice.
We shall study a file 'logo.mf' that generates the seven letters of
METAFONT's . There also are "" files 'logo10.mf', 'logo9.mf',
etc., which use 'logo.mf' to produce fonts in various sizes. For
example, a font containing the 10-point characters 'METAFONT'
could be generated for the hypothetical "luxo" printer by running METAFONT\ with
the command line

"'

\mode=luxo; input logo10

"'

if "luxo" mode really existed.

The main purpose of 'logo10.mf' is to establish the "sharped" values of
several ad hoc dimensions; then it inputs 'logo.mf', which does the
rest of the work. Here is the entire file 'logo10.mf':

"'

font_size 10pt#;
ht#:=6pt#;
xgap#:=0.6pt#;
u#:=4/9pt#;
s#:=0;
o#:=1/9pt#;
px#:=2/3pt#;
input logo
end

"'

Similar files 'logo9.mf' and 'logo8.mf' will produce 9-point
'{\manual hijklmnj}' and 8-point
'{\manual opqrstuq}'; the letters get a little
wider in relation to their height, and the intercharacter spacing
gets significantly wider, as the size gets smaller:

"'

font_size 9pt#; font_size 8pt#;
ht#:=.9*6pt#; ht#:=.8*6pt#;
xgap#:=.9*0.6pt#; xgap#:=.8*0.6pt#;
u#:=.91*4/9pt#; u#:=.82*4/9pt#;
s#:=.08pt#; s#:=.2pt#;
o#:=1/10pt#; o#:=1/12pt#;
px#:=.9*2/3pt#; px#:=.8*2/3pt#;
input logo input logo
end end

"'

It is interesting to compare the font generated by 'logo10.mf' to the
font generated by 'logo8.mf' with 'mag=10/8': Both fonts will have
the same values of "ht", "xgap", and "px", when the magnification has been
taken into account. But the magnified 8-point font has a slightly larger
value of "u" and a positive value of "s"; this changes
'METAFONT' to '{\manual/0123451}'.

**[Dangerous Bend]** Every font has a "," which is a more-or-less
arbitrary number that reflects the size of type it is intended to blend
with. Users of TeX\ select magnified fonts in two ways, either
by specifying an "at size" or by specifying a scale factor (times 1000).
For example, the 8-point METAFONT\ logo can be used at 10/8 magnification by
referring either to "logo8' 'at' '10pt'' or to "logo8' 'scaled' '1250''
in a TeX\ document. When an "" is specified, the amount of
magnification is the stated size divided by the design size. A typeface
designer can specify the design size by using plain METAFONT's '^@font\_size@'
command as illustrated on the previous page. \ (If no design size is
specified, METAFONT\ will set it to $128\pt$, by default.)

The file 'logo.mf' itself begins by defining three more ad hoc dimensions
in terms of the parameters that were set by the parameter file; these
dimensions will be used in several of the programs for individual letters.
Then 'logo.mf' makes the conversion to pixel units:

"'

mode_setup;
ygap#:=(ht#/13.5u#)*xgap#;
leftstemloc#:=2.5u#+s#;
barheight#:=.45ht#;
define_pixels(s,u,xgap,ygap,leftstemloc,barheight);
py#:=.9px#; define_blacker_pixels(px,py);
pickup pencircle xscaled px yscaled py; logo_pen:=savepen;
define_corrected_pixels(o);

"'

There's nothing new here except the use of '^"savepen"' in the
second-last line; this, as we will see in Chapter 16, makes the
currently-picked-up pen available for repeated use in the
subsequent program.

After the initial definitions just shown, 'logo.mf' continues with
programs for each of the seven letters. For example,
here is the program for '{\manual }', which illustrates the
\rightfig 11a ({224\apspix} x {216\apspix}) ^-11pt
use of $u\0$, $s\0$, $"ht"\0$, "logo\_pen", "leftstemloc", $o$,
"xgap", and "barheight":

"'

beginchar("E",14u#+2s#,ht#,0);
pickup logo_pen;
x1=x2=x3=leftstemloc;
x4=x6=w-x1+o; x5=x4-xgap;
y1=y6; y2=y5; y3=y4;
bot y1=0; top y3=h;
y2=barheight;
draw z6--z1--z3--z4; draw z2--z5;
labels(1,2,3,4,5,6);
endchar;

"'

We have seen the essentials of the {\manual M} and the {\manual T} in
Chapter 4; programs for the other letters will appear later.

### Exercise
The ad hoc dimensions $"ht"\0$, $"xgap"\0$, $u\0$, $s\0$,
$o\0$, and $"px"\0$ defined in the parameter files all affect the letter
'{\manual E}' defined by this program. For each of these dimensions,
tell what would happen to the '{\manual E}' if that dimension were
increased slightly while all the others stayed the same.

#### Answer
Increasing $"ht"\0$ would make the letter shape and the bounding
box taller; increasing $"xgap"\0$ would move point 5 to the left, thereby
making the middle bar shorter; increasing $u\0$ would make the shape and
its bounding box wider; increasing $s\0$ would widen the bounding box
at both sides without changing the letter shape; increasing $o\0$ would
move points 4, 5, and 6 to the right; increasing $"px"\0$ would make
the pen thicker (preserving the top edge of the upper bar, the bottom
edge of the lower bar, and the center of the middle bar and the stem).

**[Dangerous Bend]** exercise Guess the program for '{\manual l}' (which is
almost the same as '{\manual i}').

#### Answer
The only possible surprise is the position of $y_1$,
which should match similar details in the '{\manual h}'
and the '{\manual j}' of Chapter 4:

"'

beginchar("F",14*u#+2s#,ht#,0); pickup logo_pen;
x1=x2=x3=leftstemloc; x4=w-x1+o; x5=x4-xgap;
y2=y5; y3=y4; bot y1=-o; top y3=h; y2=barheight;
draw z1--z3--z4; draw z2--z5;
labels(1,2,3,4,5); endchar;

"'

**[Dangerous Bend]** exercise Write the complete programs for '{\manual h}'
and '{\manual j}', based on the information in Chapter 4,
but using the style of the program for '{\manual i}' above. The character
widths should be $18u\0+2s\0$ and $13u\0+2s\0$, respectively.
\checkequals\metaT\exno

#### Answer
The quantity called "ss" in Chapter 4 is now "leftstemloc".

"'

beginchar("M",18*u#+2s#,ht#,0); pickup logo_pen;
x1=x2=leftstemloc; x4=x5=w-x1; x3=w-x3;
y1=y5; y2=y4; bot y1=-o; top y2=h+o; y3=y1+ygap;
draw z1--z2--z3--z4--z5;
labels(1,2,3,4,5); endchar;|smallskip
beginchar("T",13*u#+2s#,ht#,0); pickup logo_pen;
lft x1=0; x2=w-x1; x3=x4=.5w;
y1=y2=y3; top y1=h; bot y4=-o;
draw z1--z2; draw z3--z4;
labels(1,2,3,4); endchar;

"'

**[Dangerous Bend]** The file 'logo.mf' also contains the following cryptic instructions,
which cause the letter pairs '{\manual jk}' and '{\manual lm}' to
be typeset closer together than their bounding boxes would imply:

"'

ligtable "T": "A" kern -.5u#;
ligtable "F": "O" kern -u#;

"'

Without these corrections 'METAFONT' would be ^^@kern@
'{\manual hijklmnj}'. Uppercase letters are often subject to
such spacing corrections, especially in logos; TeX\ will adjust the spacing
if the typeface designer has supplied ^@ligtable@ information like this.

**[Dangerous Bend]** Finally, 'logo.mf' closes with four more commands, which provide
further information about how to typeset with this font:

"'

font_quad 18u#+2s#;
font_normal_space 6u#+2s#;
font_normal_stretch 3u#;
font_normal_shrink 2u#;

"'

A ^@font\_quad@ is the unit of measure that a TeX\ user calls one "em''
when this font is selected. The normal space, stretch, and shrink parameters
^^@font\_normal\_space@ ^^@font\_normal\_stretch@ ^^@font\_normal\_shrink@
define the interword spacing when text is being typeset in this font.
Actually a font like 'logo10' is rarely used to typeset anything except
the one word, 'METAFONT'; but the spacing parameters have been
included just in case somebody wants to typeset a sentence like
'{\manual kn illiji jmhkjm ml hmnjknk mljin kji nmnlkj jmllii}'.

**[Dangerous Bend]** An optional '' or '' sign may be typed after '@font\_size@',
'@font\_quad@', etc., in case you think the file looks better that way.

**[Dangerous Bend]** Notice that "sharped" units must be given in the ^@ligtable@
kerning commands and in the definition of device-independent
parameters like @font\_size@
and @font\_quad@. Appendix F discusses the complete rules of @ligtable@
and other commands by which METAFONT\ programs can send important information
to typesetting systems like TeX. Adding these extra bits of information
to a METAFONT\ program after a font has been designed is something like
adding an index to a book after that book has been written and proofread.

**[Double Dangerous Bend]** exercise What's the longest English word that can be typeset
with the font 'logo9'?

#### Answer
'{\manual nmnkjmnihinj}'; possibly also '{\manual hijklmmjnmji}';
and Georgia suggests that '{\manual knjiinlimllhinj}'
might be a legal term.

**[Dangerous Bend]** Let's summarize the general contents of 'logo.mf', now that we
have seen it all, because it provides an example of a complete typeface
description (even though there are only seven letters):\enddanger

- The file begins by defining ad hoc dimensions and converting
them to pixel units, using @mode\_setup@, @define\_pixels@, etc.

- Then come programs for individual letters. \ (These programs
are often preceded by macro definitions for subroutines that occur several
times. For example, we will see later that the '{\manual k}' and the
'{\manual m}' of the logo are drawn with the help of a subroutine that makes
half of a superellipse; the definition of this macro actually comes near
the beginning of 'logo.mf', just before the programs for the letters.)

- Finally there are special commands like ^@ligtable@ and
^@font\_quad@, to define parameters of the font that are helpful
when typesetting.

- The file is accompanied by parameter files that define
ad hoc dimensions for different incarnations of the typeface.

We could make lots of different parameter files, which would produce
lots of different (but related) variations on the METAFONT\ logo; thus, 'logo.mf'
defines a "" in the sense of Chapter 1.

**[Dangerous Bend]** exercise What changes would be necessary to generalize the 'logo'
routines so that the bar-line height is not always 45 per cent of the
character height?

#### Answer
Delete the line of 'logo.mf' that defines 'barheight#', and
insert that line into each of the parameter files 'logo10.mf', 'logo9.mf',
'logo8.mf'. Then other bar-line heights are possible by providing new
parameter files; another degree of "meta-ness" has therefore been added
to the meta-font.

**[Dangerous Bend]** (":='') have been used instead
of equations ("='') in the parameter files 'logo10.mf',
'logo9.mf', and 'logo8.mf', as well as
in the opening lines of 'io.mf' in Chapter 5; this contradicts the
advice in Chapter 10, where we are told to stick to equations unless
assignments are absolutely necessary. The author has found it convenient
to develop the habit of using assignments whenever ad hoc dimensions
are being defined, because he often makes experimental files in which
the ad hoc dimensions are changed several times. For example, it's a good
idea to test a particular letter with respect to a variety of different
parameter settings when that letter is first being designed; such
experiments can be done easily by copying the ad hoc parameter definitions
from parameter files into a test file, provided that the parameters
have been defined with assignments instead of equations.

**[Dangerous Bend]** TeX\ users have found it convenient to have fonts in a series
of magnifications that form a geometric series. A font is said
to be scaled by ' 1' if it has been magnified by 1.2;
it is scaled by 'magstep 2' if it has been magnified by $1.2\times1.2=1.44$;
it is scaled by 'magstep 3' if it has been magnified by $1.2\times1.2\times1.2=
1.728$; and so on. Thus, if a job uses a font that is scaled by magstep 2,
and if that entire job is magnified by magstep 1, the font actually used
for printing will be scaled by magstep 3. The additive nature of magsteps
makes it more likely that fonts will exist at the desired sizes when
jobs are magnified. Plain METAFONT\ supports this convention by allowing
constructions like

"'

\mode=cheapo; mag=magstep 2; input logo9

"'

if you want to generate the 9-point METAFONT\ logo for the "cheapo" printer,
magnified by 1.44 (i.e., by magstep 2). You can also write "magstep' '0.5''
for what TeX\ calls "stephalf''; this magnifies by $\sqrt1.2$.

**[Double Dangerous Bend]** The sharped forms of dimensions are actually represented by plain
METAFONT\ in terms of printer's points, so that '$"pt"\0$' turns out to be
equal to 1. However, it is best for programmers not to make use of this
fact; a program ought to say, e.g., '$"em"\0:=10"pt"\0$', even though
the '$"pt"\0$' in this construction is redundant, and even though the
computer would run a few microseconds faster without it.

**[Double Dangerous Bend]** exercise Suppose you want to simulate a low-resolution printer
on a high resolution device; for concreteness, let's say that
"luxo" is supposed to produce the output of "cheapo", with each black
"cheapo" pixel replaced by a $10\times10$ square of black "luxo" pixels.
Explain how to do this to the 'logo10' font, by making appropriate
changes to 'logo.mf'. Your output file should be called 'cheaplogo10.2000gf'.

#### Answer
(This is tricky.) \ Insert the lines

"'

if known pixmag: begingroup interim hppp:=pixmag*hppp;
special "title cheapo simulation" endgroup;
extra_endchar:="currentpicture:=currentpicture scaled pixmag;"
& "w:=w*pixmag;" & extra_endchar; fi

"'

right after "mode_setup'' in 'logo.mf', and also include the line

"'

if known pixmag: hppp:=pixmag*hppp; vppp:=pixmag*vppp; fi

"'

at the very end of that file. Then run METAFONT\ with

"'

\mode=cheapo; input cheaplogo10

"'

where the file "cheaplogo10.mf'' says simply "pixmag=10;' 'input' 'logo10''.
\ (The interim "hppp" setting and the ^@special@ command are
used to fool METAFONT\ into giving the appropriate extension to the
file name. Incidentally, you could print with this font on "cheapo"
at ten-fold magnification if you told TeX\ to use the font "cheaplogo10'
'scaled' '10000''; but on "luxo" you would simply call this font
"cheaplogo10''.)

\endchapter

A great Temptation must be withstood with great Resolution.
or WILLIAM , *Expository Notes on the New Testament*
(c.1700)

What some invent, the rest enlarge.

> --- JONATHAN , *Journal of a Modern Lady* (1729)


# Chapter 12. Boxes

\looseness=-1
Let's pause now to take a closer look at the "bounding boxes" that enclose
individual characters. In olden days, metal type was cast on a
rectangular body in which each piece of type had the same vertical
extent, although the type widths would vary from character to character.
Nowadays we are free of the mechanical constraints imposed by metal type,
but the former metaphors are still useful: A typesetting system like
TeX\ imagines that each character fits into a rectangular box, and words are
typeset by putting such boxes snugly next to each other.

\else \\\let\next\dolist \fi
\next}

\copy0\kern-\makelightbox}
The main difference
between the old conventions and the new ones is that type boxes are now
allowed to vary in height as well as in width. For example, when TeX\
typesets 'A line of type.'\ it puts boxes together that essentially look
like this: '\demoboxA line of type.'. \ (The 'A'
appears in a box 'A\maketypebox' that
sits on a given baseline, while the 'y' appears in a box
'y\maketypebox' that descends below the
baseline.) \ TeX\ never looks inside a box to see what character actually
appears there; TeX's job is to put boxes together in the right places
on a page, based only on the box sizes. It is a typeface designer's job
to decide how big the boxes should be and to create the characters inside
the boxes.

Boxes are two-dimensional objects, but we ascribe three dimensions to them
because the vertical component is divided into two quantities, the
(above the ) and the
(below the baseline). The horizontal dimension is, of course, called
the . Here is a picture of a typical box, showing its
so-called and baseline:

{
={$\uparrow$}
= to {$\mid$}
={\copy0
\nointerlineskip \copy1
\nointerlineskip \copy1
\moveleft 1emheight
\copy1 \nointerlineskip
\copy1 \nointerlineskip
{$\downarrow$}
}
={\copy0
\moveleft 1emdepth
{$\downarrow$}
}
={
{\samplebox6em

3pt to 6em Baseline}

\arrows6emwidth}
\indent
={$\vcenter$}
{Reference point$-$$\rightarrow$}
\box4

{\box2\nointerlineskip\box3}}

The example characters in previous chapters have all had zero depth, but
we will soon be seeing examples in which both height and depth are relevant.

A character shape need not fit inside the boundaries of its box. Indeed,
*italic* and *slanted* letters are put into ordinary boxes
just as if they were not slanted, so they frequently stick out at the right.
For example, the letter 'g' in the font you are now reading ()
can be compared with the '*g*' in the corresponding slanted
font ():

>
to 40pt{\ifproofmode\hrule
=2.5in 6pt \fiverm
(A figure will be inserted here; too bad you can't see it now.
It shows two g's, as claimed. In fact, the same figure appeared
on page 63 of The TeXbook.)
\hrule\fi}

The slanted '*g*' has been drawn as if its box were skewed right at the
top and left at the bottom, keeping the baseline fixed; but TeX\ is told
in both cases that the box is $5\pt$ wide, $4.3055\pt$ high, and $1.9444\pt$
deep. Slanted letters will be spaced properly in spite of the fact that their
boxes have been straightened up, because the letters will match correctly
at the baseline.

**[Dangerous Bend]** Boxes also have a fourth dimension called the {^italic
correction}, which gives TeX\ additional information about whether or
not a letter protrudes at the right. For example, the italic correction
for an unslanted 'g' in 'cmr10' is $0.1389\pt$, while the corresponding
slanted letter in 'cmsl10' has an italic correction of $0.8565\pt$. The
italic correction is added to a box's width when math formulas like $g^2$ or $*g*^2$ are being typeset, and also in other cases as
explained in *The TeX book*.

Plain METAFONT's ^@beginchar@ command establishes the width, height, and depth
of a box. These dimensions should be given in terms of ""
quantities that do not vary with the resolution or magnification, because
the size of a character's type box should not depend in any way on the device
that will be used to output that character. It is important to be able to
define documents that will not change even though the technology for printing
those documents is continually evolving. METAFONT\ can be used to produce fonts for
new devices by introducing new "modes," as we have seen in Chapter 11,
but the new fonts should still give the same box dimensions to each character.
Then the device-independent files output by TeX\ will not have to be
changed in any way when they are printed or displayed with the help of
new equipment.

The three dimensions in a @beginchar@ command are given in reverse
alphabetical order: First comes the width, then the height, then the depth.
The @beginchar@ routine converts these quantities into pixel units
and assigns them to the three variables , , and . In fact,
@beginchar@ rounds these dimensions to the nearest whole number of
pixels; hence $w$, $h$, and $d$ will always be integers.

METAFONT's pixels are like squares on , with pixel boundaries
at points with integer coordinates. The left edge of the type box lies
on the line $x=0$, and the right edge lies on the line $x=w$; we have
$y=h$ on the top edge and $y=-d$ on the bottom edge. There are $w$ pixels
in each row and $h+d$ in each column, so there are exactly $wh+wd$ pixels
inside the type box.

Since $w$, $h$, and $d$ are integers, they probably do not exactly match
the box dimensions that are assumed by device-independent typesetting
systems like TeX. Some characters will be a fraction of a pixel too wide;
others will be a fraction of a pixel too narrow. However, it's still possible
to obtain satisfactory results if the pixel boxes are stacked together
based on their $w$ values and if the accumulated error is removed in the
spaces between words, provided that the box positions do not
too far away from their true device-independent locations. A designer should
strive to obtain letterforms that work well together when they are placed
together in boxes that are an integer number of pixels wide.

**[Double Dangerous Bend]** You might not like the value of $w$ that @beginchar@ computes by
rounding the device-independent width to the nearest pixel boundary.
For example, you might want to make the letter 'm' one pixel wider, at
certain resolutions, so that its three stems are equally spaced or so that
it will go better with your 'n'. In such a case you can assign a new value
to $w$, at any time between @beginchar@ and ^@endchar@. This new value
will not affect the device-independent box width assumed by TeX, but it
should be respected by the software that typesets files using your font.

={
{{ to 140\apspix{\hidecoords(0,h)
\hidecoords(w\mkern-2mu,h)}

\figbox12a{140\apspix}{360\apspix}

to 140\apspix{\hidecoords(0,-d)
\hidecoords(w\mkern-2mu,-d)}}}}
=0pt

Here's an example of a character that has nonzero width, height, and depth;
it's the left in fonts like 'cmr10'.
Computer Modern typefaces are generated by METAFONT\ programs that involve
lots of parameters, so this example also illustrates the principles of
"": Many different varieties of left parentheses can be
drawn by this one program. But let's focus our attention first on the
comparatively simple way in which the box dimensions are established and
used, before looking into the details of how a meta-parenthesis has
actually been specified.

>
'"Left parenthesis"';
@numeric@ $"ht"\0$, $"dp"\0$;
$"ht"\0="body\_height"\0$; \ $.5["ht"\0,-"dp"\0]="axis"\0$;
@beginchar@('"("'$,7u\0,"ht"\0,"dp"\0)$;
@italcorr@ $"ht"\0\ast"slant"-.5u\0$;
@pickup@ "fine.nib";
$\penpos1("hair"-"fine",0)$;\vadjust{\box0}
$\penpos2(.75["thin","thick"]-"fine",0)$;
$\penpos3("hair"-"fine",0)$;
$\mathop"rt"x_1r=\mathop"rt"x_3r= w-u$; \
$\mathop"lft"x_2l=x_1-4u$;
$\mathop"top"y_1=h$; \
$y_2=.5[y_1,y_3]="axis"$;
@filldraw@ $z_1l\xs(2l,1l)\ldots z_2l$
$\ldots\xs(3l,2l)z_3l$
$\dashto z_3r\xs(2r,3r)\ldots z_2r$
$\ldots\xs(1r,2r)z_1r\dashto\cycle$;
@penlabels@$(1,2,3)$; \ @endchar@;

The width of this left parenthesis is $7u\0$, where $u\0$
is an ad hoc parameter that figures in all the widths of the Computer
Modern characters. The height and depth have been calculated in such a way
that the top and bottom of the bounding box are equally distant from an
imaginary line called the , which is important in mathematical
typesetting. \ (For example, TeX\ puts the bar line at the axis
in fractions like $1\over2$; many symbols like '$+$' and '$=$', as well as
parentheses, are centered on the axis line.) \ Our example program puts the
axis midway between the top and bottom of the type by saying that
'$.5["ht"\0,-"dp"\0]="axis"\0$'. We also place the top at position
'$"ht"\0="body\_height"\0$'; here $"body\_height"\0$ is the
height of the tallest characters in the entire typeface.
It turns out that $"body\_height"\0$ is exactly $7.5"pt"\0$ in 'cmr10', and
$"axis"\0=2.5"pt"\0$; hence $"dp"\0=2.5"pt"\0$,
and the parenthesis is exactly $10\pt$ tall.

The program for '(' uses a ^@filldraw@ command, which we haven't
seen before in this book; it's basically a combination of @fill@
and @draw@, where the filling is done with the currently-picked-up pen.
Some of the Computer Modern fonts have characters with "" edges
while others have "" edges; the difference is due to the pen that
is used to @filldraw@ the shapes. This pen is a circle whose diameter
is called ^"fine"; when "fine" is fairly large, @filldraw@ will produce
rounded corners, but when $"fine"=0$ (as it is in 'cmr10') the corners
will be sharp.

The statement '$\penpos1("hair"-"fine",0)$' makes the breadth of a
simulated broad-edge pen equal to $"hair"-"fine"$ at position 1; i.e.,
the distance between $z_1l$ and $z_1r$ will be $"hair"-"fine"$.
We will be filling a region between $z_1l$ and $z_1r$ with a
circle-shaped pen nib whose diameter is "fine"; the center of that
nib will pass through $z_1l$ and $z_1r$, hence the pen will
effectively add ${1\over2}"fine"$ to the breadth of the stroke at
either side. The overall breadth at position 1 will therefore be
${1\over2}"fine"+("hair"-"fine")+{1\over2}"fine"\;=\;"hair"$.
(Computer Modern's " thickness" parameter, which governs
the breadth of the thinnest strokes, is called "hair".) \ Similarly,
the statement '$\penpos2(.75["thin","thick"]-"fine",0)$' makes the
overall breadth of the pen at position 2 equal to $.75["thin","thick"]$,
which is $3\over4$ of the way between two other parameters that govern
stroke breadths in Computer Modern routines. If "fine" is increased while
"hair", "thin", and "thick" stay the same, the effect will simply be to
produce more rounded corners at positions 1 and 3, with little or no effect
on the rest of the shape, provided that "fine" doesn't get so large
that it exceeds "hair".

{{\dimen0=#3\apspix =7\dimen0
#1
\kern270\apspix \kern-#4\apspix
\dimen2=#4\apspix \dimen2 by -#5\apspix
\figbox#2{7\dimen0}{2\dimen2}
\kern-2\dimen2 \kern#4\apspix \kern90\apspix
0pt plus 1fil
to{$##$
u=#3
"ht"=#4
"axis"=#5
"fine"=#6
"hair"=#7
"thin"=#8
"thick"=#9}}}

Here, for example, are five different left parentheses, drawn by our example
program with various settings of the parameters:
$$en cmr10 12a 20 270 90 0 8 9 25
en cmbx10 12b 23 270 90 0 13 17 41
en cmvtt10 12c 21 250 110 22 22 25 25
en cmssdc10 12d 19 270 95 8 23 40 40
en cmti10 12e 18.4 270 90 7 8 11 23 $$
Parameter values are shown here in ^"proof"\ mode pixel units,
36 to the point. \ (Thus, for example, the value of $u\0$ in 'cmr10' is
${20\over36}"pt"\0$.) \ Since 'cmbx10' is a "bold extended" font,
its unit width $u$ is slightly larger than the unit width of 'cmr10',
and its pen widths (especially "thick") are significantly larger.
The "variable-width typewriter" font 'cmvtt10' has soft edges and
strokes of almost uniform thickness, because "fine" and "hair" are almost
as large as "thin" and "thick". This font also has a raised axis and a smaller
height. An intermediate situation occurs in 'cmssdc10', a "sans serif
demibold condensed" font that is similar to the type used in the chapter titles
of this book; $"thick"="thin"$ in this font, but hairlines are noticeably
thinner, and "fine" provides slightly rounded corners. The "text italic"
font 'cmti10' has rounded ends, and the character shape has been
by .25; this means that each point $(x,y)$ has been moved to position
$(x+.25y,y)$, in the path that is filled by @filldraw@.

**[Dangerous Bend]** The vertical line just to the right of the italic left parenthesis
shows the of that character, i.e., the fourth box
dimension mentioned earlier. This quantity was defined by the statement
'^@italcorr@ $"ht"\0\ast"slant"-.5u\0$' in our program; here ^"slant" is
a parameter of Computer Modern that is zero in all the unslanted fonts,
but $"slant"=.25$ in the case of 'cmti10'. The expression following
@italcorr@ should always be given in sharped units. If the value is
negative, the italic correction will be zero; otherwise the italic
correction will be the stated amount.

**[Dangerous Bend]** The author has obtained satisfactory results by making the italic
correction roughly equal to $.5u$ plus the maximum amount by which the
character sticks out to the right of its box. For example, the top right
end of the left parenthesis will be nearly at position $(w-u,"ht")$ before
slanting, so its $x$ coordinate after slanting will be $w-u+"ht"\ast"slant"$;
this will be the rightmost point of the
character, if we assume that $"slant"\ge0$. Adding $.5u$, subtracting $w$,
and rewriting in terms of sharped units gives the stated formula. Notice
that when $"slant"=0$ the statement reduces to '@italcorr@ $-.5u\0$';
this means that unslanted left parentheses will have an italic correction
of zero.

**[Dangerous Bend]** exercise Write a program for right parentheses, to go with these
left parentheses.

#### Answer
The changes are straightforward, except for the italic correction
(for which a rough estimate like the one shown here is good enough):

>
'"Right parenthesis"';
@numeric@ $"ht"\0,"dp"\0$; \
$"ht"\0="body\_height"\0$; \
$.5["ht"\0,-"dp"\0]="axis"\0$;
@beginchar@('")"'$,7u\0,"ht"\0,"dp"\0)$;
\ @italcorr@ $"axis"\0\ast"slant"-.5u\0$;
@pickup@ "fine.nib"; \ $\penpos1("hair"-"fine",0)$;
$\penpos2(.75["thin","thick"]-"fine",0)$; \ $\penpos3("hair"-"fine",0)$;
$\mathop"lft"x_1l=\mathop"lft"x_3l=u$; \
$\mathop"rt"x_2r=x_1+4u$; \
$\mathop"top"y_1=h$; \
$y_2=.5[y_1,y_3]="axis"$;
@filldraw@ $z_1l\xs(2l,1l)\ldots z_2l\ldots\xs(3l,2l)z_3l$
$\dashto z_3r\xs(2r,3r)
\ldots z_2r\ldots\xs(1r,2r)z_1r\dashto\cycle$;
@penlabels@$(1,2,3)$; \ @endchar@;

We will see in Chapter 15 that it's possible to guarantee perfect symmetry
between left and right parentheses by using picture transformations.

The reader should bear in mind that the conventions of plain METAFONT\ and of
Computer Modern are not hardwired into the METAFONT\ language; they are merely
examples of how a person might use the system, and other typefaces may well
be better served by quite different approaches. Our program for left
parentheses makes use of @beginchar@, @endchar@, @italcorr@, @penlabels@,
@pickup@, "penpos", "lft", "rt", "top", "z", and @filldraw@, all of which
are defined somewhat arbitrarily in Appendix B as part of the plain base;
it also uses the quantities "u", "body\_height", "axis", "fine", "hair",
"thin", "thick", and "slant", all of which are arbitrary parameters that
the author decided to introduce in his programs for Computer Modern. Once
you understand how to use arbitrary conventions like these, you will be
able to modify them to suit your own purposes.

### Exercise
(For people who know TeX.) \ It's fairly clear that the width of
a type box is important for typesetting, but what use does TeX\ make of
the height and depth?

#### Answer
When horizontal lines are being typeset, TeX\ keeps track of the
maximum height and maximum depth of all boxes on the line; this determines
whether or not extra space is needed between baselines. The height and depth
are also used to position an accent above or below a character, and to
place symbols in mathematical formulas. Sometimes
boxes are also stacked up vertically, in which case their heights and depths
are just as important as their widths are for horizontal setting.

**[Double Dangerous Bend]** The primitive commands by which METAFONT\ actually learns the dimensions
of each box are rarely used directly, since they are intended to be embedded
in higher-level commands like @beginchar@ and @italcorr@. But if you must
know how things are done at the low level, here is the secret: There are
four internal quantities called ^"charwd", ^"charht", ^"chardp", and ^"charic",
whose values at the time of every ^@shipout@ command are assumed to be the
box dimensions for the character being shipped out, in units of printer's
points. \ (See
the definitions of @beginchar@ and @italcorr@ in Appendix B for examples
of how these quantities can be manipulated.)

**[Double Dangerous Bend]** Besides "charwd" and its cousins, METAFONT\ also has four other
internal variables whose values are recorded at the time of every
@shipout@:\enddanger

- ^"charcode" is rounded to the nearest integer
and then converted to a number between 0 and 255, by adding or subtracting
multiples of 256 if necessary; this "$c$ code" is the of the
character within its font.

- ^"charext" is rounded to the nearest integer;
the resulting number is a secondary code that can be used to distinguish
between two or more characters with equal $c$ codes. \ (TeX\ ignores
"charext" and assumes that each font contains at most 256 characters; but
extensions to TeX\ for languages can use "charext" to handle
much larger fonts.)

- ^"chardx" and "chardy" represent horizontal and
vertical *escapement* in units of pixels. \ (Some typesetting
systems use both of these device-dependent amounts to alter their current
position on a page, just after typesetting each character. Other systems,
like typical software associated with TeX, assume that $"chardy"=0$
but use "chardx" as the horizontal escapement whenever a horizontal
movement by "chardx" does not cause the subsequent position to
too far from the device-independent position defined by accumulated
"charwd" values. Plain METAFONT's @endchar@ routine keeps $"chardy"=0$, but
sets $"chardx":=w$ just before shipping a character to the output. This
explains why a change to will affect the spacing between adjacent
letters, as discussed earlier.) \looseness=-1

**[Double Dangerous Bend]** Two characters with the same $c$ code
should have the same box dimensions and escapements; otherwise
the second character will override the specifications of the first. The boolean
expression ' $c$' can be used to determine whether or not
a character with a particular $c$ code has already been shipped out.

**[Dangerous Bend]** Let's conclude this chapter by contemplating a METAFONT\ program that
generates the "" symbol, since that symbol appears so
often in this book. It's a custom-made character intended to be used only at
the very beginnings of paragraphs in which the baselines of the text are
exactly $11\pt$ apart. Therefore it extends below its baseline by $11\pt$;
but it is put into a box of depth zero, because TeX\ would otherwise
think that the first line of the paragraph contains an extremely deep
character, and such depth would cause the second line to be moved down.
$$\def\comment{{\%} }
{ to{\indent#}
$"baselinedistance"\0:=11"pt"\0$; \ ^@define\_pixels@("baselinedistance");
$"heavyline"\0:=50/36"pt"\0$; \ ^@define\_blacker\_pixels@("heavyline");
$@beginchar@(127,25u\0,"h\_height"\0+"border"\0,0)$; \
'"Dangerous bend symbol"';
\pickup @pencircle@ scaled "rulethickness";
\ $\mathop"top"y_1={25\over27}h$; \ $\mathop"lft"x_4=0$;
$x_1+x_1=x_1a+x_1b=x_4b+x_2a=x_4+x_2=x_4a+x_2b=x_3b+x_3a=
x_3+x_3=w$;
$x_4a=x_4b=x_4+u$; \ $x_3b=x_1a=x_1-2u$;
$y_4+y_4=y_4a+y_4b=y_3b+y_1a=y_3+y_1=y_3a+y_1b=y_2b+y_2a=
y_2+y_2=0$;
$y_1a=y_1b=y_1-{2\over27}h$; \ $y_4b=y_2a=
y_4+{4\over27}h$;
@draw@ $z_1a\to z_1\to z_1b\ddashto z_2a\to z_2\to z_2b\ddashto$
\indent $z_3a\to z_3\to z_3b\ddashto z_4a\to z_4\to z_4b
\ddashto cycle$;\comment the signboard
$x_10=x_11=x_12=x_13=.5w-u$;
\ $x_14=x_15=x_16=x_17=w-x_10$;
$y_10=y_14={28\over27}h$; \ $\mathop"bot"y_13=-"baselinedistance"$;
$z_11=(z_10\to z_13)\;intersectionpoint\;
(z_1a\{z_1a-z_4b\}\to z_1\{"right"\})$;
$y_15=y_11$; \ $y_16=y_12=-y_11$; \ $y_17=y_20=y_21=y_13$;
@draw@ $z_11\dashto z_10\dashto z_14\dashto z_15$;
@draw@ $z_12\dashto z_13$;
@draw@ $z_16\dashto z_17$; \comment the signpost
$x_20=w-x_21$; \ $x_21-x_20=16u$;
\ @draw@ $z_20\dashto z_21$; \comment ground level
$x_36=w-x_31$; \ $x_36-x_31=8u$;
\ $x_32=x_33=x_36$; \ $x_31=x_34=x_35$;
$y_31=-y_36={12\over27}h$; \ $y_32=-y_35={9\over27}h$;
\ $y_33=-y_34={3\over27}h$;
\pickup @pencircle@ scaled "heavyline";
@draw@ $z_32\{z_32-z_31\}\to z_33\ddashto
z_34\to z_35\{z_36-z_35\}$;
\comment the dangerous bend
\pickup ^@penrazor@ xscaled "heavyline"
($(z_32-z_31)+90$);
@draw@ $z_31\dashto z_32$;
\ @draw@ $z_35\dashto z_36$; \comment upper and lower bars
^@labels@$(1a,1b,2a,2b,3a,3b,4a,4b,@range@ 1 @thru@ 36)$; \ @endchar@;
^^@range@^^@thru@
}$$

={
\figbox12f{500\apspix}4.2in}
=0pt

{\tolerance=2000 \hbadness=2000 \spaceskip=.3333em plus .25em minus .12em
\hangindent 515\apspix
to 515\apspix{\box0}
This program has several noteworthy points of interest:
(1) The first parameter to ^@beginchar@ here is 127, not a
string; this puts the character into font 127. \ (2) A sequence
of equations like '$a=w-b$; $a'=w-b'$' can conveniently be shortened to
'$a+b=a'+b'=w$'. \ (3) Three hyphens '$\ddashto$' is an abbreviation for a
line with "infinite" tension, i.e., an almost straight line that
connects smoothly to its curved neighbors. \ (4) An 'intersectionpoint'
operation finds out where
two paths cross; we'll learn more about this in Chapter 14.}

\endchapter

Well, we are in the same box.

> --- RIDER , *Dawn* (1884)

A story, too,
may be boxed.

> --- DOROTHY , *Newspaper Nomenclature* (1927)


# Chapter 13. Drawing, Filling, and Erasing

The pictures that METAFONT\ produces are made up of tiny pixels that are either
"on" or "off"; therefore you might imagine that the computer works
behind the scenes with some sort of , and that it darkens some
of the squares whenever you tell it to @draw@ a line or to @fill@ a region.

\next}

\belowdisplayskip by-2pt
=\tinypix
\indent\spread##!}
METAFONT's internal graph paper is actually more sophisticated than this.
Pixels aren't simply "on" or "off" when METAFONT\ is working on a picture;
they can be "doubly on" or "triply off." Each pixel contains a
small *integer* value, and when a character is finally shipped out
to a font the black pixels are those whose value is greater than zero.
For example, the two commands

>
^@fill@ $(0,3)\dashto(9,3)\dashto(9,6)\dashto(0,6)\dashto\cycle$;
@fill@ $(3,0)\dashto(3,9)\dashto(6,9)\dashto(6,0)\dashto\cycle$

yield the following $9\times9$ pattern of pixel values:
\beginpixdisplay
000111000
000111000
000111000
111222111
111222111
111222111
000111000
000111000
000111000

Pixels that have been filled twice now have a value of 2.

When a simple region is "filled," its pixel values are all increased by 1;
when it is "unfilled," they are all decreased by 1. The command

>
^@unfill@ $(1,4)\dashto(8,4)\dashto(8,5)\dashto(1,5)\dashto\cycle$

will therefore change the pattern above to
\beginpixdisplay
000111000
000111000
000111000
111222111
100111001
111222111
000111000
000111000
000111000

The pixels in the center have not been erased (i.e., they will still be
black if this picture is output to a font), because they still have a
positive value.

Incidentally, this example illustrates the fact that the edges between
METAFONT's pixels are lines that have integer , just as the
squares on graph paper do. For example, the lower left '0' in
the $9\times9$ array above corresponds to the pixel whose boundary is
'$(0,0)\dashto(1,0)\dashto(1,1)\dashto(0,1)\dashto\cycle$'. The $(x,y)$
coordinates of the points inside this pixel lie between 0 and 1.

### Exercise
What are the $(x,y)$ coordinates of the four corners of the
*middle* pixel in the $9\times9$ array?

#### Answer
$(4,4)$, $(4,5)$, $(5,5)$, $(5,4)$. \ (Therefore the command

>
@unfill@ $(4,4)\dashto(4,5)\dashto(5,5)\dashto(5,4)\dashto\cycle$

will decrease the value of this pixel by 1.)

### Exercise
What picture would have been obtained if the @unfill@ command
had been given *before* the two @fill@ commands in the examples
above?

#### Answer
The result would be exactly the same; @fill@ and @unfill@ commands
can be given in any order. \ (After an initial @unfill@ command, some
pixel values will be $-1$, the others will be zero.)

### Exercise
Devise an @unfill@ command that will produce the pixel values
\beginpixdisplay
000111000
000101000
000101000
111212111
100101001
111212111
000101000
000101000
000111000

when it is used just after the @fill@ and @unfill@ commands already given.

#### Answer
@unfill@ $(4,1)\dashto(4,8)\dashto(5,8)\dashto(5,1)\dashto\cycle$.

A "simple" region is one whose boundary does not intersect itself; more
complicated effects occur when the boundary lines cross. For example,

>
@fill@ $(0,1)\dashto(9,1)\dashto(9,4)\dashto(4,4)\dashto$
\indent$(4,0)\dashto(6,0)\dashto
(6,3)\dashto(8,3)\dashto(8,2)\dashto(0,2)\dashto\cycle$

produces the pixel pattern
\beginpixdisplay
000011111
000011001
111122111
000011000

Notice that some pixels receive the value 2, because they're "^doubly
filled." There's also a "" where the pixel values remain zero,
even though they are surrounded by filled pixels; the pixels in that hole
are not considered to be in the region, but the doubly filled pixels
are considered to be in the region twice.

### Exercise
Show that the first $9\times9$ cross pattern on the previous
page can be generated by a single @fill@ command. \ (The nine pixel
values in the center should be 2, as if two separate regions had been
filled, even though you are doing only one @fill@.)

#### Answer
Here are two of the many solutions:

>
@fill@ $(0,3)\dashto(9,3)\dashto(9,6)\dashto(6,6)\dashto(6,9)\dashto$
\indent $(3,9)\dashto(3,0)\dashto(6,0)\dashto(6,6)\dashto(0,6)\dashto\cycle$;
@fill@ $(0,3)\dashto(9,3)\dashto(9,6)\dashto(0,6)\dashto(0,3)\dashto$
\indent $(3,3)\dashto(3,0)\dashto(6,0)\dashto(6,9)\dashto(3,9)\dashto
(3,3)\dashto\cycle$.

(It turns out that *any* pixel pattern can be obtained by a single,
sufficiently hairy @fill@ command. But unnatural commands are usually also
inefficient and unreadable.)

### Exercise
What do you think is the result of '@fill@ $(0,0)\dashto(1,0)\dashto
(1,1)\dashto(0,1)\dashto(0,0)\dashto(1,0)\dashto(1,1)\dashto(0,1)\dashto
\cycle$'?

#### Answer
The value of the enclosed pixel is increased by 2. \ (We'll see later
that there's a simpler way to do this.)

A @fill@ command can produce even stranger effects when its boundary lines
cross in only one place. If you say, for example,

>
@fill@ $(0,2)\dashto(4,2)\dashto(4,4)\dashto(2,4)\dashto(2,0)
\dashto(0,0)\dashto\cycle$

METAFONT\ will produce the $4\times4$ pattern
= to\tinypix{
$riptscriptstyle{ to3pt\over}$\kern\pixcorr}
=0pt
\beginpixdisplay
0011
0011
!\copy0\copy0 \spread00
!\copy0\copy0 \spread00

where '$ to3pt\over$' stands for the value $-1$. Furthermore the
machine will report that you have a "" whose "^turning
number" is zero! What does this mean? Basically, it means that your
path loops around on itself something like a figure 8; this causes a
breakdown in METAFONT's usual rules for distinguishing the "inside" and
"outside" of a curve.

**[Dangerous Bend]** Every cyclic path has a *turning number* that can be understood
as follows. Imagine that you are driving a car along the path and that you
have a digital compass that tells in what direction you're heading. For
example, if the path is

>
$(0,0)\dashto(2,0)\dashto(2,2)\dashto(0,2)\dashto\cycle$

you begin driving in direction $0^\circ$, then you make four left turns.
After the first turn, your compass heading is $90^\circ$; after the
second, it is $180^\circ$; and after the third it is $270^\circ$. \ (The
compass direction increases when you turn left and decreases when you turn
right; therefore it now reads $270^\circ$, not $-90^\circ$.) \ At the
end of this cycle the compass will read $360^\circ$, and if you go around
again the reading will be $720^\circ$. Similarly, if you had traversed the
path

>
$(0,0)\dashto(0,2)\dashto(2,2)\dashto(2,0)\dashto\cycle$

(which is essentially the same, but in the opposite direction), your compass
heading would have started at $90^\circ$ and ended at $-270^\circ$;
in this case each circuit would have *decreased* the reading
by $360^\circ$. It is clear that a drive around any cyclic path will
change the compass heading by some multiple of $360^\circ$, since you
end in the same direction you started. The turning number of a path is
defined to be $t$ if the compass heading changes by exactly $t$ times
$360^\circ$ when the path is traversed. Thus, the two example cycles we have
just discussed have turning numbers of $+1$ and $-1$, respectively; and
the "strange path" on the previous page that produced both positive and
negative pixel values does indeed have a turning number of 0.

**[Dangerous Bend]** Here's how METAFONT\ actually implements a @fill@ command, assuming that
the cyclic path being filled has a *positive* turning number:
The path is first "," if necessary, so that it lies entirely on
the edges of pixels; in other words, it is distorted slightly so that it
is confined to the lines between pixels on graph paper. \ (Our examples so
far in this chapter have not needed any such adjustments.) \ Then each
individual pixel value is increased by $j$ and decreased by $k$ if an
infinite horizontal line to the left of that pixel intersects the
digitized path $j$ times when the path is traveling downward and $k$ times
when it is traveling upward. For example, let's look more closely at the
non-simple path on the previous page that enclosed a hole:
$$\def\\#1{ to 11pt{$#1$}}

{\tenex}{\tenex}}}}

{\tenex}{\tenex}}}}

{\indent#
\\a\\a\\a\\a\over\down\\b\over\\b\over\under\\b\over\under\\b\over\\b\up
\under\\a\under\\a\under\\a\under\\a\down\under\\b\under\\b\up
\under\\c\under\\c\down\\d\up
\down\under\\e\under\\e\under\\e\under\\e\down\under\\f\under\\f\up
\under\\g\under\\g\under\\g\up
\\a\\a\\a\\a\down\under\\b\under\\b\up\\h\\h\\h}$$
Pixel $d$ has $j=2$ descending edges and $k=1$ ascending edges to its left,
so its net value increases by $j-k=1$; pixels $g$ are similar.
Pixels $c$ have $j=k=1$, so they lie in a "hole" that is unfilled;
pixels $f$ have $j=2$ and $k=0$, so they are doubly filled. This rule
works because, intuitively, the inside of a region lies at the *left*
of a path whose turning number is positive.

**[Dangerous Bend]** exercise True or false: When the turning number of a cyclic path is
positive, a @fill@ command increases each individual pixel value by $l-m$,
if an infinite horizontal line to the *right* of that pixel intersects
the digitized path $l$ times when the path is traveling upward and $m$ times
when it is traveling downward. \ (For example, pixels $e$ have $l=2$ and
$m=1$; pixels $c$ have $l=m=1$.)

#### Answer
True; $j-k=l-m$, since $k+l=j+m$. \ (What comes up must go down.)

**[Dangerous Bend]** When the turning number is negative, a similar rule applies,
except that the pixel values are *decreased* by $j$ and *increased* by $k$; in this case the inside of the region lies at the
*right* of the path.

**[Dangerous Bend]** But when the turning number is zero, the inside of the region
lies sometimes at the left, sometimes at the right. METAFONT\ uses the rule
for positive turning number and reports that the path is "strange."
You can avoid this error message by setting '$"turningcheck":=0$';
^^"turningcheck" in this case the rule for positive turning number is
always used for filling, even when the turning number is negative.

Plain METAFONT's ^@draw@ command is different from @fill@ in two important ways.
First, it uses the currently-picked-up pen, thereby "thickening" the path.
Second, it does not require that the path be cyclic. There is also a third
difference, which needs to be mentioned although it is not quite as important:
A @draw@ command may increase the value of certain pixels by more than 1,
even if the shape being drawn is fairly simple. For example, the pixel pattern
{indent=0pt
\beginpixdisplay
0000000000000000000000000000000000000000000000000000000000000000000000
0000001111122222111110000000000000000000000000011111111000000000000000
0000111111111211111111100000000000000000000011111111111111000000000000
0001111111111011111111110000000000000000001111111111111111110000000000
0001111111111011111111110000000000000000111111111111111111111100000000
0011111111110001111111111000000000000001111111111111111111111110000000
0011111111110001111111111000000000000011111111111111111111111111000000
0011111111110001111111111000000000000111111111111111111111111111100000
0111111111100000111111111100000000001111111111111111111111111111110000
0111111111100000111111111100000000001111111111111111111111111111110000
0111111111100000111111111100000000011111111111111111111111111111111000
0111111111100000111111111100000000011111111111111111111111111111111000
0111111111100000111111111100000000111111111111111112111111111111111100
0111111111100000111111111100000000111111111111111112111111111111111100
0111111111100000111111111100000001111111111111111122111111111111111110
0111111111100000111111111100000001111111111111211121111211111111111110
0111111111100000111111111100000001111111111111112122221111111111111110
0111111111100000111111111100000001111111111111111100111111111111111110
0111111111100000111111111100000001111111111111112000011111111111111110
0111111111100000111111111100000001111111111112211000011211111111111110
0111111111100000111111111100000000111111111111110000001111111111111100
0111111111100000111111111100000000111111111111110000001111111111111100
0111111111100000111111111100000000011111111111100000000111111111111000
0111111111100000111111111100000000001111111111000000000011111111110000
0111111111100000111111111100000000000011111100000000000000111111000000
0000000000000000000000000000000000000000000000000000000000000000000000

}
was produced by two @draw@ commands. The left-hand shape came from

>
\pickup ^@penrazor@ scaled 10; \% a pen of width 10 and height 0
@draw@ $(6,1)\{"up"\}\to(13.5,25)\to\{"down"\}(21,1)$;

it's not difficult to imagine why some of the top pixels get the value 2
here because an actual razor-thin pen would cover those pixels twice as it
follows the given path. But the right-hand shape, which came from

>
\pickup @pencircle@ scaled 16; \ @draw@ $(41,9)\to(51,17)\to(61,9)$

is harder to explain; there seems to be no rhyme or reason to the pattern
of 2's in that case. METAFONT's method for drawing curves with thick pens is
too complicated to explain here, so we shall just regard it as a curious
process that occasionally shoots out extra spurts of ink in the interior
of the shape that it's filling. Sometimes a pixel value even gets as high
as 3 or more; but if we ignore such anomalies and simply consider the set
of pixels that receive a positive value, we find that a reasonable shape
has been drawn.

The left-parenthesis example in Chapter 12 illustrates the ^@filldraw@
command, which is like @fill@ in that it requires a cyclic path, and like
@draw@ in that it uses the current pen. Pixel values are increased inside
the region that you would obtain by drawing the specified path with the current
pen and then filling in the interior. Some of the pixel values in this
region may increase by 2 or more. The turning number of the path
should be nonzero.

Besides @fill@, @draw@, and @filldraw@, you can also say '^@drawdot@',
as illustrated at the beginning of Chapter 5. In this case you should specify
only a single point; the currently-picked-up pen will be used to increase
pixel values by 1 around that point. Chapter 24 explains that this gives
slightly better results than if you were to draw a one-point path.

**[Dangerous Bend]** There's also an ^@undraw@ command, analogous to @unfill@; it
decreases pixel values by the same amount that @draw@ would increase them.
Furthermore---as you might expect---^@unfilldraw@ and ^@undrawdot@ are the
respective opposites of @filldraw@ and @drawdot@.

**[Dangerous Bend]** If you try to use @unfill@ and/or @undraw@ in connection with
@fill@ and/or @draw@, you'll soon discover that something else is
necessary. Plain METAFONT\ has a ^@cullit@ command that replaces all
negative pixel values by 0 and all positive pixel values by 1. This
"" operation makes it possible to erase unwanted sections
of a picture in spite of the vagaries of @draw@ and @undraw@, and in spite of
the fact that overlapping regions may be doubly filled.

**[Dangerous Bend]** The command '^@erase@ @fill@ $c$' is an abbreviation for
'@cullit@; @unfill@ $c$; @cullit@'; this zeros out the pixel values inside
the cyclic path $c$, and sets other pixel values to 1 if they were positive
before erasing took place. \ (It works because the initial @cullit@ makes
all the values 0 or 1, then the @unfill@ changes the values inside $c$
to 0 or negative. The final @cullit@ gets rid of the negative values,
so that they won't detract from future filling and drawing.) \ You can
also use '@draw@', '@filldraw@', or '@drawdot@' with '@erase@'; for example,
'@erase@ @draw@ $p$' is an abbreviation for '@cullit@; @undraw@ $p$;
@cullit@', which uses the currently-picked-up pen as if it were an
eraser applied to path $p$.

{
\medbreak
shape 7 3pc 17pc 3pc 17pc
0pc 20pc 0pc 20pc 0pc 20pc 0pc 20pc 0pc 29pc

to0pt{\dbend}
\rightfig 13a ({166.66667\apspix} x {133.33333\apspix}) ^9pt
The cube at the right of this paragraph illustrates one of the effects that
is easily obtained by erasing. First the eight points are defined, and
the "back" square is drawn; then two lines of the "front" square are
erased, using a somewhat thicker pen; finally the remaining lines are
drawn with the ordinary pen:

>
$s\0:=5"pt"\0$; \ @define\_pixels@$(s)$; \ \% side of the square
$z_1=(0,0)$; \ $z_2=(s,0)$; \ $z_3=(0,s)$; \ $z_4=(s,s)$;
^@for@ $k=1$ @upto@ 4: $z[k+4]=z[k]+({2\over3}s,{1\over3}s)$; \ @endfor@
\pickup @pencircle@ scaled $.4"pt"$; \
@draw@ $z_5\dashto z_6\dashto z_8\dashto z_7\dashto \cycle$;
\pickup @pencircle@ scaled $1.6"pt"$; \
@erase@ @draw@ $z_2\dashto z_4\dashto z_3$;
\pickup @pencircle@ scaled $.4"pt"$; \
@draw@ $z_1\dashto z_2\dashto z_4\dashto z_3\dashto \cycle$;
@for@ $k=1$ @upto@ 4: @draw@ $z[k]\dashto z[k+4]$; \ @endfor@.

At its true size the resulting looks like this:
'{\manual\cubea}'.}

**[Dangerous Bend]** exercise Modify the draw-and-erase construction in the preceding
paragraph so that you get the
'{\manual\cubeb}' instead.

#### Answer
The tricky part is to remember that '@erase@ @draw@ $z_i\dashto z_j$'
will erase pixels near $z_i$ and $z_j$. Therefore if $z_3\dashto z_4$ is
drawn before $z_4\dashto z_2$, we can't erase $z_4\dashto z_2$ without losing
some of $z_3\dashto z_4$; it's necessary to erase only part of one line.
One way to solve the problem is to do the following, after defining the
points and picking up the pen as before:

>
@draw@ $z_3\dashto z_4$; \ @draw@ $z_5\dashto z_6$;
^@cullit@; \ \pickup @pencircle@ scaled $1.6"pt"$;
^@undraw@ $z_7\dashto {1\over2}[z_7,z_5]$; \
@undraw@ $z_2\dashto {1\over2}[z_2,z_4]$;
@cullit@; \ \pickup @pencircle@ scaled $.4"pt"$;
@draw@ $z_3\dashto z_1\dashto z_2\dashto z_4$; \
@draw@ $z_5\dashto z_7\dashto z_8\dashto z_6$;
@for@ $k=1$ @upto@ 4: \ @draw@ $z[k]\dashto z[k+4]$; \ @endfor@.

(Note that it would not be quite enough to erase only from $z_7$ to
${1\over3}[z_7,z_5]$!)
It's also possible to solve this problem without partial erasing, if we
use additional features of METAFONT\ that haven't been explained yet. Let's
consider only the job of drawing $z_7\dashto z_5\dashto z_6$ and
$z_3\dashto z_4\dashto z_2$, since the other eight lines can easily be
added later. Alternative Solution 1 uses picture operations:

>
@pen@ "eraser"; \ $"eraser"=@pencircle@$ scaled $1.6"pt"$;
@draw@ $z_3\dashto z_4$; \
@erase@ @draw@ $z_7\dashto z_5$ ^@withpen@ "eraser"; \
@draw@ $z_7\dashto z_5$;
@picture@ "savedpicture"; \ $"savedpicture"="currentpicture"$; \ ^@clearit@;
@draw@ $z_6\dashto z_5$; \
@erase@ @draw@ $z_2\dashto z_4$ ^@withpen@ "eraser"; \
@draw@ $z_2\dashto z_4$;
^@addto@ "currentpicture" @also@ "savedpicture".

Alternative Solution 2 is trickier, but still instructive; it uses
'^@withweight@' options and the fact that @draw@ does not increase any
pixel values by more than the stated weight when the path is a straight
line:

>
@draw@ $z_3\dashto z_4$; \
^@undraw@ $z_7\dashto z_5$ @withpen@ "eraser";
@draw@ $z_7\dashto z_5$ @withweight@ 2; \
^@cullit@ @withweight@ 2;
@draw@ $z_6\dashto z_5$; \
^@undraw@ $z_2\dashto z_4$ @withpen@ "eraser";
@draw@ $z_2\dashto z_4$ @withweight@ 2;

(These alternative solutions were suggested by Bruce .)

**[Dangerous Bend]** exercise Write a METAFONT\ program to produce the symbol
'{\manual\bicentennial}'. \ [*Hints:* The character is $10\pt$
wide, $7\pt$ high, and $2\pt$ deep. The starlike path can be defined by
five points connected by "tense" lines as follows:

>
@pair@ "center"; \ $"center"=(.5w,2"pt")$;
@numeric@ "radius"; \ $"radius"=5"pt"$;
@for@ $k=0$ @upto@ 4: \ $z[k]="center"+("radius",0)$
$(90+{360\over5}k)$; \ @endfor@
@def@ :: = $\to\tension 5\to$ @enddef@;
@path@ "star"; \ $"star"=z_0::z_2::z_4::z_1::z_3::\cycle$;

You probably want to work with of ^"star" instead of drawing the
whole path at once, in order to give the illusion that the curves cross over
and under each other.]

#### Answer
Here's an analog of the first solution to the previous
exercise:

>
@beginchar@('"*"'$,10"pt"\0,7"pt"\0,2"pt"\0)$;
@pair@ "center"; \dots *as in the hint*
\pickup @pencircle@ scaled $.4"pt"$; \ @draw@ "star";
@cullit@; \ \pickup @pencircle@ scaled $1.6"pt"$;
@for@ $k=0$ @upto@ 4:
\ @undraw@ subpath$(k+.55,k+.7)$ of "star"; \ @endfor@
@cullit@; \ \pickup @pencircle@ scaled $.4"pt"$;
@for@ $k=0$ @upto@ 4: \ @draw@ subpath$(k+.47,k+.8)$ of "star"; \ @endfor@
@labels@$(0,1,2,3,4)$; \ @endchar@.

However, as in the previous case, there's an Alternate Solution 1
by Bruce that is preferable because it doesn't depend
on magic constants like .55 and .47:

>
@beginchar@ $\ldots$ *as above* $\ldots$ scaled $.4"pt"$;
@picture@ "savedpicture"; \ $"savedpicture"=@nullpicture@$;
@pen@ "eraser"; \ $"eraser":=@pencircle@$ scaled $1.6"pt"$;
@for@ $k=0$ @upto@ 4:
\indent @draw@ subpath$(k,k+1)$ of "star"; @cullit@;
\indent @undraw@ subpath$(k+2,k+3)$ of "star" @withpen@ "eraser"; @cullit@;
\indent @addto@ "savedpicture" @also@ "currentpicture"; @clearit@; @endfor@
$"currentpicture":="savedpicture"$; \ @labels@$(0,1,2,3,4)$; \ @endchar@.

**[Dangerous Bend]** exercise What does the command '@fill@ "star"' do, if "star" is the
path defined above?

#### Answer
It increases pixel values by 1 in the five lobes of the star, and by 2
in the central pentagon-like region.

\decreasehsize 6pc

**[Dangerous Bend]** exercise Devise a called '^@overdraw@' such that the command
\rightfig 13aa (50pt x 100pt) ^11pt
'@overdraw@ $c$' will erase the inside of region $c$ and will then draw the
boundary of $c$ with the currently-picked-up pen, assuming that $c$ is a
cyclic path that doesn't intersect itself. \ (Your macro could be used, for
example, in the program

>
@path@ $S$; \ $S=((0,1)\to(2,0)\to(4,2)\to$
\indent$(2,5.5)\to(0,8)\to(2,10)\to(3.5,9))$ scaled $9"pt"$;
@for@ $k=0$ @upto@ 35: @overdraw@ ^"fullcircle" scaled 3"mm"
\indent shifted $k/35\ast \mathoplength S$ of $S$;
@endfor@

to create the curious shown here.)

#### Answer
@def@ @overdraw@ @expr@ $c$ = @erase@ @fill@ $c$; @draw@ $c$ @enddef@.

\restorehsize

**[Double Dangerous Bend]** exercise The Watchband Corporation has a logo that
looks like this:
\displayfig 13bb (.5in)
Explain how to produce it (or something very similar) with METAFONT\!.

#### Answer
First we need to generalize the ^@overdraw@ macro of the previous
exercise so that it applies to arbitrary cycles $c$, even those that are
self-intersecting:

>
@def@ @overdraw@ @expr@ $c$ = ^@begingroup@ @save@ "region";
\indent@picture@ "region"; $"region":=@nullpicture@$;
\indent^@interim@ $"turningcheck":=0$; ^@addto@ "region" @contour@ $c$;
\indent^@cull@ "region" @dropping@ $(0,0)$;
\indent^@cullit@; @addto@ "currentpicture" ^@also@ $-"region"$; @cullit@;
\indent@draw@ $c$ ^@endgroup@ @enddef@;

(This code uses operations defined later in this chapter; it erases the
"region" of pixels that would be made nonzero by the command '@fill@ $c$'.)
\ The watchband is now formed by overdrawing its links, one at a time,
doing first the ones that are underneath:

>
@beginchar@$('"M"',1.25"in"\0,.5"in"\0,0)$; \
\pickup @pencircle@ scaled .4"pt";
$z_1=(20,-13)$; \ $z_2=(30,-6)$; \ $z_3=(20,1)$; \ $z_4=(4,-7)$;
\indent $z_5=(-12,-13)$; \ $z_6=(-24,-4)$; \ $z_7=(-15,6)$;
@path@ $M$; $M=("origin"\to z_1\to z_2\to z_3\to z_4\to z_5\to z_6\to z_7\to$
\indent$"origin"\to -z_7\to -z_6\to -z_5\to -z_4\to -z_3\to -z_2\to -z_1\to\cycle)$
^^"origin" \indent\indent scaled $(h/26)$ shifted $(.5w,.5h)$;
@def@ @link@(@expr@ $n$) =
\indent @overdraw@ subpath ${1\over3}(n,n+1)$ of $M\;\dashto$
\indent\indent subpath ${1\over3}(n+25,n+24)$ of $M\;\dashto\;\cycle\;$
@enddef@;
@for@ $k=1$ @upto@ 12: @link@$(k+11)$; @link@$(12-k)$; @endfor@
@endchar@;

**[Dangerous Bend]** Chapter 7 points out that variables can be of type '^@picture@',
and Chapter 8 mentions that expressions can be of type '@picture@', but
we still haven't seen any examples of picture variables or picture
expressions. Plain METAFONT\ keeps the currently-worked-on picture in a
picture variable called ^"currentpicture", and you can copy it by
equating it to a picture variable of your own. For example, if you
say '@picture@ $v[\,]$' at the beginning of your program, you can write
equations like

>
$v_1="currentpicture"$;

this makes $v_1$ equal to the picture that has been drawn so far; i.e.,
it gives $v_1$ the same array of pixel values that "currentpicture" now has.

\def\dbend{{\manual}}

**[Dangerous Bend]** Pictures can be added or subtracted; for example, $v_1+v_2$

stands for the picture whose pixel values are the sums of the pixel
values of $v_1$ and $v_2$. The " " sign that
heads this paragraph was made by substituting the following code for
the '@endchar@' in the program at the end of Chapter 12:

>
@picture@ "dbend"; \ $"dbend"="currentpicture"$;
@endchar@; \ \% end of the normal dangerous bend sign
@beginchar@$(0,25u\0,"h\_height"\0+"border"\0,0)$;
@fill@ $(0,-11"pt")\dashto(w,-11"pt")\dashto(w,h)\dashto(0,h)\dashto\cycle$;
$"currentpicture":="currentpicture"-"dbend"$;
@endchar@;\ \% end of the reversed dangerous bend sign

The pixel values in "dbend" are all zero or more;
thus the pixels with a positive value, after "dbend" has been subtracted from
a filled rectangle, will be those that are inside the rectangle
but zero in "dbend".

**[Dangerous Bend]** We will see in Chapter 15 that pictures can also be shifted,
reflected, and rotated by multiples of $90^\circ$. For example,
the statement '$"currentpicture":="currentpicture"$ shifted 3"right"'
shifts the entire current picture three pixels to the right.

**[Dangerous Bend]** There's a "constant" picture called ^@nullpicture@, whose pixel
values are all zero;
plain METAFONT\ defines '^@clearit@' to be an abbreviation for the
assignment '$"currentpicture":=@nullpicture@$'. The current picture is
cleared automatically by every ^@beginchar@ and ^@mode\_setup@ command,
so you usually don't have to say '@clearit@' in your own programs.

**[Dangerous Bend]** Here's the formal syntax for picture expressions. Although METAFONT\ has
comparatively few built-in operations that deal with entire pictures,
the operations that do exist have the same syntax as the similar operations
we have seen applied to numbers and pairs.
\beginsyntax
<picture primary>\is<picture variable>
\alt[nullpicture]
\alt[(]<picture expression>[)]
\alt<plus or minus><picture primary>
<picture secondary>\is<picture primary>
\alt<picture secondary><transformer>
<picture tertiary>\is<picture secondary>
\alt<picture tertiary><plus or minus><picture secondary>
<picture expression>\is<picture tertiary>
\endsyntax

**[Dangerous Bend]** The "total weight" of a picture is the sum of all its pixel
values, divided by 65536; you can compute this numeric quantity by
saying

>
*picture primary*.

METAFONT\ divides by 65536 in order to avoid overflow in case of huge pictures.
If the totalweight function returns a number whose absolute
value is less than .5, as it almost always is, you can safely divide that number
by ^"epsilon" to obtain the integer sum of all pixel values
(since $"epsilon"=1/65536$).

**[Dangerous Bend]** Let's turn to the computer again and try to evaluate some simple
picture expressions interactively, using the general routine 'expr.mf'
of Chapter 8. When METAFONT\ says "gimme'', you can type

"'

hide(fill unitsquare) currentpicture

"'

and the machine will respond as follows:

"'

>> Edge structure at line 5:
row 0: 0+ 1- "

"'

What does this mean? Well, '^@hide@' is plain METAFONT's sneaky way to insert
a command or sequence of commands into the middle of an expression; such
commands are executed before the rest of the expression is looked at. In
this case the command '@fill@ "unitsquare"' sets one pixel value of the
current picture to 1, because ^"unitsquare" is plain METAFONT's abbreviation
for the path $(0,0)\dashto(1,0)\dashto(1,1)\dashto(0,1)\dashto\cycle$. The
value of "currentpicture" is displayed as "row' '0:' '0+' '1-'', because
this means
"in row 0, the pixel value increases at $x=0$ and decreases at $x=1$."

**[Dangerous Bend]** METAFONT\ represents pictures internally by remembering only the vertical
where pixel values change. For example, the picture just displayed
has just two edges, both in row 0, i.e., both in the row between $y$ coordinates
0 and 1. \ (Row $k$ contains vertical edges whose $x$ coordinates are integers
and whose $y$ coordinates run between $k$ and $k+1$.) \ The fact that edges
are represented, rather than entire arrays of pixels, makes it possible for
METAFONT\ to operate efficiently at high resolutions, because the number of edges
in a picture is essentially proportional to the while the total
number of pixels is proportional to the resolution *squared*. A ten-fold
increase in resolution therefore calls for only a ten-fold (rather than a
hundred-fold) increase in memory space and execution time.

{#1\kern\pixcorr#2}{#3\kern\pixcorr#4}}}

**[Double Dangerous Bend]** Continuing our computer experiments, let's declare a picture variable
and fill a few more pixels:

"'

hide(picture V; fill unitsquare scaled 2; V=currentpicture) V

"'

The resulting picture has pixel values $\pixpat1121\,$,
and its edges are shown thus:

"'

>> Edge structure at line 5:
row 1: 0+ 2- "
row 0: 0+ 2- 0+ 1- "

"'

If we now type "-V'', the result is similar but with the signs changed:

"'

>> Edge structure at line 5:
row 1: 0- 2+ "
row 0: 0- 2+ 0- 1+ "

"'

(You should be doing the experiments as you read this.) \ A more interesting
picture transformation occurs if we ask for "V' 'rotated-90''; the picture
$\pixpat2111$ appears below the baseline, hence the following edges are shown:

"'

>> Edge structure at line 5:
row -1: " 0++ 1- 2-
row -2: " 0+ 2-

"'

Here '' denotes an edge where the weight increases by 2. The edges appear
*after* s '\|' in this case, while they appeared
*before* vertical lines in the previous examples; this means that METAFONT\
has sorted the edges by their $x$ coordinates. Each @fill@ or @draw@ instruction
contributes new edges to a picture, and unsorted edges accumulate until
METAFONT\ needs to look at them in left-to-right order. \ (Type

"'

V rotated-90 rotated 90

"'

to see what $V$ itself looks like when its edges have been sorted.) \ The
expression

"'

V + V rotated 90 shifted 2right

"'

produces an edge structure with both sorted and unsorted edges:

"'

>> Edge structure at line 5:
row 1: 0+ 2- " 0+ 2-
row 0: 0+ 2- 0+ 1- " 0+ 1+ 2--

"'

In general, addition of pictures is accomplished by simply combining the
unsorted and sorted edges of each row separately.

**[Double Dangerous Bend]** exercise Guess what will happen if you type "hide(cullit)'
'currentpicture'' now; and verify your guess by actually doing the experiment.

#### Answer
The pixel pattern $\pixpat1121$ is culled to $\pixpat1111\,$,
and METAFONT\ needs to sort the edges as it does this; so the result is simply

"'

row 1: " 0+ 2-
row 0: " 0+ 2-

"'

**[Double Dangerous Bend]** exercise Guess (and verify) what will happen when you type the
expression

"'

(V + V + V rotated 90 shifted 2right
- V rotated-90 shifted 2up) rotated 90.

"'

[You must type this monstrous formula all on one line, even though it's too
long to fit on a single line in this book.]

#### Answer
The pixel pattern is $\pixpat1121+\pixpat1121+\pixpat1112-\pixpat2111
=\pixpat1243$ before the final rotation, with the reference point at the
lower left corner of the 4; after rotation it is $\pixpat2314\,$, with the
reference point at the lower *right* corner of the 4. Rotation causes
METAFONT\ to sort the edges, but the transition values per edge are never
more than $\pm3$. You weren't expected to know about this limit of $\pm3$,
but it accounts for what is actually reported:

"'

row 1: " -2++ -1+ 0---
row 0: " -2+ -1+++ 0--- 0-

"'

**[Double Dangerous Bend]** If you ask for "V' 'rotated' '45'', METAFONT\ will complain that
$45^\circ$ rotation is too hard. \ (Try it.) \ After all, square pixels
can't be unless the angle of rotation is a multiple of $90^\circ$.
On the other hand, "V' 'scaled-1'' does work; you get

"'

>> Edge structure at line 5:
row -1: 0- -2+ 0- -1+ "
row -2: 0- -2+ "

"'

**[Double Dangerous Bend]** exercise Why is "V' 'scaled-1'' different from "-V''?

#### Answer
"V' 'scaled-1'' should be the same as "V' 'rotated' '180'',
because transformations apply to coordinates rather than to pixel values.
\ (Note, incidentally, that the reflections "V' ' and
"V' ' both work, and that "V' 'scaled-1'' is the same as
"V' 'xscaled-1' 'yscaled-1''.)

**[Double Dangerous Bend]** exercise Experiment with "V' 'shifted' '(1.5,3.14159)'' and
explain what happens.

#### Answer
The result is the same as "V' 'shifted' '(2,3)''; the coordinates
of a shift are rounded to the nearest integers when a picture is being shifted.

**[Double Dangerous Bend]** exercise Guess and verify the result of "V' 'scaled' '2''.

#### Answer
'row 3: 0+ 4- '\|break
'row 2: 0+ 4- '\|break
'row 1: 0+ 4- 0+ 2- '\|break
'row 0: 0+ 4- 0+ 2- '\|\nobreak

(Scaling of pictures must be by an integer.)

**[Double Dangerous Bend]** exercise Why does the machine always speak of an
"at' 'line' '5''?

#### Answer
METAFONT\ is currently executing instructions after having read
as far as line 5 of the file 'expr.mf'.

**[Double Dangerous Bend]** That completes our computer experiments. But before you log off,
you might want to try typing "totalweight V/epsilon'', just to verify
that the sum of all pixel values in $V$ is 5.

**[Dangerous Bend]** The commands we have discussed so far in this chapter---@fill@,
@draw@, @filldraw@, @unfill@, etc.---are not really primitives of METAFONT;
they are macros of plain METAFONT\!, defined in Appendix B. Let's look now
at the low-level operations on pictures that METAFONT\ actually performs
behind the scenes. Here is the syntax:
\beginsyntax
<picture command>\is<addto command>\alt<cull command>
<addto command>\is[addto]<picture variable>[also]<picture expression>
\alt[addto]<picture variable>[contour]<path expression><with list>
\alt[addto]<picture variable>[doublepath]<path expression><with list>
<with list>\is<empty>\alt<with list><with clause>
<with clause>\is[withpen]<pen expression>
\alt[withweight]<numeric expression>
<cull command>\is[cull]<picture variable><keep or drop><pair expression>
\alt<cull command>[withweight]<numeric expression>
<keep or drop>\is[keeping]\alt[dropping]
\endsyntax
The *picture variable* in these commands should contain a known picture;
the command modifies that picture, and assigns the resulting new value
to the variable.

**[Dangerous Bend]** The first form of *addto command*, '@addto@ $V$ @also@ $P$',
has essentially the same meaning as '$V:=V+P$'. But the @addto@ statement
is more efficient, because it destroys the old value of $V$ as it adds $P$;
this saves both time and space. Earlier in this chapter we discussed
the , which was said to have been
formed by the statement '$"currentpicture":="currentpicture"-"dbend"$'.
That was a little white lie; the actual command was
'@addto@ "currentpicture" @also@ $-"dbend"$'.

**[Dangerous Bend]** The details of the other forms of '@addto@' are slightly more
complex, but (informally) they work like this, when $V="currentpicture"$
and $q=$^"currentpen":

>
Plain METAFONT&Corresponding METAFONT\ primitives

^@fill@ $c$&@addto@ $V$ @contour@ $c$
^@unfill@ $c$&@addto@ $V$ @contour@ $c$ @withweight@ $-1$
^@draw@ $p$&@addto@ $V$ @doublepath@ $p$ @withpen@ $q$
^@undraw@ $p$&@addto@ $V$ @doublepath@ $p$ @withpen@ $q$ @withweight@ $-1$
^@filldraw@ $c$&@addto@ $V$ @contour@ $c$ @withpen@ $q$
^@unfilldraw@ $c$&@addto@ $V$ @contour@ $c$ @withpen@ $q$ @withweight@ $-1$

**[Double Dangerous Bend]** The second form of *addto command* is '@addto@ $V$ @contour@ $p$',
followed by optional clauses that say either '@withpen@ $q$' or
'@withweight@ $w$'. In this case $p$ must be a cyclic path; each pen $q$
must be known; and each weight $w$ must be either $-3$, $-2$, $-1$, $+1$,
$+2$, or $+3$, when rounded to the nearest integer. If more than one pen or
weight is given, the last specification overrides all previous ones. If no
pen is given, the pen is assumed to be '@nullpen@'; if no weight is given,
the weight is assumed to be $+1$. Thus, the second form of *addto command*
basically identifies a picture variable $V$, a cyclic path $p$, a pen $q$,
and a weight $w$; and it has the following meaning, assuming that
"turningcheck" is $\le0$: If $q$ is the null pen, path $p$ is digitized
and each pixel value is increased by $(j-k)w$, where $j$ and $k$ are the
respective numbers of downward and upward path edges lying to the left
of the pixel (as explained earlier in this chapter). If $q$ is not the
null pen, the action is basically the same except that $p$ is converted to
another path that "s" $p$ with respect to the shape of $q$;
this modified path is digitized and filled as before. \ (The modified path
may cross itself in unusual ways, producing strange squirts of ink as
illustrated earlier. But it will be well behaved if path $p$ defines a
region, i.e., if a car that drives counterclockwise
around $p$ never turns toward the right at any time.)

**[Double Dangerous Bend]** If $"turningcheck">0$ when an '$@addto@\ldots@contour@$' command
^^"turningcheck" is being performed, the action is the same as just
described, provided that path $p$ has a positive .
However, if $p$'s turning number is negative, the action depends on
whether or not pen $q$ is simple or complex; a complex pen is one whose
boundary contains at least two points. If the turning number is negative
and the pen is simple, the weight $w$ is changed to $-w$. If the turning
number is negative and the pen is complex, you get an error message about
a "." Finally, if the turning number is zero, you get
an error message about a "," unless the pen is simple and
$"turningcheck"\le1$. Plain METAFONT\ sets $"turningcheck":=2$; the ^@filldraw@
macro in Appendix B avoids the "backwards path" error by explicitly
reversing a path whose turning number is negative.

**[Dangerous Bend]** We mentioned that the command '@fill@ $(0,2)\dashto(4,2)\dashto
(4,4)\dashto(2,4)\dashto(2,0)\dashto(0,0)\dashto\cycle$' causes METAFONT\
to complain about a strange path; let's take a closer look at the
error message that you get:

"'

> 0 ENE 1 NNE 2 (NNW WNW) WSW 3 SSW 4 WSW 5 (WNW NNW) NNE 0
! Strange path (turning number is zero).

"'

What does this mean? The numbers represent "^time" on the cyclic path,
from the starting point at time 0, to the next key point at time 1,
and so on, finally returning to the starting point. Code names like
'' stand for like "East by North East";
METAFONT\ decides in which of eight "" each part of a path travels,
and 'ENE' stands for all directions between the angles $0^\circ$
and $45^\circ$, inclusive. Thus, this particular strange path starts in
octant 'ENE' at time 0, then it turns to octant after time 1.
An octant name is parenthesized when the path turns through that octant
without moving; thus, for example, octants and are bypassed
on the way to octant . It's possible to compute the turning number
from the given sequence of octants; therefore, if you don't think
your path is really strange, the abbreviated octant codes should reveal
where METAFONT\ has decided to take an unexpected turn. \ (Chapter 27 explains
more about strange paths.)

**[Double Dangerous Bend]** The third form of *addto command* is '@addto@ $V$ @doublepath@ $p$',
followed by optional clauses that define a pen $q$ and a weight $w$ as in
the second case. If $p$ is not a cyclic path, this case reduces to the
second case, with $p$ replaced by the doubled-up path
'$p\mathbin{\&}\mathopreversep \mathbin{\&}\cycle$' (unless $p$
consists of only a single point, when the new path is simply
'$p\to\cycle$'). On the other hand if $p$ is a cyclic
path, this case reduces to *two* addto commands of the second type,
in one of which $p$ is reversed; "turningcheck" is ignored during both of
those commands.

**[Dangerous Bend]** An anomalous result may occur in the statement '@draw@ $p$'
or, more generally, in '@addto@ $V$ @doublepath@ $p$ @withpen@ $q$' when
$p$ is a very small cyclic path and the current pen $q$ is very large: Pixels
that would be covered by the pen regardless of where it is placed on $p$
might retain their original value. If this unusual circumstance hits you,
the cure is simply to include the additional statement '@draw@ $z$' or
'@addto@ $V$ @doublepath@ $z$ @withpen@ $q$', where $z$ is any point
of $p$, since this will cover all of the potentially uncovered pixels.

**[Dangerous Bend]** The ^@cull@ command transforms a picture variable so that
all of its pixel values are either 0 or a specified weight $w$, where $w$ is
determined as in an @addto@ command. A pair of numbers $(a,b)$ is given,
where $a$ must be less than or equal to $b$. To cull "@keeping@ $(a,b)$"
means that each new pixel value is $w$ if and only if the corresponding
old pixel value $v$ was included in the range $a\le v\le b$; to cull
"@dropping@ $(a,b)$" means that each new pixel value is $w$ if and only
if the corresponding old pixel value $v$ was *not* in that range.
Thus, for example, '^@cullit@' is an abbreviation for

> \belowdisplayskip by -4pt
@cull@ "currentpicture" @keeping@ $(1,"infinity")$

or for

> \abovedisplayskip by -4pt
@cull@ "currentpicture" @dropping@ $(-"infinity",0)$

(which both mean the same thing). A more complicated example is

>
@cull@ $V_5$ @dropping@ $(-3,2)$ @withweight@ $-2$;

this changes the pixel values of $V_5$ to $-2$ if they were $-4$ or less,
or if they were 3 or more; pixel values between $-3$ and $+2$, inclusive,
are zeroed.

**[Dangerous Bend]** A cull command must not change pixel values from zero to nonzero.
For example, METAFONT\ doesn't let you say '@cull@ $V_1$ @keeping@ $(0,0)$',
since that would give a value of 1 to infinitely many pixels.

**[Dangerous Bend]** exercise What is the effect of the following sequence of commands?

>
@picture@ $V[\,]$;
$V_1=V_2="currentpicture"$;
@cull@ $V_1$ @dropping@ $(0,0)$;
@cull@ $V_2$ @dropping@ $(-1,1)$;
$"currentpicture":=V_1-V_2$;

#### Answer
The pixel values of "currentpicture" become 1 if they were $\pm1$,
otherwise they become 0.

**[Dangerous Bend]** exercise Given two picture variables $V_1$ and $V_2$, all of whose
pixel values are known to be either 0 or 1, explain how to replace $V_1$ by
(a) $V_1\cap V_2$; \ (b) $V_1\cup V_2$; \ (c) $V_1\oplus V_2$. \ [The
$V_1\cap V_2$ has 1's where $V_1$ and $V_2$ both are 1;
the $V_1\cup V_2$ has 0's where $V_1$ and $V_2$ both are 0;
the or
$V_1\oplus V_2$ has 1's where $V_1$ and $V_2$ are unequal.]

#### Answer
(a) @addto@ $V_1$ @also@ $V_2$; @cull@ $V_1$
@keeping@ $(2,2)$. \ (b) Same, but cull keeping $(1,2)$.
\ (c) Same, but cull keeping $(1,1)$.

**[Double Dangerous Bend]** exercise Explain how to test whether or not two picture variables
are equal.

#### Answer
Subtract one from the other, and cull the result dropping $(0,0)$;
then test to see if the total weight is zero.

**[Double Dangerous Bend]** exercise Look at the definitions of @fill@, @draw@, etc., in
Appendix B and determine the effect of the following statements:

>
\llapa) @draw@ $p$ @withpen@ $q$;
\llapb) @draw@ $p$ @withweight@ 3;
\llapc) @undraw@ $p$ @withweight@ $w$;
\llapd) @fill@ $c$ @withweight@ $-2$ @withpen@ $q$;
\llape) @erase@ @fill@ $c$ @withweight@ 2 @withpen@ "currentpen";
\llapf) @cullit@ @withweight@ 2.

#### Answer
(a) Same as '@draw@ $p$', but using $q$ instead of the
currently-picked-up pen. \ (b) Same effect as '@draw@ $p$; @draw@ $p$;
@draw@ $p$' (but faster). \ (c) Same as '@draw@ $p$ @withweight@ $w$',
because @undraw@'s '@withweight@ $-1$' is overridden.
\ (d) Same as '@unfilldraw@ $c$; @unfilldraw@ $c$',
but using $q$ instead of "currentpen".
\ (e) Same as '@erase@ @filldraw@ $c$', because the '@withweight@ 2' is
overridden. \ [Since @erase@ has culled all weights to 0 or 1, there's
no need to "doubly erase."]
\ (f) Same effect as '@cullit@; @addto@ "currentpicture" @also@
"currentpicture"' (but faster).

**[Double Dangerous Bend]** exercise Devise a ^@safefill@ macro such that '@safefill@ $c$' increases
the pixel values of "currentpicture" by 1 in all pixels whose value would
be changed by the command '@fill@ $c$'. \ (Unlike @fill@, the @safefill@ command
never stops with a "" error; furthermore, it never increases
a pixel value by more than 1, nor does it decrease any pixel values, even
when the cycle $c$ is quite wild.)

#### Answer
@vardef@ @safefill@ @expr@ $c$ $=$ ^@save@ "region";break
@picture@ "region"; $"region"=@nullpicture@$;break
^@interim@ ^"turningcheck"$:=0$;break
@addto@ "region" @contour@ $c$; \
@cull@ "region" @dropping@ $(0,0)$;break
@addto@ "currentpicture" @also@ "region" @enddef@.

**[Double Dangerous Bend]** exercise Explain how to replace a character by its "":
All black pixels whose four closest neighbors are also
black should be changed to white, because they are in the interior.
\ (Diagonally adjacent neighbors don't count.)

#### Answer
@cull@ "currentpicture" @keeping@ $(1,"infinity")$;break
@picture@ $v$; \ $v:="currentpicture"$;break
@cull@ "currentpicture" @keeping@ $(1,1)$ @withweight@ 3;break
@addto@ "currentpicture" @also@
$v\;-\;v$ shifted "right"break
$-\;v$ shifted "left"
$-\;v$ shifted "up"
$-\;v$ shifted "down";break
@cull@ "currentpicture" @keeping@ $(1,4)$.

**[Double Dangerous Bend]** exercise In John 's "Game of ," pixels are said to
be either alive or dead. Each pixel is in contact with eight neighbors.
The live pixels in the $(n+1)$st generation are those who were dead and
had exactly three live neighbors in the $n$th generation, or those
who were alive and had exactly two or three live neighbors in the $n$th
generation. Write a short METAFONT\ program that displays successive
generations on your screen.

#### Answer
(We assume that "currentpicture" initially has some configuration
in which all pixel values are zero or one; one means "alive.")

>
@picture@ $v$; @def@ $c$ $=$ "currentpicture" @enddef@;
@forever@: \ $v:=c$; \ @showit@;
@addto@ $c$ @also@ $c$ shifted "left" $+$ $c$ shifted "right";
@addto@ $c$ @also@ $c$ shifted "up" $+$ $c$ shifted "down";
@addto@ $c$ @also@ $c-v$; \ @cull@ $c$ @keeping@ $(5,7)$; \ @endfor@.

(It is wise not to waste too much computer time watching this program.)

\endchapter

Blot out, correct, insert, refine,
Enlarge, diminish, interline;
Be mindful, when Invention fails,
To scratch your Head, and bite your Nails.

> --- JONATHAN , *On Poetry: A Rapsody* (1733)

The understanding that can be gained from computer drawings
is more valuable than mere production.

> --- IVAN E. , *Sketchpad* (1963)


# Chapter 14. Paths

The of regions to be filled, and the of
moving pens, are "" that can be specified by the general methods
introduced in Chapter 3. METAFONT\ allows variables and expressions to be of
type @path@, so that a designer can build new paths from old ones in many
ways. Our purpose in this chapter will be to complete what Chapter 3
began; we shall look first at some special features of plain METAFONT\ that
facilitate the creation of paths, then we shall go into the details of
everything that METAFONT\ knows about pathmaking.

A few handy paths have been predefined in Appendix B as part of plain METAFONT\!,
because they turn out to be useful in a variety of applications. For example,
^"quartercircle" is a path that represents one-fourth of a of
diameter 1; it runs from point $(0.5,0)$ to point $(0,0.5)$.
The METAFONT\ program

>
@beginchar@('"a"'$,5"pt"\0,5"pt"\0,0)$;
@pickup@ @pencircle@ scaled $(.4"pt"+"blacker")$;
@draw@ "quartercircle" scaled 10"pt"; \ @endchar@;

therefore produces the character '{\manual\circa}' in position
"a'' of a font.

### Exercise

Write a program that puts a *filled* quarter-circle
'{\manual\circb}'\ into font position "b''.

#### Answer
@beginchar@('"b"'$,5"pt"\0,5"pt"\0,0)$;break
@fill@ $((0,0)\dashto"quartercircle"\dashtocycle)$
scaled 10"pt"; \ @endchar@.

### Exercise

Why are the '{\manual\circa}' and '{\manual\circb}'\
characters of these examples only $5\,$pt wide and $5\,$pt high, although
they are made with the path '"quartercircle" scaled 10"pt"'?

#### Answer
A "quartercircle" corresponds to a circle whose diameter
is 1; the radius is $1\over2$.

**[Dangerous Bend]** exercise
Use a *rotated* quarter-circle to produce '{\manual\circc}'
in font position "c''.

#### Answer
@beginchar@('"c"'$,5"pt"\0,5"pt"\0,0)$;break
@pickup@ @pencircle@ scaled $(.4"pt"+"blacker")$;break
@draw@ "quartercircle" rotated 90 scaled 10"pt" shifted $(5"pt",0)$;
\ @endchar@.

**[Dangerous Bend]** exercise
Use "quartercircle" to produce '{\manual\circd}'
in font position "d''.

#### Answer
@beginchar@('"d"'$,5"pt"\0\astsqrt2,5"pt"\0,0)$;break
@pickup@ @pencircle@ scaled $(.4"pt"+"blacker")$;break
@draw@ $((0,0)\dashto"quartercircle"\dashtocycle)$
rotated 45 scaled 10"pt" shifted $(.5w,0)$;break
@endchar@.

Plain METAFONT\ also provides a path called ^"halfcircle" that gives you
'{\manual\circc\circa}'; this path is actually made from two
quarter-circles, by defining

>
"halfcircle" $=$ "quartercircle" \& $"quartercircle"\,rotated\,90$.

And of course there's also ^"fullcircle", a complete circle of unit diameter:

>
"fullcircle" $=$ "halfcircle" \& $"halfcircle"\,rotated\,180$ \& cycle.

You can draw a circle of diameter $D$ centered at $(x,y)$ by saying

>
@draw@ "fullcircle" scaled $D$ shifted $(x,y)$;

similarly,\ '@draw@ "fullcircle"
xscaled $A$ yscaled $B$'
yields an with axes $A$ and $B$.

Besides circles and parts of circles, there's also a standard square path
called "unitsquare"; this is a cycle that runs from $(0,0)$ to $(1,0)$
to $(1,1)$ to $(0,1)$ and back to $(0,0)$. For example, the command
'@fill@ "unitsquare"' adds 1 to a single pixel value, as discussed in
the previous chapter.

### Exercise
Use "fullcircle" and "unitsquare" to produce the characters
'{\manual\circe}' and '{\manual\circf}' in font positions "e''
and "f'', respectively. These characters should be $10\,$pt wide
and $10\,$pt tall, and their centers should be $2.5\,$pt above
the baseline.

#### Answer
@beginchar@('"e"'$,10"pt"\0,7.5"pt"\0,2.5"pt"\0)$;break
@pickup@ @pencircle@ scaled $(.4"pt"+"blacker")$;break
@for@ $D=.2w,.6w,w$: \
@draw@ "fullcircle" scaled $D$ shifted $(.5w,.5[-d,h])$;break
@endfor@ @endchar@.

The program for '{\manual\circf}' is similar, but '"fullcircle"
scaled $D$' is replaced by

>
"unitsquare" shifted $-(.5,.5)$ rotated 45 scaled $(D/sqrt2)$.

\hrule

{\figbox14a{220\apspix}{690\apspix}
{=18pc \def\\ indent=0pt

\obeylines
@path@ $"branch"[\,]$, "trunk";
\\
$"branch"_1= "flex"((0,660),(-9,633),(-22,610))$
\& "flex"$((-22,610),(-3,622),(17,617))$
\& "flex"$((17,617),(7,637),(0,660))$ \& cycle;
\\
$"branch"_2="flex"((30,570),(10,590),(-1,616))$
\& "flex"$((-1,616),(-11,592),(-29,576),(-32,562))$
\& "flex"$((-32,562),(-10,577),(30,570))$ \& cycle;
\\
$"branch"_3="flex"((-1,570),(-17,550),(-40,535))$
\& "flex"$((-40,535),(-45,510),(-60,477))$
\& "flex"$((-60,477),(-20,510),(40,512))$
\& "flex"$((40,512),(31,532),(8,550),(-1,570))$ \& cycle;
\\
$"branch"_4="flex"((0,509),(-14,492),(-32,481))$
\& "flex"$((-32,481),(-42,455),(-62,430))$
\& "flex"$((-62,430),(-20,450),(42,448))$
\& "flex"$((42,448),(38,465),(4,493),(0,509))$ \& cycle;
\\
$"branch"_5="flex"((-22,470),(-23,435),(-44,410))$
\& "flex"$((-44,410),(-10,421),(35,420))$
\& "flex"$((35,420),(15,455),(-22,470))$ \& cycle;
\\
$"branch"_6="flex"((18,375),(9,396),(5,420))$
\& "flex"$((5,420),(-5,410),(-50,375),(-50,350))$
\& "flex"$((-50,350),(-25,375),(18,375))$ \& cycle;
\\
$"branch"_7="flex"((0,400),(-13,373),(-30,350))$
\& "flex"$((-30,350),(0,358),(30,350))$
\& "flex"$((30,350),(13,373),(0,400))$ \& cycle;
\\
$"branch"_8="flex"((50,275),(45,310),(3,360))$
\& "flex"$((3,360),(-20,330),(-70,300),(-100,266))$
\& "flex"$((-100,266),(-75,278),(-60,266))$
\& "flex"$((-60,266),(0,310),(50,275))$ \& cycle;
\\
$"branch"_9="flex"((10,333),(-15,290),(-43,256))$
\& "flex"$((-43,256),(8,262),(58,245))$
\& "flex"$((58,245),(34,275),(10,333))$ \& cycle;
\\
$"branch"_10="flex"((8,262),(-21,249),(-55,240))$
\& "flex"$((-55,240),(-51,232),(-53,220))$
\& "flex"$((-53,220),(-28,229),(27,235))$
\& "flex"$((27,235),(16,246),(8,262))$ \& cycle;
\\
$"branch"_11="flex"((0,250),(-25,220),(-70,195))$
\& "flex"$((-70,195),(-78,180),(-90,170))$
\& "flex"$((-90,170),(-5,188),(74,183))$
\& "flex"$((74,183),(34,214),(0,250))$ \& cycle;
\\
$"branch"_12="flex"((8,215),(-35,175),(-72,155))$
\& "flex"$((-72,155),(-75,130),(-92,110),(-95,88))$
\& "flex"$((-95,88),(-65,117),(-54,104))$
\& "flex"$((-54,104),(10,151),(35,142))$
$\to"flex"((42,130),(60,123),(76,124))$
\& "flex"$((76,124),(62,146),(26,180),(8,215))$ \& cycle;
\\
$"trunk"=(0,660)\ddashto(-12,70)\to\{\curl 5\}(-28,-8)$
\& "flex"$((-28,-8),(-16,-4),(-10,-11))$
\& "flex"$((-10,-11),(0,-5),(14,-10))$
\& "flex"$((14,-10),(20,-6),(29,-11))$
\& $(29,-11)\{\curl 4\}\to(10,100)\ddashtocycle$;
}}

Sometimes it's necessary to draw rather complicated curves, and plain METAFONT\
provides a '^"flex"' operation that can simplify this task. The
construction '$"flex"(z_1,z_2,z_3)$' stands for the path
'$z_1\to z_2\{z_3-z_1\}\to z_3$',
and similarly '$"flex"(z_1,z_2,z_3,z_4)$' stands for
'$z_1\to z_2\{z_4-z_1\}\to z_3\{z_4-z_1\}\to z_4$'; in general

>
$"flex"(z_1,z_2,\ldots,z_n-1,z_n)$

is an abbreviation for the path

>
$z_1\to z_2\{z_n-z_1\}\to\;\cdots\;\to z_n-1\{z_n-z_1\}\to z_n$.

The idea is to specify two endpoints, $z_1$ and $z_n$, together with
one or more intermediate points where the path is traveling in the
same direction as the straight line from $z_1$ to $z_n$; these
intermediate points are easy to see on a typical curve, so they
are natural candidates for key points.

For example, the command

>
@fill@ \ $"flex"(z_1,z_2,z_3)$ \& $"flex"(z_3,z_4,z_5)$
\indent\& $"flex"(z_5,z_6,z_7)$ \& $"flex"(z_7,z_8,z_9,z_1)$ \& cycle

will fill the shape
\displayfig 14b (7pc)
after the points $z_1$, \dots, $z_9$ have been suitably defined. This
shape occurs as the fourth branch from the top of ","
a tree that is often used to symbolize . The thirteen
paths on the opposite page were defined by simply sketching the tree on
a piece of graph paper, then reading off approximate values of key
points "by eye" while typing the code into a computer. \ (A good radio
or television program helps to stave off boredom when you're typing
a bunch of data like this.) \ The entire
figure involves a total of 47 flexes, most of which are pretty mundane;
but $"branch"_12$ does contain an interesting subpath of the form

>
$"flex"(z_1,z_2,z_3)\to"flex"(z_4,z_5,z_6)$,

which is an abbreviation for

>
$z_1\to z_2\{z_3-z_1\}\to z_3\to z_4\to z_5\{z_6-z_4\}\to z_6$.

Since $z_3\ne z_4$ in this example, a smooth curve runs through all six
points, although two different flexes are involved.

\hangindent -1in \hangafter-2
Once the paths have been defined,
\rightfig 14aa (.5in x 1.25in) ^-8pt
it's easy to use them to make
symbols like the white-on-black medallion shown here:

>
@beginchar@('"T"'$,.5"in"\0,1.25"in"\0,0)$;
*Define the thirteen paths on the preceding pages*;
@fill@ "superellipse"$((w,.5h),(.5w,h),(0,.5h),(.5w,0),.8)$;
$"branch"_0="trunk"$;
@for@ $n=0$ @upto@ 12:
^@unfill@ $"branch"[n]$ shifted $(150,50)$ scaled $(w/300)$;
@endfor@ @endchar@;

The oval shape that encloses this tree is a ^"superellipse", which is
another special kind of path provided by plain METAFONT\!. To get a general
shape of this kind, you can write

>
"superellipse"$("right\_point","top\_point","left\_point","bottom\_point",
"superness")$

where '"superness"' controls the amount by which the curve differs from a
true . For example, here are four superellipses, drawn with varying
amounts of , using a
@pencircle@ xscaled 0.7"pt" yscaled 0.2"pt" rotated 30:
\displayfig 14c (150\apspix)
The "superness" should be between 0.5 (when you get a diamond) and 1.0
(when you get a square); values in the vicinity of 0.75 are usually preferred.
The zero symbol "0'' in this book's typewriter font was
drawn as a superellipse of superness $2\approx.707$, which
corresponds to a normal ellipse; the uppercase letter "O'' was
drawn with superness $2\approx.841$, to help distinguish it
from the zero. The ambiguous symbol '{\cmman0}' (which is not in the
font, but METAFONT\ can of course draw it) lies between these two extremes; its
superness is 0.77.

**[Double Dangerous Bend]** A mathematical superellipse satisfies the equation $\vert
x/a\vert^\beta+\vert y/b\vert^\beta=1$, for some exponent $\beta$. It has
extreme points $(\pm a,0)$ and $(0,\pm b)$, as well as the "corner"
points $(\pm\sigma a,\pm\sigma b)$, where $\sigma=2$ is the
superness. The tangent to the curve at $(\sigma a,\sigma b)$ runs in the
direction $(-a,b)$, hence it is parallel to a line from $(a,0)$ to
$(0,b)$. Gabriel invented the superellipse in 1818, and
Piet popularized the special case
$\beta=2.5$ [see Martin , *Mathematical
Carnival* (New York: Knopf, 1975), 240--254]; this special case
corresponds to a superness of $2\approx.7578582832552$. Plain METAFONT's
"superellipse" routine does not produce a perfect superellipse, nor does
^"fullcircle" yield a true circle, but the results are close enough for
practical purposes.

**[Double Dangerous Bend]** exercise Try "superellipse" with superness values less than 0.5
or greater than 1.0; explain why you get weird shapes in such cases.

#### Answer
There are inflection points, because there are no bounding triangles
for the '$\ldots$' operations in the "superellipse" macro of Appendix B,
unless $.5\le s\le1$.

Let's look now at the symbols that are used between key points, when we
specify a path. There are five such tokens in plain METAFONT:

>
$\to$&free curve;
$\ldots$&bounded curve;
$\dashto$&straight line;
$\ddashto$&"tense" line;
\&&splice.

In general, when you write '$z_0\to z_1\to*etc.*\to z_n-1\to z_n$',
METAFONT\ will compute the path of length $n$ that represents its idea of the
"most pleasing curve" through the given points $z_0$ through $z_n$.
The symbol '$\ldots$' is essentially the same as '$\to$', except
that it confines the path to a bounding triangle whenever possible, as
explained in Chapter 3. A straight line segment '$z_k-1\dashto z_k$'
usually causes the path to change course abruptly at $z_k-1$ and $z_k$.
By contrast, a segment specified by '$z_k-1\ddashto z_k$' will be a
straight line that blends smoothly with the neighboring curves; i.e., the
path will enter $z_k-1$ and leave $z_k$ in the direction of
$z_k-z_k-1$. \ (The "trunk" of El Palo Alto makes use of this option,
and we have also used it to draw the signboard of the dangerous bend
symbol at the end of Chapter 12.) \ Finally, the '\&' operation joins two
independent paths together at a common point, just as '\&' concatenates
two strings together.

Here, for example, is a somewhat silly path that illustrates all five
basic types of joinery:
\displayfig 14d (120\apspix)

>
$z_0=(0,100)$; \ $z_1=(50,0)$; \ $z_2=(180,0)$;
@for@ $n=3$ @upto@ 9: $z[n]=z[n-3]+(200,0)$; \ @endfor@
@draw@ $z_0\to z_1\ddashto z_2\ldots\{"up"\}z_3$
\& $z_3\to z_4\dashto z_5\ldots\{"up"\}z_6$
\& $z_6\ldots z_7\ddashto z_8\to\{"up"\}z_9$.

**[Dangerous Bend]** The '$\ldots$' operation is usually used only when one or both of the
adjacent directions have been specified (like '$\{"up"\}$' in this example).
Plain METAFONT's ^"flex" construction actually uses '$\ldots$',
not '$\to$' as stated earlier, because this avoids inflection points in
certain situations.

**[Dangerous Bend]** A path like '$z_0\ddashto z_1\ddashto z_2$' is almost indistinguishable
from the broken line '$z_0\dashto z_1\dashto z_2$', except that if you
enlarge the former path you will see that its lines aren't perfectly
straight; they bend just a little, so that the curve is "smooth" at
$z_1$ although there's a rather sharp turn there. \ (This means that
the operations discussed in Chapter 24 will apply.) \
For example, the path $(0,3)\ddashto(0,0)\ddashto(3,0)$ is equivalent to

>
$(0,3)\to \controls\,(-0.0002,2.9998)\and (-0.0002,0.0002)$
$\to(0,0)\to \controls\,(0.0002,-0.0002) \and (2.9998,-0.0002)\to(3,0)$

while $(0,3)\dashto(0,0)\dashto(3,0)$ consists of two perfectly straight
segments:

>
$(0,3)\to \controls\,(0,2)\and (0,1)$
$\to(0,0)\to \controls\,(1,0) \and (2,0)\to(3,0)$.

**[Dangerous Bend]** exercise Plain METAFONT's ^"unitsquare" path is defined to be
'$(0,0)\dashto(1,0)\dashto(1,1)\dashto(0,1)\dashto\cycle$'.
Explain how the same path could have been defined using only '$\to$' and '\&',
not '$\dashto$' or explicit directions.

#### Answer
$(0,0)\to(1,0)\;\&\;(1,0)\to(1,1)\;\&\;(1,1)\to(0,1)
\;\&\;(0,1)\to(0,0)\;\&\;\cycle$. Incidentally, if each '\&' in this path
is changed to '$\to$', we get a path that goes through the same points;
but it is a path of length 8 that comes to a complete stop at each
corner. In other words, the path remains motionless between times $1\le t\le2$,
$3\le t\le4$, etc. This length-8 path therefore behaves somewhat strangely
with respect to the '' operation. It's better to use '\&'
than to repeat points of a path.

**[Double Dangerous Bend]** Sometimes it's desirable to take a path and change all its
connecting links to '$\ddashto$', regardless of what they were originally;
the key points are left unchanged. Plain METAFONT\ has a ^@tensepath@ operation
that does this. For example, @tensepath@ "unitsquare" $=$
$(0,0)\ddashto(1,0)\ddashto(1,1)\ddashto(0,1)\ddashto\cycle$.

When METAFONT\ is deciding what curves should be drawn in place of '$\to$' or
'$\ldots$', it has to give special consideration to the beginning and
ending points, so that the path will start and finish as gracefully as
possible. The solution that usually works out best is to make the first
and last path segments very nearly the same as arcs of circles; an
unadorned path of length 2 like '$z_0\to z_1\to z_2$' will therefore turn
out to be a good approximation to the unique circular arc that passes
through $(z_0,z_1,z_2)$, except in extreme cases. You can change this
default behavior at the endpoints either by specifying an explicit
direction or by specifying an amount of "." If you call for
curliness less than 1, the path will decrease its curvature in the
vicinity of the endpoint (i.e., it will begin to turn less sharply); if
you specify curliness greater than 1, the curvature will increase.
\ (See the definition of El Palo Alto's "trunk", earlier in this chapter.)

Here, for example, are some pairs of parentheses that were drawn using
various amounts of curl. In each case the shape was drawn by a statement
of the form '@penstroke@ $z_0e\{\curl c\}\to z_1e\to\{\curl c\}z_2e$';
different values of $c$ produce different-looking parentheses:\def\\

>
curl value\hidewidth&0&1&2&4&"infinity"
yields&\cmman 1\\2&\cmman 3\\4&\cmman 5\\6&\cmman 7\\8&\cmman 9\\:

(The parentheses of Computer Modern typefaces are defined by the
somewhat more general scheme described in Chapter 12; explicit directions are
specified at the endpoints, instead of curls, because this produces
better results in unusual cases when the characters are extremely
tall or extremely wide.)

**[Dangerous Bend]** The amount of curl should not be negative. When the curl is
very large, METAFONT\ doesn't actually make an extremely sharp turn at the endpoint;
instead, it changes the rest of the path so that there is comparatively
little curvature at the neighboring point.

**[Dangerous Bend]** Chapter 3 points out that we can change METAFONT's default curves
by specifying nonstandard "" between points, or even by
specifying explicit control points to be used in the four-point method.
Let us now study the full syntax of path expressions, so that we
can come to a complete understanding of the paths that METAFONT\ is able to make.
Here are the general rules:
\beginsyntax
<path primary>\is<pair primary>\alt<path variable>
\alt[(]<path expression>[)]
\alt[reverse]<path primary>
\alt[subpath]<pair expression>[of]<path primary>
<path secondary>\is<pair secondary>\alt<path primary>
\alt<path secondary><transformer>
<path tertiary>\is<pair tertiary>\alt<path secondary>
<path expression>\is<pair expression>\alt<path tertiary>
\alt<path subexpression><direction specifier>
\alt<path subexpression><path join>[cycle]
<path subexpression>\is<path expression not ending with direction specifier>
\alt<path subexpression><path join><path tertiary>
<path join>\is<direction specifier><basic path join><direction specifier>
<direction specifier>\is<empty>
\alt[][curl]<numeric expression>[]
\alt[]<pair expression>[]
\alt[]<numeric expression>[,]<numeric expression>[]
<basic path join>\is[\&]\alt[..]\alt[..]<tension>[..]\alt[..]<controls>[..]
<tension>\is[tension]<tension amount>
\alt[tension]<tension amount>[and]<tension amount>
<tension amount>\is<numeric primary>
\alt[atleast]<numeric primary>
<controls>\is[controls]<pair primary>
\alt[controls]<pair primary>[and]<pair primary>
\endsyntax
The operations '$\ldots$' and '$\dashto$' and '$\ddashto$' are conspicuously
absent from this syntax; that is because Appendix B defines them as macros:

>
$\ldots$&is an abbreviation for '$\to\tension\atleast1\to$';
$\dashto$&is an abbreviation for '$\{\curl1\}\to\{\curl1\}$';
$\ddashto$&is an abbreviation for '$\to\tension"infinity"\to$'.

**[Dangerous Bend]** These syntax rules specify a wide variety of possibilities, even though
they don't mention '$\dashto$' and such things explicitly, so we shall
now spend a little while looking carefully at their implications.
A path expression essentially has the form

>
$p_0 j_1 p_1 j_2\cdots j_n p_n$

where each $p_k$ is a tertiary expression of type pair or path, and where
each $j_k$ is a "path join." A path join begins and ends with a
"direction specifier," and has a "basic path join" in the middle.
A direction specifier can be empty, or it can be '$\{\curl c\}$'
for some $c\ge0$, or it can be a direction vector enclosed in braces.
For example, '$\{"up"\}$' specifies an upward direction, because plain
METAFONT\ defines ^"up" to be the pair $(0,1)$. This same direction could be
specified by '$\{(0,1)\}$' or '$\{(0,10)\}$', or without parentheses as
'$\{0,1\}$'. If a specified direction vector turns out to be $(0,0)$,
METAFONT\ behaves as if no direction had been specified; i.e., '$\{0,0\}$'
is equivalent to '*empty*'. An empty direction specifier is implicitly
filled in by rules that we shall discuss later.

**[Dangerous Bend]** A basic path join has three essential forms: \ (1) '\&' simply
concatenates two paths, which must share a common endpoint.
\ (2) '$\to\tension\alpha\and\beta\to$' means that a curve should be
defined, having respective "tensions" $\alpha$ and $\beta$.
Both $\alpha$ and $\beta$ must be equal to 3/4 or more;
we shall discuss later in this chapter.
\ (3) '$\to\controls u\and v\to$' defines a curve with intermediate
control points $u$ and $v$.

**[Dangerous Bend]** Special abbreviations are also allowed, so that the long forms
of basic path joins can usually be avoided: '$\to$' by itself stands for
'$\to\tension 1\and1\to$',
while '$\to\tension\alpha\to$' stands for
'$\to\tension\alpha\and\alpha\to$',
and '$\to\controls u\to$' stands for
'$\to\controls u\and u\to$'.

**[Dangerous Bend]** Our examples so far have always constructed paths from points;
but the syntax shows that it's also possible to write, e.g.,
'$p_0\to p_1\to p_2$' when the $p$'s themselves are paths. What does
this mean? Well, every such path will already have been changed into a
sequence of curves with explicit control points; METAFONT\ expands such
paths into the corresponding sequence of points and basic path joins
of type (3). For example, '$((0,0)\to(3,0))\to(3,3)$' is essentially
the same as '$(0,0)\to\controls\,(1,0)\and(2,0)\to(3,0)\to(3,3)$',
because '$(0,0)\to(3,0)$' is the path
'$(0,0)\to\controls\,(1,0)\and(2,0)\to(3,0)$'.
If a cycle is expanded into a subpath in this way, its cyclic
nature will be lost; its last point will simply be a copy of its first point.

**[Dangerous Bend]** Now let's consider the rules by which empty direction specifiers
can inherit specifications from their environment.
An empty direction specifier at the beginning or end of a path, or just next
to the '\&' operator, is effectively replaced by '$\{\curl1\}$'.
This rule should be interpreted properly with respect to cyclic paths, which
have no beginning or end; for example, '$z_0\to z_1\,\&\,z_1\to z_2\to\cycle$'
is equivalent to
'$z_0\to z_1\{\curl1\}\&\{\curl1\}z_1\to z_2\to\cycle$'.

**[Dangerous Bend]** If there's a nonempty direction specifier after a point but not
before it, the nonempty one is copied into both places. Thus, for example,
'$\to z\{w\}$' is treated as if it were '$\to\{w\}z\{w\}$'. If there's
a nonempty direction specifier before a point but not after it, the
nonempty one is duplicated in a similar way. A basic path join
'$\to\controls u\and v\to$' specifies explicit control points that
override any direction specifiers that may immediately surround it.

**[Dangerous Bend]** An empty direction specifier next to an explicit control point
inherits the direction of the adjacent path segment. More precisely,
'$\to z\to\controls u\and v\to$' is treated as if it were
'$\to\{u-z\}z\to\controls u\and v\to$' if $u\ne z$, or as if it were
'$\to\{\curl1\}z\to\controls u\and v\to$' if $u=z$. Similarly,
'$\to\controls u\and v\to z\to$' is treated as if $z$ were followed by
$\{z-v\}$ if $z\ne v$, by $\{\curl1\}$ otherwise.

**[Double Dangerous Bend]** After the previous three rules have been applied, we might still
be left with cases in which there are points surrounded on both sides
by empty direction specifiers. METAFONT\ must choose appropriate directions
at such points, and it does so by applying the following algorithm
due to John [*Discrete and Computational Geometry 1*
(1986), 123--140]: Given a sequence

>
$z_0\{d_0\}\to\tension\alpha_0\and\beta_1\to z_1
\to\tension\alpha_1\and\beta_2\to z_2$
$*etc.*\;z_n-1\to\tension\alpha_n-1\and\beta_n\to\{d_n\}z_n$

for which interior directions need to be determined, we will regard the
$z$'s as if they were complex numbers. Let $l_k=\vert z_k-z_k-1\vert$ be
the distance from $z_k-1$ to $z_k$, and let
$\psi_k=\arg\bigl((z_k+1-z_k)/(z_k-z_k-1 )\bigr)$ be the turning angle
at $z_k$. We wish to find direction vectors $w_0$, $w_1$, \dots, $w_n$ so
that the given sequence can effectively be replaced by

>
$z_0\{w_0\}\to\tension\alpha_0\and\beta_1\to\{w_1\}z_1
\{w_1\}\to\tension\alpha_1\and\beta_2\to\{w_2\}z_2$
$*etc.*\;z_n-1\{w_n-1\}\to
\tension\alpha_n-1\and\beta_n\to\{w_n\}z_n$.

Since only the directions of the $w$'s are significant, not the magnitudes,
it suffices to determine the angles $\theta_k=\arg\bigl(w_k/(z_k+1-z_k
)\bigr)$. For convenience, we also let $\phi_k=\arg\bigl((z_k-z_k-1)/w_k
\bigr)$, so that
$${\indent$\theta_k+\phi_k+\psi_k\;=\;0$.$(\ast)$}$$
Hobby's paper introduces the notion of "" according to
which the following equations should hold at interior points:
$${\indent$\beta_k^2l_k\bigl(\alpha_k-1(\theta_k-1
+\phi_k)-3\phi_k\bigr)=\alpha_k^2l_k+1\bigl(\beta_k+1
(\theta_k+\phi_k+1)-3\theta_k\bigr)$.$({\ast}{\ast})$}$$
We also need to consider boundary conditions. If $d_0$ is an explicit
direction vector $w_0$, we know $\theta_0$; otherwise $d_0$ is
'$\curl\gamma_0$' and we set up the equation
$${\indent$\alpha_0^2\bigl(\beta_1(\theta_0+\phi_1)-3\theta_0\bigr)
=\gamma_0\beta_1^2\bigl(\alpha_0(\theta_0+\phi_1)-3\phi_1\bigr)$.
$({\ast}{\ast}{\ast})$}$$
If $d_n$ is an explicit vector $w_n$, we know $\phi_n$; otherwise
$d_n$ is '$\curl\gamma_n$' and we set
$${\indent$\beta_n^2\bigl(\alpha_n-1(\theta_n-1+\phi_n)-3\phi_n
\bigr)=\gamma_n\alpha_n-1^2\bigl(\beta_n(\theta_n-1+\phi_n)-3
\theta_n-1\bigr)$.$({\ast}{\ast}{\ast}')$}$$
It can be shown that the conditions $\alpha_k\ge3/4$, $\beta_k\ge
3/4$, $\gamma_k\ge0$ imply that there is a unique solution to the
system of equations consisting of $(\ast)$ and $({\ast}{\ast})$ for $0<k<n$
plus the two boundary equations; hence the desired quantities $\theta_0$,
\dots, $\theta_n-1$ and $\phi_1$, \dots, $\phi_n$ are uniquely determined.
\ (The only exception is the degenerate case $n=\gamma_0\gamma_1=1$.)

**[Double Dangerous Bend]** A similar scheme works for cycles, when there is no '$\{d_0\}$'
or '$\{d_n\}$'. In this case equations $(\ast)$ and $({\ast}{\ast})$
hold for all $k$.

**[Double Dangerous Bend]** exercise Write out the equations that determine the directions chosen
for the general cycle
'$z_0\to\tension\alpha_0\and\beta_1\to
z_1\to\tension\alpha_1\and\beta_2\to
z_2\to\tension\alpha_2\and\beta_3\to\cycle$'
of length 3. \ (You needn't try to solve the equations.)

#### Answer
Let $\delta_1=z_1-z_0$, $\delta_2=z_2-z_1$, $\delta_3=z_0-z_2$;
$l_1=\vert\delta_1\vert$, $l_2=\vert\delta_2\vert$, $l_3=\vert\delta_3\vert$;
$\psi_1=\arg(\delta_2/\delta_1)$, $\psi_2=\arg(\delta_3/\delta_2)$,
$\psi_3=\arg(\delta_1/\delta_3)$. The equations to be solved are
$(\ast)$ and $({\ast}{\ast})$ for $1\le k\le3$, where $\alpha_3=\alpha_0$
and $\beta_4=\beta_1$. These six equations determine
$\theta_1,\theta_2,\theta_3$ and $\phi_1,\phi_2,\phi_3$.

**[Double Dangerous Bend]** Whew---
these rules have determined the directions at all points.
To complete the job of path specification, we need merely explain how
to change a segment like '$z_0\{w_0\}\to\tension\alpha\and\beta\to\{w_1\}
z_1$' into a segment of the form
'$z_0\to\controls u\and v\to z_1$';
i.e., we finally want to know METAFONT's
magic recipe for choosing the control points $u$ and $v$.
If $\theta=\arg\bigl(w_0/(z_1-z_0)\bigr)$ and
$\phi=\arg\bigl((z_1-z_0)/w_1\bigr)$, the control points are

>
$u=z_0+e(z_1-z_0)f(\theta,\phi)/\alpha,
v=z_1-e(z_1-z_0)f(\phi,\theta)/\beta$,

where $f(\theta,\phi)$ is another formula due to John Hobby:

>
$\displaystyle f(\theta,\phi)=
{2+\sqrt2\,(\sin\theta-{1\over16}\sin\phi)
(\sin\phi-{1\over16}\sin\theta)(\cos\theta-\cos\phi)\over
3\,\bigl(1+{1\over2}(\sqrt5-1)\cos\theta+{1\over2}(3-\sqrt5\,)\cos\phi\bigr)}.$

**[Double Dangerous Bend]** There's yet one more complication. If the tensions $\alpha$ and/or
$\beta$ have been preceded by the keyword '', the values of
$\alpha$ and/or $\beta$ are increased, if necessary, to the minimum
values such that $u$ and $v$ do not lie outside the ","
which is discussed near the end of Chapter 3.

**[Dangerous Bend]** What do these complex rules imply, for METAFONT\ users who aren't "into"
mathematics? The most important fact is that the rules for paths are
invariant under shifting, scaling, and rotation. In other words, if the
key points $z_k$ of a path are all shifted, scaled, and/or rotated in the
same way, the resulting path will be the same as you would get by
shifting, scaling, and/or rotating the path defined by the unmodified
$z_k$'s (except of course for possible rounding errors). However,
this invariance property does not hold if the points or paths are
xscaled and yscaled by separate amounts.

**[Dangerous Bend]** Another consequence of the rules is that specifications
have a fairly straightforward interpretation in terms of control points,
when the adjacent directions have been given: The formulas for $u$ and $v$
simply involve division by $\alpha$ and $\beta$. This means, for example,
that a tension of 2 brings the control points halfway in towards the
neighboring key points, and a tension of "infinity" makes the points very
close indeed; contrariwise, tensions less than 1 move the control
points out.

**[Dangerous Bend]** Tension and curl specifications also influence METAFONT's choices of
directions at the key points. That is why, for example, the construction
'$z_k-1\ddashto z_k$' (which means '$z_k-1\to\tension"infinity"\to
z_k$') affects the direction of a larger path as it enters
$z_k-1$ and leaves $z_k$.

**[Dangerous Bend]** The rules imply that a change in the position of point $z_n$
causes a change in the curve near point $z_0$, when METAFONT\ has to choose
directions at all points between $z_0$ and $z_n$. However, this effect
is generally negligible except in the vicinity of the changed point.
You can verify this by looking, for example, at the control
points that METAFONT\ chooses for the path '$(0,0)\to(1,0)\to(2,0)\to
(3,0)\to(4,0)\ldots\{"up"\}(5,y)$', as $y$ varies.

**[Double Dangerous Bend]** exercise Run METAFONT\ on the "expr'' file of Chapter 8, and ask
to see the path expression '^"unitsquare" shifted $(0,1)\;\to\;$
"unitsquare" shifted $(1,0)$'. Account for the results that you get.

#### Answer
The path is of length 9, and it is equivalent to
'$(0,1)\dashto(1,1)\dashto(1,2)\dashto(0,2)\dashto(0,1)\{"down"\}
\to\{"right"\}(1,0)\dashto(2,0)\dashto(2,1)\dashto(1,1)\dashto(1,0)$'.
Although "unitsquare" is a cycle, the cycle is broken when it is used
inside a larger path; the resulting non-cyclic square path goes "down"
when it ends and "right" when it begins.

**[Double Dangerous Bend]** exercise We've said that '$\dashto$' is plain METAFONT's abbreviation
for '$\{\curl1\}\to\{\curl1\}$'. Would there be any essential difference
if '$\dashto$' were defined to mean '$\{\curl2\}\to\{\curl2\}$'?

#### Answer
Yes; for example, '$z_0\to z_1\to z_2\dashto z_3$' would be
equivalent to '$z_0\to z_1\to\{\curl2\}z_2\{\curl2\}\to\{\curl2\}z_3$'.
But a path like $z_0\dashto z_1\dashto z_2\dashto z_3$ would not be
affected, because all directions would turn out to be the same as before.
(The path '$z_0\{\curl a\}\to\{\curl b\}z_1$' is a straight line regardless
of the values of $a$ and $b$, because equations $({\ast}{\ast}{\ast})$
and $({\ast}{\ast}{\ast}')$ always have the solution $\theta_0=\phi_1=0$
when $n=1$.)

**[Double Dangerous Bend]** exercise Look closely at the syntax of *path expression* and
explain what METAFONT\ does with the specification '$(0,0)\to(3,3)\to\cycle
\{\curl1\}$'.

#### Answer
It treats this as '$((0,0)\to(3,3)\to\cycle)\{\curl1\}$'; i.e.,
the part up to and including 'cycle' is treated as a subpath
(cf. "p2'' in Chapter 8). The cycle is broken, after which we have
'$(0,0)\to\controls\,(2,-2)\and(5,1)\to(3,3)\to\controls\,(1,5)\and
(-2,2)\to(0,0)\{\curl1\}$'. Finally the '$\{\curl1\}$' is dropped,
because all control points are known. \ (The syntax by itself isn't
really enough to answer this question, as you probably realize.
You also need to be told that the computation of directions and
control points is performed whenever METAFONT\ uses the last two
alternatives in the definition of *path expression*.)

**[Dangerous Bend]** Now let's come back to simpler topics relating to paths.
Once a path has been specified, there are lots of things you can
do with it, besides drawing and filling and suchlike. For example,
if $p$ is a path, you can reverse its direction by saying 'reverse $p$';
the of '$z_0\to\controls u\and v\to z_1$' is
'$z_1\to\controls v\and u\to z_0$'.

**[Dangerous Bend]** exercise True or false: length reverse $p$ $=$ length $p$,
for all paths $p$.

#### Answer
True. The length of a path is the number of
'$z_k\to\controls u_k\and v_k+1\to z_k+1$' segments that it contains,
after all control points have been chosen.

**[Dangerous Bend]** It's convenient to associate "" with paths,
by imagining that we move along a path of length $n$ as time passes
from 0 to $n$. \ (Chapter 8 has already illustrated this notion, with
respect to an almost-but-not-quite-circular path called 'p2'; it's a good idea
to review the discussion of paths and in Chapter 8 now before
you read further.) \ Given a path

>
$p=z_0\to\controls u_0\and v_1\to z_1\,*etc.*\,z_n-1\to
\controls u_n-1\and v_n\to z_n$

and a number $t$, METAFONT\ determines 'point $t$ of $p$' as follows:
If $t\le0$, the result is $z_0$; if $t\ge n$, the result is $z_n$;
otherwise if $k\le t<k+1$, it is $(t-k)[z_k,u_k,v_k+1,z_k+1]$,
where we generalize the '$t[\alpha,\beta]$' notation
so that $t[\alpha,\beta,\gamma]$ means
$t\bigl[t[\alpha,\beta],t[\beta,\gamma]\bigr]$
and $t[\alpha,\beta,\gamma,\delta]$ means
$t\bigl[t[\alpha,\beta,\gamma],t[\beta,\gamma,\delta]\bigr]$. \ (This
is a polynomial in $t$, cf. Chapter 3.) \
Given a cyclic path

>
$c=z_0\to\controls u_0\and v_1\to z_1\,*etc.*\,z_n-1\to
\controls u_n-1\and v_n\to\cycle$

and a number $t$, METAFONT\ determines 'point $t$ of $c$' in essentially the
same way, except that $t$ is first reduced modulo $n$ so as to lie
in the range $0\le t<n$.

**[Double Dangerous Bend]** exercise True or false: point $t$ of $(z_0\dashto z_1)$ $=$
$t[z_0,z_1]$.

#### Answer
True if $0\le t\le1$, except perhaps for rounding errors;
otherwise false. The path $z_0\dashto z_1$ is equivalent to '$z_0\to
\controls1/3[z_0,z_1]\and2/3[z_0,z_1]\to z_1$', and the
polynomial simplifies because $t[w,w+\delta,w+2\delta,w+3\delta]=w+3t\delta$.
Incidentally, 'point $t$ of $(z_0\ddashto z_1)$' is usually quite
different from $t[z_0,z_1]$.

**[Dangerous Bend]** Given a path $p$ and two time values $t_1\le t_2$,
'subpath $(t_1,t_2)$ of $p$' contains all the values
'point $t$ of $p$' as $t$ varies from $t_1$ to $t_2$. There's no problem
understanding how to define this subpath when $t_1$ and $t_2$ are integers;
for example,

>
subpath $(2,4)$ of $p$ $=$ $z_2\to\controls u_2\and v_3\to z_3
\to\controls u_3\and v_4\to z_4$

in the notation above, if we assume that $n\ge 4$. The fractional case is
handled by "stretching time" in one segment of the curve; for example,
if $0<t<1$ we have

>
subpath $(0,t)$ of $p$ $=$ $z_0\to\controls t[z_0,u_0]\and
t[z_0,u_0,v_1]\to t[z_0,u_0,v_1,z_1]$;
subpath $(t,1)$ of $p$ $=$ $t[z_0,u_0,v_1,z_1]\to\controls
t[u_0,v_1,z_1]\and t[v_1,z_1]\to z_1$.

These two subpaths together account for all points of
'$z_0\to\controls u_0\and v_1\to z_1$'. To get subpath $(t_1,t_2)$ of $p$
when $0<t_1<t_2<1$, METAFONT\ applies this construction twice, by computing
subpath $(t_1/t_2,1)$ of subpath $(0,t_2)$ of $p$.

**[Double Dangerous Bend]** The operation 'subpath $(t_1,t_2)$ of $p$' is defined for all
combinations of times $(t_1,t_2)$ and paths $p$ by the following rules:
Let $n=length\,p$. \ (1) If $t_1>t_2$, subpath $(t_1,t_2)$ of $p$ $=$
reverse subpath $(t_2,t_1)$ of $p$. Henceforth we shall assume that
$t_1\le t_2$. \ (2) If $t_1=t_2$, subpath $(t_1,t_2)$ of $p$ $=$
point $t_1$ of $p$, a path of length zero. Henceforth we shall assume that
$t_1<t_2$.
\ (3) If $t_1<0$ and $p$ is a cycle, subpath $(t_1,t_2)$ of $p$ $=$
subpath $(t_1+n,t_2+n)$ of $p$. If $t_1<0$ and $p$ is not a cycle,
subpath $(t_1,t_2)$ of $p$ $=$ subpath $\bigl(0,\max(0,t_2)\bigr)$ of $p$.
Henceforth we shall assume that $t_1\ge0$.
\ (4) If $t_1\ge n$ and $p$ is a cycle, subpath $(t_1,t_2)$ of $p$ $=$
subpath $(t_1-n,t_2-n)$ of $p$.
If $t_1<n<t_2$ and $p$ is a cycle, subpath $(t_1,t_2)$ of $p$ $=$
subpath $(t_1,t_2)$ of $(p\,\&\,p\,\&\,\cycle)$.
If $t_2>n$ and $p$ is not a cycle, subpath $(t_1,t_2)$ of $p$ $=$
subpath $\bigl(\min(t_1,n),n\bigr)$ of $p$.
Henceforth we shall assume that $0\le t_1<t_2\le n$.
\ (5) If $t_1\ge1$, subpath $(t_1,t_2)$ of $p$ $=$
subpath $(t_1-1,t_2-1)$ of subpath $(1,n)$ of $p$, where
subpath $(1,n)$ of $p$ is obtained by removing the first segment of $p$.
Henceforth we shall assume that $0\le t_1<1$.
\ (6) If $t_2>1$, subpath $(t_1,t_2)$ of $p$ $=$
subpath $(t_1,1)$ of $p$ \& subpath $(1,t_2)$ of $p$.
Henceforth we shall assume that $0\le t_1<t_2\le 1$.
\ (7) The remaining cases were defined in the preceding paragraph.

**[Double Dangerous Bend]** exercise What is the length of
'subpath $(2.718,3.142)$ of $p$'?

#### Answer
If $p$ is a cycle, or if $p$ is a path of length $\ge4$, the
stated subpath has length 2. Otherwise the length is
$\max(0,length\,p-2)$.

**[Dangerous Bend]** Besides 'point $t$ of $p$', METAFONT\ allows you to speak of
' $t$ of $p$' and ' $t$ of $p$';
this gives access to the control points of a path. Let

>
$p=z_0\to\controls u_0\and v_1\to z_1\,*etc.*\,z_n-1\to
\controls u_n-1\and v_n\to z_n$.

If $t<n$, postcontrol $t$ of $p$ is the first control point in
subpath $(t,n)$ of $p$; if $t\ge n$, postcontrol $t$ of $p$ is $z_n$.
If $t>0$, precontrol $t$ of $p$ is the last control point in
subpath $(0,t)$ of $p$; if $t\le 0$, precontrol $t$ of $p$ is $z_0$.
In particular, if $t$ is an integer, postcontrol $t$ of $p$ is $u_t$
for $0\le t<n$, and precontrol $t$ of $p$ is $v_t$ for $0<t\le n$.

**[Dangerous Bend]** The ability to extract key points and control points makes it
possible to define interesting operations such as plain METAFONT's ^"interpath"
function, which allows you to . For example,
'"interpath"$(1/3,p,q)$' will produce a path of length $n$ whose
points are 1/3[point $t$ of $p,\,$ point $t$ of $q$] for $0\le t\le n$,
given any paths $p$ and $q$ of length $n$. It can be defined by a
fairly simple program:

>
@vardef@ "interpath"(@expr@ $a,p,q) =$
@for@ $t=0$ @upto@ length$\,p-1$: $a$[point $t$ of $p,\,$
point $t$ of $q$]
$\to\controls$ $a$[postcontrol $t$ of $p,\,$
postcontrol $t$ of $q$]
and $a$[precontrol $t+1$ of $p,\,$
precontrol $t+1$ of $q$] $\to$ @endfor@
@if@ cycle $p$: cycle\% assume that $p,q$ are both cycles
or both noncycles
@else@: $a$[point "infinity" of $p$, point "infinity" of $q$]
@fi@ @enddef@;

**[Dangerous Bend]** On February 14, 1979, the author
bought a box of chocolates and placed the box on a piece of
graph paper (after suitably disposing of the contents).
The experimental data gathered in this way led to a "definitive"
heart shape:

>
$"heart"=(100,162)\to(140,178)\{"right"\}\to(195,125)\{"down"\}$
$\to(100,0)\{\curl0\}
\to\{"up"\}(5,125)\to\{"right"\}(60,178)\to(100,162)$;

it is interesting to interpolate between ^"heart" and other paths, by using
a program like

>
@for@ $n=0$ @upto@ 10: @draw@ "interpath"$(n/10,p,"heart")$; @endfor@.

For example, the left illustration below was obtained by taking

>
$p=(100,0)\dashto(300,0)\dashto(200,0)\dashto(100,0)\dashto(0,0)
\dashto(-100,0)\dashto(100,0)$;

notice that "interpath" doesn't necessarily preserve smoothness at the key
points. The right illustration was obtained by duplicating point
$(100,0)$ in "heart" (thereby making it a path of length 7) and taking

>
$p=(100,200)\dashto(200,200)\dashto(200,100)$
$\dashto(200,0)\dashto(0,0)\dashto(0,100)\dashto(0,200)\dashto(100,200)$.

\displayfig 14bb\&cc (1in)

**[Dangerous Bend]** Plain METAFONT\ allows you to say ' $t$ of $p$' in order
to determine the direction in which path $p$ is moving at time $t$. This is
simply an abbreviation for '(postcontrol $t$ of $p)-($precontrol $t$ of $p$)'.
Sometimes a path veers abruptly and has no unique direction; in this case
the direction function gives a result somewhere between the two possible
extremes. For example, the "heart" path above turns a corner at
time 3; 'direction 3 of "heart"' turns out to be
$(-93.29172,0)$, but 'direction $3-"epsilon"$ of "heart"' is
$(-46.64589,-31.63852)$ and 'direction $3+"epsilon"$ of "heart"' is
$(-46.64589,31.63852)$.

\catcode'\"=\other
\indent to #1##&##
}

{\nobreak}}

**[Dangerous Bend]** Conversely, METAFONT\ can tell you when a path heads in
a given direction. You just ask for ' $w$ of $p$', where
$w$ is a direction vector and $p$ is a path. This operation is best
understood by looking at examples, so let's resume our dialog with the
computer by applying METAFONT\ to the "expr'' file as in Chapter 8. When
METAFONT\ first says "gimme'', our opening strategy this time will be
to type

"'

hide(p3 = (0,0)right..up(1,1)) p3

"'

so that we have a new path to play with. Now the fun begins:

\begindemo230pt
\demohead
directiontime right of p3&0
directiontime up of p3&1
directiontime down of p3&-1
directiontime (1,1) of p3&0.5
directiontime left of reverse p3&1
direction directiontime (1,2) of p3 of p3&(0.23126,0.46251)
directiontime right of subpath(epsilon,1) of p3&0
directiontime right of subpath(2epsilon,1)of p3&-1
directiontime (1,1) of subpath(epsilon,1) of p3&0.49998
direction epsilon of p3&(0.55226,0)
direction 2epsilon of p3&(0.55229,0.00003)
directiontime dir 30 of p3&0.32925
angle direction 0.32925 of p3&29.99849
angle direction 0.32925+epsilon of p3&30.00081
directionpoint up of p3&(1,1)
\enddemo
Note that directiontime yields $-1$ if the specified direction doesn't occur.
At time ^"epsilon", path $p_3$ is still traveling right, but at time
2"epsilon" it has begun to turn upward. The '' operation
is analogous to directiontime, but it gives the point on the path rather
than the time of arrival. ^^"fullcircle"
\begindemo230pt
\demohead
directiontime up of fullcircle&0
directiontime left of fullcircle&2
directiontime right of fullcircle&6
directiontime (-1,1) of fullcircle&1
directiontime (epsilon,infinity) of fullcircle&8
directiontime right of unitsquare&0
directiontime up of unitsquare&1
directiontime (1,1) of unitsquare&1
directiontime (-1,1) of unitsquare&2
\enddemo
If a path travels in a given direction more than once, directiontime
reports only the first time. The ^"unitsquare" path has sharp turns at
the corners; directiontime considers that all directions between the
incoming and outgoing ones are instantaneously present.

**[Double Dangerous Bend]** It's possible to construct pathological paths in which unusual
things happen. For example, the path $p=(0,0)\to\controls\,(1,1)\and(0,1)
\to(1,0)$ has a "" at time 0.5, when it comes to a dead stop and
turns around. \ $\bigl($If you ask for 'direction 0.5 of $p$', the answer
is zero, while direction $0.5-\epsilon$ of $p$ is $(0,2\epsilon)$ and
direction $0.5+\epsilon$ of $p$ is $(0,-2\epsilon)$.$\bigr)$ \ The
directiontime operation assumes that all possible directions actually
occur when a path comes to a standstill, hence 'directiontime "right"
of $p$' will be 0.5 in this case even though it might be argued that
$p$ never turns to the right. Paths with cusps are numerically unstable,
and they might become "" after transformations are applied,
because rounding errors might change their . The path $p$
in this example has control points that correspond to tensions of only
about 0.28 with respect to the initial and final directions; since METAFONT\ insists
that s be at least 0.75, this anomalous path could never have arisen
if the control points hadn't been given explicitly.

**[Double Dangerous Bend]** exercise Write macros called ^"posttension" and ^"pretension"
that determine the effective tensions of a path's control points at
integer times $t$. For example, '"pretension" 1 of ($z_0\to
\tension\alpha\and\beta\to z_1$)' should be $\beta$ (approximately).
Test your macro by computing "posttension" 0 of $\bigl((0,0)\{"right"\}
\ldots\{"up"\}(1,10)\bigr)$.

#### Answer
@vardef@ "posttension" @expr@ $t$ of $p$ $=$break
@save@ $q$; @path@ $q$;break
$q=point\,t\,of\,p\,\{direction\,t\,of\,p\}
\to\{direction\,t\!+\!1\,of\,p\}\,
point\,t\!+\!1\,of\,p$;break
length(postcontrol 0 of $q$ $-$ point 0 of $q$)break
/length(postcontrol $t$ of $p$ $-$ point $t$ of $p$) @enddef@;break
@vardef@ "pretension" @expr@ $t$ of $p$ $=$break
@save@ $q$; @path@ $q$;break
$q=point\,t\!-\!1\,of\,p\,\{direction\,
t\!-\!1\,of\,p\}\to\{direction\,t\,of\,p\}\,
point\,t\,of\,p$;break
length(precontrol 1 of $q$ $-$ point 1 of $q$)break
/length(precontrol $t$ of $p$ $-$ point $t$ of $p$) @enddef@;
\nobreak
The stated posttension turns out to be 4.54019.

**[Dangerous Bend]** We have now discussed almost all of the things that METAFONT\ can do
with paths; but there's one more important operation to consider,
namely . Given two paths $p$ and $q$, you can write

>
$p$ intersectiontimes $q$

and the result will be a pair of times $(t,u)$ such that point $t$
of $p$ $\approx$ point $u$ of $q$. For example, using the
'expr' routine,^^"halfcircle"
\begindemo245pt
\demohead
unitsquare intersectiontimes fullcircle&(0.50002,0)
unitsquare intersectiontimes fullcircle rotated 90&(0.50002,6)
reverse unitsquare intersectiontimes fullcircle&(0.50002,2)
fullcircle intersectiontimes unitsquare&(0,0.50002)
halfcircle rotated 45 intersectiontimes unitsquare&(1,3.5)
halfcircle rotated 89 intersectiontimes unitsquare&(0.02196,3.5)
halfcircle rotated 90 intersectiontimes unitsquare&(0,3.50002)
halfcircle rotated 91 intersectiontimes unitsquare&(-1,-1)
halfcircle rotated 45 intersectiontimes fullcircle&(0,1)
fullcircle intersectiontimes (-0.5,0)&(4,0)
unitsquare intersectionpoint fullcircle&(0.5,0)
reverse unitsquare intersectionpoint fullcircle&(0,0.5)
\enddemo
Notice that the result is $(-1,-1)$ if the paths don't intersect.
The last two examples illustrate the ''
operator, which yields the common point of intersection. Both
intersectiontimes and intersectionpoint apply at the of
, hence parentheses were not needed in these examples.

**[Dangerous Bend]** exercise J. H. (a student) wanted to construct a path $r$
that started on some previously defined path $p$ and proceeded
up to the point where it touched another path $q$, after which $r$ was
supposed to continue on path $q$. So he wrote

>
@path@ $r$; \ @numeric@ $t,u$; \ $(t,u)=p$ intersectiontimes $q$;
$r=subpath\,(0,t)\,of\,p\;\;\&\;\;
subpath\,(u,"infinity")\,of\,q$;

but it didn't work. Why not?

#### Answer
The '\&' had to be changed to '$\to$', because point $t$ of $p$
might not be exactly equal to point $u$ of $q$.

**[Double Dangerous Bend]** If the paths intersect more than once, METAFONT\ has a somewhat
peculiar way of deciding what times $(t,u)$ should be reported by
'$p$ intersectiontimes $q$'. Suppose $p$ has length $m$ and $q$ has
length $n$. \ (Paths of length 0 are first changed into motionless paths
of length 1.) \ METAFONT\ proceeds to examine subpath $(k,k+1)$ of $p$
versus subpath $(l,l+1)$ of $q$, for $k=0$, \dots, $m-1$ and $l=0$,
\dots, $n-1$, with $l$ varying most rapidly. This reduces the general
problem to the special case of paths of length 1, and the times $(t,u)$
for the first such intersection found are added to $(k,l)$. But within
paths of length 1 the search for intersection times is somewhat
different: Instead of reporting the "lexicographically smallest" pair
$(t,u)$ that corresponds to an intersection, METAFONT\ finds the $(t,u)$
whose "" representation $(.t_1u_1t_2u_2\ldots\,)_2$
is minimum, where $(.t_1t_2\ldots\,)_2$ and $(.u_1u_2\ldots\,)_2$ are
the radix-2 representations of $t$ and $u$.

**[Double Dangerous Bend]** exercise (A mathematical puzzle.) \ The path
$p=(0,0)\to\controls\,(2,2)\and(0,1)\to(1,0)$ loops on itself, so there
are times $t<u$ such that point $t$ of $p$ $\approx$ point $u$ of $p$.
Devise a simple way to compute $(t,u)$ in a METAFONT\ program, without
using the subpath operation.

#### Answer
Since $p$ intersects itself infinitely often at times $(t,t)$,
the task may seem impossible; but METAFONT's shuffled-binary search procedure
provides a way. Namely, $p$ intersectiontimes reverse $p$ $=$
$(0.17227,0.28339)$, from which we can deduce that $t=0.17227$ and
$1-u=0.28339$.

**[Dangerous Bend]** Let's conclude this chapter by applying what we've learned about
paths to a real-life example. The was
published for many years by Academic Press, and its cover page carried the
following , which was designed by J. C. Knuth
to blend with the style of type
used elsewhere on that page:
\displayfig 14dd (25mm)
A METAFONT\ program to produce this logo made it possible for the editors
of the journal to use it on letterheads in their correspondence.
Here is one way to write that program, without needing to erase anything:
^^"superellipse" ^^"whatever"
^^@forsuffixes@
$${ toindent{\sevenrm#\ \ \ }&#
1&@beginchar@('"A"'$,29"mm"\0,25"mm"\0,0)$; \
$"thick"\0:=2"mm"\0$; \ $"thin"\0:=5/4"mm"\0$;
2&@define\_whole\_blacker\_pixels@$("thick","thin")$;
3&@forsuffixes@ $\$=a,b,c$: \ @transform@ \$;
4& @forsuffixes@ $e=l,r$: \ @path@ $\$e,\$'e$; \
@numeric@ $t\$[\,]e$; \ @endfor@ @endfor@
5&$\penpos1("thick",0)$; $\penpos2("thick",90)$;
$\penpos3("thick",180)$; $\penpos4("thick",270)$;
6&$\penpos5("thick",0)$; $\penpos6("thick",90)$;
$\penpos7("thick",180)$; $\penpos8("thick",270)$;
7&$x_2=x_4=x_6=x_8=.5[x_5,x_7]=.5w$; \ $x_1r=w$; \ $x_3r=0$; \
$x_5-x_7=y_6-y_8$;
8&$y_1=y_3=y_5=y_7=.5[y_6,y_8]=.5h$; \ $y_2r=h$; \ $y_4r=0$; \
$y_6r=.75h$;
9&@forsuffixes@ $e=l,r$: \ $a.e=b'e=c'e="superellipse"
(z_1e,z_2e,z_3e,z_4e,.75)$;
10& $a'e=b.e=c.e="superellipse"
(z_5e,z_6e,z_7e,z_8e,.72)$; \ @endfor@
11&$\penposa1("thin",0)$; \ $\penposa5("whatever",-90)$; \
$\penposa9("thin",180)$;
12&$x_a1l-x_a9l=1/3(x_5l-x_7l)$; \ $x_a5=.5w$; \
$y_a1=y_a9$; \ $y_a5r=4/7h$;
13&$x_a3l=x_a1l$; \ $x_a3r=x_a1r$; \ $x_a4r=1/6[x_a3r,x_1l]$; \
$x_0=.5w$; \ $y_0=.52h$;
14&$x_a6l+x_a4l=x_a6r+x_a4r=
x_a7l+x_a3l=x_a7r+x_a3r=x_a9+x_a1=w$;
15&\thickmuskip=4mu $y_a3r=y_a4r=y_a6r=y_a7r=.2[y_2l,y_0]$; \
$y_a3l=y_a4l=y_a6l=y_a7l=y_a3r-"thin"$;
16&$z_a4l=z_a4r
+("thin",0)\,rotated(angle(z_a4r-z_a5r)+90)$
17&$+"whatever"\ast(z_a4r-z_a5r)$; \
$z_a4l-z_a5l="whatever"\ast(z_a4r-z_a5r)$;
18&$z=a.r\;intersectionpoint\;(z_0\dashto(w,0))$; \
$y_a1-y_a5=length(z-z_0)$;
19&$b="identity"$ shifted $(0,y_0-y_a1)$
rotatedaround$(z_0,90-angle(z_0-(w,0)))$;
20&$c=b$ reflectedabout $(z_2,z_4)$;
21&@for@ $n=1,3,4,5,6,7,9$:
\ @forsuffixes@ $e=l,,r$: \ @forsuffixes@ $\$=b,c$:
22& $z_{\$[n]e}=z_a[n]e$ transformed \$; \ @endfor@ @endfor@ @endfor@
23&@forsuffixes@ $e=l,r$: \ @forsuffixes@ $\$=a,b,c$:
24& $z_{\$2e}=\$r$ intersectionpoint $(z_{\$1e}\dashto z_{\$3e})$;
25& $z_{\$8e}=\$r$ intersectionpoint $(z_{\$9e}\dashto z_{\$7e})$;
26& $t_{\$1e}=xpart(\$e$
intersectiontimes $(z_{\$1l}\dashto z_{\$3l}))$;
27& $t_{\$9e}=xpart(\$e$
intersectiontimes $(z_{\$9l}\dashto z_{\$7l}))$;
28& $t_{\$4e}=xpart(\$'e$
intersectiontimes $(z_{\$5r}\dashto z_{\$4l}))$;
29& $t_{\$6e}=xpart(\$'e$
intersectiontimes $(z_{\$5r}\dashto z_{\$6l}))$; \ @endfor@ @endfor@
30&^@penstroke@ subpath$(t_a9e,t_b6e)$ of $a.e$;
31&@penstroke@ subpath$(t_b4e,t_c4e)$ of $b'e$;
32&@penstroke@ subpath$(t_c6e,t_a1e+8)$ of $c'e$;
33&@penstroke@ subpath$(t_a6e,t_b9e)$ of $a'e$;
34&@penstroke@ subpath$(t_b1e,t_c1e)$ of $b.e$;
35&@penstroke@ subpath$(t_c9e,t_a4e+8)$ of $c.e$;
36&@forsuffixes@ $\$=a,b,c$: \
@penlabels@$(\$1,\$2,\$3,\$4,\$5,\$6,\$7,\$8,\$9)$;
37& @penstroke@ $z_{\$2e}\dashto z_{\$3e}\dashto z_{\$4e}\dashto
z_{\$5e}\dashto z_{\$6e}\dashto z_{\$7e}\dashto z_{\$8e}$; \ @endfor@
38&@penlabels@(^@range@ 0 ^@thru@ 8); \ @endchar@;
}$$
Lines 5--10 of this program define the main superellipses of the figure.
The outer superellipse is eventually drawn as three separate strokes
in lines 30--32, and the inner one is drawn as three strokes in lines 33--35.
The rest of the figure consists of three arrows, whose point labels are
prefaced by the respective labels $a,b,c$. Lines 11--18 define the '$a$'
arrow; then lines 19--22 transform these points into the '$b$' and '$c$'
arrows, anticipating some of the things we shall discuss in Chapter 15.
Thirty-six intersections between arrows and superellipses are computed
in lines 23--29, and the arrows are finally drawn by the penstrokes
specified in lines 36--37.

\displayfig 14e (4.5in)

\endchapter

The route is indicated by dots,

the days' journeys are expressed by numbers,

and letters are used to locate notable places and sites.

... We arrived at the Arroyo de San Francisco,

beside which stream is the redwood tree I spoke of yesterday;

I measured its height with the Graphometer

and reckoned it to be fifty yards high, more or less.

> --- FRAY PEDRO , *Diary* (1776)

The practical teaching of the masters of Art
was summed by the O of .

> --- JOHN , *The Cestus of Aglaia* (1865)


# Chapter 15. Transformations

Points, paths, pens, and pictures can be shifted, scaled, rotated,
and revamped in a variety of ways. Our aim in this chapter will be to
learn all about the built-in metamorphoses of METAFONT, because
they can make programs simpler and more versatile.

The basic have already appeared in many examples, but let's
start by reviewing them here:

>
$(x,y)$ $(a,b)$&$=(x+a,y+b)$;
$(x,y)$ $s$&$=(sx,sy)$;
$(x,y)$ $s$&$=(sx,y)$;
$(x,y)$ $s$&$=(x,sy)$;
$(x,y)$ $s$&$=(x+sy,y)$;
$(x,y)$ $\theta$&$=(x\cos\theta-y\sin\theta,
x\sin\theta+y\cos\theta)$;
$(x,y)$ $(u,v)$&$=(xu-yv,xv+yu)$.

One of the nice things about METAFONT\ is that you don't have to remember the
sine-and-cosine formulas of trigonometry; you just have to know that
'$(x,y)$ rotated $\theta$' means 'the vector $(x,y)$ rotated $\theta$ degrees
counterclockwise around $(0,0)$', and the computer does all the necessary
calculations by itself. The operation of zscaling may look a bit strange,
but it is simply a combination of rotating by angle$\,(u,v)$ and scaling
by length$\,(u,v)$.

Plain METAFONT\ provides two more transformations that are commonly needed: You can
say '$(x,y)$ $(z_0,\theta\mkern1mu)$' if you want to rotate
around point $z_0$ instead of point $(0,0)$. And you can say
'$(x,y)$ $(z_1,z_2)$' if you want to find the point directly
opposite $(x,y)$ on the other side of the straight line that runs through
$z_1$ and $z_2$.

All of these operations are special manifestations of a single glorious
maneuver that can be written in the general form

>
$(x,y)$ $t$.

Here $t$ is a variable (or primary expression) of type ^@transform@; it
stands for any desired sequence of shiftings, scalings, slantings, etc.,
all in one fell swoop.

You can give between transforms, just as you can give equations
between other types of things in METAFONT\ programs. Thus, for example,
you might say

>
@transform@ $t[\,]$; \ $t_2=t_1$ shifted $(2,2)$ rotated 30;

then an expression like '$(x,y)$ transformed $t_1$ shifted $(2,2)$ rotated 30'
can be abbreviated to '$(x,y)$ transformed $t_2$', which is simpler and faster.

There's a special transform variable called ^"identity" with the amazing
property that

>
$(x,y)$ transformed "identity" $=$ $(x,y)$

for all $x$ and $y$. You might think that "identity" is useless, since it
does nothing, but in fact it's a natural starting point for building other
transforms. For example, line 19 of the program at the end of the previous
chapter says

>
$b="identity"$ shifted $(0,y_0-y_a1)$ rotatedaround$(z_0,"theta")$;

this defines the transform variable $b$ to be a compound transformation
that is used on lines 21 and 22 to construct the lower left arrow
as a shifted and rotated copy of the upper arrow, in the character being drawn.

**[Dangerous Bend]** A @transform@ variable $t$ represents six numbers
$(t_x,t_y,t_xx,t_xy,t_yx,t_yy)$, in much the same way
as a @pair@ variable represents two numbers $(x,y)$. The general
transformation '$(x,y)$ transformed $t$' is simply an abbreviation for

>
$(t_x+x\,t_xx+y\,t_xy,\;t_y+x\,t_yx+y\,t_yy)$;

thus, for example, '$t_xy$' appears in the xpart of the transform as the
coefficient of $y$. If you say '^@show@ $t$' when $t$ is a completely
unknown transform, the computer will type

"'

>> (xpart t,ypart t,xxpart t,xypart t,yxpart t,yypart t)

"'

just as it would type '>> (xpart u,ypart u)' for a completely
unknown variable $u$ of type @pair@. You can access individual components
of a transform by referring to ' $t$', ' $t$',

' $t$', etc.

\catcode'\"=\other
\indent to #1##&##
}

{\nobreak}}

**[Dangerous Bend]** Once again, we can learn best by computer experiments with the
'expr' file (cf. Chapter 8); this time the idea is to play with transforms:
\begindemo175pt
\demohead
identity&(0,0,1,0,0,1)
identity shifted (a,b)&(a,b,1,0,0,1)
identity scaled s&(0,0,s,0,0,s)
identity xscaled s&(0,0,s,0,0,1)
identity yscaled s&(0,0,1,0,0,s)
identity slanted s&(0,0,1,s,0,1)
identity rotated 90&(0,0,0,-1,1,0)
identity rotated 30&(0,0,0.86603,-0.5,0.5,0.86603)
identity rotatedaround ((2,3),90)&(5,1,0,-1,1,0)
(x,y) rotatedaround ((2,3),90)&(-y+5,x+1)
(x,y) reflectedabout ((0,0),(0,1))&(-x,y)
(x,y) reflectedabout ((0,0),(1,1))&(y,x)
(x,y) reflectedabout ((5,0),(0,10))&(-0.8y-0.6x+8,0.6y-0.8x+4)
\enddemo

**[Dangerous Bend]** exercise Guess the result of "(x,y) reflectedabout ((0,0),(1,0))''.

#### Answer
'(x,-y)'.

**[Dangerous Bend]** exercise What transform takes $(x,y)$ into $(-x,-y)$?

#### Answer
$(x,y)$ rotated 180, or $(x,y)$ scaled $-1$.

**[Dangerous Bend]** exercise True or false: $\bigl(-(x,y)\bigr)$ transformed $t$
$=$ $-\bigl((x,y)$ transformed $t\bigr)$.

#### Answer
True if and only if $xpart\,t=ypart\,t=0$. If the
stated equation holds for at least one pair $(x,y)$, it holds for all $(x,y)$.
According to the syntax of Chapter 8, METAFONT\ interprets '$-(x,y)$ transformed $t$'
as $\bigl(-(x,y)\bigr)$ transformed $t$. \ (Incidentally, mathematicians
call METAFONT's transformers "," and the special case in
which the xpart and ypart are zero is called ".")

**[Dangerous Bend]** In order to have some transform variables to work with, it's necessary
to "" some declarations and commands before giving the next 'expr's:
\begindemo175pt
\demohead
hide(transform t[]) t1&(xpart t1,ypart t1,xxpart...)
hide(t1=identity zscaled(1,2)) t1&(0,0,1,-2,2,1)
hide(t2=t1 shifted (1,2)) t2&(1,2,1,-2,2,1)
t2 xscaled s&(s,2,s,-2s,2,1)
unknown t2&false
transform t2&true
t1=t2&false
t1<t2&true
inverse t2&(-1,0,0.2,0.4,-0.4,0.2)
inverse t2 transformed t2&(0,0,0.99998,0,0,0.99998)
hide(t3 transformed t2=identity) t3&(-1,0,0.2,0.4,-0.4,0.2)
\enddemo
The ^"inverse" function finds the transform that undoes the work
of another; the equation that defines $t_3$ above shows how to
calculate an inverse indirectly, without using "inverse".

**[Dangerous Bend]** Like numeric expressions and pair expressions, transform
expressions can be either "" or "" at any given
point in a program. \ (If any component of a transform is unknown, the
whole transform is regarded as unknown.) \ You are always allowed to use
the constructions

>
*known* transformed *known*
*unknown* transformed *known*
*known* transformed *unknown*

but METAFONT\ will balk at '*unknown* transformed *unknown*'. This is
not the most lenient rule that could have been implemented, but it
does have the virtue of being easily remembered.

**[Dangerous Bend]** exercise If $z_1$ and $z_2$ are unknown pairs, you can't
say '$z_1$ shifted $z_2$', because 'shifted $z_2$' is an unknown
transform. What can you legally say instead?

#### Answer
$z_1+z_2$.

\def\dbend{{\manual}}

**[Dangerous Bend]** exercise Suppose "dbend" is a picture variable that contains
a normal dangerous bend sign, as in the "reverse-video" example
of Chapter 13. Explain how to transform it into the ^left-handed
dangerous bend that heads this paragraph.

#### Answer
@beginchar@$(126,25u\0,"h\_height"\0+"border"\0,0)$; \
'"Dangerous left bend"';break
$"currentpicture":="dbend"$ reflectedabout $\bigl((.5w,0),(.5w,h)\bigr)$; \
@endchar@;
The same idea can be used to create right as perfect mirror
images of left parentheses, etc., if the parentheses aren't slanted.

**[Dangerous Bend]** The next three lines illustrate the fact that you can specify
a transform completely by specifying the images of three points:
\begindemo175pt
\demohead
hide((0,0)transformed t4=(1,2)) t4&(1,2,xxpart t4,xypart t4,...)
hide((1,0)transformed t4=(4,5)) t4&(1,2,3,xypart t4,3,yypart t4)
hide((1,4)transformed t4=(0,0)) t4&(1,2,3,-1,3,-1.25)
\enddemo
The points at which the transform is given shouldn't all lie on
a straight line.

**[Dangerous Bend]** Now let's use transformation to make a little , based
on a '{\manual\oneu}' shape replicated four times:
\xleaders{$\vcenter{{\manual\fouru}}$}\

\displayfig 15a (396\apspix)

The following program merits careful study:
$${ toindent{\sevenrm#\ \ \ }&#
1&@beginchar@('"4"'$,11"pt"\0,11"pt"\0,0)$;
2&@pickup@ @pencircle@ scaled 3/4"pt" yscaled 1/3 rotated 30;
3&@transform@ $t$;
4&$t="identity"$ $\bigl((.5w,.5h),-90\bigr)$;
5&$x_2=.35w$; \ $x_3=.6w$;
6&$y_2=.1h$; \ $"top"\,y_3=.4h$;
7&@path@ $p$; \ $p=z_2\{"right"\}\ldots\{"up"\}z_3$;
8&$"top"\,z_1$ $=$ point .5 of $p$ transformed $t$;
9&@draw@ $z_1\ldots p$;
10&@addto@ "currentpicture" @also@ "currentpicture" transformed $t$;
11&@addto@ "currentpicture" @also@ "currentpicture"
transformed ($t$ transformed $t$);
12&@labels@$(1,2,3)$; \ @endchar@;
}$$
^^@addto@
Lines 3 and 4 compute the transform that moves each
'{\manual\oneu}' to its clockwise neighbor. Lines 5--7 compute the
right half of the '{\manual\oneu}'. Line 8 is the most
interesting: It puts point $z_1$ on the rotated path. Line 9 draws the
'{\manual\oneu}', line 10 changes it into two, and line 11 changes
two into four. The parentheses on line 11 could have been omitted, but it
is much faster to transform a transform than to transform a picture.

**[Double Dangerous Bend]** METAFONT\ will transform a expression only when $t_xx$,
$t_xy$, $t_yx$, and $t_yy$ are integers and either $t_xy=t_yx=0$
or $t_xx=t_yy=0$; furthermore, the values of $t_x$ and $t_y$ are
rounded to the nearest integers. Otherwise the transformation would not
take pixel boundaries into pixel boundaries.

**[Double Dangerous Bend]** exercise Explain how to rotate the ornament by $45^\circ$.
\xleaders{$\vcenter{{\manual\fourc}}$}\

#### Answer
Change line 9 to

>
@draw@ $(z_1\ldots p)$ rotatedaround$\bigl((.5w,.5h),-45\bigr)$
@withpen@ @pencircle@ scaled 3/4"pt" yscaled 1/3 rotated $-15$;

Plain METAFONT\ maintains a special variable called ^"currenttransform",
behind the scenes. Every ^@fill@ and ^@draw@ command is affected by this
variable; for example, the statement '@fill@ $p$' actually fills the
interior of the path

>
$p$ transformed "currenttransform"

instead of $p$ itself. We haven't mentioned this before, because
"currenttransform" is usually equal to "identity"; but nonstandard
settings of "currenttransform" can be used for special effects that
are occasionally desired. For example, it's possible to change
'METAFONT' to '{\manual 89:;<=>:}'\ by simply saying

>
$"currenttransform":="identity"$ slanted 1/4

and executing the programs of 'logo.mf' that are described in Chapter 11;
no other changes to those programs are necessary.

It's worth noting that the pen nib used to draw '{\manual 89:;<=>:}'\
was not slanted when "currenttransform" was changed; only the "tracks" of
the pen, the paths in @draw@ commands, were modified. Thus the slanted image
was not simply obtained by slanting the unslanted image.

**[Double Dangerous Bend]** When fonts are being made for devices with ,
plain METAFONT\ will set "currenttransform" to '"identity" yscaled
^"aspect\_ratio"', and ^@pickup@ will similarly yscale the pen nibs
that are used for drawing. In this case the slanted
'{\manual 89:;<=>:}'\ letters should be drawn with

>
$"currenttransform":="identity"$ slanted 1/4 yscaled "aspect\_ratio".

**[Double Dangerous Bend]** exercise Our program for
'2.5pt{\manual\fouru}' doesn't work when pixels
aren't square. Fix it so that it handles a general "aspect\_ratio".

#### Answer
Replace lines 10 and 11 by

>
@pickup@ @pencircle@ scaled 3/4"pt" yscaled 1/3 rotated $-60$;
@draw@ ($z_1\ldots p$) transformed $t$;
@addto@ "currentpicture" @also@ "currentpicture"
rotatedaround$\bigl((.5w,.5h)$ yscaled "aspect\_ratio"$,-180\bigr)$;

\endchapter

Change begets change. Nothing propagates so fast.

> --- CHARLES , *Martin Chuzzlewit* (1843)

There are some that never know how to change.

> --- MARK , *Joan of Arc* (1896)

\beginChapter Chapter 16. Calligraphic\\Effects

were introduced in Chapter 4, and we ought to make a systematic study
of what METAFONT\ can do with them before we spill any more ink. The purpose
of this chapter will be to explore the uses of "fixed" pen nibs---i.e.,
variables and expressions of type ^@pen@---rather than to consider
the creation of shapes by means of outlines or penstrokes.

When you say '^@pickup@ ^*pen expression*', the macros of plain METAFONT\ do
several things for you: They create a representation of the specified
pen nib, and assign it to a pen variable called ^"currentpen"; then they
store away information about the top, bottom, left, and right extents of
that pen, for use in ^"top", ^"bot", ^"lft", and ^"rt" operations.
A ^@draw@ or ^@drawdot@ or ^@filldraw@ command will make use of
"currentpen" to modify the current picture.

You can also say '@pickup@ *numeric expression*'; in this case the numeric
expression designates the code number of a previously picked-up pen
that was saved by '^"savepen"'. For example, the 'logo.mf' file in Chapter 11
begins by picking up the pen that's used to draw 'METAFONT', then
it says '$"logo\_pen":="savepen"$'. Every character program later in that
file begins with the command '@pickup@ "logo\_pen"', which is a fast
operation because it doesn't require the generation of a new
pen representation inside the computer.

**[Dangerous Bend]** Caution: Every time you use "savepen", it produces a new integer
value and stashes away another pen for later use. If you keep doing this,
METAFONT's memory will become cluttered with the representations of pens
that you may never need again. The command '^@clear\_pen\_memory@'
discards all previously saved pens and lets METAFONT\ start afresh.

**[Dangerous Bend]** But what is a *pen expression*? Good question. So far in this book,
almost everything that we've picked up was a pencircle followed by
some sequence of transformations; for example, the "logo\_pen" of
Chapter 11 was '@pencircle@ xscaled "px" yscaled "py"'. Chapter 13
also made brief mention of another kind of pen, when it said

>
@pickup@ ^@penrazor@ scaled 10;

this command picks up an infinitely thin pen that runs from point
$(-5,0)$ to point $(5,0)$ with respect to its center. Later in this
chapter we shall make use of pens like

>
^@pensquare@ xscaled 30 yscaled 3 rotated 30;

this pen has a rectangular boundary measuring 30 pixels $\times$ 3 pixels,
inclined at an angle of $30^\circ$ to the baseline.

**[Dangerous Bend]** You can define pens of any al shape by saying
'^@makepen@ $p$', where $p$ is a cyclic path. It turns out that METAFONT\
looks only at the key points of $p$, not the control points, so we may
as well assume that $p$ has the form $z_0\dashto z_1\dashto*etc.*\dashto
\cycle$. This path must have the property that it turns left at every
key point (i.e., $z_k+1$ must lie to the left of the line from $z_k-1$
to $z_k$, for all $k$), unless the cycle contains fewer than three key
points; furthermore the path must have a of 1 (i.e.,
it must not make more than one counterclockwise loop). Plain METAFONT's
@penrazor@ stands for
'@makepen@ $\bigl((-.5,0)\dashto(.5,0)\dashto \cycle\bigr)$',
and @pensquare@ is an abbreviation for
'@makepen@ $\bigl("unitsquare"$ shifted $-(.5,.5)\bigr)$'.
But @pencircle@ is not defined via @makepen@; it is a
primitive operation of METAFONT. It represents a true of diameter 1,

passing through the points $(\pm.5,0)$ and $(0,\pm.5)$.

**[Dangerous Bend]** The complete syntax for pen expressions is rather short, because
you can't really do all that much with pens. But it also contains a
surprise:
\beginsyntax
<pen primary>\is<pen variable>
\alt[(]<pen expression>[)]
\alt[nullpen]
<future pen primary>\is[pencircle]
\alt[makepen]<path primary>
<pen secondary>\is<pen primary>
<future pen secondary>\is<future pen primary>
\alt<future pen secondary><transformer>
\alt<pen secondary><transformer>
<pen tertiary>\is<pen secondary>
\alt<future pen secondary>
<pen expression>\is<pen tertiary>
\endsyntax
The constant '^@nullpen@' is just the single point $(0,0)$, which is
invisible---unless you use it in ^@filldraw@, which then reduces to
^@fill@. \ (A ^@beginchar@ command initializes "currentpen" to @nullpen@,
in order to reduce potentially dangerous dependencies between the programs
for different characters.) \
The surprise in these rules is the notion of a ","
which stands for a path or an ellipse that has not yet been converted
into METAFONT's internal representation of a true pen. The conversion process
is rather complicated, so METAFONT\ procrastinates until being sure that no
more transformations are going to be made. A true pen is formed at the
tertiary level, when future pens are no longer permitted in the syntax.

**[Dangerous Bend]** The distinction between pens and future pens would make no
difference to a user, except for another surprising fact: All of METAFONT's
pens are convex polygons, even the pens that are made from @pencircle@
and its variants! Thus, for example, the pen you get from an
untransformed pencircle is identical to the pen you get by specifying
the

>
@makepen@$\,\bigl((.5,0)\dashto(0,.5)\dashto(-.5,0)\dashto
(0,-.5)\dashto\cycle\bigr)$.

And the pens you get from '@pencircle@ scaled 20' and '@pencircle@
xscaled 30 yscaled 20' are polygons with 32 and 40 sides, respectively:
\displayfig 16a\&b (220\apspix)
The vertices of the polygons, shown as heavy dots in this illustration,
all have "half-integer" coordinates; i.e., each coordinate is either
an integer or an integer plus 1/2. Every polygon that comes from a
@pencircle@ is symmetric under $180^\circ$ rotation; furthermore,
there will be reflective left/right and top/bottom symmetry if the future
pen is a circle, or if it's an ellipse that has not been rotated.

**[Dangerous Bend]** This conversion to polygons explains why future pens must, in
general, be distinguished from ordinary ones. For example, the extra
parentheses in '(@pencircle@ xscaled 30) yscaled 20' will yield
a result quite different from the elliptical polygon just illustrated.
The parentheses force conversion of '@pencircle@ xscaled 30' from
future pen to pen, and this polygon turns out to be

>
$(12.5,-0.5) \dashto (15,0) \dashto (12.5,0.5)$
$\dashto (-12.5,0.5) \dashto
(-15,0) \dashto (-12.5,-0.5) \dashto\cycle$,

an approximation to a $30\times1$ ellipse. Then yscaling by 20 yields
\displayfig 16c (220\apspix)

**[Dangerous Bend]** Why does METAFONT\ work with polygonal approximations to circles,
instead of true circles? That's another good question. The main reason is
that suitably chosen polygons give better results than the real thing,
when is taken into account. For example, suppose we want
to draw a straight line of slope 1/2 that's exactly one pixel thick, from
$(0,y)$ to $(200,y+100)$. The image of a perfectly circular pen of
diameter 1 that travels along this line has outlines that run from
$(0,y\pm\alpha)$ to $(200,y+100\pm\alpha)$, where
$\alpha=\sqrt5/4\approx0.559$. If we digitize these outlines and fill the
region between them, we find that for some values of $y$ (e.g., $y=0.1$)
the result is a repeating pixel pattern like
'\smash{{$\vcenter{\offinterlineskip
={\manual R}
{\hphantom{$\,\ldots\,$}\kern5\copy4$\,\ldots\,$}
{\hphantom{$\,\ldots\,$}\kern3\copy4\copy4}
{\hphantom{$\,\ldots\,$}\kern\copy4\copy4}
{\smash{$\,\ldots\,$}\copy4}}$}}'; but for other values of $y$ (e.g.,
$y=0.3$) the repeating pattern of pixels is to11pt50 percent darker:
'\smash{2pt{$\vcenter{\offinterlineskip
={\manual R}
{\hphantom{$\,\ldots\,$}\kern4\copy4\copy4$\,\ldots\,$}
{\hphantom{$\,\ldots\,$}\kern2\copy4\copy4\copy4}
{\hphantom{$\,\ldots\,$}\copy4\copy4\copy4}
{\smash{$\,\ldots\,$}\copy4}}$}}'. Similarly, some diagonal
lines of slope 1 digitize to be twice as dark as others, when a truly
circular pen is considered. But the diamond-shaped nib that METAFONT\ uses
for a pencircle of diameter 1 does not have this defect; all straight
lines of the same slope will digitize to lines of uniform darkness.
Moreover, curved lines drawn with the diamond nib always yield one pixel per
column when they move more-or-less horizontally (with slopes between $+1$
and $-1$), and they always yield one pixel per row when they move vertically.
By contrast, the outlines of curves drawn with circular pens produce
occasional "blots." Circles and ellipses of all diameters can profitably
be replaced by polygons whose sub-pixel corrections to the ideal shape
will produce better digitizations; METAFONT\ does this in accordance with the
interesting theory developed by John D. in his Ph.D.
dissertation (Stanford University, 1985).

**[Double Dangerous Bend]** It's much easier to compute the outlines of a polygonal pen that
follows a given curve than to figure out the corresponding outlines of
a truly circular pen; thus polygons win over circles with respect
to both quality and speed. When a curve is traveling in a
direction between the edge vectors $z_k+1-z_k$ and $z_k-z_k-1$ of
a polygonal pen, the curve's outline will be offset from its center
by $z_k$. If you want fine control over this curve-drawing process,
METAFONT\ provides the primitive operation ' $w$ of $p$', where
$w$ is a vector and $p$ is a pen. If $w=(0,0)$, the result is $(0,0)$;
if the direction of $w$ lies strictly between $z_k+1-z_k$ and $z_k
-z_k-1$, the result is $z_k$; and if $w$ has the same direction as
$z_k+1-z_k$ for some $k$, the result is either $z_k$ or $z_k+1$,
whichever METAFONT\ finds most convenient to compute.

**[Double Dangerous Bend]** exercise Explain how to use penoffset to find the point or
points at the "top" of a pen (i.e., the point or points with largest
$y$ coordinate).

#### Answer
If there are two points $z_k$ and $z_k+1$ with maximum
$y$ coordinate, the value of 'penoffset $(-"infinity","epsilon")$ of $p$'
will be $z_k$ and 'penoffset $(-"infinity",-"epsilon")$ of $p$' will
be $z_k+1$; 'penoffset "left" of $p$' will be one or the other. If
there's only one top point, all three of these formulas will produce it.
\ (Actually METAFONT\ also allows pens to be made with three or more
vertices in a straight line. If there are more than two top vertices,
you can use penoffset to discover the first and the last, as above;
furthermore, if you really want to find them all, ^@makepath@ will produce
a path from which they can be deduced in a straightforward manner.)

**[Double Dangerous Bend]** The primitive operation '^@makepath@ $p$', where $p$ is
a (polygonal) pen whose vertices are $z_0$, $z_1$, \dots, $z_n-1$,
produces the path '$z_0\to\controls z_0\and z_1\to z_1\to*etc.*\to
z_n-1\to\controls z_n-1\and z_0\to\cycle$', which is one of the
paths that might have generated $p$. This gives access to all the
offsets of a pen.

**[Double Dangerous Bend]** When a @pencircle@ is transformed by any of the operations
in Chapter 15, it changes into an ellipse of some sort, since all of
METAFONT's transformations preserve ellipse-hood. The diameter of the
ellipse in each direction $\theta$ is decreased by $2\min\bigl(
\vert{\sin\theta}\vert,\vert{\cos\theta}\vert\bigr)$ times the current
value of ^"fillin", before converting to a polygon; this helps to
compensate for the variation in thickness of diagonal strokes with
respect to horizontal or vertical strokes, on certain output devices.
\ (METAFONT\ uses "fillin" only when creating polygons from ellipses,
but users can of course refer to "fillin" within their own routines
for drawing strokes.) \ The final polygon will never be perfectly flat
like ^@penrazor@, even if you say 'xscaled 0' and/or 'yscaled 0';
its center will always be surrounded at least by the basic diamond nib
that corresponds to a circle of diameter 1.

**[Dangerous Bend]** exercise Run METAFONT\ on the 'expr' file of Chapter 8 and look at
what is typed when you ask for "pencircle'' and "pencircle'
'scaled' '1.1''. \ (The first will exhibit the diamond nib, while
the second will show a polygon that's equivalent to @pensquare@.) \
Continue experimenting until you find the "threshold" diameter where
METAFONT\ decides to switch between these two polygons.

#### Answer
'@pencircle@ scaled 1.06060' is the diamond but
'@pencircle@ scaled 1.06061' is the square. \ (This assumes that
^"fillin"$=0$. If, for example, $"fillin"=.1$, the change doesn't
occur until the diameter is 1.20204.) \ The next change is at diameter
1.5, which gives a diamond twice the size of the first.

**[Dangerous Bend]** METAFONT's polygonal pens work well for drawing lines and curves,
but this pleasant fact has an unpleasant corollary: They do not always
digitize well at the , where curves start and stop. The
reason for this is explored further in Chapter 24; polygon vertices that
give nice uniform stroke widths might also be "ambiguous" points that
cause difficulties when we consider rounding to the raster. Therefore a
special ^@drawdot@ routine is provided for drawing one-point paths.
It is sometimes advantageous to apply @drawdot@ to the first and last
points of a path $p$, after having said '^@draw@ $p$'; this can
fatten up the endpoints slightly, making them look more consistent with
each other.

**[Dangerous Bend]** Plain METAFONT\ also provides two routines that can be used to clean up
endpoints in a different way: The command '^@cutoff@$\,(z,\theta)$'
removes half of the ^"currentpen" image at point $z$, namely all points
of the pen that lie in directions between $(\theta-90)^\circ$ and
$(\theta+90)^\circ$ from the center point. And the command '^@cutdraw@ $p$'
is an abbreviation for the following three commands:

>
@draw@ $p$; \ @cutoff@(point 0 of $p$, $180+$angle
direction 0 of $p$);
@cutoff@(point "infinity" of $p$, angle
direction "infinity" of $p$).

The effect is to draw a curve whose ends are clipped perpendicular to the
starting and ending directions. For example, the command

>
@cutdraw@ $z_4\to\controls z_1\and z_2\to z_6$

produces the following curve, which invites comparison with the corresponding
uncut version at the end of Chapter 3:
\displayfig 16d (5pc)

\decreasehsize 48mm

**[Dangerous Bend]** Here's another example of @cutoff@, in which the endpoints of
\rightfig 16e ({208\apspix} x {216\apspix}) ^15pt
METAFONT's '' have been cropped at $10^\circ$ angles to the
perpendicular of the stroke direction:

"'

pickup logo_pen;
top lft z1=(0,h); top rt z2=(w,h);
top z3=(.5w,h); z4=(.5w,0);
draw z1--z2;
cutoff(z1,170); cutoff(z2,-10);
draw z3--z4; cutoff(z4,-80).

"'

\restorehsize

**[Double Dangerous Bend]** The @cutoff@ macro of Appendix B deals with several things
that we've been studying recently, so it will be instructive to look
at it now (slightly simplified):

>
@def@ @cutoff@(@expr@ $z,"theta"$) $=$
$"cut\_pic":=@nullpicture@$;
^@addto@ "cut\_pic" @doublepath@ $z$ @withpen@ "currentpen";
@addto@ "cut\_pic" @contour@
$((0,-1)\dashto(1,-1)\dashto(1,1)\dashto(0,1)\dashto\cycle)$
scaled $1.42(1+\max(-"pen\_lft","pen\_rt","pen\_top",-"pen\_bot"))$
rotated "theta" shifted "z";
^@cull@ "cut\_pic" @keeping@ $(2,2)$ @withweight@ $-1$;
@addto@ "currentpicture" @also@ "cut\_pic" @enddef@.

The main work is done in a separate variable called "cut\_pic",
so that neighboring strokes won't be affected. First "cut\_pic" is set to
the full digitized pen image (by making a ^@doublepath@ from a single
point). Then a rectangle that includes the cutoff region is added in;
^"pen\_lft", "pen\_rt", "pen\_top", and "pen\_bot" are the quantities used
to compute the functions ^"lft", ^"rt", ^"top", and ^"bot", so they bound
the size of the pen. The culling operation produces the intersection of
pen and rectangle, which is finally subtracted from "currentpicture".

**[Double Dangerous Bend]** We shall conclude this chapter by studying two examples of how
METAFONT's pen-and-curve-drawing facilities can combine in interesting ways.
First, let's examine two "" characters
\displayfig 16f\&g (50\apspix)
which were both created by a single command of the form

>
@draw@ $z_1\to\controls z_2\and z_3\to z_4$.

The left example was done with a ^@pencircle@ xscaled .8"pt" yscaled .2"pt"
rotated 50, and the right example was exactly the same but with ^@pensquare@.
The control points $z_2$ and $z_3$ that made this work were defined by

>
$y_2-y_1=y_4-y_3=3(y_4-y_1)$;
$z_2-z_1=z_4-z_3="whatever"\astdir\,50$.

The second pair of equations is an old calligrapher's trick, namely to start
and finish a stroke in the direction of the pen you're holding.
The first pair of equations is a mathematician's trick, based on the
fact that the n polynomial} $t[0,3,-2,1]$ goes from
0 to 1 to 0 to 1 as $t$ goes from 0 to .25 to .75 to 1.

**[Double Dangerous Bend]** Next, let's try to draw a fancy with
the same two pens, holding them at a $20^\circ$ angle instead of a
$50^\circ$ angle. Here are two examples
\displayfig 16h\&i (195\apspix)
that can be created by '^@filldraw@' commands:

>
@filldraw@ $z_1\to\controls z_2\to z_3$
$\dashto("flex"(z_3,.5[z_3,z_4]+"dishing",z_4))$
shifted$\,(0,-"epsilon")$
$\dashto z_4\to\controls z_5\to z_6\dashto\cycle$.

The ^"dishing" parameter causes a slight rise between $z_3$ and $z_4$;
the ^"flex" has been lowered by ^"epsilon" in order to avoid the danger
of "," which might otherwise be caused by tiny loops
at $z_3$ or $z_4$. But the most interesting thing about this example
is the use of double control points, $z_2$ and $z_5$, in two of the
path segments. \ (Recall that '$\controls z_2$' means the same thing
as '$\controls z_2\and z_2$'.) \ These points were determined
by the equations

>
$x_2=x_1$; \ $z_2=z_3+"whatever"\astdir\,20$;
$x_5=x_6$; \ $z_5=z_4+"whatever"\astdir\,-20$;

thus, they make the strokes vertical at $z_1$ and $z_6$, parallel to the
pen angle at $z_3$, and parallel to the complementary angle at $z_4$.

\endchapter

The pen, probably more than any other tool,
has had the strongest influence upon lettering
in respect of serif design ...
It is probable that the letters [of the Trajan column]
were painted before they were incised,
and though their main structure is attributed to the pen
and their ultimate design to the technique of the chisel,
they undoubtedly owe much of their freedom
to the influence of the brush.

> --- L. C. , *Roman Lettering* (1938)

Remember that it takes time, patience, critical practice
and knowledge to learn any art or craft.
No "art experience" is going to result from any busy work
for a few hours experimenting with the edged pen.
... Take as much time as you require,
and do not become impatient.
If it takes a month to get it,
then be happy that it takes only a month.

> --- LLOYD , *Italic Calligraphy \& Handwriting* (1969)


# Chapter 17. Grouping

We have now covered all the visual, graphic aspects of METAFONT---its
points, paths, pens, and pictures; but we still don't know everything
about METAFONT's organizational, administrative aspects---its programs.
The next few chapters of this book therefore concentrate on
how to put programs together effectively.

A METAFONT\ program is a sequence of statements separated by semicolons and
followed by '^@end@'. More precisely, the syntax rules
\beginsyntax
<program>\is<statement list><statement>[end]
<statement list>\is<empty>\alt<statement>[;]<statement list>
\endsyntax
define a *program* in terms of a *statement*.

But what are ? Well, they are of various kinds. An "equation"
states that two expressions are supposed to be equal. An "assignment"
assigns the value of an expression to a variable. A "declaration"
states that certain variables will have a certain type.
A "definition" defines a macro. A "title" gives a descriptive name to
the character that is to follow. A "command" orders METAFONT\ to do some
specific operation, immediately. The "" tells METAFONT\ to
do absolutely nothing. And a "" is a list of other
statements treated as a .
\beginsyntax
<statement>\is<equation>\alt<assignment>\alt<declaration>
\alt<definition>\alt<title>\alt<command>\alt<empty>
\alt[begingroup] <statement list> <statement> [endgroup]
\endsyntax
We've given the syntax for *equation* and *assignment* in Chapter 10;
the syntax for *declaration* appeared in Chapter 7; *definition* and
*title* and *command* will appear in later chapters. Our main concern
just now is with the final type of *statement*, where @begingroup@
and @endgroup@ bind other statements into a unit, just as parentheses
add structure to the elements of an algebraic expression.

The main purpose of grouping is to protect the values of variables in
one part of the program from being clobbered in another. A symbolic token
can be given a new meaning inside a group, without changing the
meaning it had outside that group. \ (Recall that METAFONT\ deals with
three basic kinds of tokens, as discussed in Chapter 6; it is impossible
to change the meaning of a numeric token or a string token, but
symbolic tokens can change meanings freely.)

There are two ways to protect the values of variables in a group. One
is called a *save command*, and the other is called an *interim command*:
\beginsyntax
<save command>\is[save]<symbolic token list>
<symbolic token list>\is<symbolic token>
\alt<symbolic token list>[,]<symbolic token>
<interim command>\is[interim]
<internal quantity>[:=]<right-hand side>
\endsyntax
The symbolic tokens in a @save@ command all lose their current meanings, but
those old meanings are put into a safe place and restored at the end of
the current group. Each token becomes undefined, as if it had never
appeared before. For example, the command

>
@save@ $x,y$

effectively causes all previously known variables like $x_1$ and $y_5r$ to
become inaccessible; the variable $x_1$ could now appear in a new equation,
where it would have no connection with its out-of-group value. You could
also give the silly command

>
@save@ @save@;

this would make the token "save'' itself into a ^*tag* instead of a
^*spark*, so you couldn't use it to save anything else until the group ended.

**[Dangerous Bend]** An @interim@ command is more restrictive than a @save@, since it
applies only to an ^*internal quantity*. \ (Recall that internal
quantities are special variables like "tracingequations" that take numeric
values only; a complete list of all the standard internal quantities can
be found in Chapter 25, but that list isn't exhaustive because you can
define new ones for your own use.) \ METAFONT\ treats an interim command just
like an ordinary assignment, except that it undoes the assignment when the
group ends.

**[Dangerous Bend]** If you save something two or more times in the same group,
the first saved value takes precedence. For example, in the construction

>
@begingroup@
\dots
@interim@ $"autorounding":=0$; \ @save@ $x$;
\dots
@interim@ $"autorounding":=1$; \ @save@ $x$;
\dots
@endgroup@

the values of "autorounding" and $x$ after the end of the group will be
their previous values just before the statement '@interim@ $"autorounding":=0$'.
(Incidentally, these might not be the values they had upon entry to the group.)

**[Dangerous Bend]** Tokens and internal quantities regain their old meanings and
values at the end of a group only if they were explicitly saved in a
@save@ or @interim@ command. All other changes in meaning and/or value
will survive outside the group.

**[Dangerous Bend]** The ^@beginchar@ operation of plain METAFONT\ includes a @begingroup@,
and ^@endchar@ includes @endgroup@. Thus, for example, interim assignments
can be made in a program for one character without any effect on other
characters.

**[Dangerous Bend]** A *save command* that's not in a group simply clears the meanings
of the symbolic tokens specified; their old meanings are not actually saved,
because they never will have to be restored. An *interim command*
outside a group acts just like a normal assignment.

**[Dangerous Bend]** If you set the internal quantity ^"tracingrestores" to a positive
value, METAFONT\ will make a note in your transcript file whenever it is
restoring the former value of a symbolic token or internal quantity.
This can be useful when you're debugging a program that doesn't seem
to make sense.

Groups can also be used within algebraic expressions. This is
the other important reason for grouping; it allows METAFONT\ to do arbitrarily
complicated things while in the middle of other calculations, thereby
greatly increasing the power of macro definitions (which we shall study
in the next chapter). A has the general form

>
'begingroup'*statement list**expression*
'endgroup'

and it fits into the syntax of expressions at the primary level. The
meaning of a group expression is: "Perform the list of statements,
then evaluate the expression, then restore anything that was saved
in this group."

**[Dangerous Bend]** Group expressions belong in the syntax rules for each type
of expression, but they were not mentioned in previous chapters because
it would have been unnecessarily distracting. Thus, for example, the syntax for
*numeric primary* actually includes the additional alternative

>
'begingroup'*statement list**numeric expression*
'endgroup'.

The same goes for *pair primary*, *picture primary*, etc.; Chapter 25
has the complete rules of syntax for all types of expressions.

**[Dangerous Bend]** exercise What is the value of the expression

"'

begingroup x:=x+1; x endgroup + begingroup x:=2x; x endgroup

"'

if $x$ initially has the value $a$? What would the value have been if
the two group expressions had appeared in the opposite order?
Verify your answers using the 'expr' routine of Chapter 8.

#### Answer
$(a+1)+(2a+2)=3a+3$ and $(2a)+(2a+1)=4a+1$, respectively.
The final value of $x$ in the first case is $2a+2$, hence $a=.5x-1$;
'expr' will report the answer as '1.5x' (in terms of $x$'s new value),
since it has not been told about '$a$'. In the second case 'expr' will,
similarly, say '2x-1'.
This example shows that $\alpha+\beta$ is not necessarily equal
to $\beta+\alpha$, when $\alpha$ and $\beta$ involve
group expressions. METAFONT\ evaluates expressions strictly from left to
right, performing the statements within groups as they appear.

**[Dangerous Bend]** exercise Appendix B defines ^"whatever" to be an abbreviation for
the group expression '@begingroup@ @save@ ?; ? @endgroup@'. Why
does this work? \checkequals\Xwhat\exno

#### Answer
The save instruction gives '?'\ a fresh meaning, hence '?'\ is
a numeric variable unconnected to any other variables. When the group
ends and '?'\ is restored to its old meaning, the value of the group
expression no longer has a name. \ (It's called a "" if
you try to @show@ it.) \ Therefore the value of the group expression
is a new, nameless variable, as desired.

**[Double Dangerous Bend]** exercise What is the value of '@begingroup@ @save@ ?; \
$(?,?)$ @endgroup@'?

#### Answer
It's a nameless pair whose xpart and ypart are equal; thus it
is essentially equivalent to '$"whatever"\ast(1,1)$'.

**[Double Dangerous Bend]** exercise According to exercise 10.\xwhat, the assignment
'$x_3:="whatever"$' will make the numeric variable $x_3$ behave like new,
without affecting other variables like $x_2$. Devise a similar stratagem
that works for arrays of @picture@ variables.

#### Answer
'$v_3:=@begingroup@$ @save@ ?; @picture@ ?; ?\ @endgroup@'
refreshes the picture variable $v_3$ without changing other variables
like $v_2$. This construction works also for pairs, pens, strings, etc.

\endchapter

It is often difficult
to account for some beginners grouping right away
and others proving almost hopeless.

> --- A. G. , *Notes on Rifle Shooting* (1913)

Rock bands prefer San Francisco groupies to New York groupies.

> --- ELLEN , *But Now I'm Gonna Move* (1971)


# Chapter 18. Definitions (also called Macros)

You can often save time writing METAFONT\ programs by letting single tokens
stand for sequences of other tokens that are used repeatedly. For example,
Appendix B defines '$\ddashto$' to be an abbreviation for
'$\to\tension"infinity"\to$', and this definition is preloaded as
part of the plain METAFONT\ base. Programs that use such definitions are not
only easier to write, they're also easier to read. But Appendix B
doesn't contain every definition that every programmer might want;
the present chapter therefore explains how you can make
of your own.

In the simplest case, you just say

>
@def@ *symbolic token* $=$ *replacement text* @enddef@

and the symbolic token will henceforth expand into the tokens of the
replacement text. For example, Appendix B says

"'

def --- = ..tension infinity.. enddef;

"'

it makes '$z_1\ddashto z_2$' become '$z_1\to\tension"infinity"\to z_2$'.
The can be any sequence of tokens not including
'@enddef@'; or it can include entire subdefinitions like
'@def@ $\ldots$ @enddef@', according to certain rules
that we shall explain later.

Definitions get more interesting when they include ,
which are replaced by when the definition is expanded.
For example, Appendix B also says

"'

def rotatedaround(expr z,theta) =
shifted -z rotated theta shifted z enddef;

"'

this means that an expression like '$z_1$ $\,(z_2,30)$' will
expand into '$z_1$ shifted $-z_2$ rotated 30 shifted $z_2$'.

The parameters "z'' and "theta'' in this definition could have been any
symbolic tokens whatever; there's no connection between them and
appearances of "z'' and "theta'' outside the definition. \ (For example,
"z'' would ordinarily stand for "(x,y)'', but it's just a simple token
here.) \ The definition could even have been written with "primitive"
tokens as parameters, like

"'

def rotatedaround(expr;,+) =
shifted-; rotated+shifted; enddef;

"'

the effect would be exactly the same. \ (Of course, there's no point in
doing such a thing unless you are purposely trying to make your
definition inscrutable.)

When "rotatedaround'' is used, the arguments that are substituted for 'z'
and 'theta' are first evaluated and put into "," so that they
will behave like primary expressions. Thus, for example, '$z_1$
rotatedaround$\,(z_2+z_3,30)$' will not expand into '$z_1$ shifted $-z_2+z_3$
rotated 30 shifted $z_2+z_3$'---which means something entirely different---but
rather into '$z_1$ shifted $-\alpha$ rotated 30 shifted $\alpha$', where
$\alpha$ is a nameless internal variable that contains the value of
$z_2+z_3$.

**[Dangerous Bend]** A capsule value cannot be changed, so an @expr@ parameter should not
appear at the left of the operator '$:=$'.

**[Dangerous Bend]** Macros are great when they work, but complicated macros sometimes
surprise their creators. METAFONT\ provides "tracing" facilities so that you
can see what the computer thinks it's doing, when you're trying to
diagnose the reasons for unexpected behavior. If you say
'^"tracingmacros"$:=1$', the transcript file of your run will record
every macro that is subsequently expanded, followed by the values of its
arguments as soon as they have been computed.
For example, 'rotatedaround$\,("up",30)$' might produce a transcript
that includes the following diagnostic information:

"'

rotatedaround(EXPR0)(EXPR1)->
shifted-(EXPR0)rotated(EXPR1)shifted(EXPR0)
(EXPR0)<-(0,1)
(EXPR1)<-30

"'

**[Dangerous Bend]** Here's another example from Appendix B. It illustrates the
usefulness of in macro definitions:

>
@def@ $\,(@expr@\ p,q)$ $=$
transformed @begingroup@
^@save@ $T$; \ ^@transform@ $T$;
$p$ transformed $T$ $=$ $p$;
$q$ transformed $T$ $=$ $q$;
$T$ $=$ $-$ $T$;
$T$ $=$ $T$;
$T$ @endgroup@ @enddef@;

thus a new transform, $T$, is computed in the midst of another expression,
and the macro 'reflectedabout($p,q$)' essentially expands into
'transformed $T$'.

Some macros, like 'rotatedaround', are meant for general-purpose use.
But it's also convenient to write that simplify
the development of particular typefaces. For example, let's consider the
METAFONT\ logo from this standpoint. The program for '{\manual E}' in
Chapter 11 starts with

"'

beginchar("E",14u#+2s#,ht#,0); pickup logo_pen;

"'

and the programs for '{\manual M}', '{\manual T}',
etc., all have almost the same beginning. Therefore we might as
well put the following definition near the top of the file 'logo.mf':

"'

def beginlogochar(expr code, unit_width) =
beginchar(code,unit_width*u#+2s#,ht#,0);
pickup logo_pen enddef;

"'

Then we can start the '{\manual E}' by saying simply

"'

beginlogochar("E",14);

"'

similar simplifications apply to all seven letters. Notice from
this example that macros can be used inside macros (since "beginchar''
and "pickup'' are themselves macros, defined in Appendix B); once you
have defined a macro, you have essentially extended the METAFONT\ language.
Notice also that ^@expr@ parameters can be expressions of any type;
for example, '"E"' is a string, and the first parameter of
'rotatedaround' is a pair.

\decreasehsize 48mm
Chapter 11 didn't give the programs for '{\manual A}' or '{\manual O}'.
\rightfig 18a ({240\apspix} x {216\apspix}) ^15pt
It turns out that those programs can be simplified if we write
them in terms of an auxiliary subroutine called "super_half''.
For example, here is how the '{\manual O}' is made:

"'

beginlogochar("O",15);
x1=x4=.5w; top y1=h+o; bot y4=-o;
x2=w-x3=1.5u+s; y2=y3=barheight;
super_half(2,1,3);
super_half(2,4,3);
labels(1,2,3,4); endchar;

"'

\restorehsize\medbreak
The 'super_half' routine is supposed to draw half of a ,
through three points whose subscripts are specified.

\restorehsize
We could define 'super_half' as a macro with three @expr@ parameters,
referring to the first point as "z[i]'', say; but there's a better way.
Parameters to macros can be classified as suffixes, by saying ^@suffix@
instead of @expr@. In this case
the actual arguments may be any ^*suffix*, i.e., any sequence of
subscripts and tags that complete the name of a variable as explained
in Chapter 7. Here's what 'super_half' looks like, using this idea:

"'

def super_half(suffix i,j,k) =
draw z.i0,y.j-y.i
... (.8[x.j,x.i],.8[y.i,y.j])z.j-z.i
... z.jx.k-x.i,0
... (.8[x.j,x.k],.8[y.k,y.j])z.k-z.j
... z.k0,y.k-y.j enddef;

"'

### Exercise
Would the program for '{\manual O}' still work if the two calls of
'super_half' had been "super_half(3,1,2)'' and "super_half(3,4,2)''?

#### Answer
Yes; the direction at 'z.j' will be either "left" or "right".

### Exercise
Guess the program for METAFONT's '{\manual A}', which has the
same width as '{\manual O}'.

#### Answer
'beginlogochar("A",15);'
\rightfig A18a ({240\apspix} x {216\apspix}) ^3pt break
'x1=.5w;'break
'x2=x4=leftstemloc;'break
'x3=x5=w-x2;'break
'top y1=h+o;'break
'y2=y3=barheight;'break
'bot y4=bot y5=-o;'break
'draw z4--z2--z3--z5;'break
'super_half(2,1,3);'break
'labels(1,2,3,4,5);'break
'endchar;'
Notice that all three calls of 'super_half' in 'logo.mf' are of the form
'"super\_half"$(2,j,3)$'. But it would not be good style to eliminate
parameters $i$ and $k$, even though 'super_half' is a
subroutine; that would make it too too special.

**[Dangerous Bend]** Besides parameters of type @expr@ and @suffix@, METAFONT\ also
allows a third type called ^@text@. In this case the actual argument
is any sequence of tokens, and this sequence is not evaluated
beforehand; a text argument is simply copied in place of the
corresponding parameter. This makes it possible to write macros that
deal with lists of things. For example, Appendix B's '@define\_pixels@'
macro is defined thus:

"'

def define_pixels(text t) =
forsuffixes a=t: a := a# * hppp; endfor enddef;

"'

this means that "define_pixels(em,cap)'' will expand into

"'

forsuffixes a=em,cap: a := a# * hppp; endfor

"'

which, in turn, expands into the tokens "em' ':=' 'em#' '*' 'hppp;'
'cap' ':=' 'cap#' '*' 'hppp;'' as we will see in Chapter 19.

**[Dangerous Bend]** Let's look now at a subroutine for drawing , since
this typifies the sort of special-purpose macro one expects to see
in the design of a meta-typeface. Serifs can take many forms,
so we must choose from myriads of possibilities. We shall consider
two rather different approaches, one based on outline-filling and the
other based on the use of a fixed pen nib. In both cases it will be
necessary to omit some of the refinements that would be desirable
in a complete typeface design, to keep the examples from
getting too complicated.

**[Dangerous Bend]**
shape 13
3pc 13pc
3pc 13pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 16pc
0pc 29pc
Our first example is a serif routine that
constructs six points $z_{\$a}$, $z_{\$b}$, \dots, $z_{\$\mkern-1muf}$ around a
\rightfig 18b (48mm x 40mm) ^26pt
given triple of "" points $z_{\$l}$, $z_{\$}$, $z_{\$r}$; here
\$ is a suffix that's a parameter to the "serif" macro. Other parameters
are: "breadth", the distance between the parallel lines that run from
$z_{\$l}$ to $z_{\$a}$ and from $z_{\$r}$ to $z_{\$\mkern-1muf}$; "theta", the
direction angle of those two lines; "left\_jut", the distance from
$z_{\$l}$ to $z_{\$b}$; and "right\_jut", the distance from $z_{\$r}$ to
$z_{\$e}$. \ (The serif "juts out" by the amounts of the
parameters.) \ There's also a "serif\_edge" macro, which constructs
the path shown. The routines refer to three variables that are assumed to
apply to all serifs: "slab", the vertical distance from $z_{\$b}$
and $z_{\$e}$ to $z_{\$c}$ and $z_{\$d}$; "bracket", the vertical distance
from $z_{\$a}$ and $z_{\$\mkern-1muf}$ to $z_{\$l}$ and $z_{\$r}$; and
"serif\_darkness", a fraction that controls how much of the triangular
regions $(z_{\$a},z_{\$l},z_{\$b})$ and $(z_{\$\mkern-1muf},z_{\$r},z_{\$e})$
will be filled in.

>
@def@ "serif"(@suffix@ \$)(@expr@
$"breadth","theta","left\_jut","right\_jut")=$
$\penpos\$("breadth"/abs\,sind\,"theta",0)$;
$z_{\$a}-z_{\$l}=z_{\$\mkern-1muf}-z_{\$r}=
("bracket"/abs\,sind\,"theta")\ast dir\,"theta"$;
$y_{\$c}=y_{\$d}$; \ $y_{\$b}=y_{\$e}=y_\$$; \
$y_{\$b}-y_{\$c}=@if@\;"theta"<0\colon\;-\;@fi@\;"slab"$;
$x_{\$b}=x_{\$c}=x_{\$l}-"left\_jut"$; \
$x_{\$d}=x_{\$e}=x_{\$r}+"right\_jut"$;
@labels@$(\$a,\$b,\$c,\$d,\$e,\$\mkern-1muf)$ @enddef@;

@def@ "serif\_edge" @suffix@ \$ =
$\bigl("serif\_bracket"(\$a,\$l,\$b)\dashto z_{\$c}$
$\dashto z_{\$d}\dashto reverse\,
"serif\_bracket"(\$\mkern-1muf,\$r,\$e)\bigr)$ @enddef@;

@def@ "serif\_bracket"(@suffix@ $i,j,k$) $=$
$\bigl(z.i\{z.j-z.i\}
\ldots"serif\_darkness"[z.j,.5[z.i,z.k]\,]\{z.k-z.i\}$
$\ldots z.k\{z.k-z.j\}\bigr)$ @enddef@;

**[Dangerous Bend]** exercise Under what circumstances will the "serif\_edge"
go through points $z_{\$l}$ and $z_{\$r}$?

#### Answer
If $"bracket"=0$ or $"serif\_darkness"=0$. \ (It's probably
not a good idea to make $"serif\_darkness"=0$, because this would lead to
an extreme case of the '$\ldots$' triangle, which might not
be numerically stable in the presence of rounding errors.)
Another case, not really desirable, is $"left\_jut"="right\_jut"=0$.

**[Dangerous Bend]** exercise Should this "serif" macro be used before
points $z_{\$l}$, $z_\$$, and $z_{\$r}$ have been defined, or should those
points be defined first?

#### Answer
That's a strange question. The "serif" routine includes a
"penpos" that defines $z_{\$l}$, $z_\$$, and $z_{\$r}$ relative
to each other, and it defines the other six points relative to them.
Outside the routine the user ought to specify just one $x$ coordinate
and one $y$ coordinate, in order to position all of the points.
This can be done either before or after "serif" is called, but
METAFONT\ has an easier job if it's done beforehand.

**[Dangerous Bend]** Here are two sample letters that show how these serif routines
might be used. The programs assume that the font has several additional
ad hoc parameters: $u$, a unit of character width; "ht", the character
height; "thin" and "thick", the two stroke weights; and "jut", the amount
by which serifs protrude on a "normal" letter like 'H'.

\displayfig 18c (252\apspix)
$$ to\indent#1em plus1fil minus1fil
&0pt\%\ #
@beginchar@('"A"'$,13u\0,"ht"\0,0)$;
$z_1=(.5w,1.05h)$;&top point
$x_4l=w-x_5r=u$; \ $y_4l=y_5r="slab"$;&bottom points
@numeric@ $"theta"[\,]$;
$"theta"_4=angle(z_1-z_4l)$;&left stroke angle
$"theta"_5=angle(z_1-z_5r)$;&right stroke angle
$"serif"(4,"thin","theta"_4,.6"jut","jut")$;&left serifs
$"serif"(5,"thick","theta"_5,"jut",.6"jut")$;&right serifs
$z_0=z_4r+"whatever"\astdir\,"theta"_4$
$=z_5l+"whatever"\astdir\,"theta"_5$;&inside top point
@fill@ $z_1\dashto "serif\_edge"_4\dashto z_0$&the left stroke
$\&\;z_0\dashto "serif\_edge"_5\dashto z_1\;\&\;\cycle$;&the
right stroke
$\penpos2("whatever","theta"_4)$;
$\penpos3("whatever","theta"_5)$;
$y_2r=y_3r=.5[y_4,y_0]$;&crossbar height
$y_2l=y_3l=y_2r-"thin"$;&crossbar thickness
$z_2="whatever"[z_1,z_4r]$;
$z_3="whatever"[z_1,z_5l]$;
@penstroke@ $z_2e\dashto z_3e$;&the crossbar
@penlabels@$(0,1,2,3,4,5)$; \ @endchar@;

@beginchar@('"I"'$,6u\0,"ht"\0,0)$;
$x_1=x_2=.5w$;
$y_1=h-y_2$; \ $y_2="slab"$;
"serif"$(1,"thick",-90,1.1jut,1.1"jut")$;&upper serifs
"serif"$(2,"thick",90,1.1jut,1.1"jut")$;&lower serifs
@fill@ $"serif\_edge"_2\dashtoreverse\,"serif\_edge"_1\dashto\cycle$;
&the stroke
@penlabels@$(1,2)$; \ @endchar@;

The illustration was prepared with $"thin"=.5"pt"$, $"thick"=1.1"pt"$,
$u=.6"pt"$, $"ht"=7"pt"$, $"slab"=.25"pt"$, $"jut"=.9"pt"$, $"bracket"="pt"$,
and $"serif\_darkness"=1/3$.

**[Dangerous Bend]** exercise Could the equations defining $y_1$ and $y_2$ in the program
for '"I"' have been replaced by '$y_1c=h$' and '$y_2c=0$'?

#### Answer
Yes; see the previous exercise. \ (But in the program for '"A"'
it's necessary to define $y_4l$ and $y_5r$, so that $"theta"_4$
and $"theta"_5$ can be calculated.)

**[Dangerous Bend]** exercise Write the program for an '"H"' to go with these letters.

#### Answer
\rightfig A18b (48mm x 43mm) ^10pt
@beginchar@('"H"'$,13u\0,"ht"\0,0)$;break
$x_1=x_2=x_5=3u$;break
$x_3=x_4=x_6=w-x_1$;break
$y_1c=y_3c=h$; \ $y_2c=y_4c=0$;break
$"serif"(1,"thick",-90,"jut","jut")$;break
$"serif"(2,"thick",90,"jut","jut")$;break
$"serif"(3,"thick",-90,"jut","jut")$;break
$"serif"(4,"thick",90,"jut","jut")$;break
@fill@ $"serif\_edge"_2$break
$\dashtoreverse\,"serif\_edge"_1\dashto\cycle$;break
@fill@ $"serif\_edge"_4$break
$\dashtoreverse\,"serif\_edge"_3\dashto\cycle$;break
$\penpos5("thin",90)$; \ $\penpos6("thin",90)$;break
$y_5=y_6=.52h$; \ @penstroke@ $z_5e\dashto z_6e$;break
@penlabels@$(1,2,3,4,5,6)$; \ @endchar@.

**[Double Dangerous Bend]** A second approach to serifs can be based on the example at
the end of Chapter 16. In this case we assume that "broad\_pen" is
a '@pensquare@ xscaled "px" yscaled "py" rotated "phi"' for
some $"px">"py"$ and some small angle "phi". Thicker strokes will
be made by using this pen to fill a larger region; the serif routine
is given the distance "xx" between $z_{\$l}$ and $z_{\$r}$.
There's a pair variable called "dishing" that
controls the curvature between $z_{\$c}$ and $z_{\$d}$. Top and
bottom serifs are similar, but they are sufficiently different that it's
easier to write separate macros for each case.

>
@def@ "bot\_serif"(@suffix@ \$)(@expr@ $"xx","theta",
"left\_jut","right\_jut")=$
$\penpos\$("xx",0)$; \
$z_{\$a}-z_{\$l}=z_{\$\mkern-1muf}-z_{\$r}=
("bracket"/abs\,sind\,"theta")\astdir\,"theta"$;
$y_{\$c}="top"\,y_{\$l}$; \ $y_{\$d}=y_{\$r}$; \
$x_{\$c}=x_{\$l}-"left\_jut"$; \ $x_{\$d}=x_{\$r}+"right\_jut"$;
$z_{\$b}=z_{\$l}+"whatever"\astdir\,"theta"
=z_{\$c}+"whatever"\astdir\,"phi"$;
$z_{\$e}=z_{\$r}+"whatever"\astdir\,"theta"
=z_{\$d}+"whatever"\astdir\,-"phi"$;
@labels@$(\$a,\$b,\$c,\$d,\$e,\$\mkern-1muf)$ @enddef@;

@def@ "bot\_serif\_edge" @suffix@ \$ $=$
$\bigl(z_{\$a}\to\controls z_{\$b}\to z_{\$c}$
$\dashto("flex"(z_{\$c},.5[z_{\$c},z_{\$d}]+"dishing",
z_{\$d}))$ shifted $(0,-"epsilon")$
$\dashto z_{\$d}\to\controls z_{\$e}\to z_{\$\mkern-1muf}
\bigr)$ @enddef@;

\displayfig 18d (272\apspix)

>
@beginchar@('"A"'$,13u\0,"ht"\0,0)$; \ @pickup@ "broad\_pen";
$z_1=(.5w,"top"\,h)$; \ $"lft"\,x_4l=w-"rt"\,x_5r=1.2u$; \
$y_4l=y_5r=0$;
@numeric@ $"theta"[\,]$; \ $"theta"_4=angle(z_1-z_4l)$; \
$"theta"_5=angle(z_1-z_5r)$;
@numeric@ "xxx";
spread-8pt{
$"px"\astsind("theta"_5-"phi")+"xxx"\astsind\,"theta"_5
= "px"\astcosd\,"phi"+"xx"$};
$"bot\_serif"(4,0,"theta"_4,.8"jut",.8"jut")$; \
$"bot\_serif"(5,"xxx","theta"_5,.6"jut",.8"jut")$;
$z_0=z_4r+"whatever"\astdir\,"theta"_4
=z_5l+"whatever"\astdir\,"theta"_5$;
@filldraw@ $z_1\dashto "bot\_serif\_edge"_4
\dashto z_0\;\&\;z_0\dashto "bot\_serif\_edge"_5
\dashto z_1\;\&\;\cycle$;
$"top"\,y_2="top"\,y_3=.45"bot"\,y_0$; \
$z_2="whatever"[z_1,z_4r]$; \ $z_3="whatever"[z_1,z_5l]$;
@draw@ $z_2\dashto z_3$; \ @penlabels@$(0,1,2,3,4,5)$; @endchar@;

@beginchar@('"I"'$,6u\0,"ht"\0,0)$; \ @pickup@ "broad\_pen";
$x_1=x_2=.5w$; \ $y_1=h$; \ $y_2=0$;
$"top\_serif"(1,"xx",-90,1.1"jut",1.1"jut")$; \
$"bot\_serif"(2,"xx",90,1.1"jut",1.1"jut")$;
@filldraw@ $"bot\_serif\_edge"_2\dashto
reverse\,"top\_serif\_edge"_1\dashto\cycle$;
@penlabels@$(1,2)$; \ @endchar@;

In the illustration, $"px"=.8"pt"$, $"py"=.2"pt"$, $"phi"=20$,
$"xx"=.3"pt"$, $u=.6"pt"$, $"ht"=7"pt"$, $"jut"=.9"pt"$, $"bracket"="pt"$,
and $"dishing"=(.25"pt",0)$ rotated 20.

**[Double Dangerous Bend]** exercise Write the missing code for "top\_serif" and
"top\_serif\_edge".

#### Answer
@def@ "top\_serif"(@suffix@ \$)(@expr@ $"xx","theta",
"left\_jut","right\_jut")=$break
$\penpos\$("xx",0)$; \
$z_{\$a}-z_{\$l}=z_{\$\mkern-1muf}-z_{\$r}=
("bracket"/abs\,sind\,"theta")\astdir\,"theta"$;break
$y_{\$c}=y_{\$d}=y_\$$; \
$x_{\$c}=x_{\$l}-"left\_jut"$; \ $x_{\$d}=x_{\$r}+"right\_jut"$;break
$z_{\$b}=z_{\$l}+"whatever"\astdir\,"theta"
=z_{\$c}+"whatever"\astdir\,-"phi"$;break
$z_{\$e}=z_{\$r}+"whatever"\astdir\,"theta"
=z_{\$d}+"whatever"\astdir\,"phi"$;break
@labels@$(\$a,\$b,\$c,\$d,\$e,\$\mkern-1muf)$ @enddef@;
\indent
@def@ "top\_serif\_edge" @suffix@ \$ $=$break
$\bigl(z_{\$a}\to\controls z_{\$b}\to z_{\$c}$break
$\dashto("flex"(z_{\$c},.5[z_{\$c},z_{\$d}]-"dishing",
z_{\$d}))$ shifted $(0,+"epsilon")$break
$\dashto z_{\$d}\to\controls z_{\$e}\to z_{\$\mkern-1muf}
\bigr)$ @enddef@;

**[Double Dangerous Bend]** exercise (For mathematicians.) \
Explain the equation for "xxx" in the program for '"A"'.

#### Answer
Assuming that $"py"=0$, the effective right stroke weight would be
$"px"\cdot\sin(\theta_5-\phi)$ if it were drawn with one stroke of "broad\_pen",
and $"xxx"\cdot\sin\theta_5$ is the additional weight corresponding to separate
strokes "xxx" apart. The right-hand side of the equation is the same
calculation in the case of vertical strokes ($\theta=90^\circ$), when the
stroke weight of '"I"' is considered. \ (Since a similar calculation
needs to be done for the letters K, V, W, X, Y, and Z, it would be a good
idea to embed these details in another macro.)

**[Double Dangerous Bend]** exercise Write the program for an '"H"' to go with these letters.

#### Answer
\rightfig A18c (48mm x 45mm) ^10pt
@beginchar@('"H"'$,13u\0,"ht"\0,0)$; \ @pickup@ "broad\_pen";break
$x_1=x_2=x_5=3u$;break
$x_3=x_4=x_6=w-x_1$;break
$y_1=y_3=h$; \ $y_2=y_4=0$;break
$"top\_serif"(1,"xx",-90,"jut","jut")$;break
$"bot\_serif"(2,"xx",90,"jut","jut")$;break
$"top\_serif"(3,"xx",-90,"jut","jut")$;break
$"bot\_serif"(4,"xx",90,"jut","jut")$;break
@filldraw@ $"bot\_serif\_edge"_2$break
$\dashtoreverse\,"top\_serif\_edge"_1\dashto\cycle$;break
@filldraw@ $"bot\_serif\_edge"_4$break
$\dashtoreverse\,"top\_serif\_edge"_3\dashto\cycle$;break
$y_5=y_6=.52h$; \ @draw@ $z_5\dashto z_6$;break
@penlabels@$(1,2,3,4,5,6)$; \ @endchar@.

**[Dangerous Bend]** A close look at the "serif\_edge" routines in these examples
will reveal that some parentheses are curiously lacking: We said
'@def@ "serif\_edge" @suffix@ \$' instead of
'@def@ "serif\_edge"(@suffix@ \$)', and we used the macro by saying
'$"serif\_edge"_5$' instead of
'$"serif\_edge"(5)$'. The reason is that METAFONT\ allows the final parameter
of a macro to be without delimiters; this is something that could not
have been guessed from a study of previous examples. It is time now
to stop looking at specific cases and to start examining the complete
set of rules for macro definitions. Here is the syntax:
\beginsyntax
<definition>\is<definition heading><is><replacement text>[enddef]
<is>\is[=]\alt[:=]
<definition heading>\is[def]<symbolic token><parameter heading>
\alt<vardef heading>
\alt<leveldef heading>
<parameter heading>\is<delimited parameters><undelimited parameters>
<delimited parameters>\is<empty>
\alt<delimited parameters>[(]<parameter type><parameter tokens>[)]
<parameter type>\is[expr]
\alt[suffix]
\alt[text]
<parameter tokens>\is<symbolic token>
\alt<parameter tokens>[,]<symbolic token>
<undelimited parameters>\is<empty>
\alt[primary]<symbolic token>
\alt[secondary]<symbolic token>
\alt[tertiary]<symbolic token>
\alt[expr]<symbolic token>
\alt[expr]<symbolic token>[of]<symbolic token>
\alt[suffix]<symbolic token>
\alt[text]<symbolic token>
\endsyntax
(We'll discuss ^*vardef heading* and ^*leveldef heading* in Chapter 20.)
\ The basic idea is that we name the macro to be defined, then we name
zero or more delimited parameters (i.e., parameters in parentheses),
then we name zero or one or two undelimited parameters.
Then comes an '$=$' sign,
followed by the replacement text, and @enddef@. The '$=$' sign might also
be '$:=$'; both mean the same thing.

**[Dangerous Bend]** Delimited parameters are of type @expr@, @suffix@, or @text@;
two or more parameters of the same type may be listed together, separated
by commas. For example, '(@expr@ $a,b$)' means exactly the same thing as
'(@expr@ $a$)(@expr@ $b$)'. Undelimited parameters have eight possible
forms, as shown in the syntax.

**[Dangerous Bend]** The *replacement text* is simply filed away for future use,
not interpreted, when METAFONT\ reads a definition. But a few tokens are
treated specially:\enddanger\nobreak

- @def@, ^@vardef@, ^@primarydef@, ^@secondarydef@, and
^@tertiarydef@ are considered to introduce definitions inside definitions.

- @enddef@ ends the replacement text, unless it matches a
previous @def@-like token (as listed in the preceding rule).

- Each *symbolic token* that stands for a parameter, by
virtue of its appearance in the *parameter heading* or \<leveldef
heading>, is changed to a special in\-ternal "parameter
token" wherever it occurs in the
replacement text. Whenever this special token is subsequently encountered,
METAFONT\ will substitute the appropriate argument.

- ^@quote@ disables any special interpretation of the immediately
following token. A '@quote@' doesn't survive in the replacement text
(unless, of course, it has been quoted).

**[Dangerous Bend]** exercise Check your understanding of these rules by
figuring out what the replacement text is, in the following weird definition:

"'

def foo(text t) expr e of p :=
def t = e enddef; quote def quote t = p enddef

"'

#### Answer
The replacement text contains ten tokens,

>
okdef*t*ok=*e*okenddef
ok;okdefoktok=*p*

where *t*, *e*, and *p* are placeholders for argument insertion.
When this macro is expanded with $"tracingmacros">0$, METAFONT\ will type

"'

foo(TEXT0)<expr>of<primary>->def(TEXT0)=(EXPR1)enddef;def.t=(EXPR2)

"'

followed by the arguments '(TEXT0)', '(EXPR1)', and '(EXPR2)'.

**[Dangerous Bend]** METAFONT\ does not expand macros when it reads a *definition*;
but at almost all other times it will replace a defined token by the
corresponding replacement text, after finding all the arguments.
The replacement text will then be read as if it had been present
in the program all along.

**[Dangerous Bend]** How does METAFONT\ determine the arguments to a macro? Well,
it knows what kinds of arguments to expect, based on the parameter
heading. Let's consider delimited arguments first:\enddanger\nobreak

- A delimited
@expr@ argument should be of the form '(*expression*)'; the expression
is evaluated and put into a special "" token that will be
substituted for the parameter wherever it appears in the replacement text.

- A delimited @suffix@ argument should be of the form
'(*suffix*)'; subscripts that occur in the suffix are evaluated
and replaced by numeric tokens. The result is a list of zero or more
tokens that will be substituted for the parameter wherever it appears
in the replacement text.

- A delimited @text@ argument should be of the form
'(*text*)', where *text* is any sequence of tokens that is balanced
with respect to the delimiters surrounding it. This sequence of tokens
will be substituted for the parameter wherever it appears in the
replacement text.

- When there are two or more delimited parameters, you can
separate the arguments by commas instead of putting parentheses around
each one. For example, three delimited arguments could be written
either as '$(a)(b)(c)$' or '$(a,b)(c)$' or '$(a)(b,c)$' or '$(a,b,c)$'.
However, this abbreviation doesn't work after text arguments, which
must be followed by ')' because text arguments can include commas.

**[Double Dangerous Bend]** Chapter 8 points out that you can use other
besides parentheses. In general, a comma following a delimited
@expr@ or @suffix@ argument is equivalent to two tokens ')(',
corresponding to whatever delimiters enclose that comma.

**[Double Dangerous Bend]** exercise After "def' 'f(expr' 'a)(text' 'b,c)=...enddef''
and "delimiters' '' ''', what are the arguments in
"fx,(,((}}))''?

#### Answer
According to the rule just stated, the first comma is an
abbreviation for "}}' '{{''. Hence the first argument is a capsule
containing the value of $x$; the second is the text "(,'';
the third is the text "(}})''.

**[Dangerous Bend]** The rules for undelimited arguments are similar. An
undelimited @primary@, @secondary@, @tertiary@, or @expr@ is the
longest syntactically correct ^*primary*, ^*secondary*, ^*tertiary*,
or ^*expression* that immediately follows the delimited arguments.
An undelimited '@expr@ $x$ $y$' specifies two arguments, found
by taking the longest syntactically correct '*expression* of *primary*'.
In each of these cases, the expression might also be preceded by an
optional '' or ''. An undelimited @suffix@ is the longest
*suffix* that immediately follows the delimited arguments; METAFONT\ also
allows '(*suffix*)' in this case, but not '=*suffix*' or ':=*suffix*'.
An undelimited @text@ essentially runs to the end of the current
statement; more precisely, it runs to the first ';'\ or '^@endgroup@' or
'^@end@' that is not part of a within the argument.

**[Dangerous Bend]** Appendix B contains lots of macros that illustrate these
rules. For example,

>
@def@ ^@fill@ @expr@ $c$ $=$ @addto@ "currentpicture" @contour@ $c$ @enddef@;
@def@ ^@erase@ @text@ $t$ $=$ @cullit@; \ $t$ @withweight@ $-1$;
@cullit@ @enddef@;

these are slight simplifications of the real definitions, but they retain the
basic ideas. The command '@erase@ @fill@ $p$' causes '@fill@ $p$' to be
the @text@ argument to @erase@, after which '$p$' becomes the @expr@
argument to @fill@.

**[Double Dangerous Bend]** exercise The '@pickup@' macro in Appendix B starts with
'@def@ @pickup@ @secondary@ $q$'; why is the argument a secondary
instead of an expression?

#### Answer
This snares s before they're converted to pens, because
@pickup@ wants to yscale by "aspect\_ratio" before ellipses change to
polygons.

**[Double Dangerous Bend]** exercise Explain why the following '^"hide"' macro allows you to
hide any sequence of statements in the midst of an expression:

>
@def@ "hide"(@text@ $t)="gobble"@begingroup@\,t;$ @endgroup@ @enddef@;
@def@ "gobble" @primary@ $g=@enddef@$;

#### Answer
The construction '"hide"(*statement list*)' expands into
'"gobble" @begingroup@ *statement list*; @endgroup@', so the
argument to "gobble" must be evaluated. The @begingroup@ causes METAFONT\
to start executing statements. When that has been done, the final
statement turns out to be *empty*, so the argument to "gobble"
turns out to be a expression (cf.\ Chapter 25). Finally,
"gobble"'s replacement text is empty, so the hidden text has indeed
disappeared. \ (The @hide@ macro in Appendix B is actually a bit
more efficient, but a bit trickier.)

\endchapter

DEFINI$'$TION, s. \ [definitio, Latin.]
1. A short description of a thing by its properties.

> --- SAMUEL , *A Dictionary of the English Language* (1755)

DEFINI$"$TION, n. \ [*L.* definitio. See Define.]
1. A brief description of a thing by its properties;
as a definition of wit or of a circle.
or NOAH , *An American
Dictionary of the English Language* (1828)


# Chapter 19. Conditions and Loops

If decisions never had to be made, life would be much easier, and so would
programming. But sometimes it is necessary to choose between alternatives,
and METAFONT\ allows programs to take different paths depending on the circumstances.
You just say something like

>
@if@ not "decisions": \ $"life":="programming":="easier"("much")$
@elseif@ $"choice"=a$: \ "program\_a"
@else@: \ "program\_b" \ @fi@

which reduces, for example, to '"program\_b"' if and only if
$"decisions"=@true@$ and $"choice"\ne a$. The normal left-to-right
order of program interpretation can also be modified by specifying
"," which tell the computer to read certain tokens repeatedly,
with minor variations, until some becomes true. We have
seen many examples of these mechanisms already; the purpose of the
present chapter is to discuss the entire range of possibilities.

METAFONT's conditions and loops are different from those in most other
programming languages, because the conditional or iterated code does
not have to fit into the syntactic structure. For example, you can
write strange things like

"'

p = (if b: 0,0)..(1,5 else: u,v fi)

"'

where the conditional text '$0,0)\to(1,5$' makes no sense by itself,
although it becomes meaningful when read in context. In this respect
conditions and loops behave like macros. They specify rules of
token transformation that can be said to take place in METAFONT's ""
before the tokens are actually digested in the computer's "."

The first conditional example above has three alternatives, in the form

>
@if@ *boolean$_1$*: *text$_1$* \
@elseif@ *boolean$_2$*: *text$_2$* \
@else@: *text$_3$* \ @fi@

and the second example has just two; there can be any number of
'^@elseif@' clauses before '^@else@:'. Only one of the conditional
texts will survive, namely the first one whose condition is true;
'@else@:'\ is always true. You can also omit '@else@:'\
entirely, in which case '@else@:*empty*' is implied just before
the closing '^@fi@'. For example, plain METAFONT's @mode\_setup@ routine
includes the conditional command

>
@if@ unknown "mag": \ $"mag":=1$; \ @fi@

whose effect is to set "mag" equal to 1 if it hasn't already received
a value; in this case there's only one alternative.

### Exercise
Would it be wrong to put the ';'\ after the '@fi@' in the example
just given?

#### Answer
Then METAFONT's "stomach" would see ';'\ if "mag" is known, but there
would be no change if "mag" is unknown. An extra semicolon is harmless,
since METAFONT\ statements can be *empty*. But it's wise to get in the habit
of putting ';'\ before @fi@, because it saves a wee bit of time and because
';'\ often belongs before ^@endfor@.

**[Dangerous Bend]** The informal rules just stated can, of course, be expressed more
formally as rules of syntax:
\beginsyntax
<condition>\is[if]<boolean expression>[:]<conditional text><alternatives>[fi]
<alternatives>\is<empty>
\alt[else][:]<conditional text>
\alt[elseif]<boolean expression>[:]<conditional text><alternatives>
\endsyntax
Every conditional construction begins with '^@if@' and ends with
'@fi@'. The conditional texts are any sequences of tokens that are
balanced with respect to '@if@' and '@fi@'; furthermore,
'@elseif@' and '@else@' can occur in a conditional text only when
enclosed by '@if@' and '@fi@'.

**[Dangerous Bend]** Each '@if@' and '@elseif@' must be followed by a
*boolean expression*, i.e., by an expression whose value is either
'@true@' or '@false@'. are named after George
, the founder of algebraic approaches to logic. Chapter 7 points
out that variables can be of type ^@boolean@, and numerous examples of
boolean expressions appear in Chapter 8. It's time now to be more
systematic, so that we will know the facts about boolean expressions just
as we have become well-versed in numeric expressions, pair expressions,
picture expressions, path expressions, transform expressions, and pen
expressions. Here are the relevant syntax rules:
\beginsyntax
<boolean primary>\is<boolean variable>
\alt[true]\alt[false]
\alt[(]<boolean expression>[)]
\alt[begingroup]<statement list><boolean expression>[endgroup]
\alt[known]<primary>\alt[unknown]<primary>
\alt<type><primary>\alt[cycle]<primary>
\alt[odd]<numeric primary>
\alt[not]<boolean primary>
<boolean secondary>\is<boolean primary>
\alt<boolean secondary>[and]<boolean primary>
<boolean tertiary>\is<boolean secondary>
\alt<boolean tertiary>[or]<boolean secondary>
<boolean expression>\is<boolean tertiary>
\alt<numeric expression><relation><numeric tertiary>
\alt<pair expression><relation><pair tertiary>
\alt<transform expression><relation><transform tertiary>
\alt<boolean expression><relation><boolean tertiary>
\alt<string expression><relation><string tertiary>
<relation>\is[]\alt[=]\alt[>]\alt[>=]\alt[=]\alt[>]
\endsyntax
Most of these operations were already explained in Chapter 8, so it's only
necessary to mention the more subtle points now. A ^*primary* of any
type can be tested to see whether it has a specific type, and whether it
has a known or unknown value based on the equations so far. In these tests,
a ^*future pen primary* is considered to be of type ^@pen@. The test
'cycle $p$' is true if and only if $p$ is a cyclic path. The 'odd' function
first rounds its argument to an integer, then tests to see if the integer
is odd. The 'not' function changes true to false and vice versa. The 'and'
function yields true only if both arguments are true; the 'or' function
yields true unless both arguments are false. Relations on pairs, transforms,
or strings are decided by the first unequal component from left to right.
\ (A is considered to be a 6-tuple as in Chapter 15.) \

**[Dangerous Bend]** exercise What do you think: Is @false@ $>$ @true@?

#### Answer
No; that would be shocking.

**[Dangerous Bend]** exercise Could '(odd $n$) and not (odd $-n$)' possibly be true?

#### Answer
Yes, if and only if $n-{1\over2}$ is an even integer.
\ (Because ambiguous values are rounded upwards.)

**[Dangerous Bend]** exercise Could '(cycle $p$) and not (known $p$)' possibly be true?

#### Answer
No.

**[Dangerous Bend]** exercise Define an 'even' macro such that 'even $n$' is true if
and only if round$(n)$ is an even integer. \ [*Hint:* There's a
slick answer.]

#### Answer
@def@ even $=$ not odd @enddef@.

**[Double Dangerous Bend]** Boolean expressions beginning with a ^*type* should not come
at the very beginning of a statement, because METAFONT\ will think that
a ^*declaration* is coming up instead of an *expression*. Thus, for
example, if $b$ is a boolean variable, the equation '$@path@\,p=b$'
should be rewritten either as '$b=@path@\,p$' or as '$(@path@\,p)=b$'.

**[Double Dangerous Bend]** A boolean expression like '$x=y$' that involves the
relation looks very much like an . METAFONT\ will consider '$=$'
to be a *relation* unless the expression to its left occurs at the
very beginning of a ^*statement* or the very beginning of a ^\<right-hand
side>. If you want to change an equation into a relation,
just insert parentheses, as in '$(x=y)=b$' or '$b=(x=y)$'.

**[Double Dangerous Bend]** After a ^*path join*, the token '' is not considered
to be the beginning of a *boolean primary*. \ (Cf.\ Chapter 14.)

**[Double Dangerous Bend]** The boolean expression '^@path@ $((0,0))$' is false, even
though '$((0,0))$' meets Chapter 14's syntax rules for
*path primary*, via *pair primary*.
A is not considered to be
of type @path@ unless the path interpretation is the only possibility.

**[Double Dangerous Bend]** exercise Evaluate 'length $((3,4))$' and 'length $((3,4)\{0,0\})$'
and 'length reverse $(3,4)$'.

#### Answer
The first is 5, because the pair is not considered to be a path.
The second and third are 0, because the pair is forced to become a path.

OK, that covers all there is to be said about conditions. What about
loops? It's easiest to explain loops by giving the syntax first:
\beginsyntax
<loop>\is<loop header>[:]<loop text>[endfor]
<loop header>\is[for]<symbolic token><is><for list>
\alt[for]<symbolic token><is><progression>
\alt[forsuffixes]<symbolic token><is><suffix list>
\alt[forever]
<is>\is[=]\alt[:=]
<for list>\is<expression>\alt<empty>
\alt<for list>[,]<expression>\alt<for list>[,]<empty>
<suffix list>\is<suffix>
\alt<suffix list>[,]<suffix>
<progression>\is<initial value>[step]<step size>[until]<limit value>
<initial value>\is<numeric expression>
<step size>\is<numeric expression>
<limit value>\is<numeric expression>
<exit clause>\is[exitif]<boolean expression>[;]
\endsyntax
As in macro definitions, '$=$' and '$:=$' are interchangeable here.

This syntax shows that loops can be of four kinds, which we might
indicate schematically as follows:

>
@for@ $x=\epsilon_1,\epsilon_2,\epsilon_3$: text($x$) @endfor@
plus 1pt
@for@ $x=\nu_1$ @step@ $\nu_2$ @until@ $\nu_3$: text($x$) @endfor@
plus 1pt
@forsuffixes@ $s=\sigma_1,\sigma_2,\sigma_3$: text($s$) @endfor@
plus 1pt
@forever@: text @endfor@

The first case expands to
'text($\epsilon_1$) text($\epsilon_2$) text($\epsilon_3$)'; the
$\epsilon$'s here are expressions of any type, not necessarily "known,"
and they are evaluated and put into before being substituted
for $x$. The $\epsilon$'s might also be empty, in which case
text($\epsilon$) is omitted.
The second case is more complicated, and it will be explained carefully
below; simple cases like '1 @step@ 2 @until@ 7' are equivalent to
short lists like '$1,3,5,7$'. The third case expands to
'text($\sigma_1$) text($\sigma_2$) text($\sigma_3$)'; the $\sigma$'s here
are arbitrary suffixes (possibly empty), in which subscripts will have been
evaluated and changed to numeric tokens before being substituted for $s$.
The final case expands into the sequence 'text text text $\ldots$',
ad infinitum; there's an escape from this (and from the other three kinds
of loop) if an *exit clause* appears in the text, as explained below.

Notice that if the loop text is a single statement that's supposed to
be repeated several times, you should put a '' just before the
@endfor@, not just after it; METAFONT's loops do not insert
automatically, because they are intended to be used in the midst of
expressions as well as with statements that are being iterated.

Plain METAFONT\ defines '^@upto@' as an abbreviation for '@step@ 1 @until@',
and '^@downto@' as an abbreviation for '@step@ $-1$ @until@'. Therefore
you can say, e.g., '@for@ $x=1$ @upto@ 9:' instead of
'@for@ $x=1,2,3,4,5,6,7,8,9$:'.

**[Dangerous Bend]** When you say '@for@ $x=\nu_1$ @step@ $\nu_2$ @until@ $\nu_3$',
METAFONT\ evaluates the three numeric expressions, which must have known values.
Then it reads the loop text. If $\nu_2>0$ and $\nu_1>\nu_3$, or if
$\nu_2<0$ and $\nu_1<\nu_3$, the loop is not performed at all. Otherwise
text($\nu_1$) is performed, $\nu_1$ is replaced by $\nu_1+\nu_2$, and
the same process is repeated with the new value of $\nu_1$.

**[Dangerous Bend]** exercise Read the rules in the previous paragraph carefully, then
explain for what values of $x$ the loop is performed if you say
(a) '@for@ $x=1$ @step@ 2 @until@ 0'. \
(b) '@for@ $x=1$ @step@ $-2$ @until@ 0'. \
(c) '@for@ $x=1$ @step@ 0 @until@ 0'. \
(d) '@for@ $x=0$ @step@ .1 @until@ 1'.

#### Answer
(a) The loop text is never executed. \
(b) It's executed only once, for $x=1$. \
(c) It's executed infinitely often, for $x=1,1,1,\ldots\,$. \
(d) Since ten times METAFONT's internal representation of
.1 is slightly larger than 1, the answer
is not what you probably expect! The loop text is executed for
$x=0$, 0.1, 0.20001, 0.30002, 0.40002, 0.50003, 0.60004, 0.70004, 0.80005,
and 0.90005 only. \ (If you want the values $(0,.1,.2,\ldots,1)$, say
'@for@ $"xx"=0$ @upto@ 10: $x:="xx"/10$; *text* @endfor@' instead.)

**[Dangerous Bend]** A *loop text* is rather like the *replacement text* of a macro.
It is any sequence of tokens that is balanced with respect to
und appearances of @for@/@forsuffixes@/@forever@ and @endfor@
delimiters. METAFONT\ reads the entire loop text quickly and stores it away
before trying to perform it or to expand macros within it. All occurrences
of the controlled *symbolic token* in the loop text are changed to
special internal parameter tokens that mean "insert an argument here,"
where the argument is of type @expr@ in the case of @for@, of
type @suffix@ in the case of @forsuffixes@. This rule implies, in
particular, that the symbolic token has no connection with similarly
named variables elsewhere in the program.

**[Dangerous Bend]** exercise What values are shown by the following program?

"'

n=0; for n=1: m=n; endfor show m,n; end.

"'

#### Answer
$m=1$, $n=0$.

**[Dangerous Bend]** The ^"flex" routine described in Chapter 14 provides an interesting
example of how loops can be used inside of macros inside of expressions:

>
@pair@ $"z\_"\,[\,]$, $"dz\_"$; \ @numeric@ "n\_";
&\% private variables
@def@ "flex"(@text@ $t$) $=$&\% $t$ is a list of pairs
^@hide@$\bigl(\,"n\_":=0$;
@for@ $z=t$: $"z\_"\,[incr\,"n\_"]:=z$; @endfor@
$"dz\_":="z\_"\,["n\_"]-"z\_"\,[1]\,\bigr)$
$"z\_"\,[1]$ @for@ $k=2$ @upto@ $"n\_"-1$:
$\ldots"z\_"\,[k]\{"dz\_"\}$ @endfor@\hidewidth
$\ldots"z\_"\,["n\_"]$ @enddef@;

The first loop stores the given pairs temporarily in an array, and it also
counts how many there are; this calculation is "hidden." Then
the actual flex-path is contributed to the program with the help of
a second loop. \ (Appendix B uses the convention that symbolic tokens
ending in '' should not appear in a user's program; this often
makes it unnecessary to '^@save@' tokens.)

**[Dangerous Bend]** When METAFONT\ encounters the construction '^@exitif@ \<boolean
expression>;', it evaluates the boolean expression. If the
expression is true, the (innermost) loop being iterated is terminated
abruptly. Otherwise, nothing special happens.

**[Dangerous Bend]** exercise Define an '^@exitunless@' macro such that
'@exitunless@ *boolean expression*;'\ will exit the current loop
if the boolean expression is false.

#### Answer
@def@ @exitunless@ @expr@ $b$ $=$ @exitif@ not $b$ @enddef@.
\ (The simpler alternative '@def@ @exitunless@ $=$ @exitif@ not
@enddef@' wouldn't work, since 'not' applies only to the following
*boolean primary*.)

**[Double Dangerous Bend]** exercise Write a METAFONT\ program that sets $p[k]$ to the $k$th
, for $1\le k\le30$. Thus, $p[1]$ should be 2,
$p[2]=3$, etc.

#### Answer
'numeric p[]; boolean n_is_prime; p[1]=2; k:=1;'break
'for n=3 step 2 until infinity:'break
' n_is_prime:=true;'break
' for j=2 upto k: if n mod p[j]=0: n_is_prime:=false; fi'break
' exitif n/p[j]<p[j]; endfor'break
' if n_is_prime: p[incr k]:=n; exitif k=30; fi'break
' endfor fi'break
^^@show@^^@str@
'show for k=1 upto 30: str p[k]&"="&decimal p[k], endfor "done" end.'

**[Double Dangerous Bend]** exercise When you run METAFONT\ on the file "expr.mf'' of
Chapter 8, you get into a '^@forever@' loop that can be stopped
if you type, e.g., "0' 'end''. But what can you type to get out
of the loop without ending the run? \ (The goal is to make
METAFONT\ type "*'', without incurring any error messages.)

#### Answer
"0; exitif true;''.

\endchapter

If? thou Protector of this damned Strumpet,
Talk'st thou to me of Ifs: thou art a Traytor,
Off with his Head.

> --- WILLIAM , *Richard the Third* (1593)

Use not vain repetitions.

> --- *6:7* (c. 70 A.D.)


# Chapter 20. More About Macros

Chapter 18 gave the basic facts about macro definitions, but it didn't
tell the whole story. It's time now for the Ultimate Truth to be revealed.

**[Dangerous Bend]** But this whole chapter consists of "dangerous bend" paragraphs,
since the subject matter will be appreciated best by people who have
worked with METAFONT\ for a little while.
We shall discuss the following topics:\enddanger

- Definitions that begin with '@vardef@'; these embed macros
into the variables of a program and extend the unary operators of
METAFONT\ expressions.

- Definitions that begin with '@primarydef@',
'@secondarydef@', or '@tertiarydef@'; these extend the
binary operators of METAFONT\ expressions.

- Other primitives of METAFONT\ that expand into sequences of tokens
in a macro-like way, including '@input@' and '@scantokens@'.

- Rules that explain when tokens are subject to expansion
and when they aren't.

**[Dangerous Bend]** First let's consider the *vardef heading* that was left
undefined in Chapter 18. The ordinary macros discussed in that chapter
begin with

>
@def@ *symbolic token**parameter heading*

and then comes '$=$', etc. You can also begin a definition by saying

>
^@vardef@ *declared variable**parameter heading*

instead; in this case the ^*declared variable* might consist of
several tokens, and you are essentially defining a variable whose
"value" is of type "macro." For example, suppose you decide to say

>
@pair@ $a.p$; \ @pen@ $a.q$; \ @path@ $a.r$; \
@vardef@ $a.s=\ldots$ @enddef@;

then $a.p$, $a.q$, and $a.r$ will be variables of types @pair@, @pen@,
and @path@, but $a.s$ will expand into a sequence of tokens. \
(The language demonstrated that it is advantageous
to include procedures as parts of variable data structures; METAFONT\ does an
analogous thing with macros.)

**[Dangerous Bend]** After a definition like '@def@ $t=\ldots$', the token $t$ becomes
a ""; i.e., you can't use it in a suffix. But after
'@vardef@ $t=\ldots$', the token $t$ remains a "," because
macro expansion will take place only when $t$ is the first token in
a variable name. Some of the definitions in Appendix B are vardefs
instead of defs for just that reason; for example,

>
@vardef@ dir @primary@ $d$ $=$ "right" rotated $d$ @enddef@

allows a user to have variable names like "p5dir''.

**[Dangerous Bend]** A variable is syntactically a primary expression, and METAFONT\ would
get unnecessarily confused if the replacement texts of vardef macros
were very different from primary expressions. Therefore, the
tokens '^@begingroup@'
and '^@endgroup@' are automatically inserted at the beginning and end
of every vardef replacement text. If you say '^@showvariable@ $a$'
just after making the declarations and definition above, the machine
will reply as follows:

"'

a.p=pair
a.q=unknown pen
a.r=unknown path
a.s=macro:->begingroup...endgroup

"'

**[Dangerous Bend]** The '' macro of Appendix B increases its argument by 1
and produces the increased value as its result. The inserted '@begingroup@'
and '@endgroup@' come in handy here:

>
@vardef@ incr @suffix@ \$ $=$ $\$:=\$+1$; \ \$ @enddef@.

Notice that the argument is a ^@suffix@, not an @expr@, because
every variable name is a special case of a ^*suffix*, and because
an ^@expr@ parameter should never appear to the left of '$:=$'.
Incidentally, according to the rules for
in Chapter 18, you're allowed to say either 'incr $v$' or 'incr$(v)$' when
applying incr to $v$.

**[Dangerous Bend]** There's another kind of vardef, in which the variable name being
defined can have any additional suffix when it is used; this suffix is
treated as an argument to the macro. In this case you write

>
@vardef@ *declared variable*'@#' *parameter heading*

and you can use '@#' in the replacement text (where it
behaves like any other @suffix@ parameter). For example, Appendix B says

>
@vardef@ $z$'@#' $=$ $(x$'@#'$,y$'@#') @enddef@;

this is the magic definition that makes '$z_3r$' equivalent to
'$(x_3r,y_3r)$', etc. In fact, we now know that "z3r'' actually
expands into eleven tokens:

"'

begingroup (x3r, y3r) endgroup

"'

**[Double Dangerous Bend]** exercise True or false: After "vardef' 'a@#' 'suffix' 'b' '='
$\ldots$ 'enddef'', the suffix argument 'b' will always be empty.

#### Answer
False; consider "a1(2)''.

**[Double Dangerous Bend]** Plain METAFONT\ includes a ^"solve" macro that uses
to find numerical solutions to , which are too
difficult to resolve in the ordinary way.
To use "solve", you first define a macro $f$ such that $f(x)$ is either
@true@ or @false@; then you say

>
"solve" $f("true\_x","false\_x")$

where "true\_x" and "false\_x" are values such that $f("true\_x")=@true@$
and $f("false\_x")=@false@$. The resulting value $x$ will be at the cutting
edge between truth and falsity, in the sense that $x$ will be within a
given ^"tolerance" of values for which $f$ yields both outcomes.

>
@vardef@ "solve"'@#'(@expr@ $"true\_x","false\_x"$) $=$
$"tx\_":="true\_x"$; \ $"fx\_":="false\_x"$;
^@forever@: $"x\_":=.5["tx\_","fx\_"]$; \
^@exitif@ abs$("tx\_"-"fx\_")\le"tolerance"$;
@if@ '@#'$("x\_")\colon\ "tx\_" \ @else@\colon\ "fx\_"\ @fi@$
:=\ "x\_"; @endfor@
"x\_" @enddef@;

**[Double Dangerous Bend]** For example, the "solve" routine makes it possible to solve the
following interesting problem posed by Richard : Given
points $z_1$, $z_2$, $z_3$, $z_4$ such that $x_1<x_2<x_3<x_4$ and
$y_1<y_2=y_3>y_4$, find the point $z$ between $z_2$ and $z_3$ such that
METAFONT\ will choose to travel "right" at $z$ in the path

>
$z_1\,\{z_2-z_1\}\to z\to\{z_4-z_3\}\,z_4$.

If we try $z=z_2$, METAFONT\ will choose a direction at $z$ that has a positive
(upward) $y$-component; but at $z=z_3$, METAFONT's chosen direction will have a
negative (downward) $y$-component. Somewhere in between is a ""
value of $z$ for which the curve will not rise above the line $y=y_2$.
What is this $z$?
\displayfig 20a (115\apspix)
Chapter 14 gives equations from which $z$ could be computed, in principle,
but those equations involve trigonometry in a complicated fashion.
It's nice to know that we can find $z$ rather easily in spite of those
complexities:

>
@vardef@ "upward"(@expr@ $x$) $=$
ypart direction 1 of $\bigl(z_1\{z_2-z_1\}
\to(x,y_2)\to\{z_4-z_3\}z_4\bigr)>0$ @enddef@;
$z=\bigl("solve"\,"upward"(x_2,x_3),y_2\bigr)$.

**[Double Dangerous Bend]** exercise It might happen in unusual cases that $"upward"(x)$
is @false@ for all $x_2\le x\le x_3$, hence "solve" is being invoked
under invalid assumptions. What result does it give then?

#### Answer
A value very close to $z_2$.

**[Double Dangerous Bend]** exercise Use "solve" to find $\root3\of10$, and compare
the answer to the obtained in the normal way.

#### Answer
'vardef lo_cube(expr x)=x*x*x<10 enddef;'break
'show solve lo_cube(0,10), 10**1/3; end.'\nobreak
With the default ^"tolerance" of 0.1,
this will show the respective values '2.14844' and '2.1544'.
A more general routine could also be written, with '10' as a parameter:

"'

vardef lo_cube[](expr x)=x*x*x<@ enddef;
show solve lo_cube10(0,10);

"'

if we ask for minimum tolerance ($"tolerance":="epsilon"$), the
result is '2.15445'; the true value is $\approx 2.15443469$.

**[Double Dangerous Bend]** The syntax for *declared variable* in Chapter 7 allows for
as well as tags in the name of the variable
being declared. Thus, you can say

>
@vardef@ $a[\,]b[\,]=\ldots$ @enddef@;

what does this mean? Well, it means that all variables like 'a1b2'
are macros with a common replacement text. Every vardef has two

implicit suffix parameters, "#@'' and "@'', which can be used in
the replacement text to discover what subscripts have actually been
used. Parameter "@'' is the final token of the variable name
("2'' in this example); parameter "#@'' is everything preceding
the final token (in this case "a1b''). These notations are supposed to
be memorable because "@'' is where you're "at," while "#@'' is
everything before and "@#'' is everything after.

**[Double Dangerous Bend]** exercise After "vardef' 'p[]dir=(#@dx,#@dy)' 'enddef'', what's
the expansion of "p5dir''?

#### Answer
'begingroup(p5dx,p5dy)endgroup'.

**[Double Dangerous Bend]** exercise Explain how it's possible to retrieve the first subscript
in the replacement text of 'vardef' 'a[]b[]' (thereby obtaining,
for example, "1'' instead of "a1b'').

#### Answer
Say "first#@'' after defining "vardef' 'first.a[]@#=@' 'enddef''.
\ (There are other solutions, e.g., using substrings of ^@str@ '#@',
but this one is perhaps the most instructive.)

**[Double Dangerous Bend]** exercise Say ' 'incr,z'' to METAFONT\ and explain
the machine's reply.

#### Answer
The machine answers thus:

"'

incr=macro:<suffix>->
begingroup(SUFFIX2):=(SUFFIX2)+1;(SUFFIX2)endgroup
z@#=macro:->begingroup(x(SUFFIX2),y(SUFFIX2))endgroup

"'

Parameters to a macro are numbered sequentially, starting with zero,
and classified as either $_n$')', $_n$')', or
$_n$')'. In a vardef, '(SUFFIX0)' and '(SUFFIX1)' are always
reserved for the implicit parameters '#@' and '@'; '(SUFFIX2)' will
be '@#', if it is used in the parameter heading, otherwise it will be the
first explicit parameter, if
it happens to be a suffix parameter.

**[Double Dangerous Bend]** A vardef wipes out all type declarations and macro definitions
for variables whose name begins with the newly defined macro variable name.
For example, "vardef' 'a'' causes variables like 'a.p'
and 'a1b2' to disappear silently; "vardef' 'a.s'' wipes out
'a.s.p', etc. Moreover, after "vardef' 'a'' is
in effect, you are not allowed to say "pair' 'a.p'' or "vardef' 'a[]'',
since such variables would be inaccessible.

**[Double Dangerous Bend]** The syntax for *definition* in Chapter 18 was incomplete,
because $\langle$vardef heading$\rangle$ and *leveldef heading* were
omitted. Here are the missing rules:
\beginsyntax
<vardef heading>\is[vardef]<declared variable><parameter heading>
\alt[vardef]<declared variable>[\#]<parameter heading>
<leveldef heading>\is<leveldef><parameter><symbolic token><parameter>
<leveldef>\is[primarydef]\alt[secondarydef]\alt[tertiarydef]
<parameter>\is<symbolic token>
\endsyntax
The new things here are @primarydef@, @secondarydef@, and @tertiarydef@,
which permit you to extend METAFONT's repertoire of binary operators. For example,
the 'dotprod' operator is defined as follows in Appendix B:

>
@primarydef@ $w$ dotprod $z$ $=$
$(xpart\,w\astxpart\,z\;+\;
ypart\,w\astypart\,z)$ @enddef@.

METAFONT's syntax for expressions has effectively gained a new rule
\beginsyntax
<numeric secondary>\is<pair secondary>[dotprod]<pair primary>
\endsyntax
in addition to the other forms of *numeric secondary*, because of this
primarydef.

**[Double Dangerous Bend]** The names '@primarydef@', '@secondarydef@',
and '@tertiarydef@' may
seem off by one, because they define operators at one level higher up:
A primarydef defines a binary operator that forms a secondary expression
from a secondary and a primary; such operators are at the same level
as '$\ast$' and 'rotated'.
A secondarydef defines a binary operator that forms a tertiary expression
from a tertiary and a secondary; such operators are at the same level
as '$+$' and 'or'.
A tertiarydef defines a binary operator that forms an expression
from an expression and a tertiary; such operators are at the same level
as '$<$' and '\&'.

**[Double Dangerous Bend]** Plain METAFONT's '' macro is defined by a
@secondarydef@ because it is analogous to '', which
occurs at the same level (namely the secondary $\rightarrow$ tertiary level):

>
@secondarydef@ $p$ intersectionpoint $q$ $=$
@begingroup@ ^@save@ $"x\_","y\_"$; \
$("x\_","y\_")=p$ intersectiontimes $q$;
@if@ $"x\_"<0$: ^@errmessage@('"The paths don't intersect"');
\ $(0,0)$
@else@: .5[point "x\_" of $p$,
point "y\_" of $q$] @fi@ @endgroup@ @enddef@.

Notice that ^@begingroup@ and ^@endgroup@ are necessary here; they aren't
inserted automatically as they would have been in a @vardef@.

**[Double Dangerous Bend]** exercise Define a '' macro operation that yields
the of two . \ (If $t_3=t_1$ transum $t_2$, then
$z$ transformed $t_3=z$ transformed $t_1+z$ transformed $t_2$,
for all pairs $z$.)

#### Answer
'secondarydef t transum tt ='break
' begingroup save T; transform T;'break
' for z=origin,up,right:'^^"origin"break
' z transformed t + z transformed tt = z transformed T; endfor'break
' T endgroup enddef.'

**[Double Dangerous Bend]** \looseness=-1
Now we've covered all the types of *definition*, and it's time to
take stock and think about the total picture. METAFONT's process
converts an input file into a long sequence of tokens, as explained in
Chapter 6, and its digestive processes work strictly on those tokens.
When a symbolic token is about to be digested, METAFONT\ looks up the token's
current meaning, and in certain cases METAFONT\ will expand that token into
a sequence of other tokens before continuing; this ""
applies to macros and to @if@ and @for@, as well as to certain other
special primitives that we shall consider momentarily. Expansion
continues until an unexpandable token is found; then the
can continue. Sometimes, however, the expansion is not carried out; for
example, after METAFONT\ has digested a @def@ token, it stops all expansion until
just after it reaches the corresponding @enddef@. A complete list of
all occasions when tokens are not expanded appears later in this chapter.

**[Double Dangerous Bend]** Let's consider all the tokens that cause expansion to occur,
whenever expansion hasn't been inhibited:\enddanger

\nobreak
- Macros. When a macro is expanded, METAFONT\ first reads and
evaluates the arguments (if any), as already explained.
\ (Expansion continues while @expr@ and @suffix@ arguments are
being evaluated, but it is suppressed within @text@ arguments.) \
Then METAFONT\ replaces the macro and its arguments by the replacement text.

break
- . When '^@if@' is expanded, METAFONT\
reads and evaluates the boolean expression, then skips ahead, if necessary,
until coming to either '^@fi@' or a condition that's true; then it will
continue to read the next token. When '^@elseif@' or '^@else@'
or '@fi@' is expanded, a conditional text has just ended, so METAFONT\
skips to the closing '@fi@' and the expansion is empty.

break
- . When '^@for@' or '^@forsuffixes@' or
'^@forever@' is expanded, METAFONT\ reads the specifications up to the colon,
then reads the loop text (without expansion) up to the @endfor@.
Finally it rereads the loop text repeatedly, with expansion. When
'^@exitif@' is expanded, METAFONT\ evaluates the following boolean
expression and throws away the semicolon; if the expression proves
to be true, the current loop is terminated.

break
- ^@scantokens@ *string primary*. When '@scantokens@'
is expanded, METAFONT\ evaluates the following primary expression, which
should be of type @string@. This string is converted to tokens by the
rules of Chapter 6, as if
it had been input from a file containing just one line of text.

break
- ^@input@ ^*filename*. When '@input@' is expanded,
the expansion is null, but METAFONT\ prepares to read from the specified
file before looking at any more tokens from its current source.
A *filename* is subject to special restrictions explained on the
next page.

break
- ^@endinput@. When '@endinput@' is expanded, the
expansion is null. But the next time METAFONT\ gets to the end of an
input line, it will stop reading from the file containing that line.

break
- ^@expandafter@. When '@expandafter@' is expanded,
METAFONT\ first reads one more token, without expanding it; let's
call this token $t$. Then METAFONT\ reads the token that comes after $t$
(and possibly more tokens, if that token takes an argument),
replacing it by its expansion. Finally, METAFONT\ puts $t$ back in front
of that expansion.

\nobreak
- '\'. When "\'' is expanded, the
expansion is null, i.e., empty.

**[Double Dangerous Bend]** The syntax for *filename* is not standard in METAFONT\!, because
different operating systems have different conventions. You should
ask your local system wizards for details on just how they have
decided to implement . The situation is complicated by
the fact that METAFONT's process of converting to tokens is irreversible;
for example, "x01'' and "x1.0'' both yield identical sequences
of tokens. Therefore METAFONT\ doesn't even try to convert a file name
to tokens; an operation must appear only in a text file, not
in a list of tokens like the replacement text of a macro! \ (You can get
around this restriction by saying

>
^@scantokens@ '"input foo"'

or, more generally,

>
^@scantokens@ ('"input "' \& "fname")

if "fname" is a string variable containing the *filename* you want to
input.) \ Although file names have nonstandard syntax, a sequence of six
or fewer ordinary letters and/or digits should be a
file name that works in essentially the same way on all installations of
METAFONT\!. Uppercase letters are considered to be distinct from their
lowercase counterparts, on many systems.

**[Double Dangerous Bend]** Here now is the promised list of all cases when expandable
tokens are not expanded. Some of the situations involve primitives
that haven't been discussed yet, but we'll get to them eventually.
Expansion is suppressed at the following times:\enddanger

\nobreak-
When tokens are being deleted during error recovery (see Chapter 5).

-
When tokens are being skipped because conditional text is being ignored.

-
When METAFONT\ is reading the definition of a macro.

-
When METAFONT\ is reading a loop text, or the symbolic token that
immediately follows @for@ or @forsuffixes@.

-
When METAFONT\ is reading the @text@ argument of a macro.

-
When METAFONT\ is reading the initial symbolic token of a *declared variable*
in a type declaration.

-
When METAFONT\ is reading the symbolic tokens to be defined by ^@delimiters@,
^@inner@, ^@let@, ^@newinternal@, or ^@outer@.

-
When METAFONT\ is reading the symbolic tokens to be shown by ^@showtoken@
or ^@showvariable@.

-
When METAFONT\ is reading the symbolic tokens to be saved by ^@save@.

-
When METAFONT\ is reading the token after ^@expandafter@, ^@everyjob@,
or the '$=$' or '$:=$' following @let@.

The expansion process is not suppressed while reading the suffix that
follows the initial token of a *declared variable*, not even in a
*vardef heading*.

\endchapter

The two lieutenants,
Fonteius Capito in Germany,

and Claudius Macro in Africa,

who opposed his advancement,
were put down.
or ,
*Sergius Sulpicius Galba* (c.125 A.D.)

By introducing macro instructions in the source language,
the designer can bring about the same ease of programming
as could be achieved by giving the computer
a more powerful operation list than it really has.
But naturally, one does not get the same advantages
in terms of economy of memory space and computer time
as would be obtained if the more powerful instructions
were really built into the machine.

> --- O. , *Computers \& Data Processing* (1970)


# Chapter 21. Random Numbers

It's fun to play games with
{\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn}
by writing programs that incorporate
an element of . You can generate unpredictable shapes, and
you can add patternless perturbations to break up the rigid symmetry that
is usually associated with mathematical constructions.
Musicians who use computers to
synthesize their compositions have found that has more "life" if
its rhythms are slightly irregular and offbeat; perfect 1--2--3--4 pulses
sound pretty dull by contrast. The same phenomenon might prove to
be true in typography.

METAFONT\ allows you to introduce controlled indeterminacy in two ways:
(1) ' $t$' gives a number $u$ that's randomly distributed
between 0 and $t$; \ (2) '' gives a $x$
that has the so-called normal distribution with mean zero and variance one.

**[Dangerous Bend]** More precisely, if $t>0$ and $u=$uniformdeviate $t$, we will
have $0\le u<t$, and for each fraction $0\le p\le1$ we will have
$0\le u<pt$ with approximate probability $p$. If $t<0$, the results are
similar but negated, with $0\ge u>t$. Finally if $t=0$, we always have
$u=0$; this is the only case where $u=t$ is possible.

**[Dangerous Bend]** A normaldeviate, $x$, will be positive about half the time and
negative about half the time. Its distribution is "" in
the sense that a particular value $x$ occurs with probability roughly
proportional to $e$; the graph of this function looks something
like a bell. The probability is about 68\% that $\vert x\vert<1$,
about 95\% that $\vert x\vert<2$, and about 99.7\% that $\vert x\vert<3$.
It's a pretty safe bet that $\vert x\vert<4$.

Instead of relying on mathematical formulas to explain this random
behavior, we can actually see the results graphically by letting METAFONT\
draw some "." Consider the following program, which
draws a $10\pt\times10\pt$ square and puts 100 little dots inside it:

>
@beginchar@$\,($incr $"code",10"pt"\0,10"pt"\0,0)$;
@pickup@ @pencircle@ scaled .3"pt"; \ @draw@ "unitsquare" scaled $w$;
@pickup@ @pencircle@ scaled 1"pt";
@for@ $k=1$ @upto@ 100:
@drawdot@(uniformdeviate $w,\,$uniformdeviate $w$);
\ @endfor@ @endchar@.

The resulting "characters," if we repeat the experiment ten times,
\n=-1 look like this:

>
\threenextn&\threenextn&\threenextn&\nextn.

And if we replace 'uniformdeviate $w$' by '$.5w+w/6\ast$normaldeviate',
we get

>
\threenextn&\threenextn&\threenextn&\nextn.

Finally, if we say '@drawdot@(uniformdeviate $w,\,.5w+w/6\ast
$normaldeviate)' the results are a mixture of the other two cases:

>
\threenextn&\threenextn&\threenextn&\nextn.

### Exercise
Consider the program fragment '@if@ uniformdeviate$\,1<
1/3$:\
"case\_a" @else@: "case\_b" @fi@'. True or false:
"case\_b" will occur about three times as often as "case\_a".

#### Answer
False; about twice as often (2/3 versus 1/3).

### Exercise
METAFONT's uniformdeviate operator usually doesn't give you an integer.
Explain how to generate random integers between 1 and $n$, in such a way
that each value will be about equally likely.

#### Answer
'1+floor uniformdeviate n'.

### Exercise
What does the formula '(uniformdeviate 1)[$z_1,z_2$]' represent?

#### Answer
A random point on the straight line segment from $z_1$ to $z_2$.
\ (The point $z_1$ itself will occur with probability about 1/65536;
but point $z_2$ will never occur.)

### Exercise
Guess what the following program will produce:

"'

beginchar(incr code,100pt#,10pt#,0);
for n:=0 upto 99:
fill unitsquare xscaled 1pt yscaled uniformdeviate h
shifted (n*pt,0); endfor endchar.

"'

#### Answer
A random "" texture, $100\pt$ wide $\times$ $10\pt$ tall:
{\rand} The density decreases uniformly as you go up in altitude.

**[Dangerous Bend]** exercise And what does this puzzle program draw?

"'

beginchar(incr code,24pt#,10pt#,0);
numeric count[];
pickup pencircle scaled 1pt;
for n:=1 upto 100:
x:=.5w+w/6*normaldeviate;
y:=floor(x/pt);
if unknown count[y]: count[y]:=-1; fi
drawdot(x,pt*incr count[y]); endfor endchar.

"'

#### Answer
A more-or-less bell-shaped : {\rand}

**[Dangerous Bend]** Let's try now to put more "life" in the METAFONT\ , by
asking Lady Luck to add small perturbations to each of the key points.
First we define "noise",

>
@vardef@ "noise" $=$ normaldeviate$\ast"craziness"$ @enddef@;

the ^"craziness" parameter will control the degree of haphazard variation.
\rightfig 21a ({240\apspix} x {216\apspix}) ^-20pt
Then we can write the following program for the logo's '{\manual n}':

>
@beginlogochar@('"N"'$,15)$;
$x_1="leftstemloc"+"noise"$;
$x_2="leftstemloc"+"noise"$;
$w-x_4="leftstemloc"+"noise"$;
$w-x_5="leftstemloc"+"noise"$;
$"bot"\,y_1="noise"-o$;
$"top"\,y_2=h+o+"noise"$;
$y_3=y_4+"ygap"+"noise"$;
$"bot"\,y_4="noise"-o$;
$"top"\,y_5=h+o+"noise"$;
$z_3="whatever"[z_4,z_5]$;
@draw@ $z_1\dashto z_2\dashto z_3$; \
@draw@ $z_4\dashto z_5$; \ @labels@$(1,2,3,4,5)$; \ @endchar@.

The illustration here was drawn with $"craziness"=0$, so there was no noise.

**[Dangerous Bend]** Three trials of the $9\pt$ '{\manual n}' with $"craziness"=.1"pt"$
gave the following results:
\displayfig 21b\&c\&d (195\apspix)
And here's what happens if you do similar things to all the
letters of METAFONT\!, with "craziness" decreasing from $.45"pt"$ to zero in
steps of $.05"pt"$:

> \global\n by 8

\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
\nextn\nextn\nextn\nextn\nextn\nextn\nextn\nextn
{\manual METAFONT}

**[Dangerous Bend]** Every time you run a program that refers to random numbers,
you'll get different results, because METAFONT\ uses the date and time of day
to change its generator. This unpredictable behavior
is normally what you want, but it can be troublesome if your
program draws a lovely shape that you'd like to see again.
Or perhaps one of your runs will uncover a program bug; you won't be able to
diagnose the problem, because it probably won't recur!
The solution is to say

>
^@randomseed@ $:=$ *numeric expression*

and to remember the value of that numeric expression. \ (The value
will automatically be recorded in the transcript file of your run.) \
You will get the same sequence of uniform and normal deviates on
any two runs that begin with the same @randomseed@, because METAFONT's
numbers are only "pseudo-random."

\endchapter

A musician whom I knew amused himself

by tuning his piano haphazardly, without any rhyme or reason.

Afterwards he played 's Sonate Path\'etique by heart.

It was an unbelievable delight to hear an old piece come back to life.

How often had I previously heard this sonata, always the same way,

never dreaming that it was capable of being developed further!

> --- AUGUST , *Chance in Artistic Creation* (1894)

[Education] must lead us from chance and arbitrariness
to rational clarity and intellectual order.

> --- L. , *Inaugural Address* (1938)


# Chapter 22. Strings

METAFONT\ is not a word processor, but a METAFONT\ programmer can process words and
other short strings of symbols in rudimentary ways. Strings can help
explain what a program is doing; for example, the 'io.mf' file of
Chapter 5 mentions '"The' 'letter' 'O"' as a title that should appear
on proofsheets, and it also says '"O"' in order to identify the
position of a character in the output font.

Chapter 6 points out that a *string token* is any sequence of
characters enclosed in double-quote ('"') marks, except that you're
not allowed to use the double-quote character itself in this way.
If you need that character, plain METAFONT\ provides it in a string of
length 1 called ^"ditto". Thus

"'

"A string expression can contain a '" & ditto & "' mark"

"'

even though a *string token* cannot.

A string expression can be used all by itself as a statement, just as
if it were an equation or declaration or command. Such a statement is called
a ^*title*, provided that it is immediately followed by a ";''.
If ^"tracingtitles"$>0$ when a title is encountered, METAFONT\
will type the title on the user's terminal. If ^"proofing"$>0$
when a title is encountered, METAFONT\ will copy the title into the output
file, so that it can be put onto proofsheets by postprocessors such
as the program described in Appendix H.

**[Dangerous Bend]** Appendix H explains how to specify the strings that are used as
for the key points on proofsheets.

**[Double Dangerous Bend]** Here's the full syntax for string expressions. All of the
activity except for ('\&') takes
place at the primary level:
\beginsyntax
<string primary>\is<string token>
\alt<string variable>
\alt[(]<string expression>[)]
\alt[begingroup]<statement list><string expression>[endgroup]
\alt[jobname]
\alt[readstring]
\alt[str]<suffix>
\alt[char]<numeric primary>
\alt[decimal]<numeric primary>
\alt[substring]<pair expression>[of]<string primary>
<string secondary>\is<string primary>
<string tertiary>\is<string secondary>
<string expression>\is<string tertiary>
\alt<string expression>[\&]<string tertiary>
\endsyntax
The new features here are 'jobname', 'readstring', 'str', 'char',
'decimal', and 'substring'; we shall consider each of them in turn.

**[Double Dangerous Bend]** The name of your job (@jobname@) is the name of the first
file you input, provided that the first line of instructions to METAFONT\
(the '' line or ) causes input of some file.
Otherwise the job name is , as in Experiment 1 of Chapter 5.

**[Double Dangerous Bend]** When you say '^@readstring@', METAFONT\ stops and waits for the user
to type a line at the terminal. The value of @readstring@ is the contents
of this line, with trailing spaces eliminated.
\ (You probably should use the @message@ command first, to give the
user a clue about what to type; for example, see the 'expr.mf' file
of Chapter 8, which gets its input expressions via @readstring@.
The ^@stop@ macro of Appendix B makes use of the fact that @readstring@
halts the computer; it doesn't actually look at the string.)

**[Double Dangerous Bend]** An arbitrary ^*suffix* is converted to a string by ^@str@,
using the method by which METAFONT\ displays suffix arguments in
diagnostic typeouts. Negative subscripts are enclosed in
square brackets; spaces or dots are inserted between tokens whose
characters belong to the same class (according to the table in
Chapter 6). For example, if $n=1$ then '@str@ $x[n]a$' is '"x1a"';
'@str@ $x\,n\,a$' is '"x.n.a"'.

**[Double Dangerous Bend]** The result of '^@char@ $n$' is a string of length 1,
representing the character whose code is $n$.
\ (Appendix C explains this code.) \ The value of $n$ is first
rounded to the nearest integer, then multiples of 256 are
added or subtracted if necessary until $0\le n<256$; this
defines @char@ $n$ in all cases.

**[Double Dangerous Bend]** The of a known numeric value $x$
is available in string form as '@decimal@ $x$'. If $x$ is negative,
the first character of this string will be "-''. If $x$ is not
an integer, a decimal point will be included, followed by as
many digits as are necessary to characterize the value. \ (These
conventions are the same as those illustrated in the example
outputs of Chapter 8.)

**[Double Dangerous Bend]** The rules for are like the rules for
in Chapter 14. METAFONT\ thinks of a string as if its characters were
written in the squares of a piece of , between
coordinates $x=0$ and $x=n$, where $n$ is the length of the string.
In simple cases, substring$\,(a,b)$
then refers to the characters between $x=a$ and $x=b$. The
rules for the general case are slightly more involved: If $b<a$,
the result will be the of substring$\,(b,a)$.
Otherwise $a$ and $b$ are replaced respectively by
$\max\bigl(0,\min(n,\round a)\bigr)$ and
$\max\bigl(0,\min(n,\round b)\bigr)$; this leads to the simple
case $0\le a\le b\le n$ described above, when the resulting
string has length $b-a$.

**[Double Dangerous Bend]** Strings can be converted into numbers, although Chapter 8
didn't mention this fact in its syntax for *numeric primary*. The
primitive operations are

>
'ASCII'*string primary*\alt
'oct'*string primary*\alt
'hex'*string primary*

where '' returns the ASCII code of the first character of the
string, '' computes an integer from a string representing
(radix 8), and '' computes an integer from
a string representing (radix 16). For example,

>
ASCII '"100"' $=$ 49; oct '"100"' $=$ 64; hex '"100"' $=$ 256.

Several exceptional conditions need to be mentioned:
(1) ASCII '""' $=-1$; otherwise ASCII yields an integer between 0 and 255.
\ (2) The characters in the string argument to 'oct' must all be
digits in the range '0'--'7'.
\ (3) The characters in the string argument to 'hex' must all be
digits in the range '0'--'9', 'A'--'F', or 'a'--'f'.
\ (4) The number that results from 'oct' or 'hex' must be less than 4096.
Thus, 'oct '"7777"'' and 'hex '"FFF"'' are the maximum legal values.

**[Double Dangerous Bend]** exercise Under what circumstances is (a) ASCII @char@ $n=n$?
\ (b) @char@ ASCII $s=s$?

#### Answer
(a) If and only if $n$ is an integer between 0 and 255.
(b) If and only if $s$ is a string of length 1.

**[Double Dangerous Bend]** exercise Why are there primitive operations to convert from
strings to numbers assuming octal notation and hexadecimal notation,
but not assuming decimal notation?

#### Answer
Whoever says that there's no such primitive operation has
forgotten about @scantokens@.

**[Double Dangerous Bend]** exercise Write an "octal" macro that converts a nonnegative
integer to an octal string.

#### Answer
'vardef octal primary n ='break
' save m,s; m:=abs round n; string s; s=decimal(m mod 8);'break
' forever: m:=m div 8; exitif m=0;'break
' s:=decimal(m mod 8) & s; endfor'break
' s enddef;'\nobreak
"str[m mod 8]'' could also be used instead of "decimal(m mod 8)''.

**[Double Dangerous Bend]** A ^*message command* allows you to communicate directly
or indirectly with the user. It has the general syntax
\beginsyntax
<message command>\is<message op><string expression>
<message op>\is[message]\alt[errmessage]\alt[errhelp]
\endsyntax
If you say '@message@ $s$', the characters of $s$ will be typed on the
terminal, at the beginning of a new line; '@errmessage@ $s$' is
similar, but the string will be preceded by "! '' and followed
by ".'', followed by lines of context as in METAFONT's normal error messages.
If the user asks for after an @errmessage@ error,
the most recent @errhelp@ string will be typed (unless it was empty).

**[Double Dangerous Bend]** METAFONT\ doesn't allow you to have an array of different
macros $m[i]$; but you can have an array of strings that have
macro-like behavior, via ^@scantokens@. The ^@mode\_def@ construction
of Appendix B exploits this idea.

\endchapter

Many other useful Practises
mecanicks perform by this Theo.
as the finding the length of strings.

> --- WILLIAM , *Geometry Epitomized* (1695)

Forgive me, if my trembling Pen displays
What never yet was sung in mortal Lays.
But how shall I attempt such arduous String?

> --- JAMES , *The Castle of Indolence* (1748)


# Chapter 23. Online Displays

How do you get pictures to appear on your screen? Plain METAFONT\ provides
the '^@showit@' command, which displays the ^"currentpicture".
Furthermore you can ask for '^@screenchars@'; this automatically
does a @showit@ at the time of each ^@endchar@. And you can see all
the action by asking for '^@screenstrokes@'; this automatically
does a @showit@ after every @draw@ or @fill@.

**[Double Dangerous Bend]** The above-described features of plain METAFONT\ are implemented
from low-level primitive commands, by macros that appear in Appendix B.
At the lowest level, METAFONT\ obeys commands such as '@display@
"currentpicture" @inwindow@ 1'; there's also an '@openwindow@'
command that defines a correspondence between METAFONT\ coordinates and
screen coordinates. The syntax is
\beginsyntax
<display command>\is[display]<picture variable>[inwindow]<window>
<window>\is<numeric expression>
<openwindow command>\is[openwindow]<window><window spec>
<window spec>\is<screen place>[at]<pair expression>
<screen place>\is[from]<screen coordinates>[to]<screen coordinates>
<screen coordinates>\is<pair expression>
\endsyntax
A *window* is an integer between 0 and 15, inclusive; it represents
one of sixteen "windows" or "portholes" that METAFONT\ provides
between its pictures and the outside world. The *window* mentioned
in a @display@ command must previously have been "opened" by
an @openwindow@ command.

**[Double Dangerous Bend]** METAFONT's windows should not be confused with the so-called
windows provided by many modern operating systems. If you have
such a system, you'll probably find that all of METAFONT's pictorial
output appears in one operating-system window, and all of its
terminal I/O appears in another, and you might be running other
jobs (like the system editor) in another. METAFONT's windows are not so
fancy as this; they are just internal subwindows of one big
picture window.

**[Double Dangerous Bend]** The command '@openwindow@ $k$ @from@ $(r_0,c_0)$ @to@ $(r_1,c_1)$
@at@ $(x,y)$' associates a rectangular area of the user's screen
(or of the user's big picture window) with pixels in METAFONT's coordinate
system. All of the numbers in this command (namely $k$, $r_0$, $c_0$,
$r_1$, $c_1$, $x$, and $y$) are rounded to the nearest integer if they
aren't integers already. Furthermore $r_0$ is replaced by
$\max\bigl(0,\min("maxr",r_0)\bigr)$ and $r_1$ is replaced by
$\max\bigl(r_0,\min("maxr",r_1)\bigr)$, where "maxr" is the maximum
number of rows on the screen; similar adjustments are made to $c_0$
and $c_1$. The two $(r,c)$ values are row and column
numbers on the screen; the topmost row is conventionally taken to be
row zero, and the leftmost column is taken to be column zero.
\ (These conventions for screen coordinates are quite different from
the normal coordinate system used everywhere else
in METAFONT\!, but somehow they seem appropriate when applied to screens.) \
Point $(x,y)$ of METAFONT's raster will be equated to the upper left
corner of the rectangle, i.e., to the upper left corner of the pixel
in screen column $c_0$ of screen row $r_0$. The window itself
occupies $r_1-r_0$ rows and $c_1-c_0$ columns. It follows that
the pixel in column $c_1$ of row $r_1$ is not in the window itself,
but it is the screen pixel diagonally just below and to the right of the
lower right corner of the window.

**[Double Dangerous Bend]** exercise What are the METAFONT\ coordinates of the boundary of
such a window?

#### Answer
Point $(x,y)$ is the upper left corner, ${(x+c_1-c_0,y)}$ is the
upper right corner, ${(x,y-r_1+r_0)}$ is the lower left corner, and
${(x+c_1-c_0,y-r_1+r_0)}$ is the lower right corner. \ (Pixels
outside this rectangle will not be displayed.)

**[Dangerous Bend]** If you run METAFONT\ on a system that doesn't support general
bitmap displays, the @display@ and @openwindow@ commands will do
nothing. You'll have to look at hardcopy output, offline.
\ (But your METAFONT\ might run a bit faster.)

**[Double Dangerous Bend]** The syntax for @display@ insists that you display a
*picture variable*, not a *picture expression*; thus, you
can't '@display@ ^@nullpicture@'. Plain METAFONT\ defines a special
variable ^"blankpicture" that's entirely blank, just so that
you can easily display nothing whenever you like.

**[Double Dangerous Bend]** A window may be opened any number of times, hence moved
to different locations on the screen. Opening a window blanks the
corresponding screen rectangle as if you had displayed "blankpicture".

**[Double Dangerous Bend]** The effect of overlapping windows is undefined, because METAFONT\
does not always repaint pixels that have remained unchanged between
displays.

**[Double Dangerous Bend]** Changes to a picture do not change the displays that were
generated from it, until you give another display command explicitly.
Thus, the images emblazoned on your screen might not exist any longer
in METAFONT's picture memory.

**[Double Dangerous Bend]** Plain METAFONT\ has an '@openit@' macro that opens
^"currentwindow"; this variable "currentwindow" is always zero
unless you change it yourself. The @showit@ macro displays
"currentpicture" in "currentwindow"; and it's also designed
to call @openit@---but only the very first time @showit@ is invoked.
This means that the screen normally won't be touched until the moment you
first try to display something.

**[Double Dangerous Bend]** Appendix E explains how to manage a more elaborate scheme
in which six windows can be used to show how vary
under six different font-parameter settings. The author
used such a six-window system when developing the Computer Modern
typefaces; here is a typical example of what appeared on his
terminal when the letter 'a' was being refined:
\displayfig 23 (68mm)

**[Double Dangerous Bend]** exercise The @openit@ macro in Appendix B specifies $(-50,300)$
as the upper left corner point of the window used for showing
all the pictures. This might clip off the bottom of a large character,
if your screen is limited to, say, 360 rows. How could you change
@openit@ so that the character images will be raised 20 rows higher
than they would be in the standard setting?

#### Answer
Redefine @openit@ so that it puts the top left at $(-50,280)$.

**[Double Dangerous Bend]** exercise Design a '^@new\_window@' routine that allocates
windows 1, 2, \dots, 15. If the user says "new_window $(u,v)'',
where '$' is any suffix and 'u,v' are pairs of coordinates for
two opposite corners of a rectangle, your macro should map that
rectangle to the next available screen rectangle and open it as
window number 'window$'. The allocation should be left to right,
top to bottom; assume that the screen is an infinite rectangle,
^"screen\_cols" wide.

#### Answer
(This routine is due to John .)

"'

newinternal n_windows;
newinternal screen_bot;
pair screen_corner;
def wipescreen =
for i:=1 upto n_windows: display blankpicture inwindow i; endfor
n_windows := screen_bot := 0; screen_corner := origin enddef;
wipescreen;
vardef new_window@#(expr u,v) = save r,c,up_lft; pair up_lft;
if n_windows=15: errmessage "No more windows left"
else: window@# := incr n_windows;
up_lft = (min(xpart u,xpart v), max(ypart u, ypart v));
(r,c) = (u+v-2up_lft) rotated 90;
if ypart screen_corner + c > screen_cols:
screen_corner:=(screen_bot,0); fi
openwindow window@# from screen_corner
to screen_corner+(r,c) at up_lft;
screen_bot := max(screen_bot,xpart screen_corner + r);
screen_corner := screen_corner + (0,c) fi; enddef;

"'

\endchapter

Editing will be done on-line with a display scope and keyboard.

> --- RICHARD L. , in *American Documentation* (1968)

In future I might be obliged to turn for material to the tube.

> --- IGOR , in *Harper's* (1970)


# Chapter 24. Discreteness and Discretion

Pixel patterns are indistinguishable from continuous curves, when the
pixels are small enough. After all, the human eye is composed of
discrete receptors, and visible light has a finite wavelength.
Our hypothetical ^"luxo" printer of Chapter 11, with its resolution
of 2000 pixels per inch, would surely be able to produce printed
pages of high quality, if it existed; the physical properties of ink
would smooth out all the tiny bumps, obliterating all the evidence that
the letterforms had been digitized. However, it will always be less
expensive to work with devices of lower resolution, and we want the output
of METAFONT\ to look as good as possible on the machines that we can afford to
buy. The purpose of this chapter is to discuss the principles of
"discreet ," i.e., to consider the tasteful application of
mathematical techniques by which METAFONT\ can be made to produce satisfactory
shapes even when the resolution is rather coarse.

The technical material in this chapter is entirely marked with danger
signs, since careful rounding tends to make METAFONT\ programs more complex; a
novice user will not wish to worry about such details. On the other hand,
an expert METAFONT er will take pains to round things properly even when
preparing high-resolution fonts, since the subtle refinements we are about
to discuss will often lead to significantly better letterforms.

We should realize before we begin that it would be a mistake to
set our hopes too high. Mechanically generated letters that are untouched
by human hands and unseen by human eyes can never be expected to compete
with alphabets that are carefully crafted to look best on a particular
device. There's no substitute for actually looking at the letters
and changing their pixels until the result looks right. Therefore our
goal should not be to make obsolete; it should rather be
to make hand-tuning tolerable. Let us try to create meta-designs so
that we would never want to change more than a few pixels per character,
say half a dozen, regardless of the resolution. At low resolutions, six
pixels will of course be a significant percentage of the whole, and at higher
resolutions six well-considered pixel changes can still lead to worthwhile
improvements. The point is that if our design comes close enough, a
person with a good bitmap-editing program will be able to optimize an
entire font in less than an hour. This is an attainable goal, if rounding
is done judiciously.

**[Dangerous Bend]** METAFONT\ tries to adjust curves automatically, so that they are
well adapted to the , if the internal quantities ^"autorounding"
and/or ^"smoothing" have positive values. \ (Plain METAFONT\ sets
$"autorounding":=2$ and $"smoothing":=1$, so you generally get these
features unless you turn them off yourself.) \ But all the examples in
this chapter will be generated with $"autorounding":="smoothing":=0$
unless otherwise mentioned, because this will keep METAFONT's automatic
mechanisms from interfering with our experiments. We shall discuss the
pros and cons of automatic rounding after we have explored the general
problem in more detail.

**[Dangerous Bend]** The first thing we need to understand about rounding is METAFONT's
procedure for a path. A path of length $n$ can be regarded
as a trajectory $z(t)$ that is traced out as $t$ varies from 0 to $n$. In
these terms, the corresponding digitized path is most easily described by
the formula 'round $z(t)$' for $0\le t\le n$; each $z(t)$ is rounded to
the nearest point with integer coordinates. For example, if a path goes
through point $(3.1,5.7)$, its digitization will go through point $(3,6)$.
The digitized trajectory makes discrete jumps at certain values of $t$,
when round $z(t)$ hops from one point to another; the two points will be
one pixel apart, and we can imagine that the digitized path traverses the
horizontal or vertical edge between them when it jumps.

**[Dangerous Bend]** When an ordinary region is being filled, this rule for
digitizing paths boils down to a simple criterion that's easy to
visualize: *A pixel belongs to the digitized region if and only if
its center point lies inside the original undigitized path.* For example,
two versions of Chapter 5's Ionian '{\manual\IOO}' are shown here
at a resolution of 200 pixels per inch, using the characteristics
of ^"lowres" mode in Appendix B:
\displayfig 24a\&b (190\apspix)
The heavy broken lines are digitized paths, and the pixels inside these
ragged boundaries are those whose centers lie in the shaded regions.

**[Dangerous Bend]** The '{\manual\IOO}' on the left has digitized well; but the
one on the right has problems, because it was based on curves that
were generated without taking the raster into account. The difference
between these two letters is entirely due to line 8 of the program
in Chapter 5, which says

>
"curve\_sidebar" $=$ round $1/18"em"$;

this equation determines the position of the leftmost and rightmost
edges of the '{\manual\IOO}' before digitization, and it leads to
the nice digitized form in the left-hand example. Without the word
'', we get the inferior right-hand example, which was
obtained by exactly the same METAFONT\ program except that "curve\_sidebar"
was set to $1/18"em"$ exactly. One little token---which changed an exact
calculation to an approximate, rounded calculation---made all the difference!

**[Dangerous Bend]** Curves that are placed in arbitrary positions on
a raster can lead to digital disasters, even though the curves themselves
aren't bad. For example, suppose we take the right-hand example above
and shift it just 0.05 and 0.10 pixels to the right:
\displayfig 24c\&d (190\apspix)
The first shift of 0.05 pixels causes a tiny to appear
at the right edge; after another small shift the pimple has grown into a
mole, and the left edge has become too . \looseness=-1

**[Dangerous Bend]** A designer who is asked to make a digital 'O' that is 22 pixels
wide will certainly have pixels in mind when making the design. Therefore
it's not surprising that our program to generate a digital 'O' should
pay attention to actual pixel positions by rounding "curve\_sidebar" as
in this example. We have distorted the infinite-resolution curve
slightly so that it will digitize well, before digitizing it.

**[Dangerous Bend]** A path $z(t)$ will digitize well if the digitization process doesn't
change it too much; thus, we want $z(t)$ to be essentially the same as
round$\,z(t)$, at all the important places. But what places are "important"?
Experience shows that the most critical points are those where the path
travels horizontally or vertically, i.e., where it runs parallel to
the raster lines. It's best to arrange things so that a curve becomes
parallel to the raster lines just when it touches or nearly touches those
lines; then it will appear to have the right curvature after digitization.
The worst case occurs when a curve becomes parallel to the raster just
when it's halfway between raster lines; then it gets a pimple or a flat spot.

**[Double Dangerous Bend]** Diagonal slopes, where a curve has a $\pm45^\circ$ tangent angle,
are also potential sources of unwanted pimples and flats. Similarly, at
higher resolutions it is sometimes possible to detect small glitches
when a curve travels with slopes of $\pm1/2$ or $\pm2/1$. Rational
slopes $m/n$ where $m$ and $n$ are small integers turn out to be
somewhat dangerous. But diagonals are of secondary importance; horizontal
and vertical slopes lead to more severe problems.

**[Dangerous Bend]** These considerations suggest a simple general principle for adapting
the outlines of shapes to be digitized: *If you know that the outline
will have a vertical tangent at some point, round the $x$ coordinate to an
integer and leave the $y$ coordinate unchanged. If you know that the
outline will have a horizontal tangent at some point, round the
$y$ coordinate to an integer and leave the $x$ coordinate unchanged.*

**[Double Dangerous Bend]** Incidentally, the horizontal tangent points in our '{\manual\IOO}'
examples were taken care of by the fact that '^@define\_corrected\_pixels@'
makes the parameter $o$ nearly an integer, together with
the fact that ^@beginchar@ makes $h$ an integer. If the $y$ coordinates
had not been rounded at the horizontal tangent points,
our bad examples would have looked even worse.

**[Dangerous Bend]** Before we go further into the study of rounding, we had better
face up to a technicality that's sometimes important: We said that the
pixels of a digitized region are those whose centers lie inside the
undigitized region; but this rule is vague about what happens when the
centers happen to fall precisely on the undigitized boundary. Similarly,
when we said that round$\,z(t)$ jumps from one point to an adjacent point,
we ignored the fact that a curve such as $z(t)=(t,t)$ actually
jumps from $(0,0)$ to $(1,1)$ when it is rounded as $t$ passes 1/2;
those points are not adjacent.
METAFONT\ skirts both of these problems in an interesting way:
It shifts all of its paths to the
right by an infinitesimal amount $\delta$, and it also shifts them
upward by an even smaller
infinitesimal amount $\delta\epsilon$, so that no path actually
touches a pixel center. Here $\delta$ and $\epsilon$ are positive numbers
that are chosen to be so small that their actual values don't matter.
For example, the path $z(t)=(t,t)$ becomes $(t+\delta,t+\delta\epsilon)$,
which jumps from $(0,0)$ to $(1,0)$ to $(1,1)$ because it momentarily
rounds to $(1,0)$ when $t=1/2-2\delta\epsilon$.

**[Dangerous Bend]** Points of the form $(m+1/2,n+1/2)$, where $m$ and $n$ are integers,
lie in the centers of their pixels. They are called "ambiguous" points
because we can't round them to the nearest integer neighbor without
deciding which of four adjacent points is to be considered the nearest.
If we imagine taking a curved outline and shifting it slowly to the
right, the digitized image makes abrupt transitions when the outline
passes over an . When a path comes near an ambiguous
point, the path is farthest away from its digitization. Thus the
ambiguous points are points of instability, and digitizing works best
when paths don't get too close to them.

**[Dangerous Bend]** Let's consider now what happens when we ^@draw@ with a pen,
instead of filling an outline. It may seem that the simplest possible @draw@
command would be something like this:

>
@pickup@ @pencircle@; \ @draw@ $(0,0)\to(10,0)$;

what could be easier? But a closer look shows that this is actually
about the worst case that could be imagined! A circular pen of
diameter 1 that goes from $(0,0)$ to $(10,0)$ has upper and lower
boundaries that go from $(0,\pm1/2)$ to $(10,\pm1/2)$,
and both of these boundaries run smack through lots of
ambiguous points. METAFONT\ has to decide whether to fill the row of pixels
with $0\le y\le1$ or the lower row with $-1\le y\le0$, neither of which is
centered on the given line. According to the rule stated earlier, METAFONT\
shifts the path very slightly to the right and very, very slightly up;
thus the pixels actually filled are bounded by
$(0,0)\dashto(10,0)\dashto(10,1)\dashto(0,1)\dashto\cycle$.

**[Dangerous Bend]** exercise Continuing this example, what pixels would have been
filled if the path had been '$(0,0)\to(10,-"epsilon")$'?

#### Answer
The entire path now has negative $y$ coordinates except at
point $(0,0)$, so the outline of the filled region is
$(0,-1)\dashto(10,-1)\dashto(10,0)\dashto(0,0)\dashto(0,1)
\dashto\cycle$. \ $\bigl($Notice that the
digitized outline actually goes up to $(0,1)$ before coming straight down
again. This fills no pixels, but METAFONT\ correctly puts "cancelling" edges
from $(0,0)$ to $(0,1)$ and back to $(0,0)$ into its edge structure, because the
point $(0,.5)$ is on the boundary and rounds to $(0,1).\bigr)$

**[Dangerous Bend]** In general when we @draw@ with a fixed pen, good digitizations
depend on where the edges of the pen happen to fall, not on the
path followed by the pen's center. Thus, for example, if the path we're
drawing has a vertical tangent at point $z_1$, we don't necessarily
want $x_1$ to be an integer; we want "lft"$\,x_1$ and "rt"$\,x_1$
to be integers. If there's a horizontal tangent at $z_2$, we want
"top"$\,y_2$ and "bot"$\,y_2$ to be integers. The pens created by
^@pencircle@ always have the property that $("lft"\,x)-("rt"\,x)$
and $("top"\,y)-("bot"\,y)$ are integers; hence both edges will
be in good or bad positions simultaneously.

**[Dangerous Bend]** Suppose that we want $x_1$ to be approximately equal to $\alpha$,
and we also want it to be at a good place for vertical tangents with respect
to the pen that has currently been picked up. One way to define $x_1$ is to say

>
$"lft"\,x_1=\round("lft"\,\alpha)$;

this does the right thing, because it makes "lft"$\,x_1$ an integer and
it also makes $x_1\approx\alpha$. Similarly, to make $y_2\approx\beta$
good for horizontal tangents, we can say

>
$"top"\,y_2=\round("top"\,\beta)$.

Such operations occur frequently in practice, so plain METAFONT\ provides
^^"good.x" ^^"good.y" convenient abbreviations: We can say simply

>
$x_1="good.x"\,\alpha$; \ $y_2="good.y"\,\beta$

instead of using indirect equations for $"lft"\,x_1$ and $"top"\,y_2$.

**[Dangerous Bend]** Let's look one last time at the letters of the METAFONT\ logo, in
order to make them round properly. Chapter 11 describes a file
that draws the seven characters, but we can improve the results by
making pixel-oriented refinements. In the first place, we can replace
the command

>
@define\_pixels@($s,u,"xgap","ygap","leftstemloc","barheight"$)

by something better: Looking at the uses of these ad hoc dimensions,
we see that ^"xgap" and ^"ygap" ought to be integers; ^"leftstemloc"
should be a "good.x" value for "logo\_pen"; and ^"barheight" should
be a "good.y" value. Therefore we say

>
^@define\_pixels@$(s,u)$;
^@define\_whole\_pixels@$("xgap","ygap")$;
^@define\_good\_x\_pixels@$("leftstemloc")$;
^@define\_good\_y\_pixels@$("barheight")$;

these commands, provided by plain METAFONT\!, will do the right thing.
\ (The "logo\_pen" should be picked up before the last two commands are
given.) \ These few changes, and a change to the '{\manual m}', suffice to
fix all the letters except '{\manual j}'.

**[Dangerous Bend]** exercise The program for METAFONT's '{\manual m}'
appears in Chapter 18. What changes would you suggest to make
it digitize well?

#### Answer
The horizontal tangents are already taken care of by the equations
$"top"\,y_1=h+o$ and $"bot"\,y_4=-o$, so nothing needs to be done there.
We should, however, say

>
$x_2=w-x_3="good.x"(1.5u+s)$

so that vertical tangents will occur in good places. Since $w$ is an
integer, and since the "logo\_pen" has left-right symmetry,
$w-x_3$ will be good if and only if $x_3$ is.

**[Dangerous Bend]** The '{\manual j}' presents a new problem,
because we want it to be symmetric between left and right. If the pen
breadth is odd, we want the character width $w$ to be odd, so that there
will be as many pixels to the left of the stem as there are to the right.
If the pen breadth is even, we want $w$ to be even. Therefore we have a
50-50 chance of being unhappy with the value of $w$ that is computed by
^@beginchar@.

**[Dangerous Bend]** exercise Prove that the value of $w$ is satisfactory for
'{\manual j}' with respect to the "logo\_pen" if and
only if $.5w$ is a good $x$ value for vertical strokes.

#### Answer
Let $b$ be the pen breadth. Then $.5w$ is a good $x$ value if and only
if $"lft"\,.5w$ is an integer; but $"lft"\,.5w=.5w-.5b$, and this is an
integer if and only if $w-b$ is even.

**[Dangerous Bend]** If $w$ is not a good value, we want to replace it by either
$w+1$ or $w-1$, whichever is closer to the device-independent width
from which $w$ was rounded. For example, if $w$ was rounded to 22 from
the ideal width 21.7, we want to change it to 21 rather than 23.
Plain METAFONT's ^@change\_width@ routine does this. Hence we have the
following program for '{\manual j}', in place of the
\rightfig 4b ({208\apspix} x {216\apspix}) ^-18pt
simpler version found in exercise 11.\metaT:

>
@beginlogochar@('"T"'$,13)$;
@if@ $.5w<>"good.x"\,.5w$: @change\_width@; @fi@
$"lft"\,x_1=-"eps"$;
$x_2=w-x_1$;
$x_3=x_4=.5w$;
$y_1=y_2=y_3$; \ $"top"\,y_1=h$; \ $"bot"\,y_4=-o$;
@draw@ $z_1\dashto z_2$; \ @draw@ $z_3\dashto z_4$;
@labels@$(1,2,3,4)$; \ @endchar@.

\decreasehsize 44mm
Chapter 4 said that '{\manual j}' was the simplest of the
seven logo letters, but it has turned out to be the trickiest.

\restorehsize

**[Double Dangerous Bend]** This program has one unexplained feature. Why was $"lft"\,x_1$
set to $-"eps"$ instead of zero? The answer requires an understanding
of the pen polygons discussed in Chapter 16. The edges of those polygons
are highly likely to pass through ambiguous points when the center of
the pen has integer or half-integer coordinates. METAFONT\ shifts paths slightly
to the right and up, in order to resolve ambiguities; therefore if
ambiguous points occur at the left and right edges of the
'{\manual j}', some pixels will be lost at the left but
gained at the right. The constant ^"eps" is 0.00049, which is small but
positive enough that METAFONT\ will surely notice it. Subtracting "eps"
from $x_1$ and adding "eps" to $x_2$ avoids ambiguous edge points and
keeps the result symmetric.

**[Double Dangerous Bend]** Since the '$o$' is always "eps" more than an
integer, it is unnecessary to do anything similar at point $z_4$;
the equation '$"bot"\,y_4=-o$' is sufficient.

**[Double Dangerous Bend]** Point $z_3$ in the middle of the '{\manual h}' is in
a satisfactory position because $"bot"\,y_3="ygap"-o$.
If $"bot"\,y_3$ were exactly an integer, the '{\manual h}' would often turn
out to be unsymmetric, because of ambiguous points on the boundary
at $z_3$.

**[Double Dangerous Bend]** exercise True or false: If "currentpen" is @pencircle@ xscaled "px"
yscaled "py", the command '@draw@ $(-"epsilon",0)\to(+"epsilon",0)$'
will produce an image that has both left-right and top-bottom symmetry.
\ (Assume that $"autorounding"="smoothing"=0$.)

#### Answer
There are no ambiguous points on the outlines of this stroke,
except perhaps on the top and bottom edges; the latter can occur only if
$\round"py"$ is odd. Hence there is always left-right symmetry, but
top-bottom symmetry might fail because of a missing row at the bottom
(e.g., when $"px"="py"=3$). In a case like the '{\manual j}'
we do have both symmetries, because $y_1$ and $x_4$ are in good positions.

**[Double Dangerous Bend]** exercise The polygon for '^@pencircle@ scaled 3' is an octagon
whose vertices are at the points $(\pm0.5,\pm1.5)$ and $(\pm1.5,\pm0.5)$.
Prove that if you '^@draw@ $(x,y)$' with this pen, the result never has
both top-bottom and left-right symmetry.

#### Answer
No matter where you place the octagon so that it isn't touching
any ambiguous points, exactly seven ambiguous points are inside it; hence
every one-point ^@draw@ fills exactly seven pixels. \ (In fact,
you always get one of the patterns
$\vcenter{{\offinterlineskip\manual
{\kern\Blankpix RR}RRR{\kern\Blankpix RR}}}$,
$\vcenter{{\offinterlineskip\manual
{\kern\Blankpix R}RRRRRR}}$,
$\vcenter{{\offinterlineskip\manual
RRRRRRR}}$, or
$\vcenter{{\offinterlineskip\manual
RRRRRR{\kern\Blankpix R}}}$.)

**[Double Dangerous Bend]** Rounding can also help to position points at which we don't
have horizontal or vertical tangents. For example, consider the
"" or "" character that's drawn by the
\rightfig 24e ({300\apspix} x {320\apspix}) ^-60pt
following program:

>
$u\0:={10\over18}"pt"\0$; \ @define\_pixels@$(u)$;
@beginchar@$\,(0,15u\0,{250\over36}"pt"\0,{70\over36}"pt"\0)$;
@pickup@ @pencircle@
scaled $(.4"pt"+"blacker")$;
$"lft"\,x_1=\round u-"eps"$;
$x_3=x_1$;
$x_2=x_4=w-x_1$;
$y_1=y_2="good.y"(.5[-d,h]+1.1"pt")$;
$y_3=y_4=h-d-y_1$;
@draw@ $z_1\dashto z_2$; \ @draw@ $z_3\dashto z_4$;
$"lft"\,x_6=\round 3u$;
$x_7=w-x_6$;
$x_8="good.x"\,.5w$;
$x_5-x_6=x_7-x_8$;
$"top"\,y_5="top"\,y_7=h+"eps"$;
$"bot"\,y_6="bot"\,y_8=-d-"eps"$;
@draw@ $z_5\dashto z_6$; \ @draw@ $z_7\dashto z_8$;
@labels@(^@range@ 1 ^@thru@ 8);
@endchar@.

If we digitize this character according to ^"lowres" mode at 200
pixels per inch, we get the following results:

>
{\manual\offinterlineskip#
SSSSSSSSSSSRSSSSSRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRSSSSSRSSSSSSSSSSS
}
{\manual\offinterlineskip#
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
}
{\manual\offinterlineskip#
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSSRRSSSSRRSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSSSSSSSSRRSSSSRRSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSSRRSSSSRRSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSSSSSSRRSSSSRRSSSSSSSS
SSRRRRRRRRRRRRRRRRRRRSS
SSRRRRRRRRRRRRRRRRRRRSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSSRRSSSSRRSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
SSSSSRRSSSSRRSSSSSSSSSS
}

The left-hand example was obtained by omitting the 'round' and '"good.x"'
instructions in the equations for $x_6$ and $x_8$. This meant that points
$z_6$ and $z_8$ fell into different, possibly unlucky, raster positions,
so the two diagonal strokes digitized differently even though they
came from essentially identical undigitized lines. The middle example
was produced by the given program without changes. And the right-hand
example was produced by drawing the diagonals in a more complicated way:
The commands '@draw@ $z_5\dashto z_6$; @draw@ $z_7\dashto z_8$;' were
replaced by

>
$y_15=y_1$; \ $z_15="whatever"[z_5,z_6]$; \
$y_36=y_3$; \ $z_36="whatever"[z_5,z_6]$;
$y_27=y_2$; \ $z_27="whatever"[z_7,z_8]$; \
$y_48=y_4$; \ $z_48="whatever"[z_7,z_8]$;

@draw@ $z_5\dashto("good.x"(x_15+.5),y_1)\dashto("good.x"(x_15-.5),y_1)$
$\dashto("good.x"(x_36+.5),y_3)\dashto("good.x"(x_36-.5),y_3)
\dashto z_6$;
@draw@ $z_7\dashto("good.x"(x_27+.5),y_2)\dashto("good.x"(x_27-.5),y_2)$
$\dashto("good.x"(x_48+.5),y_4)\dashto("good.x"(x_48-.5),y_4)
\dashto z_8$;

The idea here was to control the goodness of the points where the
diagonals intersect the horizontal bar lines, and to hide one of the
"" inside each bar line. If we do the same three experiments
but triple the resolution, we get similar results but the differences are
not quite so obvious:

>
{\manual\offinterlineskip#
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
}
{\manual\offinterlineskip#
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
}
{\manual\offinterlineskip#
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
}

**[Dangerous Bend]** When letters are drawn by filling outlines, the left and right
outlines are digitized independently; therefore corresponding outlines
should usually be offset from each other by an integer amount whenever
possible. For example, suppose that the letter '' is being drawn
with commands like

>
$\penpos2("stem",0)$; \ $\penpos4("stem",0)$

to specify the stroke widths at the base of the two .
We will therefore have $x_2r-x_2l=x_4r-x_4l="stem"$. If
"stem" is not an integer, say $"stem"=2.7$, we might have
$x_2l=2.1$, $x_2r=4.8$, $x_4l=9.6$, $x_4r=12.3$;
then $x_2r-x_2l$ will digitize to $5-2=3$, so the left stem
will be three pixels wide, but the right stem will be only
$12-10=2$ pixels wide. We could get around this problem by
insisting that either $x_2l$ or $x_2r$ be an integer,
and that either $x_4l$ or $x_4r$ be an integer; then both stems
would be three pixels wide. But other quantities calculated from "stem"
(e.g., the breadth of diagonal strokes) would then be based on a
value of 2.7 instead of the stem width 3 that an observer of the
font actually perceives. Therefore it is best to make "stem" an integer.
The proper way to do this is generally to say

>
^@define\_whole\_blacker\_pixels@("stem");

this command computes "stem" from $"stem"\0$ by the formula

>
$"stem":=\max\bigl(1,\,\round("stem"\0\ast"hppp"+"blacker")\bigr)$.

(Notice that this rounding operation is not allowed to reduce "stem"
to zero at low resolutions.)

**[Dangerous Bend]** Even when the "stem" width is an integer in the 'n' example,
we probably want to arrange things so that $x_2l$, $x_2r$, $x_4l$,
and $x_4r$ are integers, because this will give the least distortion
under digitization. Suppose, however, that it's most convenient to define
the pen position at the center of the stroke instead of at the edge; i.e.,
the program would say just '$x_2=\alpha$' if rounding were not taken into
account. How should $x_2$ be defined, when we want $x_2l$ to be an
integer? We could say

>
$x_2=\alpha$; \ $x_2l:=\round x_2l$; \ $x_2r:=\round x_2r$; \
$x_2:=.5[x_2l,x_2r]$

but that's too complicated; moreover, it will fail if any other
variables depend on $x_2$, $x_2l$, or $x_2r$, because such
dependencies are forgotten when new values are assigned.
In the case of fixed pens we solved this problem by saying
'$x_2="good.x"\,\alpha$'; but the "good.x" function doesn't know
about "stem". One solution is to say

>
$x_2l=\round(\alpha-.5"stem")$,

or equivalently, '$x_2r=\round(\alpha+.5"stem")$'. This does the
job all right, but it isn't completely satisfying. It requires
knowledge of the breadth that was specified in the $\penpos2$ command,
and it works only when the "penpos" angle is 0. If the "penpos" command
is changed, the corresponding equation for rounding must be
changed too. There's another solution that's more general and more
attractive once you get used to it:

>
$x_2l=\round\bigl(x_2l-(x_2-\alpha)\bigr)$.

Why does this work? The argument to '' must be a known value,
but both $x_2l$ and $x_2$ are unknown. Fortunately, their difference
$x_2l-x_2$ is known, because of the $\penpos2$ command. The
rounding operation makes $x_2\approx\alpha$ because it makes $x_2l$
approximately equal to the value of $x_2l$ minus the difference
between $x_2$ and $\alpha$.

**[Double Dangerous Bend]** exercise The generality of this technique can be appreciated
by considering the following more difficult problem that the author
faced while designing a '': Suppose you want $x_1-x_2$ to be
an integer and $x_3\approx x_4$, and suppose that $x_2$, $x_3-x_1$,
and $x_4+x_1$ are known; but $x_1$ is unknown, hence $x_3$ and $x_4$
are also unknown. According to our general idea, we want to specify an
equation of the form '$x_1-x_2=\round(x_1-x_2+f)$', where $x_1-x_2+f$
is known and $f$ is a formula that should be approximately zero.
In this case $x_3-x_4$ is approximately zero, and $(x_3-x_1)-(x_4+x_1)$
is known; what value of $f$ should we choose?

#### Answer
$f=.5(x_4-x_3)$; the desired equation is
'$x_1-x_2=\round\bigl(x_1-x_2+.5(x_4-x_3)\bigr)$'.

**[Double Dangerous Bend]** In many fonts, such as the one you are now reading,
curved lines swell out so that the thick parts of '' are actually
a bit broader than the stems of 'n'. Therefore the
font routines discussed in Appendix E have two parameters,
$"stem"\0$ and $"curve"\0$, to govern the stroke thickness.
For example, the font used in the present paragraph has
$"stem"\0=2/3"pt"\0$ and $"curve"\0=7/9"pt"\0$. Both of these should
be integers, hence the ^@font\_setup@ macro in Appendix E
dutifully says

>
@define\_whole\_blacker\_pixels@$("stem","curve")$.

Although this looks good on paper, it can cause problems at certain
low resolutions, because the rounding operation might make ^"stem" and
^"curve" rather different from each other even though $"stem"\0$ and
$"curve"\0$ are fairly close. For example, the resolution might be
just at the value where 'cmr9''s "stem" turns out to be only 2
but "curve" is 3. Curves shouldn't be that much darker than stems;
they would look too splotchy. Therefore plain METAFONT\
has a '^@lowres\_fix@' subroutine, and Appendix E says

>
@lowres\_fix@("stem","curve") 1.2

after "stem" and "curve" have been defined as above. In this particular
case @lowres\_fix@ will reset $"curve":="stem"$ if it turns out that the
ratio $"curve"/"stem"$ is greater than 1.2 times the ratio
$"curve"\0/"stem"\0$. Since $"curve"\0/"stem"\0=7/6$ in the case of 'cmr9',
this means that the ratio $"curve"/"stem"$ after rounding is allowed
to be at most 1.4; if $"curve"=3$ and $"stem"=2$, the "curve" parameter
will be lowered to 2. In general the command

>
@lowres\_fix@($d_1,d_2,\ldots,d_n$) $r$

will set $d_n:=\cdots d_2:=d_1$ if $\max(d_1,d_2,\ldots,d_n)/\!
\min(d_1,d_2,\ldots,d_n)$ is greater than
$r\cdot\max(d_1\0,d_2\0,\ldots,d_n\0)/\!\min(d_1\0,d_2\0,\ldots,d_n\0)$.

**[Double Dangerous Bend]** exercise
shape 12
3pc 201pt
3pc 201pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 237pt
0pc 29pc
\rightfig 4e ({180\apspix} x {225\apspix}) ^15pt
Good digitization can also require attention to the shapes of the
digitized angles where straight lines meet. The purpose of
the present exercise is to illustrate the relevant ideas by
studying the '{\manual}' symbol, for which a program
appears in Chapter 4. If that program is used without change to produce
low-resolution s, the results might turn out to be unsatisfactory
because, for example, point 3 at the right of the triangle
might digitize into a snubnosed or asymmetric shape.
If $y_3$ is an integer, the triangle will be top-bottom symmetric, but
the right-hand tip will be two pixels tall and this will look too blunt.
Therefore we should choose $y_3$ to be an integer plus 1/2.
Given this value of $y_3$, what will be the shape of the rightmost
four columns of the digitized tip, as $x_3$ varies?

#### Answer
Let $x_3=n+{1\over2}+\theta$, where $n$ is an integer and
$0\le\theta<1$. By drawing lines of slope $30^\circ$ from the pixel
centers, we find that there are three cases for the rightmost four
columns:

>
Case A,
$\vcenter{{\offinterlineskip\manual
RRRRRRRR}}$;
Case B,
$\vcenter{{\offinterlineskip\manual
RRRRRRRRRR}}$;
Case C,
$\vcenter{{\offinterlineskip\manual
RRRRRRRRRRRR}}$.

Case A occurs for $0\le\theta<2\sqrt3-3$; Case B occurs for
$2\sqrt3-3\le\theta<\sqrt3-1$; Case C occurs for
$\sqrt3-1\le\theta<1$. The tip in Case A looks a bit too sharp,
and Case C looks too blunt, so Case B seems best. This case occurs
when $x_3$ is near an integer, so it's OK to let $x_3$ be an integer.

**[Double Dangerous Bend]** exercise Continuing the previous exercise, assume that $x_1$
is an integer. What value of $y_1$ will make the upper tip of the
triangle look like
'$\vcenter{{\offinterlineskip\manual
RRRRRRR}}$' after digitization?

#### Answer
Let $y_1=n+\theta$. If $\theta$ lies between
${1\over2}\sqrt3-{1\over2}$ and ${1\over6}\sqrt3+{1\over2}$,
the top row after digitization will contain two black pixels.
If $\theta$ lies between ${1\over6}\sqrt3+{1\over2}$ and
${5\over6}\sqrt3-{1\over2}$, we get the desired shape. Otherwise
we get '$\vcenter{{\offinterlineskip\manual
RRRRRRRR}}$'.

**[Double Dangerous Bend]** exercise Concluding the previous exercise, modify the
program of Chapter 4 so that the upper tip and
the upper part of the right tip both digitize to the shape
'$\vcenter{{\offinterlineskip\manual
RRRRRRR}}$'.

#### Answer
(We choose $\theta={1\over2}\sqrt3$ in the previous exercise, since
this is the midpoint of the desirable interval.) The equations
are changed to

>
$x_1=x_2=w-x_3=\round s$;
$y_3=.5+floor\,.5h$;
$z_1-z_2=(z_3-z_2)$ rotated 60;
$y_1:=.5sqrt3+\round(y_1-.5sqrt3)$;
$y_2:=h-y_1$;

and then we @fill@ $z_1\dashto z_2\dashto z_3\dashto\cycle$ as before.

**[Double Dangerous Bend]** So far in this chapter we've assumed that pixels are square. But
sometimes we need to prepare output for devices with
general rectangular pixels, and this adds an extra dimension of
complexity to rounding. Plain METAFONT\ sets things up so that
^"currenttransform" multiplies all $y$ coordinates by
^"aspect\_ratio", when paths are filled or drawn, or when pens are
picked up. Furthermore the ^"top" and ^"bot" functions divide the
amount of offset by "aspect\_ratio". This means that METAFONT\ programs
can still be written as if pixels were square;
the normal 'angle' and 'direction' functions, etc., can be used.
But the good places for rounding horizontal tangents are not at
integer values of $y$ in general, they are actually at values that
will become integers after multiplication by the aspect ratio.

**[Double Dangerous Bend]** The ^"vround" function rounds its argument to the nearest
$y$ coordinate that corresponds to a pixel boundary in the
general case. Thus if $"aspect\_ratio"=1$, "vround" simply rounds
to the nearest integer, just like 'round'; but if, say,
$"aspect\_ratio"=4/3$, then "vround" will round to the nearest
multiple of $3/4$. Plain METAFONT\ uses "vround" instead of 'round'
when it computes an correction, and also when ^@beginchar@
computes the values of and . The ^"good.y" function produces
a good $y$ value that takes "aspect\_ratio" properly into account.

**[Double Dangerous Bend]** exercise Without looking at Appendix B, try to guess how
the "vround" and "good.y" macros are defined.

#### Answer
@vardef@ "vround" @primary@ $v$ $=$break
floor$(v\ast"aspect\_ratio"+.5)/"aspect\_ratio"$ @enddef@;break
@vardef@ "good.y" @primary@ $y$ $=$break
"vround"$(y+"pen\_top")-"pen\_top"$ @enddef@.

**[Double Dangerous Bend]** exercise What are the "ambiguous points" when pixels
are not square?

#### Answer
$\bigl(m+1/2,(n+1/2)/"aspect\_ratio"\bigr)$. These are the points
that "currenttransform" maps into pixel centers.

**[Double Dangerous Bend]** The METAFONT\ as we have described it so far will round
properly with respect to arbitrary aspect ratios if we make only
a few more refinements. The value of "ygap" should be vrounded
instead of rounded, so we initialize it by saying

>
^@define\_whole\_vertical\_pixels@("ygap").

Furthermore we should say

>
$"ho"\0:=o\0$; \ ^@define\_horizontal\_corrected\_pixels@("ho");

and "ho" should replace in the equations for $x_4$ in the programs
for '{\manual i}' and '{\manual l}'.
Everything else should work satisfactorily as it stands.

**[Double Dangerous Bend]** Appendix B includes macros ^"good.top", ^"good.bot", ^"good.lft",
and ^"good.rt" that take pairs as arguments. If you say, for example,
'$z_3="good.top"(\alpha,\beta)$' it means that $z_3$ will be near
$(\alpha,\beta)$ and that when $z_3$ is modified by ^"currenttransform"
the top point of ^"currentpen" placed at the transformed point will
be in a good raster position.

**[Dangerous Bend]** METAFONT's '^"autorounding"' feature tries to adjust curves to the
raster for you, but it is a mixed blessing. Here's how it works:
If the internal quantity "autorounding" is positive, the $x$ coordinates
of all paths that are filled or drawn are rounded to good raster positions
wherever there's a vertical tangent; and the $y$ coordinates
are rounded to good raster positions wherever there's a horizontal
tangent. The rest of the curve is distorted appropriately, as if
the raster were stretching or shrinking slightly. If $"autorounding">1$,
you get even more changes: Paths are perturbed slightly at $\pm45^\circ$
tangent directions, so that second-order and flat spots don't
appear there.

**[Dangerous Bend]** For example, if we return to the Ionian '{\manual\IOO}' with
which we began this chapter, let's suppose that "curve\_sidebar" was left
unrounded. We saw that the result was bad when "autorounding" was 0;
when $"autorounding"=1$ and 2 we get this:
\displayfig 24f\&g (190\apspix)
The stroke has gotten a lot thinner at the sides, by comparison with
the original design (which, incidentally, can be seen in the illustrations
below). Although autorounding has produced a fairly recognizable O shape,
the character of the original has been lost, especially in the case
$"autorounding"=2$; indeed, the inner outline has been brought towards the
center, in the upper left and lower right sectors, and this has made the
digitized inner boundary perfectly symmetric!

**[Double Dangerous Bend]** There's an internal quantity called ^"granularity", normally
equal to 1, which affects autorounding by effectively scaling up
the raster size. If, for example, $"granularity"=4$, the autorounded
$x$ coordinates and $y$ coordinates will become multiples of 4 instead
of simply integers. The illustrations above were produced by
setting $"granularity"=10$ and $"mag"=10$; this made the
effects of autorounding visible. The granularity should always be an integer.

**[Double Dangerous Bend]** Besides "autorounding", there's a 'smoothing' feature
that becomes active when ^"smoothing"$>0$. The basic idea is
to try to make the edges of a curve follow a regular progression
instead of wobbling. A complete discussion of the smoothing algorithm
is beyond the scope of this manual, but an example should make the
general idea clear: Let's use the letters $R$ and $D$ to stand for
single-pixel steps to the right and down, respectively. If a digitized
path goes '"RDDRDRDDD"', say, the number of downward steps per
rightward step is first decreasing, then increasing; the "smoothing"
process changes this to '"RDDRDDRDD"'. If smoothing is applied to the
Ionian '{\manual\IOO}' shapes above, nothing happens; but if we go back
to the original obtained with $"autorounding"=0$, we get a few changes:
\displayfig 24b\&h (190\apspix)
Three pixels have been added by "smoothing" in the right-hand illustration;
e.g., a pattern "RDRDDDDRDD" has become "RDDRDDDRDD".

**[Dangerous Bend]** If you do your own rounding, it turns out that autorounding
and smoothing usually change very few pixels, if any; thus your
safest strategy is probably to turn them off in such cases. If you
define your strokes by outlines, autorounding and smoothing
apply independently to the left and right edges, so they may
hurt as often as they help; again, they should probably be turned off.
But if you are drawing with fixed pens, autorounding generally
works well and saves a lot of fuss. If the pens are circles or
nearly circles, smoothing is also helpful; but if the pens are
more "calligraphic," they are supposed to produce nonsmooth
edges occasionally, so you had better set $"smoothing":=0$.

**[Double Dangerous Bend]** If you "" a font by modifying "currenttransform"
as described in Chapter 15, positions of horizontal tangency will
remain the same. But positions of vertical tangency will change
drastically, and they will probably not fall in known parts
of your design. This means, for example, that autorounding will be
helpful in a slanted pen-generated font like the
'{\manual 89:;<=>:}' logo. However, the author
found that the outline-generated letters of
came out better with $"autorounding"=0$, because
autorounding tended to make some characters too dark and others too light.

**[Double Dangerous Bend]** The effect of autorounding can be studied numerically
if you set ^"tracingspecs" to a positive value; this displays METAFONT's
internal calculations as it finds horizontal, vertical, and diagonal
tangent points. \ (METAFONT\ prepares to digitize paths by first
subdividing each B\'ezier segment into pieces that travel in only one
"" direction.) \ For example, if $"autorounding"=0$
and $"tracingspecs"=1$, and if "curve\_sidebar" is left unrounded,
the file 'io.log' will contain the following information about the
outer curve of the '{\manual\IOO}':
\beginlines .71pt
'Path at line 15, before subdivision into octants:'
'(1.53745,9.05345)..controls (1.53745,4.00511) and (5.75409,-0.00049)'
' ..(10.85147,-0.00049)..controls (16.2217,-0.00049) and (20.46255,4.51297)'

' ..(20.46255,9.94655)..controls (20.46255,14.99713) and (16.23842,19.00049)'

' ..(11.13652,19.00049)..controls (5.77066,19.00049) and (1.53745,14.48491)'

' ..cycle'

'Cycle spec at line 15, after subdivision:'
|(1.53745,9.05345)
' ..controls (1.53745,6.58786) and (2.54324,4.371)'
| ..(4.16621,2.74803)
|
' ..controls (5.8663,1.04794) and (8.24362,-0.00049)'
| ..(10.85147,-0.00049)
|
\endlines
$\ldots$ and so on; there are lots more numbers! What does this all mean?

Well, the first segment of the curve, from $(1.53745,9.05345)$ to
$(10.85147,-0.00049)$,
has been subdivided into two parts at the place where the slope is $-1$.
The first of these parts travels basically 'South by South East' and
the second travels 'East by South East'. The other three segments are
subdivided in a similar way (not shown here). If you try the same
experiment but with $"autorounding"=1$, some rather different numbers
emerge: \looseness=-1

\beginlines
'Cycle spec at line 15, after subdivision and autorounding:'
|(2,9.05348)
' ..controls (2,6.50526) and (3.02194,4.22272)'
| ..(4.6577,2.58696)
|
' ..controls (6.2624,0.98225) and (8.45786,0)'
| ..(10.85873,0)
|
\endlines
Point $(1.53745,9.05345)$, where there was a vertical tangent, has been
rounded to $(2,9.05348)$; point $(10.85147,-.00049)$, where there was
a horizontal tangent, has been rounded to $(10.85873,0)$; the intermediate
control points have been adjusted accordingly. \ (Rounding of $x$ coordinates
has been done separately from $y$ coordinates.) \ Finally, with
$"autorounding"=2$, additional adjustments are made so that the
$45^\circ$ transition point will occur at what METAFONT\ thinks is a good spot:
\beginlines
'Cycle spec at line 15, after subdivision and double autorounding:'
|(2,9.05348)
' ..controls (2,6.6761) and (3.07103,4.42897)'
| ..(4.78537,2.71463)
|
' ..controls (6.46927,1.03073) and (8.62749,0)'
| ..(10.85873,0)
|
\endlines
(Notice that $4.78537+2.71463=7.50000$; when the slope
is $-1$ at a transition point $(x,y)$, the curve stays as far away as
possible from ambiguous points near the transition if $x+y+.5$ is an integer.)

\endchapter

{{\offinterlineskip\manual{#
SRRRRRRRRRSSSSSSSSSSSRRRRRRSSSSSSSRRRRRRRRRSSSSSSS
SSRRRSSSSSRRSSSSSSSRRSSSSSSRRSSSSSSRRRSSSSRRSSSSSS
SSSRRSSSSSSRRSSSSSRRSSSSSSSSRRSSSSSSRRSSSSSRRSSSSS
SSSRRSSSSSSRRSSSSRRSSSSSSSSSSRRSSSSSRRSSSSSRRSSSSS
SSSRRSSSSSSRRSSSRRSSSSSSSSSSSSRRSSSSRRSSSSSRRSSSSS
SSSRRSSSSSSRRSSSRRSSSSSSSSSSSSRRSSSSRRSSSSSRRSSSSS
SSSRRSSSSSSRRSSRRSSSSSSSSSSSSSSRRSSSRRSSSSSRRSSSSS
SSSRRSSSSSRRSSSRRSSSSSSSSSSSSSSRRSSSRRSSSSRRSSSSSS
SSSRRSSRRRRSSSSRRSSSSSSSSSSSSSSRRSSSRRRRRRSSSSSSSS
SSSRRSSSSSSSSSSRRSSSSSSSSSSSSSSRRSSSRRSSRRRSSSSSSS
SSSRRSSSSSSSSSSRRSSSSSSSSSSSSSSRRSSSRRSSSRRRSSSSSS
SSSRRSSSSSSSSSSRRSSSSSSSSSSSSSSRRSSSRRSSSSRRRSSSSS
SSSRRSSSSSSSSSSSRRSSSSSSSSSSSSRRSSSSRRSSSSSRRRSSSS
SSSRRSSSSSSSSSSSRRSSSSSSSSSSSSRRSSSSRRSSSSSSRRSSSS
SSSRRSSSSSSSSSSSSRRSSSSSSSSSSRRSSSSSRRSSSSSSRRRSSS
SSSRRSSSSSSSSSSSSSRRSSSSSSSSRRSSSSSSRRSSSSSSSRRRSS
SSRRRRSSSSSSSSSSSSSRRSSSSSSRRSSSSSSRRRRSSSSSSSRRRS
SRRRRRRSSSSSSSSSSSSSSRRRRRRSSSSSSSRRRRRRSSSSSSSRRR
\kern23\Blankpix RRR
\kern24\Blankpix RRR
\kern25\Blankpix RRR
\kern26\Blankpix RRRR
}}}

> --- PIERRE , *B\'ele Pr\'erie* (1601)

{{\offinterlineskip\manual#
QQQQQPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQPPPPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQPPPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQPPPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
\kern7\blankpix}{\offinterlineskip\manual{#
\kern19\blankpix PPPPPPPPPP
QQQQQQQQQQQQQQQQPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQ
QQQQQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQ
QQQQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQ
QQQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQ
QQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQ
QQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQ
QQQQQQQPPPPPPPPPPPPPPQQQQQQPPPPPPPPPPPPPPQQQQQQQ
QQQQQQQPPPPPPPPPPPPQQQQQQQQQQPPPPPPPPPPPPQQQQQQQ
QQQQQQPPPPPPPPPPPPQQQQQQQQQQQQPPPPPPPPPPPPQQQQQQ
QQQQQQPPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQQ
QQQQPPPPPPPPPPPQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQQ
QQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQPPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQQQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQQPQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQQPPQQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPQQQQQQQQQQPPPPQQQQQQQQPPPPPPPPPPQQQ
QQQPPPPPPPPPPPQQQQQQQQPPPPPPQQQQQQQPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQQQPPPPPPPPQQQQQQPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQQPPPPPPPPPQQQQQQPPPPPPPPPQQQQ
QQQQPPPPPPPPPPQQQQQPPPPPPPPPPPQQQQQPPPPPPPPQQQQQ
QQQQPPPPPPPPPPQQQQQQQPPPPPPPPPPQQQQPPPPPPPPQQQQQ
QQQQPPPPPPPPPPPQQQQQQQPPPPPPPPPPQQQPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQPPPPPPPPPQQQPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPQQQQQQQQPPPPPPPPQQQPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPPPPPPQQQQQQ
QQQQQQPPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPPPPQQQQQQQ
QQQQQQPPPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPPQQQQQQQQ
QQQQQQQPPPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPQQQQQQQQ
QQQQQQQPPPPPPPPPPPPPPQQQQQQQQPPPPPPPPPPQQQQQQQQQ
QQQQQQQQPPPPPPPPPPPPPPPQQQQQQPPPPPPPPPQQQQQQQQQQ
QQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQ
QQQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQ
QQQQQQQQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQ
QQQQQQQQQQQQPPPPPPPPPPPPPPPPPPPPQQPPPPPPPPQQQQQQ
QQQQQQQQQQQQQQPPPPPPPPPPPPPPPPPPQQPPPPPPPPPQQQQQ
QQQQQQQQQQQQQQQQPPPPPPPPPPPPPPQQQQPPPPPPPPPPQQQQ
\kern19\blankpix PPPPPPP\kern9\blankpix PPPPPPPPPPP
\kern36\blankpix PPPPPPPPP
\kern37\blankpix PPPPPPP
\kern37\blankpix PPPPPP
\kern38\blankpix PPPP
\kern39\blankpix PP
\kern39\blankpix P
}}{\offinterlineskip\manual#
QQQQQPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQPPPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQPPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQPPPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPPPPPPQPPPPPPPPPQQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQPPPPPPPPPPQQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQPPPPPPPPPPPQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQPPPPPPPPPPQQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQPPPPPPPPPPPQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQPPPPPPPPPPQQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQPPPPPPPPPPPQQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQPPPPPPPPPPPQQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQPPPPPPPPPPPQQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQPPPPPPPPPPPQQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQPPPPPPPPPPPQQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQPPPPPPPPPPPQQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQPPPPPPPPPPPQQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPPQQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQPPPPPPPPPPPPQQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPPPQ
QQQQQPPPPPPPPPPQQQQQQQQQQQQQQQQPPPPPPPPPPPPQ
\kern7\blankpix}}

> --- MATTHEW , *Bell Centennial* (1978)

\beginChapter Chapter 25. Summary of\\Expressions

We've seen that METAFONT\ can handle a wide variety of algebraic ;
now it's time to consolidate what we have learned. The purpose of this
chapter and the one that follows is to present a precise and concise
summary of everything that METAFONT\ knows how to do.

We shall be concerned here solely with METAFONT's operations,
rather than with the higher-level features of the plain METAFONT\ base that
comprise the bulk of typical programs. Therefore novice users should put
off reading Chapters 25 and 26 until they feel a need to know what
goes on at the more mundane levels inside the computer. Appendix B contains
a summary of the features of plain METAFONT\!, together with a ready-reference guide
to the things that most people want to know about METAFONT\ usage.

The remainder of this chapter is set in small type, like that of the
present paragraph, since it is analogous to material that is marked
"doubly dangerous" in other chapters. Instead of using dangerous
bend signs repeatedly, let us simply agree that Chapters 25 and 26 are
dangerous by definition.

Chapter 8 introduced the general idea of expressions and the four-fold
"primary, secondary, tertiary, expression" on which
their syntax is based. METAFONT's variables can have any of eight types:
@boolean@, @numeric@, @pair@, @path@, @pen@, @picture@, @string@,
and @transform@. Its expressions can actually have nine different
types, although the ninth one---""---is not particularly
interesting since it has only one possible value. Here is the overall
syntax:
\beginsyntax
<primary>\is<boolean primary>\alt<numeric primary>
\alt<pair primary>\alt<path primary>
\alt<pen primary>\alt<future pen primary>
\alt<picture primary>\alt<string primary>
\alt<transform primary>\alt<vacuous primary>\endgraf
<secondary>\is<boolean secondary>\alt<numeric secondary>
\alt<pair secondary>\alt<path secondary>
\alt<pen secondary>\alt<future pen secondary>
\alt<picture secondary>\alt<string secondary>
\alt<transform secondary>\alt<vacuous secondary>\endgraf
<tertiary>\is<boolean tertiary>\alt<numeric tertiary>
\alt<pair tertiary>\alt<path tertiary>
\alt<pen tertiary>\alt<picture tertiary>
\alt<string tertiary>\alt<transform tertiary>
\alt<vacuous tertiary>\endgraf
<expression>\is<boolean expression>\alt<numeric expression>
\alt<pair expression>\alt<path expression>
\alt<pen expression>\alt<picture expression>
\alt<string expression>\alt<transform expression>
\alt<vacuous expression>
\endsyntax
We shall discuss the different types of expressions in alphabetic order;
thus, if you are dying to know what a "vacuous" expression is,
you should skip to the end of the chapter. \looseness=-1

\medbreak
-
Boolean expressions were discussed in Chapter 19. The full syntax has
one more operation, 'charexists', that was not mentioned there:
\beginsyntax
<boolean primary>\is<boolean variable>\alt<boolean argument>
\alt[true]\alt[false]
\alt[(]<boolean expression>[)]
\alt[begingroup]<statement list><boolean expression>[endgroup]
\alt[known]<primary>\alt[unknown]<primary>
\alt<type><primary>\alt[cycle]<primary>
\alt[odd]<numeric primary>
\alt[charexists]<numeric primary>
\alt[not]<boolean primary>
<boolean secondary>\is<boolean primary>
\alt<boolean secondary>[and]<boolean primary>
<boolean tertiary>\is<boolean secondary>
\alt<boolean tertiary>[or]<boolean secondary>
<boolean expression>\is<boolean tertiary>
\alt<numeric expression><relation><numeric tertiary>
\alt<pair expression><relation><pair tertiary>
\alt<transform expression><relation><transform tertiary>
\alt<boolean expression><relation><boolean tertiary>
\alt<string expression><relation><string tertiary>
<relation>\is[]\alt[=]\alt[>]\alt[>=]\alt[=]\alt[>]
\endsyntax
The expression 'charexists $x$' is true if and only if a ^@shipout@
command has previously been done with ^"charcode"$=x$. \ (The value
of $x$ is first rounded to an integer, and reduced to the range
$0\le x<256$ by adding or subtracting multiples of 256.)

In these rules, tokens like "true'' that appear in typewriter type stand for
any whose current meaning is the same as the meaning of "true''
when METAFONT\ starts from scratch; the particular token "true''---whose
meaning may indeed change as a program runs---is not really involved.

The special tokens "('' and ")'' in these rules do not refer to
; they refer to any matching pair of defined
by a ^@delimiters@ command.

A *boolean variable* denotes a ^*variable* whose type is @boolean@; a
$\langle$numeric variable$\rangle$ is a *variable* whose type is
@numeric@; and so on. The syntax for *variable* was discussed in
Chapter 7. A *boolean argument* is an ^@expr@ to a macro,
where the value of the expression is of type @boolean@;
@expr@ arguments are put into special ""
tokens as explained in Chapter 18.

\medbreak
-
Numeric expressions have the richest syntax of all, because they form the
nucleus of the entire METAFONT\ language:
\beginsyntax
<numeric atom>\is<numeric variable>\alt<numeric argument>
\alt<numeric token primary>
\alt<internal quantity>
\alt[normaldeviate]
\alt[(]<numeric expression>[)]
\alt[begingroup]<statement list><numeric expression>[endgroup]
\alt[length]<numeric primary>\alt[length]<pair primary>
\alt[length]<path primary>\alt[length]<string primary>
\alt[ASCII]<string primary>\alt[oct]<string primary>\alt[hex]<string primary>
\alt<pair part><pair primary>\alt<transform part><transform primary>
\alt[angle]<pair primary>
\alt[turningnumber]<path primary>\alt[totalweight]<picture primary>
\alt<numeric operator><numeric primary>
\alt[directiontime]<pair expression>[of]<path primary>
<numeric token primary>\is<numeric token>[/]<numeric token>
\alt<numeric token not followed by
'/$\langle$numeric token$\rangle$'>
<numeric primary>\is<numeric atom not followed by []<expression>[,]>
\alt<numeric atom>[]<numeric expression>
[,]<numeric expression>[]
<pair part>\is[xpart]\alt[ypart]
<transform part>\is<pair part>\alt[xxpart]\alt[xypart]\alt[yxpart]\alt[yypart]
<numeric operator>\is[sqrt]\alt[sind]\alt[cosd]\alt[mlog]\alt[mexp]
\alt[floor]\alt[uniformdeviate]\alt<scalar multiplication operator>
<scalar multiplication operator>\is<plus or minus>
\alt<numeric token primary not followed by + or - or a numeric token>
<numeric secondary>\is<numeric primary>
\alt<numeric secondary><times or over><numeric primary>
<times or over>\is[*]\alt[/]
<numeric tertiary>\is<numeric secondary>
\alt<numeric tertiary><plus or minus><numeric secondary>
\alt<numeric tertiary><Pythagorean plus or minus><numeric secondary>
<plus or minus>\is[+]\alt[-]
<Pythagorean plus or minus>\is[++]\alt[+-+]
<numeric expression>\is<numeric tertiary>
\endsyntax
Each of the operations mentioned in this syntax has already been explained
somewhere in this book; Appendix I tells where.

\medbreak
This is a good time to list all of the internal quantities that are
initially present in METAFONT:

>
^"tracingtitles"&show titles online when they appear
^"tracingequations"\hidewidth&show each variable when it becomes known
^"tracingcapsules"\hidewidth&show capsules as well as variables
^"tracingchoices"&show the control points chosen for paths
^"tracingspecs"&show subdivision of paths into octants before digitizing
^"tracingpens"&show vertices of pens as they are made from future pens
^"tracingcommands"\hidewidth
&show commands and operations before they're performed
^"tracingrestores"&show when a symbol or internal quantity is restored
^"tracingmacros"&show macros before they are expanded
^"tracingedges"&show digitized edges as they are computed
^"tracingoutput"&show digitized edges as they are output
^"tracingonline"&show long diagnostics on the terminal and in the log
^"tracingstats"&log the memory usage at end of job
^"pausing"&show lines on the terminal before they are read
^"showstopping"&stop after each @show@ command
^"fontmaking"&produce font metric output
^"proofing"&produce proof mode output
^"turningcheck"&reorient clockwise paths, flag strange ones
^"warningcheck"&advise when a variable value gets large
^"smoothing"&remove certain glitches from digitized curves
^"autorounding"&move paths to "good" tangent points
^"granularity"&the pixel size for "autorounding"
^"fillin"&the extra darkness of diagonals (to be counteracted)
^"year"&the current year (e.g., 1986)
^"month"&the current month (e.g., 3 $\equiv$ March)
^"day"&the current day of the month
^"time"&the number of minutes past midnight when job started
^"charcode"&the number of the next character to be output
^"charext"&the extension code of the next character to be output
^"charwd"&the width of the next character to be output, in points
^"charht"&the height of the next character to be output, in points
^"chardp"&the depth of the next character to be output, in points
^"charic"&the italic correction of the next character, in points
^"chardx"&the device's $x$ movement for the next character, in pixels
^"chardy"&the device's $y$ movement for the next character, in pixels
^"designsize"&the approximate size of the current typeface, in points
^"hppp"&the number of horizontal pixels per point
^"vppp"&the number of vertical pixels per point
^"xoffset"&the horizontal displacement of shipped-out characters
^"yoffset"&the vertical displacement of shipped-out characters
^"boundarychar"&the right boundary character for ligatures and kerns

All of these quantities are numeric. They are initially zero at the
start of a job, except for "year", "month", "day", and "time", which
are initialized to the time the run began; furthermore, "boundarychar" is
initially $-1$. A "granularity" of zero is equivalent to $"granularity"=1$.
A preloaded base file like plain METAFONT\ will usually give nonzero values to
several other internal quantities on this list.

\medbreak
-
Now we come to expressions of type @pair@, which are the second most
important elements of METAFONT\ programs:
\beginsyntax
<pair primary>\is<pair variable>\alt<pair argument>
\alt[(]<numeric expression>[,]<numeric expression>[)]
\alt[(]<pair expression>[)]
\alt[begingroup]<statement list><pair expression>[endgroup]
\alt<numeric atom>[]<pair expression>[,]<pair expression>[]
\alt<scalar multiplication operator><pair primary>
\alt[point]<numeric expression>[of]<path primary>
\alt[precontrol]<numeric expression>[of]<path primary>
\alt[postcontrol]<numeric expression>[of]<path primary>
\alt[penoffset]<pair expression>[of]<pen primary>
\alt[penoffset]<pair expression>[of]<future pen primary>
<pair secondary>\is<pair primary>
\alt<pair secondary><times or over><numeric primary>
\alt<numeric secondary>[*]<pair primary>
\alt<pair secondary><transformer>
<transformer>\is[rotated]<numeric primary>
\alt[scaled]<numeric primary>
\alt[shifted]<pair primary>
\alt[slanted]<numeric primary>
\alt[transformed]<transform primary>
\alt[xscaled]<numeric primary>
\alt[yscaled]<numeric primary>
\alt[zscaled]<pair primary>
<pair tertiary>\is<pair secondary>
\alt<pair tertiary><plus or minus><pair secondary>
\alt<path tertiary>[intersectiontimes]<path secondary>
<pair expression>\is<pair tertiary>
\endsyntax
A pair is a special case of a path (namely, it's a path of length zero);
Chapter 19 explains that METAFONT\ doesn't change the type from pair to path
unless there is no other way to meet the syntax rules.

\medbreak
-
Speaking of paths, they come next in our survey:
\beginsyntax
<path primary>\is<pair primary>\alt<path variable>\alt<path argument>
\alt[(]<path expression>[)]
\alt[begingroup]<statement list><path expression>[endgroup]
\alt[makepath]<pen primary>\alt[makepath]<future pen primary>
\alt[reverse]<path primary>
\alt[subpath]<pair expression>[of]<path primary>
<path secondary>\is<pair secondary>\alt<path primary>
\alt<path secondary><transformer>
<path tertiary>\is<pair tertiary>\alt<path secondary>
<path expression>\is<pair expression>\alt<path tertiary>
\alt<path subexpression><direction specifier>
\alt<path subexpression><path join>[cycle]
<path subexpression>\is<path expression not ending with direction specifier>
\alt<path subexpression><path join><path tertiary>
<path join>\is<direction specifier><basic path join><direction specifier>
<direction specifier>\is<empty>
\alt[][curl]<numeric expression>[]
\alt[]<pair expression>[]
\alt[]<numeric expression>[,]<numeric expression>[]
<basic path join>\is[\&]
\alt[..]
\alt[..]<tension>[..]
\alt[..]<controls>[..]
<tension>\is[tension]<tension amount>
\alt[tension]<tension amount>[and]<tension amount>
<tension amount>\is<numeric primary>
\alt[atleast]<numeric primary>
<controls>\is[controls]<pair primary>
\alt[controls]<pair primary>[and]<pair primary>
\endsyntax
Chapter 14 tells all about path creation.

\medbreak
-
Pens and future pens coexist as follows:
\beginsyntax
<pen primary>\is<pen variable>\alt<pen argument>
\alt[nullpen]
\alt[(]<pen expression>[)]
\alt[begingroup]<statement list><pen expression>[endgroup]
<future pen primary>\is<future pen argument>
\alt[pencircle]
\alt[makepen]<path primary>
<pen secondary>\is<pen primary>
<future pen secondary>\is<future pen primary>
\alt<future pen secondary><transformer>
\alt<pen secondary><transformer>
<pen tertiary>\is<pen secondary>
\alt<future pen secondary>
<pen expression>\is<pen tertiary>
\endsyntax
See Chapter 16 for a thorough discussion of pen usage.

\medbreak
-
Pictures can be null, added, or subtracted:
\beginsyntax
<picture primary>\is<picture variable>\alt<picture argument>
\alt[nullpicture]
\alt[(]<picture expression>[)]
\alt[begingroup]<statement list><picture expression>[endgroup]
\alt<plus or minus><picture primary>
<picture secondary>\is<picture primary>
\alt<picture secondary><transformer>
<picture tertiary>\is<picture secondary>
\alt<picture tertiary><plus or minus><picture secondary>
<picture expression>\is<picture tertiary>
\endsyntax
Chapter 13 is the definitive reference for picture operations.

\medbreak
-
Strings are still fresh in our minds from Chapter 22, but we should
repeat the syntax again for completeness here.
\beginsyntax
<string primary>\is<string variable>\alt<string argument>
\alt<string token>
\alt[jobname]
\alt[readstring]
\alt[(]<string expression>[)]
\alt[begingroup]<statement list><string expression>[endgroup]
\alt[str]<suffix>
\alt[char]<numeric primary>
\alt[decimal]<numeric primary>
\alt[substring]<pair expression>[of]<string primary>
<string secondary>\is<string primary>
<string tertiary>\is<string secondary>
<string expression>\is<string tertiary>
\alt<string expression>[\&]<string tertiary>
\endsyntax
There's nothing more to say about strings.

\medbreak
-
Chapter 15 explains transforms, but gives no formal syntax. The rules are:
\beginsyntax
<transform primary>\is<transform variable>\alt<transform argument>
\alt[(]<transform expression>[)]
\alt[begingroup]<statement list><transform expression>[endgroup]
<transform secondary>\is<transform primary>
\alt<transform secondary><transformer>
<transform tertiary>\is<transform secondary>
<transform expression>\is<transform tertiary>
\endsyntax
Note that ^"identity" doesn't appear here; it is a variable defined
in Appendix B, not a primitive of the language.

\medbreak
-
Finally, we come to the new kind of expression, which wasn't mentioned
in previous chapters because it is so trivial.
\beginsyntax
<vacuous primary>\is<vacuous argument>
\alt<compound>
\alt[(]<vacuous expression>[)]
\alt[begingroup]<statement list><vacuous expression>[endgroup]
<vacuous secondary>\is<vacuous primary>
<vacuous tertiary>\is<vacuous secondary>
<vacuous expression>\is<vacuous tertiary>
\endsyntax
A *compound* is defined in Chapter 26.

**[Double Dangerous Bend]** exercise Construct minimal examples of each of the
nine types of expression (boolean, numeric, \dots, vacuous).
You should use only "" in your constructions, not *tag*
tokens or capsules; in particular, variables are not permitted
(otherwise this exercise would be too easy). Your expressions should
be as short as possible in the sense of *fewest tokens*; the number
of keystrokes needed to type them is irrelevant.

#### Answer
By looking at the syntax rules, we find, for example,

>
*boolean expression*&'true'
*numeric expression*&'0'
*pair expression*&'(0,0)'
*path expression*&'makepath pencircle'
*pen expression*&'nullpen'
*picture expression*&'nullpicture'
*string expression*&'""'
*transform expression*&Impossible!
*vacuous expression*&'begingroup endgroup'

Every *transform expression* includes either a variable or a capsule.
Incidentally, there are some amusing alternative 5-token solutions for
*pair expression*:

"'

postcontrol 0 of makepath nullpen
makepath pencircle intersectiontimes makepath nullpen

"'

\endchapter

This is of you very well remembred,
and well and sommaryly rehersed.

> --- THOMAS , *A Dialogue Concernynge Heresyes* (1529)

Below the tomato blobs was a band of white with vertical black stripes,
to which he could assign no meaning whatever,
till some one else came by, murmuring:
"What expression he gets with his foreground!"
...
Ah, they were all Expressionists now, he had heard, on the Continent.
So it was coming here too, was it?

> --- JOHN , *To Let* (1921)


# Chapter 26. Summary of the Language

The grand tour of METAFONT's syntax that was begun in the previous chapter
is concluded in this one, so that a complete reference guide is
available for people who need to know the details.
\ (Another summary appears in Appendix B.)

METAFONT\ actually has a few features that didn't seem to be worth mentioning
in earlier chapters, so they will be introduced here as part of our
exhaustive survey. If there is any disagreement between something that
was said previously and something that will be said below, the facts
in the present chapter should be regarded as better approximations
to the .

We shall study METAFONT's digestive processes, i.e., what METAFONT\ does in
response to the tokens that arrive in its "stomach."

Chapter 6 describes the process by which input files are converted to
lists of tokens in METAFONT's "mouth," and Chapters 18--20 explain how
expandable tokens are converted to unexpandable ones in METAFONT's "gullet"
by a process similar to regurgitation. In particular, conditions and
loops are handled by the expansion mechanism, and we need not
discuss them further. When unexpandable tokens
finally reach METAFONT's gastro-intestinal tract, the real activities
begin; expressions are evaluated, equations are solved, variables are
declared, and commands are executed. In this chapter we shall discuss the
primitive operations that actually draw pictures and produce output.

Let's start by looking at the full syntax for *program* and for
*statement*:
\beginsyntax
<program>\is<statement list><non-title statement>[end]
\alt<statement list><non-title statement>[dump]
<statement list>\is<empty>\alt<statement>[;]<statement list>
<statement>\is<empty>\alt<title>
\alt<equation>\alt<assignment>\alt<declaration>
\alt<definition>\alt<compound>\alt<command>
<title>\is<string expression>
<compound>\is[begingroup]<statement list><non-title statement>[endgroup]
<command>\is<save command>
\alt<interim command>
\alt<newinternal command>
\alt<randomseed command>
\alt<let command>
\alt<delimiters command>
\alt<protection command>
\alt<everyjob command>
\alt<show command>
\alt<message command>
\alt<mode command>
\alt<picture command>
\alt<display command>
\alt<openwindow command>
\alt<shipout command>
\alt<special command>
\alt<font metric command>
\endsyntax
The *empty* statement does nothing, but it is very handy because you can
always feel safe when you put extra semicolons between statements.
A *title* does almost nothing, but it provides useful documentation
as explained in Chapter 22.
The syntax of *equation* and *assignment* can be found in Chapter 10;
*declaration* is in Chapter 7; *definition* is in Chapters 18 and 20.
We shall concentrate in this chapter on the various types of **, especially on those that haven't been mentioned before.
\beginsyntax
<save command>\is[save]<symbolic token list>
<symbolic token list>\is<symbolic token>
\alt<symbolic token list>[,]<symbolic token>
<interim command>\is[interim]
<internal quantity>[:=]<right-hand side>
\endsyntax
The @save@ and @interim@ commands cause values to be restored at the end
of the current group, as discussed in Chapter 17.
\beginsyntax
<newinternal command>\is[newinternal]<symbolic token list>
\endsyntax
Each of the symbolic tokens specified in a @newinternal@ command will
henceforth behave exactly as an *internal quantity*, initially zero.
Thus, they can be used in @interim@ commands; they are but not
(see Chapter 7). Since METAFONT\ can access internal
quantities quickly, you can use them to gain efficiency.
\beginsyntax
<randomseed command>\is[randomseed][:=]<numeric expression>
\endsyntax
The @randomseed@ command specifies a "seed" value that defines
the pseudo-random numbers to be delivered by
'uniformdeviate' and 'normaldeviate' (cf. Chapter 21).
The default value, if you don't specify your own seed, is
^^"day" ^^"time" $"day"+"time"\ast"epsilon"$.
\beginsyntax
<let command>\is[let]<symbolic token><is><symbolic token>
<is>\is[=]\alt[:=]
\endsyntax
The @let@ command changes the current meaning of the left-hand token
to the current meaning of the right-hand token. For example,
after '@let@ $"diamonds"=@forever@$', the token "diamonds" will
introduce loops. If the left-hand token was the first token of
any variable names, those variables all disappear. If the right-hand
token was the first token in any variable names, those variables
remain unchanged, and the left-hand token becomes
an unknown, independent variable. \ (The purpose of @let@ is to redefine
primitive meanings or macro meanings, not to equate variables in any way.)
\ If the right-hand symbol is one of a pair of matching delimiters,
the subsequent behavior of the left-hand symbol is undefined.
For example, it's a bad idea to say '@let@ $[\,[=($; @let@ $]\,]=)$'.
\beginsyntax
<delimiters command>\is[delimiters]<symbolic token><symbolic token>
\endsyntax
The @delimiters@ command gives new meanings to the two symbolic tokens;
henceforth they will match each other (and only each other). For example,
Appendix B says '@delimiters@ ()'; without this command, parentheses
would be ordinary symbolic tokens. Any distinct symbolic tokens can be
defined to act as delimiters, and many different pairs of delimiters
can be in use simultaneously.
\beginsyntax
<protection command>\is[outer]<symbolic token list>
\alt[inner]<symbolic token list>
\endsyntax
A "" stamp is added to or removed from symbolic tokens
by an @outer@ or @inner@ command, without changing the essential meanings
of those tokens. A token that has been called @outer@ should not appear
when METAFONT\ is skipping over tokens at high speed; the program will stop
and insert an appropriate delimiter, if an @outer@ token is sensed in
the wrong place, since such tokens are supposed to occur only at
"quiet" times. \ (Unquiet times occur when METAFONT\ is skipping tokens
because of a false , or because it is reading the ^replacement
text of a macro or the of a loop, or because it is scanning
the to a macro, or because it is erroneous
tokens that were found at the end of a statement.) \ Without such
protection, a missing right delimiter could cause METAFONT\ to eat up your
whole program before any error was detected; @outer@ tokens keep such
errors localized. An @inner@ command undoes the effect of @outer@; so
does '@let@', and so does any other command or definition that changes the
meaning of a symbolic token. All tokens are initially @inner@.
\beginsyntax
<everyjob command>\is[everyjob]<symbolic token>
\endsyntax
The command '@everyjob@$\,S$' tells METAFONT\ that token $S$ should be inserted
first, just before the input file is read, when a job starts. \ (This
is meaningful only in a base file that will be loaded or preloaded
at the beginning of a run; it is analogous to TeX's '\everyjob' command.)
\beginsyntax
<show command>\is[show]<expression list>
\alt[showvariable]<symbolic token list>
\alt[showtoken]<symbolic token list>
\alt[showdependencies]
\alt[showstats]
\endsyntax
A simple @show@ command displays the value of each expression, in turn.
Paths, pens, and pictures are shown only in the transcript file, unless
^"tracingonline" is positive. The @showvariable@ command gives the
structure of all variables that begin with a given external tag,
together with their values in an abbreviated form; this allows you to see
which of its subscripts and suffixes have occurred. For example, if you're
using plain METAFONT\ conventions, '@showvariable@ $x,y$' will show all
coordinates that have been defined since the last @beginchar@. The @showtoken@
command gives the current meaning of a token, so that you can tell whether
it is primitive or not, @outer@ or not. (If @showvariable@ is applied to
a spark instead of a tag, it gives the same information as @showtoken@.)
\ Every unknown numeric variable that's currently dependent is shown by
@showdependencies@ (except that unknown capsules are shown only
when ^"tracingcapsules" is positive). And finally, @showstats@ gives
information about METAFONT's current memory usage.
Each of these commands will stop and say "!' ', if the internal
quantity "showstopping" has a positive value; this gives you a chance
to enter more @show@ commands ly, while you're trying to
debug a program.
\beginsyntax
<message command>\is<message op><string expression>
<message op>\is[message]\alt[errmessage]\alt[errhelp]
\endsyntax
Communication with the user is possible via @message@, @errmessage@,
and @errhelp@, as discussed in Chapter 22.
\beginsyntax
<mode command>\is[batchmode]\alt[nonstopmode]
\alt[scrollmode]\alt[errorstopmode]
\endsyntax
The four "mode commands" control the amount of interaction during error
recovery, just as in TeX. A job starts in @errorstopmode@, and you can
also resurrect this mode by METAFONT; @scrollmode@,
@nonstopmode@, and @batchmode@ are the modes you get into by hitting
"S'', "R'', or "Q'', respectively, in response to error messages
(cf. Chapter 5).
\beginsyntax
<picture command>\is<addto command>\alt<cull command>
<addto command>\is[addto]<picture variable>[also]<picture expression>
\alt[addto]<picture variable>[contour]<path expression><with list>
\alt[addto]<picture variable>[doublepath]<path expression><with list>
<with list>\is<empty>\alt<with list><with clause>
<with clause>\is[withpen]<pen expression>
\alt[withweight]<numeric expression>
<cull command>\is[cull]<picture variable><keep or drop><pair expression>
\alt<cull command>[withweight]<numeric expression>
<keep or drop>\is[keeping]\alt[dropping]
\endsyntax
The @addto@ and @cull@ commands are the principal means of making
changes to pictures; they are discussed fully in Chapter 13.
\beginsyntax
<display command>\is[display]<picture variable>[inwindow]<window>
<window>\is<numeric expression>
<openwindow command>\is[openwindow]<window><window spec>
<window spec>\is<screen place>[at]<pair expression>
<screen place>\is[from]<screen coordinates>[to]<screen coordinates>
<screen coordinates>\is<pair expression>
\endsyntax
Chapter 23 explains how to display stuff on your screen via @display@
and @openwindow@.
\beginsyntax
<shipout command>\is[shipout]<picture expression>
\endsyntax
You may have wondered how METAFONT\ actually gets pictorial information into
a font. Here at last is the answer: '@shipout@ $v$' puts the pixels of
positive weight, as defined by the picture expression $v$, into a ^generic
font output file, where they will be the bitmap image associated with
character number $"charcode"\bmod256+"charext"\ast256$. The pixels of $v$
are shifted by $("xoffset","yoffset")$ as they are shipped out.
\ (However, no output is done if ^"proofing"$<0$. The values of
^"xoffset", ^"yoffset", ^"charcode", and ^"charext" are first rounded to
integers, if necessary.) \ This command also saves the values of
^"charwd", ^"charht", ^"chardp", ^"charic", ^"chardx", and "chardy"; they
will be associated with the current "charcode" when ^font metric
information is produced. \ (See Appendices F and G for the basic
principles of font metric information and generic font files.)
\beginsyntax
<special command>\is[special]<string expression>
\alt[numspecial]<numeric expression>
\endsyntax
The @special@ and @numspecial@ commands send alphabetic and numeric
information
to the generic font output file, if "proofing" is nonnegative.
For example, the labels on proofsheets are specified in this
way by macros of plain METAFONT\!. Appendices G and H provide further details.

\medbreak
We have now discussed every kind of command but one; and the remaining
one is even more special than the *special command*, so we had better
defer its discussion to an appendix. Appendix F will complete the syntax
by defining *font metric command*. For now, we merely need to know that
font metric commands specify fussy font facts; examples are the kerning and
'@font\_normal\_space@' statements in the METAFONT\ logo program of Chapter 11.

\medbreak
And there's one more loose end to tie up, going back to the very
first syntax rule in this chapter: The token '^@dump@' can be
substituted for '^@end@', if a special version of METAFONT\ called
'' is being used. This writes a file containing the macros
defined so far, together with the current values of variables and
the current meanings of symbolic tokens, so
that they can be loaded as a base file. \ (It is analogous to
TeX's '\dump' command.) \ Base files are discussed at the end of
Appendix B.

**[Double Dangerous Bend]** exercise Run METAFONT\ with the input ^^@outer@ ^^@delimiters@ ^^@showtoken@

"'

\newinternal a;
let b=a; outer a,b,c;
let c=b; delimiters a::;
showtoken a,b,c; end

"'

and explain the computer's responses.

#### Answer
The responses are

"'

> a=left delimiter that matches ::
> b=(outer) a
> c=a

"'

because: $a$ has been redefined from internal quantity to delimiter;
$b$ is still an internal quantity (named $a$), and it has been stamped
@outer@; $c$ denotes the same internal quantity, but it hasn't got outerness.

\endchapter

Our life is frittered away by detail.
An honest man has hardly need
to count more than his ten fingers,
or in extreme cases he may add his ten toes,
and lump the rest. Simplicity, simplicity, simplicity!
I say, let your affairs be as two or three,
and not a hundred or a thousand ...
Simplify, simplify.

> --- HENRY DAVID , *Walden* (1854)

The awesome memory of thy ever attentive computer
accepts all words as .
Think, therefore, in analytical, modular steps,
for the truth or untruth spoken through thy fingertips
will be acted upon unerringly.
or HERMANN , *The Ten Commandments of
Photo-Typesetting* (1982)


# Chapter 27. Recovery from Errors

OK, everything you need to know about METAFONT\ has been explained---unless you
happen to be fallible. If you don't plan to make any errors, don't bother to
read this chapter. Otherwise you might find it helpful to make use of some
of the ways that METAFONT\ tries to pinpoint bugs in your programs.

In the trial runs you did when reading Chapter 5, you learned the general
form of , and you also learned the various ways in which
you can respond to METAFONT's complaints. With practice, you will be able to
correct most errors "online," as soon as METAFONT\ has detected them, by
inserting and deleting a few things. On the other hand, some errors are
more devastating than others; one error might cause some other perfectly
valid construction to be loused up. Furthermore, METAFONT\ doesn't always
diagnose your errors correctly, since the number of ways to misunderstand
the rules is vast; METAFONT\ is a rather simple-minded computer program that
doesn't readily comprehend the human point of view. In fact, there will be times
when you and METAFONT\ disagree about something that you feel makes perfectly
good sense. This chapter tries to help avoid a breakdown in communication
by explaining how to learn METAFONT's reasons for its actions.

Ideally you'll be in a mellow mood when you approach METAFONT\!, and you will
regard any error
messages as amusing puzzles---"Why did the machine do
that?"---rather than as personal insults.
METAFONT\ knows how to issue more than a hundred different sorts of error messages,
and you probably never will encounter all of them, because some types of
mistakes are very hard to make.

Let's go back to the '' example file of Chapter 5, since it
has more to teach us. If you have a better memory than the author, you'll
recall that the first error message was

"'

>> mode.setup
! Isolated expression.
<to be read again>
;
l.1 mode setup;

?

"'

In Chapter 5 we just charged ahead at this point, but it would be more

normal for a mature METAFONT er to think "Shucks, I meant to type
"mode_setup'', but I forgot the underscore. Luckily this didn't cause
any harm; METAFONT\ just found an , '"mode.setup"', which
it will ignore. So let me now insert the correct command, '@mode\_setup@'."

Good thinking; so you type "I mode_setup'', right? Wrong $\ldots$ sorry.
Lots of error messages occur before METAFONT\ has read a in
preparation for another ; the important clue in this case
comes from the two lines

"'

<to be read again>
;

"'

which tell us that the semicolon is still pending. So the correct
response would have been to type "I;' 'mode_setup'' instead. Without
the semicolon, you get what appears at first to be a horrible mess:

"'

! Extra tokens will be flushed.
<to be read again>
warningcheck
mode_setup->warningcheck
:=0;if.unknown.mode:mode=proof;fi...
<insert> mode_setup
|quad
<to be read again>
;
l.1 mode setup;

?

"'

But relax, there's a simple way out. The help message says

'Please insert a now in front of anything that you
don't want me to delete'; all you have to do is type "I;'' and
the net effect will be the same as if you had correctly inserted a semicolon
before 'mode_setup' in the first place.

The moral of this story is: *When you insert a new statement during
error recovery, you frequently need to put a semicolon just ahead of it.*
But if you forget, METAFONT\ gives you another chance.

After proceeding through 'badio' with the interactions suggested in

Chap\-ter 5, we will come again to the error

"'

>> 0.08682thinn+144
! Undefined x coordinate has been replaced by 0.

"'

(This is where the erroneous "thinn'' was detected.) \ The help message for
this error has some curious advice:

"'

(Chapter 27 of The METAFONTbook explains that
you might want to type 'I ???' now.)

"'

Chapter 27? That's us! What happens if we do type "I ???'' now? We get

"'

y4r=-0.9848thinn+259.00049
x4r=-0.08682thinn+144
y4=-0.4924thinn+259.00049
x4l=0.08682thinn+144
! OK.

"'

It is now abundantly clear that "thin'' was misspelled. Plain METAFONT\
defines '' to be a macro that shows all of the current
dependencies between numeric variables and stops with '';
this is useful because a badly typed variable name might have become a
instead of an , in which
case it would be revealed by "???'' but not by the error message.

One more example of online error correction should suffice to make
the general strategy clear. Suppose you accidentally type square brackets
instead of parentheses; the computer will scream:

"'

! A primary expression can't begin with '['.
<inserted text>
0
<to be read again>
[
<*> show round[
1 + sqrt43];
?

"'

(By coincidence, the help message for this particular error also refers to
Chapter 27.) \ When METAFONT\ needs to see an expression, because of the tokens
it has already digested, it will try to insert "0'' in order to keep going.
In this case we can see that zero isn't what we intended; so we type
"7'' to delete the next seven tokens, and the computer comes back with

"'

<*> show round[1 + sqrt43]
;
?

"'

Now "I (1 + sqrt43)'' will insert the correct formula, and the program will
be able to continue happily as if there were no mistake.

### Exercise
Why was "7'' the right number of tokens to delete?

#### Answer
We want to delete

>
ok0ok[ok1ok+oksqrt
ok43ok]

from the sequence of tokens that METAFONT\ is about to read next, in order to
get rid of the right bracket, which we can see is going to be just as
erroneous as the left bracket was. However, there is another way to
proceed (and indeed, this alternative would be preferable to counting
tokens, if the bracketed expression were longer): We could simply

delete 2 tokens, then "I(''. This would produce another error stop,

"'

! Missing ')' has been inserted.
<to be read again>
]
<*> show round[1 + sqrt43]
;
? H
I found no right delimiter to match a left one. So I've
put one in, behind the scenes; this may fix the problem.
|null
?

"'

after which it's easy to delete the "]'' and continue successfully.

**[Dangerous Bend]** exercise If the user hadn't deleted or inserted anything, but had
just plunged ahead, METAFONT\ would have come up with another error:

"'

>> 0
! Extra tokens will be flushed.
<to be read again>
[
<to be read again>
(7.55743)
<to be read again>
]
<*> show round[1 + sqrt43]
;
?

"'

Explain what happened. What should be done next?

#### Answer
METAFONT\ looked ahead, to see if the expression being evaluated
was going to be something like "round 0[1+sqrt43,x]''. But when it
found no comma, it put back several tokens so that they could be
read again. \ (The subexpression '1+sqrt43' had already been evaluated,
so a "" for its value, 7.55743, was inserted among the
tokens to be reread.) \ The expression ended with '0', and 'round 0' was
shown. Then METAFONT\ found extra tokens following the @show@ command; a
semicolon should have come next. To continue, the user should just plunge
ahead recklessly once again, letting METAFONT\ delete those unwanted tokens.

It's wise to remember that the first error in your program may well spawn
spurious "errors" later on, because anomalous commands can inflict
serious injury on METAFONT's ability to cope with the subsequent material.
But most of the time you will find that a single run through the
machine will locate all of the places in which your input conflicts
with METAFONT's rules.

**[Dangerous Bend]** Sometimes an error is so bad that METAFONT\ is forced to quit
prematurely. For example, if you are running in ^@batchmode@ or
^@nonstopmode@, METAFONT\ makes an "" if it needs
input from the terminal; this happens when a necessary file can't
be opened, or when no ^@end@ was found in the input.
Here are some of the messages you might get just before
METAFONT\ gives up the ghost: \enddanger

{

\fatal
Fatal base file error; I'm stymied.

This means that the preloaded base you have specified cannot be used,
because it is corrupted or was prepared for a different version of METAFONT\!.
\fatal
That makes 100 errors; please try again.
METAFONT\ has scrolled past 100 errors since the last statement ended, so
it's probably in an endless .
\fatal
I can't go on meeting you like this.

A previous error has gotten METAFONT\ out of whack. Fix it and try again.
\fatal
This can't happen.

Something is wrong with the METAFONT\ you are using. Complain fiercely.
}

**[Dangerous Bend]** There's also a dreadful message that METAFONT\ issues only with
great reluctance. But it can happen:

"'

METAFONT capacity exceeded, sorry.

"'

This, alas, means that you have tried to stretch METAFONT\ too far. The
message will tell you what part of METAFONT's memory has become overloaded;
one of the following nineteen things will be mentioned:

>
'number of strings'(strings and names of symbolic tokens and files)
'pool size'(the characters in such strings)
'main memory size'(pairs, paths, pens, pictures, token lists,
transforms, etc.)
'hash size'(symbolic token names)
'input stack size'(simultaneous input sources)
'number of internals'(internal quantities)
'rounding table size'(transitions between octants in cycles)
'parameter stack size'(macro parameters)
'buffer size'(characters in lines being read from files)
'text input levels'(@input@ files and error insertions)
'path size'(key points per path)
'move table size'(rows of picture being simultaneously accessed)
'pen polygon size'(pen offsets per octant)
'ligtable size'(accumulated @ligtable@ instructions)
'kern'(distinct kern amounts)
'extensible'(built-up characters)
'headerbyte'(largest @headerbyte@ address)
'fontdimen'(largest @fontdimen@ address)
'independent variables'(distinct numeric variables)

The current amount of memory available will also be shown.

**[Dangerous Bend]** If you have a job that doesn't overflow METAFONT's capacity, yet
you want to see just how closely you have approached the limits,
just set ^"tracingstats" to a positive value before the end of your
job. The log file will then conclude with a report on your actual
usage of the first nine things named above (i.e., the number of strings,
\dots, the buffer size), in that order.
Furthermore, the @showstats@ command can be used to discover the current
string memory and main at any time during a run.
The main memory statistics are broken into two
parts; "490&5950'' means, for example, that 490 words are being used
for "large" things like pens, capsules, and
transforms, while 5950 words are being used for "small" things like
tokens and edges.

**[Dangerous Bend]** What can be done if METAFONT's capacity is exceeded? All of the
above-listed components of the capacity can be increased, except the memory
for kerns and extensible characters, provided
that your computer is large enough; in fact, the space necessary to
increase one component can usually be obtained by decreasing some
other component, without increasing the total size of METAFONT\!.
If you have an especially important application, you may be able
to convince your local system people to provide you with a special
METAFONT\ whose capacities have been hand-tailored to your needs.
But before taking such a drastic step, be sure that you are using
METAFONT\ properly. If you have specified a gigantic picture that has
lots of transitions between black and white pixels, you should
change your approach, because METAFONT\ has to remember every change between
adjacent pixel values in every currently accessible picture.
If you keep saving different pens, you might be wasting memory as
discussed in Chapter 16. If you have built up an enormous macro library,
you should realize that METAFONT\ has to remember all of the replacement texts
that you define; therefore if memory space is in short supply, you should
load only the macros that you need.

**[Dangerous Bend]** Some erroneous METAFONT\ programs will overflow any finite
memory capacity. For example, after "def recurse=(recurse)enddef'', the
use of 'recurse' will immediately bomb out:

"'

! METAFONT capacity exceeded, sorry [input stack size=30].
recurse->(recurse
)
recurse->(recurse
)
recurse->(recurse
)
...

"'

The same sort of error will obviously occur no matter how much you increase
METAFONT's input stack size.

**[Dangerous Bend]** Most implementations of METAFONT\ allow you to the program
in some way. This makes it possible to diagnose the causes of ^infinite
loops, if the machine doesn't stop because of memory limitations.
METAFONT\ switches to ^@errorstopmode@ when interrupted; hence
you have a chance to insert commands into the input: You can abort the
run, or you can ^@show@ or change the current contents of variables,
etc. In such cases you will probably want to "" your diagnostic
commands, for example by typing

"'

I hide(showstopping:=1; alpha:=2; show x)

"'

so that you don't mess up the expression METAFONT\ is currently evaluating.
Interruption can also give you a feeling for where METAFONT\ is spending most
of its time, if you happen to be using an inefficient macro, since random
interrupts will tend to occur in whatever place METAFONT\ visits most often.

**[Dangerous Bend]** METAFONT's second most frustrating error messages are its occasional
claims that you have "" paths. Sometimes a glance at your
output will make it clear that you did indeed specify a path that
crossed over itself, something like a figure-8; but sometimes a path
that looks fine to you will be rejected by the computer. In such
cases you need to decipher METAFONT's octant codes, which look scary at
first although they turn out to be helpful when you get used to them.
For example, let's reconsider 'branch4' of , from
the program in Chapter 14:

"'

branch4=
flex((0,509),(-14,492),(-32,481))
&flex((-32,481),(-42,455),(-62,430))
&flex((-62,430),(-20,450),(42,448))
&flex((42,448),(38,465),(4,493),(0,509))
&cycle;

"'

If the number '450' in the third had been '452' instead,
METAFONT\ would have stopped and told you this:

"'

> 0 SSW WSW 1 2 SSW 3 WSW 4 (WNW NNW) NNE ENE 5 ESE 6 (ENE)
NNE NNW 7 WNW NNW 8 NNE 0 (NNW WNW WSW)
! Strange path (turning number is zero).
<to be read again>
;
<for(4)> ...]shifted(150,50)scaled(w/300);
ENDFOR
l.94 endfor
endchar;
?

"'

The "for(4)'' in the fifth-last line implies that 'branch4' is
at fault, because it says that the ^@for@ loop index is 4;
but the codes like '' are your only clues about why
'branch4' is considered strange. \ (A simpler example appeared
in Chapter 13, which you might want to review now.) \

You probably also have a 'proof' mode diagram:
\displayfig 27a (34mm)
Starting at time 0, and at the point $(0,509)$, the path goes South by
Southwest, then West by Southwest until time 2 (the end of the first flex).
Then it goes 'SSW' again, and 'WSW' again (that's the second flex).
But at time 4, the path makes a sharp turn through the directions
'WNW' and 'NNW', *without moving* (because these octant codes are in
parentheses). Aha! That's where the path was supposed to turn
, through 'SSW' and 'SSE' and 'ESE'; METAFONT\ turned clockwise
because it was the shortest way to go. The path actually makes a little
loop at time 4, between the end of the second flex and the beginning of
the third. Therefore its turning number is indeed zero, and the path is
strange by definition.

**[Dangerous Bend]** exercise At what point do the second and third flexes cross,
in this example?

#### Answer
The little program

"'

path p,q; p=flex((-32,481),(-42,455),(-62,430));
q=flex((-62,430),(-20,452),(42,448));
show p intersectiontimes q, p intersectionpoint q,
angle -direction 2 of p, angle direction 0 of q; end

"'

gives the following results:

"'

>> (1.88403,0.07692)
>> (-59.32149,432.59523)
>> 43.14589
>> 45.47263

"'

(Actually, the paths would also cross if '452' were '451', but
it's such a close call that METAFONT\ doesn't call the path strange;
METAFONT\ prefers to turn when the amount of turn
is close enough to $180^\circ$, even if it's slightly more.)

**[Dangerous Bend]** There are three main ways to avoid problems with strange paths.
One is to stay away from paths that turn so abruptly. Or you can displace the
paths by "epsilon", as in the serif example at the end of Chapter 16.
\ (Displacing by ^"eps" would be even safer.) \ Or you can discipline
yourself to fill all cycles counterclockwise, so that you can set
^"turningcheck"$:=0$; this means that METAFONT\ won't check for
strange paths, but that's OK because tiny little loops won't hurt anything
if you are filling cycles in the correct direction.

**[Double Dangerous Bend]** Sometimes the octant codes of a strange path are shown backwards,
because the system may have tried to reverse the path to get rid of
its strangeness.

Sooner or later---hopefully sooner---you'll get METAFONT\ to process your
whole file without stopping once to complain. But maybe the output
still won't be right; the mere fact that METAFONT\ didn't stop doesn't mean
that you can avoid looking at proofsheets. At this stage it's usually easy to
see how to fix typographic errors by correcting the input; hardcopy proofs
such as those discussed in Appendix H usually clear up obvious mistakes,
especially if you have remembered to label the key points in your constructions.

But your output may contain seemingly inexplicable errors.
If you can't find out what went wrong, try the old trick of simplifying
your program: Remove all the things that do work, until you obtain
the shortest possible input file that fails in the same way as the
original. The shorter the file, the easier it will be for you or somebody
else to pinpoint the problem.

**[Dangerous Bend]** One of the important tricks for shortening a buggy program is to
assign a positive value to ^"tracingspecs", because this will put all the
key points and control points of a problematic path into your log file. \
(See the example at the end of Chapter 24, "before subdivision.") \ If
something is wrong with the treatment of some path, you can copy the
path's description from the log file and use it directly in METAFONT\ input,
thereby avoiding all the complexity of equations that might have been
involved in that path's original creation.

**[Dangerous Bend]** We've just talked about "tracingstats" and "tracingspecs";
METAFONT\ is able to produce lots of other kinds of tracing. For example,
Chapter 22 discusses ^"tracingtitles",
Chapter 18 discusses ^"tracingmacros", Chapter 17 discusses
^"tracingrestores", and Chapter 9 discusses ^"tracingequations".
You can also invoke ^"tracingchoices", which shows all paths before and
after their are chosen according to the rules
in Chapter 14; or ^"tracingpens", which shows the pen polygons that
arise when a future pen becomes a full-fledged @pen@; or ^"tracingoutput",
which shows every picture that's shipped out, using edge-transitions
to represent the pixel values as illustrated in Chapter 13. Each of
these types of tracing is enabled by assigning a positive value to the
corresponding internal quantity; for example, you can simply set
$"tracingpens":=1$ (or ^@interim@ $"tracingpens":=1$)
if you want the data about pens.

**[Dangerous Bend]** If ^"tracingcommands"$=1$, METAFONT\ shows every
just before it is carried out. If $"tracingcommands"=2$, METAFONT\ also shows
every just before it is expanded (except that
macros are separate, they're traced only when $"tracingmacros">0$). And if
$"tracingcommands"=3$, METAFONT\ also shows every
just before it is evaluated. Thus you can get "stream of
consciousness" information about everything METAFONT\ is doing.

**[Dangerous Bend]** can be monitored by setting ^"tracingedges"
$:=1$. For example, if we ask METAFONT\ to draw the Ionian '{\manual\IOO}'
of Chapter 5 at a resolution of 100 pixels per inch (^"lowres" mode
with ^"mag"$=.5$), "tracingedges" will report as follows:\enddanger
\beginlines
'Tracing edges at line 15: (weight 1)'
'(1,5)(1,2)(2,2)(2,1)(3,1)(3,0)(8,0)(8,1)(9,1)(9,2)(10,2)(10,8)(9,8)'
'(9,9)(8,9)(8,10)(3,10)(3,9)(2,9)(2,8)(1,8)(1,5).'

'Tracing edges at line 15: (weight -1)'
'(3,5)(3,2)(4,2)(4,1)(7,1)(7,2)(8,2)(8,8)(7,8)(7,9)(4,9)(4,8)(3,8)(3,5).'
\endlines
By following these edges (and negating their weights on the inner boundary)
we find that the character at this low resolution is symmetric:

>
{\offinterlineskip\manual#
SSSRRRRRSSS
SSRRSSSRRSS
SRRSSSSSRRS
SRRSSSSSRRS
SRRSSSSSRRS
SRRSSSSSRRS
SRRSSSSSRRS
SRRSSSSSRRS
SSRRSSSRRSS
SSSRRRRRSSS}

**[Double Dangerous Bend]** Further information about digitization comes out when
$"tracingedges">1$, if fixed pens are used to ^@draw@ or ^@filldraw@ a
shape. In this case detailed information is presented about the activity
in each direction; straight line "" edges are
also reported whenever METAFONT\ changes from one to another.

**[Double Dangerous Bend]** The "tracing"$\ldots$ commands put all of their output into your log
file, unless the ^"tracingonline" parameter is positive; in the latter
case, all diagnostic information goes to the terminal as well as to the
log file. Plain METAFONT\ has a ^@tracingall@ macro that turns on the
maximum amount of tracing of all kinds. It not only sets up
"tracingcommands", "tracingedges", "tracingspecs", and so on,
it also sets $"tracingonline":=1$, and it sets ^"showstopping"$:=1$ so
that you can do interactive debugging via ^@show@ commands. This is the works.
There's also ^@loggingall@, which is like @tracingall@ except that it
doesn't touch "tracingonline" or "showstopping". You can say ^@interact@
if you want just $"tracingonline":="showstopping":=1$. Finally, there's
^@tracingnone@, which shuts off every form of tracing after you've had enough.

**[Double Dangerous Bend]** Some production versions of METAFONT\ have been streamlined for
speed. These implementations don't look at the value of ^"tracingstats",
nor do you get extra information when $"tracingedges">1$,
because METAFONT\ runs faster when it doesn't have
to maintain statistics or keep tabs on whether tracing is required.
If you want all of METAFONT's diagnostic tools, you should be sure to
use the right version.

**[Double Dangerous Bend]** If you set ^"pausing"$:=1$, METAFONT\ will give you a chance to edit
each line of input as it is read from the file. In this way you can
make temporary patches (e.g., you can insert @show@$\ldots$ commands)
while troubleshooting, without changing the actual contents
of the file, and you can keep METAFONT\ running at human speed.

Final hint: When working on a large font, it's best to prepare
only a few characters at a time. Set up a "test" file and a "master"
file, and do your work in the test file. \ (Appendix E suggests a
convenient way to prepare control files that supply parameters to individual
test characters as well as to the whole font.) \
After the characters come out looking right, you can append them to the
master file; and you can run the master file through METAFONT\ occasionally,
in order to see how the font is shaping up. Characters can always be
moved back to the test file if you have to fix some unexpected problems.

**[Double Dangerous Bend]** exercise Final exercise: Find all of the in this
manual, and all of the .

#### Answer
If this exercise isn't just a joke, the title of this
appendix is a lie. \ (When you've solved this exercise you might also
try to find all the lies and/or jokes that are the same in both
this book and *The TeX book*.)

Final exhortation: GO FORTH now and create
*masterpieces of digital typography!*

\endchapter

With respect to the directions of the route

I may have made some errors.

> --- FRAY PEDRO , *Diary* (1776)

The road to wisdom? Well, it's plain
and simple to express:
\centering to#=0pt
Err
and err
and err again
but less
and less
and less.

> --- PIET , *Grooks* (1966)


# Appendix A. Answers to All the Exercises

The preface to this manual points out the wisdom of trying to figure out
each exercise before you look up the answer here. But these answers are intended
to be read, since they occasionally provide additional information that
you are best equipped to understand when you have just worked on a problem.

\immediate\closeout\ans

\endchapter

Looke into this Businesse thorowly,
And call these foule Offendors to their Answeres.
or WILLIAM ,
*Second Part of Henry the Sixth* (1594)

If you can't solve a problem,
you can always look up the answer.
But please, try first to solve it by yourself;
then you'll learn more and you'll learn faster.
or DONALD E. , *The
{\manual \char'\\]\char'\^\char'\_efg\char'\^*} (1986)


# Appendix B. Basic Operations

This appendix defines the macros of the plain METAFONT\ base. Let's begin

with an informal of all the features that are available.

skip=3pt plus .5pt

\medbreak- *things:* \
'true', 'false'; \ \ \bb'known"unknown"cycle'\ee*expression*;\\
2pt to 7pt
\smash{3pt{'odd' *numeric*; \ \ 'charexists' *numeric*;}}\\
\bb'boolean"numeric"pair"path'
'pen"picture"string"transform'\ee*expression*; \
\bb*boolean**numeric**pair**string**transform*\ee
\bb'<"<="="<>">=">'\ee
\bb*boolean**numeric**pair**string**transform*\ee;\\
3pt
'not' *boolean*; \ *boolean* 'and' *boolean*; \ *boolean* 'or' *boolean*.

\medbreak- *things:* \
'tracingtitles', \dots, 'yoffset' (see Chapter 25);\\
'eps', 'epsilon', 'infinity'; \ 'tolerance', 'join_radius', 'displaying'; \
*constant*;\\
\bb'sqrt"sind"cosd"mlog"mexp'\ee*numeric*; \
\bb'floor"round"hround"vround"ceiling'\ee*numeric*; \
\bb'lft"rt"top"bot"good.x"good.y'\ee*numeric*;\\
\bb'xpart"ypart'\ee\bb*pair**transform*\ee; \
\bb'xxpart"xypart"yxpart"yypart'\ee*transform*; \
\bb'ASCII"oct"hex'\ee*string*;\\
'normaldeviate'; \ 'uniformdeviate' *numeric*; \ 'whatever';\\
6pt
'angle' *pair*; \ 'turningnumber' *cycle*; \ 'totalweight' *picture*;\\
\bb'+''-'*constant*\ee*numeric*; \
\bb'incr"decr'\ee*variable*; \
'byte'\bb*numeric**string*\ee;\\
*numeric*\bb'+"-'\ee*numeric*; \
*numeric*\bb'++"+-+'\ee*numeric*;\\
to24pt
\smash{*numeric*\bb*/**\ee*numeric*}; \
*numeric*\bb'mod"div'\ee*numeric*;\\
*pair* 'dotprod' *pair*; \
\bb'max"min'\ee'('*numerics*')'; \
\bb'abs"length'\ee\bb*numeric**pair**path**string*\ee;\\
*numeric*'['*numeric*','*numeric*']'; \
'solve'*function*'('*numeric*','*numeric*')';\\
'directiontime' *pair* 'of' *path*.

\medbreak- *things:* \
'left', 'right', 'up', 'down', 'origin'; \
'('*numeric*','*numeric*')';\\
'z'*suffix*; \ 'dir' *numeric*; \ 'unitvector' *pair*; \ 'round' *pair*;\\
\bb'lft"rt"top"bot'\ee*pair*; \
\bb'good.lft"good.rt"good.top"good.bot'\ee*pair*; \
\bb'point"precontrol"postcontrol"direction'\ee
*numeric* 'of' *path*;\\
\bb'+''-'*constant*\ee*pair*; \
*pair*\bb'+"-'\ee*pair*; \
*numeric*'['*pair*','*pair*']';\\
*numeric*'*'*pair*; \
*pair*\bb'*"/'\ee*numeric*; \
*pair**transformer*;\\
*path*\bb'intersectionpoint"intersectiontimes'\ee*path*; \
\bb'max"min'\ee'('*pairs*')';\\
3pt
'penoffset' *pair* 'of' *pen*; \
'directionpoint' *pair* 'of' *path*.

\medbreak- *things:* \
'quartercircle', 'halfcircle', 'fullcircle';\\
'unitsquare'; \
'flex('*pairs*')'; \
'makepath' *pen*;\\
'superellipse('*pair*','*pair*','*pair*','*pair*','*numeric*')';\\
'reverse' *path*; \
'counterclockwise' *path*; \
'tensepath' *path*;\\
*path**transformer*; \
'interpath('*numeric*','*path*','*path*')';\\
\bb*pair**path*\ee
\bb''*pair*'"'*curl*''*empty*\ee
\bb'.."..."..'*tension*'.."..'*controls*'..'
'--"---"&"softjoin'\ee
\bb''*pair*'"'*curl*''*empty*\ee
\bb*pair**path*'cycle'\ee;\\
'subpath' *pair* 'of' *path*.

\medbreak- *things:* \
'pencircle', 'pensquare', 'penrazor', 'penspeck';\\
'nullpen'; \ 'currentpen'; \
'makepen' *path*; \
*pen**transformer*.

\medbreak- *things:* \
'nullpicture', 'blankpicture'; \ 'unitpixel';\\
'currentpicture'; \
\bb'+"-'\ee*picture*; \
*picture*\bb'+"-'\ee*picture*;\\
*picture**transformer*.

\medbreak- *things:* \
'"constant"'; \ 'ditto'; \ 'jobname'; \ 'readstring';\\
'str'*suffix*; \
'decimal' *numeric*; \
'char' *numeric*;\\
*string* '&' *string*; \
\bb'max"min'\ee'('*strings*')'; \
'substring' *pair* 'of' *string*.

\medbreak- *things:* \
'identity'; \ 'currenttransform';\\
'inverse' *transform*; \
*transform**transformer*.

skip by 3pt
amount by 3pt
\medbreak- *:* \
'transformed' *transform*;\\
\bb'rotated"slanted'\ee*numeric*; \
\bb'scaled"xscaled"yscaled'\ee*numeric*; \
\bb'shifted"zscaled'\ee*pair*;\\
'reflectedabout('*pair*','*pair*')'; \
'rotatedaround('*pair*','*numeric*')'.

\medbreak- *:*\\
'if' *boolean*': '*text* \bb'elseif'*boolean*': '*text*\ee$$
\bb'else:' *text**empty*\ee'fi'.

break- *:* \ 'forever:' *text* 'endfor';\\
'for' $\nu$ \bb'=":='\ee
\bb*numeric* 'upto' *numeric*
*numeric* 'downto' *numeric*
*numeric*'step'
*numeric*'until'*numeric*\ee
':' *text$(\nu)$* 'endfor';\\
'for' $\epsilon$ \bb'=":='\ee
*expressions*':' *text$(\epsilon)$* 'endfor';\\
'forsuffixes' $\sigma$ \bb'=":='\ee
*suffixes*':' *text$(\sigma)$* 'endfor';\\
'exitif' *boolean*';' ;
'exitunless' *boolean*';' .

\medbreak- *:* \
'???'; \ 'interact'; \
'hide('*statements*')';\\
'loggingall', 'tracingall', 'tracingnone'.

- *:* \
'\mode='*mode name*; \ 'mag='\bb*numeric*'magstep'*numeric*\ee;\\
'screenchars'; \ 'screenstrokes'; \ 'imagerules'; \ 'gfcorners'; \
'nodisplays';\\
'notransforms'; \ 'input' *filename*.

\medbreak- *:* \
'mode_setup'; \ 'fix_units';\\
'pixels_per_inch', 'blacker', 'fillin', 'o_correction';\\
'mm#', 'cm#', 'pt#', 'pc#', 'dd#', 'cc#', 'bp#', 'in#';\\
'mm', 'cm', 'pt', 'pc', 'dd', 'cc', 'bp', 'in';\\
'mode_def'; \ 'extra_setup';\\
\bb'define_pixels'
'define_whole_pixels'
'define_whole_vertical_pixels'
'define_good_x_pixels'
'define_good_y_pixels'
'define_blacker_pixels'
'define_whole_blacker_pixels'
'define_whole_vertical_blacker_pixels'
'define_corrected_pixels'
'define_horizontal_corrected_pixels'
'lowres_fix'\ee'('*names*')'.

skip by-4pt
amount by-4pt
\medbreak- *Character and font administration:*\\
'beginchar('*code*','*width$\0$*','*height$\0$*','*depth$\0$*')'; \ \
'extra_beginchar';\\
'italcorr' *numeric$\0$*; \ 'change_width'; \ 'endchar'; \ \
'extra_endchar';\\
\bb'font_size"font_slant"font_normal_space'
'font_normal_stretch"font_normal_shrink"font_x_height'
'font_quad"font_extra_space'\ee
\bb'='':='*empty*\ee
*numeric$\0$*; \
\bb'ligtable'*ligs/kerns*'charlist'*codes*'extensible'*codes*
'fontdimen'*info*'headerbyte'*info*\ee;\\
\bb'font_identifier"font_coding_scheme'\ee
\smash{\bb=:=*empty*\ee}
*string*.

\medbreak- *:* \
'penpos'*suffix*'('*length*','*angle*')'; \
'penstroke' *path($e$)*;\\
'pickup'\bb*pen**saved pen number*\ee; \
*pen number*':=savepen'; \ 'clear_pen_memory';\\
6pt'pen_lft', 'pen_rt', 'pen_top', 'pen_bot';\\
\bb'fill"unfill"filldraw"unfilldraw'\ee*cycle*; \
\bb'draw"undraw"cutdraw'\ee*path*; \
\bb'drawdot"undrawdot'\ee*pair*;\\
to 10pt'erase' *picture command*; \
'cutoff('*pair*','*angle*')';\\
'addto' *picture variable* 'also' *picture*;\\
'addto' *picture variable*\bb'contour' *cycle*'doublepath' *path*\ee
${\bb'withpen'*pen*'withweight'*numeric*\ee}^
{\smash{3pt{$riptstyle\ge0$}}}\!$;\\
'cull' *picture variable*\bb'keeping"dropping'\ee*pair*
\bb'withweight'*numeric**empty*\ee.

\medbreak- *:* \
'currentwindow'; \
'screen_rows', 'screen_cols';\\
'openwindow' *numeric* 'from' *screen pair* 'to' *screen pair*
'at' *pair*;\\
'display' *picture variable* 'inwindow' *numeric*.

skip by 4pt
amount by 2pt
\medbreak- *:* \
*empty*; \ *string*; \ 'begingroup' *statements* 'endgroup';\\
\bb*boolean**numeric**pair**path*
*pen**picture**string**transform*\ee
${\bb\bb'=":='\ee
\bb*boolean**numeric**pair**path*
*pen**picture**string**transform*\ee\ee}^
{\smash{6pt{$riptstyle\ge1$}}}\!\!$;
\bb'boolean"numeric"pair"path'
'pen"picture"string"transform'\ee*names*;\\
'save' *names*; \
'interim' *internal* ':=' *numeric*; \
'let' *name*\bb'=":='\ee*name*;\\
\bb'def"vardef'\ee*name**parameters*\bb'=":='\ee
*text*'enddef';\\
to24pt\bb'primarydef"secondarydef"tertiarydef'\ee
\ $\alpha$ *name* $\beta$ \bb'=":='\ee
*text$(\alpha,\beta)$*'enddef';\\
'showit'; \ 'shipit'; \ 'cullit'; \ 'openit'; \
'clearit'; \ 'clearxy'; \ 'clearpen';\\
'stop' *string*; \
'show' *expressions*; \
\bb'message"errmessage"errhelp'\ee*string*;\\
\bb'showvariable"showtoken'\ee*names*; \
\bb'showdependencies"showstats'\ee;\\
see also Chapter 26 for some more exotic commands.

skip by -1pt
amount by 1pt
\medbreak- *information:*\\
\bb'labels"penlabels'\ee
\bb'top"lft"rt"bot'*empty*\ee
\bb'nodot'*empty*\ee
'('*suffixes*')';\\
'makelabel'\bb'top"lft"rt"bot'*empty*\ee
\bb'nodot'*empty*\ee
'('*string*','*pair*')'; \
\bb'titlefont"labelfont"grayfont"slantfont'\ee *name*;\\
\bb'proofrule"screenrule'\ee'('*pair*','*pair*')'; \
'makegrid('*numerics*')('*numerics*')';\\
'proofrulethickness' *numeric$\0$*; \ 'proofoffset' *pair*.

\medbreak- *Hacks:* \ 'gobble', 'gobbled', 'killtext'; \
'capsule_def'; \ 'numtok'.

\medbreak

**[Dangerous Bend]** The remainder of this appendix contains an edited transcript
of the "plain ," which is a set of macros that come with
normal implementations of METAFONT\!. These macros serve three basic purposes:
\ (1) They make METAFONT\ usable, because METAFONT's primitive capabilities
operate at a very low level. A "virgin" METAFONT\ system that has no
macros is like a newborn baby that has an immense amount to learn about
the real world; but it is capable of learning fast. \ (2) The plain
METAFONT\ macros provide a basis for more elaborate and powerful bases
tailored to individual tastes and applications. You can do a lot with
plain METAFONT\!, but pretty soon you'll want to do even more. \ (3) The macros
also serve to illustrate how additional bases can be designed. \enddanger

Somewhere in your computer system you should be able to find a file called
that contains what has been preloaded into the
running METAFONT\ system that you use. That file should match the
code discussed below, except that it might do some things in an
equivalent but slightly more efficient manner.

When we come to macros whose use has not yet been explained---for
example, somehow 'softjoin' and 'stop' never made it
into Chapters 1 through 27---we shall consider them from a user's
viewpoint. But most of the comments that follow are addressed to a
potential base-file designer.

A special program called is used to install METAFONT; 'INIMF' is
just like METAFONT\ except that it is able to '^@dump@' a base file
suitable for preloading. This operation requires additional program
space, so 'INIMF' generally has less memory available
than you would expect to find in a production version of METAFONT\!.

## Getting started

A base file has to have a ^@delimiters@
command near the beginning, since 'INIMF' doesn't have any delimiters
built in. The first few lines usually also give the base file a name and
version number as shown here.
\beginlines
|
|
|
'string base_name, base_version; base_name="plain"; base_version="2.71";'

' "Preloading the plain base, version " & base_version;'

|delimiters ();
\endlines

Next we define some of the simplest macros, which provide "syntactic sugar"
for commonly occurring idioms.
For example, '@stop@ '"hello"'' displays "hello'' on the terminal and waits
until *return* is typed.
\beginlines
'def " = step 1 until enddef; def " = step -1 until enddef;'
'def " expr c = exitif not c enddef;'
'let '| = \;
|let \\ = \;
'def '| = ] ] enddef;
'def " = curl 1..curl 1 enddef;'
'def " = .. tension infinity .. enddef;'
'def " = .. tension atleast 1 .. enddef;'

'def " primary g = enddef; def " text t = enddef;'
'primarydef g " gg = enddef;'
'def "(text t) = exitif numeric begingroup t; endgroup; enddef;'
'def " = hide(interim showstopping:=1; showdependencies) enddef;'
'def " expr s = message s; gobble readstring enddef;'
\endlines
(Chapter 20 points out that "\'' is an expandable token that expands
into nothing. Plain METAFONT\ allows also "\\'', because there's a
formatting program called that uses '\\' to insert extra spacing
in a listing.) \ The "clever" code for @hide@
is based on the fact that a expression is not numeric;
hence no loop is exited, ^^@exitif@ and the computer doesn't mind the
fact that we may not be in a loop at all.

The values of are next on the agenda:
\beginlines
':=1; '|:=2;
|:=2;
|:=1;

'def '| =
' hide(showstopping:=1; tracingonline:=1) enddef;'
'def '| =
' tracingcommands:=3; tracingedges:=2; tracingtitles:=1;'
' tracingequations:=1; tracingcapsules:=1; tracingspecs:=1;'
' tracingpens:=1; tracingchoices:=1; tracingstats:=1;'
' tracingoutput:=1; tracingmacros:=1; tracingrestores:=1;'
' enddef;'
'def '| =
' tracingonline:=1; showstopping:=1; loggingall enddef;'
'def '| =
' tracingcommands:=0; tracingonline:=0; showstopping:=0;'
' tracingedges:=0; tracingtitles:=0; tracingequations:=0;'
' tracingcapsules:=0; tracingspecs:=0; tracingpens:=0;'
' tracingchoices:=0; tracingstats:=0; tracingoutput:=0;'
' tracingmacros:=0; tracingrestores:=0; enddef;'
\endlines
The user can say @interact@ in the midst of a statement; but
@loggingall@, @tracingall@, and @tracingnone@ should come
between statements. \ (You don't need a after them,
because they come equipped with their own closing ";''.)

## Math routines

The second major part of 'plain.mf'
contains the definitions of basic constants and mathematical
macros that extend the primitive capabilities of METAFONT's expressions.
\beginlines
|
'newinternal eps,epsilon,infinity;'
| := .00049;
| := 1/256/256;
| := 4095.99998;
break
|
'pair right,left,up,down,origin;'
'=(0,0); "=-"=(0,1); "=-"=(1,0);'
break
|
'path quartercircle,halfcircle,fullcircle,unitsquare;'
'=(rightup..(right+up)/sqrt2..upleft) scaled .5;'
'=quartercircle & quartercircle rotated 90;'
'=halfcircle & halfcircle rotated 180 & cycle;'
'=(0,0)--(1,0)--(1,1)--(0,1)--cycle;'
break
|
'transform identity;'
'for z=origin,right,up: z transformed " = z; endfor'
break
|
'picture blankpicture,unitpixel;'
|=nullpicture;
'=nullpicture; addto unitpixel contour unitsquare;'
break
|
'string ditto; '| = char 34;
break
|
'def capsule_def(suffix s) primary u = def s = u enddef enddef;'
'capsule_def(pensquare) makepen(unitsquare shifted -(.5,.5));'
'capsule_def(penrazor) makepen((-.5,0)--(.5,0)--cycle);'
'pen penspeck; penspeck=pensquare scaled eps;'
\endlines
The ^@pensquare@ and ^@penrazor@ constants are defined here in a
surprisingly roundabout way, just so that they can be
instead of pens. METAFONT\ can transform a future pen much faster than a
pen, since pens have a complex internal data structure, so this
trick saves time. But how does it work? Well, a variable cannot
be a future pen, but a can; hence @pensquare@ and @penrazor@
are defined, via ^@capsule\_def@, to be macros that expand into single capsules.
Incidentally, ^@penspeck@ is an extremely tiny little pen that is used by the
@drawdot@ macro. Since it is not intended to be transformed,
we are better off making it a pen; then it's immediately ready for use.

Now that the basic constants have been defined, we turn to
mathematical operations. There's one operation that has no arguments:
\beginlines
|
'vardef " = save ?; ? enddef;'
\endlines
The reasoning behind this is discussed in exercise 17.\Xwhat.

Operations that take one argument are introduced next.
\beginlines
|
'let " = length;'

'vardef " primary u ='
' if numeric u: floor(u+.5)'
' elseif pair u: (hround xpart u, vround ypart u)'
' else: u fi enddef;'

'vardef " primary x = floor(x+.5) enddef;'
'vardef " primary y = floor(y.o_+.5)_o_ enddef;'

'vardef " primary x = -floor(-x) enddef;'
break
'vardef " primary s = if string s: ASCII fi s enddef;'
break
'vardef " primary d = right rotated d enddef;'

'vardef " primary z = z/abs z enddef;'
break
'vardef " primary T ='
' transform T_; T_ transformed T = identity; T_ enddef;'
break
'vardef " primary c ='
' if turningcheck>0:'
' interim ":=0;'
' if " c <= 0: reverse fi fi c enddef;'
break
'vardef " expr r ='
' for k=0 upto length r - 1: point k of r --- endfor'
' if cycle r: cycle else: point infinity of r fi enddef;'
\endlines
Notice that the variable "T_'' was not saved by the "inverse"
function. The plain base routines gain by
using "" tokens that are assumed to be distinct
from any of the user's tokens; these private tokens always
end with the character, "_''. If ordinary user programs
never contain such token names, no surprises will occur,
provided that different macro designers who combine their routines are
careful that their private names are not in conflict.

The private tokens "o_'' and "_o_'' used in 'vround' stand
for "*aspect_ratio'' and "/aspect_ratio'', respectively,
as we shall see shortly.

Now we define 'mod' and 'div', being careful to do this in such a way that
the identities $a(x\;mod\;y)=(ax)\;mod\;(ay)$ and
$(ax)\;div\;(ay)=x\;div\;y$ are valid.
\beginlines
|
'primarydef x " y = (x-y*floor(x/y)) enddef;'
'primarydef x " y = floor(x/y) enddef;'
'primarydef w " z = (xpart w * xpart z + ypart w * ypart z) enddef;'
\endlines

The "**'' operator is designed to be most efficient when it's used
for squaring. A separate '' routine is used for exponents
other than 2, so that METAFONT\ doesn't have to skip over lots of tokens
in the common case. The 'takepower' routine is careful to give the
correct answer in expressions like "(-2)**(-3)'' and "0**0''.
\beginlines
'primarydef x " y = if y=2: x*x else: takepower y of x fi enddef;'
'def takepower expr y of x ='
' if x>0: mexp(y*mlog x)'
' elseif (x=0) and (y>0): 0'
' else: 1'
' if y=floor y:'
' if y>=0: for n=1 upto y: *x endfor'
' else: for n=-1 downto y: /x endfor fi'
' else: hide(errmessage "Undefined power: " & decimal x&"**"&decimal y)'
' fi fi enddef;'
\endlines

METAFONT's primitive path operations have been defined in such a way that the
following higher-level operations are easy:
\beginlines
'vardef " expr t of p ='
' postcontrol t of p - precontrol t of p enddef;'

'vardef " expr z of p ='
' a_:=" z of p;'
' if a_<0: errmessage("The direction doesn't occur"); fi'
' point a_ of p enddef;'

'secondarydef p " q ='
' begingroup save x_,y_; (x_,y_)=p " q;'
' if x_<0: errmessage("The paths don't intersect"); (0,0)'
' else: .5[point x_ of p, point y_ of q] fi endgroup'
'enddef;'
\weakendlines
The private token "a_'' will be declared as an .
Internal quantities are more than ordinary numeric variables.

Plain METAFONT's '' operation provides a way to hook paths together
without the abrupt change of direction implied by '\&'. Assuming that
the final point of $p$ is the first point of $q$, the path '$p$ softjoin $q$'
begins on $p$ until coming within "join\_radius" of this common point;
then it curves over and finishes $q$ in essentially the same way.
The internal quantity ^"join\_radius" should be set to the desired
value before softjoin is applied. \ (This routine is due to N. N. .)
\beginlines
'tertiarydef p softjoin q ='
' begingroup c_:=" scaled 2join_radius shifted point 0 of q;'
' a_:=ypart(c_ intersectiontimes p); b_:=ypart(c_ intersectiontimes q);'
' if a_<0:point 0 of pdirection 0 of p else: subpath(0,a_) of p fi'
' ... if b_<0:direction infinity of qpoint infinity of q'
' else: subpath(b_,infinity) of q fi endgroup enddef;'
'newinternal join_radius,a_,b_; path c_;'
\endlines

The remaining math operators don't fall into the ordinary patterns; something
is unusual about each of them. First we have "incr'' and "decr'', which apply
only to variables; they have the side effect of changing the variable's value.
\beginlines

'vardef " suffix $ = $:=$+1; $ enddef;'
'vardef " suffix $ = $:=$-1; $ enddef;'
\weakendlines
You can say either "incr' 'x'' or "incr' '(x)'', within
an expression; but neither of them are valid statements by themselves.

To reflect about a line, we compute a on the fly:
\beginlines
'def '|(expr w,z) =
' transformed'
' begingroup transform T_;'
' w transformed T_ = w; z transformed T_ = z;'
| xxpart T_ = -yypart T_; xypart T_ = yxpart T_;
' T_ endgroup enddef;'

'def '|(expr z, d) =
' shifted -z rotated d shifted z enddef;'
'let '| = rotatedaround;
\endlines

Now we come to an interesting trick: The user writes something like
'min$(a,b)$' or 'max$(a,b,c,d)$', and
METAFONT's notation for macro calls makes it easy to separate the first argument
from the rest---assuming that at least two arguments are present.
\beginlines
'vardef '|(expr u)(text t) =
' save u_; setu_ u; for uu = t: if uu>u_: u_:=uu; fi endfor'
' u_ enddef;'

'vardef '|(expr u)(text t) =
' save u_; setu_ u; for uu = t: if uu<u_: u_:=uu; fi endfor'
' u_ enddef;'

'def setu_ primary u ='
' if pair u: pair u_ elseif string u: string u_ fi;'
' u_=u enddef;'
\weakendlines
^^"setu\_" Appendix D discusses some variations on this theme.

The routine defines part of a path whose directions at the
endpoints will depend on the environment, because this path is not
enclosed in parentheses.
\beginlines
|def flex(text t) =
' hide(n_:=0; for z=t: z_[incr n_]:=z; endfor'
' dz_:=z_[n_]-z_1)'
' z_1 for k=2 upto n_-1: ...z_[k]{dz_} endfor ...z_[n_] enddef;'
'newinternal n_; pair z_[],dz_;'
\endlines

The five parameters to "superellipse" are the right, the top, the left,
the bottom, and the superness.
\beginlines
'def "(expr r,t,l,b,s)='
' rup...(s[xpart t,xpart r],s[ypart r,ypart t])t-r...'
' tleft...(s[xpart t,xpart l],s[ypart l,ypart t])l-t...'
' ldown...(s[xpart b,xpart l],s[ypart l,ypart b])b-l...'
' bright...(s[xpart b,xpart r],s[ypart r,ypart b])r-b...cycle enddef;'
\endlines

Chapter 14 illustrates the "interpath" routine, which interpolates
between paths to find a path that would be written '$a[p,q]$' if
METAFONT's macro notation were more general.
\beginlines
'vardef "(expr a,p,q) ='
' for t=0 upto length p-1: a[point t of p, point t of q]'
' ..controls a[postcontrol t of p, postcontrol t of q]'
' and a[precontrol t+1 of p, precontrol t+1 of q] .. endfor'
' if cycle p: cycle'
' else: a[point infinity of p, point infinity of q] fi enddef;'
\endlines

Finally we come to the "solve" macro, which has already been presented
in Chapter 20. Appendix D gives further illustrations of its use.
\beginlines
'vardef '|@#(expr true_x,false_x)=
' tx_:=true_x; fx_:=false_x;'
' forever: x_:=.5[tx_,fx_]; exitif abs(tx_-fx_)<=tolerance;'
' if @#(x_): tx_ else: fx_ fi :=x_; endfor'
| x_ enddef;
'newinternal ", tx_,fx_,x_; tolerance:=.1;'

## Conversion to pixels

The next main subdivision of 'plain.mf'
contains macros and constants that help convert dimensions from
device-independent "sharped" or "true" units into the pixel units
corresponding to a particular device. First comes a subroutine that
computes eight basic units, assuming that the number
^^@fix\_units@
of ^"pixels\_per\_inch" is known:
\beginlines
|def fix_units =
' mm:=pixels_per_inch/25.4; cm:=pixels_per_inch/2.54;'
' pt:=pixels_per_inch/72.27; pc:=pixels_per_inch/6.0225;'
' dd:=1238/1157pt; cc:=12dd;'
' bp:=pixels_per_inch/72; in:=pixels_per_inch;'
| hppp:=pt;
| vppp:=aspect_ratio*hppp;
' enddef;'
\endlines

are actually expressed in terms of points, but a virtuous
user will not write programs that exploit this fact.
\beginlines
'mm#=2.84528; pt#=1; dd#=1.07001; bp#=1.00375;'
'cm#=28.45276; pc#=12; cc#=12.84010; in#=72.27;'
\endlines

A particular device is supposed to be modeled by four parameters, called
^"pixels\_per\_inch", ^"blacker", ^"o\_correction", and ^"fillin", as discussed
in Chapter 11. Appropriate
values will be assigned to these internal quantities by @mode\_setup@.
\beginlines
|newinternal pixels_per_inch;
|newinternal blacker, o_correction;
\endlines
(The fourth parameter, "fillin", is already an internal quantity of METAFONT\!.)

Here are the ten principal ways to convert from
sharped units to pixels:
\beginlines
'def define_pixels(text t) ='
' forsuffixes $=t: $:=$.#*hppp; endfor enddef;'
'def define_whole_pixels(text t) ='
' forsuffixes $=t: $:=hround($.#*hppp); endfor enddef;'
'def define_whole_vertical_pixels(text t) ='
' forsuffixes $=t: $:=vround($.#*hppp); endfor enddef;'
'def define_good_x_pixels(text t) ='
' forsuffixes $=t: $:=good.x($.#*hppp); endfor enddef;'
'def define_good_y_pixels(text t) ='
' forsuffixes $=t: $:=good.y($.#*hppp); endfor enddef;'
'def define_blacker_pixels(text t) ='
' forsuffixes $=t: $:=$.#*hppp+blacker; endfor enddef;'
'def define_whole_blacker_pixels(text t) ='
' forsuffixes $=t: $:=hround($.#*hppp+blacker);'
' if $<=0: $:=1; fi endfor enddef;'
'def define_whole_vertical_blacker_pixels(text t) ='
' forsuffixes $=t: $:=vround($.#*hppp+blacker);'
' if $<=0: $:=1_o_; fi endfor enddef;'
'def define_corrected_pixels(text t) ='
' forsuffixes $=t: $:=vround($.#*hppp*o_correction)+eps; endfor enddef;'
'def define_horizontal_corrected_pixels(text t) ='
' forsuffixes $=t: $:=hround($.#*hppp*o_correction)+eps; endfor enddef;'
\endlines

Chapter 24 discusses the ^@lowres\_fix@ routine, which helps to correct
anomalies that may have occurred when sharped dimensions were rounded
to whole pixels.
\beginlines
'def lowres_fix(text t) expr ratio ='
' begingroup save min,max,first;'
' forsuffixes $=t:'
' if unknown min: min=max=first=$; min#=max#=$.#;'
' elseif $.#<min#: min:=$; min#:=$.#;'
' elseif $.#>max#: max:=$; max#:=$.#; fi endfor'
' if max/min>ratio*max#/min#: forsuffixes $=t: $:=first; endfor fi'
' endgroup enddef;'

## Modes of operation

The standard way to create a font with
plain METAFONT\ is to start up the program by saying

>
'\mode='*mode name*'; mag='*magnification*'; input '
*font file name*

in response to METAFONT's initial ''.
The is omitted if the magnification is 1, and the is omitted
if 'mode=proof'. Additional commands like "screenchars'' might be
given before the ''; we shall discuss them later. If you are
using another base file, called say the "super'' base, this whole
command line should be preceded by "&super''. The mode name should have
been predeclared in your base file, by the 'mode_def' routine below.
If, however, you need a special mode that isn't in the base, you can put
its commands into a file (e.g., "specmode.mf'') and invoke it
by saying

>
'="specmode"; mag='*magnification*'; input '
*font file name*

instead of giving a predeclared mode name.

Here is the ^@mode\_setup@ routine,
which is usually one of the first macros to be called in a METAFONT\ program:
\beginlines
'def mode_setup ='
' warningcheck:=0;'
' if unknown mode: mode=proof; fi'
' numeric aspect_ratio; transform currenttransform;'
' scantokens if string mode:("input "&mode) else: mode_name[mode] fi;'
' if unknown mag: mag=1; fi'
' if unknown aspect_ratio: aspect_ratio=1; fi'
' displaying:=proofing;'
' pixels_per_inch:=pixels_per_inch*mag;'
' if aspect_ratio=1: let o_=\; let _o_=\'
' else: def o_=*aspect_ratio enddef; def _o_=/aspect_ratio enddef fi;'
' fix_units;'
| scantokens extra_setup;
' currenttransform:='
' if unknown currenttransform: identity else: currenttransform fi'
' yscaled aspect_ratio;'
' clearit;'
' pickup pencircle scaled (.4pt+blacker);'
' warningcheck:=1; enddef;'
'def " = string mode; mode enddef;'
'string extra_setup, mode_name[];'
|extra_setup="";
'newinternal '|;
\endlines
^^"extra\_setup" ^^"mode\_name"
The first '^@scantokens@' in @mode\_setup@ either reads a special
file or calls a macro that expands into commands defining the mode.
Notice that "aspect\_ratio" is always cleared to an undefined value
when these commands are performed; you can't simply give a value to
"aspect\_ratio" when you set "mode" and "mag". If the aspect ratio
isn't assigned a definite value by the mode routine, it will become unity,
and the "o_'' and "_o_'' operations will be omitted from subsequent
calculations. Notice also that the mode commands might do something special
to "mag", since "mag" isn't examined until after the mode routine has
acted. The "currenttransform" might also be given a special value. METAFONT's
^"warningcheck" is temporarily disabled during these computations, since
there might be more than 4096 pixels per inch. After @mode\_setup@ is
finished, the "currentpicture" will be null, the "currenttransform"
will take the "aspect\_ratio" into account, and the "currentpen" will be a
circular nib with the standard default thickness of $0.4\pt$. \ (You should
save this pen if you want to use it in a character, because @beginchar@
will clear it away.)

Plain TeX\ has a convention for magnifying fonts in terms of "magsteps,"
where magstep $m=1.2^m$. A geometric progression of font sizes is
convenient, because scaling by magstep $m$ followed by magstep $n$ is
equivalent to scaling by magstep $m+n$.
\beginlines
'vardef " primary m = mexp(46.67432m) enddef;'
\endlines

When a mode is defined (e.g., "proof''), a numeric variable of that
name is created and assigned a unique number (e.g., 1). Then an
character is appended, and a macro is defined for the
resulting name (e.g., "proof_''). The "mode\_name" array is used to
convert between number and name (e.g., "mode\_name"$_1=$'"proof_"').
\beginlines
'def mode_def suffix $ ='
' $:=incr number_of_modes;'
' mode_name[$]:=str$ & "_";'
' " " def scantokens mode_name[$] enddef;'
'newinternal number_of_modes;'
\endlines
(This ^@mode\_def@ strategy was suggested by Bruce .)

Three basic modes are now defined, starting with two for proofing:
\beginlines
|
'mode_def " ='
| proofing:=2;
| fontmaking:=0;
| tracingtitles:=1;
| pixels_per_inch:=2601.72;
| blacker:=0;
| fillin:=0;
| o_correction:=1;
' enddef;'
break
|
'mode_def " ='
| proof_;
| proofing:=1;
| extra_setup:=extra_setup&"grayfont black";
| let makebox=maketicks;
' enddef;'
\weakendlines
Notice that "smoke" mode saves a lot of fuss by calling on "proof_'';
this is the macro that was defined by the first @mode\_def@.

A typical mode for font generation appears next. ^^"fontmaking"
\beginlines
|
'mode_def " ='
| proofing:=0;
| fontmaking:=1;
| tracingtitles:=0;
| pixels_per_inch:=200;
| blacker:=.65;
| fillin:=.2;
| o_correction:=.4;
' enddef;'

|localfont:=lowres;
\endlines
Installations of METAFONT\ typically have several more predefined modes, and they
generally set "localfont" to something else. Such alterations should
not be made in the master file 'plain.mf'; they should appear in a separate
file, as discussed below.

## Drawing and filling

Now we come to the macros that provide
an interface between the user and METAFONT's primitive picture commands.
^^"currentpen" ^^"currentpicture" ^^"currenttransform"
First, some important program variables are introduced:
\beginlines
'pen currentpen;'
'path currentpen_path;'
'picture currentpicture;'
'transform currenttransform;'
'def t_ = transformed currenttransform enddef;'
\endlines

The key macros are ^@fill@, ^@draw@, ^@filldraw@, and ^@drawdot@.
\beginlines
'def fill expr c = addto_currentpicture contour c.t_ enddef;'
'def addto_currentpicture = addto currentpicture enddef;'
'def draw expr p ='
' addto_currentpicture doublepath p.t_ withpen currentpen enddef;'
'def filldraw expr c = fill counterclockwise c withpen currentpen enddef;'
'def drawdot expr z = if unknown currentpen_path: def_pen_path_ fi'
' addto_currentpicture contour'
' currentpen_path shifted (z.t_) withpen penspeck enddef;'
'def def_pen_path_ ='
' hide(currentpen_path=tensepath makepath currentpen) enddef;'
\endlines

And they have negative counterparts:
\beginlines
'def " expr c = fill c withweight -1 enddef;'
'def " expr p = draw p withweight -1 enddef;'
'def " expr c = filldraw c withweight -1 enddef;'
'def " expr z = drawdot z withweight -1 enddef;'
'def " text t = begingroup interim default_wt_:=-1;'
' cullit; t withweight -1; cullit; endgroup enddef;'
'newinternal default_wt_; default_wt_:=1;'
\endlines

It's more difficult to cut off the ends of a stroke, but the
following macros (discussed near the end of Chapter 16) do the job:
\beginlines
'def '| expr p =
' cutoff(point 0 of p, 180+angle direction 0 of p);'
' cutoff(point infinity of p, angle direction infinity of p);'
' culldraw p enddef;'
break
'def " expr p = addto pic_ doublepath p.t_ withpen currentpen;'
' cull pic_ dropping(-infinity,0) withweight default_wt_;'
' addto_currentpicture also pic_; pic_:=nullpicture; killtext enddef;'
'vardef "(expr z,theta) ='
' interim autorounding := 0; interim smoothing := 0;'
' addto pic_ doublepath z.t_ withpen currentpen;'
' addto pic_ contour'
' (cut_ scaled (1+max(-pen_lft,pen_rt,pen_top,-pen_bot))'
' rotated theta shifted z)t_;'
' cull pic_ keeping (2,2) withweight -default_wt_;'
' addto currentpicture also pic_; pic_:=nullpicture enddef;'
'picture pic_; pic_:=nullpicture;'
'path cut_; cut_ = ((0,-1)--(1,-1)--(1,1)--(0,1)--cycle) scaled 1.42;'
\weakendlines
The use of ^"default\_wt\_" here makes '^@erase@ @cutdraw@' work. The
private variable "pic\_" is usually kept equal to @nullpicture@ in
order to conserve memory space.

Picking up a pen not only sets "currentpen", it also establishes
the values of ^"pen\_lft", ^"pen\_rt", ^"pen\_top", and ^"pen\_bot",
which are used by "lft", "rt", "top", and "bot".
\beginlines
'def " secondary q ='
' if numeric q: numeric_pickup_ else: pen_pickup_ fi q enddef;'
'def numeric_pickup_ primary q ='
' if unknown pen_[q]: errmessage "Unknown pen"; clearpen'
' else: currentpen:=pen_[q];'
' pen_lft:=pen_lft_[q]; pen_rt:=pen_rt_[q];'
' pen_top:=pen_top_[q]; pen_bot:=pen_bot_[q];'
' currentpen_path:=pen_path_[q] fi; enddef;'
'def pen_pickup_ primary q ='
' currentpen:=q yscaled aspect_ratio;'
' pen_lft:=xpart penoffset down of currentpen;'
' pen_rt:=xpart penoffset up of currentpen;'
' pen_top:=(ypart penoffset left of currentpen)_o_;'
' pen_bot:=(ypart penoffset right of currentpen)_o_;'
' path currentpen_path; enddef;'
'newinternal pen_lft,pen_rt,pen_top,pen_bot,pen_count_;'
\endlines
And saving a pen saves all the relevant values for later retrieval.
\beginlines
'vardef " = pen_[incr pen_count_]=currentpen;'
' pen_lft_[pen_count_]=pen_lft;'
' pen_rt_[pen_count_]=pen_rt;'
' pen_top_[pen_count_]=pen_top;'
' pen_bot_[pen_count_]=pen_bot;'
' pen_path_[pen_count_]=currentpen_path;'
' pen_count_ enddef;'
break
'def " = currentpen:=nullpen;'
' pen_lft:=pen_rt:=pen_top:=pen_bot:=0;'
' path currentpen_path; enddef;'
break
'def clear_pen_memory ='^^@clear\_pen\_memory@
' pen_count_:=0;'
' numeric pen_lft_[],pen_rt_[],pen_top_[],pen_bot_[];'
' pen currentpen,pen_[];'
' path currentpen_path, pen_path_[];'
' enddef;'
\endlines

The four basic pen-edge functions offer no surprises:
^^"lft"^^"rt"^^"top"^^"bot"
\beginlines
'vardef lft primary x = x + if pair x: (pen_lft,0) else: pen_lft fi enddef;'
'vardef rt primary x = x + if pair x: (pen_rt,0) else: pen_rt fi enddef;'
'vardef top primary y = y + if pair y: (0,pen_top) else: pen_top fi enddef;'
'vardef bot primary y = y + if pair y: (0,pen_bot) else: pen_bot fi enddef;'
\endlines
There are six functions that to good positions for pen placement.
\beginlines
'vardef " primary x = hround(x+pen_lft)-pen_lft enddef;'
'vardef " primary y = vround(y+pen_top)-pen_top enddef;'
'vardef " primary z = save z_; pair z_;'
' (z_+(pen_lft,0))t_=round((z+(pen_lft,0))t_); z_ enddef;'
'vardef " primary z = save z_; pair z_;'
' (z_+(pen_rt,0))t_=round((z+(pen_rt,0))t_); z_ enddef;'
'vardef " primary z = save z_; pair z_;'
' (z_+(0,pen_top))t_=round((z+(0,pen_top))t_); z_ enddef;'
'vardef " primary z = save z_; pair z_;'
' (z_+(0,pen_bot))t_=round((z+(0,pen_bot))t_); z_ enddef;'
\endlines

So much for fixed pens. When pen-like strokes are defined by
outlines, the ^"penpos" macro is of primary importance. Since "penpos"
may be used quite frequently, we might as well write out the $x$ and $y$
coordinates explicitly instead of using the (somewhat slower) $z$ convention:
\beginlines
'vardef penpos@#(expr b,d) ='
' (x@#r-x@#l,y@#r-y@#l)=(b,0) rotated d;'
' x@#=.5(x@#l+x@#r); y@#=.5(y@#l+y@#r) enddef;'
\endlines

Simulated pen strokes are provided by the convenient ^@penstroke@ command.
\beginlines
'def penstroke text t ='
' forsuffixes e = l,r: path_.e:=t; endfor'
' if cycle path_.l: cyclestroke_'
' else: fill path_.l -- reverse path_.r -- cycle fi enddef;'
'def cyclestroke_ ='
' begingroup interim turningcheck:=0;'
' addto pic_ contour path_.l.t_ withweight 1;'
' addto pic_ contour path_.r.t_ withweight -1;'
' cull pic_ dropping origin withweight default_wt_;'
' addto_currentpicture also pic_;'
' pic_:=nullpicture endgroup enddef;'
'path path_.l,path_.r;'

## Proof labels and rules

The next main section of 'plain.mf'
is devoted to macros for the annotations on proofsheets. These macros
are discussed in Appendix H, and they use the ^@special@ and ^@numspecial@
commands discussed in Appendix G.

Labels are generated at the lowest level by @makelabel@:^^"lcode\_"
\beginlines
'vardef '|@#(expr s,z) =
' if known z: special lcode_@# & s;'
' numspecial xpart(z.t_); numspecial ypart(z.t_) fi enddef;'

'string lcode_,lcode_.top,lcode_.lft,lcode_.rt,lcode_.bot,'
' lcode_.top.nodot,lcode_.lft.nodot,lcode_.rt.nodot,lcode_.bot.nodot;'
'lcode_.top=" 1"; lcode_.lft=" 2"; lcode_.rt=" 3"; lcode_.bot=" 4";'
|lcode_=" 0";
'lcode_.top.nodot=" 5"; lcode_.lft.nodot=" 6";'
'lcode_.rt.nodot=" 7"; lcode_.bot.nodot=" 8";'
\endlines

Users generally don't invoke @makelabel@ directly, because there's a convenient
shorthand. For example, '@labels@$(1,2,3)$' expands into
'@makelabel@('"1"'$,z_1$); @makelabel@('"2"'$,z_2$);
@makelabel@('"3"'$,z_3$)'.
\ (But nothing happens if ^"proofing"$\le1$.)
\beginlines
'vardef "@#(text t) ='
' if proofing>1: forsuffixes $=t: makelabel@#(str$,z$); endfor fi enddef;'
'vardef "@#(text t) ='
' if proofing>1: forsuffixes $$=l,,r: forsuffixes $=t:'
' makelabel@#(str$.$$,z$.$$); endfor endfor fi enddef;'
\endlines
When there are lots of purely numeric labels, you can say, e.g.,

>
@labels@(1, @range@ 5 @thru@ 9, @range@ 100 @thru@ 124, 223)

which is equivalent to '@labels@$(1,5,6,7,8,9,100,101,\ldots,124,223)$'.
Labels are omitted from the proofsheets if the corresponding $z$ value
isn't known, so it doesn't hurt (much) to include unused subscript numbers
in a range.
\beginlines
'def " expr x = numtok[x] enddef;'
'def " suffix x=x enddef;'
'tertiarydef m " n ='
' m for x=m+1 step 1 until n: , numtok[x] endfor enddef;'
\weakendlines
(This @range@ abbreviation will work in any ^@forsuffixes@ list;
and in a '@for@' list you can even omit the word '@range@'.
But you might fill up METAFONT's main memory if too many values are involved.)

A straight line will be drawn on the proofsheet by @proofrule@.
Although @makelabel@ takes the current transform into account,
@proofrule@ does not. There's also a corresponding routine '@screenrule@'
that puts a straight line in the current picture, so that design
guidelines will be visible on your screen:
\beginlines
'def "(expr w,z) ='
' special "rule"; numspecial xpart w; numspecial ypart w;'
' numspecial xpart z; numspecial ypart z enddef;'
'def "(expr w,z) ='
' addto currentpicture doublepath w--z withpen rulepen enddef;'
'pen rulepen; rulepen = pensquare scaled 2;'
\endlines
(The ^"rulepen" is two pixels wide, because screen rules are usually
drawn exactly over raster lines. A two-pixel-wide pen straddles the pixel
edges so that you can "see" the correct line position. If
a two-pixel-wide line proves to be too dark, you can redefine
"rulepen" to be simply ^@pensquare@; then METAFONT\ will draw the
thinnest possible screen rule, but it will be
a half-pixel too high and a half-pixel too far to the right.)

You can produce lots of proof rules with ^@makegrid@, which connects
an arbitrary list of $x$ coordinates with an arbitrary list
of $y$ coordinates:
\beginlines
'def makegrid(text xlist,ylist) ='
' xmin_ := min(xlist); xmax_ := max(xlist);'
' ymin_ := min(ylist); ymax_ := max(ylist);'
' for x=xlist: proofrule((x,ymin_), (x,ymax_)); endfor'
' for y=ylist: proofrule((xmin_,y), (xmax_,y)); endfor'
' enddef;'
\endlines

Finally we have a few macros that allow further communication with
the hardcopy proof-drawing routine of Appendix H. You can change the
fonts, the thickness of proof rules, and the position of the image
on its page.
\beginlines
'vardef " suffix $ = special "titlefont "&str$ enddef;'
'vardef " suffix $ = special "labelfont "&str$ enddef;'
'vardef " suffix $ = special "grayfont "&str$ enddef;'
'vardef " suffix $ = special "slantfont "&str$ enddef;'
'def '| primary z =
' special "offset"; numspecial xpart z; numspecial ypart z enddef;'
'vardef " expr x ='
' special "rulethickness"; numspecial x enddef;'

## Character and font administration

After this elaborate preparation, we're finally ready
to consider the @beginchar@$\,\ldots\,$@endchar@
framework for the individual characters of a font. Each ^@beginchar@ begins
a group, which should end at the next ^@endchar@. Then @beginchar@
stores the given character code and device-independent
box dimensions in METAFONT's internal variables ^"charcode", ^"charwd",
^"charht", and ^"chardp". Then it computes the device-dependent box
dimensions , , and . Finally it
clears the $z$ variables, the current picture, and the
current pen.
\beginlines
'def beginchar(expr c,w_sharp,h_sharp,d_sharp) ='
' begingroup'
' charcode:=if known c: byte c else: 0 fi;'
' charwd:=w_sharp; charht:=h_sharp; chardp:=d_sharp;'
' w:=hround(charwd*hppp); h:=vround(charht*hppp); d:=vround(chardp*hppp);'
' charic:=0; clearxy; clearit; clearpen; scantokens extra_beginchar;'
' enddef;'
\endlines
The is normally zero, unless the user gives an
'^@italcorr@' command; even then, the correction stays zero unless
the given value is positive:
\beginlines
'def italcorr expr x_sharp = if x_sharp>0: charic:=x_sharp fi enddef;'
\endlines
When we want to change the pixel width $w$ from even to odd or vice
versa, the ^@change\_width@ macro does the right thing.
\beginlines
'def change_width ='
' w:=w if w>charwd*hppp:- else:+ fi 1 enddef;'
\endlines
(The user might also decide to change $w$ in some other way.) \ The
current value of $w$ at the time of @endchar@ will be the
"official" pixel width of the character, ^"chardx", that is
shipped to the 'gf' output file.
\beginlines
'def endchar ='
' scantokens extra_endchar;'
' if proofing>0: makebox(proofrule); fi'
| chardx:=w;
' shipit;'
' if displaying>0: makebox(screenrule); showit; fi'
' endgroup enddef;'
\endlines
Extensions to these routines can be provided by putting commands in the
string variables ^"extra\_beginchar" and ^"extra\_endchar".
\beginlines
'string extra_beginchar, extra_endchar;'
'extra_beginchar=extra_endchar="";'
\endlines

A "" that surrounds the character according to the
specifications given in @beginchar@ is produced by ^@makebox@, which
takes into account the possibility that pixels might not be square.
An extra line is drawn to mark the width of the character with its
included, if this correction is nonzero.
\beginlines
'def makebox(text r) ='
| for y=0,h.o_,-d.o_: r((0,y),(w,y)); endfor
| for x=0,w: r((x,-d.o_),(x,h.o_)); endfor
' if charic<>0: r((w+charic*hppp,h.o_),(w+charic*hppp,.5h.o_)); fi'
' enddef;'
\endlines

The ^@maketicks@ routine is an alternative to @makebox@ that draws less
conspicuous lines. This makes it easier to visualize a character's
appearance near the edges of its bounding box.
\beginlines
'def maketicks(text r) ='
' for y=0,h.o_,-d.o_: r((0,y),(10,y)); r((w-10,y),(w,y)); endfor'
' for x=0,w: r((x,10-d.o_),(x,-d.o_)); r((x,h.o_-10),(x,h.o_)); endfor'
' if charic<>0: r((w+charic*hppp,h.o_-10),(w+charic*hppp,h.o_)); fi'
' enddef;'
\endlines

Overall information about the font as a whole is generally supplied
^^@font\_size\_etc@
by the following commands, which are explained in Appendix F.
\beginlines
'def font_size expr x = designsize:=x enddef;'
'def font_slant expr x = fontdimen 1: x enddef;'
'def font_normal_space expr x = fontdimen 2: x enddef;'
'def font_normal_stretch expr x = fontdimen 3: x enddef;'
'def font_normal_shrink expr x = fontdimen 4: x enddef;'
'def font_x_height expr x = fontdimen 5: x enddef;'
'def font_quad expr x = fontdimen 6: x enddef;'
'def font_extra_space expr x = fontdimen 7: x enddef;'

'def font_identifier expr x = font_identifier_:=x enddef;'
'def font_coding_scheme expr x = font_coding_scheme_:=x enddef;'
'string font_identifier_, font_coding_scheme_;'
'font_identifier_=font_coding_scheme_="UNSPECIFIED";'

## The endgame

What have we left out? A few miscellaneous
things still need to be handled. First, we almost forgot to define the
^"z" convention for points:
\beginlines
'vardef z@#=(x@#,y@#) enddef;'
\endlines
Then we need to do something rudimentary about METAFONT's "windows."
^^"screen\_rows" ^^"screen\_cols"
\beginlines
'newinternal screen_rows, screen_cols, currentwindow;'
|screen_rows:=400;
|screen_cols:=500;

'def '| = openwindow currentwindow from origen
| to (screen_rows,screen_cols) at (-50,300) enddef;
'def showit_ = display currentpicture inwindow currentwindow enddef;'
'def '| = openit; let showit=showit_; showit enddef;
\endlines
Plain METAFONT\ has several other terse commands similar to '@openit@' and '@showit@':
\beginlines
'def " = save x,y enddef;'
'def " = currentpicture:=nullpicture enddef;'
'def " = shipout currentpicture enddef;'
'def " = cull currentpicture dropping (-infinity,0) enddef;'
\endlines

\medbreak
The next several macros are handy things to put on your
when you are starting a METAFONT\ job (i.e., just before "input' \<font file
name>'):

- 'screenchars'. Say this when you're making a font
but want the characters to be displayed just before they are shipped out.
- 'screenstrokes'. Say this when you're in "proof" mode
and want to see each stroke as it's added to the current picture.
- 'imagerules'. Say this when you want to include the bounding box
in the current character, before you begin to draw it.
- 'gfcorners'. Say this when you expect to make proofsheets
with large pixels, from a low-resolution font.
- 'nodisplays'. Say this to save computer time when you don't
want "proof" mode to display each character automatically.
- 'notransforms'. Say this to save computer time when you know
that the current transform is the identity.
\beginlines
'def '| =
' extra_endchar:=extra_endchar&"showit;" enddef;'

'def '| =
' def addto_currentpicture text t='
' addto currentpicture t; showit enddef; enddef;'
break
'def '| =
' extra_beginchar:=extra_beginchar & "makebox(screenrule);" enddef;'
break
'def '| =
' extra_setup:=extra_setup & "let makebox=maketicks;proofing:=1;" enddef;'
break
'def '| =
' extra_setup:=extra_setup & "displaying:=0;" enddef;'

'def '| =
' let t_ = \ enddef;'
\endlines

We make '^@bye@' synonymous with '^@end@', just in case TeX\ users expect
METAFONT\ programs to end like TeX\ documents do.
\beginlines
'let bye = end; outer end,bye;'
\endlines

And finally, we provide the default environment that a user gets when
^^@clear\_pen\_memory@ ^^@mode\_setup@
simple experiments like those at the beginning of Chapter 5 are desired.
\beginlines
|clear_pen_memory;
|mode_setup;
'numeric ",'|;
\weakendlines
Whew! That's the end of the 'plain.mf' file.

## Adapting to local conditions

In order to make plain METAFONT\
programs interchangeable between different computers, everybody should use
the same 'plain.mf' base. But there are some things that clearly should
be customized at each installation:

- Additional modes should be defined, so that fonts
can be made for whatever output devices are of interest.

- The proper ^"localfont" mode should be established.

- The correct numbers should be assigned to
^"screen\_rows" and ^"screen\_cols".

break

Here's an example of a supplementary file "local.mf''
that would be appropriate for a computer center with the
hypothetical "cheapo" and "luxo" printers described in Chapter 11.
We assume that "cheapo" mode is to be identical to "lowres" mode,
except that the "cheapo" fonts should be generated with a *negative*
value of ^"fillin" (because "cheapo" tends to make diagonal lines lighter
than normal, not heavier). The terminal screens are assumed to be
768 pixels wide and 512 pixels high.
\beginlines
|
'base_version:=base_version&"/drofnats";'

'screen_rows:=512; screen_cols:=768;'

|mode_def cheapo =
| lowres_;
| fillin:=-.1;
' enddef;'

|mode_def luxo =
| proofing:=0;
| fontmaking:=1;
| tracingtitles:=1;
| pixels_per_inch:=2000;
| blacker:=.1;
| fillin:=.1;
| o_correction:=1;
' enddef;'

'localfont:=cheapo;'
\weakendlines
The macro '^@bye@' might also be redefined, as suggested at the close
of Appendix F.

To prepare a preloaded base file at this installation, a suitably
privileged person should run in the following way:

"'

This is METAFONT, Version 2.0 (INIMF) 8 NOV 1989 10:09
**plain
(plain.mf
Preloading the plain base, version 2.0)
*input local
(local.mf)
*dump
Beginning to dump on file plain.base

"'

(The stuff after "**'' or "*'' is typed by the user; everything
else is typed by the system. A few more messages actually come out.)

Notice that 'local.mf' does not include any new macros or features that a
programmer could use in a special way. Therefore it doesn't make plain
METAFONT\ incompatible with implementations at other computing centers.

Changes and/or extensions to the 'plain.mf' macros should never be made,
unless the resulting base file is clearly distinguished from the standard
plain base. But new, differently named bases are welcome.
For example, the author prepared a special base for the
fonts, so that they could be generated without first
reading the same 700 lines of macro definitions each time. To load
this base at high speed, he can type "&cm'' after METAFONT's initial
"**''. (Or, on some machines, he has a special
version called "cmmf'' in which the new base is already present.)

\endchapter

None but the Base, in baseness doth delight.

> --- MICHAEL , *Robert, Duke of Normandy* (1605)

So far all was plain sailing, as the saying is;
but Mr. Till knew that his main difficulties were yet to come.

> --- FRANCIS E. , *Milford Malvoisin* (1842)


# Appendix C. Character Codes

Different computers tend to have different ways of representing the
characters in files of text, but METAFONT\ gives the same results on
all machines, because it converts everything to a standard internal
code when it reads a file. METAFONT\ also converts back from its internal
representation to the appropriate external code, when it writes
a file of text; therefore most users need not be aware of the fact
that the have actually switched back and forth inside the machine.

The purpose of this appendix is to define METAFONT's internal code,
which has the same characteristics on all implementations of METAFONT\!.
The existence of such a code is important, because it
makes METAFONT\ programs portable.
METAFONT's scheme is based on the American Standard Code for
Information Interchange, known popularly as "." There are
128 codes, numbered 0 to 127; we conventionally express the numbers
in al notation, from 'oct"000"' to 'oct"177"', or in
adecimal notation, from 'hex"00"' to 'hex"7F"'. Thus, the value of
'ASCII"b"' is normally called 'oct"142"' or 'hex"62"', not 98. In the
scheme, codes 'oct"000"' through 'oct"037"' and
code 'oct"177"' are assigned to special functions; for example,
code 'oct"007"' is called 'BEL', and it means "Ring the bell."
The other 95 codes are assigned to visible symbols and to the
blank space character. Here is a
chart that shows ASCII codes in such a way that octal and hexadecimal
equivalents can easily be read off:
\beginchart{\global\count255='41\postdisplaypenalty=0\tentt
\def\chartstrut4.3pt to13.6pt}
&\oct00x&&NUL&&SOH&&STX&&ETX&&EOT&&ENQ&&ACK&&BEL&&\oddline0
&\oct01x&&BS&&HT&&LF&&VT&&FF&&CR&&SO&&SI&\evenline
&\oct02x&&DLE&&DC1&&DC2&&DC3&&DC4&&NAK&&SYN&&ETB&&\oddline1
&\oct03x&&CAN&&EM&&SUB&&ESC&&FS&&GS&&RS&&US&\evenline
&\oct04x&& &&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline2
&\oct05x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&\evenline
&\oct06x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline3
&\oct07x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&\evenline
&\oct10x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline4
&\oct11x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&\evenline
&\oct12x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline5
&\oct13x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&\evenline
&\oct14x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline6
&\oct15x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&\evenline
&\oct16x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\oddline7
&\oct17x&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&DEL&\evenline
\endchart

Ever since ASCII was established in the early 1960s, people have had
different ideas about what to do with positions 'oct"000"' thru 'oct"037"' and
'oct"177"', because most of the functions assigned to those codes are
appropriate only for special purposes like file transmission, not for
applications to printing or to interactive computing.
Manufacturers soon started producing line printers that were capable of
generating 128 characters, 33 of which were tailored to the special needs
of particular customers; part of the advantage of a standard code was
therefore lost.
An extended ASCII code intended for text editing and interactive computing
was developed at several universities about 1965, and
for many years there have been terminals in use at Stanford, MIT,
Carnegie-Mellon, and elsewhere that have 120 or 121 symbols, not just 95.
For example, the author developed METAFONT\ on a keyboard that
includes the symbols '{\tentex}', '{\tentex}',
'{\tentex}', and '{\tentex}', which are easier to use than
the character pairs '{\tentex}', '{\tentex}', '{\tentex}',
and '{\tentex}'. The full character set looks like this:
\beginchart{\tentex\postdisplaypenalty=0}
\normalchart
\endchart
METAFONT\ can also be configured to accept any or all of the character codes
128--255.
However, METAFONT\ programs that make use of anything in addition to the 95
standard ASCII characters cannot be expected to run on other systems, so
the use of extended character sets is discouraged.

A possible middle ground has been suggested, based on the fact that
it's easy to write a
program that converts extended-character files into standard files by
substituting "<>'' for '{\tentex}', etc. In the author's
implementation at Stanford, the symbols
'{\tentex}', '{\tentex}', '{\tentex}',
and '{\tentex}' are considered to be in the same class as
'{\tentex<}', '{\tentex=}', '{\tentex:}', and '{\tentex>}' when tokens are
formed (see Chapter 6). Tokens like '{\tentex=}'
and '{\tentex<}' are therefore distinct, although
they both become '{\tentex<>=}' after
conversion. As long as such tokens are avoided,
the author's programs can easily be expurgated into a
portable form for general distribution. \ (Another feasible approach would
have been to convert nonstandard codes to character pairs during METAFONT's
input process; that would have been slightly less efficient.)

Computers with non-ASCII character sets should specify a correspondence
between 95 distinct characters and the standard ASCII codes 'oct"040"'
thru 'oct"176"'. METAFONT\ programs written on any such machines will be
completely interchangeable with each other.

\endchapter

If any shall suggest, that some of the Enquiries here insisted upon
(as particularly those about the Letters of the Alphabet)
do seem too minute and trivial, for any prudent Man
to bestow his serious thoughts and time about.
Such Persons may know, that the discovery
of the true nature and Cause of any the most minute thing,
doth promote real Knowledge,
and therefore cannot be unfit for any Mans endeauours,
who is willing to contribute to the advancement of Learning.

> --- JOHN , *Towards a Real Character* (1668)

Clearly even the simple A.B.C. is a thing of mystery.
Like all codes, it should not be trifled with,
but it is to be feared that in modern times
it has not always been respected.

> --- STANLEY , *On Type Faces* (1923)


# Appendix D. Dirty Tricks

Any powerful computer language can be used in ways that go considerably
beyond what the language designer originally had in mind, especially
when macro expansion is possible. Sometimes the unexpected constructions
are just amusing; sometimes they are disgustingly arcane. But
sometimes they turn out to be quite useful, and they graduate from "tricks"
to the status of "techniques." \ (For example, several of the macros
now in Appendix B started out as suggestions for Appendix D.) \
In any case, gurus of a language always like to explore its limits.
The depths of METAFONT\ have hardly been plumbed, but this appendix probably
reached a new low at the time it was written.

Acknowledgment: More than half of the ideas in this appendix are due to
John , who has been a tireless and inspiring co-worker during the
entire development of the new METAFONT\ system.

amount by -.5pt
\abovedisplayskip by -.5pt
\belowdisplayskip by -.5pt

= spread-7\fontdimen4\font
Please don't read this material until you've had
= to{ plenty of experience with plain METAFONT\!.}
{\leaders{\dbend}{\box0\box1}}
\nointerlineskip
After you have read and understood the secrets below, you'll
know all sorts of devious combinations of METAFONT\ commands,
and you will often be tempted to write inscrutable macros. Always remember,
however, that there's usually a simpler and better way to do something
than the first way that pops into your head. You may not have to
resort to any subterfuge at all, since METAFONT\ is able to do lots of things
in a straightforward way. Try for simple solutions first.

## Macro madness

If you need to write complicated , you'll
need to be familiar with the fine points in Chapter 20. METAFONT's symbolic tokens
are divided into two main categories, "expandable" and "unexpandable";
the former category includes all macros and @if@$\,\ldots\,$@fi@ tests and
@for@$\,\ldots\,$@endfor@ loops, as well as special operations like @input@,
while the latter category includes the primitive operators and commands
listed in Chapters 25 and 26. The expansion of expandable tokens takes place
in METAFONT's "," but primitive statements (including equations,
declarations, and the various types of commands) are done in METAFONT's
"." There's a communication between the two, since the stomach
evaluates expressions that are needed as arguments to the mouth's macros;
any statement can be embedded in a group expression, so arbitrarily
complicated things can be done as part of the process.

Let's begin by considering a toy problem that is treated at the beginning
of Appendix D in *The TeX book*, in case some readers are interested in
comparing TeX\ to METAFONT\!. Given a numeric variable $n\ge0$, we wish to
define a macro 'asts' whose replacement text consists of precisely
$n$ asterisks. This task is somewhat tricky because expansion is suppressed
when a replacement text is being read; we want to use a ^@for@ loop, but
loops are special cases of expansion. In other words,

"'

def asts = for x=1 upto n: * endfor enddef

"'

defines 'asts' to be a macro with a @for@ loop in its replacement text;
\belowdisplayskip by -1.5pt
in practice, 'asts' would behave as if it contained $n$ asterisks (using
possibly different values of $n$), but
we have not solved the stated problem. The alternative

"'

def makedef primary n =
def asts = for x=1 upto n: * endfor enddef enddef;
makedef n

"'

"freezes" the present value of $n$; but this doesn't solve the problem either.

amount by .5pt
\abovedisplayskip by .5pt
\belowdisplayskip by 2pt

One solution is to build up the definition by adding one asterisk at a time,
using ^@expandafter@ as follows:

"'

def asts = enddef;
for x=1 upto n:
expandafter def expandafter asts expandafter = asts * enddef;
endfor.

"'

The three @expandafter@s provide a "finger" into the replacement text,
before @def@ suppresses expansion; without them the replacement text
would turn out to be "asts' '*'', causing infinite recursion.

This solution involves a running time proportional to $n^2$, so the
reader might wonder why a simpler approach like

"'

expandafter def expandafter asts expandafter =
for x = 1 upto n: * endfor enddef

"'

wasn't suggested? The reason is that this doesn't work, unless $n=0$!
A @for@ loop isn't entirely expanded by @expandafter@; only METAFONT's first
step in loop expansion is carried out. Namely, the loop text is read,
and a special token '' is placed at its end.
Later on when METAFONT's mouth encounters "ENDFOR'' (which incidentally is an
expandable token, but it wasn't listed in Chapter 20), the loop text is
re-inserted into the input stream, unless of course the loop has finished.
The special 'ENDFOR' is an '^@outer@' token, hence it should not
appear in replacement texts; METAFONT\ will therefore stop with a "^forbidden
token" error if you try the above with $n\ge1$.
^^@inner@ You might try to defeat the outerness by saying

"'

for x=1: inner endfor;

"'

but METAFONT\ won't let you. And even if this had worked, it wouldn't have
solved the problem; it would simply have put 'ENDFOR' into the
replacement text of 'asts', because expansion is inhibited when the
replacement text is being read.

There's another way to solve the problem that seems to have running
time proportional to $n$ rather than $n^2$:

"'

scantokens("def asts=" for x=1 upto n: & "* " endfor) enddef;

"'

but actually METAFONT's string
operation takes time proportional to the length of the strings it
deals with, so the running time is still order $n^2$.
Furthermore, the operations in METAFONT\ are rather primitive,
because this isn't a major aspect of the language; so it turns out that
this approach uses order $n^2$ storage cells in the string pool, although
they are recycled later. Even if the were infinite, METAFONT's
"" would be exceeded for large $n$, because ^@scantokens@
puts the string into the input buffer before scanning it.

Is there a solution of order $n$? Yes, of course. For example,

"'

def a=a* enddef;
for x=0 upto n:
if x=n: def a=quote quote def asts = enddef; fi
expandafter endfor a enddef;
showtoken asts.

"'

(The first '^@quote@' is removed by the @for@, hence one will survive until
$a$ is redefined. If you don't understand this program, try
running it with $n=3$; insert an isolated expression "0;'' just before
the "if'', and look at the lines of context that are shown when
METAFONT\ gives you four error messages.) \ The only flaw in this method is
that it uses up $n$ cells of stack space; METAFONT's
may have to be increased, if $n$ is bigger than 25 or so.

break
The asterisk problem is just a puzzle; let's turn now to a genuine
application. Suppose we want to define a macro called '"ten"'
whose replacement text is the contents of the parameter file
in Chapter 11, up to but *not* including the last two lines of
that file. Those last two lines say

"'

input logo
end

"'

The "ten" macro will make it possible to set up the 10-point parameters
repeatedly (perhaps alternating with 9-point parameters in a "nine" macro);
Appendix E explains how to create a meta-design tool via such macros.

One idea would be to try to input the entire file 'logo10.mf' as the
replacement text for "ten". We could nullify the effect of the last three
unwanted tokens by saying

"'

save input,logo,end;
forsuffixes s=input,logo,end: let s=\; endfor

"'

just before "ten" is used. To get the entire file as a replacement text,
we can try one of the approaches that worked in the asterisk problem, say

"'

expandafter def expandafter ten expandafter = input logo10 enddef.

"'

But this first attempt runs awry if we haven't already redefined '^@end@';
Appendix B makes '@end@' an '^@outer@' token, preventing its appearance
in replacement texts. So we say '^@inner@ @end@'
and try again, only to discover an unwritten law that somehow never
came up in Chapters 20 or 26:

"'

Runaway definition?
font_size10pt#;ht#:=6pt#;xgap#:=0.6pt#;u#:=4/9pt#;s#:=0;o#:=1/ ETC.
! File ended while scanning the definition of ten.
<inserted text>
enddef
l.2 ...fter ten expandafter = input logo10
enddef;

"'

The is invisible; but it's treated like an '@outer@'
token, in the sense that a file should never end when METAFONT\ is passing
rapidly over text.

Therefore this whole approach is doomed to failure. We'll have to find a
way to stop the replacement text before the file ends.
OK, we'll redefine '@input@' so that it means '@enddef@', and
redefine "logo" so that it means '^@endinput@'.

"'

let INPUT = input; let input = enddef; let logo = endinput;
expandafter def expandafter ten expandafter = INPUT logo10;
showtoken ten.

"'

It works! By the way, the line with three @expandafter@s can be replaced by
a more elegant construction that uses @scantokens@ as follows:

"'

scantokens "def ten=" INPUT logo10;

"'

This does the job because METAFONT\ always looks ahead and expands the token
immediately following an expression that is being evaluated. \ (The
expression in this case is the string '"def' 'ten="', which is an argument
to @scantokens@. The token that immediately follows an expression
almost always needs to be examined in order to be sure that the expression
has ended, so METAFONT\ always examines it.) \ Curiously, the @expandafter@
alternative causes "ten"'s replacement text to begin with the tokens
"font_size10pt#;ht#:=...'', while the @scantokens@ way makes it start
with "designsize:=(10);ht#:=...''. Do you see why? In the second case,
expansion continued until an unexpandable token ("designsize'') was
found, so the 'font_size' macro was changed into its replacement text; but
@expandafter@ just expanded "INPUT''.

Now let's make the problem a bit harder. Suppose we know that "input''
comes at the end of where we want to read, but we don't know that "logo''
will follow. We know that some program file name will be there, but
it might not be for the logo font. Furthermore, let's assume that "end''
might not be present; therefore we can't simply redefine it to be @enddef@.
In this case we can make "input'' into a right , and
read the file as a *delimited *;
that will give us enough time to insert other tokens, which will
terminate the input and flush the unwanted file name. But the construction
is more complex:

"'

let INPUT = input; delimiters begintext input;
def makedef(expr name)(text t) =
expandafter def scantokens name = t enddef;
endinput flushfilename enddef;
def flushfilename suffix s = enddef;
makedef("ten") expandafter begintext INPUT logo10;
showtoken ten.

"'

This example merits careful study, perhaps with '^@tracingall@' to
show exactly how METAFONT\ proceeds. We have assumed that the unknown file
name can be parsed as a suffix; this solves the problem that a file cannot
end inside of a @text@ parameter or a false condition. \ (If we knew that
'@end@' were present, we could have replaced "endinput' 'flushfilename'' by
"if' 'false:''\ and redefined "end'' to be "fi''.)

Let's turn now to a simpler problem. METAFONT\ allows you to consider the
'' of two boolean expressions, but it always evaluates both
expressions. This is problematical in situations like

"'

if pair x and (x>(0,0)): A else: B fi

"'

because the expression "x>(0,0)'' will stop with an error message
unless $x$ is of type @pair@. The obvious way to avoid this error,

"'

if pair x: if x>(0,0): A else: B fi else: B fi

"'

is cumbersome and requires 'B' to appear twice. What we want is a
"" operation in which the second boolean expression is
evaluated only if the first one turns out to be true; then we can safely write

"'

if pair x cand (x>(0,0)): A else: B fi.

"'

Similarly we might want "" in which the second operand is
evaluated only if the first is false, for situations like

"'

if unknown x cor (x<0): A else: B fi.

"'

Such and macros can be defined as follows:

"'

def cand(text q) = startif true q else: false fi enddef;
def cor(text q) = startif true true else: q fi enddef;
tertiarydef p startif true = if p: enddef;

"'

the are now evaluated only when necessary. We have essentially
^^@if@ replaced the original line by

"'

if if pair x: x>(0,0) else: false fi: A else: B fi.

"'

This construction has one catch; namely, the right-hand operands of 'cand' and
'cor' must be explicitly enclosed in delimiters. But delimiters are only a
minor nuisance, because the operands to 'and' and 'or' usually need them
anyway. It would be impossible to make 'cand' and 'cor' obey the normal
expression ; when macros make primary/secondary/tertiary
distinctions, they evaluate their arguments, and such evaluation is
precisely what 'cand' and 'cor' want to avoid.

If these 'cand' and 'cor' macros were changed so that they took
*undelimited* text arguments, the text argument wouldn't stop at a colon.
We could, however, use such modified macros with
instead. For example, after

"'

let = begingroup; let = endgroup;
def cand text q = startif true q else: false fi enddef

"'

we could write things like

"'

if (pair x) cand x>(0,0): A else: B fi.

"'

(Not that this buys us anything; it just illustrates a property of
undelimited text arguments.) \ Group delimiters
are not valid delimiters of *delimited* text arguments.

Speaking of group delimiters, the gratuitous ^@begingroup@ and ^@endgroup@
tokens added by ^@vardef@ are usually helpful, but they can be a nuisance.
For example, suppose we want to write a 'zz' macro such that
"zz1..zz2..zz3'' expands into

"'

z1dz1..z2dz2..z3dz3

"'

It would be trivial to do this with @def@:

"'

def zz suffix $ = z${dz$} enddef;

"'

but this makes 'zz' a "." Let's suppose that we want to use
@vardef@, so that 'zz' will be usable in suffixes of variable names.
Additional @begingroup@ and @endgroup@ delimiters will mess up the
syntax for paths, so we need to get rid of them. Here's one way to
finesse the problem:

"'

vardef zz@# =
endgroup gobbled true z@#dz@# gobble begingroup enddef.

"'

The and functions of Appendix B will remove the ^vacuous
expressions '@begingroup@ @endgroup@' at the beginning and end of
the replacement text.

(The initial @begingroup@ @endgroup@ won't be gobbled if the vardef is
being read as a primary instead of as a secondary, tertiary, or
expression. But in such cases you probably don't mind having @begingroup@
present.)

## Fortuitous loops

The '' and '' macros in Appendix B make use of the fact
that commas are like ")('' in argument lists. Although the
definition heading is

"'

def max(expr x)(text t)

"'

we can write 'max$(a,b,c)$' and this makes $x=a$ and $t=$'$b,c$'.
Of course, a person isn't supposed to say 'max$(a)(b)(c)$'.

Here are two more applications of the idea: We want '$(a,b,c)$'
to be true if and only if $a\le b\le c$; and we want
'^@equally\_spaced@$(x_1,x_2,x_3)\,"dx"$' to produce the equations
'$x_2-x_1=x_3-x_2="dx"$'.

"'

def inorder(expr x)(text t) =
((x for u=t: <= u)
and (u endfor gobbled true true)) enddef;
def equally_spaced(expr x)(text t) expr dx =
x for u=t: - u = u endfor gobbled true
- dx enddef.

"'

Isn't this fun? \ (Look closely.)

There is a problem, however, if we try to use these macros with
loops in the arguments. Consider the expressions

"'

inorder(for n=1 upto 10: a[n], endfor infinity),
inorder(a[1] for n=2 upto 10: ,a[n] endfor),
inorder(a[1],a[2] for n=3 upto 10: ,a[n] endfor);

"'

the first two give error messages, but the third one works!
The reason is that, in the first two cases,
the @for@ loop begins to be expanded before METAFONT\ begins to read the
, hence rears its ugly head again.
We can avoid this problem by rewriting the macros in a more complicated
way that doesn't try to single out the first argument $x$:

"'

def inorder(text t) =
expandafter startinorder for u=t:
<= u endgroup and begingroup u endfor
gobbled true true endgroup) enddef;
def startinorder text t =
(begingroup true enddef;
def equally_spaced(text t) expr dx =
if pair dx: (whatever,whatever) else: whatever fi
for u=t: - u = u endfor gobbled true
- dx enddef;

"'

Two separate tricks have been used here: (1) The '^@endgroup@' within
'inorder' will stop an undelimited text argument; this gets rid
of the unwanted "<=' 'u'' at the beginning. (2) A throwaway variable,
'^"whatever"', nullifies an unwanted equation at the beginning of
'@equally\_spaced@'. With the new definitions,
all three of the expressions above will be understood,
and so will things like

"'

equally_spaced(for n=1 upto 10: x[n], endfor whatever) dx.

"'

Furthermore the single-argument cases now work:
'inorder($a$)' will always be true, and
'@equally\_spaced@($x)\,"dx"$' will produce no new equations.

If we want to improve and in the same way, so that a person can
specify loop arguments like

"'

max(a[1] for n=2 upto 10: ,a[n] endfor)

"'

and so that 'max($a)=a$' in the case of a single argument, we have to
work harder, because max and min treat their first argument in quite
a special way; they need to apply the special macro ^"setu\_", which defines
the type of the auxiliary variable "u\_". The fastest way to solve this
problem is probably to use a token whose meaning changes during the
first time through the loop:

"'

vardef max(text t) =
let switch_ = firstset_;
for u=t: switch_ u>u_: u_ := u ;fi endfor
u_ enddef;
vardef min(text t) =
let switch_ = firstset_;
for u=t: switch_ u<u_: u_ := u ;fi endfor
u_ enddef;
def firstset_ primary u =
save u_; setu_ u; let switch_ = if; if false: enddef.

"'

Incidentally, the author's first programs for max and min
contained an interesting bug. They started with '@save@ "u\_"', and they
tried to recognize the first time through the loop by testing if "u\_" was
unknown. This failed because "u\_" could be constantly unknown in
well-defined cases like max$(x,x+1,x+2)$.

## Types

Our programs for 'inorder', 'equally_spaced', and
'max' are careful not to make unnecessary assumptions about the type
of an expression. The 'round' and 'byte' functions in Appendix B
are further examples of macros that change behavior based
on the types of their @expr@ arguments. Let's look more closely at
applications of type testing. \looseness=-1

When the author was developing macros for plain METAFONT\!, his first
"correct" solution for 'max' had the following form:

"'

vardef max(text t) =
save u_; boolean u_;
for u=t: if boolean u_: setu_ u
elseif u_<u: u_ := u fi; endfor
u_ enddef.

"'

This was interesting because it showed that there was no need to
set "u\_" to true or false; the simple fact that it was boolean
was enough to indicate the first time through the loop. \ (A slightly
different "setu\_" macro was used at that time.)

We might want to generalize the '' operation of METAFONT\ so that
'scaled $(x,y)$' is shorthand for ' $x$ $y$'.
That's pretty easy:

"'

let SCALED = scaled;
def scaled primary z =
if pair z: xscaled xpart z yscaled ypart z
else: SCALED z fi enddef;

"'

It's better to keep the primitive operation "SCALED' 'z'' here than to replace
it by the slower variant "xscaled' 'z' 'yscaled' 'z''.

METAFONT\ allows you to compare booleans, numerics, pairs, strings, and
transforms for equality; but it doesn't allow the expression
'$p=q$' where $p$ and $q$ are paths or pens or pictures. Let's
write a general macro such that '$p==q$'
will be true if and only if $p$ and $q$ are known and equal,
whatever their type.

"'

tertiarydef p == q =
if unknown p or unknown q: false
elseif boolean p and boolean q: p=q
elseif numeric p and numeric q: p=q
elseif pair p and pair q: p=q
elseif string p and string q: p=q
elseif transform p and transform q: p=q
elseif path p and path q:
if (cycle p = cycle q) and (length p = length q)
and (point 0 of p = point 0 of q): patheq p of q
else: false fi
elseif pen p and pen q: (makepath p == makepath q)
elseif picture p and picture q: piceq p of q
elseif vacuous p and vacuous q: true
else: false fi enddef;
vardef vacuous primary p =
not(boolean p or numeric p or pair p or path p
or pen p or picture p or string p or transform p) enddef;
vardef patheq expr p of q =
save t; boolean t; t=true;
for k=1 upto length p:
t := (postcontrol k-1 of p = postcontrol k-1 of q)
and (precontrol k of p = precontrol k of q)
and (point k of p = point k of q);
exitunless t; endfor
t enddef;
vardef piceq expr p of q =
save t; picture t;
t=p; addto t also -q;
cull t dropping origin;
(totalweight t=0) enddef;

"'

If $p$ and $q$ are numeric or pair expressions, we could relax the condition
that they both be known by saying '@if@ known $(p-q)$: $p=q$ @else@: @false@ @fi@';
transforms could be handled similarly by testing each of their six parts.
But there's no way to tell if booleans, paths, etc., have been equated
when they're both unknown, without the risk of irrevocably changing the
values of other variables.

##

METAFONT\ has a built-in solution mechanism
for linear equations, but it balks at nonlinear ones.
You might be able to solve a set of nonlinear equations yourself by
means of algebra or calculus, but in difficult cases it is probably
simplest to use the '^"solve"' macro of plain METAFONT\!. This makes it
possible to solve $n$ equations in $n$ unknowns, provided that at most
one of the equations is nonlinear when one of the unknowns is fixed.

The general technique will be illustrated here in the case $n=3$.
Let us try to find numbers $a$, $b$, and $c$ such that
$$\eqalign{-2a+3b/c&=c-3;
ac+2b&=c^3-20;
a^3+b^3&=c^2.}$$
When $c$ is fixed, the first two equations are linear in $a$ and $b$.
We make an inequality out of the remaining equation by changing '$=$'
to '$<$', then we embed the system in a boolean-valued function:

"'

vardef f(expr c) = save a,b;
-2a + 3b/c = c - 3;
a*c + 2b = c*c*c - 20;
a*a*a + b*b*b < c*c enddef;
c = solve f(1,7);
-2a + 3b/c = c - 3;
a*c + 2b = c*c*c - 20;
show a, b, c.

"'

If we set ^"tolerance"$="epsilon"$ (which is the minimum value
that avoids infinite looping in the "solve" routine), the values
$a=1$, $b=2$, and $c=3$ are shown (so it is obvious that the example
was rigged). If "tolerance" has its default value 0.1, we get
$a=1.05061$, $b=2.1279$, $c=3.01563$; this would probably be close
enough for practical purposes, assuming that the numbers represent
pixels. \ (Increasing the tolerance saves time because it
decreases the number of iterations within "solve"; you have to
balance time versus necessary accuracy.)

The only tricky thing about this use of "solve" was the choice of the
numbers 1 and 7 in '$f(1,7)$'. In typical applications we'll usually have
obvious values of the unknown where $f$ will be true and false,
but a bit of experimentation was necessary for the problem considered
here. In fact,
it turns out that $f(-3)$ is true and $f(-1)$ is false, in this
particular system; setting $c="solve"\,f(-3,-1)$ leads to
another solution: $a=7.51442$, $b=-7.48274$, $c=-2.3097$. Furthermore,
it's interesting to observe that this system has no solution with
$c$ between $-1$ and $+1$, even though $f(+1)$ is true and
$f(-1)$ is false! When $c\rightarrow0$, the quantity $a^3+b^3$
approaches $-\infty$ when $c$ is positive, $+\infty$ when $c$ is
negative. An attempt to '"solve" $f(1,-1)$' will divide by zero and
come up with several arithmetic overflows.

\hangindent=-42mm \hangafter=-7
Let's consider now a real application instead of a contrived example.
\rightfig Da (34mm x 24mm) ^20pt
We wish to find the vertices of a
$z_1l$, $z_1r$, $z_0l$, $z_0r$, such that

>
$x_1l=a$; \ \ $y_1r=b$; \ \ $z_0r=(c,d)$;
length$(z_1r-z_1l)$ $=$ length$(z_0r-z_0l)$ $=$ "stem",

and such that the lines $z_1r\dashto z_1l$ and
$z_1r\dashto z_0r$ meet at a given angle $\phi$. We can consider
the common angle $\theta$ of $z_1r-z_1l$ and $z_0r-z_0l$ to be
the "nonlinear" unknown, so the equations to be solved can be
written

>
$\penpos1("stem",\theta)$; \ \ $\penpos0("stem",\theta)$;
$x_1l=a$; \ \ $y_1r=b$; \ \ $z_0r=(c,d)$;
angle$(z_1r-z_0r)\,=\,\theta+\phi$.

When $\theta$ has a given value, all but the last of these equations
are linear; hence we can solve them by turning the crank in our general method:

"'

vardef f(expr theta) = save x,y;
penpos1(stem,theta); penpos0(stem,theta);
x1l=a; y1r=b; z0r=(c,d);
angle(z1r-z0r)<theta+phi enddef;
theta=solve f(90,0);
penpos1(stem,theta); penpos0(stem,theta);
x1l=a; y1r=b; z0r=(c,d);
show z1l,z1r,z0l,z0r,theta,angle(z1r-z0r).

"'

For example, if $a=1$, $b=28$, $c=14$, $d=19$, $"stem"=5$, and $\phi=80$,
we get

> \def
$(1,23.703)$&$(3.557,28)$&$(11.443,14.703)$&$(14,19)$&59.25&139.25

as answers when $"tolerance"="epsilon"$, and

> \def
$(1,23.702)$&$(3.554,28)$&$(11.446,14.702)$&$(14,19)$&59.28&139.25

when $"tolerance"=0.1$.
The function $f$ prescribed by the general method
can often be simplified; for example, in this case we can remove
redundancies and get just

"'

vardef f(expr theta) = save x,y;
penpos1(stem,theta); x1l=a; y1r=b;
angle(z1r-(c,d))<theta+phi enddef.

"'

The problem just solved can be called the " problem," because it arose in
connection with N. N. 's meta-design of a
'{\manual?}', and because it appears in Appendix D.

## Nonlinear interpolation

Suppose a designer has empirically determined good values of some quantity
$f(x)$ for several values of $x$; for example, $f(x)$ might be a
stroke weight or a serif length or an amount of overshoot, etc. These
empirical values can be generalized and incorporated into a
if we are able to between the original $x$'s, obtaining
$f(x)$ at intermediate points.

Suppose the data points are known for $x=x_1<x_2<\cdots<x_n$. We can
represent $f(x)$ by its graph, which we can assume is well approximated
by the METAFONT\ path defined by

>
$F\,=\,\bigl(x_1,f(x_1)\bigr)\to\bigl(x_2,f(x_2)\bigr)\to
*etc.*\to\bigl(x_n,f(x_n)\bigr)$

if $f(x)$ is a reasonable . Therefore interpolation can be
done by using path intersection (!):

"'

vardef interpolate expr F of x = save t; t =
if x < xpart point 0 of F: extrap_error 0
elseif x > xpart point infinity of F: extrap_error infinity
else: xpart(F intersectiontimes verticalline x) fi;
ypart point t of F enddef;
def extrap_error = hide(errhelp "The extreme value will be used.";
errmessage "'interpolate' has been asked to extrapolate";
errhelp "") enddef;
vardef verticalline primary x =
(x,-infinity)--(x,infinity) enddef;

"'

For example, if $f(1)=1$, $f(3)=2$, and $f(15)=4$, this interpolation
scheme gives 'interpolate $(1,1)\to(3,2)\to(15,4)$ of 7' the
approximate value 3.37.

## Drawing with

Let's leave numerical computations
now and go back into the realm of pictures. Bruce has suggested
an extension of plain METAFONT's '^@clearit@/^@showit@/^@shipit@' commands
by which '^@fill@' and '^@draw@' essentially operate on imaginary sheets of
clear plastic. A new command '^@keepit@' places a fresh sheet of plastic
on top of whatever has already been drawn, thereby preserving the covered image
against subsequent erasures.

We can implement @keepit@ by introducing a new picture variable
^"totalpicture", and new boolean variables ^"totalnull", ^"currentnull",
then defining macros as follows:

"'

def clearit = currentpicture:=totalpicture:=nullpicture;
currentnull:=totalnull:=true; enddef;
def keepit = cull currentpicture keeping (1,infinity);
addto totalpicture also currentpicture;
currentpicture:=nullpicture;
totalnull:=currentnull; currentnull:=true; enddef;
def addto_currentpicture =
currentnull:=false; addto currentpicture enddef;
def mergeit (text do) =
if totalnull: do currentpicture
elseif currentnull: do totalpicture
else: begingroup save v; picture v; v:=currentpicture;
cull v keeping (1,infinity); addto v also totalpicture;
do v endgroup fi enddef;
def shipit = mergeit(shipout) enddef;
def showit_ = mergeit(show_) enddef;
def show_ suffix v = display v inwindow currentwindow enddef;

"'

The "totalnull" and "currentnull" bookkeeping isn't strictly necessary,
but it contributes greatly to the efficiency of this scheme if the
extra generality of @keepit@ is not actually being used.
The '$v$' computations in @mergeit@ involve copying the accumulated
picture before displaying it or shipping it out; this takes time,
and it almost doubles the amount of memory needed, so we try to avoid it
when possible.

## Filing pictures

If you want to store a picture in a file
and read it in to some other METAFONT\ job, you face two problems:
(1) METAFONT's @shipout@ command implicitly culls the picture, so that only
binary data is left. Pixel values $>0$ are distinguished from pixel
values $\le0$, but no other information about those values will survive.
\ (2) The result of ^@shipout@ can be used in another METAFONT\ job only if
you have an auxiliary program that converts from binary format
to a METAFONT\ source program; METAFONT\ can write 'gf' files, but it can't
read them.

These problems can be resolved by using METAFONT's or
as the output medium, instead of using the 'gf' file. For example, let's
consider first the use of ^"tracingedges". Suppose we say

>
"tracingedges" $:=$ 1;
*any sequence of @fill@, @draw@, or @filldraw@ commands*
@message@ '"Tracing edges completed."'; \ $"tracingedges":=0$;

then the log file will contain lines such as the following:
\beginlines
'Tracing edges at line 15: (weight 1)'
'(1,5)(1,2)(2,2)(2,1)(3,1)(3,0)(8,0)(8,1)(9,1)(9,2)(10,2)(10,8)(9,8)'
'(9,9)(8,9)(8,10)(3,10)(3,9)(2,9)(2,8)(1,8)(1,5).'

'Tracing edges at line 15: (weight -1)'
'(3,5)(3,2)(4,2)(4,1)(7,1)(7,2)(8,2)(8,8)(7,8)(7,9)(4,9)(4,8)(3,8)(3,5).'

'Tracing edges at line 18: (weight -1)'
'(No new edges added.)'

'Tracing edges completed.'
\endlines
Let us write macros so that these lines are acceptable input to METAFONT\!.

"'

def Tracing=begingroup save :,[,],Tracing,edges,at,weight,w;
delimiters []; let Tracing = endfill; interim turningcheck := 0;
vardef at@#(expr wt) = save (,); w := wt;
let ( = lp; let ) = rp; fill[gobble begingroup enddef;
let edges = \; let weight = \; let : = \; enddef;
def lp = [ enddef;
def rp = ] -- enddef;
vardef No@# = origin enddef;
def endfill = cycle] withweight w endgroup; enddef;
def completed = endgroup; enddef;

"'

^^"turningcheck" ^^@save@ ^^@delimiters@
The precise form of edge-traced output, with its limited vocabulary
and its restricted use of parentheses and commas, has been exploited here.

With slight changes to this code, you can get weird effects.
For example, if the definition of 'rp' is changed to "]..tension 4..'',
and if "scaled' '5pt'' is inserted before "withweight'',
the image will be an "" character:
\displayfig Daa (18.5mm)
(The bumps at the left here are due to the repeated points "(1,5)'' and
"(3,5)'' in the original data. You can remove them by adding an extra
pass, first tracing the edges that are output by the *unmodified*
'Tracing' macros.)

Although the effects of @fill@ and @draw@ can be captured by
"tracingedges", other operations like are not traced.
Let us therefore consider the more general picture representation
that METAFONT\ produces when ^"tracingoutput" is positive, or when you
ask it to ^@show@ a picture (see Chapter 13). The macros on the next
page will recreate a picture from input of the form

"'

beginpicture
row 1: 1+ -2- " 0+ 2-
row 0: " 0+ 2++ 5---
row -2: 0- -2+ "
endpicture

"'

where the middle three lines have been copied verbatim from a transcript
file. \ (The task would be easier if the token "-'' didn't have
to perform two different functions!)

"'

let neg_ = -; let colon_ = :;
def beginpicture =
begingroup save row, ", :, ---, --, +, ++, +++, v, xx, yy, done;
picture v; v := nullpicture; interim turningcheck := 0;
let --- = mmm_; let -- = mm_;
let + = p_; let ++ = pp_; let +++ = ppp_;
let row = pic_row; let " = relax; let : = pic_colon; : enddef;
def pic_row primary y = done; yy := y; enddef;
def pic_colon primary x =
if known x colon_ ; xx := x; pic_edge fi enddef;
def pic_edge =
let - = m_;
addto v contour unitsquare xscaled xx shifted(0,yy) enddef;
def mmm_ = withweight 3; let - = neg_; : enddef;
def mm_ = withweight 2; let - = neg_; : enddef;
def m_ = withweight 1; let - = neg_; : enddef;
def p_ = withweight neg_1; let - = neg_; : enddef;
def pp_ = withweight neg_2; let - = neg_; : enddef;
def ppp_ = withweight neg_3; let - = neg_; : enddef;
transform xy_swap; xy_swap = identity rotated 90 xscaled -1;
def endpicture = done;
v transformed xy_swap transformed xy_swap endgroup enddef;

"'

The reader will find it instructive to study these macros closely.
When "done'' appears, it is an unknown primary, so 'pic_colon'
will not attempt to generate another edge. Each new edge also
inserts a cancelling edge at $x=0$. The two applications ^^"xy\_swap"
of 'xy_swap' at the end will clear away all redundant edges. (Double
swapping is a bit faster than the operation "rotated-90' 'rotated' '90''
that was used for this purpose in Chapter 13.)

## Fattening a pen

Let's move on to another aspect of
METAFONT\ by considering
an operation on : Given a @pen@ value $p$,
the task is to construct a pen '^@taller@ $p$' that is one pixel
taller. For example, if $p$ is the nib
'$(0.5,0)\dashto(0,0.5)\dashto(-0.5,0)\dashto(0,-0.5)\dashto\cycle$',
the taller nib will be

>
$(0.5,0.5)\dashto(0,1)\dashto(-0.5,0.5)\dashto(-0.5,-0.5)\dashto(0,-1)
\dashto(0.5,-0.5)\dashto\cycle$;

if $p$ is a tilted '$(-x,-y)\dashto(x,y)\dashto\cycle$',
the taller nib will be

>
$(-x,-y-0.5)\dashto(x,y-0.5)\dashto(x,y+0.5)\dashto(-x,-y+0.5)\dashto\cycle$,

assuming that $x>0$. The macro itself turns out to be fairly simple, but
it makes instructive use of and pen operations.

We want to split the pen into two parts, a "bottom" half and a "top"
half; the bottom half should be shifted down by .5 pixels, and the
top half should be shifted up. The dividing points between halves occur
at the leftmost and rightmost vertices of the pen. Hmmm; a potential problem
arises if there are two or more leftmost or rightmost points; for example,
what if we try to make '@taller@ @taller@ $p$'? Fortunately METAFONT\ doesn't
mind if a pen polygon has three or more consecutive vertices that
lie on a line, hence we can safely choose *any* leftmost
point and any rightmost point.

The next question is, "How should we find leftmost and rightmost
points?" We will, of course, use ^@makepath@ to find the set of all
vertices; so we could simply traverse the path and find the minimum
and maximum $x$ coordinates. However, it will be faster (and more fun)
to use either or for this purpose.
Let's try directiontime first:

"'

vardef taller primary p =
save r, n, t, T; path r;
r = tensepath makepath p; n = length r;
t = round directiontime up of r;
T = round directiontime down of r;
if t>T: t := t-n; fi
makepen(subpath(T-n,t) of r shifted .5down
-- subpath(t,T) of r shifted .5up -- cycle) enddef;

"'

The result of @makepath@ has control points equal to their adjacent
vertices, so it could not be used with directiontime.
\ (If any key point is equal to its precontrol or postcontrol,
the "" of the path is zero at that point; directiontime
assumes that all directions occur whenever the velocity drops to zero.) \
Therefore we have used '^@tensepath@'.
This almost works, once we realize that the values
of $t$ and $T$ sometimes need to be rounded to integers. But it
fails for pens like @penspeck@ that have points very close together,
since @tensepath@ is no better than an unadulterated @makepath@ in such cases.
Furthermore, even if we could define a nice path from $p$ (for example
by scaling it up), we would run into problems of
numerical instability, in cases like @penrazor@ where
the pen polygon takes a $180^\circ$ turn. Razor-thin pens cannot be recognized
easily, because they might have more than two vertices; for example,
rotations of future pens such as
'@makepen@($"left"\to"origin"\to"right"\to\cycle$)' are problematical.

We can obtain a more robust result by using penoffset, because
this operation makes use of the convexity of the polygon. The
"fastest" solution looks like this:

"'

vardef taller primary p =
save q, r, n, t, T; pen q; q = p;
path r; r = makepath q; n = length r;
t = round xpart(r intersectiontimes penoffset up of q);
T = round xpart(r intersectiontimes penoffset down of q);
if t>T: t := t-n; fi
makepen(subpath(T-n,t) of r shifted .5down
-- subpath(t,T) of r shifted .5up -- cycle) enddef;

"'

(The argument $p$ is copied into $q$, in case it's a ;
this means that the conversion of future pen to pen need be
done only once instead of three times.)

## n} polynomials

And now, for our last trick,
let's try to extend METAFONT's syntax so that it will accept generalized
formulas of the form '$t[u_1,\ldots,u_n]$' for all $n\ge2$.
\ (This notation was introduced for $n=3$ and 4 in Chapter 14, when we were
considering fractional subpaths.) \ If $n>2$, the identity

>
$t[\,u_1,\ldots,u_n]\;=\;t\bigl[t[u_1,\ldots,u_n-1],t[u_2,\ldots,u_n]\,\bigr]$

defines $t[u_1,\ldots,u_n]$ recursively, and it can be shown that the
alternative definition

>
$t[\,u_1,\ldots,u_n]\;=\;t\bigl[t[u_1,u_2],\ldots,t[u_n-1,u_n]\,\bigr]$

gives the same result. \ (Indeed, we have

>
$\displaystyle t[u_1,\ldots,u_n]\;=\;\sum_k=1^n{n-1\choose k-1}
(1-t)tu_k,$

a Bernshte{\u\i}n polynomial of order $n-1$.)

Our problem is to change the meaning of METAFONT's so that
expressions like '$1/2[a,b,c,d]$' will evaluate to '$.125a+.375b+.375c
+.125d$' in accordance with the formulas just given, but we don't want
to mess up the other primitive uses of brackets in contexts like
"x[n]'' and "path' 'p[][]a''. We also want to be able to use
brackets inside of brackets.

The reader is challenged to try solving this problem before looking at
the weird solution that follows. Perhaps there is a simpler way?

"'

def lbrack = hide(delimiters []) lookahead [ enddef;
let [[[ = [; let ]]] = ]; let [ = lbrack;
def lookahead(text t) =
hide(let [ = lbrack;
for u=t, hide(n_ := 0; let switch_ = first_): switch_ u; endfor)
if n_<3: [[[t]]] else: Bernshtein n_ fi enddef;
def first_ primary u =
if numeric u: numeric u_[[[]]]; store_ u
elseif pair u: pair u_[[[]]]; store_ u fi;
let switch_ = store_ enddef;
def store_ primary u = u_[[[incr n_]]] := u enddef;
primarydef t Bernshtein nn = begingroup save r; r =
begingroup for n=nn downto 2:
for k=1 upto n-1: u_[[[k]]]:=t[[[u_[[[k]]],u_[[[k+1]]] ]]];
endfor endfor u_[[[1]]] endgroup; numeric u_[[[]]];
r endgroup enddef;

"'

The most subtle thing about this code is the way it uses the 'empty'
option of a ^*for list* to dispense with .
Since METAFONT\ evaluates all the expressions of a ^@for@ loop before
reading the loop text, and since "n_'' and "u_'' are used here
only when no recursion is taking place, it is unnecessary to
their values even when brackets are nested inside of brackets.
However, the auxiliary variables "u_[[['$k$']]]'' must not remain
independent at the end.

Of course this trick slows METAFONT\ down tremendously, whenever brackets
appear, so it is just of academic interest. But it seems to work
in all cases except with respect to formulas that involve ''
(two consecutive brackets); the latter token, which plain METAFONT\ expands
to "]' ']'', is not expanded when 'lookahead' reads its ^text
argument, hence the user must remember to insert a space between
consecutive brackets. \looseness=-1

\endchapter

Their tricks an' craft hae put me daft,
They've taen me in, an' a' that.

> --- ROBERT , *The Jolly Beggar* (1799)

Ebery house hab him dutty carner.

> --- and , *Jamaica Proverbs and Sayings* (1927)


# Appendix E. Examples

We've seen lots of examples of individual letters or parts of letters;
let's concentrate now on the problem of getting things all together.
The next two pages contain the entire contents of an example file
"logo.mf'', which generates the letters of the METAFONT\ . The file
is short, because only seven letters are involved, and because those letters
were intentionally done in a style that would be easy for the system they name.
But the file is complete, and it illustrates in simplified form all
the essential aspects of larger fonts: Ad hoc dimensions are
converted to pixels; subroutines are defined; programs for
individual letters appear; intercharacter and interword
spacing conventions are nailed down. Furthermore, the character programs
are careful to draw letters that will be
well adapted to the raster, even if pixels on the output device are
not square.

We've been studying the 'METAFONT' letters off and on since Chapter 4, making
our examples slightly more complex as more of the language has been
encountered. Finally we're ready to pull out all the stops and look at the
real, professional-quality 'logo.mf', which incorporates all the best
suggestions that have appeared in the text and in answers to the exercises.

It's easy to generate a font with 'logo.mf', by proceeding as explained
in Chapter 11. For example, the 'logo10' font that produces 'METAFONT' in
10-point size can be created for a low-resolution printer by running
METAFONT\ with the

"'

\mode=lowres; input logo10

"'

where the 'logo10.mf' appears in that chapter. Furthermore
the slanted version '{\manual 89:;<=>:}'\ can be created by
inputting the parameter file 'logosl10.mf', which says simply

"'

slant := 1/4;
input logo10

"'

The ^"slant" parameter affects ^"currenttransform" as explained in
Chapter 15.

There isn't a great deal of "" in the 'logo.mf' design,
because only a few forms of the METAFONT\ logo are needed. However, some
interesting variations are possible; for example, if we use the
parameter files

> \def \belowdisplayskip by 3pt
'font_size 30pt#;'&'font_size 10pt#;'
'ht#:=25pt#;'&'ht#:=6pt#;'
'xgap#:=1.5pt#;'&'xgap#:=2pt#;'
'u#:=3/9pt#;'&'u#:=4/3pt#;'
's#:=1/3pt#;'&'s#:=-2/3pt#;'
'o#:=2/9pt#;'&'o#:=1/9pt#;'
'px#:=1pt#;'&'px#:=1/3pt#;'
'slant:=-1/9;'

we get {\manual BCDGHIJD} and {\manual KLUVWvwU},
\ respectively.

\obeylines\everyparindent=0pt
|
|

'mode_setup;'
'if unknown slant: slant:=0 else: currenttransform:='
' identity slanted slant yscaled aspect_ratio fi;'

|ygap#:=(ht#/13.5u#)*xgap#;
|ho#:=o#;
|leftstemloc#:=2.5u#+s#;
|barheight#:=.45ht#;
|py#:=.9px#;

'define_pixels(s,u);'
'define_whole_pixels(xgap);'
'define_whole_vertical_pixels(ygap);'
'define_blacker_pixels(px,py);'
'pickup pencircle xscaled px yscaled py;'
'logo_pen:=savepen;'
'define_good_x_pixels(leftstemloc);'
'define_good_y_pixels(barheight);'
'define_corrected_pixels(o);'
'define_horizontal_corrected_pixels(ho);'

'def beginlogochar(expr code, unit_width) ='
' beginchar(code,unit_width*u#+2s#,ht#,0);'
' pickup logo_pen enddef;'

'def super_half(suffix i,j,k) ='
' draw z.i0,y.j-y.i'
' ... (.8[x.j,x.i],.8[y.i,y.j])z.j-z.i'
' ... z.jx.k-x.i,0'
' ... (.8[x.j,x.k],.8[y.k,y.j])z.k-z.j'
' ... z.k0,y.k-y.j enddef;'

'beginlogochar("M",18);'
'x1=x2=leftstemloc; x4=x5=w-x1; x3=w-x3;'
'y1=y5; y2=y4; bot y1=-o;'
'top y2=h+o; y3=y1+ygap;'
'draw z1--z2--z3--z4--z5;'
'labels(1,2,3,4,5); endchar;'

'beginlogochar("E",14);'
'x1=x2=x3=leftstemloc;'
'x4=x6=w-x1+ho; x5=x4-xgap;'
'y1=y6; y2=y5; y3=y4;'
'bot y1=0; top y3=h; y2=barheight;'
\nointerlineskip
\smash{{
{\figboxEb{224\apspix}{216\apspix}}

{\figboxA18a{240\apspix}{216\apspix}}

{\figboxEa{208\apspix}{216\apspix}}
}}
\obeylines\everyparindent=0pt
\smash{{
{\figbox18a{240\apspix}{216\apspix}}

{\figbox4c{288\apspix}{216\apspix}}

{\figbox11a{224\apspix}{216\apspix}}

{\figbox21a{240\apspix}{216\apspix}}
}}\nointerlineskip
'draw z6--z1--z3--z4; draw z2--z5;'
'labels(1,2,3,4,5,6); endchar;'

'beginlogochar("T",13);'
'italcorr ht#*slant + .5u#;'
'if .5w<>good.x .5w: change_width; fi'
'lft x1=-eps; x2=w-x1; x3=x4=.5w;'
'y1=y2=y3; top y1=h; bot y4=-o;'
'draw z1--z2; draw z3--z4;'
'labels(1,2,3,4); endchar;'

'beginlogochar("A",15);'
'x1=.5w; x2=x4=leftstemloc; x3=x5=w-x2;'
'top y1=h+o; y2=y3=barheight;'
'bot y4=bot y5=-o;'
'draw z4--z2--z3--z5; super_half(2,1,3);'
'labels(1,2,3,4,5); endchar;'

'beginlogochar("F",14);'
'x1=x2=x3=leftstemloc;'
'x4=w-x1+ho; x5=x4-xgap;'
'y2=y5; y3=y4; bot y1=-o;'
'top y3=h; y2=barheight;'
'draw z1--z3--z4; draw z2--z5;'
'labels(1,2,3,4,5); endchar;'

'beginlogochar("O",15);'
'x1=x4=.5w; top y1=h+o; bot y4=-o;'
'x2=w-x3=good.x(1.5u+s); y2=y3=barheight;'
'super_half(2,1,3); super_half(2,4,3);'
'labels(1,2,3,4); endchar;'

'beginlogochar("N",15);'
'x1=x2=leftstemloc; x3=x4=x5=w-x1;'
'bot y1=bot y4=-o;'
'top y2=top y5=h+o; y3=y4+ygap;'
'draw z1--z2--z3; draw z4--z5;'
'labels(1,2,3,4,5); endchar;'

'ligtable "T": "A" kern -.5u#;'
'ligtable "F": "O" kern -u#;'

'font_quad:=18u#+2s#;'
'font_normal_space:=6u#+2s#;'
'font_normal_stretch:=3u#;'
'font_normal_shrink:=2u#;'
'font_identifier:="MFLOGO" if slant<>0: & "SL" fi;'
'font_coding_scheme:="AEFMNOT only";'

Everything in 'logo.mf' has already been explained previously in this
book except for the very last two lines, which define a '^@font\_identifier@'
and a '^@font\_coding\_scheme@'. These are optional bits of information
that are discussed in Appendix F. Furthermore an
has been specified for the letter '{\manual T}', since it's the final
letter of '{\manual 89:;<=>:}'.

The program for a complete typeface will differ from the program for
this simple logo font primarily in degree; there will be lots more
parameters, lots more subroutines, lots more characters, lots more
ligatures and kerns and whatnot. But there will probably also be
more administrative machinery, designed to facilitate the creation,
testing, and modification of characters, since a large enterprise
requires good organization. The remainder of this appendix is
devoted to an example of how this might be done: We shall discuss
the additional kinds of routines that the author found
helpful while he was developing the family
of typefaces.

The complete, unexpurgated programs for Computer Modern appear in *Computers \& Typesetting*, Volume E; but since they have evolved
over a long period of time, they are rather complex. We shall simplify
the details so that it will be easier to grasp the important issues
without being distracted by irrelevant technicalities.

The simple logo fonts discussed above are generated by two types
of files: There are parameter files like 'logo10.mf', and there is
a program file 'logo.mf'. The Computer Modern fonts, being more
extensive, are generated by four types of files: There are
like "cmr10.mf'', which specify the
ad hoc dimensions for particular sizes and styles of type; there are
like "roman.mf'', which serve as chief
executives of the font-generation process; there are
like "punct.mf'', which contain programs
for individual characters; and there's a called
"cmbase.mf'', which contains the subroutines and other macros used
throughout the system.

Our logo example could have been cast in this more general mold by moving
the character programs into a program file "METAFON.mf'', and by moving
most of the opening material into a base file "logobase.mf''
that looks like this:
\beginlines
|
|logobase:=1;

'def font_setup ='
' if unknown slant: slant:=0 else: currenttransform:='

\smash{\vdots} to10pt
1pt(the previous code is unchanged)
' define_corrected_pixels(o);'
' define_horizontal_corrected_pixels(ho); enddef;'
\endlines
followed by the definitions of 'beginlogochar' and 'super_half'.
Then we're left with a driver file 'logo.mf' that looks like this:
\beginlines
|
'if unknown logobase: input logobase fi'

|mode_setup; font_setup;
|input METAFON

'ligtable "T": "A" kern -.5u#;'
\weakendlines
and so on, concluding as before.

In general, a parameter file calls on a driver file, which calls on
one or more program files; the base file contains predefined macros
shared by all. There may be several driver files, each using a
different combination of program files; for example, Computer Modern
has "roman.mf'' and "italic.mf'',
both of which call on 'punct.mf' to generate punctuation marks,
although they use different program files to generate the lowercase
alphabets. Characters are partitioned into program files so that
they can be shared by different drivers.

Parameter files in Computer Modern don't quite follow the conventions
of 'logo10.mf'. Here, for example, are the
opening and closing lines of :
\beginlines
|
'if unknown cmbase: input cmbase fi'

'font_identifier "CMR"; font_size 10pt#;'

|u#:=20/36pt#;
|width_adj#:=0pt#;
|serif_fit#:=0pt#;

\vdots
|low_asterisk:=false;
|math_fitting:=false;

|generate roman
\endlines
The main differences are: \ (1) There's special code at the beginning, to
make sure that 'cmbase.mf' has been loaded. The base file includes
several things that are needed right away; for example, 'cmbase' declares
the variables '"serifs"' and '^"monospace"' to be of type @boolean@,
so that boolean-valued parameter assignments like '$"serifs":=@true@$'
will be legal. \ (2) The @font\_identifier@ is defined in the parameter file,
not in the driver file. \ (3) The last line says '^@generate@' instead of
'@input@'; the base file defines @generate@ to be the same as @input@,
but other meanings are assigned by utility routines that we'll study later.
\ (4) The final '^@end@' is no longer present in the parameter file.

The 'roman.mf' driver looks like this (vastly simplified):
^^@font\_slant@ ^^@font\_quad@ ^^@font\_normal\_space@
^^@font\_normal\_stretch@ ^^@font\_normal\_shrink@
\beginlines
|

'mode_setup; font_setup;'

|input romanu;
|input romanl;
|input romand;
|input punct;

'font_slant slant;'
'if monospace: font_quad 18u#;'
| font_normal_space 9u#;
'else: font_quad 18u#+4letter_fit#;'
| font_normal_space 6u#+2letter_fit#;
| font_normal_stretch 3u#;
' font_normal_shrink 2u#;'
| input romlig;
' " "f": "i" =: oct"014", "f" =: oct"013", "l" =: oct"015",'
' "'" kern u#, "?" kern u#, "!" kern u#;'
| ligtable oct"013": "i" =: oct"016", "l" =: oct"017",
' "'" kern u#, "?" kern u#, "!" kern u#;'
| ligtable "-": "-" =: oct"173";
| ligtable oct"173": "-" =: oct"174";
| ligtable "'": "'" =: oct"134";
| ligtable "'": "'" =: oct"042",
' "?" kern 2u#, "!" kern 2u#;'
'fi; '
\endlines
In a font like , all characters will be exactly
$9u\0$ wide. Both 'cmr10' and 'cmtt10' use the 'roman' driver, but
'roman' omits the ligatures and changes the interword spacing
when it is producing monospaced fonts.

The program files of Computer Modern have slightly different conventions
from those of plain METAFONT\!. Here, for example, are the
programs for two of the simplest :
\beginlines
'cmchar "Period";'
'numeric dot_diam#; dot_diam# = if monospace: 5/4 fi dot_size#;'
'define_whole_blacker_pixels(dot_diam);'
'beginchar(".",5u#,dot_diam#,0);'
'adjust_fit(0,0); pickup fine.nib;'
'pos1(dot_diam,0); pos2(dot_diam,90);'
|x1l=good.x(x1l+.5w-x1); bot y2l=0; z1=z2; dot(1,2);
'penlabels(1,2); endchar;'

{\figbox{Ec\&Ed}3in{360\apspix}}

'iff not monospace: cmchar "Em dash";'
'beginchar(oct"174",18u#,x_height#,0);'
'italcorr .61803x_height#*slant + .5u#;'
'adjust_fit(letter_fit#,letter_fit#);'
'pickup crisp.nib; pos1(vair,90); pos2(vair,90);'
'y1r=y2r=good.y(y1r+.61803h-y1); lft x1=-eps; rt x2=w+eps;'
|filldraw stroke z1e--z2e;
'penlabels(1,2); endchar;'
\endlines
The new structural features in these programs are: (1) '^@cmchar@',
which appears at the very beginning of each character program;
(2) '^@iff@ *boolean expression*:', which precedes @cmchar@ if
the character is to be generated only when the boolean expression
is true; (3) '^@adjust\_fit@', which can change the amount of white space
at the character's left and/or right; (4) pens called '"fine.nib"' and
'"crisp.nib"'; (5) new macros '"pos"', '"dot"', and '"stroke"',
discussed further below.

The base file 'cmbase.mf' begins as follows:
\beginlines
|

|cmbase:=1;

|let cmchar = relax;
|let generate = input;

'newinternal slant, superness,' $\ldots$ |
'boolean serifs, monospace,' $\ldots$ |
\endlines
These few lines are straightforward enough. Although 'cmchar' is defined
to be the same as , which does nothing, the definition of
'cmchar' will be changed by certain utility programs below; this will
prove to be a convenience when characters are designed, tested, and maintained.

The next few lines of 'cmbase' are trickier. They implement the '@iff@'
feature, which bypasses unwanted characters at high speed.
\beginlines
'let semi_ = ;; let colon_ = :; let endchar_ = endchar;'
'def iff expr b ='
' if b: let next_ = use_it else: let next_ = lose_it fi;'
' next_ enddef;'
'def use_it = let : = restore_colon; enddef;'
'def restore_colon = let : = colon_; enddef;'
'def lose_it = let endchar = fi; inner cmchar; let ; = fix_ semi_'
' if false enddef;'
'def fix_ = let ; = semi_; let endchar = endchar_; outer cmchar; enddef;'
'def always_iff = let : = endgroup; killboolean enddef;'
'def killboolean text t = use_it enddef;'
'outer cmchar;'
\weakendlines
^^@always\_if@ ^^@inner@ ^^@outer@
(The 'lose_it' routine assumes that every character program will end
with "endchar;''.)

The most interesting part of 'cmbase' is probably the way it allows the
"" of each character to be fine-tuned. The amount of
space at the left and right edges of the character's ""
can be adjusted without actually shifting the picture, and without
changing the width that was specified in @beginchar@. Here's how it works:
After a @beginchar@ command and an optional @italcorr@, each Computer
Modern character program is supposed to say

>
@adjust\_fit@(*left sidebearing adjustment*,
*right sidebearing adjustment*);

sidebearing adjustments are given in true, "sharped" units.
The ^@adjust\_fit@ routine essentially adds extra space at the left
and right, corresponding to the sidebearing adjustments. An ad hoc
dimension called "^"letter\_fit"$\0$" is also added to all sidebearings,
behind the scenes.

Our example program for the '"."'\ says simply '@adjust\_fit@$(0,0)$';
this means that only "letter\_fit" is added. The program for em-dash
says '@adjust\_fit@$("letter\_fit"\0,\allowbreak"letter\_fit"\0)$', hence
the sidebearings are increased by 2"letter\_fit" at each side.
The total character width of the em-dash comes to $18u\0+
4"letter\_fit"\0$ (which is indeed one em, the value of ^@font\_quad@
specified in the 'roman' driver file).

The program for lowercase '' in file 'romanl.mf' says
'@adjust\_fit@$("serif\_fit"\0,0)$'; this adds the ^"serif\_fit"
parameter at the left, to compensate for the possible appearance
of a serif at the left of this character. The "serif\_fit" is
zero in 'cmr10', but it has a negative value in a font,
and a positive value when serifs are extralong.

The nice thing about @adjust\_fit@ is that it's an "add-on"
specification that doesn't affect the rest of the character design.
The program can still be written as if 0 were the left edge and
$w$ were the right edge; afterwards the fit can be adjusted without
changing the program or the shapes.

There are two versions of @adjust\_fit@, one for normal fonts
and one for fonts. Both of them are slightly complicated
by something called ^"shrink\_fit", which will be explained later;
for the moment, let's just imagine that $"shrink\_fit"=0$. Here is the
routine for the normal case:
\beginlines
'def normal_adjust_fit(expr left_adjustment,right_adjustment) ='
' l := -hround(left_adjustment*hppp)-letter_fit;'
' interim xoffset := -l;'
' charwd := charwd+2letter_fit#+left_adjustment+right_adjustment;'
' r := l+hround(charwd*hppp)-shrink_fit;'
' w := r-hround(right_adjustment*hppp)-letter_fit;'
' enddef;'
\endlines
Variables ^"l" and ^"r" are set to the actual pixel boundaries of the
character; thus, plain METAFONT's bounding box has $0\le x\le w$, but
Computer Modern's has $l\le x\le r$. has been done
very carefully so that the sidebearings will have consistent
relationships across an entire font. Notice that has been
recalculated; this means that @adjust\_fit@ can affect the digitization,
but---we hope---in a beneficial way.

In a monospaced font, the @adjust\_fit@ routine changes the
unit-width parameter, ^"u", so that the total width after adjustment
comes out to be constant. Similar adjustments are made to parameters
like ^"jut", the nominal serif length. The width of all characters
in a monospaced font will be $"mono\_charwd"\0$ in true units,
^"mono\_charwd" in pixels. The italic correction of all
characters will be $"mono\_charic"\0$.
\beginlines
'def mono_adjust_fit(expr left_adjustment,right_adjustment) ='
' numeric expansion_factor; mono_charwd# = 2letter_fit#'
' + expansion_factor*(charwd+left_adjustment+right_adjustment);'
' forsuffixes $=u,jut,' $\ldots$ ':'
' $ := $.#*expansion_factor*hppp; endfor'
' l := -hround(left_adjustment*expansion_factor*hppp)-letter_fit;'
' interim xoffset := -l;'
' r := l+mono_charwd-shrink_fit;'
' w := r-hround(right_adjustment*expansion_factor*hppp)-letter_fit;'
' charwd := mono_charwd#; charic := mono_charic#;'
' enddef;'
\weakendlines
It took the author umpteen trials to get this routine right.

The ^"xoffset" calculations in @adjust\_fit@ are enough to shift the
character by the proper amount when it's being . We just
have to take care of getting the correct character width in pixels,
and 'cmbase' does this by setting
^^"extra\_endchar"
\beginlines
'extra_endchar := extra_endchar&"r:=r+shrink_fit;w:=r-l;";'
\endlines

No other changes to plain METAFONT's ^@endchar@ routine are needed; but we do
need to redefine and , in order to show the
adjusted bounding box. It's convenient to change 'makebox' so that it also
slants the box, in a slanted font, and so that it draws vertical lines
one unit apart as aids to the designer; several more horizontal lines
are also drawn:
\beginlines
'def makebox(text rule) ='
' for y=0,asc_height,body_height,x_height,bar_height,'
| -desc_depth,-body_depth: rule((l,y)t_,(r,y)t_); endfor
| for x=l,r: rule((x,-body_depth)t_,(x,body_height)t_); endfor
' for x=u*(1+floor(l/u)) step u until r-1:'
| rule((x,-body_depth)t_,(x,body_height)t_); endfor
' if charic<>0:'
| rule((r+charic*pt,h.o_),(r+charic*pt,.5h.o_)); fi
' enddef;'

'def maketicks(text rule) ='
' for y=0,h.o_,-d.o_:'
| rule((l,y),(l+10,y)); rule((r-10,y),(r,y)); endfor
' for x=l,r: rule((x,10-d.o_),(x,-d.o_));'
| rule((x,h.o_-10),(x,h.o_)); endfor
' if charic<>0:'
| rule((r+charic*pt,h.o_-10),(r+charic*pt,h.o_)); fi
' enddef;'
\weakendlines
(Examples of the new 'makebox' routine appear in the illustrations for
period and em-dash earlier in this appendix, and also in Chapter 23.)

Plain METAFONT's ^@change\_width@ routine must also be generalized:
\beginlines
|def change_width = if not monospace:
' if r+shrink_fit-l = floor(charwd*hppp): w := w+1; r := r+1;'
' else: w := w-1; r := r-1; fi fi enddef;'
\endlines

The Computer Modern ^@font\_setup@ routine is invoked at the beginning of
each driver file. This is what converts sharped units to pixels;
@font\_setup@ also computes additional quantities that are important to the
font as a whole. It's a long macro, but here are its important features:
\beginlines
'def font_setup ='
' define_pixels(u,jut,' $\ldots$ ');'
' define_whole_pixels(letter_fit,fine,crisp,' $\ldots$ ');'
' define_whole_vertical_pixels(body_height,cap_height,' $\ldots$ ');'
' define_whole_blacker_pixels(hair,stem,curve,' $\ldots$ ');'
' define_whole_vertical_blacker_pixels(vair,slab,' $\ldots$ ');'
' define_corrected_pixels(o,' $\ldots$ ');'
break
' if monospace: mono_charwd# := 9u#; define_whole_pixels(mono_charwd);'
' mono_charic# := max(0,body_height#*slant);'
' let adjust_fit = mono_adjust_fit;'
' else: let adjust_fit = normal_adjust_fit; fi'
' lowres_fix(stem,curve) 1.2;'
^^@lowres\_fix@ break
' '*Initialize pen nibs, see below*
break
' ":=identity slanted slant'
' yscaled aspect_ratio scaled ";'
' shrink_fit := 1+hround(2letter_fit#*hppp)-2letter_fit;'
' if not string mode: if mode <= smoke: shrink_fit := 0; fi fi'
' enddef;'
\endlines
If $"letter\_fit"\0=0$, the '^"shrink\_fit"' is set to 1; otherwise
"shrink\_fit" is 0, 1, or 2, depending on how "letter\_fit" has
rounded to an integer. This amount is essentially subtracted from
before each character in the font has been drawn. Experience shows that
this trick greatly improves the readability of fonts at
and .

Many of the Computer Modern characters are drawn with ^@filldraw@, which
is a mixture of outline-filling and fixed-pen drawing. Several macros
are included in 'cmbase' to facilitate filldrawing, especially
'^"pos"' and '^"stroke"':
\beginlines
'vardef pos@#(expr b,d) ='
' (x@#r-x@#l,y@#r-y@#l)=(b-currentbreadth,0) rotated d;'
' x@#=.5(x@#l+x@#r); y@#=.5(y@#l+y@#r) enddef;'
break
'vardef stroke text t ='
' forsuffixes e=l,r: path_.e:=t; endfor'
' path_.l -- reverse path_.r -- cycle enddef;'
\endlines
Thus "pos" is like ^"penpos", except that it subtracts ^"currentbreadth"
from the overall breadth. \ (Cf. the program for left parentheses in
Chapter 12.) \ The "stroke" routine is a simplified alternative to
@penstroke@, such that @penstroke@ is equivalent to '@fill@ "stroke"'
if the specified path isn't a cycle.

The value of "currentbreadth" is maintained by redefining plain METAFONT's
'^"numeric\_pickup\_"' macro so that it includes the new line
\beginlines
' if known breadth_[q]: currentbreadth:=breadth_[q]; fi'
\endlines
The ^@clear\_pen\_memory@ macro is redefined so that its second line now says
\beginlines
' numeric pen_lft_[],pen_rt_[],pen_top_[],pen_bot_[],breadth_[];'
\endlines
relevant entries of the "breadth\_" array will be defined by @font\_setup@,
as we'll see soon.

The example programs for period and em-dash say '@pickup@ "fine.nib"' and
'@pickup@ "crisp.nib"'. These nibs are initialized by @font\_setup@ in
the following way:
\beginlines
' clear_pen_memory;'
' forsuffixes $ = fine,crisp,' $\ldots$ ':'
' $.breadth := $;'
' pickup if $=0: nullpen else: pencircle scaled $; $ := $-eps fi;'
' $.nib := "; breadth_[$.nib] := $;'
' forsuffixes $$ = lft,rt,top,bot: shiftdef($.$$,$$ 0); endfor endfor'
\weakendlines
If, for example, we have $"fine"=4$, this code sets $"fine.breadth":=4$,
$"fine.nib":=1$, $"fine":=4-"eps"$, and $"breadth\_"[1]:=4-"eps"$.
\ (A small amount ^"eps" has been subtracted so that "pos" will
usually find $b-"currentbreadth">0$.) \ Furthermore, four subroutines
^"fine.lft", "fine.rt", "fine.top", and "fine.bot" are defined, so
that it's easy to refer to the edges of "fine.nib" when it has not been
picked up. These four subroutines are created by a slightly
tricky macro:
\beginlines
'def shiftdef(suffix $)(expr delta) ='
' vardef $ primary x = x+delta enddef enddef;'
\endlines

OK, we've just about covered everything in 'cmbase' that handles the
extra administrative complexity inherent in a large-scale design.
The rest of the base file simply contains subroutines like
^"serif" and ^"dot", for recurring features of the characters themselves.
Such subroutines needn't be shown here.

To make a binary file called , there's a trivial file "cm.mf'':
\beginlines
|
'input cmbase; '
\endlines

\medbreak
Besides parameter files, driver files, program files, and the base file,
the Computer Modern routines also include a number of
that provide a convenient environment for designing new characters and
improving old ones. We'll conclude this appendix by studying the contents
of those utility files.

Let's suppose, for example, that test proofs have revealed problems
with the characters 'k' and 'S', so we want to fix them. Instead of
working with the font as a whole, we can copy the programs for those two
characters (and only those two) into a temporary file called ''.
Then we can run METAFONT\ on the file '', which says the following:
\beginlines
|
'if unknown cmbase: input cmbase fi'
'mode_setup;'

'def generate suffix t = enddef;'
'input cmr10; font_setup;'
break
'let echar = endchar;'
'def endchar = echar; stop "done with char "&decimal charcode&". " enddef;'
'let iff = always_iff;'

'input test; bye'
\endlines
This will produce proofs of 'k' and 'S', using the 'cmr10' parameters.
Notice the simple trick by which 'rtest' is able to stay in charge
after inputting 'cmr10', without letting the 'roman' driver come into
action: "generate'' is redefined so that it becomes innocuous.
Furthermore 'rtest' changes so that METAFONT\ will and
display each character before moving on to the next. The ''
convention is changed to "always_iff'', so that every test character will
^^@always\_iff@ be tested even if the boolean expression is undefined;
this makes it easier to copy from program files
into the test file and back again, since the 'iff' indications do not
have to be touched.

If you invoke METAFONT\ with "\mode=lowres;' 'input' 'rtest'', you'll generate
a low-resolution font called 'rtest' with the parameters of 'cmr10',
but containing only the characters in the test file. If you leave out
the mode, you get proof mode as usual.

There are similar pseudo-drivers 'ttest.mf' (for 'cmtt10' instead of 'cmr10'),
'btest.mf' (for 'cmbx10'), etc.; these make it possible to try the
test characters with many different parameter settings. There's also
'ztest.mf', which inputs parameters from a temporary file "z.mf'' that
contains special parameters of interest at the moment. \ (If file
'z.mf' does not exist, you'll get a chance to specify another
parameter file, online.) \looseness=-1

A more elaborate called "6test.mf'' allows you
to test up to six parameter settings simultaneously, and to see the
results all at once on your screen, as illustrated in Chapter 23.
Here is the program that does the necessary magic:
\beginlines
|
'if unknown cmbase: input cmbase fi'
|mag=.5;
'mode_setup; let mode_setup=\;'

'boolean running;'
'def abort = hide(scrollmode; running := false) enddef;'
'def pause = stop "done with char "&decimal charcode&". " enddef;'
'let iff = always_iff;'
'def ligtable text t=enddef;'
'def charlist text t=enddef;'
'def extensible text t=enddef;'
break
'string currenttitle;'
'let semi = ;; let echar = endchar; let endchar = enddef;'
'def cmchar expr s = currenttitle := s;'
' let ; = testchar semi quote def chartext = enddef;'
'def testchar = semi let ; = semi;'
' running := true; errorstopmode;'
' for k=1 upto 6:'
' if running: if known params[k]: scantokens params[k]; font_setup;'
' currentwindow:=k;'
' currenttitle & ", " & fontname[k];'
' chartext echar; fi fi endfor'
' pause; enddef;'
break
'string params[],fontname[];'
'params[1] = "roman_params"; fontname[1] = "cmr10";'
'params[2] = "sans_params"; fontname[2] = "cmssbx10";'
'params[3] = "ital_params"; fontname[3] = "cmti10";'
'params[4] = "tt_params"; fontname[4] = "cmtt10";'
'params[5] = "bold_params"; fontname[5] = "cmb10";'
'params[6] = "quote_params"; fontname[6] = "cmssqi8";'
break
'w_rows = floor 1/2 screen_rows; w_cols = floor 1/3 screen_cols;'
'def open(expr k,i,j)='
' openwindow k from ((i-1)*w_rows,(j-1)*w_cols) to (i*w_rows,j*w_cols)'
' at (-10,140) enddef;'
'def openit ='
' open(1,1,1); open(2,1,2); open(3,1,3);'
' open(4,2,1); open(5,2,2); open(6,2,3); enddef;'
break
'begingroup delimiters begintext generate;'
' def makedef(expr s)(text t) ='
' expandafter def scantokens s = t enddef; flushtext enddef;'
' def flushtext suffix t = enddef;'
' for k=1 upto 6: if known params[k]:'
' makedef(params[k])'
' expandafter expandafter expandafter begintext'
' scantokens ("input "&fontname[k]); fi endfor'
'endgroup;'

'input test; bye'
\endlines
^^@errorstopmode@ ^^@scrollmode@ ^^@quote@ ^^@openwindow@ ^^@openit@
^^"currentwindow" ^^@expandafter@ ^^@scantokens@
Parameters are moved from parameter files into macros, using a trick
discussed near the beginning of Appendix D. Then ^@cmchar@ is redefined
so that the entire text of each character-to-be-tested will be embedded
in another macro called "chartext". Each instance of "chartext" is
repeatedly applied to each of the six font setups.

An error that occurs with the first or second set of parameters may be
so bad that you won't want to see what happens with the third, fourth,
fifth, and sixth sets. For example, when 'test.mf' contains characters
that are being newly designed, some equations might have been omitted
or mistyped, so the results will be ludicrous. In this case you can
the program and type "I' '. The '6test' routine
has an 'abort' macro that will stop at the end of the current font setup
and move directly to the next character, without trying any of the
remaining parameter combinations.

It's possible to include material in 'test.mf' that isn't part of
a character program. For example, you might want to redefine a subroutine
in the base file. Only the character programs themselves (i.e., the
sequences of tokens between '@cmchar@' and '@endchar@;') are subject to
six-fold repetition.

Some large characters may not appear in full, because there might not be
room for them on the screen at the stated magnification. You can make
everything smaller by running METAFONT\ with, say, "=1/3; input 6test''.
The computer will stop with an error message, saying that the equation
"mag=.5'' is ; but you can safely proceed, because you
will have the magnification you want.

\endchapter

An ensampull yn doyng ys more commendabull
\indent{\cmman}en ys techyng o{\cmman}er prechyng.

> --- JOHN , *The Festyuall* (c.1400)

Old people love to give good advice,

to console themselves for no longer being able to give bad examples.

> --- , *Maximes* (1665)


# Appendix F. Font Metric Information

The TeX\ typesetting system assumes that some "intelligence" has been
built into the fonts it uses. In other words, information stored with
TeX's fonts will have important effects on TeX's behavior. This
has two consequences: (a) Typesetting is quite flexible, since few
conventions are frozen into TeX\ itself. (b) Font designers must work
a little harder, since they have to tell TeX\ what to do. The purpose
of this appendix is to explain how you, as a font designer, can cope
with (b) in order to achieve spectacular successes with (a).

The information used by TeX\ is embedded in compact binary files called
TeX\ Font Metric () files. Although the "t'' in "tfm'' stands
for TeX, this is an artifact of history, because other formatting systems
can work with 'tfm' files too. The files should have been called just "fm'',
but it's too late now.

METAFONT\ is able to produce two different kinds of binary output files.
One, a "gf'' file, contains digitized character shapes and some additional
information needed by programs that drive printing devices; such files
are discussed in Appendix G. The other type of output is a 'tfm' file,
which contains font information used by formatting routines like TeX;
such files are our present concern. You get a 'tfm' file if and only
if METAFONT's internal quantity '^"fontmaking"' is positive at the end
of your job. \ (Plain METAFONT's @mode\_setup@ routine usually sets
"fontmaking" to an appropriate value automatically.)

The 'tfm' file contains some information about each character, some
information about combinations of characters, and some information
about the font as a whole. We shall consider these three kinds
of information in turn. All of the font metric data that refers to
physical dimensions should be expressed in device-independent,
"" units; when a particular font is produced with different
modes or magnifications, all its 'tfm' files should be identical.

A formatting program like TeX\ needs to know the size of each character's
" ." For example, when TeX\ typesets a word like
'box', it places the first letter 'b' into a little box in such a way that
the METAFONT\ pixel whose lower left corner is at $(0,0)$ will appear
on the baseline of the current line being typeset, at the left edge
of the box. \ (We assume for simplicity that ^"xoffset" and ^"yoffset"
were zero when 'b' was shipped out.) \ The second letter, 'o', is placed
in a second little box adjacent to the first one, so we obviously must tell
TeX\ how wide to make the 'b'.

In fact, TeX\ also wants to know the height and depth of each letter.
This affects the placing of , if you wish to typeset
'\d{\ b}\d{\ o}\d{\ x}\d{\ y}', and it also
avoids overlap when adjacent lines contain boxes that go unusually
far above or below the baselines.

A total of four dimensions is given for each character, in sharp
units (i.e., in units of printer's points):

- ^"charwd", the width of the bounding box.
- ^"charht", the height (above the baseline) of the bounding box.
- ^"chardp", the depth (below the baseline) of the bounding box.
This is a *positive* number if the character descends below the
baseline, even though the corresponding $y$ values are negative.
- ^"charic", the character's "." TeX\
adds this amount to the width of the box (at the right-hand side)
in two cases: (a) When the user specifies an italic correction explicitly,
by typing " immediately after the character. (b) When an
character is used in math mode, unless it has a subscript but no
superscript. For example, the italic correction is applied to '$P$' in
the formulas '$P(x)$' and '$P^2$', but not in the formula '$P_n$';
it is applied to position the superscript but not the subscript
in '$P_n^2$'.

In plain METAFONT\ programs, you specify "charwd", "charht", and "chardp"
in a ^@beginchar@ command, and you specify "charic" (if it's positive)
in an ^@italcorr@ command. But @beginchar@ and @italcorr@ are macros,
not primitives of METAFONT\!. What really happens is that METAFONT\ records the
value of its internal quantities "charwd", "charht", "chardp", and "charic"
at the time of a ^@shipout@ command. These values (and all other
dimensions to be mentioned below) must be less than $2048"pt"\0$ in
absolute value.

A font contains at most 256 character codes; the operator
can be used to tell which codes have already appeared. If two or more
characters are shipped out with the same code number (possibly with
different ^"charext" values), the "charwd",
"charht", "chardp", and "charic" of the final one are assumed to
apply to them all.

At most 15 different nonzero heights, 15 different nonzero depths,
and 63 different nonzero italic corrections may appear in a single
font. If these limits are exceeded, METAFONT\ will change one or more
values, by as little as possible, until the restriction holds.
A warning message is issued if such changes are necessary; for example,

"(some' 'charht' 'values' 'had' 'to' 'be' 'adjusted' 'by' 'as' 'much'
'as' '0.12pt)'' means that you had too many different nonzero heights, but
METAFONT\ found a way to reduce the number to at most 15 by changing some of
them; none of them had to be changed by more than 0.12 points. No warning
is actually given unless the maximum amount of perturbation exceeds
${1\over16}\pt$.

\medbreak
The next kind of information that TeX\ wants is concerned with
pairs of adjacent characters that are typeset from the same font.
For example, TeX\ moves the 'x' slightly closer to the 'o' in the
word 'box', and it moves the 'o' slightly away from the 'b', because
of information stored in the 'tfm' file for the font you're now reading.
This space adjustment is called . Otherwise (if the
three characters had simply been placed next to each other according
to their "charwd" values) the word would have been 'box', which
looks slightly worse. Similarly, there's a difference between
'difference' and 'difference', because the 'tfm' file tells TeX\
to substitute the ligature 'ff' when there are two f's in a row.

Ligature information and kerning information is specified in short
"" of a particularly simple form. Here's an example
that illustrates most of the features (although it is not a serious
example of typographic practice):
\beginlines
' "f": "f" =: oct"013", "i" '\"=: oct"020", skipto 1;|
'ligtable "o": "b": "p": "e" kern .5u#, "o" kern .5u#, "x" kern-.5u#,'
' 1:: "!" kern u#;'
\endlines
This sequence of instructions can be paraphrased as follows:

\hangindent 3pc
Dear TeX, when you're typesetting an 'f' with this font, and when the
following character also belongs to this font, look at it closely because
you might need to do something special: If that following character is
another 'f', replace the two f's by character code 'oct"013"'
[namely ''];
if it's an 'i', retain the 'f' but replace the 'i' by character code
'oct"020"' [a dotless ''];
otherwise skip down to label "1::''\ for further instructions.
When you're typesetting an 'o' or 'b' or 'p', if the next input to TeX\ is
'e' or 'o', add a half unit
of space between the letters; if it's an 'x', subtract a half unit; if it's an
exclamation point, add a full unit. The last instruction applies also
to exclamation points following 'f' (because of the label "1::'').

When a character code appears in front of a colon, the colon "labels"
the starting place for that character's ligature and kerning program,
which continues to the end of the ligtable statement. A double colon denotes
a "local label"; a 'skipto' instruction advances to the next matching local
label, which must appear before 128 ligtable steps intervene. The special
label \'\":' can be used to initiate ligtable instructions for an invisible
"left boundary character" that is implicitly present just before every
word; an invisible "right boundary character" equal to ^"boundarychar" is
also implicitly present just after every word, if "boundarychar" lies between
0 and 255.

The general syntax for ligtable programs is pretty easy to guess from
these examples, but we ought to exhibit it for completeness:
\beginsyntax \chardef\\='\|
<ligtable command>\is[ligtable]<ligtable program><optional skip>
<ligtable program>\is<ligtable step>\alt<ligtable program>[,]<ligtable step>
<optional skip>\is[,][skipto]<code>\alt<empty>
<ligtable step>\is<code><ligature op><code>
\alt<code>[kern]<numeric expression>
\alt<label><ligtable step>
<ligature op>\is[=:]\alt[\\=:]\alt[\\=:>]\alt[=:\\]\alt[=:\\>]
\alt[\\=:\\]\alt[\\=:\\>]\alt[\\=:\\>>]
<label>\is<code label>\alt<code>[::]\alt[\\\\:]
<code label>\is*code*[:]
<code>\is<numeric expression>\alt<string expression>
\endsyntax
A *code* should have a numeric value between 0 and 255, inclusive,
after having been rounded to the nearest integer; or it should be a
string of length 1, in which case it denotes the corresponding
code (Appendix C). For example, '"A"' and '64.61' both
specify the code value 65. Vertical bars to the left or right of "=:''\
tell TeX\ to retain the original left and/or right character that invoked a
ligature. Additional ">'' signs tell TeX\ to advance its focus of attention
instead of doing any further @ligtable@ operations at the current
character position.

*Caution:* Novices often go overboard on kerning. Things usually
work out best if you kern by at most half of what looks right to you
at first, since kerning should not be noticeable by its presence
(only by its absence). Kerning that looks right in a logo or in a
headline display often interrupts the rhythm of reading when it appears
in ordinary textual material.

You can improve TeX's efficiency by ordering the steps of a ligtable
program so that the most frequent alternatives come first.
TeX\ will stop reading the program when it finds the first "hit."

\medbreak
Several characters of a font can be linked together in a series
by means of a ^@charlist@ command. For example,

"'

charlist oct"000": oct"020": oct"022": oct"040": oct"060"

"'

is used in the font to specify the left parentheses that
TeX\ uses in displayed math formulas, in increasing order of size.
TeX\ follows charlists to make variable-size delimiters and
variable-width , as well as to link text-size operators
like '$\sum$' to the display-size '$\displaystyle\sum$'.

TeX\ builds up large delimiters by using "" characters,
which are specified by giving top, middle, bottom, and repeatable
characters in an ^@extensible@ command. For example, the extensible
left in 'cmex10' are defined by

"'

extensible oct"060": oct"060", 0, oct"100", oct"102";

"'

this says that character code 'oct"060"' specifies an extensible
delimiter constructed from itself as the top piece, from character number
'oct"100"' as the bottom piece, and from character number 'oct"102"' as
the piece that should be repeated as often as necessary to reach
a desired size. In this particular example there is no middle
piece, but characters like curly braces have a middle piece as well.
A zero value in the top, middle, or bottom position means that
no character should be used in that part of the construction;
but a zero value in the final position means that character number zero
is the repeater. The width of an extensible character is taken to
be the width of the repeater. \looseness=-1

The first eight different sizes of parentheses available to TeX\ in
'cmex10', when the user asks for "\left('', look like this:

>
$\bigl(\Bigl(\biggl(\Biggl(
\mathopen{{$\left( to20.5pt\right.delimiterspace=0pt$}}
\mathopen{{$\left( to23.5pt\right.delimiterspace=0pt$}}
\mathopen{{$\left( to26.5pt\right.delimiterspace=0pt$}}
\mathopen{{$\left( to29.5pt\right.delimiterspace=0pt$}}$

According to what we know from the examples of @charlist@ and @extensible@
above, the first four of these are the characters in positions
'oct"000"', 'oct"020"', 'oct"022"', and 'oct"040"'. The other four have
character 'oct"060"' on top; character 'oct"100"' is at the bottom;
and there are respectively zero, one, two, and three occurrences
of character 'oct"102"' in the middle.

Here is the formal syntax:
\beginsyntax
<charlist command>\is[charlist]<labeled code>
<labeled code>\is<code>
\alt<code label><labeled code>
<extensible command>\is[extensible]<code label><four codes>
<four codes>\is<code>[,]<code>[,]<code>[,]<code>
\endsyntax
Notice that a *code label* can appear in a @ligtable@, @charlist@, or
@extensible@ command. These appearances are mutually exclusive: No code may be
used more than once as a label. Thus, for example, a character with a
ligature/kerning program cannot also be @extensible@, nor can it be
in a @charlist@ (except as the final item).

\medbreak
The last type of information that appears in a 'tfm' file applies to
the font as a whole. Two kinds of data are involved, bytes and
numerics; and they are specified in "headerbyte" and "fontdimen"
commands, according to the following general syntax:
\beginsyntax
<headerbyte command>\is[headerbyte]<numeric expression>[:]<byte list>
<fontdimen command>\is[fontdimen]<numeric expression>[:]<numeric list>
<byte list>\is<code>
\alt<byte list>[,]<code>
<numeric list>\is<numeric expression>
\alt<numeric list>[,]<numeric expression>
\endsyntax
We shall defer discussion of header bytes until later, because they
are usually unnecessary. But @fontdimen@ commands are important.
Numeric parameters of a font can be specified by saying, e.g.,

"'

fontdimen 3: 2.5, 6.5, 0, 4x

"'

which means that parameters 3--6 are to be 2.5, 6.5, 0, and $4x$,
respectively. These are the parameters that TeX\ calls '\fontdimen3'
thru '\fontdimen6'. \ (Parameter numbering is old-fashioned:
There is no '\fontdimen0'.)

The first seven fontdimen parameters have special significance, so plain
METAFONT\ has seven macros to specify them symbolically, one at a time:

- ^@font\_slant@ ('\fontdimen1') is the amount of
per point; TeX\ uses this information when raising or lowering an
accent character.
- ^@font\_normal\_space@ ('\fontdimen2') is the interword spacing.
If the value is zero, all characters of this
font will be considered to be "" in math mode, so the
will be added more often than otherwise.
- ^@font\_normal\_stretch@ ('\fontdimen3') is the
of interword spacing, as explained in *The TeX book*.
- ^@font\_normal\_shrink@ ('\fontdimen4') is the
of interword spacing, as explained in *The TeX book*.
- ^@font\_x\_height@ ('\fontdimen5') is the height of characters
for which accents are correctly positioned. An accent over a character
will be raised by the difference between the character's "charht"
and this value. The is also the unit of height that
TeX\ calls one "ex''.
- ^@font\_quad@ ('\fontdimen6') is the unit of width that
TeX\ calls one "em''.
- ^@font\_extra\_space@ ('\fontdimen7') is the additional amount
added to the normal interword space between sentences, depending
on the "space factor" as defined in *The TeX book*.

Parameters are zero unless otherwise specified.

Math symbol fonts for TeX\ are required to have at least 22 fontdimen
parameters, instead of the usual seven; math extension fonts need at least 13.
Appendix G of *The TeX book* explains the precise significance
of these additional parameters, which control such things as the
placement of superscripts and subscripts.

\medbreak
The of a font is not one of the fontdimen
parameters; it's an internal quantity of METAFONT\ that is actually output
among the header bytes as explained below. When a TeX\ user asks
for a font "at'' a certain size, the font is scaled by the ratio
between the "" and the design size. For example,
'cmr10' has a design size of $10\pt$; if a TeX\ user requests
"cmr10' 'at' '15pt'', the result is the same as "cmr10' 'scaled' '1500''
(or, in plain METAFONT\ terms, 'cmr10' with 'mag=1.5').

What does the design size really mean? It's an imprecise notion,
because there need be no connection between the design size and any specific
measurement in a font. Typographers have always been vague when
they speak about "10 point" fonts, because some fonts look larger
than others even though the horizontal and vertical dimensions are the same.
It's something like dress sizes or shoe sizes.

In general, the design size is a statement about the approximate size
of the type. Type with a larger design size generally looks bigger
than type with a smaller design size. Two fonts with the same design
size are supposed to work well together; for example, 'cmr9' and
'cmtt9' both have $9\pt$ design size, although the uppercase letters of
'cmtt9' are quite a bit smaller ("A'' versus 'A').

The "designsize" must be at least $1"pt"\0$. And, as with all 'tfm'
dimensions, it must be less than $2048"pt"\0$. Any other value is
changed to $128"pt"\0$.

METAFONT\ looks at the value of ^"designsize" only when the job ends, so you
needn't set it before characters are shipped out. At the end of a job,
when the 'tfm' file is being written, METAFONT\ checks to make sure that every
dimension of the font is less than 16 times the design size in absolute
value, because this limitation is imposed by the 'tfm' file format. Thus,
for example, if the design size is $10\pt$, you cannot have a character
whose width or height is $160\pt$ or more. If one or more dimensions prove
to be too big, METAFONT\ will tell you how many of them had to be changed.

\medbreak
The ^@headerbyte@ command is similar to @fontdimen@, but it gives
8-bit *code* data instead of numeric information. For example,

"'

headerbyte 33: 0, 214, 0, "c"

"'

says that bytes 33--36 of the 'tfm' file header will be 0, 214,
0, and 99. The first four header bytes (numbers 1--4) are automatically
set to a , unless you have specified other values for
at least one of those bytes. \ (This check sum will match a similar
value in the 'gf' file, so that other typesetting software can check
the consistency of the different files they use.) \ Similarly,
the next four header bytes (numbers 5--8) are set automatically to
the design size times $2$, unless you have specified something
else. \looseness=-1

TeX\ looks only at the first eight header bytes, so you needn't use the
header\-byte command if you are simply producing a font for
standard TeX. But other software that reads 'tfm' files may have
a need for more header information. For example, the original
'tfm' format (developed by Lyle at Palo Alto
Research Center) included ^@font\_coding\_scheme@ information
in bytes 9--48 of the header, and ^@font\_identifier@ information in
bytes 49--68. The design size of certain fonts was also packed into
byte 72. Each font in the "Xerox world" is uniquely identified by
its font identifier and its design size, rather than by its font file name.

The "font coding scheme" is merely a comment that can be used
to help understand large collections of fonts; it's usually a nice thing
to know. Some of the coding scheme names in common use are

>
'TeX text'&'TeX math italic'
'TeX typewriter text'&'TeX math symbols'
'XEROX text'&'TeX math extension'
'ASCII'&'TeX extended ASCII'
'PI'&'GRAPHIC'

The coding-scheme string should not include parentheses.

Here are macros that can be used, if desired, to convert plain
METAFONT's @font\_identifier@ and @font\_coding\_scheme@ into the format

required by Ramshaw's original 'tfm' files:
\beginlines
|def BCPL_string(expr s,n) =
' for l:=if length(s)>=n: n-1 else: length(s) fi: l'
' for k:=1 upto l: , substring (k-1,k) of s endfor'
' for k:=l+2 upto n: , 0 endfor endfor enddef;'

' end;'
'def bye = if fontmaking>0:'
' headerbyte 9: BCPL_string(font_coding_scheme_,40);'
' special "codingscheme " & font_coding_scheme_;'
' headerbyte 49: BCPL_string(font_identifier_,20);'
' special "identifier " & font_identifier_;'
' headerbyte 72: max(0, 254 - round 2designsize); fi'
' end enddef;'
' bye,end;'
\endlines
These macros could be included among the extensions to
'plain.mf' at particular installations. When a user says '^@bye@' instead
of '^@end@', the additional headerbyte documentation will then be
automatically inserted into the 'tfm' file.

\medbreak
Let us now conclude this appendix by summarizing what we've learned.
A METAFONT\ programmer can provide various types of information about how
to typeset with a font, by using font metric commands. Simple versions
of these commands, sufficient for simple fonts, are standard operations
in plain METAFONT; examples have appeared in Chapter 11
and the beginning of Appendix E. The general cases are handled by
five types of font metric commands:
\beginsyntax
<font metric command>\is<ligtable command>
\alt<charlist command>
\alt<extensible command>
\alt<fontdimen command>
\alt<headerbyte command>
\endsyntax
This completes the syntax of METAFONT\ that was left slightly unfinished
in Chapter 26.

\endchapter

Such things induced me to untangle the chaos

by introducing order where it had never been before:

I think I may say I have had the good fortune to succeed

with an exactness \& a precision leaving nothing more to be desired,

by the invention of Typographic points.

> --- PIERRE , *Manuel Typographique* (1764)

One should absorb the color of life,
but one should never remember its details.
Details are always vulgar.

> --- OSCAR , *The Picture of Dorian Gray* (1890)


# Appendix G. Generic Font Files

METAFONT's main output goes into a or "Generic Font" file, so-called
because it can easily be translated into any other digital font format,
although it does not match the specifications of any "name brand"
manufacturer. The purpose of this appendix is to explain exactly what
kinds of information go into the 'gf' file, and under what circumstances
METAFONT\ puts things there.

A 'gf' file is a compact binary representation of a digitized font,
containing all the information needed by ""
software that produces printed documents from TeX's files. The
exact internal representation scheme of 'gf' files doesn't concern us
here, but we ought to know what type of data is encoded.

The first thing in a 'gf' file is a string that explains its origin.
METAFONT\ writes strings of the form

"'

METAFONT output 1986.06.24:1635

"'

based on the values of the internal quantities ^"day", ^"month",
^"year", and ^"time" when the 'gf' file was started. \ (In this case
$"day"=24$, $"month"=6$, $"year"=1986$,
and $"time"=16\times60+35=995$.)

After the opening string, the 'gf' file contains a sequence of
"special" commands interspersed with shipped-out character images.
are intended to provide a loophole for future
extensions to METAFONT's set of primitives, so that METAFONT\ itself will not
have to change. Some specials are predefined, but others will
undoubtedly be created in years to come. \ (TeX\ has an analogous
'\special' command, which puts an arbitrary string into a 'dvi' file.)

A special command gets into the 'gf' file when you say '^@special@
*string*' or '^@numspecial@ *numeric*' at a time when
^"proofing"$\ge0$. A @special@ string should come before
@numspecial@, and it
should either be a keyword all by itself or it should consist of a keyword
followed by a space followed by additional information. Keywords that
specify operations requiring numeric arguments should be followed by
numbers produced by @numspecial@. For example, the '^@proofrule@' macro
in Appendix B expands into a sequence of five special commands,

>
@special@ '"rule"';
@numspecial@ $x_1$; \ @numspecial@ $y_1$;
@numspecial@ $x_2$; \ @numspecial@ $y_2$;

this represents a rule on the proofsheet that runs from point $(x_1,y_1)$
to point $(x_2,y_2)$. If you say "grayfont gray5'', the ^@grayfont@
macro in Appendix B expands to '@special@ '"grayfont gray5"''.
Software that reads 'gf' files will examine all of the special strings,
until coming to a space or to the end of the string. If the resulting
keyword isn't known to the program, the special string will be ignored,
together with all numspecials that immediately follow. But when the
keyword is known, the program will be able to determine the corresponding
arguments. For example, the 'GFtoDVI' program described in Appendix H
knows about the plain METAFONT\ keywords "rule'' and "grayfont''.

METAFONT\ might also create @special@ commands on its own initiative, but only
when "proofing" is strictly greater than zero. There are
two cases: (1) When a ^*title* statement occurs,
the special string ""title "'\&*title*'
is output. \ (This is how the phrase "The letter O'' got onto your
proofsheets in the experiments of Chapter 5.) \ (2) Just before a
character image is shipped out, METAFONT\ implicitly executes the following
sequence of instructions:

>
@if@ round $"xoffset"<>0$: \ @special@ '"xoffset"'; \
@numspecial@ round ^"xoffset"; @fi@
@if@ round $"yoffset"<>0$: \ @special@ '"yoffset"'; \
@numspecial@ round ^"yoffset"; @fi@

A ^@shipout@ command sends a digitized picture to the 'gf'
file, if $"proofing"\ge0$, but nothing is output if $"proofing"<0$.
Furthermore the current values of ^"charwd", ^"charht", ^"chardp", ^"charic",
^"chardx", and ^"chardy" are stored away for the current ^"charcode";
these values are stored in all cases, regardless of the value of "proofing".
The current character code is henceforth said to "exist." ^^@charexists@

When a is shipped out, its pixels of positive value are
considered to be "black," and all other pixels are considered to be
"white." The pattern of blacks and whites is encoded in such a way
that doubling the resolution approximately doubles the length of the
'gf' output, in most cases.

METAFONT\ reports its progress by typing "['$c$']'' on the terminal
when character code $c$ is being shipped out. \ (The '' is typed
before output conversion begins, and the '' is typed after; hence you
can see how much time output takes.) \ If "charext" is nonzero, after
being rounded to an integer, the typed message is "['$c$'.'$x$']'' instead;
for example, "[65.3]'' refers to character 65 with extension code 3.

TeX\ allows only 256 characters per font, but extensions of TeX\
intended for languages will presumably use the "charext"
feature. All characters with the same code share the same width,
height, and depth, but they can correspond to distinct graphics if they have
different extension codes.

\medbreak
A @special@ command generally refers to the picture that follows it,
rather than the picture that precedes it. Special commands before the
first digitized picture might, however, give instructions about
the font as a whole. Special commands that follow the final picture
invariably refer to the font as a whole. \ (For example, the
'^@bye@' macro at the end of Appendix F creates two special
strings that will appear after the final character of a font.)

\medbreak
No 'gf' file will be written unless a character is shipped out or a
special command is performed at a time when $"proofing"\ge0$, or unless a
title statement is encountered at a time when $"proofing">0$. When one of
these things first happens, the 'gf' file receives its name. If no
^@input@ commands have yet occurred, METAFONT\ will set the job name to
''; otherwise the job name will already have been determined. The
full name of the 'gf' file will be
'*jobname*'.'*resolution*'gf'', where the *resolution* is
based on the current value of ^"hppp". \ (If $"hppp"\le0$, the resolution
will be omitted; otherwise it will be converted to an equivalent number of
pixels per inch, in the horizontal dimension.) \ Subsequent @input@
operations or changes to "hppp" will not change the
name of the 'gf' file.

\medbreak
The end of a 'gf' file contains a bunch of numeric data needed for
typesetting. First come the and the ;
these match precisely the data in the 'tfm' file, unless the header
bytes of the 'tfm' have explicitly been set to something else.
Then come the values of "hppp" and "vppp". \ (These are the values
at the end of the job, so "hppp" might not agree with the *resolution*
value in the 'gf' file name.)

Finally, the 'gf' file gets the ^"charwd", ^"chardx", and ^"chardy"
of each existing character code. The values of "chardx" and "chardy"
represent desired "escapements" when characters are typeset on a
particular device (cf.\ Chapter 12). The "charwd" values are identical to
the widths in the 'tfm' file.

\medbreak
The check sum is based entirely on the "charwd" data; two fonts
with the same character widths will have the same check sum, but
two fonts with different character widths will almost never have
the same check sum.

The purpose of check sums can be understood by considering the following
scenario: A font named 'cmr10' might be generated by METAFONT\ at any time,
producing a 'tfm' file called 'cmr10.tfm' and a 'gf' file called,
say, 'cmr10.300gf'. A document named 'doc', which uses 'cmr10',
might be generated by TeX\ at any time, producing a 'dvi' file
called 'doc.dvi'; TeX\ had to read 'cmr10.tfm' in order to
produce this 'dvi' file. Now on some future date, a ""
program will be used to print 'doc.dvi', using the font
'cmr10.300gf'. Meanwhile, the font may have changed.
If the current 'gf' file doesn't match the 'tfm' file that was assumed
by TeX, mysterious glitches will probably occur in the printed document,
because 'dvi' information is kept concise by the assumption that the
device driver knows the 'tfm' widths of all characters. Potential
problems are kept to a minimum if TeX\ puts the assumed design size
and check sum of each font into the 'dvi' files it produces;
a device driver can then issue a warning message when it finds a
'gf' file that is inconsistent with TeX's assumptions.

\endchapter

But if our Letter-Cutter will have no Forge,
yet he must of necessity accommodate himself
with a Vice, Hand-Vice, Hammers,
Files, Small and Fine Files (commonly
called Watch-makers Files)
of these he saves all, as they wear out.

> --- JOSEPH , *Mechanick Exercises* (1683)

The natural definition lists all possible generic characters.

> --- CAROLUS , *Philosophia Botanica* (1751)


# Appendix H. Hardcopy Proofs

A font cannot be proved correct like a mathematical theorem; a font must
be seen to be believed. Moreover, if some characters of a font are faulty,
the best way to fix them is to look at diagrams that indicate what went wrong.
Therefore METAFONT\ is incomplete by itself; additional programs are needed to
convert the output of METAFONT\ into graphic form.

The purpose of this appendix is to discuss two such auxiliary programs,
which serve as examples of many others that could be devised. The first
of these, called , takes 'gf' files and converts them into
files, which can be printed just like the output of TeX. Each
character image in the 'gf' file will have a printed page to itself, with
labeled points and with bounding boxes just as in the illustrations
we have seen throughout this book. \ (Indeed, the illustrations in this
book were produced by 'GFtoDVI'.) \ The second auxiliary program to
be discussed below is TeX\ itself; we shall look at a set of TeX\ macros
designed to facilitate font testing.

## Large scale proofs

The 'gf' files produced by plain METAFONT\
when it is in ^"proof" mode or ^"smoke" mode can be converted to
annotated diagrams by running them through 'GFtoDVI', as we know from
the experiments in Chapter 5. It's also possible to study low-resolution
characters with 'GFtoDVI', especially if plain METAFONT's
'' feature has been used.
We shall now take a thorough look at what 'GFtoDVI' can do.

All communication from METAFONT\ to 'GFtoDVI' comes through the 'gf' file and
from options that you might type when you run 'GFtoDVI'. If there are
no "" commands in the 'gf' file (cf. Appendix G), each page
of 'GFtoDVI''s output will show just the "black" pixels of a character;
furthermore there will be a title line at the top of the page, showing
the date and time of the METAFONT\ run, together with the character code
number and extension code (if they are nonzero). The black pixels are
typeset via characters of a so-called "," described in
detail below; by changing the gray font you can produce a variety of
different outputs from a single 'gf' file.

To get other things on your proof sheets, "special" commands must
appear in the 'gf' file. For example, METAFONT\ will automatically output
a 'title' command, if $"proofing">0$, as explained in Appendix G;
'GFtoDVI' will typeset this title on the title line of the next character
image that follows the command. If there are several title statements,
they all will appear; they are supposed to fit on a single line.

The most important special commands tell 'GFtoDVI' to create labeled
points on the character diagram. When you say, for example,
'^@labels@$(1,2)$' in a plain METAFONT\ program, at a time when
^"proofing"$>1$, the macros of Appendix B will convert this to the
special commands

>
@special@ '" 01"'; \ ^@numspecial@ $x_1$; \ @numspecial@ $y_1$;
@special@ '" 02"'; \ @numspecial@ $x_2$; \ @numspecial@ $y_2$;

'GFtoDVI' will then put a dot labeled "1'' at point $(x_1,y_1)$
and a dot labeled "2'' at $(x_2,y_2)$.

Labels are placed in one of four positions relative to their dots---
either at the top, the left, the right, or the bottom. 'GFtoDVI' will
ordinarily try to place all labels so that they don't interfere with
each other, and so that they stay clear of other dots.
But if you want to exercise fine control over the placement
yourself, you can say, for example, '@labels@."top"$(1a,2a)$'; in this
case the specified labels will appear above their dots, regardless of whether or
not other labels and/or dots are thereby overprinted. The 'gf' file
in this case will contain

>
@special@ '" 11a"'; \ @numspecial@ $x_1a$; \ @numspecial@ $y_1a$;
@special@ '" 12a"'; \ @numspecial@ $x_2a$; \ @numspecial@ $y_2a$.

'GFtoDVI' looks at the character following a leading blank space to
determine what sort of labeling convention is desired; the subsequent
characters are the text of the label.

The command '@labels@."top"$(1a,2a)$' in plain METAFONT\ is just an
abbreviation for '^@makelabel@."top"('"1a"'$,z_1a$);
@makelabel@."top"('"2a"'$,z_2a$)', when $"proofing">1$; the @makelabel@
macro is really the fundamental one, and you should use it directly if you
want more unusual effects. Suppose, for example, you just want to
put a dot but no label at point $z_5$; then you can say
'@makelabel@('""'$,z_5$)'. And suppose you want to put a label to the
left of point $z_5$ but with no dot; you can say
'@makelabel@."lft".^"nodot"('"5"'$,z_5$)'. Furthermore you could say
'@makelabel@."lft".^"nodot"('"5"'$,z_5-(2,3)$)' to move that label left
by 2 pixels and down by 3 pixels, thereby getting the effect of a label
that is diagonally adjacent to its dot. Labels without dots can also
be used to put words on a diagram.

'GFtoDVI' recognizes nine varieties of labels in all, based on the
first two characters of the special string command:

- @makelabel@ (special '" 0"'): choose the label position automatically.
- @makelabel@."top" (special '" 1"'): center the label just above
the dot.
- @makelabel@."lft" (special '" 2"'): place the label just left of
the dot.
- @makelabel@."rt" (special '" 3"'): place the label just right of
the dot.
- @makelabel@."bot" (special '" 4"'): center the label just below
the dot.
- @makelabel@."top"."nodot" (special '" 5"'): like "top", but omit
the dot.
- @makelabel@."lft"."nodot" (special '" 6"'): like "lft", but omit
the dot.
- @makelabel@."rt"."nodot" (special '" 7"'): like "rt", but omit
the dot.
- @makelabel@."bot"."nodot" (special '" 8"'): like "bot", but omit
the dot.

The first case is called *autolabeling*; this is the normal command.
Autolabeling always places a dot, whether or not that dot overlaps other dots,
but you don't always get a label. Autolabels are typeset only after
all explicit labels have been established; then 'GFtoDVI' tries to
place as many of the remaining labels as possible.

If there's no place to put an autolabel, an "" is
put in the upper right corner of the proofsheet. For example, the
overflow equation "5 = 5r + (-4.9,0)'' means that there was no room
for label '5', whose dot is 4.9 pixels to the left of the dot for '5r'
(which is labeled).

You can avoid overflow equations by sending 'GFtoDVI' the special command
'" /"' instead of '" 0"'; this is a variant of autolabeling that
does everything as usual except that the label will simply be forgotten if
it can't be placed. To do this with plain METAFONT\!, set
'$"lcode\_":=$'" /"'' near the beginning of your program; ^"lcode\_"
is the string that @makelabel@ uses to specify autolabeling.

The next most important kind of annotation for proofs is a straight line
or "." Plain METAFONT's command for this is '^@proofrule@$(z_1,z_2)$',
which expands to

>
@special@ '"rule"'; \ @numspecial@ $x_1$; \ @numspecial@ $y_1$;
@numspecial@ $x_2$; \ @numspecial@ $y_2$.

'GFtoDVI' has trouble drawing diagonal rules, because standard
format includes no provision for drawing straight lines unless they are
vertical or horizontal. Therefore you might get an error message
unless $x_1=x_2$ (vertical rule) or $y_1=y_2$ (horizontal rule).
However, a limited escape from this restriction is available via a
"," by which 'GFtoDVI' is able to typeset diagonal lines
as sequences of characters. Only one slope is permitted per job,
but this is better than nothing (see below).

To control the weight of proof rules, you say, e.g., '^@proofrulethickness@
1.5$"mm"\0$' in a plain METAFONT\ program; this expands to

>
@special@ '"rulethickness"'; \ @numspecial@ $1.5"mm"\0$.

Each horizontal or vertical rule is drawn as if by a pen of the current
rulethickness, hence you can get different weights of lines in a single
diagram. If the current rulethickness is negative, no rule will appear; if
it is zero, a default rulethickness based on a parameter of the gray font
will be used; if it is positive, the stated thickness will be increased if
necessary until it equals an integer number of pixels, and that value will
be used to draw the rule. At the beginning of each character the current
rulethickness is zero.

You can reposition an entire diagram on its page by saying '^@proofoffset@
$(x,y)$'; this expands to

>
@special@ '"offset"'; \ @numspecial@ $x$; \ @numspecial@ $y$

and it tells 'GFtoDVI' to shift everything except the title line on the
next character image, $x$ pixels to the right and $y$ pixels upward.

'GFtoDVI' uses four fonts to typeset its output: (1) The *title font* is used for the top line on each page.
(2) The label font is used for all labels.
(3) The gray font is used for dots and for black pixels.
(4) The slant font is used for diagonal rules.
Appropriate default fonts will be used at each installation unless
you substitute specific fonts yourself, by using the @special@ commands
^@titlefont@, ^@labelfont@, ^@grayfont@, or ^@slantfont@.
'GFtoDVI' also understands special strings like '|"grayfontarea
/usr/dek"|', which can be used to specify a nonstandard file area
or directory name for the gray font. Furthermore the 'gf' file might

say, e.g.,

>
@special@ '"labelfontat"'; \ @numspecial@ 20

if you want the label font to be loaded at $20\pt$ instead of its ^design
size. The area name and the at size must be given after the font name
itself; in other words, ""grayfont"'' cancels a previous
""grayfontarea"''.

The four fonts used by 'GFtoDVI' must be established before the first
character bitmap appears in the 'gf' file. This means that the special font
commands must be given before the first ^@shipout@ or ^@endchar@ in your
program; but they shouldn't appear until after ^@mode\_setup@, so that
your 'gf' file will have the correct name. If it's inconvenient to
specify the fonts that way, you can change them at run time when
you use 'GFtoDVI': Just type '' following the name of the 'gf' file
that's being input, and you will be asked to type special strings online.
For example, the run-time dialog might look like this:

"'

This is GFtoDVI, Version 2.0
GF file name: io.2602gf/
Special font substitution: labelfont cmbx10
OK; any more? grayfont black
OK; any more?

"'

After the final carriage return, 'GFtoDVI' does its normal thing,
ignoring font specifications in the file that conflict with those
just given.

##

A proof diagram constructed by 'GFtoDVI' can
be regarded as an array of rectangles, where each rectangle is either
blank or filled with a special symbol that we shall call '{\manual R}'. A
blank rectangle represents a white pixel, while {\manual R} represents a
black pixel. Additional labels and reference lines are often superimposed
on this array of rectangles; hence it is usually best to choose a symbol
{\manual R} that has a somewhat gray appearance, although any symbol can
actually be used.

In order to construct such proofs, 'GFtoDVI' needs to work with
a special type of font known as a "gray font"; it's possible to
obtain a wide variety of different sorts of proofs by using different
sorts of gray fonts. The next few paragraphs explain exactly what gray
fonts are supposed to contain, in case you want to design your own.

The simplest gray font contains only two characters, namely {\manual R}
and another symbol that is used for dots that identify key points.
If proofs with relatively large pixels are desired, a two-character
gray font is all that's needed. However, if the pixel size is to be
relatively small, practical considerations make a two-character
font too inefficient, since it requires the typesetting of tens
of thousands of tiny little characters; printing-device drivers
rarely work very well when they are presented with data that is
so different from ordinary text. Therefore a gray font with small
pixels usually has a number of characters that replicate {\manual R} in
such a way that comparatively few characters actually need to be
typeset.

Since many printing devices are not able to cope with
arbitrarily large or complex characters, it is not possible for a
single gray font to work well on all machines. In fact,
{\manual R} must have a width that is an integer multiple of the printing
device's units of horizontal and vertical positioning,
since rounding the positions of grey
characters would otherwise produce unsightly streaks on proof output.
Thus, there is no way to make the gray font as device-independent as
normal fonts of type can be.

This understood, we can now take a look at what 'GFtoDVI' expects to
see in a gray font. The character {\manual R} always appears in position 1. It
must have positive height $h$ and positive width $w$; its depth
and italic correction are ignored.

Positions 2--120 of a gray font are reserved for special combinations of
{\manual R}'s and blanks, stacked on top of each other. None of these
character codes need be present in the font; but if they are, the slots
must be occupied by characters of width $w$ that have certain
configurations of {\manual R}'s and blanks, prescribed for each character
position. For example, position 3 of the font should either contain no
character at all, or it should contain a character consisting of two
{\manual R}'s, one above the other; one of these {\manual R}'s should rest
on the baseline, and the other should appear immediately below.

It will be convenient to use a horizontal notation like '{\manual RSRRS}'
to stand for a vertical stack of {\manual R}'s and blanks. The convention
will be that the stack is built from bottom to top, and the topmost
rectangle should sit on the baseline. Thus, '{\manual RSRRS}' stands
actually for a character of height $h$ and depth $4h$ that looks like this:

>
{\offinterlineskip{\manual#
\phantomR
R\smash{{.5pt{$\longleftarrow$ baseline}}}
R
\phantomR
R
}}

We use a horizontal notation in this discussion instead of a vertical one
because column vectors take too much space, and because the horizontal
notation corresponds to binary numbers in a convenient way.

Positions 1--63 of a gray font are reserved for the patterns {\manual R},
{\manual RS}, {\manual RR}, {\manual RSS}, {\manual RSR}, and so on up to
{\manual RRRRRR}, just as in the normal binary notation of the numbers
1--63, with {\manual R}'s substituted for 1's and blanks for 0's.
Positions 64--70 are reserved for the special patterns {\manual RSSSSSS},
{\manual RRSSSSS}, {\manual RRRSSSS}, {\manual RRRRSSS}, {\manual
RRRRRSS}, {\manual RRRRRRS}, {\manual RRRRRRR} of length seven; positions
71--78 are, similarly, reserved for the length-eight patterns {\manual
RSSSSSSS} through {\manual RRRRRRRR}. The length-nine patterns {\manual
RSSSSSSSS} through {\manual RRRRRRRRR} are assigned to positions 79--87,
the length-ten patterns to positions 88--97, the length-eleven patterns to
positions 98--108, and the length-twelve patterns to positions 109--120.

Position 0 of a gray font is reserved for the "dot" character, which
should have positive height $h'$ and positive width $w'$. When 'GFtoDVI'
wants to put a dot at some place $(x,y)$ on the figure, it positions
the dot character so that its reference point is at $(x,y)$. The
dot will be considered to occupy a rectangle whose corners are at
$(x\pm w',y\pm h')$; the rectangular
box for a label will butt up against the rectangle enclosing the dot.

All other character positions of a gray font (namely, positions 121--255)
are unreserved, in the sense that they have no predefined meaning.
But 'GFtoDVI' may access them via the ^@charlist@ feature of
'tfm' files, starting with any of the characters in positions
1--120. In such a case each succeeding character in a list should be
equivalent to two of its predecessors, horizontally adjacent to each other.
For example, in

>
@charlist@ 53: 121: 122: 123

character 121 will stand for two 53's, character 122 for two 121's (i.e.,
four 53's), and character 123 for two 122's (i.e., eight 53's). Since
position 53 contains the pattern {\manual RRSRSR}, character 123 in this example
would have height $h$, depth $5h$, and width $8w$, and it would stand for
the pattern

>
{\offinterlineskip{\manual#
RRRRRRRR
\phantomSSSSSSSS
\smash{{.5pt{$\longleftarrow$ baseline}}}
RRRRRRRR
\phantomSSSSSSSS
RRRRRRRR
RRRRRRRR
}}

Such a pattern is, of course, rather unlikely to occur in a 'gf' file,
but 'GFtoDVI' would be able to use if it were present. Designers
of gray fonts should provide characters only for patterns that they think
will occur often enough to make the doubling worthwhile. For example,
the character in position 120 ({\manual RRRRRRRRRRRR}), or whatever is the
tallest stack of {\manual R}'s present in the font, is a natural candidate for
repeated doubling.

Here's how 'GFtoDVI' decides what characters of the gray font will be used,
given a configuration of black and white pixels: If there are no black
pixels, stop. Otherwise look at the top row that contains at least one
black pixel, and the eleven rows that follow. For each such column,
find the largest $k$ such that $1\leq k\leq120$ and the gray font contains
character $k$ and the pattern assigned to position $k$ appears in the
given column. Typeset character $k$ (unless no such character exists)
and erase the corresponding black pixels; use doubled characters,
if they are present in the gray font, if two or more consecutive equal
characters need to be typeset. Repeat the same process on the remaining
configuration, until all the black pixels have been erased.

If all characters in positions 1--63 are present, this process is guaranteed to
take care of at least six rows each time; and with characters 64--120 as well,
it usually takes care of twelve, since all patterns that contain at most
one "run" of {\manual R}'s are present.

Some of the ^@fontdimen@ parameters discussed in Appendix F are important
in gray fonts. The ^@font\_slant@ value $s$, if nonzero, will cause
'GFtoDVI' to skew its output; in this case the character {\manual R} will
presumably be a parallelogram with a corresponding slant, rather than the
usual rectangle. METAFONT's coordinate $(x,y)$ will appear in physical position
$(xw+yhs,yh)$ on the proofsheets. \ (This is appropriate for proofing unslanted
fonts whose pixels will become slanted by mechanical obliquing.)

Parameter @fontdimen@ 8 of a gray font specifies the thickness of rules
that go on the proofs. If this parameter is zero, TeX's default
rule thickness (0.4 pt) will be used.
The other parameters of a gray font are ignored by 'GFtoDVI', but
it is conventional to set ^@font\_normal\_space@ and ^@font\_quad@ to $w$,
^@font\_x\_height@ to $h$.

For best results the designer of a gray font should choose $w$ and $h$
so that the user's 'dvi'-to-hardcopy software will not make any
rounding errors. Furthermore, the dot should be an even number $2m$ of
pixels in diameter, and the rule thickness should work out to an
even number $2n$ of pixels; then the dots and rules will be centered on
the correct positions, in the common case of integer coordinates. Gray fonts
are almost always intended for particular output devices, even though
"dvi'' stands for "device independent"; we use 'dvi' files for METAFONT\
proofs chiefly because software to print 'dvi' files is already in place.

The METAFONT\ program for a fairly versatile gray font generator, called
'', appears on the next few pages. It should be invoked by a
parameter file that establishes values of several quantities:

- If ^"large\_pixels" is of type @boolean@, only 15 characters
will be generated; otherwise there will be 123.
- If ^"pix\_picture" is of type @picture@, it should be the
desired pixel image '{\manual R}', and in this case ^"pix\_wd" and
^"pix\_ht" should be the width and height in pixels. Otherwise a default
gray pixel pattern will be used.
- If ^"rep" is known, it should be a positive integer; the default
pixel pattern will be replicated so that the final
proofs will be "rep" times bigger than usual, and the pattern will be clipped
slightly at the edges so that discrete pixels can be seen plainly.
- If ^"lightweight" is of type @boolean@, the default pixel
pattern will be only half as dark as usual.
- If ^"dotsize" is known, it should be the diameter of the
special dot character, in pixel units.
- The ^@font\_identifier@ should be specified.

(The "rep" and "lightweight" options are ignored if "pix\_picture" is
explicitly given.) \
Since gray fonts are inherently device-dependent, we do not start
with "sharp" dimensions as in normal fonts; we go backwards and
compute the sharp units from pixel units.

The name of each gray font should include the name of the device for
which it is intended. \ (A "favorite" proof device can also be chosen
at each installation, for which the alternate font names ''
and '' are valid; these installation-dependent fonts are the
defaults for "proof" mode and "smoke" mode.)

Here, for example, is a suitable parameter file "graycheap.mf'', which
generates a vanilla-flavored gray font for the hypothetical "cheapo"
printer:
\beginlines
|

'if mode<>cheapo: errmessage "This file is for cheapo only"; fi'

'font_identifier "GRAYCHEAP";'
'input grayf'
\endlines
(The proofsheet resolution will be 50 pixels per inch, because "cheapo" has
200 pixels per inch, and the default "pix\_picture" in 'grayf'
will be four pixels square in this case.) \ If the default pixel pattern
turns out to be such a dark gray that the labels and rules are obscured,
the statement "boolean lightweight'' should be added. A solid black font
with slightly higher-resolution images can be generated by the following
file "blackcheap.mf'':
\beginlines
|

'if mode<>cheapo: errmessage "This file is for cheapo only"; fi'

'picture pix_picture; pix_wd := pix_ht := 3;'
'pix_picture := unitpixel scaled 3;'

'font_identifier "BLACKCHEAP";'
'input grayf'
\endlines
And here is a file "graycheap5.mf'' that generates a gray font suitable
for studying large proofs of low-resolution characters:
\beginlines
|

'if mode<>cheapo: errmessage "This file is for cheapo only"; fi'

'rep=5; boolean large_pixels;'

'font_identifier "GRAYCHEAP";'
'input grayf'
\endlines

Now let's look at the program file "grayf.mf'' itself. It begins with
a simple test to ensure that "mag" and "rep" are positive integers, if
they're known; then comes some less obvious code that handles
magnification in a nonstandard way:
\beginlines
|
|

'forsuffixes m = mag,rep:'
' if unknown m: m := 1;'
' elseif (m<1) or (m<>floor m):'
' errmessage "Sorry, " & str m & " must be a positive integer";'
' m := 1; fi endfor'
break
'mg := mag; mag := 1; mode_setup;'
'if mg>1: hppp := hppp*mg; vppp := vppp*mg;'
' extra_endchar:='
' "if charcode>0:currentpicture:=currentpicture scaled mg;fi;"'
' & extra_endchar; fi;'
\endlines
This circumlocution is the easiest way to guarantee that the file
will be completely unaffected by magnification.

The next part of 'grayf' computes the pixel representation, "pix\_picture".
\beginlines
'if picture pix_picture: rep := 1;'
' cull pix_picture keeping (1,infinity);'
'else: for z=(0,2),(1,0),(2,3),(3,1):'
' fill unitsquare shifted z; endfor'
' if not boolean lightweight:'
' addto currentpicture also'
' currentpicture rotated 90 xscaled -1; fi'
' if unknown scale: scale := max(1,round(pixels_per_inch/300)); fi'

' if rep>1: picture pix;'
' currentpicture := currentpicture shifted-(1,1); pix := currentpicture;'
' for r=1 upto rep-1: addto currentpicture also pix shifted(4r,0); endfor'
' cullit; pix := currentpicture;'
' for r=1 upto rep-1: addto currentpicture also pix shifted(0,4r); endfor'
' unfill unitsquare xscaled 4rep yscaled 2 shifted-(1,1);'
' unfill unitsquare yscaled 4rep xscaled 2 shifted-(1,1); cullit; fi'
' picture pix_picture; pix_picture := currentpicture scaled scale;'
' pix_wd := pix_ht := 4scale*rep; fi'
\weakendlines
The lightweight pattern has 4 of every 16 pixels turned on; the normal
pattern has twice as many.

Character 0 is the dot, which is quite simple:
\beginlines
'def # = *72.27/pixels_per_inch enddef;'
'if unknown dotsize: dotsize := 2.5pix_wd/rep; fi'

'beginchar(0,1.2dotsize#,1.2dotsize#,0);'
'fill fullcircle scaled dotsize scaled mg; endchar;'
\endlines

The special coding scheme of gray fonts is implemented next:
\beginlines
'numeric a[]; newinternal b,k;'
'def next_binary ='
' k := 0; forever: if k>b: a[incr b] := 0; fi'
' exitif a[k]=0; a[k] := 0; k := k+1; endfor'
' a[k] := 1 enddef;'
'def next_special_binary ='
' if a[0]=1: for k=0 upto b: a[k] := 0; endfor a[incr b]'
' else: k := 0; forever: exitif a[incr k]=1; endfor'
' a[k-1] fi := 1 enddef;'
break
'def make_char ='
' clearit; next_binary;'
' for k=0 upto b: if a[k]=1:'
' addto currentpicture also pix_picture shifted(0,-k*pix_ht); fi endfor'
' charcode := charcode+1; chardp := b*charht;'
' scantokens extra_endchar; shipout currentpicture enddef;'
\endlines

Now we are ready to generate all the pixel characters.
^^@charlist@^^"chardx"^^"charwd"^^"charht"
\beginlines
'charwd := pix_wd#; charht := pix_ht#; chardx := pix_wd*mg;'
'b := -1;'

'if boolean large_pixels:'
' for k=1 upto 7: make_char; charlist k:k+120; endfor'
' charcode := 120; b := -1;'
' addto pix_picture also pix_picture shifted (chardx,0);'
' charwd := 2charwd; chardx := 2chardx;'
' for k=1 upto 7: make_char; endfor'
'else: for k=1 upto 63: make_char; endfor'
' let next_binary = next_special_binary;'
' for k=64 upto 120: make_char; endfor'
' for k=121,122: charcode := k;'
' addto currentpicture also currentpicture shifted (chardx,0);'
' charwd := 2charwd; chardx := 2chardx;'
' scantokens extra_endchar; shipout currentpicture; endfor'
' charlist 120:121:122; fi'
\endlines

The program closes by establishing fontwide parameters:
\beginlines
'font_coding_scheme "GFGRAY";'
'font_size 8(pix_wd#);'
'font_normal_space pix_wd#;'
'font_x_height pix_ht#;'
'font_quad pix_wd#;'
'fontdimen 8: if known rulethickness: rulethickness'
' else: pix_wd#/(2rep) fi;'
'bye.'
\weakendlines
(The extra complications of an ^"aspect\_ratio" or a slant have not
been addressed.)

##

'GFtoDVI' also makes use of another special
type of font, if it is necessary to typeset slanted rules. The format of
such so-called "slant fonts" is quite a bit simpler than the format of
gray fonts.

A slant font contains exactly $n$ characters, in positions 1 to $n$,
for some positive integer $n$.
The character in position $k$ represents a slanted line $k$ units
tall, starting at the baseline. These lines all have a fixed slant ratio $s$.
The vertical "unit" is usually chosen to be an integral number of pixels,
small enough so that it suffices to draw rules that are an
integer number of units high; in fact, it should probably be no larger
than the thickness of the rules being drawn.

The following simple algorithm is used to typeset a rule that is $m$ units
high: Compute $q=\lceil m/n\rceil$; then typeset $q$ characters of
approximately equal size, namely $(m\bmod q)$ copies of character number
$\lceil m/q\rceil$ and $q-(m\bmod q)$ copies of character number
$\lfloor m/q\rfloor$. For example, if $n=15$ and $m=100$, we have $q=7$;
a 100-unit-high rule will be composed of 7 pieces, using characters
14, 14, 14, 14, 14, 15, 15.

'GFtoDVI' looks at the ^"charht" of character $n$ only, so the 'tfm' file
need not be accurate about the heights of the other characters. \ (This is
fortunate, since format allows at most 15 different nonzero
heights per font.)

The ^"charwd" of character $k$ should be $k/n$ times $s$ times the "charht"
of $n$.

The ^@font\_slant@ parameter should be $s$. It is customary to
set the parameter @fontdimen@ 8 to the thickness of
the slanted rules, but 'GFtoDVI' doesn't look at it.

Here's an example of a slant-font parameter file, "slantcheap6'',
for the "cheapo" printer and a slant of 1/6:
\beginlines
|

'if mode<>cheapo: errmessage "This file is for cheapo only"; fi'

|s=1/6;
|n=30;
|r#=.4pt#;
|u=1;

'font_identifier "SLANTCHEAP6";'
'input slant'
\endlines
The corresponding program file "slant.mf'' looks like this:
\beginlines
|
|
|
|
|
|

'if unknown mag: mag := 1;'
'elseif (mag<1) or (mag<>floor mag):'
' errmessage "Sorry, mag must be a positive integer"; mag := 1; fi'
break
'mg := mag; mag := 1; mode_setup; u# := u*72.27/pixels_per_inch;'
'pixels_per_inch := pixels_per_inch*mg; fix_units;'
break
'define_whole_pixels(u); define_blacker_pixels(r);'
'pickup pencircle scaled r; ruler := savepen;'
break
'for k=1 upto n:'
' beginchar(k,k*u#*s,n*u#,0);'
| pickup ruler; draw origin--(k*u*s,k*u);
' unfill (lft -1,bot -1)--(rt 1,bot -1)'
| --(rt 1,0)--(lft -1,0)--cycle;
' unfill ((lft -1,0)--(rt 1,0)'
' --(rt 1,top 1)--(lft -1,top 1)--cycle) shifted (k*u*s,k*u);'
' endchar; endfor'
break
'font_size 16pt#;'
'font_slant s;'
'fontdimen 8: r#;'
'font_coding_scheme "GFSLANT";'
'bye.'
\endlines

## Font samples

The real test of a font is its appearance
at the final size, after it has actually been typeset. The TeX\
typesetting system can be used with the following example macro file
'' (in addition to plain TeX\ format) to
put a new font through its paces.

We shall comment on typical uses of 'testfont' as we examine its parts.
At the beginning, 'testfont.tex' turns off several of TeX's normal features.
\beginlines
|

|\tracinglostchars=0
|\tolerance=1000
|\raggedbottom
|\nopagenumbers
|indent=0pt
|\hyphenpenalty=200
|\doublehyphendemerits=30000

|\newlinechar='@
|\chardef\other=12

|\newcount\m \newcount\n \newcount\p \newdimen\dim
\endlines

Then there are macros to print the time and date---an extremely valuable
thing to have on any proofsheet.
\beginlines
'\def{\ifcase\month\or'
' January\or February\or March\or April\or May\or June\or'
' July\or August\or September\or October\or November\or December\fi'
' \space\day, \year}'
'\def\hours{\n=\time \n 60'
' \m=-\n \m 60 \m \time'
' \twodigits\n\twodigits\m}'
'\def\twodigits#1{\ifnum #1<10 0\fi #1}'
\endlines

An online "menu" of the available test routines will be typed at your
terminal if you request '\help'.
\beginlines
'{\catcode'\'\"=0 \catcode'\\=\other
\"gdef'\"help{'\"message{
|\init switches to another font;@
|\end or e finishes the run;@
|\table prints the font layout in tabular format;@
|\text prints a sample text, assuming TeX text font conventions;@
|\sample combines \table and \text;@
|\mixture mixes a background character with a series of others;@
|\alternation interleaves a background character with a series;@
|\alphabet prints all lowercase letters within a given background;@
|\ALPHABET prints all uppercase letters within a given background;@
|\series prints a series of letters within a given background;@
|s prints a comprehensive test of lowercase;@
|\uppers prints a comprehensive test of uppercase;@
|\digits prints a comprehensive test of numerals;@
|\math prints a comprehensive test of TeX math italic;@
|\names prints a text that mixes upper and lower case;@
|\punct prints a punctuation test;@
|\bigtest combines many of the above routines;@
|\help repeats this message;@
'and you can use ordinary TeX commands (e.g., to \input a file).}}}'
\endlines

The program prompts you for a font name. If the font is in your local
directory instead of a system directory, you might have to
specify the directory name as part of the font name. You should
also specify scaling if the font has been magnified, as in the example
of Chapter 5. Several fonts can be tested during a single run, if you
say "\init'' before "\end''.
\beginlines
'\def\init{\message@Name of the font to test = '
' \read-1 to\fontname \startfont'
' \message{Now type a test command (\string\help\space for help):}}'
'\def\startfont{\font\testfont=\fontname \spaceskip=0pt'
' {\sevenrm Test of \fontname\ on \ at \hours}'
' '
' \testfont \setbaselineskip'
' \ifdim\fontdimen6\testfont<10pt \rightskip=0pt plus 20pt'
' \else\rightskip=0pt plus 2em \fi'
| \spaceskip=\fontdimen2\testfont
' \xspaceskip=\fontdimen2\testfont'
' \xspaceskip by\fontdimen7\testfont}'
\endlines
The specified font will be called '\testfont'. As soon as you have
specified it, '\init' calls on '\startfont', which puts a title line
on the page; then it chooses what it hopes will be a good distance between
baselines, and gets ready to typeset text with "" margins.
\ (The code above improves on plain TeX's .)

The baselineskip distance is taken to be $6\pt$ plus the height of the
tallest character plus the depth of the deepest character. This is the
distance between baselines for "series" tests, but it is decreased
by $4\pt$ when the sample text is set. If you
want to change the baseline distance chosen by 'testfont',
you can just say, e.g., "=11pt''.
\beginlines
'\def\setbaselineskip{={\n=0'
|\loop\char\n \ifnum \n<255 \n 1 \repeat}
'=6pt }'
\endlines

When 'testfont' prompts you for a ""
or a "" or an "," you
can type the character you want (assuming ASCII code);
or you can say, e.g., "#35'' to get character code number 35.
Codes 0--32 and 127--255 have to be specified with the "#'' option,
on non-fancy installations of TeX,
and so does code 35 (which is the ASCII code of "#'' itself).
\beginlines
|\def\setchar#1{{\escapechar-1\message{\string#1 character = }
' \def\do##1{\catcode'##1=\other}\dospecials'
' \read-1 to\next'
' \expandafter\finsetchar\next\next#1}}'
'\def\finsetchar#1#2\next#3{\global\chardef#3='#1'
' \ifnum #3='\# \global\chardef#3=#2 \fi}'
'\def\promptthree{\setchar\background'
' \setchar\starting \setchar\ending}'
\endlines
(The TeX\ hackery here is a bit subtle, because special characters
like "\'' and "$'' must temporarily lose their special significance.)

Suppose the background character is "o'' and the starting and ending
characters are respectively "p'' and "q''. Then the
operation will typeset "opooppooopppop'' and "oqooqqoooqqqoq'';
the operation will typeset "opopopopopopopopo'' and
"oqoqoqoqoqoqoqoqo''. Other patterns could be added in a similar way.
\beginlines
'\def\mixture{\promptthree \domix\mixpattern}'
'\def\alternation{\promptthree \domix\altpattern}'
'\def\mixpattern{\0\1\0\0\1\1\0\0\0\1\1\1\0\1}'
'\def\altpattern{\0\1\0\1\0\1\0\1\0\1\0\1\0\1\0\1\0}'
'\def\domix#1{\chardef\0=\background \n=\starting'
' \loop \chardef\1=\n #1\endgraf'
' \ifnum \n<\ending \n 1 \repeat}'
\endlines

The '\series' operation puts the background character between all the
others (e.g., "opoqo''). Special series containing the lowercase
letters of TeX\ text fonts (including '', '',
'', and '') and the uppercase letters (including
'', '', and '') are provided.
Although '\mixture' and '\alternation' show you the effects of
ligatures and kerning, '\series' does not.
\beginlines
'\def\!{\discretionary{\background}{\background}{\background}}'
'\def\series{\promptthree \!\doseries\starting\ending}'
'\def\doseries#1#2{\n=#1\loop\char\n\!\ifnum\n<#2\n 1 \repeat}'
'\def\complower{\!\doseries'a'z\doseries'31'34}'
'\def\compupper{\!\doseries'A'Z\doseries'35'37}'
'\def\compdigs{\!\doseries'0'9}'
'\def\alphabet{\setchar\background\complower}'
'\def\ALPHABET{\setchar\background\compupper}'
\endlines
(A long series might fill more than one line; TeX's '\discretionary'
break operation is used here so that the background character will end
the line and be repeated at the beginning of the next.)

A "comprehensive" test uses a series of background characters
against a series of others. The series will consist of lowercase
letters (''), uppercase letters (''), or
numerals ('').
\beginlines
'\defs{\docomprehensive\complower'a'z'31'34}'
'\def\uppers{\docomprehensive\compupper'A'Z'35'37}'
'\def\digits{\docomprehensive\compdigs'0'4'5'9}'
'\def\docomprehensive#1#2#3#4#5{\chardef\background=#2'
' \loop#1 \ifnum\background<#3\m=\background\m 1'
' \chardef\background=\m \repeat \chardef\background=#4'
' \loop#1 \ifnum\background<#5\m=\background\m 1'
' \chardef\background=\m \repeat}'
\endlines

The test puts uppercase letters and accents
together with lowercase letters. The accents will look funny
if the test font doesn't have them in plain TeX's favorite positions.
\beginlines
'\def\names{ {\AA}ngel\aa\ Beatrice Claire'
' Diana \'Erica Fran\ccoise Ginette H\'el\'ene Iris'
' Jackie K\=aren {\L}au\.ra Mar{\'\i}a N\Hata{\l}{\u\i}e {\O}ctave'
' Pauline Qu\^eneau Roxanne Sabine T\ a{\'\j}a Ur\vsula'
' Vivian Wendy Xanthippe Yv{\o}nne Z\"azilie}'
\endlines

Punctuation marks are tested in juxtaposition with different
sorts of letters, by the '' macro:
\beginlines
'\def\punct{\dopunctmin\dopunctpig\dopuncthid'
' \dopunctHIE\dopunctTIP\dopunctfluff'
' \$1,234.56 + 7/8 = 9\% @ \#0}'
'\def\dopunct#1{#1,\ #1:\ #1;\ '#1'\'
' ?"'#1?\ !"'#1!\ (#1)\ [#1]\ #1*\ #1.}'
\endlines

Mixtures and alternations and series are excellent ways to discover
that letters are too dark, too light, or too tightly spaced. But
a font also has to be readable; in fact, this is the number one
objective. So 'testfont' provides a sample ''. One of the sentences
is optional, because it contains lots of accents and unusual letters;
you can omit it from the text by saying ''.
Furthermore, you can type your own text, online, or you can input one from

a file, instead of using this canned example.
\beginlines
'\def\text{{-4pt'
'=abcdefghijklmnopqrstuvwxyz'
'\ifdim>2 \ifdim 15pc>2 =15pc \else=2 \fi\fi'
'On November 14, 1885, Senator \& Mrs. Leland Stanford called together at'
'their San Francisco mansion the 24 prominent men who had been chosen as'
'the first trustees of The Leland Stanford Junior University. They'
'handed to the board the Founding Grant of the University, which they had'
'executed three days before. This document---with various amendments,'
'legislative acts, and court decrees---remains as the University's'
'charter. In bold, sweeping language it stipulates that the objectives of'
'the University are "to qualify students for personal success and direct'
'usefulness in life; and to promote the publick welfare by exercising an'
'influence in behalf of humanity and civilization, teaching the blessings'
'of liberty regulated by law, and inculcating love and reverence for the'
'great principles of government as derived from the inalienable rights of'
'man to life, liberty, and the pursuit of happiness." \moretext'
'(!"'THE DAZED BROWN FOX QUICKLY GAVE 12345--67890 JUMPS!)}}'
'\def\moretext{?"'But aren't Kafka's Schlo{\ss} and {\AE}sop's {\OE}uvres'
'often na{\"\i}ve vis-\'a-vis the d{\ae}monic ph{\oe}nix's official'
'r\^ole in fluffy souffl\'es? }'
'\def\omitaccents{\let\moretext=}'
\endlines

Now comes one of the hardest parts of the file, from the TeX\
standpoint: The '\table' macro prints a font diagram, omitting
groups of sixteen characters that are entirely absent from the font.
The format of this table is the same as that used in Appendix F
of *The TeX book*. When the font contains unusually large characters
that ought to be vertically centered, you should say ''
before "\table''. \ (A TeX\ math symbol font or math extension font
would use this feature.)
\beginlines
|\def\oct#1{{\'#1}}
|\def\hex#1{{\H#1}}
|\def\setdigs#1"#2{\gdef\h#2
| \m=\n \m by 64 \xdef\0{\the\m}
' \m by-64 \m by\n \m by 8 \xdef\1{\the\m}}'
|\def\testrow{={\penalty 1\def\\{\char"\h}
| \\0\\1\\2\\3\\4\\5\\6\\7\\8\\9\\A\\B\\C\\D\\E\\F
| \global\p=\lastpenalty}}
'\def\oddline{'
' {\nointerlineskip}'
' \multispan19\hrulefill&'
' ={ 2.3pt{\hex{\h x}}}\smash{\box0}'
' {\nointerlineskip}}'
'\newif\ifskipping'
'\def\evenline{\loop\skippingfalse'
' \ifnum\n<256 \m=\n \m 16 \chardef\next=\m'
' \expandafter\setdigs\meaning\next \testrow'
' \ifnum\p=1 \skippingtrue \fi\fi'
' \ifskipping \global\n 16 \repeat'
' \ifnum\n=256 \let\next=\endchart\else\let\next=\morechart\fi'
' \next}'
'\def\morechart{{\hrule\penalty5000}'
' \chartline \oddline \m=\1 \m 1 \xdef\1{\the\m}'
' \chartline \evenline}'
'\def\chartline{&\oct{\0\1x}&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&\:&&}'
'\def\chartstrut4.5pt to14pt'
'\def\table{$$\global\n=0'
' to'
' \chartstrut##0pt plus10pt&'
' &##&\vrule##'
' 6.5pt'
' &&&\oct0&&\oct1&&\oct2&&\oct3&&\oct4&&\oct5&&\oct6&&\oct7&\evenline}'
'\def\endchart{{\hrule}'
' 11.5pt&&&\hex 8&&\hex 9&&\hex A&&\hex B&'
' &\hex C&&\hex D&&\hex E&&\hex F&$$}'
|\def\:{={\noboundary\char\n\noboundary}
' \ifdim>7.5pt\reposition'
' \else\ifdim>2.5pt\reposition\fi\fi'
' \box0\global\n 1 }'
'\def\reposition{={\box0}\dim='
' \dim 2pt =\dim}'
'\def\centerlargechars{'
' \def\reposition{={$\vcenter{\box0}$}}}'
\endlines

Two of the most important combinations of tests are treated now:
prints the '\table' and the '\text'; gives
you the works, plus a mysterious word that is traditional in type
specimens:
\beginlines
'\def\sample{\table\text}'

'\def\bigtest{\sample'
' hamburgefonstiv HAMBURGEFONSTIV'
' \names \punct s \uppers \digits}'
\endlines

Finally, there's a '\math'
routine useful for checking out the spacing in the
fonts used by plain TeX; '\mathsy' does a similar thing for the
uppercase letters in a math symbols font.
\beginlines
'\def\math{=\testfont \testfont=\skewtrial'
' \Gamma="100 \Delta="101'
' \Theta="102 \Lambda="103 \Xi="104'
' \Pi="105 \Sigma="106 \Upsilon="107'
' \Phi="108 \Psi="109 \Omega="10A'
' \def\iii \def\jjj'
' \def\\##1{'\"##1'\"+}\mathtrial'
' \def\\##1{##1_2+}\mathtrial'
' \def\\##1{##1^2+}\mathtrial'
' \def\\##1##1/2+\mathtrial'
' \def\\##12/##1+\mathtrial'
' \def\\##1##1,+\mathtrial'
' \def\\##1d##1+\mathtrial'
' \let\ii=\imath \let\jj=\jmath \def\\##1{\hat##1+}\mathtrial}'
'\newcount\skewtrial \skewtrial='177'
'\def\mathtrial{$\\A \\B \\C \\D \\E \\F \\G \\H \\I \\J \\K \\L \\M \\N'
' \\O \\P \\Q \\R \\S \\T \\U \\V \\W \\X \\Y \\Z \\a \\b \\c \\d \\e \\f'
' \\g \\h \\\ii \\\jj \\k \\l \\m \\n \\o \\p \\q \\r \\s \\t \\u \\v \\w'
' \\x \\y \\z \\\alpha \\\beta \\\gamma \\\delta \\\epsilon \\\zeta'
' \\\eta \\\theta \\\iota \\\kappa \\\lambda \\\mu \\\nu \\\xi \\\pi'
' \\\rho \\\sigma \\\tau \\\upsilon \\\phi \\\chi \\\psi \\\omega'
' \\\vartheta \\\varpi \\\varphi \\\Gamma \\\Delta \\\Theta \\\Lambda'
' \\\Xi \\\Pi \\\Sigma \\\Upsilon \\\Phi \\\Psi \\\Omega'
' \\tial \\\ell \\\wp$}'
|\def\mathsy{\skewtrial='060
' \def\mathtrial{$\\A \\B \\C \\D \\E \\F \\G \\H \\I \\J \\K \\L'
' \\M \\N \\O \\P \\Q \\R \\S \\T \\U \\V \\W \\X \\Y \\Z$}'
' \math}'
\endlines

The last line of 'testfont' is
\beginlines
'\ifx\noinit!\else\init\fi'
\endlines
and it means "automatically call '' unless "\noinit'' is
an exclamation point." Why this? Well,
you might have your own test file from which you'd like to use the
facilities of 'testfont', without typing commands online.
If your file says "\let\noinit!' '\input testfont'' TeX\ will
read in 'testfont' but the routine will not prompt you for a file name.
The file can then continue to test one or more fonts by saying, e.g.,
\beginlines
'\def\fontnamecmbx10 \startfont\sample'
'\def\fontnamecmti10 scaled \startfont\sample'
\endlines
thereby defining directly, and using
to do the initialization instead of '\init'.

\medbreak
To conclude this appendix, let's look at the listing of a file
that can be used to test special constructions in math fonts
with the conventions of plain TeX:
\beginlines
'\raggedright \rightskip=2em plus 5em minus 2em'
break
'$\hbar \not\equiv B$, but $\sqrt C \mapsto \sqrt x$,'
'$Z \hookrightarrow W$, $Z \hookleftarrow W$,'
'$Z \longmapsto W$, $Z \bowtie W$, $Z \models W$,'
'$Z \Longrightarrow W$, $Z \longrightarrow W$,'
'$Z \longleftarrow W$, $Z \Longleftarrow W$,'
'$Z \longleftrightarrow W$, $Z \Longleftrightarrow W$,'
'$\overbracevery long things for testing$,'
'$\underbracevery long things for testing$,'
'$Z \choose W$, $Z \brack W$, $Z \brace W$, $Z \sqrt W$,'
'$Z \cong W$, $Z \notin W$, $Z \rightleftharpoons W$,'
'$\widehat Z$, $\widehatZW$, $\widehatZ+W$,'
'$\widetilde Z$, $\widetildeZW$, $\widetildeZ+W$.'
break
'\def\sizetest#1#2{$$'
' \Bigggl#1\bigggl#1\Biggl#1\biggl#1\Bigl#1\bigl#1\left#1'
' \bullet'
' \right#2\bigr#2\Bigr#2\biggr#2\Biggr#2\bigggr#2\Bigggr#2$$}'
'\def\biggg#1{{{$\left#1 to20.5pt\right.$}}}'
'\def\bigggl{\mathopen\biggg} \def\bigggr{\mathclose\biggg}'
'\def\Biggg#1{{{$\left#1 to23.5pt\right.$}}}'
'\def\Bigggl{\mathopen\Biggg} \def\Bigggr{\mathclose\Biggg}'
break
'\sizetest () \sizetest [] \sizetest \lgroup\rgroup'
'\sizetest \lmoustacheoustache \sizetest \vert\Vert'
'\sizetest \arrowvert\Arrowvert \sizetest \uparrow\downarrow'
'\sizetest \updownarrow\Updownarrow \sizetest \Uparrow\Downarrow'
'\sizetest \bracevert{\delimiter"342} \sizetest \backslash/'
'\sizetest \langle\rangle \sizetest \lbrace\rbrace'
'\sizetest \lceil\rceil \sizetest \lfloor\rfloor'
break
'$$\sqrt{\sqrt{\sqrt{\sqrt{\sqrt{\sqrt{\sqrt{\sqrt{\sqrt-1}}}}}}}}$$'
break
'\def\dobig{\do\bigvee \do\bigwedge \do\bigotimes \do\bigoplus \do\bigodot'
' \do\bigcap \do\bigcup \do\biguplus \do\bigsqcup'
' \do\int \do\ointop \doint \do\prod \do\coprod \do\sum}'
'\def\do#1{#1_a^b A} $\dobig$ $$\dobig$$'
break
'e'
\endlines

\endchapter

Be sure of it: Giue me the Occular proofe.

> --- WILLIAM , *Othello* (1604)

The figure itself appears here
as a very necessary adjunct to the verbalization.
In Euclid's presentation we cannot wholly follow the argumentation
without the figure, and unless we are strong enough
to imagine the figure in our mind's eye, we would also be reduced
to supplying our own figure if the author had not done it for us.
Notice also that the language of the proof has a
formal and severely restricted quality about it.
This is not the language of history, nor of drama,
nor of day to day life;
this is language that has been sharpened and refined so as to serve
the precise needs of a precise but limited intellectual goal.

> --- P. J. and R. , *Proof* (1981)


# Appendix I. Index

The author has tried to provide as complete an index as possible, so that
people will be able to find things that are tucked away in obscure
corners of this long book. Therefore the index itself is rather long. A
short summary of the simpler aspects of METAFONT\ appears at the beginning of
Appendix B; a summary of the standard character classes for tokens
can be found at the end of Chapter 6; a summary of other special things
appears under 'tables' below.

Page numbers are \underbarunderlined in the index when they represent
the definition or the main source of information about whatever is being
indexed. \ (Underlined entries are the most definitive, but not
necessarily the easiest for a beginner to understand.) \ A page number is
given in italics (e.g., '123') when that page contains an instructive
example of how the concept in question might be used. Sometimes both
underlining and italics are appropriate. When an index entry refers to a
page containing a relevant exercise, the answer to that exercise (in
Appendix A) might divulge further information; an answer page is not
indexed here unless it refers to a topic that isn't included in the
statement of the relevant exercise.

Index entries for quoted symbols like 'T' refer to example programs
that draw the symbols in question.

Symbolic tokens that are preceded by an asterisk (*) in this index are
primitives of METAFONT; i.e., they are built in. It may be dangerous to
redefine them.

\begindoublecolumns
=9.9pt
skip=0pt plus .8pt

\raggedright \tolerance=5000 \hbadness=5000 fillskip 0pt plus 3em
glue=.4em

3pt.\mskip2mu1pt.\mskip1mu}}

\catcode'\.=\other \catcode'\;=\other \catcode'\@=\other \catcode'\+=\other}

\underline{\box0}$\let\next=+
\else\let\next=#1\fi \next}

\hyphenpenalty=10000 \exhyphenpenalty=10000

\hangindent 2em
'6test.mf', 312--313.
'#' (hash mark), \see sharped dimensions.
'\#', 200--201.
'##' (traced equation), 80--83, 239.
'###' (removed independent variable), 83.
'####' (deduced equation), 81.
*'#@' (prefix of at point), +177, @251.
|
*'&' (ampersand), 213--214, \see concatenation.
\sub for preloaded bases, +35, 279.
''' (apostrophe or prime), @25, @55, @81.
'"' (double-quote mark), +50--+51.
'""' (empty string), +188, 236, 254, @276, @294, @328.
'(', 103--105, 128, 318.
'(' (left parenthesis), 59, +60, 61, @62--@63, 71--73, 165, 210--215.
'((', 51.
')' (right parenthesis), 59, +60, 61, @62--@63, 71--73, 165, 210--215.
'))', 51.
*'[' (left bracket), 9--10, +54, 55, 60, +72, 80, 211--212, 298--299, 324.
'[[', 61.
'[]' (collective subscript), +56, 177, @273.
'[1]' (progress report), 37, +324.
*']' (right bracket), 9--10, +54, 55, 60, +72, 80, 211--212, 298--299, 324.
']]', 61, @162, +262, 299.
*'' (left brace), 16--18, 60, +129, 213.
'', 61, 289.
*'' (right brace), 16--18, 60, +129, 213.
'', 61, 289.
*'+' (plus sign), @62, @63, +72, 80, 211.
*'++' (Pythagorean addition), @+66, @67, 72, 211.
\sub (double edge), 117, 296--297.
'+++' (triple edge), 296--297.
*'+-+' (Pythagorean subtraction), @+66, 72, 211, @238.
*'-' (minus sign), @62, @63, +72, 80, 211, 297.
'--' (straight join), @24--@26, 127--129, @234, +262.
\sub (double edge), 117, 296--297.
'---' (tense join), @107, 127--129, +262.
\sub (triple edge), 296--297.
'->' (macro expansion), 44, 160, 249, 251.
'---' (em dash), 306.
'_' (underline), 49, +51, 173, 265, 270.
'*' (asterisk), 285--286.
\sub as prompt character, 31, 37, 279.
\sub \llap{\char'\*}as times sign, @59, @62--@64, +72, +73, 80, 211--212.
'**', as command-line prompt, 31--32, 35--40, 187, 269, 279.
\sub as exponentiation sign, @59, @64, 72, @237, @251, +265.
'/' (slash), 328, 329.
\sub \llap{\char'\*}as divided-by sign, @59, @62, @63, +72, 80, 82, 211.
\| (vertical line), 117, 297.
*'\' (backslash), +179, @236, @262.
\sub at beginning of command line, @31, @38, 40.
'\\', +262.
*'<' (less than sign), @64, @65, +170, 210, 237.
*'<=' (less than or equal to), @64, 65, +170, 210, 282.
'<-' (argument value), 160.
*'<>' (unequal to), @64, 65, +170, 210, 282.
** (angle brackets), 49--50.
*'=' (equals sign), @5, @6, @23, @64, @75--@85, +88, 97, 165, 167, +170,
171, 210, 218.
'==', 292.
*'=:' (ligature replacement), @305, @306, @316, +317.
*\"=:|, @316, +317.
*\"=:>|, +317.
*'=:'\|, +317.
*'=:'\">|, +317.
*\"=:'\', +317.
*\"=:'\">', +317.
*\"=:'\">>', +317.
'\rlap/=' (unequals sign), 282.
*'>' (greater than sign), @64, +170, 210, 237.
'>>' (shown value), 41, 62.
*'>=' (greater than or equal to), @64, 65, +170, 210, 282.
*',' (comma), 57, 72, 73, 129, 155, 165--167, 171, 211--213, 218, 317, 318.
',,', 51.
'.' (period), 43, +50, 51.
'\char'\.', 306.
*'..' (free join), @7, @15--@19, @24, 127--133, 213.
'...' (bounded join), 18--19, 127, 248, +262.
'...' (truncation of displayed context), 44.
*';' (semicolon), 155, 169, 171, 172, 187, 217, 223--224, 263, 312.
';;', 51.
*':' (colon), 169, 171, 317--319.
*'::' (local label), +317.
*\'\":' (left boundary label), +317.
*':=' (gets), @28, @33, 87, +88, 97, @98, 155--156, 159, 165, 167, 171,
176, 218, 282.
'?', @41, +42--+43.
'???', @224, +262.
'!' (exclamation point), 41, 189.
*'@' (at point), +177, @251.
*'@#' (suffix of at point), @176, +177, +178, 251, @273--@274.
\newletter
'a', 192.
'A', 10--11, 163, 164, 248, 302--303.
'abort', 312--313.
'abs' (absolute value), @66, 82, @238, +264.
accents, 315, 317.
accuracy, 50, @62--@69, @143, 237.
ad hoc dimensions, 92, @95.
Adams, John, 359.
addition of pictures, 115, @117, @245.
addition of vectors, 9, @68.
*'addto', +118--+119, @144, @151, @242--@245.
*addto command*, 118, +220.
'adjust_fit', 306--308.
{\AE}schylus, 47.
{\AE}sopus, 340.
affine transformations, 247.
algebraic operations, 59--73, 209--215, 230.
Algol, 57, 89.
Alingham, William, 189.
Allen, Fred (= Sullivan, John Florence), 85.
almost digitized character, 296.
*'also', +118, 220, @242--@245.
'\alternation', 338.
alternatives, 169.
'always_iff', +307, @311--@312.
ambiguous points, 150, 198--200, 204.
American Mathematical Society, ii, ix.
anatomy of METAFONT, 169, 179, 217, 285, +344.
*'and', @65, +129, +170, 210, 213, 288--289.
Anderson, Izett William, 299.
*'angle', @29, @67, +72, @107, @135, 211, @238.
angle brackets, 49--50.
angle of pen, 21--22, 26--28, 152, 164.
arccosine, arcsine, arctangent, \see 'angle'.
arguments, 159--160, +166--+167, 210, 288.
arithmetic, 59--63.
arrays, 54--57.
ASCII, 49, 188, 281--283, 317.
*'ASCII', 72, +188, 211.
'aspect_ratio', 94, 145, 204, 269, 335.
*assignment*, +88.
assignments, @28, @33, 87--89, @98, 159.
*'at', +191, 220, @252, @277, @312.
at size, 96, 319.
*'atleast', 129, +132, 213, @262.
*'autorounding', 127, 195, +204--+205, @206, 212, @262, @264, 271--272.
axis, 103.
\newletter
'b', 308.
background character, @40, 338--339.
Backus, John Warner, 49.
backwards path, 119.
'badio.mf', 41, 223.
'barheight', 96, 161, 199, 302--303.
base file, 34--35, 261, 278--279, +304, 307.
baseline, 75--77, +101.
*basic path join*, 129, +213.
*'batchmode', +219, 226.
BCPL strings, 320.
bean-like shape, 15--16, 21--22, 24--25.
beauty, v, 185.
Beethoven, Ludwig van, 185.
'beginchar', 35, 76, @96, 102--103, 107, 115, 148, 156, 197, 199, 204,
+275, 316.
*'begingroup', +155--+157, 175, 178, 210--215, 217, @236, @243, @275, @289.
'beginlogochar', 160, 302.
Bell, Eric Temple, 11.
bell-shaped distribution, +183, 251.
Bernshte{\u\i}n, Serge{\u\i} Natanovich, 14.
\sub polynomials, 14, 133, 152, 246, 298--299.
B\'ezier, Pierre Etienne, 14.
Bibby, Duane Robert, i.
Bierce, Ambrose Gwinnett, ix.
'\bigtest', +341.
Billawala, Nazneen Noorudin, 266, 294.
binary search, 176--177, @293--@294.
'black', 270, 332--333.
black-letter, 294.
black/white reversal, 115.
'blacker', 93--94, 268, +270--+271.
'blankpicture', 192, +263.
Boole, George, 170.
*'boolean', 55, +56.
*boolean expression*, 170, +210.
boolean expressions, 170, 257.
*boolean primary*, 170, +210.
*boolean secondary*, 170, +210.
*boolean tertiary*, 170, +210.
'bot', @23, 80, 147, 151, 204, +273.
boundaries, 24--29, 123--125.
*'boundarychar', 212, 317.
bounded curves, 19, 132.
bounding box, 22, 35, 76, +101--+107, 276, 307, 315.
bounding triangle, 19, 132.
box, \see bounding box.
'bp' (big point), 92, +267, 268.
braces, 16--18, 60, +129, 213.
bracket notation, \see mediation.
brackets, 9--10, +54, 55, 60, +72, 80, 211--212, 298--299, 324.
broad-edge pens, 26--29, 151--152, 162--165.
Bront\"e, Emily Jane, 73.
Bruck, Richard Hubert, 29.
buffer size, 226, 286.
built-up symbols, 318.
Burkitt, William, 99.
Burns, Robert, 299.
'bye', +278, 279, @306, +321, 324.
'byte', +264, @275.
*byte list*, +318.
\newletter
$c$ code, 106, 324.
Camden, William, 51.
Campbell, John Campbell, 359.
'cand', 288--289.
'CAPSULE', 239.
'capsule_def', 264.
capsules, 159, 166, 172, 210, 239, 247, 254, 264.
Carter, Matthew, 207.
Cartesian coordinates, 5--6, 191.
'cc' (cicero), 92, +267, 268.
'ceiling', @65, 66, 72, +264.
'\centerlargechars', 340, +341.
chance, 183--185.
'change_width', @199, +276, +309.
*'char', 187, +188, 214, @263.
*'charcode', 106, 210, 212, +220, @275, 324.
*'chardp', 106, 212, 220, @275, +315--+316, 324.
*'chardx', 106, 212, 220, @276, +324, @334.
*'chardy', 106, 212, 220, +324.
*'charexists', +106, 210, 316, 324.
*'charext', 106, 212, +220, 316, 324.
*'charht', 106, 212, 220, @275, +315--+316, 324, @334, @335.
*'charic', 106, 212, 220, @275, +315--+316, 324.
*'charlist', @317, +318, 331, @334, @335.
*charlist command*, +318.
*'charwd', 106, 212, 220, @275, +315--+316, 324, @334, @335.
'cheapo', 91--93, 99, 278--279, 332--333.
check sums, 320, 324, +325.
Chinese characters, 3, 106, 324.
circles, 123--124, 148.
'clear_pen_memory', 147, +273, @278, @310.
'clearit', 115, @242, @275, +277, 295.
'clearpen', +272, @275.
'clearxy', @275, +277.
'cm' (centimeter), @18, 92, +267, 268.
'cm.base', 35, 279, 311.
'cmchar', @306, +307, 312--313.
'cmex10', 317--318.
'cmmf', 35, 279.
'cmr9', 203, 320.
'cmr10', 101, 305--306, 319.
'cmr10.mf', 305.
'cmsl10', 101.
'cmtt10', 306.
*code* and *code label*, +317.
codes, 281--283.
Colburn, Dorothy, 107.
collective subscripts, 56, 177.
*command*, +217.
command line, 38, 187, 269, 277, 301.
commands, 155, 217--220, 230, 321.
comments, 43, 50--51.
commutativity, 247.
comparison, @65, 80, 170.
compass directions, 26, 119, 206--207, 228--229.
complex numbers, 69.
*compound*, +217.
compound statement, +155, 217.
Computer Modern, 35, 103--105, 203, 206, 279, 304--313.
concatenation, of paths, @70--@71, @123, 127--129, +130, 137, @245, @266.
\sub of strings, @69, 73, 84--85, +187, @278, @286, @312.
*condition*, +169.
conditional and/or, 288--289.
conditions, 169--171, 179, 219, 259.
constants, 59, @62, 263--264.
contents of this manual, table, x--xi.
*'contour', +118--+119, 220.
control points, @13--@19, 70--71, 133, 229.
*'controls', @19, 70--71, +129--+130, 133, @152, 213.
*controls*, 129, +213.
conversion to pixel units, 259, +268.
convex polygons, @119, 147, 297--298.
Conway, John Horton, 121.
coordinates, 5--11, 23, 109, 191, 193.
'cor', 288--289.
corner pixels, 93--94.
*'cosd', @67, 72, 211.
cosines, 67, 69.
counterclockwise, 111, 119, 229, 255.
'counterclockwise', +264.
Cowper, William, 51.
'craziness', 184--185.
crispness, 103--104.
cube roots, 177.
cubes, 113.
*'cull', 118, +120, @151, @243--@245.
*cull command*, 118, +220.
'culldraw', @271, +272.
culling, 113, 120, @151, @242--@245, 296.
'cullit', @113, 120, @242, @243, +277.
Cundall, Frank, 299.
*'curl', @17, +128--+131, 213, 234.
'currentbreadth', 310--311.
'currentnull', 295.
'currentpen', 118, 147, 150, 204, +271--+272.
'currentpicture', 114, @115, @116, 118, 120, 191, +271--+272, 295.
'currenttransform', 94, @145, 204, +269, 271, 301, 310.
'currentwindow', 192, @312.
curves, 13--19, \see paths.
cusps, 136.
'cutdraw', @151, +271--+272.
'cutoff', @150--@151, +272.
*'cycle', @15, @16, @24--@28, @69, +129--+131, 170, 171, 210, 213.
\newletter
'd', 35, @76, 102, 204, +275.
'd', 294.
da Vinci, Leonardo, 19.
dangerous bend, vii, 11, 106--107, 115, 143.
Darwin, Charles Robert, 57.
data structures, 53--57.
Davis, Philip Jacob, 343.
*'day', +212, 218, 323.
'dd' (didot point), 92, +267, 268.
de Casteljau, Paul de Faget, 14.
debugging tricks, 229--231, 286.
*'decimal', +187--+188, 214.
*decimal digit*, +50.
decimal point, 50--51.
decimal representation, 188.
*declaration*, +56, 171.
*declaration list*, +57.
declarations, 56--57.
declarative versus imperative, 87.
*declared suffix*, +57.
*declared variable*, +57, 175.
'decr', +266.
*'def', @36, @159--@162, +165--+167.
'default_wt_', 271--272.
'define_blacker_pixels', @33, 92--93, @106, +268, 302.
'define_corrected_pixels', 93, 197, +268, 302.
'define_good_x_pixels', 199, +268, 302.
'define_good_y_pixels', 199, +268, 302.
'define_horizontal_corrected_pixels', @204, +268, 302.
'define_pixels', @33, 92, @106, 199, +268, 302.
'define_whole_blacker_pixels', 202, +268.
'define_whole_pixels', 199, +268, 302.
'define_whole_vertical_blacker_pixels', +268.
'define_whole_vertical_pixels', @204, +268, 302.
*definition*, +165.
*definition heading*, +165.
definitions, 159--167, 175--180.
deleting tokens, 42--43, 225.
*delimited parameters*, +165.
delimiters, 61, 167, 210, 254, 288--289.
*'delimiters', 61, 180, 210, +218, @221, @262, @296, @299, @313.
*delimiters command*, +218.
dependent variables, +81--+83, 88, 224.
depth, 101.
Derek, Bo, 287.
Descartes, Ren\'e, 6, 11, 19.
design size, 96, +319--+320, 324, 329.
*'designsize', 212, 320.
device drivers, 323, 325.
diagnostic aids, 229--231, 259, 286.
diamond-shaped nib, 148--149, 297.
Dickens, Charles John Huffam, 145.
difference of pictures, 115, @244.
digestion process, 179, 217--221.
*digit string*, +50.
digitization, 111, 149, 195--207, 230.
'\digits', 339.
dimensions, 92, +267.
'dir', @18, @67, @68, @83--@84, @135, @163--@164, 175, @233, +264.
'direction', @69, 70, @135, @235, +265.
*direction specifier*, 129, +213.
'directionpoint', @135, +265.
*'directiontime', @135, @+136, 211, 245, 265, @298.
'dishing', 152, 164.
*'display', +191--+192, 220.
*display command*, +220.
'displaying', 269, 276, 278.
distance, 76, 84, \also 'length'.
'ditto', @187, +263.
'div', +265.
division, @59, @62, @63, 80, 82.
\sub of numeric tokens, 61, 73.
Dopping, Olle, 181.
'dot', 306, 311.
dot product, 69.
'dotprod', @68--@69, 178, @238, 265.
'dotsize', 332, 334.
double-quote mark, 50--51, 187.
*'doublepath', 118, +119, @151, 220.
doubly filled pixels, 110--112.
'down', @32, +263.
'downto', 172, +262.
'draw', @7, @15--@19, 21, 112, 118--120, 145, 147, 150, 198, 230, +271, 295.
\sub one point, 22, 150, 200, 253.
'drawdot', @31, 113, 147, +150, 234, +271.
Drayton, Michael, 279.
drift, 102, 106.
driver files, 304--306.
*'dropping', 118, +120, 220.
*'dump', 217, +221, 262, @279, @311.
D\"urer, Albrecht, 13, 19.
'.dvi', 32, 40, 103, 106, 323, 327, 328.
\newletter
'e', 27--29, 273.
'E', 96--97, 204, 302--303.
edge structure, 116--117, 296--297.
edges, 116.
editing, 46.
efficiency, 39, 99, 116, 141, 144, 147, 228, 230, 234, 244, 264, 265, 277,
291, 297, 298.
El Palo Alto, 124--126, 139, 228--229.
ellipses, 123, 126.
Ellis, Henry Havelock, 11.
*'else', +169--+170, 179.
*'elseif', +169--+170, 179.
em dash, 306.
emergency stops, 226.
empty option in **for** list, 171, +172, @299.
empty statement, 155, 217.
empty text argument, 299.
*'end', @31, @37, 155, 167, 217, 221, 226, 278, 287, 305, @321.
end of a file, 287.
'endchar', @36, 102, 156, 191, +276, 309, 311, 329.
*'enddef', @94, @159--@164, 165, @175--@178.
*'endfor', @18, @39, +171--+172, @173, 250, @290.
'ENDFOR', 45, 286, 290.
*'endgroup', +155--+157, 167, 175, 178, 210--215, 217, @236, @243,
@276, @289, @290.
ending character, @40, 338--339.
*'endinput', +179, @287--@288.
endpoints, 128, 150--151.
'ENE', 119, 206--207, 228.
enormous number, 63, 236.
envelopes, 118--119, 150, 230.
'eps', 93, @199--@200, 229, +263, @310--@311.
'epsilon', @62--@69, 115, @135, 152, 229, +263.
equality test, general, 292.
equality versus equation, 171.
'equally_spaced', 290.
*equation*, +88.
equations, @5, @6, @23, @75--@85, 88, @141, 171.
\sub nonlinear, 84--85, 176--177, @292--@294.
equilateral triangle, 25, 203.
'erase', @113, 120, 167, +271, 272.
*'errhelp', +189, 219, @294.
*'errmessage', @178, +189, 219, @294.
error messages, 41--46, 223--228.
*'errorstopmode', +219, 227, @313.
'ESE', 206--207, 228--229.
*'everyjob', 180, +219.
*everyjob command*, +219.
Evetts, Leonard Charles, 153.
exercises, viii, 5--231.
*exit clause*, +171.
*'exitif', 171, +173, @176, 179, @262.
'exitunless', 173, +262.
expandable tokens, 179, 230.
*'expandafter', +179, 180, @270, @286--@290, @313.
expansion process, +179--+180, @285--@291.
exponential, \see 'mexp'.
*'expr', @160, @162, 165, @166, 167, @176, 210.
'(EXPR'$_n$')', 44, 160, 249, 251.
'expr.mf', +61, 62--71, 116--117, 132, 135--137, 142--143, 150, 173.
*expression*, 167, +209.
expressions, 59--73, 209--215.
*'extensible', 318.
*extensible command*, +318.
external tags, 55, 218.
'extra_beginchar', 275--276, @278.
'extra_endchar', 276, @277, @309.
'extra_setup', 269, @270, @278.
'!' 'Extra' 'tokens' 'will' 'be' 'flushed', 43--44, 224--225.
\newletter
'F', 97, 204, 302--303.
*'false', 55, @64--@65, 170, 210.
faster operation, 39, 99, 141, 144, 147, 228, 230, 234, 244, 264, 265, 277,
291, 297, 298.
'Fatal' 'base' 'file' 'error', 226.
fatter pens, 297--298.
*'fi', +169--+170, 179.
'!' 'File' 'ended...', 287.
file names, 36, 39, +180, 324, 329.
*filename*, 179--180.
'fill', @24--@27, 109--112, @116, 118--121, 145, 167, +271, 295.
'filldraw', @103--@105, 112--113, 118--119, 147, 148, @152, @164,
230, +271, @306, 310.
*'fillin', +93--+94, 150, 212, 247, 268, 278--279.
'fine', 103--104, 306--307, 310--311.
'fine.lft', 311.
'fix_units', +267.
flat spots, 196--197.
'flex', @124--@125, 127, @152, 173, 228--229, +267.
*'floor', @65, 66, 72, 83, 211, @253.
flushing, 43--44, 219, 224--225.
Font, Fray Pedro, 139, 231.
*font metric command*, +321.
font metric information, 39, 220, 315--321.
'font_coding_scheme', +277, @303, 304, +320--+321.
'font_extra_space', +277, 319.
'font_identifier', +277, @303, 304, @305, 320, @332--@333.
'font_normal_shrink', @97, +276, @305, 319.
'font_normal_space', @97, +276, @305, 319, 332.
'font_normal_stretch', @97, +276, @305, 319.
'font_quad', @97, +277, 308, 319, 332.
'font_setup', 203, 305, 309--312.
'font_size', @95, 96, +276.
'font_slant', +276, @305, 319, 331, @335--@336.
'font_x_height', +277, 319, 332.
*'fontdimen', @276--@277, +318--+319, 331--332, @335.
*fontdimen command*, +318.
*'fontmaking', 54, @94, 211, @270, +315.
'\fontname', 342.
*'for', @18, @39, @113, +171--+173, 179, 228, @285--@291, @299.
*for list*, +171, 299.
forbidden tokens, 173, +218--+219, 286.
*'forever', @61, +171--+173, @176, 179.
*'forsuffixes', +171--+172.
{\sevenrm FORTRAN} language, 237.
*four codes*, +318.
four-point method for curves, 13--14, 133.
Fournier, Simon Pierre, 321.
fractions, 61, @62--@63, +72, 73.
*'from', +191, 220, @252, @277, @312.
'fullcircle', @114, 123--124, 126, @135--@137, +263, @266.
Fulton, A\period\ G\period, 157.
function values by interpolation, 294--295.
*future pen primary*, 148, +214.
*future pen secondary*, 148, +214.
future pens, 148--149, 170, 249, 264, 298.
\newletter
Galsworthy, John, 215.
Gardner, Martin, 126.
'generate', 305, 307, 311, 313.
'gf', 32, 241, 295, 323--325.
'gfcorners', 277, +278, 327.
'GFtoDVI', 32, 37, 187, 327--336.
'gimme', 61--62.
Giotto di Bondone, 139.
'gobble', @167, +262, @289.
'gobbled', +262, @289--@290.
golden ratio, 11.
'good.bot', 204, +273.
'good.lft', 204, +273.
'good.rt', 204, +273.
'good.top', 204, +273.
'good.x', @198, @268, +273.
'good.y', @198, 204, @268, +273.
Goudy, Frederic William, 19.
grammatical rules, 49--50.
*'granularity', +205, 212, 262, 310.
graph paper, 5, 102, 109, 188.
'gray', 332.
gray fonts, 327, 330--335.
'grayf.mf', 332--335.
'grayfont', 270, +275, 323, 329.
'grayfontarea', 329.
'grayfontat', 329.
greater than or equal to, 65.
greatest integer function, \see 'floor'.
grid, 5, 109, 275.
Grimm, Jakob Ludwig Karl, 73.
Grimm, Wilhelm Karl, 73.
group delimiters, 289.
group expressions, 157, 160.
groups, 155--157, 167.
Gu Guoan, 3.
\newletter
'h', @22--@25, 35--36, @76--@78, 102, 204, +275.
'H', 163, 165.
Haggard, Sir Henry Rider, 107.
hairlines, 104--105.
'halfcircle', 123, @136, +263.
hamburgefonstiv, 341.
hand tuning, 195.
*'headerbyte', 318, +320--+321.
*headerbyte command*, +318.
hearts, 134.
height, 101.
Hein, Piet, 126, 231.
help messages, 43--45, 189, 224--225.
Herbin, Auguste, 3.
Hersh, Reuben, 343.
*'hex', +188, 211, 281.
hex symbol, 7--8, 28--29.
hexadecimal notation, 188.
'hide', @116, @143, 167, @173, @227, +262.
hierarchy of operators, 60--61, 71--73, 137, 209, 289.
histogram, 251.
Hobby, John Douglas, viii, 3, 130, 131, 149, 252, 285.
holes, 110.
Holland, Philemon, 51.
Homerus, 51.
homogeneous transforms, 247.
*'hppp', 92--93, 212, 267, 268, 324.
'hround', +264, @268.
Hult\'en, Karl Gunnar Pontus, 3.
\newletter
'I', 28, 32, 39, 163, 164.
'!' 'I' 'can't' 'go' 'on', 226.
IBM Corporation, ix.
'identity', @141--@145, 215, +263.
*'if', +169--+170, 179, 289.
'iff', @306, +307, 311.
'imagerules', 277, +278.
imperative versus declarative, 87.
impossible cube, 113.
'in' (inch), 92, +267, 268.
inaccessible token, 286.
incomplete string, 50--51.
inconsistent equations, 82, 313.
'incr', @39, 176--177, +266.
independent variables, +81--+83, 88, 224, 226, 299.
infinite loops, 172, 226--227.
'infinity', @62--@69, +263, @266.
inflection points, 18--19.
'INIMF', 221, 262, 279.
'\init', +337, 342.
*initial value*, +171.
*'inner', 180, +218--+219, 286--287, @307, @321.
'inorder', 290.
*'input', +179, 180, @269, @287--@288, 324.
input stack size, 226, 287.
inserting text online, 42, 45, 61, 188, 223--225.
integers, 65--66.
'interact', 230, +262.
interacting with METAFONT, 42--45, 61, 188--189, 191--193, 219, 223--225.
*'interim', +155--+156, 230, @243, @244, @271, @272.
*interim command*, 155, +218.
internal quantities, 54--55, 88, 218, 262, 265--266.
\sub table, 211--212.
*internal quantity*, 156, 218.
'interpath', 134, +267.
interpolation, 2, 134, 294--295.
interrupting METAFONT, 219, 227--228, 313.
intersection, of lines, 84.
\sub of paths, 136--137.
\sub of pictures, 120.
'intersectionpoint', @107, @137, @138, 178, +265.
*'intersectiontimes', +136, @178, 213, @265, @294, @298.
'inverse', @143, +264.
inverse video, 115, 118.
*'inwindow', +191, 220, @277.
Io, 33, 40, 47.
*is*, 165, 171, +218.
Isis, 40.
'!' 'Isolated expression', 223.
isolated math characters, 316, 319.
'italcorr', @103--@105, +275, @303, @306, @316.
italic corrections, 102, 105, 275, 276, 304, 315--316, 319.
italic type, 55, 206, 341.
\newletter
jaggies, 201.
*'jobname', +187, 214, 324.
Johnson, Samuel, 167.
Johnston, Edward, 29.
'join_radius', 266.
jokes, viii, 231.
*Journal of Algorithms*, 137--139.
'jut', 162, 308.
\newletter
Kafka, Franz, 340.
Kandinski\u\i, Vasili\u\i\ Vasil'evich, 3.
*keep or drop*, +118, 220.
*'keeping', 118, +120, 220.
'keepit', 295.
*'kern', @97, @316, +317.
kerning, 97, 316--317.
'killtext', +262, @272.
knife, 24.
*'known', @65, 79--82, 143, +170, 210.
Knuth, Donald Ervin, i, ii, ix, 3, 134, 192, 206, 255, 282, 291, 304, 308, 345,
361.
Knuth, Nancy Jill Carter, ix, 134, 137.
\newletter
'l', 308--309.
La Rochefoucauld, Fran\c cois VI, 313.
*label*, +317--+318.
*labeled code*, +318.
'labelfont', +275, 329.
'labelfontarea', 329.
'labelfontat', 329.
'labels', @107, +274, 327--328.
labels in font metric information, 317--318.
labels on 'proof' mode output, 37, 187, 274--275.
'labels.top', 328.
Lam\'e, Gabriel, 126.
'large_pixels', 332.
'lcode_', 274, 328.
le B\'e, Pierre, 207.
least integer function, \see 'ceiling'.
Leban, Bruce Philip, 242, 243, 270, 295.
'left', @16, +263.
left-handed dangerous bend, 143.
'leftstemloc', 96, 199, 302.
*'length', @66, @69, 72, 210, 238.
less than or equal to, 65.
*'let', 53, 180, +218, @287--@289, @299, @311.
*let command*, +218.
'letter_fit', 307--308.
*leveldef* and *leveldef heading*, 165, +178.
'lft', @23, @77, 80, 147, 151, +273.
lies, viii, 231.
Life, 121.
*ligature op*, +317.
ligatures, 305--306, 315--317.
'lightweight', 332.
*'ligtable', @97, @305--@306, +316--+317.
*ligtable command*, +317.
*ligtable program*, +317.
*ligtable step*, +317.
*limit value*, +171.
line, point to be on, 83--84.
linear dependencies, 82--83.
linear forms, 64, 82.
Linn\'e, Carl von (= Linn\ae us, Carolus), 325.
'local.mf', 278--279, 321.
'localfont', 39, 271, 278, @279.
locations of characters within a font, 106--107, 281--283, 320.
Lockyer, Sir Joseph Norman, 57.
log file, 42, 46, 62, 230, 295--297.
logarithm, \see 'mlog'.
'loggingall', 230, +263.
logo of METAFONT, ii, 22--23, 95--99, 160--161, 184--185, 199--200, 204, 301--304.
'logo.mf', 95--98, 199, 302--303.
logos, *i*, 97, @114, @137--@139.
'logo10.mf', 95, 287, 301, 304.
*loop* and *loop header*, +171.
loop text, 171--172, 219, 286.
loops, 169, 171--173, 179, 226--227, 259, 290--291, 299.
low-resolution proofs, 99, 327.
's', 339.
'lowres', 196, 201, 230, +270.
'lowres_fix', 203, +268, 310.
'luxo', 91--94, 99, 195, 278--279.
\newletter
'M', 23, 97, 200, 302--303.
macros, @36--@37, 53, 114, 159--167, 175--179, 285--299.
'mag', @39, +91--+93, 98, 169, 230, 269, 278, 333--334.
magnets, 60--61.
magnification, 38--40, 91--99.
'magstep', 98, +270.
'makebox', 270, +276, 309.
'makegrid', +275.
'makelabel', +274, 328.
*'makepath', +150, 213, 247, @298.
*'makepen', +147--+148, 214, @264.
'maketicks', 270, +276, 309.
mastication, 169, 179, 285.
'\math', 341.
Matthew, Saint, 173.
'max', @65, +266, 290--291.
maximum, 65.
mediation, 9--11, 14, @63, @68, 72, 80, 133, 298--299.
memory usage, 226--227.
*'message', @61, +189, @262.
*message command*, 189, +219.
*message op*, 189, +219.
meta-design, 1--3, 103--105, 294.
meta-font, 1--3, 98, 192, 301--304.
meta-ness, 3, 301.
METAFONT, the logo, ii, 22--23, 95--99, 160--161, 184--185, 199--200,
204, 301--304.
\sub the name, 1--3.
'METAFONT' 'capacity' 'exceeded', 226--227.
METAFONT79, viii.
*'mexp', @+67, 72, 211, @265, @270.
'mf', 31, 35.
'.mf', 36.
'mfput', 31--32, 187, 324.
'MFT', 262.
midpoints, 9, 13.
Mies van der Rohe, Ludwig, 185.
'min', @65, +266, 290--291.
minimum, 65.
Mirk, John, 313.
'!' 'Missing' ")'' 'has' 'been' 'inserted', 254.
misspelling, 45, 224.
'\mixture', @40, +338.
*'mlog', @+67, 72, 211, @265.
'mm' (millimeter), @76, 91--92, +267, 268.
M\"obius, August Ferdinand, 114.
mock curvature, 131.
'mod', @66, +265.
'mode', @38--@39, @75, 91--94, 269, 278.
*mode command*, +219.
'mode_def', 94, 189, @+270, @278--@279.
'mode_name', 269.
'mode_setup', @32--@34, 75, 76, 91--94, @96, 115, 169, +269, 278, @304, @305,
329.
'mono_charwd', 308.
'monospace', 305--308.
*'month', +212, 323.
More, Sir Thomas, 215.
Morison, Stanley, ix, 283.
mouth, 169, 179, 285.
Moxon, Joseph, 325.
Mulford, Clarence Edward, 89.
multiplication, @59, @62--@64, 69, 79--80, 82.
\sub of vector by scalar, 9.
music, 183, 185.
\newletter
'n', 201--203.
'N', 184--185, 302--303.
'\names', 339.
National Science Foundation, ix.
Naur, Peter, 49, 89.
negation, of pictures, 115.
\sub of vectors, 9.
'new_window', 193.
*'newinternal', 180, +218.
*newinternal command*, +218.
nice tangent points, 177.
'NNE', 119, 228.
'NNW', 26, 119, 228--229.
'nodisplays', 277, +278.
'nodot', 274, 328.
nonlinear equations, 84--85, 176--177, @292--@294.
nonsquare pixels, 94, 145, 204.
*'nonstopmode', +219, 226.
*'normaldeviate', @68, 72, @183--@185, 210.
*'not', @65, +170, 210.
'notransforms', 277, +278.
*'nullpen', +148, 214, @272.
*'nullpicture', +115, 192, 214, @272, @277.
*'numeric', 55, +56, @65, 88.
*numeric atom*, 72, +210.
*numeric expression*, 72, +211.
numeric expressions, 72--73, 257.
*numeric list*, +318.
*numeric operator*, 72, +211.
*numeric primary*, 72, +211.
*numeric secondary*, 72, 178, +211.
*numeric tertiary*, 72, +211.
*numeric token*, +50, 236.
*numeric token primary*, 72, +211.
numeric tokens, 49--50, 166.
\sub maximum value, 50.
\sub rounded fractional values, 50.
'numeric_pickup_', +272, 310.
*'numspecial', 220, @274, +323--+324, @327--@329.
'numtok', @+274.
\newletter
'o', @23, @34, +93, 197, 200, 204, 240, 302.
'o', 203.
'O', 32--37, 161, 199, 302--303.
'o_correction', 93--94, 268.
*'oct', +188, 211, 281.
octal notation, 188.
octants, 119, 206--207, 228--230.
*'odd', +170, 210, 250.
*'of', 73, 129, 165--167, 187, 211--214.
of-the-way function, \see mediation.
off by $x$, 82.
Office of Naval Research, ix.
'offset', 275, 329.
'!' 'OK', 219, 224.
'\omitaccents', 340.
one-point **draw**, 22, 150, 200, 253.
online interaction, 42--45, 61, 188--189, 191--193, 219, 223--225.
'openit', +277, 312.
*'openwindow', +191--+193, 220, @277, @312.
*openwindow command*, 191, +220.
operands, 59.
operators, 59, 230.
*optional skip*, +317.
*'or', @65, +170, 210, 237, 288--289.
order of operations, 60--61, 137, 247, 289.
oriental characters, 3, 106, 324.
'origin', @77--@78, @243, @251, +263.
ornament, 144--145.
Orwell, George (= Blair, Eric Arthur), 85.
*'outer', 180, +218--+219, 221, 286--287, @307, @321.
outlines, 121.
output of METAFONT, 39, 42, 315--325.
'overdraw', 114, 243.
overflow labels, 37, 328.
overlays, 295.
overshoot, 23, 34, 93, 197, 200, 204, 302.
\newletter
'P', 207.
Paget, Francis Edward, 279.
*'pair', 55, +56, 65.
*pair expression*, 73, +213.
pair expressions, 73, 171, 258.
*pair part*, +211.
*pair primary*, 73, +212.
*pair secondary*, 73, +212.
*pair tertiary*, 73, +213.
Palais, Richard Sheldon, ii.
parallel lines, 84.
parallelogram, 293--294.
*parameter*, +178.
parameter files, 301, 304.
*parameter heading*, +165.
*parameter tokens*, +165.
*parameter type*, +165.
parameters, v, 1--3.
\sub to fonts, 95, 103--104, 305.
\sub to macros, 159--167, 175--178.
parentheses, 51, 59, +60, 61, 71, 128, 210--215, 247.
Pascal language, 54.
*'path', 55, +56, 171.
*path expression*, 129, +213.
path expressions, 129--134, 258.
*path join*, 129--130, 171, +213.
*path primary*, 129, +213.
*path secondary*, 129, +213.
*path tertiary*, 129, +213.
paths, 13--19, 123--139.
*'pausing', 211, +231.
'pc' (pica), 92, +267, 268.
pels, \see pixels.
*'pen', 55, +56, @65, 170.
*pen expression*, 147, 148, +214.
pen expressions, 147--148, 258, 298.
*pen primary*, 148, +214.
*pen secondary*, 148, +214.
*pen tertiary*, 148, +214.
'pen_bot', 151, +272.
'pen_lft', 151, +272.
'pen_rt', 151, +272.
'pen_top', 151, +272.
*'pencircle', @21--@23, @28, @29, +147--+149, @150--@152, 198, 200, 214.
'penlabels', 36, +274.
*'penoffset', +150, 212, 230, @298.
'penpos', @26--@29, 37, 80, @103, @162, +273, 310.
'penrazor', @107, @112, 147, 150, +264, 297.
pens, 21--29, 147--152, 297--298.
'penspeck', +264, @271.
'pensquare', 147, 152, +264, 275.
'penstroke', 27--29, @138, +273.
perpendicular, 29, 69, 84, 235.
'pickup', @21--@23, 145, 147, +272.
*'picture', 55, +56, @114.
*picture command*, 118, +220.
*picture expression*, 115, +214.
picture expressions, 115, 258.
\sub transformation of, 144, 297.
*picture primary*, 115, +214.
*picture secondary*, 115, +214.
*picture tertiary*, 115, +214.
pictures, 109--121.
pimples, 196--197, 204.
'pix_ht', 332, @333.
'pix_picture', 332, @333.
'pix_wd', 332, @333.
pixels, 5, 109, 259, 324.
'pixels_per_inch', 267, 268.
plain METAFONT\ base, 34, +257--279.
'plain.mf', 261--278.
*plus or minus*, 72, +211.
*'point', @69--@70, 73, @114, +133, 212, @267.
polygonal path, 24, 297.
pool size, 226, 286.
'pos', 310.
*'postcontrol', +134, 212, @267.
'posttension', 136.
precedence, 60--61, 71--73, 137, 289.
*'precontrol', +134, 212, @267.
'pretension', 136.
pretty-printed METAFONT\ programs, 262.
*'primary', 165, 167.
*primary*, 71, 170, +209.
*'primarydef', 166, @+178.
prime numbers, 173.
primitives, 53, 209, 345.
private tokens, 173, 265, 270.
product, @59, @62--@64, 69, 79--80, 82.
\sub of vector by scalar, 9.
*program*, 155, +217.
program files, 304, 306.
*progression*, +171.
'proof' mode, 92, 93, 104, +270, 327.
*'proofing', @94, 187, 211, 220, @270, 274, +323--+324, 327.
'proofoffset', +275, 329.
'proofrule', +274, 323, 328--329.
'proofrulethickness', +275, 329.
proofsheets, 37, 261, 327--343.
*protection command*, +218.
pseudo-driver files, 311--313.
'pt' (printer's point), @21--@23, @33, 91--92, +267, 268.
'\punct', 339.
punctuation marks, 306.
Pythagorean addition, @+66, @67, 72, 211.
*Pythagorean plus or minus*, 72, +211.
Pythagorean subtraction, @+66, 72, 211, @238.
\newletter
'Q', 207.
'quartercircle', 123, +263.
Quick, Jonathan Horatio, 54, 137.
*'quote', +166, 172, @270, @286, @312.
\newletter
'r', 308--309.
'R', 207.
'\raggedright', 338.
Ramshaw, Lyle Harold, 320.
random numbers, 183--185.
*'randomseed', 185, 218.
*randomseed command*, +218.
'range', @107, @138, @200, +274.
raster, 5, 91, 109, 195.
*'readstring', @61, +187--+188, 214.
recipes, 2.
recursion, 227.
redundant equations, 82.
reference point, 77, +101.
'reflectedabout', @138, 141, @142, 160, +266.
reinitializing a variable, 88, 157.
*relation*, 170, +210.
relations, @64--@65, 170--171.
'relax', @31, +262, @307.
remainder, 66.
'rep', 332, 335.
replacement text, 159, +166, 219.
resolution, 6, 38--39, 91--99, 116.
*return* key, 31.
*'reverse', 129, +132, 213.
reverse video, 115, 118.
Reynolds, Lloyd Jay, 153.
'right', @26, @68, +263.
*right-hand side*, +88, 171.
*'rotated', @21--@22, @25, 27, 44, @68, 73, @107, @114, @117, +141, 213, @238.
'rotatedabout', +266.
'rotatedaround', @138, 141, @142, @144, 159--160, +266.
'round', @66, 196, 202, +264, @273.
rounding, 34--35, 50, 195--207, 308.
'rt', @23, @77, 80, @103, 147, 151, +273.
'rtest.mf', 311.
'rule', 274, 328.
'rulepen', +274, 275.
rules on proofsheets, 328--329.
'rulethickness', 275, 329.
runaway, 287.
Running, Theodore Rudolph, 47.
Ruskin, John, 139.
\newletter
'S', 40, 114.
'safefill', 121.
'\sample', 341.
sans-serif, 105, 305, 308.
*'save', +155--+156, @160, 173, @178, 180, 218, @236, @244, @296, 299.
*save command*, 155, +218.
'savepen', @96, 147, +272, @310.
*scalar multiplication operator*, 72, +211.
*'scaled', @21--@23, @68, 73, +141, 213, 244, 291.
*'scantokens', @61, +179, @180, 189, 251, @269, @270, @286--@288, @313.
scatter plots, 183.
*screen coordinates*, 191, +220.
*screen place*, 191, +220.
'screen_cols', 193, 277, @278.
'screen_rows', 277, @278.
'screenchars', 191, +277.
'screenrule', 274, 278.
'screenstrokes', 191, +277.
*'scrollmode', @61, +219, @313.
*'secondary', 165, 167.
*secondary*, 71, +209.
*'secondarydef', 166, @178.
selective complement, 120.
semantics, 50.
semicolons, 155, 169, 171, 172, 187, 217, 223--224, 263, 312.
'serif_fit', 308.
serifs, 152, 162--165, 308.
Serlio, Sebastiano, 19.
'setu_', 266, 291.
Shakespeare, William, 173, 255, 343.
sharped dimensions, @32--@35, 91--99, 102--103, 268, 315.
'shiftdef', 311.
*'shifted', @68, 73, @117, +141, 213.
'shipit', @31, @276, +277, 295.
*'shipout', 106, 210, +220, @277, @295, 316, 324, 329.
*shipout command*, +220.
*'show', 142, +219, @227, 230, @250, 296.
*show command*, +219.
*'showdependencies', 81, 83, +219, @262.
'showit', @31, 191, @276, +277, 295.
*'showstats', +219.
*'showstopping', 211, 219, @227, 230, @262.
*'showtoken', 180, +219, @221.
*'showvariable', 175, 177, 180, +219.
'shrink_fit', 308--310.
shrinkability, 319.
shuffled binary numbers, 137.
sidebearings, 10, 34--35, 307--308.
{\sevenrm SIMULA67} language, 175.
*'sind', @67, 72, 211.
*'skipto', @316, +317.
skyline, 251.
'slant', 105, 206, 301--303, 310, 319.
slant fonts, 329, 335--336.
*'slanted', @68, 73, 105, +141, 213.
'slantfont', +275, 329.
'slantfontarea', 329.
'slantfontat', 329.
'smode', 269.
'smoke' mode, 38, 75, 93, +270, 327.
*'smoothing', 55, 195, 205--206, 212, @262.
'softjoin', 262, +266.
'solve', 176--177, +267, @292--@294.
'(some' 'charht' 'values...)', 316.
Southall, Richard Francis, 176.
spaces, 43, 50, 236, 319.
sparks, +53--+55, 156, 175, 215, 219, 289.
*'special', 220, @240--@241, @274, +323--+324, @327--@329.
*special command*, +220.
special-purpose macros, 160, 248.
*'sqrt', @59, @64, 72, 211.
square roots, 66, \also 'sqrt'.
'SSE', 206--207, 228--229.
'SSW', 119, 228--229.
stack positions, 227.
Stanford, Amasa Leland, 340.
Stanford, Jane Elizabeth Lathrop, 340.
Stanford University, 125, 340.
star, 114.
'\startfont', +337, 338, @342.
starting a job, 39, 95, 259, 277.
starting character, @40, 338--339.
*statement*, 155, 171, +217.
*statement list*, 155, +217.
statements, 155, 217--221.
\sub summary, 260--261.
stems, 201--203.
*'step', @18, 171.
*step size*, +171.
stomach, 169, 217, 285.
'stop', +262, @311--@312.
stopping METAFONT, \see 'end'.
*'str', +187--+188, 214, @250, @251.
strange paths, 110--111, 119, 121, 136, 152, 228--229.
Stravinski{\u\i}, Igor' F\"edorovich, 193.
stretchability, 319.
Strindberg, Johan August, 185.
*'string', 55, +56.
*string expression*, 73, 187, +214.
string expressions, @69, 187--189, 258, 286.
*string primary*, 187, +214.
*string secondary*, 187, +214.
*string tertiary*, 187, +214.
string tokens, 49--51.
'stroke', @306, 310.
*'subpath', @70, @71, 114, 129, +133, 134, 188, 213, @298.
subroutines, \see macros.
*subscript*, +54.
subscripts, 54--57.
*'substring', @69, 187, +188, 214, @320.
subtraction, of pictures, 115, @244.
\sub of vectors, 9.
Suetonius Tranquillus, Gaius, 181.
*'suffix', @161, 165, @176.
*suffix*, +54, 161, 176, 188.
*suffix list*, +171, 236.
'(SUFFIX'$_n$')', 44, 251.
sum, of pictures, 115, @117, @245.
\sub of transforms, 178.
\sub of vectors, 9, @68.
'superellipse', @126, @138, +267.
superellipses, 126, 161.
'superness', 126.
Sutherland, Ivan Edward, 121.
Swift, Jonathan, 99, 121.
*symbolic token list*, 155, +218.
symbolic tokens, 49--51.
symmetric difference, 120.
syntax rules, 49--50.
System Development Foundation, ix.
\newletter
'T', 22--23, 97, 151, 199--200, 302--303.
tables of METAFONT\ trivia:
\sub character classes, 51.
\sub character codes, 281--282.
\sub expandable tokens, 179--180.
\sub 'fontdimen' parameters, 319.
\sub internal quantities, 211--212.
\sub language features, 257--261.
\sub proof label options, 328.
\sub types, 55.
\sub units of measure, 92.
tags, +53--+55, 156, 175, 218--219.
'takepower', +265.
taller pens, 297--298.
tapered stroke, 28.
'tensepath', 128, +264, @298.
*'tension', @15--@16, @114, +129--+132, 136, @296.
*tension*, 129, +213.
*tension amount*, 129, +213.
*'tertiary', 165, 167.
*tertiary*, 71, @137, +209.
*'tertiarydef', 166, +178, @266.
'test.mf', 311--313.
'testfont.tex', 40, 336--342.
TeX, 1, 34, 40, 91, 96, 98, 101--103, 315, 336--343, 361.
*'text', @161, +165--+167.
'\text', 340.
'(TEXT'$_n$')', 45, 249, 251.
text arguments, 219, 288--291, 299.
'.tfm', 39, 315--321, 333, 335.
'!' 'This' 'can't' 'happen', 226.
Thomson, James, 189.
Thoreau, Henry David, 221.
'thru', @107, @138, @200, +274.
tilde, 152.
*'time', +212, 218, 323.
time in paths, 119, 133--137.
*times or over*, 72, +211.
Tinguely, Jean, 3.
*title*, +187, 217--218, 323.
'title', 323, 327.
'titlefont', +275, 329.
'titlefontarea', 329.
'titlefontat', 329.
*'to', +191, 220, @252, @277, @312.
'<to' 'be' 'read' 'again>', 223.
Tobin, Georgia Kay Mase, ii, 240.
tokens, 42--43, +49--+51, 210.
'tolerance', 176, 251, 267, 293.
'top', @23, @77, 80, @103, 147, 151, 204, +273.
Tory, Geoffroy, 19.
'totalnull', 295.
*'totalweight', +115, 211, @292.
'tracingall', 230, +263, 288.
*'tracingcapsules', 211, 219, 239.
*'tracingchoices', 211, +229.
*'tracingcommands', 211, +230.
*'tracingedges', 211, +230, @295--@296.
*'tracingequations', 80--83, 211, 229.
*'tracingmacros', +160, 211, 229.
'tracingnone', 230, +263.
*'tracingonline', @61, 80, 211, 219, +230.
*'tracingoutput', 211, +229--+230, 296.
*'tracingpens', 211, +229, 230.
*'tracingrestores', +156, 211, 229.
*'tracingspecs', 206--207, 211, +229.
*'tracingstats', 211, +227, 230.
*'tracingtitles', 55, @94, +187, 211, 229.
Trajanus, 153.
trajectories, \see paths.
transcript file, 42, 46, 62, 230, 295--297.
*'transform', 55, +56, 57, 141--143, @160, 266.
*transform expression*, +215.
transform expressions, 141--143, 170, 178, 258.
*transform part*, +211.
*transform primary*, +215.
*transform secondary*, +215.
*transform tertiary*, +215.
transformations, 44, 141--145.
*'transformed', 73, 141--145, 213.
*transformer*, 73, +213.
transition lines, 230.
'transum', 178.
trial path, 235.
triangle, 24--25, 203.
trigonometric functions, 67, 69, 131, 177.
*'true', 55, @64--@65, 170, 210.
truth, viii, 217, 221.
*TUGboat*, ix, 361.
turning numbers, 110, +111, 112, 119, 136, 147.
*'turningcheck', 112, +119, 212, 229, @244, 262, 296.
*'turningnumber', 111, 211, 257, @264.
Twain, Mark (= Clemens, Samuel Langhorne), 145.
*type*, +56, 171.
type declarations, 56.
types, 55.
typewriter type, 55, 105.
typographic errors, 45, 224.
\newletter
'u', 103--104, 305--308.
'!' 'Undefined' 'coordinate', 224.
undelimited arguments, +167.
*undelimited parameters*, +165.
undelimited suffix parameters, +167, 176, 266, 270.
underline characters, 49, +51, 173, 265, 270.
'undraw', 113, 118, 120, @242, +271.
'undrawdot', 113, +271.
unequal to, 65.
'unfill', @25, 27, 109--110, 118, @126, +271.
'unfilldraw', 113, 118, +271.
*'uniformdeviate', @68, 72, +183, 184, 211.
union, 120.
Union Jack, 7.
'unitpixel', +263, @333.
units of measure, 33, 91--99, 267--268.
\sub table, 92.
'unitsquare', @116, 123--124, 128, 132, 136, +263.
'unitvector', @238, +264.
*'unknown', +170, 210.
unknown quantities, nonnumeric, 84--85, 143.
\sub numeric, 79--83.
*'until', @18, 171.
'up', @32, @129, +263.
'\uppers', 339.
'upto', @39, 172, +262.
utility files, 311--313.
\newletter
*vacuous expression*, +215.
vacuous expressions, 209, +215, 250, 262, 289, 292.
*vacuous primary*, +215.
*vacuous secondary*, +215.
*vacuous tertiary*, +215.
valentine, 134.
values, disappearance of, 56, 83, 88, 156--157, 177--178, 218, 239, 299.
*'vardef', 166, @175--@178, 289.
*vardef heading*, 165, +178.
*variable*, 54, +55, 210.
variables, 53--57, 59.
\sub reinitializing, 88, 157.
vector subtraction principle, 9.
vectors, 9--10, 77.
velocity zero, 136, 298.
Venezky, Richard Lawrence, 193.
*'vppp', 212, 267, 324.
'vround', @204, @+264, @268.
\newletter
'w', @22--@25, 35--36, @76--@78, 102--103, 106, +275--+276, 308--310.
'w', 202.
*'warningcheck', 212, @269, 270.
Warren, Mercy Otis, 359.
Webster, Noah, 167.
'whatever', @83--@84, @138, 157, @233, 239, +264, @290.
width, 101.
Wilde, Oscar Fingal O'Flahertie Wills, 321.
Wilkins, John, ii, 283.
Willis, Ellen Jane, 157.
*window*, 191, +220.
*window spec*, 191, +220.
*with clause*, +118, 220.
*'withpen', 118, 220, @242.
*'withweight', 118, 220, @242, @297.
'WNW', 119, 228--229.
'WSW', 119, 228--229.
\newletter
$x$ coordinates, @5--@7.
x-height, 319.
Xerox Corporation, 320.
'xgap', 95--96, 199.
*'xoffset', 212, +220, @309, 315, 324.
xor, 120.
*'xpart', @68, 72, @138, 142, 211.
*'xscaled', @21--@22, @68, 73, +141, 213, 244, 291.
*'xxpart', 72, 142, @160, 211.
'xy_swap', 297.
*'xypart', 142, @160, 211.
\newletter
$y$ coordinates, @5--@7.
*'year', +212, 323.
'ygap', 96, 199.
*'yoffset', 212, +220, 315, 324.
*'ypart', @68, 72, 142, 211, 238.
*'yscaled', @21--@23, @68, 73, +141, 213, 244, 291.
*'yxpart', 142, @160, 211.
*'yypart', 142, @160, 211.
\newletter
'z' convention, 7, @68, 69, 251, +277.
Zapf, Hermann, iii, 221.
zero, 236.
*'zscaled', @68--@69, 73, +141, 213.
'ztest.mf', 312.
\enddoublecolumns
\endchapter

The more we search,
the More are we Deceived.

> --- MERCY OTIS , *To Mr. Adams* (1773)

A heavy weight is now to be removed from my conscience.
So essential did I consider an Index to be to every book,
that I proposed to bring a Bill into Parliament
to deprive an author who publishes a book without an Index
of the privilege of copyright; and, moreover,
to subject him, for his offence, to a pecuniary penalty.
Yet, from difficulties started by my printers,
my own books have hitherto been without an Index.
or LORD , *Lives of the Chief Justices
of England*, vol. 3 (1857)


# Appendix J. Joining the TeX\ Community

This appendix is about grouping of another kind: TeX\ and METAFONT\ users from
around the world have banded together to form the TeX\ Users Group (TUG),
in order to exchange information about common problems and solutions.

A newsletter/journal called *TUGboat* has been published
since 1980, featuring articles about all aspects of TeX\ and METAFONT\!.
TUG has a network of "site coordinators" who serve as focal points of
communication for people with the same computer configurations.
Occasional short courses are given,
to provide concentrated training in special topics; videotapes of
these courses are available for rental.
Meetings of the entire TUG membership are held at least once a year.
You can buy METAFONT\ T-shirts at these meetings.

Information about membership in TUG and subscription to *TUGboat*
is available from

{\obeylines
TeX\ Users Group
'email: TUG@tug.org'
'internet: http://www.tug.org'
}

\endchapter

TUG is established to serve members having a common interest
in TeX, a system for typesetting technical text,
and in {\manual \char'\\]\char'\^\char'\_efg\char'\^}\!,
a system for font design.
or T.5exE X
USERS GROUP, *Bylaws, Article II* (1983)

Don't delay, subscribe today! That address again is
TeX\ Users Group
email: {\eighttt TUG\char'\@ tug.org}
internet: {\eighttt http://www.tug.org/}

> --- DONALD E. , *The TeX book* (1996)

\end
