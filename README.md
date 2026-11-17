# s60-browser-shell

The browser of [Phorepoc OS](https://github.com/Phorepoc): tabs with a tab grid, private tabs, light and dark themes, the
address bar at the top or the bottom, a choice of search engine, downloads. The app (`phebrowser.exe`, "Browser" in the
launcher) is custom-drawn with the Etesian design language. It draws pages with a web engine that it finds at run time
through the [webengine](https://github.com/Phorepoc/webengine) interface: install one from Catalogue,
[WebKit](https://github.com/Phorepoc/webkit-symbian) or [NetSurf](https://github.com/Phorepoc/netsurf-symbian). No engine is
part of this repository, its packages or any image.

It is an S60 shell: built on CONE and the S60 platform APIs, so it also aims to run on older Nokia S60 devices. Other
shells (Qt 4.8, GTK) can be written over the same [webengine](https://github.com/Phorepoc/webengine) interface and reuse
the same engine packages.

## Two ways to get it

**Built into an image.** This repository is a layer, like [catalogue](https://github.com/Phorepoc/catalogue): it brings an
`os/` tree and a `registry/`. Add it after `webengine` to a board's `REPOS` in `board.conf` (or to `PHOREPOC_ADAPTATIONS` in
a local build) and the browser is part of the image, with a ROM stub so the released SIS can update it.

**Installed from Catalogue.** Every release has `browser-arm.sis` (Phorepoc phones and older Symbian^3 phones) and
`browser-x32.sis` (the PC), built by the [release workflow](.github/workflows/release.yml) with the pdk's `package.yml`.
On Phorepoc the SIS installs over the image's copy (the ROM-upgrade flag against the image's stub); uninstalling it
brings that copy back.

## License

EPL-2.0 OR GPL-2.0-or-later (LICENSE, LICENSES/EPL-2.0.txt). See NOTICE and AUTHORS.
