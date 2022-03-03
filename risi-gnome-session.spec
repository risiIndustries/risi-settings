Name:           risi-gnome-session
Version:        0.4
Release:        8%{?dist}
Summary:        Session for risiOS

License:        GPLv3+
URL:            https://github.com/risiOS/risi-gnome-session
Source0:        https://github.com/risiOS/risi-gnome-session/archive/refs/heads/main.tar.gz#/%{name}-main.tar.gz

Provides: 	gnome-session-xsession
Provides: 	gnome-session-wayland-session

Requires:	gnome-session
Requires:	gnome-shell-extension-appindicator
Requires:	gnome-shell-extension-drive-menu
Requires:	gnome-shell-extension-risi-gnome
Requires:	gnome-shell-extension-dock-from-dash
Requires:	gnome-shell-extension-sound-output-device-chooser
Requires: adw-gtk-theme

BuildArch:  noarch

%description
GNOME Session for risiOS (allows custom settings and themes)

%prep
%autosetup -n %{name}-main
%build
%install
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0/schemas
mkdir -p %{buildroot}%{_datarootdir}/gnome-session/sessions
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/modes
mkdir -p %{buildroot}%{_datarootdir}/wayland-sessions
mkdir -p %{buildroot}%{_datarootdir}/xsessions
install -m 755 00_risi.gschema.override %{buildroot}%{_datarootdir}/glib-2.0/schemas/00_risi.gschema.override
install -m 755 risi.json %{buildroot}%{_datarootdir}/gnome-shell/modes/risi.json
install -m 755 risi.desktop %{buildroot}%{_datarootdir}/xsessions/risi.desktop
install -m 755 risi.desktop %{buildroot}%{_datarootdir}/wayland-sessions/risi.desktop
install -m 755 risi-wayland.desktop %{buildroot}%{_datarootdir}/wayland-sessions/risi-wayland.desktop
install -m 755 risi-xorg.desktop %{buildroot}%{_datarootdir}/xsessions/risi-wayland.desktop
install -m 755 risi.session %{buildroot}%{_datarootdir}/gnome-session/sessions

%files
%{_datarootdir}/glib-2.0/schemas/00_risi.gschema.override
%{_datarootdir}/gnome-shell/modes/risi.json
%{_datarootdir}/xsessions/risi.desktop
%{_datarootdir}/xsessions/risi-xorg.desktop
%{_datarootdir}/wayland-sessions/risi.desktop
%{_datarootdir}/wayland-sessions/risi-wayland.desktop

%changelog
* Thu Feb 25 2022 PizzaLovingNerd
- Fixed GNOME Shell Theme
- Fixed Wayland session not showing up
- Fixed Settings not working.

* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
