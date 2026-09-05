# Septabee Arch package

Inspired by and ported from the Nix flakes from [Fiona42069](https://github.com/Fiona42069/septabee-flake/blob/main/flake.nix) and [TaeruAlethea](https://github.com/TaeruAlethea/nix-config/blob/main/flake.nix)

Build and install on Arch:

```sh
makepkg -si
septabee
```

The normal Arch `base-devel` build environment is required. `makepkg` uses
libarchive to extract the 7z download, so a separate 7zip dependency is not
needed. The upstream checksum is the original flake's SHA-256 converted to hex.

Binaries, helper programs, fonts, and data live together in
`/usr/lib/septabee`. `/usr/bin/septabee` creates the same per-user ABI directory
as the Nix wrapper and launches from the asset directory. Arch's standard
library paths replace Nix's `autoPatchelfHook`; no binary patching is needed.
The two Nix Wayland dependencies map to one Arch `wayland` package.

## LLVM/JIT runtime

The package includes Septabee's ABI-8 JIT runtime (release 2), downloaded and
checksum-verified at build time. Python is needed only to extract its custom
SBRT container during the build. The system `llvm` package is not required.

On launch, a fresh or incomplete runtime directory is populated from the
packaged copy into `$XDG_DATA_HOME/Septabee/llvm-stuffs/abi-8` (default:
`~/.local/share/Septabee/llvm-stuffs/abi-8`). Existing complete runtimes are
preserved, including updates installed by the app. No online installer is
needed for a fresh installation of this packaged version.

## Realtime capability

The desktop entry starts Septabee through a transient systemd user service
with `LimitRTTIME=infinity`. This prevents a zero realtime CPU-time limit
inherited from the desktop launcher from disabling audio. Terminal launches
continue to use `/usr/bin/septabee` directly.

The package grants `CAP_SYS_NICE` to the app and sound helper after installation
and upgrades through `septabee.install`, matching the flake's NixOS module.
This permits elevated scheduling priority.

## Limitations

The archive includes no license text, including for its bundled fonts.
`license=('custom')` is a placeholder; check upstream redistribution terms
and include the applicable license files before publishing this package,
including terms for the bundled JIT runtime.
Building the package does not validate GUI startup or audio. Additional libraries loaded by plugins or optional
graphics backends may require additional packages.
