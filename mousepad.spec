%define debug_package %{nil}
%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	A simple text editor for Xfce
Name:		mousepad
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		Editors
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/mousepad/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	intltool
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

%build
%configure \
	--disable-static \
	--enable-dbus \
	--enable-gtk3=yes

%make_build

%install
%make_install

%find_lang %{name}

desktop-file-install \
    --remove-category="Application" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy


