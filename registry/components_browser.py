# Copyright The Phorepoc Authors
# SPDX-License-Identifier: Apache-2.0

"""components_browser -- the browser frontend (merged into core's registry when this repository is a layer:
PHOREPOC_ADAPTATIONS=<board adaptations>:<path to webengine>:<path to browser>, see the pdk's tools/emitter/paths.py). Paths
are relative to the merged OS tree.

  phebrowser      the browser (phebrowser.exe, "Browser" in the launcher): the image's copy and the x32 SIS
  phebrowser_arm  the same app as a stock-loader ARM image, for the ARM SIS (Phorepoc phones and older Symbian^3 phones)

Build:  phe component resources phebrowser && phe component build phebrowser        (ARM SIS: -arch arm phebrowser_arm)
Package: recipes/sis.sh (make_sis.py --rom-upgrade with the licence files)

An image built with this layer carries a ROM stub for the app (`rom_stub`, the pdk's tools/rom_stubs.py), so the released SIS
(same UID, ROM-upgrade flag) installs over the image's copy and uninstalling it brings that copy back.
"""
import os

from paths import OS_ROOT

_SRC = os.path.join(OS_ROOT, "src", "phebrowser")
_ICON = r"resource\apps\phebrowser_icon.mbm=" + os.path.join(_SRC, "data", "phebrowser_icon.mbm")

COMPONENTS = {
    # sis: laid out RAM-loadable (the SIS installs this build). heap_max = the image's rom_heap.tsv value, which only the ROM copy
    # gets: an installed copy keeps its image header's (engines allocate through the process heap).
    "phebrowser": dict(needs="webengine", mmp=os.path.join(_SRC, "phebrowser.mmp"), sis=True, heap_max=0x10000000,
                       rom_data=[_ICON],
                       rom_stub=dict(name="Phorepoc Browser", files=[r"sys\bin\phebrowser.exe", r"resource\apps\phebrowser.rsc",
                                                                     r"resource\apps\phebrowser_icon.mbm",
                                                                     r"private\10003a3f\import\apps\phebrowser_reg.rsc"])),
    # stock loader (`device`): their framework DLLs serve the 2010 ordinals it imports; no _ZTI data imports, which stock firmware
    # does not serve. package_only: never built by --all (it would overwrite the image's phebrowser.exe); only package.yml names it.
    "phebrowser_arm": dict(needs="webengine", mmp=os.path.join(_SRC, "phebrowser.mmp"), rom="phebrowser.exe",
                           package_only=True, arm_only=True, device=True, sis=True, rtti=True, import_typeinfo=False,
                           static_ctors=True, arm_heap_max=0x10000000, rom_data=[_ICON]),
}
