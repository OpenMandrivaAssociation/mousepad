%define debug_package %{nil}

Summary:	A simple text editor for Xfce
Name:		mousepad
Version:	0.3.0
Release:	6
License:	GPLv2+
Group:		Editors
URL:		http://www.xfce.org
Source:		http://archive.xfce.org/src/apps/mousepad/0.3/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtksourceview-2.0)
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
%configure2_5x \
	--disable-static \
	--enable-dbus

%make

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install \
    --remove-category="Application" \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Apr 06 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-8
+ Revision: 789515
- rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-7
+ Revision: 633047
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-6mdv2011.0
+ Revision: 579624
- rebuild for new xfce 4.7.0

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-5mdv2010.1
+ Revision: 543274
- rebuild for mdv 2010.1

* Sat Oct 17 2009 Crispin Boylan <crisb@mandriva.org> 0.2.16-4mdv2010.0
+ Revision: 458044
- Add patch1
- Bump release
- Fix find with patch from ubuntu (upstream #5831)

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2.16-3mdv2010.0
+ Revision: 440120
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-2mdv2009.1
+ Revision: 349164
- rebuild whole xfce

* Sat Feb 28 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.16-1mdv2009.1
+ Revision: 346126
- drop patch 1, not needed anymore
- update to new version 0.2.16

* Sat Jan 03 2009 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.2.14-1mdv2009.1
+ Revision: 324027
- New upstream release

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.13-5mdv2009.1
+ Revision: 294904
- rebuild for new Xfce4.6 beta1

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2.13-4mdv2009.0
+ Revision: 252786
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.13-2mdv2008.1
+ Revision: 170066
- Patch0: fix recent items sort

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.13-1mdv2008.1
+ Revision: 110066
- new version 0.2.13
- new license policy
- spec file clean

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.12-5mdv2008.0
+ Revision: 89948
- rebuild

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-4mdv2008.0
+ Revision: 71244
- remove X-MandrivaLinux from desktop file

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-3mdv2008.0
+ Revision: 32841
- s/imagemagick/ImageMagick

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12-2mdv2008.0
+ Revision: 32817
- spec file clean
- drop old style menu
- tune up desktop file
- add icon macro to %%post and %%postun


* Tue Jan 23 2007 plouf <plouf> 0.2.12-1mdv2007.0
+ Revision: 112308
- New release 0.2.12

* Tue Dec 12 2006 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.2.10-1mdv2007.1
+ Revision: 95212
- New release 0.2.10
- Import mousepad

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 0.2.6-1mdv2007.0
- 0.2.6
- xdg

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.4-2mdk
- Fix BuildRequires

* Wed Apr 26 2006 Jerome Soyer <saispo@mandriva.org> 0.2.4-1mdk
- New release 0.2.4

* Fri Nov 25 2005 Marcel Pol <mpol@mandriva.org> 0.2.2-3mdk
- fix menu

* Tue Aug 02 2005 Marcel Pol <mpol@mandriva.org> 0.2.2-2mdk
- buildrequires ImageMagick

* Tue Apr 05 2005 Charles A Edwards <eslrahc@bellsouth.net> 0.2.2-1mdk
- 0.2.2

* Mon Mar 07 2005 Marcel Pol <mpol@mandrake.org> 0.2.1-1mdk
- 0.2.1
- buildrequires libxfcegui4-devel
- strip binary

* Thu Feb 03 2005 Charles A Edwards <eslrahc@bellsouth.net> 0.1.1-1mdk
- 0.1.1
- change Group to Editors
- BR chrpath and strip /bin

* Sat Jan 22 2005 Charles A Edwards <eslrahc@bellsouth.net> 0.1.0-1mdk
- 1st Mdk release

