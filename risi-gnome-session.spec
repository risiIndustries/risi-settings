Name:           risi-gnome-session
Version:        0.1
Release:        1%{?dist}
Summary:        Session for risiOS

License:        GPLv3+
URL:            https://github.com/risiOS/risi-gnome-session
Source0:        https://github.com/risiOS/risi-gnome-session/archive/refs/heads/main.tar.gz#/%{name}-main.tar.gz

Provides: 	gnome-session-xsession
Provides: 	gnome-session-wayland-session

Requires:	gnome-session
Requires:	gnome-shell-extension-just-perfection
Requires:	gnome-shell-extension-blur-my-shell
# Requires:	gnome-shell-extension-tiling-assistant <-- Add back once packaged
Requires:	gnome-shell-extension-appindicatorsupport

BuildArch:	noarch

%description
GNOME Session for risiOS (allows custom settings and themes)

%prep
%autosetup -n %{name}-main
%build
%install
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/modes
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/theme
mkdir -p %{buildroot}%{_datarootdir}/wayland-sessions
mkdir -p %{buildroot}%{_datarootdir}/xsessions
install -m 755 10_risi-settings.gschema.override %{buildroot}%{_datarootdir}/glib-2.0/10_risi-settings.gschema.override
install -m 755 risi.json %{buildroot}%{_datarootdir}/gnome-shell/modes/risi.json
install -m 755 risi.css %{buildroot}%{_datarootdir}/gnome-shell/theme/risi.css
install -m 755 risi.desktop %{buildroot}%{_datarootdir}/xsessions/risi.desktop
install -m 755 risi-wayland.desktop %{buildroot}%{_datarootdir}/wayland-sessions/risi-wayland.desktop

%files
/usr/share/glib-2.0/10_risi-settings.gschema.override
/usr/share/gnome-shell/modes/risi.json
/usr/share/gnome-shell/theme/risi.css
/usr/share/xsessions/risi.desktop
/usr/share/wayland-sessions/risi-wayland.desktop

%changelog
* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
