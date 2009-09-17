#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PerlIO
%define	pnam	gzip
Summary:	PerlIO::gzip - Perl extension to provide a PerlIO layer to gzip/gunzip
Summary(pl.UTF-8):	PerlIO::gzip - rozszerzenie perla dostarczające warstwę PerlIO do operacji gzip/gunzip
Name:		perl-PerlIO-gzip
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NW/NWCLARK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	933fdf283a0d2739f7630420569e3b24
URL:		http://search.cpan.org/dist/PerlIO-gzip/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the
format used by the gzip program. Compression and Decompression are
implemented, but not together. If you attempt to open a file for
reading and writing the open will fail.

%description -l pl.UTF-8
PerlIO::gzip dostarcza wartstwę PerlIO, która potrafi operować na
plikach w formatach używanych przez program gzip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/PerlIO/*.pm
%dir %{perl_vendorarch}/auto/PerlIO/gzip
%{perl_vendorarch}/auto/PerlIO/gzip/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PerlIO/gzip/*.so
%{_mandir}/man3/*
