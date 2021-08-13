Name:           risi-gnome-session
Version:        0.1
Release:        2%{?dist}
Summary:        Session for risiOS

License:        GPLv3+
URL:            https://github.com/risiOS/risi-gnome-session

Source0:        10_risi-settings.gschema.override
Source1:        risi.css
Source2:        risi.desktop
Source3:        risi.json
Source4:        risi-wayland.desktop

Provides: 	gnome-session-xsession
Provides: 	gnome-session-wayland-session

Requires:	gnome-session
Requires:	gnome-shell-extension-just-perfection
Requires:	gnome-shell-extension-blur-my-shell
# Requires:	gnome-shell-extension-tiling-assistant <-- Add back once packaged
Requires:	gnome-shell-extension-appindicator-support

BuildArch:	noarch

%description
GNOME Session for risiOS (allows custom settings and themes)

%prep
%autosetup
%build
%install
mkdir -p /usr/share/glib-2.0
mkdir -p /usr/share/gnome-shell/modes
mkdir -p /usr/share/gnome-shell/theme
mkdir -p /usr/share/wayland-sessions
mkdir -p /usr/share/xsessions
install -m 755 10_risi-settings.gschema.override %{buildroot}%{_datarootdir}/glib-2.0/10_risi-settings.gschema.override
install -m 755 risi.json %{buildroot}%{_datarootdir}/gnome-shell/modes/risi.json
install -m 755 risi.css %{buildroot}%{_datarootdir}/gnome-shell/theme/risi.css
install -m 755 risi.desktop %{buildroot}%{_datarootdir}/usr/share/xsessions/risi.desktop
install -m 755 risi-wayland.desktop %{buildroot}%{_datarootdir}/usr/share/wayland-sessions/risi-wayland.desktop
install -m 755 risi-wayland.desktop %{buildroot}%{_datarootdir}/usr/share/xsessions/risi-wayland.desktop

%files
/usr/share/glib-2.0/10_risi-settings.gschema.override
/usr/share/gnome-shell/modes/risi.json
/usr/share/gnome-shell/theme/risi.css
/usr/share/xsessions/risi.desktop
/usr/share/xsessions/risi-wayland.desktop
/usr/share/wayland-sessions/risi-wayland.desktop

%changelog
* Mon Aug 12 2021 PizzaLovingNerd
- Fixed GNOME Shell Theme
- Fixed Wayland session not showing up
- Fixed Settings not working.

* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
