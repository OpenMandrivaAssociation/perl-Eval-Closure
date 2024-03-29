%define	modname	Eval-Closure
%define modver 0.14

Summary:	Safely and cleanly create closures via string eval
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Eval::Closure
Source0:	http://www.cpan.org/authors/id/D/DO/DOY/Eval-Closure-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl-devel

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
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE MANIFEST README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


