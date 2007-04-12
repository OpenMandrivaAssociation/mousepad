%define name    mousepad 
%define version 0.2.12
%define iconname %{name}.png
%define debug_package %{nil}

Summary: A simple text editor for Xfce
Name: %{name}
Version: %{version}
Release: %mkrel 1
License: GPL
Group: Editors
Source: %{name}-%{version}.tar.bz2
URL: http://erikharrison.net/software/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:  gtk2-devel
BuildRequires:  chrpath
BuildRequires:	libxfcegui4-devel
BuildRequires:	ImageMagick
BuildRequires:  perl(XML::Parser)
BuildRequires: desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

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
%setup -q -n %{name}-%{version}

%build 
 
%configure2_5x

%make

%install
rm -Rf %{buildroot} 
%makeinstall_std

# fix rpath
chrpath -d $RPM_BUILD_ROOT%{_bindir}/%{name} 
# strip binary
strip $RPM_BUILD_ROOT%{_bindir}/%{name}


%find_lang %{name} --with-gnome

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
convert %{name}.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname} 
convert %{name}.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 

 
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}):\
	command="%{_bindir}/%{name}"  \
	icon="%{iconname}" \
	title="Mousepad" \
	longtitle="Text Editor" \
	needs="x11" \
	section="More Applications/Editors" \
        xdg="true"
EOF   

desktop-file-install --vendor="" \
-remove-category="Application" \
--add-category="X-MandrivaLinux-MoreApplications-Editors" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
 
 
%post
%{update_menus}
%{update_desktop_database}

%postun
%{clean_menus}
%{clean_desktop_database}

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README 
%{_bindir}/* 
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/* 
%{_menudir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}


