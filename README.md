# Septabee Arch package

Build and install on Arch:

```sh
makepkg -si
septabee
```

You can also launch **Septabee** from your desktop's application menu.

The normal Arch `base-devel` build environment is required. `makepkg` uses
libarchive to extract the 7z download, so a separate 7zip dependency is not
needed. The upstream checksum is the flake's SHA-256 converted to hex.

Binaries, helper programs, fonts, and data live together in
`/usr/lib/septabee`. `/usr/bin/septabee` creates the same per-user ABI directory
as the Nix wrapper and launches from the asset directory. Arch's standard
library paths replace Nix's `autoPatchelfHook`; no binary patching is needed.
The two Nix Wayland dependencies map to one Arch `wayland` package.

## Optional realtime capability

The flake's NixOS module separately grants `CAP_SYS_NICE` to the app and sound
helper. The package does not grant this automatically. To reproduce that
capability setup, with Arch's `libcap` installed:

```sh
sudo setcap cap_sys_nice=ep /usr/lib/septabee/septabee /usr/lib/septabee/septabee-sounds
```

This permits elevated scheduling priority. Package upgrades replace the files,
so reapply the command after upgrades if you use it.

## Limitations

The archive includes no license text, including for its bundled fonts.
`license=('custom')` is a placeholder; check upstream redistribution terms
and include the applicable license files before publishing this package.
Building the package does not validate GUI startup, audio, or the app's
runtime LLVM downloads. Additional libraries loaded by plugins or optional
graphics backends may require additional packages.
