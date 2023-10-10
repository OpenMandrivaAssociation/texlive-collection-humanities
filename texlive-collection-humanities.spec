Name:		texlive-collection-humanities
Epoch:		1
Version:	68465
Release:	1
Summary:	Humanities packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-humanities.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-alnumsec
Requires:	texlive-arydshln
Requires:	texlive-bibleref
Requires:	texlive-bibleref-lds
Requires:	texlive-bibleref-mouth
Requires:	texlive-bibleref-parse
Requires:	texlive-covington
Requires:	texlive-dramatist
Requires:	texlive-dvgloss
Requires:	texlive-ecltree
Requires:	texlive-edfnotes
Requires:	texlive-ednotes
Requires:	texlive-eledform
Requires:	texlive-eledmac
Requires:	texlive-expex
Requires:	texlive-gb4e
Requires:	texlive-gmverse
Requires:	texlive-jura
Requires:	texlive-juraabbrev
Requires:	texlive-juramisc
Requires:	texlive-jurarsp
Requires:	texlive-ledmac
Requires:	texlive-leipzig
Requires:	texlive-lexikon
Requires:	texlive-lexref
Requires:	texlive-lineno
Requires:	texlive-linguex
Requires:	texlive-liturg
Requires:	texlive-metrix
Requires:	texlive-parallel
Requires:	texlive-parrun
Requires:	texlive-phonrule
Requires:	texlive-plari
Requires:	texlive-play
Requires:	texlive-poemscol
Requires:	texlive-poetrytex
Requires:	texlive-qobitree
Requires:	texlive-qtree
Requires:	texlive-rrgtrees
Requires:	texlive-rtklage
Requires:	texlive-screenplay
Requires:	texlive-sides
Requires:	texlive-stage
Requires:	texlive-textglos
Requires:	texlive-thalie
Requires:	texlive-tree-dvips
Requires:	texlive-verse
Requires:	texlive-xyling

%description
Packages for law, linguistics, social sciences, humanities,
etc.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
