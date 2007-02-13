# TODO:
# - SECURITY: http://securitytracker.com/alerts/2004/Sep/1011367.html
Summary:	LaTeX to RTF converter program
Summary(pl.UTF-8):	Konwerter z formatu LaTeXa do RTF
Name:		latex2rtf
Version:	1.9.16a
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/latex2rtf/%{name}-%{version}.tar.gz
# Source0-md5:	b1c766baeb645c954fb2454fc51c5f03
URL:		http://latex2rtf.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX to RTF converter.

%description -l pl.UTF-8
Program do przetwarzania dokumentów z formatu TeX (LaTeX) na format
Rich Text Format, czytany przez programy firmy Microsoft.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_INSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INST_DIR="install -d" \
	INST_BIN=install \
	INST_DAT=install

install doc/latex2rtf.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc doc/credits README ChangeLog Copyright
%attr(755,root,root) %{_bindir}/latex2*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
