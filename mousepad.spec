#define debug_package %{nil}
%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	A simple text editor for Xfce
Name:		mousepad
Version:	0.6.3
Release:	1
License:	GPLv2+
Group:		Editors
URL:		https://www.xfce.org
Source0:	https://archive.xfce.org/src/apps/mousepad/%{url_ver}/%{name}-%{version}.tar.bz2
#Patch0:		0001-Port-to-gtksourceview-4.patch

BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gspell-1)
BuildRequires:	intltool

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
%autopatch -p1

%build
%configure \
	--disable-static \
	--enable-dbus \
	--enable-gtk3=yes \
	--enable-keyfile-settings

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/*
%{_libdir}/libmousepad.so*
%{_datadir}/applications/org.xfce.mousepad.desktop
%{_datadir}/applications/org.xfce.mousepad-settings.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
#{_datadir}/polkit-1/actions/org.xfce.mousepad.policy
%{_datadir}/metainfo/org.xfce.mousepad.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/org.xfce.mousepad.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.mousepad.svg
