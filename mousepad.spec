%define debug_package %{nil}

Summary:	A simple text editor for Xfce
Name:		mousepad
Version:	0.2.16
Release:	8
License:	GPLv2+
Group:		Editors
URL:		http://www.xfce.org
Source:		http://mocha.xfce.org/archive/xfce-4.6.0/src/%{name}-%{version}.tar.bz2
Patch1:		mousepad-0.2.16-find_gtk2.18.patch
BuildRequires:	gtk2-devel
BuildRequires:	chrpath
BuildRequires:	libxfcegui4-devel >= 4.6.0
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils

%description
Mousepad is a text editor for Xfce based on Leafpad. The initial reason for
Mousepad was to provide printing support, which would have been difficult
for Leafpad for various reasons.

Although some features are under development, currently Mousepad has the
following features:

    * Complete support for UTF-8 text
    * Cut/Copy/Paste and Select All text
    * Search and Replace
    * Font selecton
    * Word Wrap
    * Character coding selection
    * Auto character coding detection (UTF-8 and some codesets)
    * Manual codeset setting
    * Infinite Undo/Redo by word
    * Auto Indent
    * Multi-line Indent
    * Display line numbers
    * Drag and Drop
    * Printing

%prep
%setup -q
%patch1 -p1

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# fix rpath
chrpath -d %{buildroot}%{_bindir}/%{name}
# strip binary
strip %{buildroot}%{_bindir}/%{name}


%find_lang %{name} --with-gnome %{name}.lang

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert %{name}.png -geometry 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert %{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png


desktop-file-install \
    --remove-category="Application" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*.png
