%define upstream_name	 Getopt-ArgvFile
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Interpolates script options from files into @ARGV or another array
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module simply interpolates option file hints in @ARGV by the contents of
the pointed files. This enables option reading from files instead of or
additional to the usual reading from the command line. Alternatively, you can
process any array instead of @ARGV which is used by default and mentioned
mostly in this manual.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
