%define iconname %{name}.png
%define debug_package %{nil}

Summary:	A simple text editor for Xfce
Name:		mousepad
Version:	0.2.12
Release:	%mkrel 4
License:	GPL
Group:		Editors
URL:		http://www.xfce.org
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel
BuildRequires:	chrpath
BuildRequires:	libxfcegui4-devel
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%configure2_5x 

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# fix rpath
chrpath -d %{buildroot}%{_bindir}/%{name}
# strip binary
strip %{buildroot}%{_bindir}/%{name}


%find_lang %{name} --with-gnome

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert %{name}.png -geometry 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{iconname}
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{iconname} 
convert %{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{iconname} 


desktop-file-install \
    --remove-category="Application" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
 
 
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README 
%{_bindir}/* 
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/* 
%{_iconsdir}/hicolor/*/apps/*.png
