pkgname=septabee-bin
# Arch versions cannot contain hyphens; preserve the flake's yeet-44 label.
pkgver=0.1
pkgrel=3
pkgdesc='Septabee (upstream prebuilt Linux binaries)'
arch=('x86_64')
url='https://septabee.nekoweb.org/'
# The archive contains no license; verify upstream terms before redistribution.
license=('custom')
depends=('bash' 'glibc' 'gcc-libs' 'libpng' 'zlib' 'vulkan-icd-loader'
  'freetype2' 'pipewire' 'libx11' 'lilv' 'zstd' 'ncurses'
  'wayland' 'libxkbcommon' 'libcap' 'llvm')
install=septabee.install
provides=('septabee')
conflicts=('septabee')
options=('!strip' '!debug')
source=('septabee_linux_B_T2.7z::https://septabee.nekoweb.org/important_stuff/SEPTABEE_DOWNLOADS/version_B/septabee_linux_B_T2.7z'
  'septabee-launcher'
  'septabee.desktop'
  'septabee.png')
sha256sums=('38c9db4414e4bbcca2e1bdc0cbb77bd046c1fded9087e3dfccad8ef2a445a1a0'
  'fba9ca7235767883bc1189b652d0a21a6bfaa184019c6a9a6eab00ea8272b8ff'
  '11c495920ec8682a8f67c28fff923aaf4ae62ba6bef6605c48f5af969789f192'
  '4173020d11dc4545b6d1788a671c854c6662858b378aef4d0f5da20b3c5762b6')

package() {
  install -d "$pkgdir/usr/lib/septabee" "$pkgdir/usr/bin"
  install -m644 "$srcdir/linux/"*.ttf "$srcdir/linux/septabee.data" \
    "$srcdir/linux/theme.bee" "$pkgdir/usr/lib/septabee/"
  install -m755 "$srcdir/linux/septabee" "$srcdir/linux/septabee-sounds" \
    "$srcdir/linux/septabee-watchdawg" "$pkgdir/usr/lib/septabee/"
  install -m755 "$srcdir/septabee-launcher" "$pkgdir/usr/bin/septabee"
  install -Dm644 "$srcdir/septabee.desktop" \
    "$pkgdir/usr/share/applications/septabee.desktop"
  install -Dm644 "$srcdir/septabee.png" \
    "$pkgdir/usr/share/icons/hicolor/256x256/apps/septabee.png"
}
