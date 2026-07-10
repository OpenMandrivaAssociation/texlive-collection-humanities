%global tl_name collection-humanities
%global tl_revision 78303

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Humanities packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-humanities
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-humanities.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(adtrees)
Requires:	texlive(bibleref)
Requires:	texlive(bibleref-lds)
Requires:	texlive(bibleref-mouth)
Requires:	texlive(bibleref-parse)
Requires:	texlive(collection-latex)
Requires:	texlive(covington)
Requires:	texlive(diadia)
Requires:	texlive(dramatist)
Requires:	texlive(dvgloss)
Requires:	texlive(ecltree)
Requires:	texlive(edfnotes)
Requires:	texlive(edmac)
Requires:	texlive(eledform)
Requires:	texlive(eledmac)
Requires:	texlive(expex)
Requires:	texlive(expex-glossonly)
Requires:	texlive(gb4e)
Requires:	texlive(gb4e-next)
Requires:	texlive(gmverse)
Requires:	texlive(interlinear)
Requires:	texlive(jura)
Requires:	texlive(juraabbrev)
Requires:	texlive(juramisc)
Requires:	texlive(jurarsp)
Requires:	texlive(langnames)
Requires:	texlive(ledmac)
Requires:	texlive(lexikon)
Requires:	texlive(lexref)
Requires:	texlive(ling-macros)
Requires:	texlive(linguex)
Requires:	texlive(linguistix)
Requires:	texlive(liturg)
Requires:	texlive(liturgy-cw)
Requires:	texlive(metrix)
Requires:	texlive(nnext)
Requires:	texlive(opbible)
Requires:	texlive(parallel)
Requires:	texlive(parrun)
Requires:	texlive(phonrule)
Requires:	texlive(plari)
Requires:	texlive(play)
Requires:	texlive(poemscol)
Requires:	texlive(poetry)
Requires:	texlive(poetrytex)
Requires:	texlive(qobitree)
Requires:	texlive(qtree)
Requires:	texlive(reledmac)
Requires:	texlive(rrgtrees)
Requires:	texlive(rtklage)
Requires:	texlive(screenplay)
Requires:	texlive(screenplay-pkg)
Requires:	texlive(sharedline)
Requires:	texlive(sides)
Requires:	texlive(stage)
Requires:	texlive(textglos)
Requires:	texlive(thalie)
Requires:	texlive(theatre)
Requires:	texlive(tree-dvips)
Requires:	texlive(verse)
Requires:	texlive(xyling)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Packages for law, linguistics, social sciences, humanities, etc.

