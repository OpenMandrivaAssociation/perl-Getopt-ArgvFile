%define module	Getopt-ArgvFile
%define name	perl-%{module}
%define version 1.10
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interpolates script options from files into @ARGV or another array
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
This module simply interpolates option file hints in @ARGV by the contents of
the pointed files. This enables option reading from files instead of or
additional to the usual reading from the command line. Alternatively, you can
process any array instead of @ARGV which is used by default and mentioned
mostly in this manual.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Getopt/*
%{_mandir}/*/*

