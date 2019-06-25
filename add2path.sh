#! /bin/bash

PYTHON_SITE_PACKAGES=$(python -m site --user-site)
AVL_PACKAGE_DIR=$(pwd)
echo "$PYTHON_SITE_PACKAGES/avl.pth"
echo $AVL_PACKAGE_DIR > "$PYTHON_SITE_PACKAGES/avl.pth"
