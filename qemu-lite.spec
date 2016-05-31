#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qemu-lite
Version  : 2.6.0
Release  : 12
URL      : http://wiki.qemu-project.org/download/qemu-2.6.0.tar.bz2
Source0  : http://wiki.qemu-project.org/download/qemu-2.6.0.tar.bz2
Summary  : OpenBIOS development utilities
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 MIT
Requires: qemu-lite-bin
Requires: qemu-lite-data
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : numactl-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : python-dev
BuildRequires : zlib-dev
Patch1: configure.patch
Patch2: qemu-acpi-0001-cache-cpuid.patch
Patch3: qemu-acpi-0002-add-pc-full.patch
Patch4: qemu-acpi-0003-load-from-kernel.patch
Patch5: qemu-acpi-0004-boot-uncompressed-kernel.patch
Patch6: qemu-acpi-0005-add-pc-lite-platform.patch
Patch7: qemu-acpi-0006-make-platform-configurable.patch
Patch8: qemu-acpi-0007-remove-find_i440fx.patch
Patch9: qemu-acpi-0008-vcpu-initialization-in-parallel.patch
Patch10: qemu-acpi-0009-expose-struct-BiosLinkerLoaderEntry.patch
Patch11: qemu-acpi-0010-expose-acpi_checksum.patch
Patch12: qemu-acpi-0011-patch-guest-ACPI-in-pc-lite.patch
Patch13: qemu-acpi-0012-set-LPC-pm_base.patch
Patch14: qemu-acpi-0013-create-MCFG-in-guest-ACPI.patch

%description
This package contains the OpenBIOS development utilities.

There are
* toke - an IEEE 1275-1994 compliant FCode tokenizer
* detok - an IEEE 1275-1994 compliant FCode detokenizer
* paflof - a forth kernel running in user space
* an fcode bytecode evaluator running in paflof

See /usr/share/doc/packages/openbios for details and examples.

Authors:
--------
    Stefan Reinauer <stepan@openbios.net>
    Segher Boessenkool <segher@openbios.net>

%package bin
Summary: bin components for the qemu-lite package.
Group: Binaries
Requires: qemu-lite-data

%description bin
bin components for the qemu-lite package.


%package data
Summary: data components for the qemu-lite package.
Group: Data

%description data
data components for the qemu-lite package.


