Name:		texlive-collection-langarabic
Epoch:		1
Version:	59594
Release:	2
Summary:	Arabic
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langarabic.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
