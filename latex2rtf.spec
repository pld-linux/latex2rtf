Summary:	LaTeX to RTF converter program
Summary(pl):	Konwerter z formatu LaTeXa do RTF
Name:		latex2rtf
Version:	1.8aa
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/latex2rtf/%{name}-%{version}.tar.gz
Source1:	polish.cfg
Patch0:		%{name}-Makefile.patch
URL:		http://latex2rtf.sourceforge.net/
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX to RTF converter.

%description -l pl
Program do przetwarzania dokumentów z formatu TeX (LaTeX) na format
Rich Text Format, czytany przez programy firmy Microsoft.

%prep
%setup -q
%patch -p0

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}" prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 install
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 simple_cfg_install

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}

gzip -9nf doc/TODO doc/l2r.txt README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/TODO.gz doc/l2r.txt.gz doc/l2r.html doc/l2r.pdf README.gz ChangeLog.gz  
%attr(755,root,root) %{_bindir}/latex2rtf
%attr(644,root,root) %{_libdir}/%{name}/*
%attr(644,root,root) %{_mandir}/man1/*
