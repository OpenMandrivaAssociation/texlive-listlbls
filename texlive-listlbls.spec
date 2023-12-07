Name:		texlive-listlbls
Version:	67215
Release:	1
Summary:	Creates a list of all labels used throughout a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listlbls
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package aims to help a LaTeX author to keep track of all
defined labels by typesetting a complete list of labels
wherever the author requests it. (Of course, the user may need
to have additional LaTeX runs to get the references right. )
This package is based on an answer David Carlisle gave on
TeX/Stackexchange in the thread 'List of all labels with
hyperlinks'.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/listlbls
%{_texmfdistdir}/tex/latex/listlbls
%doc %{_texmfdistdir}/doc/latex/listlbls

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
