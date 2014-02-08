# revision 27322
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-humanities
Epoch:		1
Version:	20120810
Release:	2
Summary:	Humanities packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-humanities.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-alnumsec
Requires:	texlive-arydshln
Requires:	texlive-bibleref
Requires:	texlive-bibleref-lds
Requires:	texlive-bibleref-mouth
Requires:	texlive-bibleref-parse
Requires:	texlive-covington
Requires:	texlive-dramatist
Requires:	texlive-ecltree
Requires:	texlive-edfnotes
Requires:	texlive-ednotes
Requires:	texlive-gb4e
Requires:	texlive-gmverse
Requires:	texlive-jura
Requires:	texlive-juraabbrev
Requires:	texlive-juramisc
Requires:	texlive-jurarsp
Requires:	texlive-ledmac
Requires:	texlive-lexikon
Requires:	texlive-lineno
Requires:	texlive-linguex
Requires:	texlive-liturg
Requires:	texlive-parallel
Requires:	texlive-parrun
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
Requires:	texlive-tree-dvips
Requires:	texlive-verse
Requires:	texlive-xyling
Requires:	texlive-collection-latex

%description
Packages for law, linguistics, the social sciences, the
humanities, etc.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813911
- Update to latest release.

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120307-1
+ Revision: 783099
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780329
- Update to latest release.
- Import texlive-collection-humanities
- Import texlive-collection-humanities

