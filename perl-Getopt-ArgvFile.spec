%define upstream_name	 Getopt-ArgvFile
Name:		perl-%{upstream_name}
Version:	1.11
Release:	6

Summary:	Interpolates script options from files into @ARGV or another array
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Getopt-ArgvFile
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSTENZEL/Getopt-ArgvFile-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module simply interpolates option file hints in @ARGV by the contents of
the pointed files. This enables option reading from files instead of or
additional to the usual reading from the command line. Alternatively, you can
process any array instead of @ARGV which is used by default and mentioned
mostly in this manual.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Getopt/*
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 407751
- rebuild using %1.11 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.11-3mdv2009.0
+ Revision: 257092
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.11-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.0
+ Revision: 20098
- 1.11


* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.10-1mdk
- Initial Mandriva release.

