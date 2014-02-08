# revision 24768
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langarabic
Epoch:		1
Version:	20120224
Release:	2
Summary:	Arabic
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langarabic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-amiri
Requires:	texlive-arabi
Requires:	texlive-arabtex
Requires:	texlive-bidi
Requires:	texlive-hyphen-arabic
Requires:	texlive-hyphen-farsi
Requires:	texlive-persian-bib
Requires:	texlive-persian-modern
Requires:	texlive-collection-basic

%description
Support for typesetting Arabic.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780331
- Update to latest release.
- Import texlive-collection-langarabic
- Import texlive-collection-langarabic

