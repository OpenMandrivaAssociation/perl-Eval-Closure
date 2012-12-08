%define upstream_name    Eval-Closure
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Summary:	Safely and cleanly create closures via string eval
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~doy/Eval-Closure-0.04/lib/Eval/Closure.pm
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOY/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
String eval is often used for dynamic code generation. For instance, Moose uses
it heavily, to generate inlined versions of accessors and constructors, which
speeds code up at runtime by a significant amount. String eval is not without
its issues however - it's difficult to control the scope it's used in (which
determines which variables are in scope inside the eval), and it can be quite
slow, especially if doing a large number of evals.

This module attempts to solve both of those problems. It provides an
eval_closure function, which evals a string in a clean environment, other than
a fixed list of specified variables. It also caches the result of the eval, so
that doing repeated evals of the same source, even with a different
environment, will be much faster (but note that the description is part of the
string to be evaled, so it must also be the same (or non-existent) if caching
is to work properly).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE MANIFEST README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-5mdv2012.0
+ Revision: 767797
- fix stupid and anal rpmlint enforcements that does not even show in the build system output.
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.40.0-3
+ Revision: 657320
- bump rel
- re-add buildarch

* Sat Apr 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.40.0-2
+ Revision: 657314
- drop noarch tag

* Sat Apr 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.40.0-1
+ Revision: 657174
- import perl-Eval-Closure

