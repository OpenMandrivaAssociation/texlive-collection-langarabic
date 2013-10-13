# revision 31684
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langarabic
Epoch:		1
Version:	20131013
Release:	1
Summary:	Arabic
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langarabic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-amiri
Requires:	texlive-arabi
Requires:	texlive-arabtex
Requires:	texlive-bidi
Requires:	texlive-ghab
Requires:	texlive-hyphen-arabic
Requires:	texlive-hyphen-farsi
Requires:	texlive-imsproc
Requires:	texlive-lshort-persian
Requires:	texlive-persian-bib
Requires:	texlive-persian-modern
Requires:	texlive-simurgh
Requires:	texlive-tram

%description
Support for Arabic and Persian.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
