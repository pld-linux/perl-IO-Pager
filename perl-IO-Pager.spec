#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Pager
Summary:	IO::Pager - Select a pager, optionally pipe output if destination is a TTY
Summary(pl.UTF-8):	IO::Pager - wybór programu stronicującego lub potoku jeśli celem jest TTY
Name:		perl-IO-Pager
Version:	2.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/J/JP/JPIERCE/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	facc50a75059c0c6e2997721860fba92
URL:		http://search.cpan.org/dist/IO-Pager/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Which
BuildRequires:	perl-Term-ReadKey
%endif
Requires:	perl-File-Which
Requires:	perl-Term-ReadKey
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Select a pager, optionally pipe output if destination is a TTY.

%description -l pl.UTF-8
Wybór programu stronicującego i opcjonalne przekazanie wyjścia do
potoku, jeśli celem jest TTY.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:echo "Y" | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# the installed library copy of tp keeps the upstream /usr/local/bin/perl shebang
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Pager/tp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tp
%{perl_vendorlib}/IO/Pager
%{perl_vendorlib}/IO/Pager.pm
%{_mandir}/man1/tp.1p*
%{_mandir}/man3/IO::Pager*.3pm*
