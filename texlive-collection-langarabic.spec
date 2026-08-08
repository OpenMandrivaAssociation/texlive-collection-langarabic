%global tl_name collection-langarabic
%global tl_revision 79885

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Arabic
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langarabic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langarabic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(alkalami)
Requires:	texlive(alpha-persian)
Requires:	texlive(amiri)
Requires:	texlive(arabdoc)
Requires:	texlive(arabi)
Requires:	texlive(arabi-add)
Requires:	texlive(arabic-book)
Requires:	texlive(arabluatex)
Requires:	texlive(arabtex)
Requires:	texlive(awami)
Requires:	texlive(bidi)
Requires:	texlive(bidihl)
Requires:	texlive(collection-basic)
Requires:	texlive(dad)
Requires:	texlive(fariscovernew)
Requires:	texlive(ghab)
Requires:	texlive(hadith)
Requires:	texlive(hvarabic)
Requires:	texlive(hyphen-arabic)
Requires:	texlive(hyphen-farsi)
Requires:	texlive(imsproc)
Requires:	texlive(iran-bibtex)
Requires:	texlive(khatalmaqala)
Requires:	texlive(kurdishlipsum)
Requires:	texlive(lshort-persian)
Requires:	texlive(luabidi)
Requires:	texlive(mohe-book)
Requires:	texlive(na-box)
Requires:	texlive(parsimatn)
Requires:	texlive(parsinevis)
Requires:	texlive(persian-bib)
Requires:	texlive(quran)
Requires:	texlive(sexam)
Requires:	texlive(simurgh)
Requires:	texlive(texnegar)
Requires:	texlive(tram)
Requires:	texlive(xepersian)
Requires:	texlive(xepersian-hm)
Requires:	texlive(xindy-persian)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Arabic and Persian.

