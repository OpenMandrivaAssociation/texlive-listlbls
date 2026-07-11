%global tl_name listlbls
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	Creates a list of all labels used throughout a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listlbls
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listlbls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package aims to help a LaTeX author to keep track of all defined
labels by typesetting a complete list of labels wherever the author
requests it. (Of course, the user may need to have additional LaTeX runs
to get the references right. ) This package is based on an answer David
Carlisle gave on TeX/Stackexchange in the thread 'List of all labels
with hyperlinks'.

