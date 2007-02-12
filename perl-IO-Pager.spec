#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Pager
Summary:	IO::Pager - Select a pager, optionally pipe output if destination is a TTY
Summary(pl.UTF-8):   IO::Pager - wybór programu stronicującego lub potoku jeśli celem jest TTY
Name:		perl-IO-Pager
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	dda54801e176089d9b93e05dc07324a4
URL:		http://search.cpan.org/dist/IO-Pager/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/IO/Pager
%{perl_vendorlib}/IO/*.pm
%{_mandir}/man3/*
