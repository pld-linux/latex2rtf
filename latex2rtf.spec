Summary:	LaTeX to RTF converter program.
Summary(pl):	Konwerter z formatu LaTeXa do RTFa.
Name:		latex2rtf
Version:	1.8aa
Release:	1
Copyright:	GPL
Group:		Tools
Group(pl):	Narzêdzia
Source0:	%name-%version.tar.gz
Source1:	polish.cfg
Patch0:		%name-Makefile.patch
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
LaTeX to RTF converter.

%description -l pl
Program do przetwa¿ania  dokumentów z formatu TeX (LaTeX) na format
czytany przez programy firmy Microsoft.

%prep
%setup -q

%patch -p0

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}
make prefix=$RPM_BUILD_ROOT%{_prefix} MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 install
make prefix=$RPM_BUILD_ROOT%{_prefix} MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 simple_cfg_install

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf doc/TODO doc/l2r.txt README ChangeLog

strip $RPM_BUILD_ROOT%{_bindir}/* || die

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/TODO.gz doc/l2r.txt.gz doc/l2r.html doc/l2r.pdf README.gz ChangeLog.gz  
%attr(755,root,root) %{_bindir}/latex2rtf
%attr(644,root,root) %{_libdir}/%{name}/*
%attr(644,root,root) %{_mandir}/man1/*.gz
