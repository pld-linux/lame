Summary:	Software to create compressed audio files
Summary(pl):	Program do tworzenia skompresowanych plików d¼wiêkowych
Name:		lame
Version:	3.51
Release:	3
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	ftp://geek.rcc.se/pub/mp3encoder/lame/%{name}%{version}.tar.gz
Patch0:		lame-tinfo.patch
Buildrequires:	ncurses-devel => 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lame is a program which can be used to create compressed audio files.
(Lame aint MP3 encoder). These audio files can be played back by
popular mp3 players such as mpg123.

%description -l pl
Lame jest programem, który s³u¿y do tworzenia skompresowanych plików
d¼wiêkowych. (Lame nie jest programem do kompresji w formacie MP3).
Stworzone pliki mo¿na odtwarzaæ dekoderami MP3, np.: mpg123.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make} CC_OPTS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

# directories
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

# binary
install -s lame $RPM_BUILD_ROOT%{_bindir}

# scripts
install auenc $RPM_BUILD_ROOT%{_bindir}
install mlame $RPM_BUILD_ROOT%{_bindir}

# documentation
install doc/man/lame.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf COPYING USAGE README $RPM_BUILD_ROOT%{_mandir}/man1/lame.1
cd doc
mv html lame-%{version}
tar czf lame-%{version}.tar.gz lame-%{version}
mv lame-%{version}.tar.gz ..

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYING,USAGE,README,lame-%{version}.tar}.gz
%attr(755,root,root) %{_bindir}/lame
%attr(755,root,root) %{_bindir}/auenc
%attr(755,root,root) %{_bindir}/mlame
%{_mandir}/man1/*
