Summary:	Software to create compressed audio files
Summary(es):	Lame es un gerador de MP3
Summary(pl):	Program do tworzenia skompresowanych plikÛw dºwiÍkowych
Summary(pt_BR):	Lame È um gerador de MP3
Name:		lame
Version:	3.91
Release:	2
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/DºwiÍk
Group(pt_BR):	AplicaÁıes/Som
Source0:	http://telia.dl.sourceforge.net/lame/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc.patch
URL:		http://www.mp3dev.org/mp3/
BuildRequires:	ncurses-devel => 4.2
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libogg-devel
BuildRequires:	nasm
BuildRequires:	autoconf
Requires:	lame-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin

%description
Lame is a program which can be used to create compressed audio files.
(Lame aint MP3 encoder). These audio files can be played back by
popular mp3 players such as mpg123.

%description -l es
LAME es un encoder MP3 GPL.

%description -l pl
Lame jest programem, ktÛry s≥uøy do tworzenia skompresowanych plikÛw
dºwiÍkowych. (Lame nie jest programem do kompresji w formacie MP3).
Stworzone pliki moøna odtwarzaÊ dekoderami MP3, np.: mpg123.

%description -l pt_BR
LAME È um encoder MP3 GPL.

%package libs
Summary:	LAME mp3 encoding library
Summary(pl):	Biblioteka koduj±ca MP3 LAME
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description libs
LAME mp3 encoding library.

%description libs -l pl
Biblioteka koduj±ca MP3 LAME.

%package libs-devel
Summary:	Header files and devel documentation
Summary(es):	Archivos para desarrollo
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja developerska
Summary(pt_BR):	Arquivos para desenvolvimento
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	lame-libs = %{version}

%description libs-devel
Header files and devel documentation for LAME libraries.

%description libs-devel -l es
Archivos de desarrolo.

%description libs-devel -l pl
Pliki nag≥Ûwkowe i dokumentacja developerska bibliotek LAME.

%description libs-devel -l pt_BR
Arquivos de desenvolvimento.

%package libs-static
Summary:	Static LAME library
Summary(es):	Bibliotecas estaticas de desarrollo
Summary(pl):	Biblioteki statyczne LAME
Summary(pt_BR):	Bibliotecas est·ticas de desenvolvimento
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	lame-libs-devel = %{version}

%description libs-static
LAME static libraries.

%description libs-static -l es
Bibliotecas estaticas de desarrollo.

%description libs-static -l pl
Biblioteki statyczne LAME.

%description libs-static -l pt_BR
Bibliotecas est·ticas de desenvolvimento.

%package x11
Summary:	GTK frame analyzer
Summary(pl):	Analizator ramek w GTK
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/DºwiÍk
Group(pt_BR):	AplicaÁıes/Som

%description x11
GTK frame analyzer.

%description x11 -l pl
Analizator ramek w GTK.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure \
	--enable-shared \
	--enable-static \
	--enable-mp3x \
	--enable-mp3rtp \
	--enable-brhist
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f	$RPM_BUILD_ROOT%{_bindir}/mp3x \
	$RPM_BUILD_ROOT%{_xbindir}

gzip -9nf Change* API DEFINES LICENSE TODO USAGE 

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/html/*.{html,css}
%doc {TODO,USAGE}.gz
%attr(755,root,root) %{_bindir}/lame
%attr(755,root,root) %{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*

%files libs
%defattr(644,root,root,755)
%doc LICENSE.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files libs-devel
%defattr(644,root,root,755)
%doc {API,DEFINES}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/lame

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*
