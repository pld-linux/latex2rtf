Summary:	LaTeX to RTF converter program
Summary(pl.UTF-8):	Konwerter z formatu LaTeXa do RTF
Name:		latex2rtf
Version:	2.2.1c
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/latex2rtf/%{name}-%{version}.tar.gz
# Source0-md5:	a660ae266969196a96f31b1f1f5d12e5
URL:		http://latex2rtf.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX to RTF converter.

%description -l pl.UTF-8
Program do przetwarzania dokumentów z formatu TeX (LaTeX) na format
Rich Text Format, czytany przez programy firmy Microsoft.

%prep
%setup -q -n %{name}-2.2.1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX" \
	DESTDIR=%{_prefix} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix} \
	MAN_INSTALL=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INST_DIR="install -d" \
	INST_BIN=install \
	INST_DAT=install

install doc/latex2rtf.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc doc/credits README ChangeLog Copyright
%attr(755,root,root) %{_bindir}/latex2png
%attr(755,root,root) %{_bindir}/latex2rtf
%{_datadir}/%{name}
%{_mandir}/man1/latex2png.1*
%{_mandir}/man1/latex2rtf.1*
%{_infodir}/latex2rtf.info*
