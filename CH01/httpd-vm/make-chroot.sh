#! /bin/bash

BIN=$1
CHROOT_FOLDER=$2

# TODO verify if BIN exist otherwise exit
# TODO verify if CHROOT_FOLDER exists otherwise exit

DEPS=$(ldd -v "${BIN}" | grep : | grep -v "Version information" | sed s'/.$//')

echo "${DEPS}" | while IFS=$'\n' read -r dep
do
    # Todo verify if file is already there otherwise don't copy it
    echo "Copy ${dep} in ${CHROOT_FOLDER}"
done

echo "Done"