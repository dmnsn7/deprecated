\LoadClass{ctexart}

\RequirePackage[left=0.5in, right=0.5in, top=0.5in, bottom=0.5in]{geometry}
\RequirePackage{calc, enumitem, fancyhdr, eso-pic}

\setitemize{nolistsep}
\def\baselinestretch{1.0}

\def\name#1{\def\@name{#1}}
\def\telephone#1{\def\@telephone{#1}}
\def\email#1{\def\@email{#1}}
\def\shiftrule{\vbox to 5pt{\vss\hrule width \linewidth height 0.4pt depth 0pt\vss}}
\def\items{\begin{itemize}}
\def\enditems{\end{itemize}}

\newlength{\@block}
\newenvironment{block}[1][]{
    \def\@arg{#1}
    \setlength{\@block}{\linewidth-0.65in-0.75cm-3.65pt}
    \ifx\@arg\empty\else\shiftrule\nobreak\fi
    \halign to \linewidth\bgroup
    \vtop{\hsize=0.65in\tabskip=0.75cm##\hfill}&
    \vtop{\hsize=\@block\tabskip=0pt##\hfill}\cr
    \vtop{\raggedright\textsc{#1}}&
    \vtop\bgroup\setlength{\linewidth}{\@block}
}{
    \egroup\cr\egroup
}

\newcounter{sec}
\renewenvironment{section}[1]{
    \stepcounter{sec}
    \begin{block}[#1]
}

\newcounter{place}[sec]
\newenvironment{place}[2][]{
    \stepcounter{place}
    \ifnum\value{place}=\@ne
    \else
    \begin{block}
        \shiftrule
        \fi
        \gdef\placename{#2}
        #1\textbf{\placename}\par
        }{
    \end{block}\label{end-\placename}
}

\AtBeginDocument{
    \pagestyle{empty}
    \vtop{
        \centering
        {\Large{\@name}}\par
        \@telephone\par
        \@email\par
        \vskip 5pt
    }
}