%prep
%setup -q -n qemu-2.6.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%configure --disable-static --disable-bluez \
--disable-brlapi \
--disable-bzip2 \
--disable-curl \
--disable-curses \
--disable-debug-tcg \
--disable-fdt \
--disable-glusterfs \
--disable-gtk \
--disable-libiscsi \
--disable-libnfs \
--disable-libssh2 \
--disable-libusb \
--disable-linux-aio \
--disable-lzo \
--disable-opengl \
--disable-qom-cast-debug \
--disable-rbd \
--disable-rdma \
--disable-sdl \
--disable-seccomp \
--disable-slirp \
--disable-snappy \
--disable-spice \
--disable-strip \
--disable-tcg-interpreter \
--disable-tcmalloc \
--disable-tools \
--disable-tpm \
--disable-usb-redir \
--disable-uuid \
--disable-vnc \
--disable-vnc-{jpeg,png,sasl} \
--disable-vte \
--disable-xen \
--enable-attr \
--enable-cap-ng \
--enable-kvm \
--enable-virtfs \
--target-list=x86_64-softmmu \
--extra-cflags="-fno-semantic-interposition -O3 -falign-functions=32" \
--datadir=/usr/share/qemu-lite \
--libdir=/usr/lib64/qemu-lite \
--libexecdir=/usr/libexec/qemu-lite
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
for file in %{buildroot}/usr/bin/*
do
dir=$(dirname "$file")
bin=$(basename "$file")
new=$(echo "$bin"|sed -e 's/qemu-/qemu-lite-/g' -e 's/ivshmem-/ivshmem-lite-/g' -e 's/virtfs-/virtfs-lite-/g')
mv "$file" "$dir/$new"
done
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qemu-lite-ga
/usr/bin/qemu-lite-system-x86_64
/usr/bin/virtfs-lite-proxy-helper
/usr/libexec/qemu-lite/qemu-bridge-helper

%files data
%defattr(-,root,root,-)
/usr/share/qemu-lite/qemu/QEMU,cgthree.bin
/usr/share/qemu-lite/qemu/QEMU,tcx.bin
/usr/share/qemu-lite/qemu/acpi-dsdt.aml
/usr/share/qemu-lite/qemu/bamboo.dtb
/usr/share/qemu-lite/qemu/bios-256k.bin
/usr/share/qemu-lite/qemu/bios.bin
/usr/share/qemu-lite/qemu/efi-e1000.rom
/usr/share/qemu-lite/qemu/efi-eepro100.rom
/usr/share/qemu-lite/qemu/efi-ne2k_pci.rom
/usr/share/qemu-lite/qemu/efi-pcnet.rom
/usr/share/qemu-lite/qemu/efi-rtl8139.rom
/usr/share/qemu-lite/qemu/efi-virtio.rom
/usr/share/qemu-lite/qemu/keymaps/ar
/usr/share/qemu-lite/qemu/keymaps/bepo
/usr/share/qemu-lite/qemu/keymaps/common
/usr/share/qemu-lite/qemu/keymaps/cz
/usr/share/qemu-lite/qemu/keymaps/da
/usr/share/qemu-lite/qemu/keymaps/de
/usr/share/qemu-lite/qemu/keymaps/de-ch
/usr/share/qemu-lite/qemu/keymaps/en-gb
/usr/share/qemu-lite/qemu/keymaps/en-us
/usr/share/qemu-lite/qemu/keymaps/es
/usr/share/qemu-lite/qemu/keymaps/et
/usr/share/qemu-lite/qemu/keymaps/fi
/usr/share/qemu-lite/qemu/keymaps/fo
/usr/share/qemu-lite/qemu/keymaps/fr
/usr/share/qemu-lite/qemu/keymaps/fr-be
/usr/share/qemu-lite/qemu/keymaps/fr-ca
/usr/share/qemu-lite/qemu/keymaps/fr-ch
/usr/share/qemu-lite/qemu/keymaps/hr
/usr/share/qemu-lite/qemu/keymaps/hu
/usr/share/qemu-lite/qemu/keymaps/is
/usr/share/qemu-lite/qemu/keymaps/it
/usr/share/qemu-lite/qemu/keymaps/ja
/usr/share/qemu-lite/qemu/keymaps/lt
/usr/share/qemu-lite/qemu/keymaps/lv
/usr/share/qemu-lite/qemu/keymaps/mk
/usr/share/qemu-lite/qemu/keymaps/modifiers
/usr/share/qemu-lite/qemu/keymaps/nl
/usr/share/qemu-lite/qemu/keymaps/nl-be
/usr/share/qemu-lite/qemu/keymaps/no
/usr/share/qemu-lite/qemu/keymaps/pl
/usr/share/qemu-lite/qemu/keymaps/pt
/usr/share/qemu-lite/qemu/keymaps/pt-br
/usr/share/qemu-lite/qemu/keymaps/ru
/usr/share/qemu-lite/qemu/keymaps/sl
/usr/share/qemu-lite/qemu/keymaps/sv
/usr/share/qemu-lite/qemu/keymaps/th
/usr/share/qemu-lite/qemu/keymaps/tr
/usr/share/qemu-lite/qemu/kvmvapic.bin
/usr/share/qemu-lite/qemu/linuxboot.bin
/usr/share/qemu-lite/qemu/multiboot.bin
/usr/share/qemu-lite/qemu/openbios-ppc
/usr/share/qemu-lite/qemu/openbios-sparc32
/usr/share/qemu-lite/qemu/openbios-sparc64
/usr/share/qemu-lite/qemu/palcode-clipper
/usr/share/qemu-lite/qemu/petalogix-ml605.dtb
/usr/share/qemu-lite/qemu/petalogix-s3adsp1800.dtb
/usr/share/qemu-lite/qemu/ppc_rom.bin
/usr/share/qemu-lite/qemu/pxe-e1000.rom
/usr/share/qemu-lite/qemu/pxe-eepro100.rom
/usr/share/qemu-lite/qemu/pxe-ne2k_pci.rom
/usr/share/qemu-lite/qemu/pxe-pcnet.rom
/usr/share/qemu-lite/qemu/pxe-rtl8139.rom
/usr/share/qemu-lite/qemu/pxe-virtio.rom
/usr/share/qemu-lite/qemu/qemu-icon.bmp
/usr/share/qemu-lite/qemu/qemu_logo_no_text.svg
/usr/share/qemu-lite/qemu/s390-ccw.img
/usr/share/qemu-lite/qemu/sgabios.bin
/usr/share/qemu-lite/qemu/slof.bin
/usr/share/qemu-lite/qemu/spapr-rtas.bin
/usr/share/qemu-lite/qemu/trace-events
/usr/share/qemu-lite/qemu/u-boot.e500
/usr/share/qemu-lite/qemu/vgabios-cirrus.bin
/usr/share/qemu-lite/qemu/vgabios-qxl.bin
/usr/share/qemu-lite/qemu/vgabios-stdvga.bin
/usr/share/qemu-lite/qemu/vgabios-virtio.bin
/usr/share/qemu-lite/qemu/vgabios-vmware.bin
/usr/share/qemu-lite/qemu/vgabios.bin
