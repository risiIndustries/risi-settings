Name:           risi-settings
Version:        38
Release:        16%{?dist}
Summary:        Default settings for risiOS

License:        GPLv3+
URL:            https://github.com/risiOS/risi-settings
Source0:        https://github.com/risiOS/risi-settings/archive/refs/heads/main.tar.gz#/%{name}-main.tar.gz

Requires:	gnome-shell-extension-drive-menu
Requires:	gnome-shell-extension-risi-gnome
Requires:	gnome-shell-extension-dock-from-dash
Requires:   gnome-shell-extension-caffeine
Requires:   adw-gtk3

BuildArch:  noarch

%description
risiOS Settings

%prep
%autosetup -n %{name}-main
%build
%install
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0/schemas
cp 00_risi.gschema.override %{buildroot}%{_datarootdir}/glib-2.0/schemas/00_risi.gschema.override

%files
%{_datarootdir}/glib-2.0/schemas/00_risi.gschema.override

%changelog
* Wed Mar 9 2022 PizzaLovingNerd
- Removed GNOME Session, now it's just GNOME settings

* Fri Feb 25 2022 PizzaLovingNerd
- Fixed GNOME Shell Theme
- Fixed Wayland session not showing up
- Fixed Settings not working.

* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
