Name:		texlive-invoice-class
Version:	49749
Release:	2
Summary:	Produces a standard US invoice from a CSV file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/invoice-class
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice-class.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice-class.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class produces a standard US commercial invoice using data
from a CSV file. Invoices can span multiple pages. The class is
configurable for different shipping addresses.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/invoice-class
%doc %{_texmfdistdir}/doc/latex/invoice-class

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
