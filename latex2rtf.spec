Summary:	LaTeX to RTF converter program
Summary(pl):	Konwerter z formatu LaTeXa do RTF
Name:		latex2rtf
Version:	1.9.12
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/latex2rtf/%{name}-%{version}.tar.gz
Source1:	polish.cfg
Patch0:		%{name}-fixc.patch
URL:		http://latex2rtf.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX to RTF converter.

%description -l pl
Program do przetwarzania dokumentów z formatu TeX (LaTeX) na format
Rich Text Format, czytany przez programy firmy Microsoft.

%prep
%setup -q
%patch -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags} -DUNIX" PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_infodir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LIBINSTALL=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INST_DIR="install -d" INST_BIN=install INST_DAT=install

#%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} MANINSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 simple_cfg_install

install doc/latex2rtf.info $RPM_BUILD_ROOT%{_infodir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}

gzip -9nf doc/credits README ChangeLog Copyright

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/latex2rtf
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
