#
# Conditional build:
%bcond_without	gtk	# without GTK+ frontend
#
Summary:	Software to create compressed audio files
Summary(es.UTF-8):	Lame es un gerador de MP3
Summary(pl.UTF-8):	Program do tworzenia skompresowanych plików dźwiękowych
Summary(pt_BR.UTF-8):	Lame é um gerador de MP3
Name:		lame
Version:	3.97
Release:	3
# libmp3lame encoder is LGPL v2+, but decoder parts (enabled by default)
# come from old mpg123 code, which was licensed on GPL
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/lame/%{name}-%{version}.tar.gz
# Source0-md5:	90a4acbb730d150dfe80de145126eef7
Patch0:		%{name}-link.patch
Patch1:		%{name}-without_gtk.patch
Patch2:		%{name}-amfix.patch
URL:		http://lame.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
BuildRequires:	libtool
BuildRequires:	nasm
BuildRequires:	ncurses-devel >= 4.2
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lame is a program which can be used to create compressed audio files.
(Lame aint MP3 encoder). These audio files can be played back by
popular MP3 players such as mpg123.

%description -l es.UTF-8
LAME es un encoder MP3 GPL.

%description -l pl.UTF-8
Lame jest programem, który służy do tworzenia skompresowanych plików
dźwiękowych. (Lame nie jest programem do kompresji w formacie MP3).
Stworzone pliki można odtwarzać dekoderami MP3, np.: mpg123.

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
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja developerska
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files and devel documentation for LAME libraries.

%description libs-devel -l es.UTF-8
Archivos de desarrolo.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja developerska bibliotek LAME.

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	%{?with_gtk:--enable-mp3x} \
	--enable-mp3rtp \
	--enable-brhist

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/lame/html

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO USAGE doc/html/*.{html,css}
%attr(755,root,root) %{_bindir}/lame
%attr(755,root,root) %{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*

%files libs
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files libs-devel
%defattr(644,root,root,755)
%doc API DEFINES
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/lame

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with gtk}
%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mp3x
%endif
