#
# Conditional build:
%bcond_without	gtk	# GTK+ frontend
#
Summary:	Software to create compressed audio files
Summary(es.UTF-8):	Lame es un gerador de MP3
Summary(pl.UTF-8):	Program do tworzenia skompresowanych plików dźwiękowych
Summary(pt_BR.UTF-8):	Lame é um gerador de MP3
Name:		lame
Version:	3.100
Release:	1
# libmp3lame encoder is LGPL v2+, but decoder parts (enabled by default)
# come from old mpg123 code, which was licensed on GPL
License:	GPL v2+ (MP3 decoder), LGPL v2+ (the rest)
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/lame/%{name}-%{version}.tar.gz
# Source0-md5:	83e260acbe4389b54fe08e0bdbf7cddb
Patch0:		%{name}-link.patch
Patch1:		%{name}-without_gtk.patch
Patch2:		%{name}-exports.patch
Patch3:		%{name}-sse.patch
URL:		http://lame.sourceforge.net/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
# with --with-fileio=sndfile (but disables stdin input)
#BuildRequires:	libsndfile-devel >= 1.0.2
BuildRequires:	libtool
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	ncurses-devel >= 4.2
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lame (LAME Ain't an MP3 Encoder) is a program which can be used to
create compressed audio files. These audio files can be played back by
popular MP3 players such as mpg123.

%description -l es.UTF-8
LAME es un encoder MP3 GPL.

%description -l pl.UTF-8
Lame (LAME Ain't an MP3 Encoder - LAME to nie program do kodowania
MP3) jest programem, który służy do tworzenia skompresowanych plików
dźwiękowych. Stworzone pliki można odtwarzać dekoderami MP3, np.:
mpg123.

%description -l pt_BR.UTF-8
LAME é um encoder MP3 GPL.

%package libs
Summary:	LAME MP3 encoding library
Summary(pl.UTF-8):	Biblioteka kodująca MP3 LAME
Group:		Libraries

%description libs
LAME MP3 encoding library.

%description libs -l pl.UTF-8
Biblioteka kodująca MP3 LAME.

%package libs-devel
Summary:	Header files and devel documentation
Summary(es.UTF-8):	Archivos para desarrollo
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja deweloperska
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files and devel documentation for LAME libraries.

%description libs-devel -l es.UTF-8
Archivos de desarrolo.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja deweloperska bibliotek LAME.

%description libs-devel -l pt_BR.UTF-8
Arquivos de desenvolvimento.

%package libs-static
Summary:	Static LAME library
Summary(es.UTF-8):	Bibliotecas estaticas de desarrollo
Summary(pl.UTF-8):	Biblioteki statyczne LAME
Summary(pt_BR.UTF-8):	Bibliotecas estáticas de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
LAME static libraries.

%description libs-static -l es.UTF-8
Bibliotecas estaticas de desarrollo.

%description libs-static -l pl.UTF-8
Biblioteki statyczne LAME.

%description libs-static -l pt_BR.UTF-8
Bibliotecas estáticas de desenvolvimento.

%package x11
Summary:	GTK+ frame analyzer
Summary(pl.UTF-8):	Analizator ramek w GTK+
Group:		Applications/Sound
Requires:	%{name}-libs = %{version}-%{release}

%description x11
GTK+ frame analyzer.

%description x11 -l pl.UTF-8
Analizator ramek w GTK+.

%prep
%setup -q
%patch0 -p1
%{!?with_gtk:%patch1 -p1}
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-cpml \
	--enable-dynamic-frontends \
	%{?with_gtk:--enable-mp3x} \
	--enable-mp3rtp \
%ifarch %{ix86}
	--enable-nasm
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/lame/html

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO USAGE doc/html/*.html
%attr(755,root,root) %{_bindir}/lame
%attr(755,root,root) %{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*

%files libs
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libmp3lame.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmp3lame.so.0

%files libs-devel
%defattr(644,root,root,755)
%doc API DEFINES
%attr(755,root,root) %{_libdir}/libmp3lame.so
%{_libdir}/libmp3lame.la
%{_includedir}/lame

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libmp3lame.a

%if %{with gtk}
%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mp3x
%endif
